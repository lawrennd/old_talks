
\ifndef{emukitSensitivityAnalysis}
\define{emukitSensitivityAnalysis}

\editme

\subsection{Emukit Sensitivity Analysis}


\notes{This introduction is based on [Introduction to Global Sensitivity Analysis with Emukit](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-sensitivity-montecarlo.ipynb) written by Mark Pullin, Javier Gonzalez, Juan Emmanuel Johnson and Andrei Paleyes. Some references include [@Kennedy-predicting00;@Sobol-sensitivity90;@Sobol-global01;@Saltelli-sensitivity04;@Saltelli-global08;@Saltelli-variance10]}

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

\installcode{mlai}

\installcode{GPy}
\installcode{pyDOE}
\installcode{EmuKit}

\setupcode{import mlai
import mlai.plot as plot}

\notes{Sensitivity analysis is a statistical technique widely used to test the reliability of real systems. Imagine a simulator of taxis picking up customers in a city like the one showed in the [Emukit playground](https://github.com/amzn/emukit-playground). The profit of the taxi company depends on factors like the number of taxis on the road and the price per trip. In this example, a global sensitivity analysis of the simulator could be useful to decompose the variance of the profit in a way that can be assigned to the input variables of the simulator.}

\notes{There are different ways of doing a sensitivity analysis of the variables of a simulator. In this notebook we will start with an approach based on Monte Carlo sampling that is useful when evaluating the simulator is cheap. If evaluating the simulator is expensive, emulators can then be used to speed up computations. We will show this in the last part of the notebook. Next, we start with a few formal definitions and literature review so we can understand the basics of Sensitivity Analysis and how it can performed with Emukit.}


\subsection{Local Sensitivity}

\notes{Given any function, $\mappingFunctionTwo(\cdot)$, we might be interested in how sensitive that function is to variations in its input space. One route to determining this is to compute the partial derivatives of that function with respect to its inputs,}
$$
\frac{\partial}{\partial\inputScalar_i} \mappingFunctionTwo(\inputVector).
$$
\notes{The matrix of all these partial derivatives is known as the Jacobian.}

\notes{These types of local sensitivity analysis can be used for determining the effect of changing an input variable around an operating point. But they don't give us an understanding of the response of the target function to variations in the input across the domain of inputs. For this, we need to look to *global sensitivity analysis*.}

\subsection{Global Sensitivity Analysis}

\notes{In global sensitivity analysis, rather than looking around a single operating point, we're interested in the overall sensitivity of a function to its inputs, or combinations of inputs, across its entire domain. The key tool in determining this sensitivity is known as the ANOVA decomposition, or the *Hoeffding-Sobol decomposition*.}

\notes{For global sensitivity analysis, we need to make an assumption about how are inputs are going to vary to create different values of the function. The fundamental object we're interested in is the total variance of the function,}
$$
\text{var}\left(\mappingFunctionTwo(\inputVector)\right) = \expectationDist{\mappingFunctionTwo(\inputVector)^2}{p(\inputVector)} - \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)}^2
$$
\notes{where}
$$
\expectationDist{h(\inputVector)}{p(\inputVector)} = \int_\inputVector h(\inputVector) p(\inputVector) \text{d}\inputVector
$$
\notes{is the expectation of the function $h(\inputVector)$ under the density $p(\inputVector)$, which represents the probability distribution of inputs we're interested in.}

\newslide{Input Density}

\notes{The total variance of the function gives us the overal variation of the function across the domain of inputs, as represented by the probability density, $p(\inputVector)$. Normally, we perform analysis by assuming that,}
$$
p(\inputVector) = \prod_{i=1}^\dataDim p(\inputScalar_i)
$$
\notes{and that each $p(\inputScalar_i)$ is *uniformly distributed* across its input domain. Assuming we scale the input domain down to the interval $[0, 1]$, that gives us}
$$
\inputScalar_i \sim \uniformSamp{0}{1}.
$$

\subsection{Hoeffding-Sobol Decomposition}

\notes{The Hoeffding-Sobol, or ANOVA, decomposition of a function allows us to write it as,}
$$
\begin{align*}
\mappingFunctionTwo(\inputVector) = & \mappingFunctionTwo_0 + \sum_{i=1}^\dataDim \mappingFunctionTwo_i(\inputScalar_i) + \sum_{i<j}^{\dataDim} \mappingFunctionTwo_{ij}(\inputScalar_i,\inputScalar_j) + \cdots \\
& + \mappingFunctionTwo_{1,2,\dots,\dataDim}(\inputScalar_1,\inputScalar_2,\dots,\inputScalar_\dataDim),
\end{align*}
$$
\newslide{}\notes{where}
$$
\mappingFunctionTwo_0 = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)}
$$
\notes{and}
$$
\mappingFunctionTwo_i(\inputScalar_i) = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector_{\sim i})} - \mappingFunctionTwo_0,
$$
\notes{where we're using the notation $p(\inputVector_{\sim i})$ to represent the input distribution with the $i$th variable marginalised,}
$$
p(\inputVector_{\sim i}) = \int p(\inputVector) \text{d}\inputScalar_i
$$
\notes{Higher order terms in the decomposition represent interactions between inputs,}
$$
\mappingFunctionTwo_{i,j}(\inputScalar_i, \inputScalar_j) = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector_{\sim i,j})} - \mappingFunctionTwo_i(\inputScalar_i) - \mappingFunctionTwo_j(\inputScalar_j) - \mappingFunctionTwo_0
$$
\notes{and similar expressions can be written for higher order terms up to $\mappingFunctionTwo_{1,2,\dots,\dataDim}(\inputVector)$.}

