\subsection{Periodic Covariance}

\define{\formula}{\kernelScalar(\inputVector, \inputVector^\prime) = \alpha\exp\left(\frac{-2\sin(\pi rw)^2}{\lengthScale^2}\right)}

\loadplotcode{periodic_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=periodic_cov,
                     name='Periodic',
                     shortname='periodic',					 
                     formula='\formula',
					 lengthscale=1.0)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/kern/')}

\includecovariance{periodic}{\formula}
