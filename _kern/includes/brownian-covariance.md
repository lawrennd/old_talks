\helpercode{%load -s brownian_cov mlai.py}
\setupcode{import teaching_plots as plot}
\setupcode{import numpy as np}


\code{x=np.linspace(0, 2, 30)[:, np.newaxis]
plot.covariance_func(x, mlai.compute_kernel, 
                     formula = r'$$\kernelScalar(t, t^\prime) = \alpha \min(t, t^\prime)$$', 
                     shortname='brownian', 
                     longname='Brownian', 
					 kernel=brownian_cov,
                     degree=4., 
					 diagrams='../slides/diagrams/kern')}


### Brownian Covariance

$$\kernelScalar(t, t^\prime) = \alpha \min(t, t^\prime)$$

\columns{
\includesvg{../slides/diagrams/kern/brownian_covariance.svg}
}{
\includegif{../slides/diagrams/kern/brownian_covariance.gif}{80%}
}{50%}{50%}

