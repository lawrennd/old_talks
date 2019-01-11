\include{_ml/includes/what-is-ml.md}

\newslide{Artificial Intelligence}
\slides{
* Machine learning is a mainstay because of importance of prediction.
}

\newslide{Uncertainty}

\slides{
* Uncertainty in prediction arises from:
* scarcity of training data and 
* mismatch between the set of prediction functions we choose and all possible prediction functions.
* Also uncertainties in objective, leave those for another day.
}
\notes{
In practice, we normally also have uncertainty associated with these functions. Uncertainty in the prediction function arises from 

1. scarcity of training data and 
2. mismatch between the set of prediction functions we choose and all possible prediction functions.

There are also challenges around specification of the objective function, but for we will save those for another day. For the moment, let us focus on the prediction function. 
}

\include{_ml/includes/neural-networks.md}
\include{_ml/includes/probabilistic-modelling.md}
\include{_ml/includes/graphical-models.md}
\include{_ml/includes/performing-inference.md}

\newslide{Multivariate Gaussian Properties}

\include{_ml/includes/multivariate-gaussian-properties-summary.md}

\slides{
\newslide{Linear Gaussian Models}
}\notes{Gaussian processes are initially of interest because}

1. linear Gaussian models are easier to deal with 
2. Even the parameters *within* the process can be handled, by considering a particular limit.

\include{_ml/includes/multivariate-gaussian-properties.md}
\include{_gp/includes/non-degenerate-gps.md}
\include{_gp/includes/gp-intro-very-short.md}

<!-- ### Two Dimensional Gaussian Distribution -->

<!-- include{_ml/includes/two-d-gaussian.md} -->

\newslide{Distributions over Functions}

\include{_gp/includes/gpdistfunc.md}

\newslide{Key Object}

* Covariance function, $\kernelMatrix$
* Determines properties of samples.
* Function of $\inputMatrix$,
    $$\kernelScalar_{i,j} = \kernelScalar(\inputVector_i, \inputVector_j)$$

\newslide{Linear Algebra}

* Posterior mean
    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \kernelMatrix^{-1}
\mathbf{y}$$

* Posterior covariance
    $$\mathbf{C}_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

\newslide{Linear Algebra}

* Posterior mean

    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \boldsymbol{\alpha}$$

* Posterior covariance
    $$\covarianceMatrix_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

\slides{
\newslide{}

\includepng{../slides/diagrams/gp/gp_rejection_sample001}{100%}{negate}

\newslide{}

\includepng{../slides/diagrams/gp/gp_rejection_sample002}{100%}{negate}

\newslide{}

\includepng{../slides/diagrams/gp/gp_rejection_sample003}{100%}{negate}

\newslide{}

\includepng{../slides/diagrams/gp/gp_rejection_sample004}{100%}{negate}

\newslide{} 

\includepng{../slides/diagrams/gp/gp_rejection_sample005}{100%}{negate}
}



\include{_kern/includes/eq-covariance.md}

\include{_gp/includes/olympic-marathon-gp.md}
\include{_gp/includes/gp-optimize.md}

\include{_gp/includes/della-gatta-gene-gp.md}
\include{_health/includes/malaria-gp.md}

\include{_kern/includes/add-covariance.md}
\include{_gp/includes/bda-forecasting.md}

\include{_kern/includes/basis-covariance.md}

\include{_kern/includes/brownian-covariance.md}

\include{_kern/includes/mlp-covariance.md}

