\notes{In some scenarios we have simulators of the same environment that have different fidelities, that is that reflect with different level of accuracy the dynamics of the real world. Running simulations of the different fidelities also have a different cost: hight fidelity simulations are more expensive the cheaper ones. If we have access to these simulators we can combine high and low fidelity simulations under the same model.

So let's assume that we have two simulators of the mountain car dynamics, one of high fidelity (the one we have used) and another one of low fidelity. The traditional approach to this form of multi-fidelity emulation is to assume that}

$$\mappingFunction_i\left(\inputVector\right) = \rho\mappingFunction_{i-1}\left(\inputVector\right) + \delta_i\left(\inputVector \right)$$

\notes{where $\mappingFunction_{i-1}\left(\inputVector\right)$ is a low fidelity simulation of the problem of interest and $\mappingFunction_i\left(\inputVector\right)$ is a higher fidelity simulation. The function $\delta_i\left(\inputVector \right)$ represents the difference between the lower and higher fidelity simulation, which is considered additive. The additive form of this covariance means that if $\mappingFunction_{0}\left(\inputVector\right)$ and $\left\{\delta_i\left(\inputVector \right)\right\}_{i=1}^m$ are all Gaussian processes, then the process over all fidelities of simuation will be a joint Gaussian process.

But with Deep Gaussian processes we can consider the form }

\newslide{Multi-Fidelity Emulation}

$$\mappingFunction_i\left(\inputVector\right) = \mappingFunctionTwo_{i}\left(\mappingFunction_{i-1}\left(\inputVector\right)\right) + \delta_i\left(\inputVector \right),$$

\notes{where the low fidelity representation is non linearly transformed by $\mappingFunctionTwo(\cdot)$ before use in the process. This is the approach taken in @Perdikaris:multifidelity17. But once we accept that these models can be composed, a highly flexible framework can emerge. A key point is that the data enters the model at different levels, and represents different aspects. For example these correspond to the two fidelities of the mountain car simulator.

We start by sampling both of them at 250 random input locations.}

\setupcode{import gym}
\code{env = gym.make('MountainCarContinuous-v0')}

\setupcode{import GPyOpt}
\code{### --- Collect points from low and high fidelity simulator --- ###

space = GPyOpt.Design_space([
        {'name':'position', 'type':'continuous', 'domain':(-1.2, +1)},
        {'name':'velocity', 'type':'continuous', 'domain':(-0.07, +0.07)},
        {'name':'action', 'type':'continuous', 'domain':(-1, +1)}])

n_points = 250
random_design = GPyOpt.experiment_design.RandomDesign(space)
x_random = random_design.get_samples(n_points)}

\notes{Next, we evaluate the high and low fidelity simualtors at those locations.}

\setupcode{import numpy as np
import mountain_car as mc}

\code{d_position_hf = np.zeros((n_points, 1))
d_velocity_hf = np.zeros((n_points, 1))
d_position_lf = np.zeros((n_points, 1))
d_velocity_lf = np.zeros((n_points, 1))

# --- Collect high fidelity points
for i in range(0, n_points):
    d_position_hf[i], d_velocity_hf[i] = mc.simulation(x_random[i, :])

# --- Collect low fidelity points  
for i in range(0, n_points):
    d_position_lf[i], d_velocity_lf[i] = mc.low_cost_simulation(x_random[i, :])}
	
\notes{It is time to build the multi-fidelity model for both the position and the velocity.

As we did in the previous section we use the emulator to optimize the simulator. In this case we use the high fidelity output of the emulator.}

\code{### --- Optimize controller parameters 
obj_func = lambda x: mc.run_simulation(env, x)[0]
obj_func_emulator = lambda x: mc.run_emulation([position_model, velocity_model], x, car_initial_location)[0]
objective_multifidelity = GPyOpt.core.task.SingleObjective(obj_func)}

\notes{And we optimize using Bayesian optimzation.}

\setupcode{from GPyOpt.experiment_design.random_design import RandomDesign}

\code{model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)
space= [{'name':'linear_1', 'type':'continuous', 'domain':(-1/1.2, +1)},
        {'name':'linear_2', 'type':'continuous', 'domain':(-1/0.07, +1/0.07)},
        {'name':'constant', 'type':'continuous', 'domain':(-1, +1)}]

design_space = GPyOpt.Design_space(space=space)
aquisition_optimizer = GPyOpt.optimization.AcquisitionOptimizer(design_space)

n_initial_points = 25
random_design = RandomDesign(design_space)
initial_design = random_design.get_samples(n_initial_points)
acquisition = GPyOpt.acquisitions.AcquisitionEI(model, design_space, optimizer=aquisition_optimizer)
evaluator = GPyOpt.core.evaluators.Sequential(acquisition)}

\code{bo_multifidelity = GPyOpt.methods.ModularBayesianOptimization(model, design_space, objective_multifidelity, acquisition, evaluator, initial_design)
bo_multifidelity.run_optimization(max_iter=50)}

\code{_, _, _, frames = mc.run_simulation(env, np.atleast_2d(bo_multifidelity.x_opt), render=True)
anim=mc.animate_frames(frames, 'Best controller with multi-fidelity emulator')}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
                  diagrams='../slides/diagrams/uq', 
				  filename='mountain_car_multi_fidelity.html')}

\newgslide{Best Controller with Multi-Fidelity Emulator}

\includehtml{../slides/diagrams/uq/mountain_car_multi_fidelity.html}{1024}{768}

\slides{250 observations of high fidelity simulator and 250 of the low fidelity simulator}
\notes{And problem solved! We see how the problem is also solved with 250 observations of the high fidelity simulator and 250 of the low fidelity simulator.}
