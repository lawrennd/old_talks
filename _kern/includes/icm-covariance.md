\helpercode{%load -s icm_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}

\code{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=icm_cov, subkernel=eq_cov,
										 B = np.asarray([[1, 0.5],[0.5, 1.5]]))}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='icm_covariance.html')}


### Intrinsic Coregionalization Model Covariance

$$\kernelScalar(i, j, \inputVector, \inputVector^\prime) = b_{i,j} \kernelScalar(\inputVector, \inputVector^\prime)$$

\columns{
\includesvg{../slides/diagrams/kern/icm_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/icm_covariance.html}{512}{384}
}{50%}{50%}

