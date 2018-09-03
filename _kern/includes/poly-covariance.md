\loadcode{polynomial_cov}{mlai}
\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}
\plotcode{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=polynomial_cov, degree=4)}

\setupplotcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='polynomial_covariance.html')}


### Polynomial Covariance

$$k(\inputVector, \inputVector^\prime) = \alpha(w \inputVector^\top
\inputVector^\prime + b)^d$$

\columns{\includesvg{../slides/diagrams/kern/poly_covariance.svg}}{\includeimg{../slides/diagrams/kern/poly_covariance.gif}{100%}{negate}{center}}{45%}{45%}

<!--\columns{
\includesvg{../slides/diagrams/kern/polynomial_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/polynomial_covariance.html}{512}{384}
}{50%}{50%}-->

