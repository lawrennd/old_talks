\subsection{RELU Covariance}

\loadcode{relu_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=relu_cov,
                     name='RELU',
                     shortname='relu',					 
                     formula='\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)',
					 w=5, b=0.5)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/kern/')}


$$\kernelScalar(\inputVector, \inputVector^\prime) = 
\alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}
{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)
\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)$$

\columns{\includesvgclass{../slides/diagrams/kern/relu_covariance.svg}}{\includeimg{../slides/diagrams/kern/relu_covariance.gif}{100%}{negate}{center}}{45%}{45%}

