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

$$k(\inputVector, \inputVector^\prime) 
= \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\ell^2}\right)$$

\columns{
\includesvg{../slides/diagrams/kern/eq_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/eq_covariance.html}{512}{384}
}{50%}{50%}

