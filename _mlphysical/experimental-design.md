---
week: 4
title: "Emulation and Experimental Design"
abstract:  >
  This lecture will review the ideas behind using surrogate models for experimental design.
layout: lecture
time: "10:00"
date: 2020-10-29
venue: Virtual (Zoom)
ipynb: true
reveal: true
transition: None
---

\include{talk-macros.tex}

\section{Emulation}

\include{_supply-chain/includes/experiment-analyze-design.md}
\include{_uq/includes/emulation.md}

\include{_gp/includes/gpy-software.md}
\include{_gp/includes/gpy-emulation.md}

$$\newcommand{\dataStd}{\sigma_{\text{noise}}}$$

\include{_uq/includes/emukit-playground.md}

\installcode{pyDOE}
\installcode{EmuKit}

\notes{This introduction is based on [An Introduction to Experimental Design with Emukit](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-experimental-design-introduction.ipynb) written by Andrei Paleyes and Maren Mahsereci.}

\include{_uq/includes/alex-forrester.md}

Experimental design.

Latin hypercube

Linear example

\setupcode{import numpy as np

from emukit.test_functions import forrester_function
from emukit.core.loop.user_function import UserFunctionWrapper
from emukit.core import ContinuousParameter, ParameterSpace}


\code{target_function, space = forrester_function()}

\code{x_plot = np.linspace(space.parameters[0].min, space.parameters[0].max, 301)[:, None]
y_plot = target_function(x_plot)}

\setupplot{import matplotlib.pyplot as plt}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_plot, y_plot, 'k', label='target Function')

ax.legend(loc=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function}{80%}}{The Forrester function [@Forrester-engineering08].}{forrester-function}

\subsection{Initial Design}

\notes{Usually, before we start the actual ExpDesign loop we need to gather a few observations such that we can fit the model. This is called the initial design and common strategies are either a predefined grid or sampling points uniformly at random.}

\code{X_init = np.array([[0.2],[0.6], [0.9]])
Y_init = target_function(X_init)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X_init, Y_init, 'ro', markersize=10, label='Observations')
ax.plot(x_plot, y_plot, 'k', label='Target Function')

ax.legend(loc=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function-initial-design.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function-initial-design}{80%}}{The initial design for the Forrester function example.}{forrester-function-initial-design}

\subsection{The Model}