\notes{Note that to compute each of these individual terms, you need to first compute the low order terms, and then compute the high order terms. This can be problematic when $\dataDim$ is large.}

\notes{We're interested in the variance of the function $\mappingFunctionTwo$, so implicitly we're assuming that the square of this function is integrable across its domain, i.e. we're assuming that $\expectationDist{\mappingFunctionTwo(\inputVector)^2}{p(\inputVector)}$ exists and is finite.}

\newslide{}

\notes{The Sobol decomposition has some important properties, in particular, it components are orthogonal, so this means that when we substitute it in to the variance, we have,}
$$
\begin{align*}
\text{var}(\mappingFunctionTwo) = & \expectationDist{\mappingFunctionTwo(\inputVector)^2 }{p(\inputVector)} - \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)}^2 \\
 = & \expectationDist{\mappingFunctionTwo(\inputVector)^2 }{p(\inputVector)} - \mappingFunctionTwo_0^2\\
 = & \sum_{i=1}^\dataDim \text{var}\left(\mappingFunctionTwo_i(\inputScalar_i)\right) + \sum_{i<j}^{\dataDim} \text{var}\left(\mappingFunctionTwo_{ij}(\inputScalar_i,\inputScalar_j)\right)  + \cdots \\ & + \text{var}\left(\mappingFunctionTwo_{1,2,\dots,\dataDim}(\inputScalar_1,\inputScalar_2,\dots,\inputScalar_\dataDim)\right).
\end{align*}
$$
\notes{So, this decomposition gives us a decomposition of the function in terms of variances. It's for this reason that it's sometimes known as an ANOVA decomposition. ANOVA stands a for *analysis of variance*. The ANOVA decomposition decomposes the function into additive variance parts that are each stemming from interactions between different inputs.}

\newslide{Sobol Indices}

\notes{As is common in various analyses of variance, we can rescale the components with the *total variance* of the function. These rescaled components are known as *Sobol indicies*.}
$$
S_\ell = \frac{\text{var}\left(\mappingFunctionTwo(\inputVector_\ell)\right)}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)},
$$
\notes{where the $\ell$ represents the relevent set of indices for the different combinations of inputs.}

\notes{In practice, For an elegant approach that exploits a particular covariance function structure to perform global sensitivity analysis see @Durrande-anova13.}

\section{Example: the Ishigami function}

\notes{We illustrate the exact calculation of the Sobol indices with the three dimensional Ishigami function of [@Ishigami-importance90].} 

\include{_uq/includes/ishigami-function.md}

\subsection{Total Variance}

\notes{The total variance $\text{var}(\dataScalar)$ in this example is}

\code{print(ishigami.variance_total)}

\notes{which is the sum of the variance of $\text{var}\left(\mappingFunctionTwo_1(\inputScalar_1)\right)$, $\text{var}\left(\mappingFunctionTwo_2(\inputScalar_2)\right)$ and $\text{var}\left(\mappingFunctionTwo_{1,3}(\inputScalar_{1,3})\right)$}

\code{print(ishigami.variance_x1, ishigami.variance_x2, ishigami.variance_x13)
print(ishigami.variance_x1 + ishigami.variance_x2 + ishigami.variance_x13)}

\subsection{First Order Sobol Indices using Monte Carlo}

\notes{The first order Sobol indices are a measure of "first order sensitivity" of each input variable. They account for the proportion of variance of $\dataScalar$ explained by changing each variable alone while marginalizing over the rest. Recall that the Sobol index of the $i$th variable is computed as}
$$
S_i = \frac{\text{var}\left(\mappingFunctionTwo_i(\inputScalar_i)\right)}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)}.
$$
\notes{This value is standardized using the total variance so it is possible to account for a fractional contribution of each variable to the total variance of the output.}

\notes{The Sobol indices for higher order interactions $S_{i,j}$ are computed similarly. Due to the normalization by the total variance, the the sum of all Sobol indices equals to one.}

\notes{In most cases we are interested in the first order indices. The Ishigami function has the benefit that these can be computed analytically. In `EmuKit` you can extract these values with the code.}

