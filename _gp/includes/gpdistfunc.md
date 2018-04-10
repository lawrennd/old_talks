\setupcode{import numpy as np
np.random.seed(4949)}

\setupcode{import teaching_plots as plot
import pods}

### Sampling a Function  {data-transition="none"}

**Multi-variate Gaussians**

-   We will consider a Gaussian with a particular structure of
    covariance matrix.

-   Generate a single sample from this 25 dimensional Gaussian
    distribution,
    $\mappingFunctionVector=\left[\mappingFunction_{1},\mappingFunction_{2}\dots \mappingFunction_{25}\right]$.

-   We will plot these points against their index.


\include{./_gp/includes/gaussian-predict-index-one-and-two.md}

### Uluru

\includeimg{../slides/diagrams/gp/799px-Uluru_Panorama.jpg}

### Prediction with Correlated Gaussians

* Prediction of $\mappingFunction_2$ from $\mappingFunction_1$ requires *conditional density*.

* Conditional density is *also* Gaussian.
    $$
    p(\mappingFunction_2|\mappingFunction_1) = \gaussianDist{\mappingFunction_2}{\frac{\kernelScalar_{1, 2}}{\kernelScalar_{1, 1}}\mappingFunction_1}{ \kernelScalar_{2, 2} - \frac{\kernelScalar_{1,2}^2}{\kernelScalar_{1,1}}}
    $$
    where covariance of joint density is given by
    $$
    \kernelMatrix = \begin{bmatrix} \kernelScalar_{1, 1} & \kernelScalar_{1, 2}\\ \kernelScalar_{2, 1} & \kernelScalar_{2, 2}\end{bmatrix}
    $$

\include{./_gp/includes/gaussian-predict-index-one-and-eight.md}
