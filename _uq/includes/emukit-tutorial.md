\ifndef{emukitTutorial}
\define{emukitTutorial}

\editme

\subsection{Emukit Tutorial}

\installcode{GPy}
\installcode{EmuKit}
\installcode{mlai}

\notes{Set up the python imports that Emukit will use.}

\setupcode{import numpy as np
import GPy}


\notes{Now set up Emukit to run.}

\setupcode{from emukit.experimental_design.experimental_design_loop import ExperimentalDesignLoop}

\notes{Let's check the help function for the experimental design loop. This is the outer loop that provides all the decision making parts of Emukit.}

\code{ExperimentalDesignLoop?}

\notes{Now let's load in the model wrapper for our probabilistic model. In this case, instead of using GPy, we'll make use of a simple model wrapper Emukit provides for a basic form of Gaussian process.}

\setupcode{from emukit.model_wrappers import SimpleGaussianProcessModel}

\notes{Let's have a quick look at how the included GP model works.}

\code{SimpleGaussianProcessModel?}

\notes{Now let's create the data.}

\code{x_min = -30.0
x_max = 30.0

x = np.random.uniform(x_min, x_max, (10, 1))
y = np.sin(x) + np.random.randn(10, 1) * 0.05}

\notes{To learn about how to include your own model in Emukit, check [this notebook](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-custom-model.ipynb) which shows how to include a `sklearn` GP model.}

\code{emukit_model = SimpleGaussianProcessModel(x, y)}

\setupcode{from emukit.core import ParameterSpace, ContinuousParameter
from emukit.core.loop import UserFunctionWrapper}

\code{p = ContinuousParameter('c', x_min, x_max)
space = ParameterSpace([p])}

\code{loop = ExperimentalDesignLoop(space, emukit_model)
loop.run_loop(np.sin, 30)}


\code{plot_min = -40.0
plot_max = 40.0

real_x = np.arange(plot_min, plot_max, 0.2)
real_y = np.sin(real_x)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

ax.plot(real_x, real_y, c='r', linewidth=2)
ax.scatter(loop.loop_state.X[:, 0].tolist(), 
           loop.loop_state.Y[:, 0].tolist(), s=50)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$', rotation=None)
ax.set_ylim([-2.5, 2.5])

ax.legend(['true function', 'acquired data points'], loc='lower right')

mlai.write_figure('emukit-sine-function.svg', directory='\writeDiagramsDir/uq')}

\notes{\figure{\includediagram{\diagramsDir/uq/emukit-sine-function}{80%}}{Experimental design in Emukit using the `ExperimentalDesignLoop`: learning function $\sin(x)$ with Emukit.}{emukit-sine-function}}

\notes{Computer the predictions from the Emukit model.}

\code{predicted_y = []
predicted_std = []
for x in real_x:
    y, var = emukit_model.predict(np.array([[x]]))
    std = np.sqrt(var)
    predicted_y.append(y)
    predicted_std.append(std)

predicted_y = np.array(predicted_y).flatten()
predicted_std = np.array(predicted_std).flatten()}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

ax.plot(real_x, predicted_y, linewidth=3)
ax.plot(real_x, real_y, c='r', linewidth=2)

ax.set_ylim([-2.5, 2.5])

ax.fill_between(real_x, predicted_y - 2 * predicted_std, 
                predicted_y + 2 * predicted_std, alpha=.5)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(['true function', 'estimated function'], loc='lower right')

mlai.write_figure('emukit-sine-function-fit.svg', directory='\writeDiagramsDir/uq')}

\notes{\figure{\includediagram{\diagramsDir/uq/emukit-sine-function-fit}{80%}}{The fit to the sine function after runnning the Emukit  `ExperimentalDesignLoop`.}{emukit-sine-function-fit}}

\notes{\codeassignment{Repeat the above experiment but using the Gaussian process model from `sklearn`. You can see step by step instructions on how to do this in [this notebook](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-custom-model.ipynb).}}

\subsection{Emukit Overview Summary}
\slides{
* *Multi-fidelity emulation*: build surrogate models for multiple sources of information;
* *Bayesian optimisation*: optimise physical experiments and tune parameters ML algorithms;
* *Experimental design/Active learning*: design experiments and perform active learning with ML models;
* *Sensitivity analysis*: analyse the influence of inputs on the outputs 
* *Bayesian quadrature*: compute integrals of functions that are expensive to evaluate.
}
\notes{The aim is to provide a suite where different approaches to emulation are assimilated under one roof. The current version of Emukit includes *multi-fidelity emulation* for build surrogate models when data is obtained from multiple information sources that have different fidelity and/or cost; *Bayesian optimisation* for optimising physical experiments and tune parameters of machine learning algorithms or other computational simulations; *experimental design and active learning*: design the most informative experiments and perform active learning with machine learning models; *sensitivity analysis*: analyse the influence of inputs on the outputs of a given system; and *Bayesian quadrature*: efficiently compute the integrals of functions that are expensive to evaluate. But it's easy to extend.}


\endif
