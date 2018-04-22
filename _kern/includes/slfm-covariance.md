\helpercode{%load -s icm_cov mlai.py}
\helpercode{%load -s slfm_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}


\code{plot.covariance_func(x, mlai.compute_kernel, 
                     formula = r'$$\kernelScalar(i, j, \inputVector, \inputVector^\prime) = w_i w_j \kernelScalar(\inputVector, \inputVector^\prime)$$', 
                     shortname='slfm', 
                     longname='Semi-parametric Latent Factor', 
					 kernel=slfm_cov,
                     subkernel=eq_cov,
					 W = np.asarray([[1, 5]]),
					 diagrams='../slides/diagrams/kern')}


### Slfm Covariance

$$\kernelScalar(i, j, \inputVector, \inputVector^\prime) = w_i w_j \kernelScalar(\inputVector, \inputVector^\prime)$$

\includehtml{../slides/diagrams/kern/slfm-covariance.html}

\columns{
\includesvg{../slides/diagrams/kern/slfm_covariance.svg}
}{
\includegif{../slides/diagrams/kern/brownian_covariance.gif}{80%}
}{50%}{50%}

