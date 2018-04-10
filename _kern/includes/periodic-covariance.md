\helpercode{%load -s periodic_cov mlai.py}
\setupcode{import teaching_plots as plot}
\setupcode{import numpy as np}

\code{x=np.linspace(-1, 1, 30)[:, np.newaxis]
plot.covariance_func(x, mlai.compute_kernel, 
                     formula = r'$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha\exp\left(\frac{-2}{\lengthScale^2}*\sin(\pi*rw)^2\right)$$', 
                     shortname='periodic', 
                     longname='Periodic', 
					 kernel=periodic_cov,
                     degree=4., 
					 diagrams='../slides/diagrams/kern')}


### Periodic Covariance

$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha\exp\left(\frac{-2}{\lengthScale^2}*\sin(\pi*rw)^2\right)$$

\columns{
\includesvg{../slides/diagrams/kern/periodic_covariance.svg}
}{
\includegif{../slides/diagrams/kern/periodic_covariance.gif}{80%}
}{50%}{50%}