\notes{Now we can start with the ExpDesign loop by first fitting a model on the collected data. 
A popular model for ExpDesign is a Gaussian process (GP) which defines a probability distribution across classes of functions, typically smooth, such that each linear finite-dimensional restriction is multivariate Gaussian [@Rasmussen:book06]. Gaussian processes are fully parametrized by a mean $\mu(\inputVector)$ and a covariance function $\kernelScalar(\inputVector,\inputVector^\prime)$.  Without loss of generality $\mu(\inputVector)$ is assumed to be zero. The covariance function $\kernelScalar(\inputVector,\inputVector^\prime)$ characterizes the smoothness and other properties of $\mappingFunction$. It is known that the kernel of the process has to be continuous, symmetric and positive definite. A widely used kernel is the exponentiated quadratic or RBF kernel: 
$$ 
\kernelScalar(\inputVector,\inputVector^\prime) = \alpha \exp{ \left(-\frac{\|\inputVector-\inputVector^\prime\|^2}{2 \ell}\right)} 
$$ 
where $\alpha$ and $\ell$ are hyperparameters.

To denote that $\mappingFunction$ is a sample from a GP with mean $\mu$ and covariance $k$ we write
$$
\mappingFunction \sim \mathcal{GP}(\mu,k).
$$ 

For regression tasks, the most important feature of GPs is that process priors are conjugate to the likelihood from finitely many observations $\dataMatrix = (y_1,\dots,y_\numData)^\top$ and $\inputMatrix =\{\inputVector_1,\dots,\inputVector_\numData\}$, $\inputVector_i\in \mathcal{X}$ of the form $\dataScalar_i = \mappingFunction(\inputVector_i) + \noiseScalar_i$ where $\noiseScalar_i \sim \gaussianSamp{0}{\dataStd^2}$ and we typically estimate $\dataStd^2$ by maximum likelihood alongside $\alpha$ and $\ell$.

We obtain the Gaussian posterior 
$$
\mappingFunction(\inputVector^*)|\inputMatrix, \dataMatrix, \theta \sim \gaussianSamp{\mu(\inputVector^*)}{\sigma^2(\inputVector^*)},
$$
where $\mu(\inputVector^*)$ and $\sigma^2(\inputVector^*)$ have a closed form solution as we've seen in the earlier lectures (see also @Rasmussen:book06).}

\notes{Note that Gaussian processes are also characterized by hyperparameters, for example in the exponatiated quadratic case we have $\paramVector = \left\{ \alpha, \ell, \dataStd^2 \right\}$ for the scale of the covariance, the lengthscale and the noise variance. Here, for simplicitly we will keep these hyperparameters fixed. However, we will usually either optimize or sample these hyperparameters using the marginal loglikelihood of the GP. 

In this module we've focussed on Gaussian processes, but we could also use any other model that returns a mean $\mu(\inputVector)$ and variance $\sigma^2(\inputVector)$ on an arbitrary input points $\inputVector$ such as Bayesian neural networks or random forests. In Emukit these different models can be used by defining a new `ModelWrapper`.}

\setupcode{import GPy
from emukit.model_wrappers.gpy_model_wrappers import GPyModelWrapper}

\code{kern = GPy.kern.RBF(1, lengthscale=0.08, variance=20)
gpy_model = GPy.models.GPRegression(X_init, Y_init, kern, noise_var=1e-10)
emukit_model = GPyModelWrapper(gpy_model)

mu_plot, var_plot = emukit_model.predict(x_plot)}

\setupplotcode{import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
from matplotlib import cm

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X_init, Y_init, 'ro', markersize=10, label='Observations')
ax.plot(x_plot, y_plot, 'k', label='Objective Function')
ax.plot(x_plot, mu_plot, 'C0', label='Model')
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - np.sqrt(var_plot)[:, 0], color='C0', alpha=0.6)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 2 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 2 * np.sqrt(var_plot)[:, 0], color='C0', alpha=0.4)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 3 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 3 * np.sqrt(var_plot)[:, 0], color='C0', alpha=0.2)
ax.legend(loc=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function-entropy.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function-entropy}{80%}}{The emulator fitted to the Forrester function with only three observations. The error bars show 1, 2 and 3 standard deviations.}{forrester-function-entropy}

\subsection{The Acquisition Function}

