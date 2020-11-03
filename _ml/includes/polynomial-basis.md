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
       '$\phi(x) = x^2$'
       '$\phi(x) = x^3$',
       '$\phi(x) = x^4$']

plot.basis(mlai.polynomial, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text, num_basis=5,
		   diagrams='\writeDiagramsDir/ml')
}

\subsection{Functions Derived from Polynomial Basis}

$$
\mappingFunction(\inputScalar) = {\color{\redColor}{mappingScalar_0}} + {\color{\magentaColor}{\mappingScalar_1 \inputScalar}} + {\color{\blueColor}{\mappingScalar_2 \inputScalar^2}} + {\color{\greenColor}{\mappingScalar_3 \inputScalar^3}} + {\color{\cyanColor}{\mappingScalar_4 \inputScalar^4}}
$$

\slides{
\define{width}{80%}
\startanimation{polynomial_basis}{0}{4}
\newframe{\includediagram{\diagramsDir/ml/polynomial_basis000}{\width}}{polynomial_basis}
\newframe{\includediagram{\diagramsDir/ml/polynomial_basis001}{\width}}{polynomial_basis}
\newframe{\includediagram{\diagramsDir/ml/polynomial_basis002}{\width}}{polynomial_basis}
\newframe{\includediagram{\diagramsDir/ml/polynomial_basis003}{\width}}{polynomial_basis}
\newframe{\includediagram{\diagramsDir/ml/polynomial_basis004}{\width}}{polynomial_basis}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/ml/polynomial_basis004}{80%}}{A polynomial basis is made up of different degrees of polynomial.}{polynomial-basis-4}}

\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('polynomial_basis{num_basis:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
			    num_basis=IntSlider(1,1,5,1))}

\endif
