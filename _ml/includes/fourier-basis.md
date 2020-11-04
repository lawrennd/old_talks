\ifndef{fourierBasis}
\define{fourierBasis}
\editme

\subsection{Fourier Basis}

\slides{* }
\notes{[Joseph Fourier](https://en.wikipedia.org/wiki/Joseph_Fourier) suggested that functions could be converted to a sum of sines and cosines. A Fourier basis is a linear weighted sum of these functions.}
$$
\mappingFunction(\inputScalar) = \mappingScalar_0  + \mappingScalar_1 \sin(\inputScalar) + \mappingScalar_2 \cos(\inputScalar) + \mappingScalar_3 \sin(2\inputScalar) + \mappingScalar_4 \cos(2\inputScalar)
$$


\setupcode{import numpy as np}
\loadcode{fourier}{mlai}


\setupplotcode{import matplotlib.pyplot as plt
import mlai
import teaching_plots as plot}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0., 0.4,],
      [0.5, 0.4],
      [1, -0.4],
      [1.25, 0.4],
      [1.5, -0.4]]
text =['$\phi(x) = 1$',
       '$\phi(x) = \sin(x)$',
       '$\phi(x) = \cos(x)$',
       '$\phi(x) = \sin(2x)$',
       '$\phi(x) = \cos(2x)$']
plot.basis(mlai.fourier, x_min=0, x_max=2, 
           fig=f, ax=ax, loc=loc, text=text,
           diagrams='\writeDiagramsDir/ml',
           num_basis=5)}

\define{\basisfunction}{fourier_basis}
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

\notes{\figure{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{004}}{80%}}{The set of functions which are combined to form a *Fourier* basis.}{fourier-basis-2}}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}

\displaycode{pods.notebook.display_plots('fourier_basis{num_basis:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							num_basis=IntSlider(0,0,4,1))}

\notes{In this code, basis functions with an *odd* index are sine and basis functions with an *even* index are cosine. The first basis function (index 0, so cosine) has a frequency of 0 and then frequencies increase every time a sine and cosine are included.}

\displaycode{pods.notebook.display_prediction(basis=mlai.fourier, num_basis=5)}

\subsection{Functions Derived from Fourier Basis}

$$
\mappingFunction(\inputScalar) = {\color{\redColor}{\mappingScalar_0}}  + {\color{\magentaColor}{\mappingScalar_1 \sin(\inputScalar)}} + {\color{\blueColor}{\mappingScalar_2 \cos(\inputScalar)}} + {\color{\greenColor}{\mappingScalar_3 \sin(2\inputScalar)}} + {\color{\cyanColor}{\mappingScalar_4 \cos(2\inputScalar)}}
$$

\slides{
\define{width}{80%}
\startanimation{fourier_function}{0}{4}
\newframe{\includediagram{\diagramsDir/ml/fourier_function000}{\width}}{fourier_function}
\newframe{\includediagram{\diagramsDir/ml/fourier_function001}{\width}}{fourier_function}
\newframe{\includediagram{\diagramsDir/ml/fourier_function002}{\width}}{fourier_function}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/fourier_function002}{80%}}{A random combination of functions from the Fourier basis. Fourier basis is made up of sine and cosine functions with different frequencies.}{fourier-function-2}}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('fourier_function{func_num:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							func_num=IntSlider(0,0,2,1))}


\endif
