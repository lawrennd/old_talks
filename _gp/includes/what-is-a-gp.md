<!-- Introduction to GPs -->

\include{../../_ml/includes/what-is-ml.md}

### Artificial Intelligence {data-transition="none"}

* Machine learning is a mainstay because of importance of prediction.

### What is Machine Learning? {data-transition="none"}

\slidenotes{
$$\text{data} + \text{model} \rightarrow \text{prediction}$$

. . .

* To combine data with a model need:

. . .

* **a prediction function** $\mappingFunction(\cdot)$ includes our beliefs about the regularities of the universe

. . .

* **an objective function** $\errorFunction(\cdot)$ defines the cost of misprediction.
}{
So how do Gaussian processes come in? Well in practice we normally perform machine learning using two functions. To combine data with a model we typically make use of:

**a prediction function** a function which is used to make the predictions. It includes our beliefs about the regularities of the universe, our assumptions about how the world works, e.g. smoothness, spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of misprediction. Typically it includes knowledge about the world's generating processes (probabilistic objectives) or the costs we pay for mispredictions (empiricial risk minimization).
}

### Uncertainty {data-transition="none"}

\slidenotes{
* Uncertainty in prediction arises from:

* scarcity of training data and 

* mismatch between the set of prediction functions we choose and all possible prediction functions.

* Also uncertainties in objective, leave those for another day.
}{
In practice, we normally also have uncertainty associated with these functions. Uncertainty in the prediction function arises from 

1. scarcity of training data and 
2. mismatch between the set of prediction functions we choose and all possible prediction functions.

There are also challenges around specification of the objective function, but for we will save those for another day. For the moment, let us focus on the prediction function. 
}

\include{../../_ml/includes/neural-networks.md}
\include{../../_ml/includes/probabilistic-modelling.md}
\include{../../_ml/includes/graphical-models.md}
\include{../../_ml/includes/performing-inference.md}

### Multivariate Gaussian Properties {data-transition="none"}

\include{../../_gp/includes/multivariate_gaussian_properties.md}
\include{../../_ml/includes/multivariate-gaussian-properties.md}
\include{../../_gp/includes/non-degenerate-gps.md}
\include{../../_gp/includes/gp-intro-very-short.md}

<!-- ### Two Dimensional Gaussian Distribution -->

<!-- include{../../_ml/includes/two_d_gaussian.md} -->

### Distributions over Functions {data-transition="none"}

\include{../../_gp/includes/gpdistfunc.md}

###  Key Object {data-transition="none"}

* Covariance function, $\kernelMatrix$

* Determines properties of samples.

* Function of $\inputMatrix$,
    $$\kernelScalar_{i,j} = \kernelScalar(\inputVector_i, \inputVector_j)$$

###  Linear Algebra {data-transition="none"}

* Posterior mean

    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \kernelMatrix^{-1}
\mathbf{y}$$

* Posterior covariance
    $$\mathbf{C}_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

###  Linear Algebra {data-transition="none"}

* Posterior mean

    $$\mappingFunction_D(\inputVector_*) = \kernelVector(\inputVector_*, \inputMatrix) \boldsymbol{\alpha}$$

* Posterior covariance
    $$\covarianceMatrix_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mappingFunctionVector}
\kernelMatrix^{-1} \kernelMatrix_{\mappingFunctionVector, *}$$

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp_prior_samples_data.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp_rejection_samples.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp_prediction.svg}


\include{../../_kern/includes/eq-covariance.md}

include{../../_gp/includes/olympic-marathon-gp.md}

\include{../../_kern/includes/basis-covariance.md}

\include{../../_kern/includes/brownian-covariance.md}

\include{../../_kern/includes/mlp-covariance.md}

### {data-transition="none"}

\includeimg{../slides/diagrams/Planck_CMB.png}{70%}

### {data-transition="none"}

<div style="fontsize:120px;vertical-align:middle;"><img src="../slides/diagrams/earth_PNG37.png" width="20%" style="display:inline-block;background:none;vertical-align:middle;border:none;box-shadow:none;">$=f\Bigg($
<img src="../slides/diagrams/Planck_CMB.png"  width="50%" style="display:inline-block;background:none;vertical-align:middle;border:none;box-shadow:none;">$\Bigg)$</div>
