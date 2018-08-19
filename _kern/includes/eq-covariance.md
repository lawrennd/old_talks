\helpercode{%load -s eq_cov mlai.py}

\setupcode{import teaching_plots as plot
import mlai
import numpy as np}

\code{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=eq_cov, lengthscale=0.2)}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='eq_covariance.html')}


### Exponentiated Quadratic Covariance

\notes{The exponentiated quadratic covariance, also known as the Gaussian covariance or the RBF covariance and the squared exponential. Covariance between two points is related to the negative exponential of the squared distnace between those points. This covariance function can be derived in a few different ways: as the infinite limit of a radial basis function neural network, as diffusion in the heat equation, as a Gaussian filter in *Fourier space* or as the composition as a series of linear filters applied to a base function.

The covariance takes the following form,}
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\ell^2}\right)
$$
\notes{where $\ell$ is the *length scale* or *time scale* of the process and $\alpha$ represents the overall process variance.}
\columns{
\includesvg{../slides/diagrams/kern/eq_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/eq_covariance.html}{512}{384}
}{50%}{50%}

