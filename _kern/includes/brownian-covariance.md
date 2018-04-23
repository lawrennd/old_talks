\helpercode{%load -s brownian_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}
\code{t=np.linspace(0, 2, 200)[:, np.newaxis]
K, anim=plot.animate_covariance_function(mlai.compute_kernel, t, 
                                         kernel=brownian_cov)}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='brownian_covariance.html')}


### Brownian Covariance

$$\kernelScalar(t, t^\prime) = \alpha \min(t, t^\prime)$$

\columns{
\includesvg{../slides/diagrams/kern/brownian_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/brownian_covariance.html}{512}{384}
}{50%}{50%}

