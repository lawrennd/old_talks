\ifndef{polynomialBasis}
\define{polynomialBasis}
\editme

\subsection{Polynomial Basis}

\setupcode{import matplotlib.pyplot as plt
import mlai
import teaching_plots as plot}

\loadcode{polynomial}{mlai}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = x$',
       '$\phi(x) = x^2$']

plot.basis(mlai.polynomial, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text,
		   diagrams='../slides/diagrams/ml')
}

\subsection{Functions Derived from Polynomial Basis}

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 \inputScalar} + {\color{yellow}\mappingScalar_2 \inputScalar^2}
$$

\slides{
\startanimation{polynomial_basis}{1}{3}
\newframe{\includediagram{../slides/diagrams/ml/polynomial_basis001}}{polynomial_basis}
\newframe{\includediagram{../slides/diagrams/ml/polynomial_basis002}}{polynomial_basis}
\newframe{\includediagram{../slides/diagrams/ml/polynomial_basis003}}{polynomial_basis}
\endanimation
}
\notes{\figure{\includediagram{../slides/diagrams/ml/polynomial_basis003}{80%}}{A polynomial basis is made up of different degrees of polynomial.}{polynomial-basis-3}}

\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('polynomial_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1,1,4,1))}

\endif