\notes{In the second step of our ExpDesign loop we use our model to compute the acquisition function. We'll review two different forms of acquisition funciton for doing this.}

\subsubsection{Uncertainty Sampling}

\notes{In uncertainty sampling (US) we hoose the next value $\inputVector_{n+1}$ at the location where the model on $\mappingFunction(\inputVector)$ has the highest marginal predictive variance}
$$
a_{US}(\inputVector) = \sigma^2(\inputVector).
$$ 
\notes{This makes sure, that we learn the function $\mappingFunction(\cdot)$ everywhere on $\mathbb{X}$ to a similar level of absolute error.}

\subsubsection{Integrated Variance Reduction}

\notes{In the integrated variance reduction (IVR) you choose the next value $\inputVector_{n+1}$ such that the total variance of the model is reduced maximally [@Sacks-design89],}
$$
a_{IVR} = \int_{\mathbb{X}}[\sigma^2(\inputVector') - \sigma^2(\inputVector'; \inputVector)]\text{d}\inputVector'\approx 
\frac{1}{\# \text{samples}}\sum_i^{\# \text{samples}}[\sigma^2(\inputVector_i) - \sigma^2(\inputVector_i; \inputVector)].
$$
\notes{Here $\sigma^2(\inputVector'; \inputVector)$ is the predictive variance at $\inputVector'$ had $\inputVector$ been observed. Thus IVR computes the overall reduction in variance (for all points in $\mathbb{X}$) had $f$ been observed at $\inputVector$.

The finite sum approximation on the right hand side of the equation is usually used because the integral over $\inputVector'$ is not analytic. In that case $\inputVector_i$ are sampled randomly. For a GP model the right hand side simplifies to}
$$
a_{LCB} \approx \frac{1}{\# \text{samples}}\sum_i^{\# \text{samples}}\frac{\kernelScalar^2(\inputVector_i, \inputVector)}{\sigma^2(\inputVector)}.
$$

\notes{IVR is arguably the more principled approach, but often US is preferred over IVR simply because it lends itself to gradient based optimization more easily, is cheaper to compute, and is exact. 

For both of them (stochastic) gradient base optimizers are used to retrieve $\inputVector_{n+1} \in \operatorname*{arg\:max}_{\inputVector \in \mathbb{X}} a(\inputVector)$.}

\setupcode{from emukit.experimental_design.acquisitions import IntegratedVarianceReduction, ModelVariance}

\code{us_acquisition = ModelVariance(emukit_model)
ivr_acquisition = IntegratedVarianceReduction(emukit_model, space)

us_plot = us_acquisition.evaluate(x_plot)
ivr_plot = ivr_acquisition.evaluate(x_plot)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_plot, us_plot / np.max(us_plot), 'green', label='US')
ax.plot(x_plot, ivr_plot / np.max(ivr_plot) , 'purple', label='IVR')

ax.legend(loc=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(-0.01, 1)

mlai.write_figure('experimental-design-acquisition-functions-forrester.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/experimental-design-acquisition-functions-forrester}{80%}}{The *uncertainty sampling* and *integrated variance reduction* acquisition functions for the Forrester example.}{experimental-design-acquisition-functions}

\subsection{ Evaluating the objective function}

\notes{To find the next point to evaluate we optimize the acquisition function using a standard gradient descent optimizer.}

\setupcode{from emukit.core.optimization import GradientAcquisitionOptimizer}

\code{optimizer = GradientAcquisitionOptimizer(space)
x_new, _ = optimizer.optimize(us_acquisition)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_plot, us_plot / np.max(us_plot), 'green', label='US')
ax.axvline(x_new, color='red', label='x_next', linestyle='--')
ax.legend(loc=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(-0.01, 1)

mlai.write_figure('experimental-design-acquisition-next-point-forrester.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/experimental-design-acquisition-next-point-forrester}{80%}}{The maxima of the acquisition function is found and this point is selected for inclusion.}{experimental-design-acquisition-functions}

\notes{Afterwards we evaluate the true objective function and append it to our initial observations.}

\code{y_new = target_function(x_new)}

\code{X = np.append(X_init, x_new, axis=0)
Y = np.append(Y_init, y_new, axis=0)}

\notes{After updating the model, you can see that the uncertainty about the true objective function in this region decreases and our model becomes more certain.}

\code{emukit_model.set_data(X, Y)
mu_plot, var_plot = emukit_model.predict(x_plot)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(emukit_model.X, emukit_model.Y, 'ro', markersize=10, label='Observations')
ax.plot(x_plot, y_plot, 'k', label='Target Function')
ax.plot(x_plot, mu_plot, 'C0', label='Model')
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - np.sqrt(var_plot)[:, 0], color='C0', alpha=0.6)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 2 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 2 * np.sqrt(var_plot)[:, 0], color='C0', alpha=0.4)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 3 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 3 * np.sqrt(var_plot)[:, 0], color='C0', alpha=0.2)
ax.legend(loc=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(-0.01, 1)

mlai.write_figure(filename='forrester-function-multi-errorbars.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function-multi-errorbars}{80%}}{The target Forrester function plotted alongside the emulation model and error bars from the emulation at 1, 2 and 3 standard deviations.}{forrester-function-multi-errorbars}

Entropy of posterior

\subsection{Emukit's experimental design interface}

\notes{Of course in practice we don't want to implement all of these steps our self. Emukit provides a convenient and flexible interface to apply experimental design. Below we can see how to run experimental design on the exact same function for 10 iterations.}

\setupcode{from emukit.experimental_design.experimental_design_loop import ExperimentalDesignLoop}

\code{ed = ExperimentalDesignLoop(space=space, model=emukit_model)

ed.run_loop(target_function, 10)}

\code{mu_plot, var_plot = ed.model.predict(x_plot)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(ed.loop_state.X, ed.loop_state.Y, 'ro', markersize=10, label='Observations')
ax.plot(x_plot, y_plot, 'k', label='Objective Function')
ax.plot(x_plot, mu_plot, 'C0', label='Model')
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - np.sqrt(var_plot)[:, 0], 
				 color='C0', alpha=0.6)

ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 2 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 2 * np.sqrt(var_plot)[:, 0], 
				 color='C0', alpha=0.4)

ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 3 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 3 * np.sqrt(var_plot)[:, 0], 
				 color='C0', alpha=0.2)
ax.legend(loc=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function-full-fit.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function-full-fit}{80%}}{The fit of the model to the Forrester function.}{forrester-function-full-fit}


\thanks

\reading

\references

