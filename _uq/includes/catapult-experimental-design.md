\ifndef{catapultExperimentalDesign}
\define{catapultExperimentalDesign}


\include{_uq/includes/catapult-simulation.md}

\editme

\subsection{Experimental Design for the Catapult}

\notes{Now we will build an emulator for the catapult using the experimental design loop.}


\setupcode{from emukit.core.initial_designs import RandomDesign}


\setupcode{from emukit.core import ContinuousParameter, ParameterSpace}

\code{variable_domain = (0,1)
           
space = ParameterSpace(
          [ContinuousParameter('rotation_axis', *variable_domain), 
           ContinuousParameter('arm_stop', *variable_domain),
           ContinuousParameter('spring_binding_1', *variable_domain),
           ContinuousParameter('spring_binding_2', *variable_domain)])}

\code{design = RandomDesign(space)
x = design.get_samples(5)
y = catapult_distance(x)[:,np.newaxis]}

\setupcode{from GPy.models import GPRegression
from emukit.model_wrappers import GPyModelWrapper
from emukit.sensitivity.monte_carlo import MonteCarloSensitivity}

\code{model_gpy = GPRegression(x,y)
model_gpy.likelihood.variance.fix(1e-5)
model_emukit = GPyModelWrapper(model_gpy)
model_emukit.optimize(messages=True)}


\setupcode{from emukit.experimental_design.experimental_design_loop import ExperimentalDesignLoop}

\code{ed = ExperimentalDesignLoop(space=space, model=model_emukit)
ed.run_loop(catapult_distance, 10)}

\code{display(model_gpy)}
