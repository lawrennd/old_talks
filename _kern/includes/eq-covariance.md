\helpercode{%load -s eq_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}


\code{plot.covariance_func(x, mlai.compute_kernel, 
                     formula = r'$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\lengthScale^2}\right)$$', 
                     shortname='eq', 
                     longname='Exponentiated Quadratic', 
					 kernel=eq_cov,
                     lengthscale=0.2., 
					 diagrams='../slides/diagrams/kern')}



### Exponentiated Quadratic Covariance {data-transition="none"}

$$k(\inputVector, \inputVector^\prime) 
= \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\ell^2}\right)$$

\includehtml{../slides/diagrams/kern/eq_covariance.html}
