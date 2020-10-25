---
week: 4
title: "Emulation and Experimental Design"
abstract:  >
  This lecture will review the ideas behind using surrogate models for experimental design.
layout: lecture
time: "10:00"
date: 2020-10-29
venue: Virtual (Zoom)
ipynb: false
reveal: false
transition: None
---

\include{talk-macros.tex}

\section{Emulation}

\include{_uq/includes/emulation.md}

\section{Emukit Playground}

\include{_uq/includes/emukit-playground.md}


Related publications and links will appear here.

Emukit https://nbviewer.jupyter.org/github/amzn/emukit/blob/master/notebooks/index.ipynb
Emukit Playground: https://amzn.github.io/emukit-playground/#!/

Examle paper: @McKay-selecting79 @Kennedy-bayesian01

 Random Sampling. Let the input values X1, * * , XN
 be a random sample from F(x). This method of sam-
 pling is perhaps the most obvious, and an entire body
 of statistical literature may be used in making infer-
 ences regarding the distribution of Y(t).
 Stratified Sampling. Using stratified sampling, all
 areas of the sample space of X are represented by
 input values. Let the sample space S of X be parti-
 tioned into I disjoint strata St. Let pi = P(X C Si)
 represent the size of Si. Obtain a random sample XiJ,j
 = 1, * * , n from Si. Then of course the ni sum to N.
 If I = 1, we have random sampling over the entire
 sample space.
 Latin Hypercube Sampling. The same reasoning
 that led to stratified sampling, ensuring that all por-
 tions of S were sampled, could lead further. If we
 wish to ensure also that each of the input variables Xk
 has all portions of its distribution represented by
 input values, we can divide the range of each Xk into
 N strata of equal marginal probability 1/N, and
 sample once from each stratum. Let this sample be
 Xkj,j = 1, ..., N. These form the Xk component, k =
 1, * , K, in Xi, i = 1, * , N. The components of the
 various X,A's are matched at random. This method of
 selecting input values is an extension of quota sam-
 pling [13], and can be viewed as a K-dimensional
 extension of Latin square sampling [11].
 One advantage of the Latin hypercube sample ap-
 pears when the output Y(t) is dominated by only a
 few of the components of X. This method ensures
 that each of those components is represented in a
 fully stratified manner, no matter which components
 might turn out to be important.
 We mention here that the N intervals on the range
 of each component of X combine to form NK cells
 which cover the sample space of X. These cells, which
 are labeled by coordinates corresponding to the inter-
 vals, are used when finding the properties of the
 sampling plan.

Experimental design.

Latin hypercube

Linear example

\setupcode{from emukit.test_functions import forrester_function
from emukit.core.loop.user_function import UserFunctionWrapper
from emukit.core import ContinuousParameter, ParameterSpace}


\code{target_function, space = forrester_function()}

\code{x_plot = np.linspace(space.parameters[0].min, space.parameters[0].max, 301)[:, None]
y_plot = target_function(x_plot)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_plot, y_plot, "k", label="target Function")

ax.legend(loc=2, prop={'size': LEGEND_SIZE})
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function.svg', directory='\writeDiagramsDir/uq')}

\subsection{Initial Design}

\notes{Usually, before we start the actual ExpDesign loop we need to gather a few observations such that we can fit the model. This is called the initial design and common strategies are either a predefined grid or sampling points uniformly at random.}

\code{X_init = np.array([[0.2],[0.6], [0.9]])
Y_init = target_function(X_init)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X_init, Y_init, "ro", markersize=10, label="Observations")
ax.plot(x_plot, y_plot, "k", label="Target Function")

ax.legend(loc=2, prop={'size': LEGEND_SIZE})
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function-initial-design.svg', directory='\writeDiagramsDir/uq')}

\subsection{The Model}

