\ifndef{icmCovariance}
\define{icmCovariance}
\editme

\subsection{Intrinsic Coregionalization Model Covariance}

\define{formula}{\kernelScalar(i, j, \inputVector, \inputVector^\prime) = b_{i,j} \kernelScalar(\inputVector, \inputVector^\prime)}

\helpercode{%load -s icm_cov mlai.py}
\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=icm_cov, subkernel=eq_cov,
										 B = np.asarray([[1, 0.5],[0.5, 1.5]]))}

\setupdisplaycode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\displaycode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='icm_covariance.html')}


\includecovariance{icm}{\formula}{Intrinsic coregionalization model covariance function.}

\endif
