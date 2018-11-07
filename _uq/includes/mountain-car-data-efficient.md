\subsection{Data Efficient Emulation}

\slides{
* For standard Bayesian Optimization ignored *dynamics* of the car.

* For more data efficiency, first *emulate* the dynamics.

* Then do Bayesian optimization of the *emulator*.}

\notes{In the previous section we solved the mountain car problem by directly emulating the reward but no considerations about the dynamics $\inputVector_{t+1} = \mappingFunction(\inputVector_{t},\textbf{u}_{t})$ of the system were made. Note that we had to run 75 episodes of 500 steps each to solve the problem, which required to call the simulator $500\times 75 =37500$ times. In this section we will show how it is possible to reduce this number by building an emulator for $f$ that can later be used to directly optimize the control.

The inputs of the model for the dynamics are the velocity, the position and the value of the control so create this space accordingly.}

\setupcode{import gym}
\code{env = gym.make('MountainCarContinuous-v0')}

\setupcode{import GPyOpt}
\code{space_dynamics = [{'name':'position', 'type':'continuous', 'domain':[-1.2, +0.6]},
                  {'name':'velocity', 'type':'continuous', 'domain':[-0.07, +0.07]},
                  {'name':'action', 'type':'continuous', 'domain':[-1, +1]}]
design_space_dynamics = GPyOpt.Design_space(space=space_dynamics)}

\notes{The outputs are the velocity and the position. Indeed our model will capture the change in position and velocity on time. That is, we will model}

\slides{* Use a Gaussian process to model}
$$\Delta v_{t+1} = v_{t+1} - v_{t}$$
\slides{and}
$$\Delta x_{t+1} = p_{t+1} - p_{t}$$

\slides{* Two processes, one with mean $v_{t}$ one with mean $p_{t}$}

\notes{with Gaussian processes with prior mean $v_{t}$ and $p_{t}$ respectively. As a covariance function, we use a Matern52.  We need therefore two models to capture the full dynamics of the system.}

\code{position_model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)
velocity_model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)}

\notes{Next, we sample some input parameters and use the simulator to compute the outputs. Note that in this case we are not running the full episodes, we are just using the simulator to compute $\inputVector_{t+1}$ given $\inputVector_{t}$ and $\textbf{u}_{t}$.}

\setupcode{import numpy as np
from GPyOpt.experiment_design.random_design import RandomDesign
import mountain_car as mc}

\code{### --- Random locations of the inputs
n_initial_points = 500
random_design_dynamics = RandomDesign(design_space_dynamics)
initial_design_dynamics = random_design_dynamics.get_samples(n_initial_points)}

\code{### --- Simulation of the (normalized) outputs
y = np.zeros((initial_design_dynamics.shape[0], 2))
for i in range(initial_design_dynamics.shape[0]):
    y[i, :] = mc.simulation(initial_design_dynamics[i, :])

# Normalize the data from the simulation
y_normalisation = np.std(y, axis=0)
y_normalised = y/y_normalisation}

\newslide{Emulator Training}
\slides{
* Used 500 randomly selected points to train emulators.

* Can make proces smore efficient through *experimental design*.
}

\notes{In general we might use much smarter strategies to design our emulation of the simulator. For example, we could use the variance of the predictive distributions of the models to collect points using uncertainty sampling, which will give us a better coverage of the space. For simplicity, we move ahead with the 500 randomly selected points. 

Now that we have a data set, we can update the emulators for the location and the velocity.}

\code{position_model.updateModel(initial_design_dynamics, y[:, [0]], None, None)
velocity_model.updateModel(initial_design_dynamics, y[:, [1]], None, None)}

\notes{We can now have a look to how the emulator and the simulator match. First, we show a contour plot of the car aceleration for each pair of can position and velocity. You can use the bar bellow to play with the values of the controler to compare the emulator and the simulator.}

\setupcode{from IPython.html.widgets import interact}

