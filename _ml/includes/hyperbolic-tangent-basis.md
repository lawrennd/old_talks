\ifndef{hyperbolicTangentBasis}
\define{hyperbolicTangentBasis}
\editme

\subsection{Hyperbolic Tangent Basis}

\slides{* }
\notes{The rectified linear unit is a basis function that used to be used a lot for neural network models. It's related to the sigmoid function by a scaling.}
$$
\basisFunc_j(\inputScalar) = \tanh(\mappingScalarTwo_j \inputScalar + \mappingScalarTwo_0)
$$

\setupcode{import numpy as np}
\loadcode{hyperbolic_tangent}{mlai}

\notes{Sigmoid or hyperbolic tangent basis was popular in the original generation of multilayer perceptron models, or deep networks. These basis functions start flat, rise and then saturate.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot
import mlai}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [-1, -0.7],
      [-0.33, 0],
      [0.33, -0.7],
      [1, 0]]
text =['$\phi(x) = 1$',
       '$\phi(x) = \\tanh(x+1.0)$',
       '$\phi(x) = \\tanh(x+0.33)$',
       '$\phi(x) = \\tanh(x-0.33)$',
       '$\phi(x) = \\tanh(x-1.0)$']
plot.basis(mlai.hyperbolic_tangent, x_min=-2.0, x_max=2.0,
           fig=f, ax=ax, loc=loc, text=text,
           diagrams='\writeDiagramsDir/ml',
           num_basis=5)}

\define{\basisfunction}{hyperbolic_tangent_basis}
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

\notes{\figure{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{004}}{80%}}{The set of functions which are combined to form a *hyberbolic tangent* basis.}{hyperbolic_tangent-basis-2}}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}

\displaycode{pods.notebook.display_plots('hyperbolic_tangent_basis{num_basis:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							num_basis=IntSlider(0,0,4,1))}

\subsection{Functions Derived from Tanh Basis}

$$
\mappingFunction(\inputScalar) = {\color{\redColor}{\mappingScalar_0}}   + {\color{\magentaColor}{\mappingScalar_1 \text{tanh}\left(\inputScalar+1\right)}}  + {\color{\blueColor}{\mappingScalar_2 \text{tanh}\left(\inputScalar+0.33\right)}}  + {\color{\greenColor}{\mappingScalar_3 \text{tanh}\left(\inputScalar-0.33\right)}} + {\color{\cyanColor}{\mappingScalar_4 \text{tanh}\left(\inputScalar-1\right)}}
$$

\slides{
\define{width}{80%}
\startanimation{hyperbolic_tangent_function}{0}{4}
\newframe{\includediagram{\diagramsDir/ml/hyperbolic_tangent_function000}{\width}}{hyperbolic_tangent_function}
\newframe{\includediagram{\diagramsDir/ml/hyperbolic_tangent_function001}{\width}}{hyperbolic_tangent_function}
\newframe{\includediagram{\diagramsDir/ml/hyperbolic_tangent_function002}{\width}}{hyperbolic_tangent_function}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/hyperbolic_tangent_function002}{80%}}{A hyperbolic tangent basis is made up of s-shaped basis functions centered at different points.}{hyperbolic_tangent-function-2}}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('hyperbolic_tangent_function{func_num:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							func_num=IntSlider(0,0,2,1))}
\endif
