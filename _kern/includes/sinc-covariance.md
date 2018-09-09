\subsection{Sinc Covariance}

\loadcode{sinc_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=sinc_cov,
                     name='Sinc',
                     shortname='sinc',					 
                     formula='\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \text{sinc}\left(\pi w r\right)',
					 w=2)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/kern/')}


$$\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \text{sinc}\left(\pi w r\right)$$

\columns{\includesvgclass{../slides/diagrams/kern/sinc_covariance.svg}}{\includeimg{../slides/diagrams/kern/sinc_covariance.gif}{100%}{negate}{center}}{45%}{45%}

