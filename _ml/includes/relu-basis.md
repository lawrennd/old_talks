\ifndef{reluBasis}
\define{reluBasis}
\editme

\subsection{Rectified Linear Units}

\slides{* }
\notes{The rectified linear unit is a basis function that emerged out of the deep learning community. Rectified linear units are popular in the current generation of multilayer perceptron models, or deep networks. These basis functions start flat, and then become linear functions at a certain threshold.}
$$
\basisFunc_j(\inputScalar) = \inputScalar\heaviside(\mappingScalarTwo_j \inputScalar + \mappingScalarTwo_0)
$$

\setupcode{import numpy as np}
\loadcode{relu}{mlai}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [-1, -0.5],
      [-0.33, 0.2],
      [0.33, -0.5],
      [1, 0.2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = xH(x+1.0)$',
       '$\phi(x) = xH(x+0.33)$',
       '$\phi(x) = xH(x-0.33)$',
       '$\phi(x) = xH(x-1.0)$']
plot.basis(mlai.relu, x_min=-2.0, x_max=2.0, 
           fig=f, ax=ax, loc=loc, text=text,
		   diagrams='\writeDiagramsDir/ml',
		   num_basis=5)}

\define{\basisfunction}{relu_basis}
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

\notes{\figure{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{004}}{80%}}{The set of functions which are combined to form a rectified linear unit basis.}{relu-basis-2}}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('relu_basis{num_basis:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							num_basis=IntSlider(0,0,4,1))}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_prediction(basis=mlai.relu, num_basis=5)}


\subsection{Functions Derived from Relu Basis}

$$
\mappingFunction(\inputScalar) = \color{\redColor}{\mappingScalar_0}   + \color{\magentaColor}{\mappingScalar_1 xH(x+1.0) } + \color{\blueColor}{\mappingScalar_2 xH(x+0.33) } + \color{\greenColor}{\mappingScalar_3 xH(x-0.33)} +  \color{\cyanColor}{\mappingScalar_4 xH(x-1.0)}
$$

\slides{
\define{width}{80%}
\startanimation{relu_function}{0}{4}
\newframe{\includediagram{\diagramsDir/ml/relu_function000}{\width}}{relu_function}
\newframe{\includediagram{\diagramsDir/ml/relu_function001}{\width}}{relu_function}
\newframe{\includediagram{\diagramsDir/ml/relu_function002}{\width}}{relu_function}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/ml/relu_function002}{80%}}{A rectified linear unit basis is made up of different rectified linear unit functions centered at different points.}{relu-function-2}}


\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('relu_function{func_num:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
            			    func_num=IntSlider(0,0,2,1))}
							
\endif
