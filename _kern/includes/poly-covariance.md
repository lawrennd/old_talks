\subsection{Polynomial Covariance}

\loadplotcode{polynomial_cov}{mlai}
\define{\formula}{\kernelScalar(\inputVector, \inputVector^\prime) = \alpha(w \inputVector^\top\inputVector^\prime + b)^d}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=polynomial_cov,
                     name='Polynomial',
                     shortname='polynomial',					 
                     formula='\formula',
					 degree=5)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/kern/')}

\includecovariance{polynomial}{\formula}