\notes{Now we can start with the ExpDesign loop by first fitting a model on the collected data. 
A popular model for ExpDesign is a Gaussian process (GP) which defines a probability distribution across classes of functions, typically smooth, such that each linear finite-dimensional restriction is multivariate Gaussian [@Rasmussen:book06](#4.-References). GPs are fully parametrized by a mean $\mu(\inputVector)$ and a covariance function $\kernelScalar(\inputVector,\inputVector')$.  Without loss of generality $\mu(\inputVector)$ is assumed to be zero. The covariance function $\kernelScalar(\inputVector,\inputVector')$ characterizes the smoothness and other properties of $\mappingFunction$. It is known that the kernel of the process has to be continuous, symmetric and positive definite. A widely used kernel is the squared exponential or RBF kernel: $$ \kernelScalar(\inputVector,\inputVector') = \theta_0 \cdot \exp{ \left(-\frac{\|\inputVector-\inputVector'\|^2}{\theta_1}\right)} $$ where $\theta_0$ and and $\theta_1$ are hyperparameters.
To denote that $\mappingFunction$ is a sample from a GP with mean $\mu$ and covariance $k$ we write
$$
\mappingFunction \sim \mathcal{GP}(\mu,k).
$$ 

For regression tasks, the most important feature of GPs is that process priors are conjugate to the likelihood from finitely many observations $\dataMatrix = (y_1,\dots,y_n)^T$ and $\inputMatrix =\{\inputVector_1,...,\inputVector_n\}$, $\inputVector_i\in \mathcal{X}$ of the form $y_i = \mappingFunction(\inputVector_i) + \epsilon_i$ where $\epsilon_i \sim \mathcal{N} (0,\sigma_{noise}^2)$ and we estimate $\sigma_{noise}$ by an additional hyperparameter $\theta_2$.
We obtain the Gaussian posterior $\mappingFunction(\inputVector^*)|\inputMatrix, \dataMatrix, \theta \sim \mathcal{N}(\mu(\inputVector^*),\sigma^2(\inputVector^*))$, where $\mu(\inputVector^*)$ and $\sigma^2(\inputVector^*)$ have a close form. See @Rasmussen:book06 for more details.}

\notes{Note that Gaussian processes are also characterized by hyperparameters $\theta = \{\theta_0, ... \theta_k\}$ such as for instance the kernel lengthscales. For simplicitly we keep these hyperparameters fixed here. However, we usually either optimize or sample these hyperparameters using the marginal loglikelihood of the GP. Of course we could also use any other model that returns a mean $\mu(\inputVector)$ and variance $\sigma^2(\inputVector)$ on an arbitrary input points $\inputVector$ such as Bayesian neural networks or random forests.}

\setupcode{import GPy
from emukit.model_wrappers.gpy_model_wrappers import GPyModelWrapper}

\code{kern = GPy.kern.RBF(1, lengthscale=0.08, variance=20)
gpy_model = GPy.models.GPRegression(X_init, Y_init, kern, noise_var=1e-10)
emukit_model = GPyModelWrapper(gpy_model)

mu_plot, var_plot = emukit_model.predict(x_plot)}

\setupplotcode{import matplotlib.pyplot as plt}

\plotcode{plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X_init, Y_init, "ro", markersize=10, label="Observations")
ax.plot(x_plot, y_plot, "k", label="Objective Function")
ax.plot(x_plot, mu_plot, "C0", label="Model")
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - np.sqrt(var_plot)[:, 0], color="C0", alpha=0.6)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 2 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 2 * np.sqrt(var_plot)[:, 0], color="C0", alpha=0.4)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 3 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 3 * np.sqrt(var_plot)[:, 0], color="C0", alpha=0.2)
ax.legend(loc=2, prop={'size': LEGEND_SIZE})
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function-entropy.svg', directory='\writeDiagramsDir/uq')}

\subsection{The Acquisition Function}

