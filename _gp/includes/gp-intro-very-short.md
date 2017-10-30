
###  {data-transition="none"}

<object class="svgplot" data="../_gp/diagrams/gp_prior_samples_few.svg">
</object>

###  {data-transition="none"}

<object class="svgplot" data="../_gp/diagrams/gp_prior_samples.svg">
</object>

###  {data-transition="none"}

<object class="svgplot" data="../_gp/diagrams/gp_prior_samples_data.svg">
</object>

###  {data-transition="none"}

<object class="svgplot" data="../_gp/diagrams/gp_rejection_samples.svg">
</object>

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

<object class="svgplot" data="../_gp/diagrams/gp_prior_samples_data.svg">
</object>

###  {data-transition="none"}

<object class="svgplot" data="../_gp/diagrams/gp_rejection_samples.svg">
</object>

###  {data-transition="none"}

<object class="svgplot" data="../_gp/diagrams/gp_prediction.svg">
</object>
