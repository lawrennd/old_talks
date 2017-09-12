
###  {data-transition="none"}

<object type="image/svg+xml" data="../gp/diagrams/gp_prior_samples_few_neg.svg">
</object>

###  {data-transition="none"}

<object type="image/svg+xml" data="../gp/diagrams/gp_prior_samples_neg.svg">
</object>

###  {data-transition="none"}

<object type="image/svg+xml" data="../gp/diagrams/gp_prior_samples_data_neg.svg">
</object>

###  {data-transition="none"}

<object type="image/svg+xml" data="../gp/diagrams/gp_rejection_samples_neg.svg">
</object>

###  Key Object {data-transition="none"}

* Covariance function, $\kernelMatrix$

* Determines properties of samples.

* Function of $\inputMatrix$,
    $$k_{i,j} = k(\mathbf{x}_i, \mathbf{x}_j)$$

###  Linear Algebra {data-transition="none"}

* Posterior mean

    $$f_D(\mathbf{x_*}) = \mathbf{k}(\mathbf{x}_*, \inputMatrix) \kernelMatrix^{-1}
\mathbf{y}$$

* Posterior covariance
    $$\mathbf{C}_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mathbf{f}}
\kernelMatrix^{-1} \kernelMatrix_{\mathbf{f}, *}$$

###  Linear Algebra {data-transition="none"}

* Posterior mean

    $$f_D(\mathbf{x_*}) = \mathbf{k}(\mathbf{x}_*, \inputMatrix) \boldsymbol{\alpha}$$

* Posterior covariance
    $$\mathbf{C}_* = \kernelMatrix_{*,*} - \kernelMatrix_{*,\mathbf{f}}
\kernelMatrix^{-1} \kernelMatrix_{\mathbf{f}, *}$$

###  {data-transition="none"}

<object type="image/svg+xml" data="../gp/diagrams/gp_prior_samples_data_neg.svg">
</object>

###  {data-transition="none"}

<object type="image/svg+xml" data="../gp/diagrams/gp_rejection_samples_neg.svg">
</object>

###  {data-transition="none"}

<object type="image/svg+xml" data="../gp/diagrams/gp_prediction_neg.svg">
</object>
