---
session: 4
title: Gaussian Processes
abstract: >
  Classical machine learning and statistical approaches to learning, such as neural networks and linear regression, assume a parametric form for functions. Gaussian process models are an alternative approach that assumes a probabilistic prior over functions. This brings benefits, in that uncertainty of function estimation is sustained throughout inference, and some challenges: algorithms for fitting Gaussian processes tend to be more complex than parametric models. 
  
  In this sessions I will introduce Gaussian processes and explain why sustaining uncertainty is important. 
date: 2020-11-13
venue: Virtual Data Science Nigeria
time: "15:00 (West Africa Standard Time)"
transition: None
---

\include{talk-macros.tex}
\include{_mlai/includes/mlai-notebook-setup.md}

\include{_gp/includes/gp-book.md}
\include{_ml/includes/first-course-book.md}
<!--include{_gp/includes/what-is-a-gp.md}-->

\include{_health/includes/malaria-gp.md}
\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/overdetermined-inaugural.md}
\include{_ml/includes/univariate-gaussian-properties.md}


\include{_ml/includes/multivariate-gaussian-properties.md}
\notes{\include{_ml/includes/linear-regression-log-likelihood.md}
\include{_ml/includes/olympic-marathon-linear-regression.md}
\include{_ml/includes/linear-regression-multivariate-log-likelihood.md}
\define{designVector}{\basisVector}
\define{designVariable}{Phi}
\define{designMatrix}{\basisMatrix}
\include{_ml/includes/linear-regression-direct-solution.md}}
\include{_ml/includes/linear-regression-objective-optimisation.md}
\include{_ml/includes/movie-body-count-linear-regression.md}

\include{_ml/includes/underdetermined-system.md}
\include{_ml/includes/two-d-gaussian.md}

\include{_ml/includes/basis-functions-nn.md}
\include{_ml/includes/relu-basis.md}

\subsection{Gaussian Processes}
\slides{
* Basis function models give non-linear predictions.
* Need to choose number and location of basis functions. 
* Gaussian processes is a general framework (basis functions special case)
* Within the framework you can consider models with infinite basis functions.
}
\notes{Models where we model the entire joint distribution of our training data, $p(\dataVector, \inputMatrix)$ are sometimes described as *generative models*. Because we can use sampling to generate data sets that represent all our assumptions. However, as we discussed in the sessions on \refnotes{logistic regression}{logistic-regression} and \refnotes{naive Bayes}{naive-bayes}, this can be a bad idea, because if our assumptions are wrong then we can make poor predictions. We can try to make more complex assumptions about data to alleviate the problem, but then this typically leads to challenges for tractable application of the sum and rules of probability that are needed to compute the relevant marginal and conditional densities. If we know the form of the question we wish to answer then we typically try and represent that directly, through $p(\dataVector|\inputMatrix)$.  In practice, we also have been making assumptions of conditional independence given the model parameters,}
$$
p(\dataVector|\inputMatrix, \mappingVector) =
\prod_{i=1}^{\numData} p(\dataScalar_i | \inputVector_i, \mappingVector)
$$
\notes{Gaussian processes are *not* normally considered to be *generative models*, but we will be much more interested in the principles of conditioning in Gaussian processes because we will use conditioning to make predictions between our test and training data. We will avoid the data conditional indpendence assumption in favour of a richer assumption about the data, in a Gaussian process we assume data is *jointly Gaussian* with a particular mean and covariance,}
$$
\dataVector|\inputMatrix \sim \gaussianSamp{\mathbf{m}(\inputMatrix)}{\kernelMatrix(\inputMatrix)},
$$
\notes{where the conditioning is on the inputs $\inputMatrix$ which are used for computing the mean and covariance. For this reason they are known as mean and covariance functions.}



\include{_ml/includes/linear-model-overview.md}

\include{_ml/includes/radial-basis.md}

\include{_gp/includes/gp-from-basis-functions.md}

\include{_gp/includes/non-degenerate-gps.md}
\include{_gp/includes/gp-function-space.md}

\include{_gp/includes/gptwopointpred.md}

\include{_gp/includes/gp-covariance-function-importance.md}
\include{_gp/includes/gp-numerics-and-optimization.md}

\include{_gp/includes/gp-optimize.md}
\include{_kern/includes/eq-covariance.md}
\include{_gp/includes/gp-summer-school.md}
\include{_gp/includes/gpy-software.md}
\include{_gp/includes/gpy-tutorial.md}

\subsection{Review}

\include{_gp/includes/other-gp-software.md}

\reading

\thanks

\references



