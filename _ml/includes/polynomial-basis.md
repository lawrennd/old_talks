\ifndef{polynomialBasis}
\define{polynomialBasis}
\editme

\subsection{Polynomial Basis}

\slides{* }
\notes{The polynomial basis combines higher order polynomials together to create the function. For example the fourth order polynomial has five components to its basis function.}
$$
\basisFunc_j(\inputScalar) = \inputScalar^j
$$

\setupcode{import numpy as np}
\loadcode{polynomial}{mlai}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import teaching_plots as plot}


\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2],
     [-0.75, -0.2],
     [-0.75, 2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = x$',
       '$\phi(x) = x^2$',
       '$\phi(x) = x^3$',
       '$\phi(x) = x^4$']

plot.basis(mlai.polynomial, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text, num_basis=5,
		   diagrams='\writeDiagramsDir/ml')}

\define{\basisfunction}{polynomial_basis}
\slides{
\define{\width}{80%}
\startanimation{\basisfunction}{0}{4}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{000}}{\width}}{\basisfunction}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{001}}{\width}}{\basisfunction}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{002}}{\width}}{\basisfunction}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{003}}{\width}}{\basisfunction}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{004}}{\width}}{\basisfunction}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{004}}{80%}}{The set of functions which are combined to form a *polynomial* basis.}{polynomial-basis-2}}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}

\displaycode{pods.notebook.display_plots('polynomial_basis{num_basis:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							num_basis=IntSlider(0,0,4,1))}

\displaycode{pods.notebook.display_prediction(basis=mlai.polynomial, num_basis=5)}

\subsection{Functions Derived from Polynomial Basis}

$$
\mappingFunction(\inputScalar) = {\color{\redColor}{\mappingScalar_0}} + {\color{\magentaColor}{\mappingScalar_1 \inputScalar}} + {\color{\blueColor}{\mappingScalar_2 \inputScalar^2}} + {\color{\greenColor}{\mappingScalar_3 \inputScalar^3}} + {\color{\cyanColor}{\mappingScalar_4 \inputScalar^4}}
$$

\slides{
\define{width}{80%}
\startanimation{polynomial_function}{0}{3}
\newframe{\includediagram{\diagramsDir/ml/polynomial_function000}{\width}}{polynomial_function}
\newframe{\includediagram{\diagramsDir/ml/polynomial_function001}{\width}}{polynomial_function}
\newframe{\includediagram{\diagramsDir/ml/polynomial_function002}{\width}}{polynomial_function}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/polynomial_function002}{80%}}{A random combination of functions from the polynomial basis.}{polynomial-function-2}}

\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('polynomial_function{func_num:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
                            func_num=IntSlider(0,0,2,1))}



\endif
