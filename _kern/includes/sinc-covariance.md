\helpercode{%load -s sinc_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}
\code{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=sinc_cov, lengthscale=0.2)}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='sinc_covariance.html')}


### Sinc Covariance

$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha\sinc\left(\frac{r}{\lengthScale}\right)$$

\columns{
\includesvg{../slides/diagrams/kern/sinc_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/sinc_covariance.html}{512}{384}
}{50%}{50%}

