\helpercode{%load -s eq_cov mlai.py}
\setupcode{import teaching_plots as plot}
\setupcode{import numpy as np}


\code{x=np.linspace(0, 2, 30)[:, np.newaxis]
plot.covariance_func(x, mlai.compute_kernel, 
                     formula = r'$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\lengthScale^2}\right)$$', 
                     shortname='eq', 
                     longname='Brownian', 
					 kernel=eq_cov,
                     lengthscale=1., 
					 diagrams='../slides/diagrams/kern')}



### Exponentiated Quadratic Covariance {data-transition="none"}

$$k(\inputVector, \inputVector^\prime) 
= \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\ell^2}\right)$$

\includehtml{../slides/diagrams/kern/eq_covariance.html}