\code{ishigami.main_effects}

\notes{But in general these indices need to be sampled using Monte Carlo or one of the quasi-Monte Carlo methods we've seen in the model-free experimental design. Details are given in [@Sobol-global01].}

\notes{With Emukit, the first-order Sobol indices can be easily computed. We first need to define the space where of target simulator is analyzed.}

\setupcode{from emukit.sensitivity.monte_carlo import ModelFreeMonteCarloSensitivity}

\code{np.random.seed(10)  # for reproducibility

num_monte_carlo_points = 10000  # Number of MC samples
senstivity_ishigami = ModelFreeMonteCarloSensitivity(target_simulator, space)
main_effects, total_effects, _ = senstivity_ishigami.compute_effects(num_monte_carlo_points = num_monte_carlo_points)
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

\notes{Computing high order sensitivity indices can be computationally very demanding in high dimensional scenarios and measuring the total influence of each variable on the variance of the output is infeasible. To solve this issue the *total* indices are used which account for the contribution to the output variance of $\inputScalar_i$ including all variance caused by the variable alone and all its interactions of any order. 

The total effect for $\inputScalar_i$ is given by:
$$ 
S_{Ti} = \frac{\expectationDist{\text{var}_{\inputScalar_i} (\dataScalar \mid \inputVector_{\sim i})}{p(\inputVector_{\sim i})}}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)} = 1 - \frac{\text{var}_{\inputVector_{\sim i}} \expectationDist{\dataScalar \mid \inputVector_{\sim i}}{p(\inputVector_{\sim i})}}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)}
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

\subsection{Computing the sensitivity indices using the output of a model}

\notes{In the example used above the Ishigami function is very cheap to evaluate. However, in most real scenarios the functions of interest are expensive and we need to limit ourselves to a few number of evaluations. Using Monte Carlo methods is infeasible in these scenarios as a large number of samples are typically required to provide good estimates of the Sobol indices.}

\notes{An alternative in these cases is to use Gaussaian process emulator of the function of interest trained on a few inputs and outputs [@Marrel-sobol09]. If the model is properly trained, its mean prediction which is cheap to evaluate, can be used to compute the Monte Carlo estimates of the Sobol indices, the variance from the GP emulator can also be used to assess our uncertainty about the Sobol indices. Let's see how we can do this in Emukit.}


\notes{We start by generating 100 samples in the input domain. Note that this a just 1% of the number of samples that we used to compute the Sobol coefficients using Monte Carlo.}

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{design = RandomDesign(space)
x = design.get_samples(500)
y = ishigami.fidelity1(x)[:,np.newaxis]}

\notes{Now, we fit a standard Gaussian process to the samples and we wrap it as an Emukit model.}

\setupcode{from GPy.models import GPRegression
from emukit.model_wrappers import GPyModelWrapper
from emukit.sensitivity.monte_carlo import MonteCarloSensitivity}

\code{model_gpy = GPRegression(x,y)
model_emukit = GPyModelWrapper(model_gpy)
model_emukit.optimize()}

\notes{The final step is to compute the coefficients using the class `ModelBasedMonteCarloSensitivity` which directly calls the model and uses its predictive mean to compute the Monte Carlo estimates of the Sobol indices. We plot the true estimates, those computed using 10000 direct evaluations of the objecte using Monte Carlo and those computed using a Gaussian process model trained on 100 evaluations.}

\code{num_mc = 10000
senstivity_ishigami_gpbased = MonteCarloSensitivity(model = model_emukit, input_domain = space)
main_effects_gp, total_effects_gp, _ = senstivity_ishigami_gpbased.compute_effects(num_monte_carlo_points = num_mc)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

main_effects_gp = {ivar: main_effects_gp[ivar][0] for ivar in main_effects_gp}

d = {'Sobol True': ishigami.main_effects,
     'Monte Carlo': main_effects,
     'GP Monte Carlo':main_effects_gp}

pd.DataFrame(d).plot(kind='bar', ax=ax)
plt.title('First-order Sobol indices - Ishigami')
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

\newslide{}

\figure{\includediagram{\diagramsDir/uq/total-effects-sobol-indices-gp-ishigami}{80%}}{Total effects as estimated by Monte Carlo and GP based Monte Carlo.}{total-effects-sobol-indices-gp-ishigami}

\notes{We observe some discrepacies with respect to the real value of the Sobol index when using the Gaussian process but we get a fairly good a approximation a very reduced number of evaluations of the original target function.}

\subsection{Conclusions}
\slides{* Sobol indices tool for explaining variance of output as coponents of input variables.}
\notes{The Sobol indices are a tool for explaining the variance of the output of a function as components of the input variables. Monte Carlo is an approach for computing these indices if the function is cheap to evaluate. Other approaches are needed when $\mappingFunctionTwo(\cdot)$ is expensive to compute.}


\endif
