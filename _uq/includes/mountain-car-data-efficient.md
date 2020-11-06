\ifndef{mountainCarDataEfficient}
\define{mountainCarDataEfficient}
\editme

\subsection{Data Efficient Emulation}

\slides{
* For standard Bayesian Optimization ignored *dynamics* of the car.
* For more data efficiency, first *emulate* the dynamics.
* Then do Bayesian optimization of the *emulator*.}

\notes{In the previous section we solved the mountain car problem by
directly emulating the reward but no considerations about the dynamics}
$$
\inputVector_{t+1} =\mappingFunctionTwo(\inputVector_{t},\textbf{u}_{t})
$$ 
\notes{of the system were made.}

\notes{We ran the simulator 25 times in the initial design, and 50
times in our Bayesian optimization loop. That required us to call the
dynamics simulation $500\times 75 =37,500$ times, because each
simulation of the car used 500 steps. In this section we will show how
it is possible to reduce this number by building an emulator for $\mappingFunctionTwo(\cdot)$
that can later be used to directly optimize the control.

The inputs of the model for the dynamics are the velocity, the
position and the value of the control so create this space
accordingly.}

\setupcode{import gym}
\code{env = gym.make('MountainCarContinuous-v0')}

\setupcode{from emukit.core import ContinuousParameter, ParameterSpace}

\code{position_dynamics_domain = [-1.2, +0.6]
velocity_dynamics_domain = [-0.07, +0.07]
action_dynamics_domain = [-1, +1]

space_dynamics = ParameterSpace(
          [ContinuousParameter('position_dynamics_parameter', *position_dynamics_domain), 
           ContinuousParameter('velocity_dynamics_parameter', *velocity_dynamics_domain),
           ContinuousParameter('action_dynamics_parameter', *action_dynamics_domain)])}

\notes{Next, we sample some input parameters and use the simulator to compute the outputs. Note that in this case we are not running the full episodes, we are just using the simulator to compute $\inputVector_{t+1}$ given $\inputVector_{t}$ and $\textbf{u}_{t}$.}

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{design_dynamics = RandomDesign(space_dynamics)
n_initial_points = 500
initial_design_dynamics = design_dynamics.get_samples(n_initial_points)}

\setupcode{import numpy as np
import mountain_car as mc}

\code{### --- Simulation of the (normalized) outputs
y_dynamics = np.zeros((initial_design_dynamics.shape[0], 2))
for i in range(initial_design_dynamics.shape[0]):
    y_dynamics[i, :] = mc.simulation(initial_design_dynamics[i, :])}

\code{# Normalize the data from the simulation
y_dynamics_normalisation = np.std(y_dynamics, axis=0)
y_dynamics_normalised = y_dynamics/y_dynamics_normalisation}

\notes{The outputs are the velocity and the position. Our model will capture the change in position and velocity on time. That is, we will model}

\newslide{}

\slides{* Use a Gaussian process to model}
$$
\Delta v_{t+1} = v_{t+1} - v_{t}
$$
\slides{and}
$$
\Delta x_{t+1} = p_{t+1} - p_{t}
$$
\slides{* Two processes, one with mean $v_{t}$ one with mean $p_{t}$}

\notes{with Gaussian processes with prior mean $v_{t}$ and $p_{t}$ respectively. As a covariance function, we use `Matern52`.  We need therefore two models to capture the full dynamics of the system.}

\setupcode{import GPy}

\code{kern_position = GPy.kern.Matern52(3)
position_model_gpy = GPy.models.GPRegression(initial_design_dynamics, y_dynamics[:, 0:1], kern_position, noise_var=1e-10)}

\code{kern_velocity = GPy.kern.Matern52(3)
velocity_model_gpy = GPy.models.GPRegression(initial_design_dynamics, y_dynamics[:, 1:2], kern_velocity, noise_var=1e-10)}

\setupcode{from emukit.model_wrappers.gpy_model_wrappers import GPyModelWrapper}
\code{position_model_emukit = GPyModelWrapper(position_model_gpy, n_restarts=5)
velocity_model_emukit = GPyModelWrapper(velocity_model_gpy, n_restarts=5)}

\newslide{Emulator Training}

\slides{* Used 500 randomly selected points to train emulators.
* Can make proces smore efficient through *experimental design*.}
\notes{In general we might use much smarter strategies to design our
emulation of the simulator. For example, we could use the variance of
the predictive distributions of the models to collect points using
uncertainty sampling, which will give us a better coverage of the
space. For simplicity, we move ahead with the 500 randomly selected
points.}

\notes{Now that we have a data set, we can update the emulators for
the location and the velocity.}

\code{position_model_emukit.optimize()
velocity_model_emukit.optimize()}

\notes{We can now have a look to how the emulator and the simulator
match. First, we show a contour plot of the car aceleration for each
pair of can position and velocity. You can use the bar bellow to play
with the values of the controler to compare the emulator and the
simulator.}

\setupdisplaycode{from IPython.html.widgets import interact}

\displaycode{control = mc.plot_control(velocity_model_emukit)
interact(control.plot_slices, control=(-1, 1, 0.05))}

