\ifndef{emukitSoftware}
\define{emukitSoftware}
\editme

\subsection{Emukit}

\figure{\includepng{\diagramsDir/uq/emukit-software-page}{80%}}{The Emukit software is a set of software tools for emulation and surrogate modeling. <https://emukit.github.io/emukit/>}{emukit-software-page}

\newslide{Emukit}
\slides{
\includepng{\diagramsDir/uq/emukit-software-page2}{80%}
\center{<https://emukit.github.io/emukit/>}
}

\installcode{GPy}
\installcode{EmuKit}

\newslide{Emukit}

\slides{
* Work by Javier Gonzalez, Andrei Paleyes, Mark Pullin, Maren Mahsereci, Alex Gessner, Aaron Klein.
* Available on [Github](https://github.com/EmuKit/emukit)
* Example [sensitivity notebook](https://github.com/EmuKit/emukit/blob/develop/notebooks/Emukit-sensitivity-montecarlo.ipynb).

}

\setupcode{import numpy as np
import GPy

from emukit.model_wrappers import GPyModelWrapper
from emukit.experimental_design.experimental_design_loop import ExperimentalDesignLoop
from emukit.core import ParameterSpace, ContinuousParameter
from emukit.core.loop import UserFunctionWrapper}

\code{x_min = -30.0
x_max = 30.0

x = np.random.uniform(x_min, x_max, (10, 1))
y = np.sin(x) + np.random.randn(10, 1) * 0.05}


\code{gpy_model = GPy.models.GPRegression(x, y)}

\code{emukit_model = GPyModelwrapper(gpy_model)}

\code{p = ContinuousParameter('c', x_min, x_max)
space = ParameterSpace([p])}

\code{loop = ExperimentalDesignLoop(space, emukit_model)
loop.run_loop(np.sn, 30)}


\code{plot_min = -40.0
plot_max = 40.0

real_x = np.arange(plot_min, plot_max, 0.2)
real_y = np.sin(real_x)}

\setupplotcode{import matplotlib.pyplot as plt}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)

ax.plot(real_x, real_y, c='r')
ax.scatter(loo.loo_state.X[:, 0].tolist(), loop.loop_state.Y[:, 0].tolist())

ax.set_title('Learning function $\sin(x)$ with Emukit')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$', rotation=None)

ax.legend(['true function', 'acquired data points'], loc='lower right')

mla.write_figure('emukit-sine-function.svg', directory='\writeDiagramsDir/uq')}


\code{predicted_y = []
predicted_std = []
for x in real_x:
    y, var = emukit_model.predict(np.array([[x]]))
    std = np.sqrt(var)
    predicted_y.append(y)
    predicted_std.append(std)

predicted_y = np.array(predicted_y).flatten()
predicted_std = np.array(predicted_std).flatten()}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)

ax.plot(real_x, real_y, c='r', )
ax.plot(real_x, predicted_y)
ax.fill_between(real_x, predicted_y - 2 * predicted_std, predicted_y + 2 * predicted_std, alpha=.5);

ax.set_title('Learning function $\sin(x)$ with Emukit')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(['true function', 'estimated function'], loc='lower right')


\newslide{Emukit Software}
\slides{
* *Multi-fidelity emulation*: build surrogate models for multiple sources of information;
* *Bayesian optimisation*: optimise physical experiments and tune parameters ML algorithms;
* *Experimental design/Active learning*: design experiments and perform active learning with ML models;
* *Sensitivity analysis*: analyse the influence of inputs on the outputs 
* *Bayesian quadrature*: compute integrals of functions that are expensive to evaluate.
}
\notes{
The aim is to provide a suite where different approaches to emulation are assimilated under one roof. The current version of Emukit includes *multi-fidelity emulation* for build surrogate models when data is obtained from multiple information sources that have different fidelity and/or cost; *Bayesian optimisation* for optimising physical experiments and tune parameters of machine learning algorithms or other computational simulations; *experimental design and active learning*: design the most informative experiments and perform active learning with machine learning models; *sensitivity analysis*: analyse the influence of inputs on the outputs of a given system; and
*Bayesian quadrature*: efficiently compute the integrals of functions that are expensive to evaluate.
}

\endif
