\ifndef{reluCovariance}
\define{reluCovariance}

\editme

\subsection{RELU Covariance}

\loadcode{relu_cov}{mlai}

\define{formula}{\kernelScalar(\inputVector, \inputVector^\prime) = 
\alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}
{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)
\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)}


\setupplotcode{import mlai.plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=relu_cov,
                     name='RELU',
                     shortname='relu',					 
                     formula='\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)',
					 w=5, b=0.5)
					 
plot.covariance_func(kernel, diagrams='\writeDiagramsDir/kern/')}

\includecovariance{relu}{\formula}{Rectified linear unit covariance function.}


\endif
