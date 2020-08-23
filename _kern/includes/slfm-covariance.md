\ifndef{slfmCovariance}
\define{slfmCovariance}

\editme

\subsection{Semi Parametric Latent Factor Covariance}

\define{formula}{\kernelScalar(i, j, \inputVector, \inputVector^\prime) = w_i w_j \kernelScalar(\inputVector, \inputVector^\prime)}

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
                    diagrams='\diagramsDir/kern', 
				    filename='slfm_covariance.html')}


\includecovariane{slfm}{\formula}{Semi-parametric latent factor model covariance function.}

\endif
