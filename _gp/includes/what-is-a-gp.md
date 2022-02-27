\ifndef{whatIsAGp}
\define{whatIsAGp}
\editme

talk-macros.gpp}l/includes/what-is-ml.md}

\newslide{Artificial Intelligence}
\slides{
* Machine learning is a mainstay because of importance of prediction.
}

talk-macros.gpp}l/includes/why-uncertainty.md}
talk-macros.gpp}l/includes/neural-networks.md}
talk-macros.gpp}l/includes/integrated-basis-functions.md}



talk-macros.gpp}l/includes/probabilistic-modelling.md}
talk-macros.gpp}l/includes/graphical-models.md}
talk-macros.gpp}l/includes/performing-inference.md}

\newslide{Multivariate Gaussian Properties}

talk-macros.gpp}l/includes/multivariate-gaussian-properties-summary.md}

\slides{
\newslide{Linear Gaussian Models}
}\notes{Gaussian processes are initially of interest because}

1. linear Gaussian models are easier to deal with 
2. Even the parameters *within* the process can be handled, by considering a particular limit.

talk-macros.gpp}l/includes/multivariate-gaussian-properties.md}
talk-macros.gpp}l/includes/linear-model-overview.md}
talk-macros.gpp}p/includes/non-degenerate-gps.md}
talk-macros.gpp}p/includes/gp-intro-very-short.md}

<!-- ### Two Dimensional Gaussian Distribution -->

<!-- include{_ml/includes/two-d-gaussian.md} -->

\newslide{Distributions over Functions}

talk-macros.gpp}p/includes/gpdistfunc.md}

\newslide{Key Object}

* Covariance function, $\kernelMatrix$
* Determines properties of samples.
* Function of $\inputMatrix$,
    $$\kernelScalar_{i,j} = \kernelScalar(\inputVector_i, \inputVector_j)$$

\newslide{Linear Algebra}

* Posterior mean
    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \kernelMatrix^{-1}
\dataVector$$

* Posterior covariance
    $$\mathbf{C}_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

\newslide{Linear Algebra}

* Posterior mean

    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \boldsymbol{\alpha}$$

* Posterior covariance
    $$\covarianceMatrix_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

talk-macros.gpp}p/includes/gp-intro-very-short.md}

talk-macros.gpp}ern/includes/eq-covariance.md}

talk-macros.gpp}p/includes/olympic-marathon-gp.md}
talk-macros.gpp}p/includes/gp-optimize.md}

talk-macros.gpp}p/includes/della-gatta-gene-gp.md}
talk-macros.gpp}ealth/includes/malaria-gp.md}

talk-macros.gpp}ern/includes/add-covariance.md}
talk-macros.gpp}p/includes/bda-forecasting.md}

talk-macros.gpp}ern/includes/basis-covariance.md}
talk-macros.gpp}ern/includes/brownian-covariance.md}
talk-macros.gpp}ern/includes/mlp-covariance.md}
talk-macros.gpp}ern/includes/relu-covariance.md}
talk-macros.gpp}ern/includes/sinc-covariance.md}
talk-macros.gpp}ern/includes/poly-covariance.md}
talk-macros.gpp}ern/includes/periodic-covariance.md}
talk-macros.gpp}ern/includes/lmc-covariance.md}
talk-macros.gpp}ern/includes/icm-covariance.md}

\endif
