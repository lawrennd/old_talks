\setupcode{import numpy as np}

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


\code{%load -s compute_kernel mlai.py}

\code{%load -s polynomial_cov mlai.py}

\code{%load -s exponentiated_quadratic mlai.py}

\plotcode{plot.two_point_sample(compute_kernel, kernel=exponentiated_quadratic, 
                      lengthscale=0.5, diagrams='../slides/diagrams/gp')}

\plotcode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', 
                            '../slides/diagrams/gp', sample=(0,12))}
							
\slides{
### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample000.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample001.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample002.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample003.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample004.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample005.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample006.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample007.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample008.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample009.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample010.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample011.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample012.svg}

A 25 dimensional correlated random variable (values ploted against index)

}
### Uluru

\includeimg{../slides/diagrams/gp/799px-Uluru_Panorama.jpg}

## Prediction with Correlated Gaussians
  * Prediction of $\mappingFunction_2$ from $\mappingFunction_1$ requires *conditional density*.
  * Conditional density is *also* Gaussian.
    $$
    p(\mappingFunction_2|\mappingFunction_1) = \gaussianDist{\mappingFunction_2}{\frac{\kernelScalar_{1, 2}}{\kernelScalar_{1, 1}}\mappingFunction_1}{ \kernelScalar_{2, 2} - \frac{\kernelScalar_{1,2}^2}{\kernelScalar_{1,1}}}
    $$
    where covariance of joint density is given by
    $$
    \kernelMatrix = \begin{bmatrix} \kernelScalar_{1, 1} & \kernelScalar_{1, 2}\\ \kernelScalar_{2, 1} & \kernelScalar_{2, 2}\end{bmatrix}
    $$

\plotcode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', 
                            '../slides/diagrams/gp', sample=(13,16))}
							
\slides{
### Prediction of $\mappingFunction_{5}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample013.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{5}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample014.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{5}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample015.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{5}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample016.svg}

A 25 dimensional correlated random variable (values ploted against index)
}
