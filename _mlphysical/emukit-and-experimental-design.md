---
week: 4
session: 2
layout: lecture
title: "Emukit and Experimental Design"
abstract: >
  A surrogate model can be explored to understand the sensitivity of the system. This lecture will review how to perform sensitivity analysis.
layout: lecture
time: "12:00"
date: 2020-10-30
venue: Virtual (Zoom)
ipynb: true
reveal: true
transition: None
---

\include{talk-macros.tex}

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

[@Kennedy-predicting00;@Sobol-sensitivity90;@Sobol-global01;@Saltelli-sensitivity04;@Saltelli-global08;@Saltelli-variance10]

This introduction is based on [Introduction to Global Sensitivity Analysis with Emukit](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-sensitivity-montecarlo.ipynb) written by Mark Pullin, Javier Gonzalez, Juan Emmanuel Johnson and Andrei Paleyes.

> A possible definition of sensitivity analysis is the following: The study of
> how uncertainty in the output of a model (numerical or otherwise) can be
> apportioned to different sources of uncertainty in the model input [@Saltelli-sensitivity04]. A related practice is ‘uncertainty analysis’, which focuses
> rather on quantifying uncertainty in model output. Ideally, uncertainty
> and sensitivity analyses should be run in tandem, with uncertainty analysis
> preceding in current practice.
>
> In Chapter 1 of @Saltelli-global08

\setupcode{import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
from matplotlib import cm}

\downloadcode{mlai}
\downloadcode{teaching_plots}
\downloadcode{gp_tutorial}

\installcode{GPy}
\installcode{pyDOE}
\installcode{EmuKit}

\setupcode{import mlai
import teaching_plots as plot}


