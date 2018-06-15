\include{_ml/includes/what-is-ml.md}

### Artificial Intelligence
\slides{
* Machine learning is a mainstay because of importance of prediction.
}
\notes{
}

### Uncertainty

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

### Multivariate Gaussian Properties

\include{_ml/includes/multivariate-gaussian-properties-summary.md}

\slides{
### Linear Gaussian Models
}\notes{Gaussian processes are initially of interest because}

1. linear Gaussian models are easier to deal with 
2. Even the parameters *within* the process can be handled, by considering a particular limit.

\include{_ml/includes/multivariate-gaussian-properties.md}
\include{_gp/includes/non-degenerate-gps.md}
\include{_gp/includes/gp-intro-very-short.md}

<!-- ### Two Dimensional Gaussian Distribution -->

<!-- include{_ml/includes/two-d-gaussian.md} -->

### Distributions over Functions

\include{_gp/includes/gpdistfunc.md}

###  Key Object

* Covariance function, $\kernelMatrix$

* Determines properties of samples.

* Function of $\inputMatrix$,
    $$\kernelScalar_{i,j} = \kernelScalar(\inputVector_i, \inputVector_j)$$

###  Linear Algebra

* Posterior mean

    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \kernelMatrix^{-1}
\mathbf{y}$$

* Posterior covariance
    $$\mathbf{C}_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

###  Linear Algebra

* Posterior mean

    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \boldsymbol{\alpha}$$

* Posterior covariance
    $$\covarianceMatrix_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

### 

\includesvg{../slides/diagrams/gp_prior_samples_data.svg}

### 

\includesvg{../slides/diagrams/gp_rejection_samples.svg}

### 

\includesvg{../slides/diagrams/gp_prediction.svg}


\include{_kern/includes/eq-covariance.md}

\include{_gp/includes/olympic-marathon-gp.md}

\include{_kern/includes/basis-covariance.md}

\include{_kern/includes/brownian-covariance.md}

\include{_kern/includes/mlp-covariance.md}

\include{_gp/includes/planck-cmp-master-gp.md}

