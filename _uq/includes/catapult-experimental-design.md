\ifndef{catapultExperimentalDesign}
\define{catapultExperimentalDesign}


\include{_uq/includes/catapult-simulation.md}

\editme

\subsection{Experimental Design for the Catapult}
\slides{* First build an experimental design loop.
* Start with model free design.
    * Random design
	* Latin hypercube sambling
	* Sobol sequences
	* Orthogonal design}
	
\notes{Now we will build an emulator for the catapult using the experimental design loop.}

\notes{We'll start with a small model-free design, we'll use a random design for initializing our model.}

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{design = RandomDesign(space)
x = design.get_samples(5)
y = catapult_distance(x)}

\setupcode{from GPy.models import GPRegression
from emukit.model_wrappers import GPyModelWrapper
from emukit.sensitivity.monte_carlo import MonteCarloSensitivity}

\notes{Set up the GPy model. The variance of the RBF kernel is set to $150^2$ because that's roughly the square of the range of the catapult. We set the noise variance to a small value.}

\code{model_gpy = GPRegression(x,y)
model_gpy.kern.variance = 150**2
model_gpy.likelihood.variance.fix(1e-5)
display(model_gpy)}

\notes{Wrap the model for EmuKit.}

\code{model_emukit = GPyModelWrapper(model_gpy)
model_emukit.optimize()}

\code{display(model_gpy)}

\newslide{Model Based Design}
\slides{* Use integrated variance reduction.
* Try afterwards with uncertainty sampling.}

\notes{Now we set up the model loop. We'll use integrated variance reduction as the acquisition function for our model-based design loop.}

\notes{*Warning*: This loop runs much slower on Google `colab` than on a local machine.}

\setupcode{from emukit.experimental_design.experimental_design_loop import ExperimentalDesignLoop}

\setupcode{from emukit.experimental_design.acquisitions import IntegratedVarianceReduction, ModelVariance}

\code{integrated_variance = IntegratedVarianceReduction(space=space,
                                                  model=model_emukit)
ed = ExperimentalDesignLoop(space=space, 
                            model=model_emukit, 
                            acquisition = integrated_variance)
ed.run_loop(catapult_distance, 10)}

\writeAssignment{The experiment above was a little slow because we used the integrated variance reduction instead of uncertainty sampling. Try repeating the experiment using uncertainty sampling (make sure not to overwrite your existing model!). What happens? Why does this happen and would you expect it to lead to a better or worse result?}{}{10}


\endif

