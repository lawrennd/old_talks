---
week: 4
layout: lecture
title: "Sensitivity Analysis"
abstract: >
  A surrogate model can be explored to understand the sensitivity of the system. This lecture will review how to perform sensitivity analysis.
layout: lecture
time: "12:00"
date: 2020-10-30
venue: Virtual (Zoom)
ipynb: false
reveal: false
transition: None
---

\include{talk-macros.tex}

[@Kennedy-predicting00;@Sobol-sensitivity90;@Sobol-global01;@Saltelli-sensitivity04;@Saltelli-global08;@Saltelli-variance10]

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

\plotcode{fig, ax = plt.subplots(1, 2, figsize=plot.big_wide_figure)
ax.append(fig.add_subplot(111, projection='3d'))

ax[0].plot(x_grid, f1,'-r')
ax[0].set_xlabel('$x_1$')
ax[0].set_ylabel('$f_1$')

ax[1].plot(x_grid,f2,'-r')
ax[1].set_xlabel('$x_2$')
ax[1].set_ylabel('$f_2$')

plt.suptitle('Non-zero Sobol components of the Ishigami function')

surf = ax[2].plot_surface(X, Y, F13, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_3$')
ax.set_zlabel('$f_{13}$')

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

\plotcode{d = {'Sobol True': ishigami.main_effects,
     'Monte Carlo': main_effects}

pd.DataFrame(d).plot(kind='bar',figsize=plot.big_wide_figsize, ax=ax)
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

\plotcode{d = {'Sobol True': ishigami.total_effects,
     'Monte Carlo': total_effects}

pd.DataFrame(d).plot(kind='bar',figsize=(12, 5), ax=ax)
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

\plotcode{main_effects_gp = {ivar: main_effects_gp[ivar][0] for ivar in main_effects_gp}

d = {'Sobol True': ishigami.main_effects,
     'Monte Carlo': main_effects,
     'GP Monte Carlo':main_effects_gp}

pd.DataFrame(d).plot(kind='bar',figsize=(12, 5))
plt.title('First-order Sobol indexes - Ishigami')
plt.ylabel('% of explained output variance')

mlai.write_figure(filename='first-order-sobol-indices-gp-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/first-order-sobol-indices-gp-ishigami}{80%}}{First Order sobol indices as estimated by Monte Carlo and GP-emulator based Monte Carlo.}{first-order-sobol-indices-gp-ishigami}


\plotcode{total_effects_gp = {ivar: total_effects_gp[ivar][0] for ivar in total_effects_gp}

d = {'Sobol True': ishigami.total_effects,
     'Monte Carlo': total_effects,
     'GP Monte Carlo':total_effects_gp}

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

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