\notes{In the second step of our ExpDesign loop we use our model to compute the acquisition function. Two example of ExpDesign acquisition functions are:


**Uncertainty Sampling (US)**: Choose the next value $x_{n+1}$ at the location where the model on $f(x)$ has the highest marginal predictive variance

$$
a_{US}(x) = \sigma^2(x)
$$ 

This makes sure, that we learn the function $f$ everywhere on $\mathbb{X}$ to a similar level of absolute error.


**Integrated variance reduction (IVR)**: Choose the next value $x_{n+1}$ such that the total variance of the model is reduced maximally [[Sacks et al. 1989]](#4.-References).

$$
a_{IVR} = \int_{\mathbb{X}}[\sigma^2(x') - \sigma^2(x'; x)]\mathrm{d}x'\approx 
\frac{1}{\# samples}\sum_i^{\# samples}[\sigma^2(x_i) - \sigma^2(x_i; x)].
$$

Here $\sigma^2(x'; x)$ is the predictive variance at $x'$ had $x$ been observed. Thus IVR compute the overall reduction in variance (for all points in $\mathbb{X}$) had $f$ been observed at $x$.
The finite sum approximation on the right hand side of the equation is usually used because the integral over $x'$ is not analytic. In that case $x_i$ are sampled randomly. For a GP model the right hand side simplifies to $a_{LCB} \approx \frac{1}{\# samples}\sum_i^{\# samples}\frac{k^2(x_i, x)}{\sigma^2(x)}$.

IVR is arguably te more principled approach, but often US is preferred over IVR simply because it lends itself to gradient based optimization more easily, is cheaper to compute, and is exact. 
For both of them (stochastic) gradient base optimizers are used to retrieve $x_{n+1} \in \operatorname*{arg\:max}_{x \in \mathbb{X}} a(x)$. }


\notes{from emukit.experimental_design.acquisitions import IntegratedVarianceReduction, ModelVariance

us_acquisition = ModelVariance(emukit_model)
ivr_acquisition = IntegratedVarianceReduction(emukit_model, space)

us_plot = us_acquisition.evaluate(x_plot)
ivr_plot = ivr_acquisition.evaluate(x_plot)

plt.figure(figsize=(12, 8))
plt.plot(x_plot, us_plot / np.max(us_plot), "green", label="US")
plt.plot(x_plot, ivr_plot / np.max(ivr_plot) , "purple", label="IVR")

plt.legend(loc=1, prop={'size': LEGEND_SIZE})
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.grid(True)
plt.xlim(0, 1)
plt.show()}


\notes{Afterwards we evaluate the true objective function and append it to our initial observations.}

\code{y_new = target_function(x_new)}

\code{X = np.append(X_init, x_new, axis=0)
Y = np.append(Y_init, y_new, axis=0)}

\notes{After updating the model, you can see that the uncertainty about the true objective function in this region decreases and our model becomes more certain.}

\code{emukit_model.set_data(X, Y)
mu_plot, var_plot = emukit_model.predict(x_plot)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(emukit_model.X, emukit_model.Y, "ro", markersize=10, label="Observations")
ax.plot(x_plot, y_plot, "k", label="Target Function")
ax.plot(x_plot, mu_plot, "C0", label="Model")
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - np.sqrt(var_plot)[:, 0], color="C0", alpha=0.6)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 2 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 2 * np.sqrt(var_plot)[:, 0], color="C0", alpha=0.4)
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 3 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 3 * np.sqrt(var_plot)[:, 0], color="C0", alpha=0.2)
ax.legend(loc=2, prop={'size': LEGEND_SIZE})
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function-multi-errorbars.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function-multi-errorbars}{80%}}{The target Forrester function plotted alongside the emulation model and error bars from the emulation at 1, 2 and 3 standard deviations.}{forrester-function-multi-errorbars}

Entropy of posterior


\subsection{Evaluation the Objective Function}

\note{To find the next point to evaluate we optimize the acquisition function using a standard gradient descent optimizer.}

\setupcode{from emukit.core.optimization import GradientAcquisitionOptimizer}

\code{optimizer = GradientAcquisitionOptimizer(space)
x_new, _ = optimizer.optimize(us_acquisition)}

\plotcode{plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_plot, us_plot / np.max(us_plot), "green", label="US")
ax.axvline(x_new, color="red", label="x_next", linestyle="--")
ax.legend(loc=1, prop={'size': LEGEND_SIZE})
ax.xlabel(r"$x$")
ax.ylabel(r"$f(x)$")
ax.grid(True)
ax.xlim(-0.01, 1)

mlai.write_figure(filename='forrester-function-fit.svg', directory='\writeDiagramsDir/uq')}

\subsection{Emukit's experimental design interface}

\notes{Of course in practice we don't want to implement all of these steps our self. Emukit provides a convenient and flexible interface to apply experimental design. Below we can see how to run experimental design on the exact same function for 10 iterations.}

\setupcode{from emukit.experimental_design.experimental_design_loop import ExperimentalDesignLoop}

\code{ed = ExperimentalDesignLoop(space=space, model=emukit_model)

ed.run_loop(target_function, 10)}

\code{mu_plot, var_plot = ed.model.predict(x_plot)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(ed.loop_state.X, ed.loop_state.Y, "ro", markersize=10, label="Observations")
ax.plot(x_plot, y_plot, "k", label="Objective Function")
ax.plot(x_plot, mu_plot, "C0", label="Model")
ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - np.sqrt(var_plot)[:, 0], color="C0", alpha=0.6)

ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 2 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 2 * np.sqrt(var_plot)[:, 0], color="C0", alpha=0.4)

ax.fill_between(x_plot[:, 0],
                 mu_plot[:, 0] + 3 * np.sqrt(var_plot)[:, 0],
                 mu_plot[:, 0] - 3 * np.sqrt(var_plot)[:, 0], color="C0", alpha=0.2)
ax.legend(loc=2, prop={'size': LEGEND_SIZE})
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_grid(True)
ax.set_xlim(0, 1)
}

\thanks

\reading

\references

