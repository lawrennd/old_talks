\subsection{Polynomial Covariance}

\loadcode{polynomial_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=polynomial_cov,
                     name='Polynomial',
                     shortname='polynomial',					 
                     formula='k(\inputVector, \inputVector^\prime) = \alpha(w \inputVector^\top\inputVector^\prime + b)^d',
					 degree=5)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/')}

$$k(\inputVector, \inputVector^\prime) = \alpha(w \inputVector^\top
\inputVector^\prime + b)^d$$

\columns{\includesvgclass{../slides/diagrams/kern/polynomial_covariance.svg}}{\includeimg{../slides/diagrams/kern/polynomial_covariance.gif}{100%}{negate}{center}}{45%}{45%}

<!--\columns{
\includesvg{../slides/diagrams/kern/polynomial_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/polynomial_covariance.html}{512}{384}
}{50%}{50%}-->

