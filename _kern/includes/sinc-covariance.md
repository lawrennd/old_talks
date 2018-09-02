\helpercode{%load -s sinc_cov mlai.py}
\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}
\plotcode{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=sinc_cov)}

\setupplotcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='sinc_covariance.html')}


\newslide{Sinc Covariance}

$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \text{sinc}\left(\frac{r}{\lengthScale}\right)$$

\columns{
\includesvg{../slides/diagrams/kern/sinc_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/sinc_covariance.html}{512}{384}
}{50%}{50%}

