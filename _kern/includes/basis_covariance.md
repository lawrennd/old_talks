\subsection{Basis Function Covariance}

\loadcode{basis_cov}{mlai}

\loadcode{radial}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{basis=mlai.Basis(function=radial, num_basis=3, data_limits=[-0.5, 0.5], width=0.25)
kernel = mlai.Kernel(function=basis_cov,
                     name='Basis Function',
                     shortname='basis',					 
                     formula='\kernelScalar(\inputVector, \inputVector^\prime) = \basisVector(\inputVector)^\top\basisVector(\inputVector^\prime)',
					 basis=basis)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/')}

$$k(\inputVector, \inputVector^\prime) = \alpha(w \inputVector^\top
\inputVector^\prime + b)^d$$

\columns{\includesvgclass{../slides/diagrams/kern/basis_covariance.svg}}{\includeimg{../slides/diagrams/kern/basis_covariance.gif}{100%}{negate}{center}}{45%}{45%}