\notes{We can see how the emulator is doing a fairly good job
approximating the simulator. On the edges, however, it struggles to
captures the dynamics of the simulator.

Given some input parameters of the linear controlling, how do the
dynamics of the emulator and simulator match? In the following figure
we show the position and velocity of the car for the 500 time steps of
an episode in which the parameters of the linear controller have been
fixed beforehand. The value of the input control is also shown.}

\code{# change the values of the linear controller to observe the trajectories.
controller_gains = np.atleast_2d([0, .6, 1])  }

\plotcode{mc.emu_sim_comparison(env, controller_gains, 
                      [position_model_emukit, velocity_model_emukit], 
                      max_steps=500, diagrams='\writeDiagramsDir/uq')}

\newslide{Comparison of Emulation and Simulation}

\figure{\includediagram{\diagramsDir/uq/emu-sim-comparison}{80%}}{Comparison between the mountain car simulator and the emulator.}{emu-sim-comparison}

\notes{We now make explicit use of the emulator, using it to replace
the simulator and optimize the linear controller. Note that in this
optimization, we don't need to query the simulator anymore as we can
reproduce the full dynamics of an episode using the emulator. For
illustrative purposes, in this example we fix the initial location of
the car.}

\notes{We define the objective reward function in terms of the simulator.}

\code{### --- Optimize control parameters with emulator
car_initial_location = np.asarray([-0.58912799, 0])}

\helpercode{def target_function_emulator(X):
	"""Run the Mountain Car simulation for each set of controller parameters in the matrix."""
    emulation_function = lambda x: mc.run_emulation([position_model_emukit, velocity_model_emukit], x, car_initial_location)[0]
    return np.asarray([emulation_function(np.atleast_2d(x)) for x in X])[:, np.newaxis]}

<!--code{### --- Reward objective function using the emulator
target_function_emulator = lambda x: mc.run_emulation([position_model, velocity_model], x, car_initial_location)[0]
objective_emulator = GPyOpt.core.task.SingleObjective(obj_func_emulator)}-->

\notes{And as before, we use Bayesian optimization to find the best possible linear controller.}

<!--\code{### --- Elements of the optimization that will use the multi-fidelity emulator
model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)}-->

\notes{The design space is the three continuous variables that make up the linear controller.}

\code{position_domain = [-1.2, +1]
velocity_domain = [-1/0.07, +1/0.07]
constant_domain = [-1, +1]

space = ParameterSpace(
          [ContinuousParameter('position_parameter', *position_domain), 
           ContinuousParameter('velocity_parameter', *velocity_domain),
           ContinuousParameter('constant', *constant_domain)])}

<!--\code{space= [{'name':'linear_1', 'type':'continuous', 'domain':(-1/1.2, +1)},
        {'name':'linear_2', 'type':'continuous', 'domain':(-1/0.07, +1/0.07)},
        {'name':'constant', 'type':'continuous', 'domain':(-1, +1)}]-->

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{design = RandomDesign(space)
n_initial_points = 25
initial_design = design.get_samples(n_initial_points)}

\notes{Now run the simulation 25 times across our initial design.}

\code{y = target_function_emulator(initial_design)}

\notes{Now we set up the surrogate model for the Bayesian optimization loop.}

\setupcode{import GPy}

\code{kern = GPy.kern.RBF(3)
model_dynamics_emulated_gpy = GPy.models.GPRegression(initial_design, y, kern, noise_var=1e-10)}

\setupcode{from emukit.model_wrappers.gpy_model_wrappers import GPyModelWrapper}

\code{model_dynamics_emulated_emukit = GPyModelWrapper(model_dynamics_emulated_gpy, n_restarts=5)
model_dynamics_emulated_emukit.optimize()}

\notes{We set the acquisition function to be expected improvement.}

\setupcode{from emukit.bayesian_optimization.acquisitions import ExpectedImprovement}

\code{acquisition = ExpectedImprovement(model_emukit)}

\notes{And we set up the main loop for the Bayesian optimization.}

\setupcode{from emukit.bayesian_optimization.loops.bayesian_optimization_loop import BayesianOptimizationLoop}

\code{bo = BayesianOptimizationLoop(space, model_dynamics_emulated_emukit, acquisition=acquisition)
bo.run_loop(target_function_emulator, 50)
results = bo.get_results()}


\code{_, _, _, frames = mc.run_simulation(env, np.atleast_2d(results.minimum_location), render=True)
anim=mc.animate_frames(frames, 'Best controller using the emulator of the dynamics')}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
                  diagrams='\writeDiagramsDir/uq', 
				  filename='mountain-car-emulated.html')}

\newslide{Data Efficiency}
\slides{* Our emulator used only 500 calls to the simulator.
* Optimizing the simulator directly required 37,500 calls to the simulator.}

\newslide{Best Controller using Emulator of Dynamics}

\figure{\includehtml{\diagramsDir/uq/mountain-car-emulated.html}{600}{450}}{Mountain car controller learnt through emulation. Here 500 calls to the simulator are used to fit the controller rather than 37,500 calls to the simulator required in the standard learning.}{mountain-car-emulated}

\notes{And the problem is again solved, but in this case we have replaced the simulator of the car dynamics by a Gaussian process emulator that we learned by calling the dynamics simulator only 500 times. Compared to the 37,500 calls that we needed when applying Bayesian optimization directly on the simulator this is a significant improvement. Of course, in practice the car dynamics are very simple for this example.}

\endif
