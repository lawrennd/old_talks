\ifndef{mountainCarMultiFidelitySolution}
\define{mountainCarMultiFidelitySolution}


\editme

\subsection{Building the Multifidelity Emulation}

\notes{It is time to build the multi-fidelity model for both the position and the velocity.}

\notes{As we did in the previous section we use the emulator to optimize the simulator. In this case we use the high fidelity output of the emulator.}

\notes{First we optimize the controller parameters}

\helpercode{def target_function(X):
	"""Run the Mountain Car simulaton for each set of controller parameters in the matrix."""
    simulation_function = lambda x: mc.run_simulation(env, x)[0]
    return np.asarray([simulation_function(np.atleast_2d(x)) for x in X])[:, np.newaxis]}

\helpercode{def target_function_emulator(X):
	"""Run the Mountain Car simulation for each set of controller parameters in the matrix using the emulation."""
    emulation_function = lambda x: mc.run_emulation([position_model_emukit, velocity_model_emukit], x, car_initial_location)[0]
    return np.asarray([emulation_function(np.atleast_2d(x)) for x in X])[:, np.newaxis]}

<!--code{obj_func = lambda x: mc.run_simulation(env, x)[0]
obj_func_emulator = lambda x: mc.run_emulation([position_model, velocity_model], x, car_initial_location)[0]
objective_multifidelity = GPyOpt.core.task.SingleObjective(obj_func)}-->

\notes{And we optimize using Bayesian optimzation.}

\setupcode{from emukit.core import ContinuousParameter, ParameterSpace}

\code{position_domain = [-1.2, +1]
velocity_domain = [-1/0.07, +1/0.07]
constant_domain = [-1, +1]

space = ParameterSpace(
          [ContinuousParameter('position_parameter', *position_domain), 
           ContinuousParameter('velocity_parameter', *velocity_domain),
           ContinuousParameter('constant', *constant_domain)])}

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{design = RandomDesign(space)
n_initial_points = 25
initial_design = design.get_samples(n_initial_points)}

n_initial_points = 25
random_design = RandomDesign(design_space)
initial_design = random_design.get_samples(n_initial_points)
acquisition = GPyOpt.acquisitions.AcquisitionEI(model, design_space, optimizer=aquisition_optimizer)
evaluator = GPyOpt.core.evaluators.Sequential(acquisition)}

\code{bo_multifidelity = GPyOpt.methods.ModularBayesianOptimization(model, design_space, objective_multifidelity, acquisition, evaluator, initial_design)
bo_multifidelity.run_optimization(max_iter=50)}

\code{_, _, _, frames = mc.run_simulation(env, np.atleast_2d(bo_multifidelity.x_opt), render=True)
anim=mc.animate_frames(frames, 'Best controller with multi-fidelity emulator')}

\setupdisplaycode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
                  diagrams='\writeDiagramsDir/uq', 
				  filename='mountain_car_multi_fidelity.html')}

\subsubsection{Best Controller with Multi-Fidelity Emulator}

\figure{\includehtml{\diagramsDir/uq/mountain_car_multi_fidelity.html}{800px}{600px}}{Mountain car learnt with multi-fidelity model. Here 250 observations of the high fidelity simulator and 250 observations of the low fidelity simulator are used to learn the controller.}{mountain-car-multi-fidelity}

\slides{250 observations of high fidelity simulator and 250 of the low fidelity simulator}
\notes{And problem solved! We see how the problem is also solved with 250 observations of the high fidelity simulator and 250 of the low fidelity simulator.}

\endif