\notes{Sensitivity analysis is a statistical technique widely used to test the reliability of real systems. Imagine a simulator of taxis picking up customers in a city like the one showed in the [Emukit playground](https://github.com/amzn/emukit-playground). The profit of the taxi company depends on factors like the number of taxis on the road and the price per trip. In this example, a global sensitivity analysis of the simulator could be useful to decompose the variance of the profit in a way that can be assigned to the input variables of the simulator.}

\notes{There are different ways of doing a sensitivity analysis of the variables of a simulator. In this notebook we will start with an approach based on Monte Carlo sampling that is useful when evaluating the simulator is cheap. If evaluating the simulator is expensive, emulators can then be used to speed up computations. We will show this in the last part of the notebook. Next, we start with a few formal definitions and literature review so we can understand the basics of Sensitivity Analysis and how it can performed with Emukit.}

\notes{Any simulator can be viewed as a function 
$$
\dataScalar=\mappingFunction(\inputVector),
$$ 
where $\inputVector$ is a vector of $\dataDim$ uncertain model inputs $\inputScalar_1,\dots,\inputScalar_\dataDim$, and $\dataScalar$ is some univariate model output. We assume that $f$ is a square integrable function and that the inputs are statistically independent and uniformly distributed within the hypercube $\inputScalar_i \in [0,1]$ for $i=1,2,\dots,\dataDim$, although the bounds can be generalized. The Sobol decomposition of $\mappingFunction(\cdot)$ allows us to write it as 
$$
\dataScalar = \mappingFunction_0 + \sum_{i=1}^\dataDim \mappingFunction_i(\inputScalar_i) + \sum_{i<j}^{\dataDim} \mappingFunction_{ij}(\inputScalar_i,\inputScalar_j) + \cdots + \mappingFunction_{1,2,\dots,\dataDim}(\inputScalar_1,\inputScalar_2,\dots,\inputScalar_\dataDim),
$$
where $\mappingFunction_0$ is a constant term, $\mappingFunction_i$ is a function of $\inputScalar_i$, $\mappingFunction_{ij}$ a function of $\inputScalar_i$ and $\inputScalar_j$, etc. A condition of this decomposition is that,
$$ 
\int_0^1 \mappingFunction_{i_1 i_2 \dots i_\dataDim}(\inputScalar_{i_1},\inputScalar_{i_2},\dots,\inputScalar_{i_\dataDim}) \text{d}\inputScalar_{k}=0, \text{ for } k = i_1,...,i_\dataDim. 
$$
This means that all the terms in the decomposition are orthogonal, which can be written in terms of conditional expected values as
$$\begin{align*}
\mappingFunction_0 &= E(\dataScalar) \\
\mappingFunction_i(\inputScalar_i) & = E(\dataScalar|\inputScalar_i) - \mappingFunction_0 \\
\mappingFunction_{ij}(\inputScalar_i,\inputScalar_j) & = E(\dataScalar|\inputScalar_i,\inputScalar_j) - \mappingFunction_0 - \mappingFunction_i - \mappingFunction_j 
\end{align*}$$
with all the expectations computed over $\dataScalar$.}

\notes{Each component $\mappingFunction_i$ (main effects) can be seen as the effect on $\dataScalar$ of varying $\inputScalar_i$ alone. The same interpretation follows for $\mappingFunction_{ij}$ which accounts for the (extra) variation of changing $\inputScalar_i$ and $\inputScalar_j$ simultaneously (second-order interaction). Higher-order terms have analogous definitions.

The key step to decompose the variation of $\dataScalar$ is to notice that
$$
\text{var}(\dataScalar) = E(\dataScalar^2) - E(\dataScalar)^2 = \int_0^1 \mappingFunction^2(\inputVector) \text{d}\inputVector - \mappingFunction_0^2
$$
and that this variance can be decomposed as
$$ 
\text{var}(\dataScalar) = \int_0^1 \sum_{i=1}^\dataDim \mappingFunction_i(\inputScalar_i) \text{d}\inputScalar_i + \int_0^1 \sum_{i<j}^{\dataDim} \mappingFunction_{ij}(\inputScalar_i,\inputScalar_j)\text{d} \inputScalar_i \text{d} \inputScalar_j + \cdots +\int_0^1 \mappingFunction_{1,2,\dots,d}(\inputScalar_1,\inputScalar_2,\dots,\inputScalar_\dataDim)\text{d}\inputVector.
$$
This expression leads to the decomposition of the variance of $\dataScalar$ as,
$$ 
\text{var}(\dataScalar) = \sum_{i=1}^\dataDim V_i + \sum_{i<j}^{\dataDim} V_{ij} + \cdots + V_{12 \dots \dataDim},
$$
where
$$ 
V_{i} = \text{var}_{\inputScalar_i} \left( E_{\inputVector_{\sim i}} (\dataScalar \mid \inputScalar_{i}) \right),
$$
$$ 
V_{ij} = \text{var}_{\inputScalar_{ij}} \left( E_{\inputVector_{\sim ij}} \left( \dataScalar \mid \inputScalar_i, \inputScalar_j\right)\right) - \operatorname{V}_{i} - \operatorname{V}_{j}
$$
and so on. The $\inputVector_{\sim i}$ notation is used to indicate all the set of variables but the $i^{th}$.}

\notes{**Note**: The previous decomposition is important because it shows how the variance in the output $\dataScalar$ can be associated to each input or interaction separately}

\subsection{Example: the Ishigami function}

\notes{We illustrate the exact calculation of the Sobol indexes with the three dimensional Ishigami function of [@Ishigami-importance90]. This is a well-known example for uncertainty and sensitivity analysis methods because of its strong nonlinearity and peculiar dependence on $\inputScalar_3$. More details of this function can be found in [@Sobol-variance99].}

\notes{Mathematically, the from of the Ishigami function is
$$
\mappingFunction(\textbf{x}) = \sin(\inputScalar_1) + a \sin^2(\inputScalar_2) + b \inputScalar_3^4 \sin(\inputScalar_1). 
$$
In this notebook we will set the parameters to be $a = 5$ and $b=0.1$ . The input variables are sampled randomly $\inputScalar_i \sim \text{Uniform}(-\pi,\pi)$.}

\notes{Next we create the function object and visualize its shape marginally for each one of its three inputs.}

\setupcode{from emukit.test_functions.sensitivity import Ishigami}

\code{### --- Load the Ishigami function
ishigami = Ishigami(a=5, b=0.1)
target_simulator = ishigami.fidelity1

### --- Define the input space in which the simulator is defined
variable_domain = (-np.pi,np.pi)
x_grid = np.linspace(*variable_domain,100)
X, Y = np.meshgrid(x_grid, x_grid)}


\notes{Before moving to any further analysis, we first plot the non-zero components $\mappingFunction(\inputVector)$. These components are 
$$\begin{align*}
\mappingFunction_1(\inputScalar_1) & = \sin(\inputScalar_1) \\
\mappingFunction_2(\inputScalar_1) & = a \sin^2 (\inputScalar_2) \\
\mappingFunction_{13}(\inputScalar_1,\inputScalar_3) & = b \inputScalar_3^4 \sin(\inputScalar_1) 
\end{align*}$$}

\code{f1 = ishigami.f1(x_grid)
f2 = ishigami.f2(x_grid)
F13 = ishigami.f13(np.array([x_grid,x_grid]).T)[:,None]}

\setupplotcode{from mpl_toolkits.mplot3d import Axes3D}

\plotcode{fig, axs = plt.subplots(2, 2, figsize=plot.big_wide_figsize)
gs = axs[1, 1].get_gridspec()
# remove the underlying axes
for ax in axs[1, 0:]:
    ax.remove()

ax2 = fig.add_subplot(gs[1, 0:], projection='3d')

axs[0,0].plot(x_grid, f1,'-r')
axs[0,0].set_xlabel('$x_1$')
axs[0,0].set_ylabel('$f_1$')

axs[0,1].plot(x_grid,f2,'-r')
axs[0,1].set_xlabel('$x_2$')
axs[0,1].set_ylabel('$f_2$')

plt.suptitle('Non-zero Sobol components of the Ishigami function')

surf = ax2.plot_surface(X, Y, F13, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_3$')
ax2.set_zlabel('$f_{13}$')

mlai.write_figure(filename='non-zero-sobol-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/non-zero-sobol-ishigami}{80%}}{The non-zero components of the Ishigami function.}{non-zero-sobol-ishigami}

\notes{The total variance $\text{var}(\dataScalar)$ in this example is}

\code{print(ishigami.variance_total)}

\notes{which is the sum of the variance of $V_1$, $V_2$ and $V_{13}$}

\code{print(ishigami.variance_x1, ishigami.variance_x2, ishigami.variance_x13)
print(ishigami.variance_x1 + ishigami.variance_x2 + ishigami.variance_x13)}

\subsection{First Order Sobol Indices using Monte Carlo}

\notes{The first order Sobol indexes are a measure of "first order sensitivity" of each input variable. They account for the proportion of variance of $\dataScalar$ explained by changing each variable alone while marginalizing over the rest. The Sobol index of the $i$th variable is computed as
$$
S_i = \frac{V_i}{\text{var}(\dataScalar)}.
$$
This value is standardized using the total variance so it is possible to account for a fractional contribution of each variable to the total variance of the output.

The Sobol indexes for higher order interactions $S_{ij}$ are computed similarly. Note that the sum of all Sobol indexes equals to one.

In most cases we are interested in the first order indexes. In the Ishigami function their values are:}

\code{ishigami.main_effects}

\notes{The most standard way of computing the Sobol indexes is using Monte Carlo. Details are given in [@Sobol-global01].

With Emukit, the first-order Sobol indexes can be easily computed. We first need to define the space where of target simulator is analyzed.}

\setupcode{from emukit.core import ContinuousParameter, ParameterSpace}

\code{target_simulator = ishigami.fidelity1
variable_domain = (-np.pi,np.pi)

space = ParameterSpace(
          [ContinuousParameter('x1', variable_domain[0], variable_domain[1]), 
           ContinuousParameter('x2', variable_domain[0], variable_domain[1]),
           ContinuousParameter('x3', variable_domain[0], variable_domain[1])])}
						
\notes{Compute the indexes is as easy as doing}

\setupcode{from emukit.sensitivity.monte_carlo import ModelFreeMonteCarloSensitivity}

\code{np.random.seed(10)  # for reproducibility

num_mc = 10000  # Number of MC samples
senstivity_ishigami = ModelFreeMonteCarloSensitivity(target_simulator, space)
main_effects, total_effects, _ = senstivity_ishigami.compute_effects(num_monte_carlo_points = num_mc)
print(main_effects)}

\notes{We compare the true effects with the Monte Carlo effects in a bar-plot. The total effects are discussed later.}

\setupplotcode{import pandas as pd}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

d = {'Sobol True': ishigami.main_effects,
     'Monte Carlo': main_effects}

pd.DataFrame(d).plot(kind='bar', ax=ax)
ax.set_title('First-order Sobol indices - Ishigami')
ax.set_ylabel('% of explained output variance')

mlai.write_figure(filename='first-order-sobol-indices-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/first-order-sobol-indices-ishigami}{80%}}{The non-zero components of the Ishigami function.}{first-order-sobol-indices-ishigami}

\subsection{Total Effects Using Monte Carlo}

\notes{Computing high order sensitivity indexes can be computationally very demanding in high dimensional scenarios and measuring the total influence of each variable on the variance of the output is infeasible. To solve this issue the *total* indexes are used which account for the contribution to the output variance of $\inputScalar_i$ including all variance caused by the variable alone and all its interactions of any order. The total effect for $\inputScalar_i$ is given by:
$$ 
S_{Ti} = \frac{E_{\inputVector_{\sim i}} \left(\text{var}_{\inputScalar_i} (\dataScalar \mid \inputVector_{\sim i}) \right)}{\text{var}(\dataScalar)} = 1 - \frac{\text{var}_{\inputVector_{\sim i}} \left(E_{\inputScalar_i} (\dataScalar \mid \inputVector_{\sim i}) \right)}{\text{var}(\dataScalar)}
$$

Note that the sum of $S_{Ti}$ is not necessarily one in this case unless the model is additive. In the Ishigami example the value of the total effects is}

\code{ishigami.total_effects}

\notes{As in the previous example, the total effects can be computed with Monte Carlo. In the next plot we show the comparison with the true total effects.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

d = {'Sobol True': ishigami.total_effects,
     'Monte Carlo': total_effects}

pd.DataFrame(d).plot(kind='bar', ax=ax)
ax.set_title('Total effects - Ishigami')
ax.set_ylabel('Effects value')

mlai.write_figure(filename='total-effects-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/total-effects-ishigami}{80%}}{The total effects from the Ishigami function as computed via Monte Carlo estimate alongside the true total effects for the Ishigami function.}{total-effects-ishigami}


\subsection{Computing the sensitivity coefficients using the output of a model}

\notes{In the example used above the Ishigami function is very cheap to evaluate. However, in most real scenarios the functions of interest are expensive and we need to limit ourselves to a few number of evaluations. Using Monte Carlo methods is infeasible in these scenarios as a large number of samples are typically required to provide good estimates of the Sobol coefficients.

An alternative in these cases is to use Gaussaian process emulator of the function of interest trained on a few inputs and outputs. If the model is properly trained, its mean prediction which is cheap to evaluate, can be used to compute the Monte Carlo estimates of the Sobol coefficients. Let's see how we can do this in Emukit.


We start by generating 100 samples in the input domain. Note that this a just 1% of the number of samples that we used to compute the Sobol coefficients using Monte Carlo.}

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{desing = RandomDesign(space)
x = desing.get_samples(500)
y = ishigami.fidelity1(x)[:,None]}

\notes{Now, we fit a standard Gaussian process to the samples and we wrap it as an Emukit model.}

\setupcode{from GPy.models import GPRegression
from emukit.model_wrappers import GPyModelWrapper
from emukit.sensitivity.monte_carlo import MonteCarloSensitivity}

\code{model_gpy = GPRegression(x,y)
model_emukit = GPyModelWrapper(model_gpy)
model_emukit.optimize()}

\notes{The final step is to compute the coefficients using the class `ModelBasedMonteCarloSensitivity` which directly calls the model and uses its predictive mean to compute the Monte Carlo estimates of the Sobol indices. We plot the true estimates, those computed using 10000 direct evaluations of the objecte using Monte Carlo and those computed using a Gaussian process model trained on 100 evaluations.}

\code{senstivity_ishigami_gpbased = MonteCarloSensitivity(model = model_emukit, input_domain = space)
main_effects_gp, total_effects_gp, _ = senstivity_ishigami_gpbased.compute_effects(num_monte_carlo_points = num_mc)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

main_effects_gp = {ivar: main_effects_gp[ivar][0] for ivar in main_effects_gp}

d = {'Sobol True': ishigami.main_effects,
     'Monte Carlo': main_effects,
     'GP Monte Carlo':main_effects_gp}

pd.DataFrame(d).plot(kind='bar', ax=ax)
plt.title('First-order Sobol indexes - Ishigami')
plt.ylabel('% of explained output variance')

mlai.write_figure(filename='first-order-sobol-indices-gp-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/first-order-sobol-indices-gp-ishigami}{80%}}{First Order sobol indices as estimated by Monte Carlo and GP-emulator based Monte Carlo.}{first-order-sobol-indices-gp-ishigami}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

total_effects_gp = {ivar: total_effects_gp[ivar][0] for ivar in total_effects_gp}

d = {'Sobol True': ishigami.total_effects,
     'Monte Carlo': total_effects,
     'GP Monte Carlo':total_effects_gp}

pd.DataFrame(d).plot(kind='bar', ax=ax)
ax.set_title('Total effects - Ishigami')
ax.set_ylabel('% of explained output variance')

mlai.write_figure(filename='total-effects-sobol-indices-gp-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/total-effects-sobol-indices-gp-ishigami}{80%}}{Total effects as estimated by Monte Carlo and GP based Monte Carlo.}{total-effects-sobol-indices-gp-ishigami}

\notes{We observe some discrepacies with respect to the real value of the coefficient when using the Gaussian process but we get a fairly good a approximation a very reduced number of evaluations of the original target function.}

\subsection{Conclusions}

\notes{The Sobol indexes are a tool for explaining the variance of the output of a function as components of the input variables. Monte Carlo is an approach for computing these indexes if the function is cheap to evaluate. Other approaches will be needed if $\mappingFunction(\cdot)$ is expensive to compute.}


\thanks

\reading

\references
