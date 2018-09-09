\subsection{Periodic Covariance}

\loadcode{periodic_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=periodic_cov,
                     name='Periodic',
                     shortname='periodic',					 
                     formula='\kernelScalar(\inputVector, \inputVector^\prime) = \alpha\exp\left(\frac{-2\sin(\pi rw)^2}{\lengthScale^2}\right)',
					 lengthscale=1.0)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/kern/')}

$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha\exp\left(\frac{-2\sin(\pi rw)^2}{\lengthScale^2}\right)$$

<!--\columns{
\includesvg{../slides/diagrams/kern/periodic_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/periodic_covariance.html}{512}{384}
}{50%}{50%}-->

\columns{\includesvgclass{../slides/diagrams/kern/periodic_covariance.svg}}{\includeimg{../slides/diagrams/kern/periodic_covariance.gif}{100%}{negate}{center}}{45%}{45%}
