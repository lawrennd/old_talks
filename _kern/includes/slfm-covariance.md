\helpercode{%load -s icm_cov mlai.py}
\helpercode{%load -s slfm_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}

\code{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=slfm_cov, subkernel=eq_cov,
										 W = np.asarray([[1],[5]])}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='slfm_covariance.html')}


### Semi Parametric Latent Factor Covariance

$$\kernelScalar(i, j, \inputVector, \inputVector^\prime) = w_i w_j \kernelScalar(\inputVector, \inputVector^\prime)$$

\columns{
\includesvg{../slides/diagrams/kern/slfm_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/slfm_covariance.html}{512}{384}
}{50%}{50%}

