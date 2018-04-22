\helpercode{%load -s periodic_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}
\code{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=periodic_cov, lengthscale=0.2)}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='periodic_covariance.html')}


### Periodic Covariance

$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha\exp\left(\frac{-2\sin(\pi rw)^2}{\lengthScale^2}\right)$$

\columns{
\includesvg{../slides/diagrams/kern/periodic_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/periodic_covariance.html}{512}{384}
}{50%}{50%}