\plotcode{control = mc.plot_control(velocity_model)
interact(control.plot_slices, control=(-1, 1, 0.05))}


\notes{We can see how the emulator is doing a fairly good job approximating the simulator. On the edges, however, it struggles to captures the dynamics of the simulator. 

Given some input parameters of the linear controlling, how do the dynamics of the emulator and simulator match? In the following figure we show the position and velocity of the car for the 500 time steps of an episode in which the parameters of the linear controller have been fixed beforehand. The value of the input control is also shown.}

\code{controller_gains = np.atleast_2d([0, .6, 1])  # change the valus of the linear controller to observe the trayectories.}

\plotcode{mc.emu_sim_comparison(env, controller_gains, [position_model, velocity_model], 
                      max_steps=500, diagrams='../slides/diagrams/uq')}

\newslide{Comparison of Emulation and Simulation}

\includesvg{../slides/diagrams/uq/emu_sim_comparison.svg}

\notes{We now make explicit use of the emulator, using it to replace the simulator and optimize the linear controller. Note that in this optimization, we don't need to query the simulator anymore as we can reproduce the full dynamics of an episode using the emulator. For illustrative purposes, in this example we fix the initial location of the car. 

We define the objective reward function in terms of the simulator.}

\code{### --- Optimize control parameters with emulator
car_initial_location = np.asarray([-0.58912799, 0]) 

### --- Reward objective function using the emulator
obj_func_emulator = lambda x: mc.run_emulation([position_model, velocity_model], x, car_initial_location)[0]
objective_emulator = GPyOpt.core.task.SingleObjective(obj_func_emulator)}

\notes{And as before, we use Bayesian optimization to find the best possible linear controller.}

\code{### --- Elements of the optimization that will use the multi-fidelity emulator
model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)}

\notes{The design space is the three continuous variables that make up the linear controller.}

\code{space= [{'name':'linear_1', 'type':'continuous', 'domain':(-1/1.2, +1)},
        {'name':'linear_2', 'type':'continuous', 'domain':(-1/0.07, +1/0.07)},
        {'name':'constant', 'type':'continuous', 'domain':(-1, +1)}]

design_space         = GPyOpt.Design_space(space=space)
aquisition_optimizer = GPyOpt.optimization.AcquisitionOptimizer(design_space)

random_design = RandomDesign(design_space)
initial_design = random_design.get_samples(25)}

\notes{We set the acquisition function to be expected improvement using ```GPyOpt```.}

\code{acquisition          = GPyOpt.acquisitions.AcquisitionEI(model, design_space, optimizer=aquisition_optimizer)
evaluator            = GPyOpt.core.evaluators.Sequential(acquisition)}

\code{bo_emulator = GPyOpt.methods.ModularBayesianOptimization(model, design_space, objective_emulator, acquisition, evaluator, initial_design)
bo_emulator.run_optimization(max_iter=50)}

\code{_, _, _, frames = mc.run_simulation(env, np.atleast_2d(bo_emulator.x_opt), render=True)
anim=mc.animate_frames(frames, 'Best controller using the emulator of the dynamics')}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
                  diagrams='../slides/diagrams/uq', 
				  filename='mountain_car_emulated.html')}

\newslide{Data Efficiency}

\slides{
* Our emulator used only 500 calls to the simulator.

* Optimizing the simulator directly required 37,500 calls to the simulator.
}

\newslide{Best Controller using Emulator of Dynamics}

\includehtml{../slides/diagrams/uq/mountain_car_emulated.html}{1024}{768}

\slides{500 calls to the simulator vs 37,500 calls to the simulator}

\notes{And the problem is again solved, but in this case we have replaced the simulator of the car dynamics by a Gaussian process emulator that we learned by calling the simulator only 500 times. Compared to the 37500 calls that we needed when applying Bayesian optimization directly on the simulator this is a great gain.}
