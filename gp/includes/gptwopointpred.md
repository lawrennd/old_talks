### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$

<small>
-   The single contour of the Gaussian density represents the
    <div class="redkey">joint distribution, $p(\mappingFunction_1, \mappingFunction_2)$</div>

. . .

-   We observe that
    <div class="greenkey">$\mappingFunction_1=?$</div>

. . .

-   Conditional density:
    <div class="redkey">$p(\mappingFunction_2|\mappingFunction_1=?)$</div>
</small>
	
### Prediction with Correlated Gaussians

-   Prediction of $\mappingFunction_2$ from $\mappingFunction_1$ requires *conditional density*.

-   Conditional density is *also* Gaussian.
    $$p(\mappingFunction_2|\mappingFunction_1) = {\mathcal{N}\left(\mappingFunction_2|\frac{\kernelScalar_{1, 2}}{\kernelScalar_{1, 1}}\mappingFunction_1,\kernelScalar_{2, 2} - \frac{\kernelScalar_{1,2}^2}{\kernelScalar_{1,1}}\right)}$$
    where covariance of joint density is given by
    $$\kernelMatrix= \begin{bmatrix} \kernelScalar_{1, 1} & \kernelScalar_{1, 2}\\ \kernelScalar_{2, 1} & \kernelScalar_{2, 2}\end{bmatrix}$$

### Prediction of $\mappingFunction_{5}$ from $\mappingFunction_{1}$ {data-transition="none"}

<object data="../gp/diagrams/two_point_sample014.svg" class="svgplot">
</object>

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{5}$ from $\mappingFunction_{1}$ {data-transition="none"}

<object data="../gp/diagrams/two_point_sample015.svg" class="svgplot">
</object>

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{5}$ from $\mappingFunction_{1}$ {data-transition="none"}

<object data="../gp/diagrams/two_point_sample016.svg" class="svgplot">
</object>

A 25 dimensional correlated random variable (values ploted against index)

### Details

-   The single contour of the Gaussian density represents the
    <div class="bluekey"> joint distribution, $p(\mappingFunction_1, \mappingFunction_5)$</div>

. . .

-   We observe a value for <div class="greenkey">$\mappingFunction_1=-?$</div>

. . .
	
-   Conditional density: <div class="redkey">$p(\mappingFunction_5|\mappingFunction_1=?$</div>.

### Prediction with Correlated Gaussians {#prediction-with-correlated-gaussians}

-   Prediction of $\mappingFunctionVector_*$ from $\mappingFunctionVector$ requires
    multivariate *conditional density*.

-   Multivariate conditional density is *also* Gaussian. 

<large>
    $$p(\mappingFunctionVector_*|\mappingFunctionVector) = {\mathcal{N}\left(\mappingFunctionVector_*|\kernelMatrix_{*,\mappingFunctionVector}\kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\mappingFunctionVector,\kernelMatrix_{*,*}-\kernelMatrix_{*,\mappingFunctionVector} \kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\kernelMatrix_{\mappingFunctionVector,*}\right)}$$</large>

-   Here covariance of joint density is given by
    $$\kernelMatrix= \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector} & \kernelMatrix_{*, \mappingFunctionVector}\\ \kernelMatrix_{\mappingFunctionVector, *} & \kernelMatrix_{*, *}\end{bmatrix}$$

### Prediction with Correlated Gaussians {#prediction-with-correlated-gaussians}

-   Prediction of $\mappingFunctionVector_*$ from $\mappingFunctionVector$ requires
    multivariate *conditional density*.

-   Multivariate conditional density is *also* Gaussian. 

<large>
$$p(\mappingFunctionVector_*|\mappingFunctionVector) = {\mathcal{N}\left(\mappingFunctionVector_*|{\boldsymbol{{\mu}}},\boldsymbol{\Sigma}\right)}$$
    $${\boldsymbol{{\mu}}}= \kernelMatrix_{*,\mappingFunctionVector}\kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\mappingFunctionVector$$
    $$\boldsymbol{\Sigma} = \kernelMatrix_{*,*}-\kernelMatrix_{*,\mappingFunctionVector} \kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\kernelMatrix_{\mappingFunctionVector,*}$$</large>

-   Here covariance of joint density is given by
    $$\kernelMatrix= \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector} & \kernelMatrix_{*, \mappingFunctionVector}\\ \kernelMatrix_{\mappingFunctionVector, *} & \kernelMatrix_{*, *}\end{bmatrix}$$

<!--frame end-->

