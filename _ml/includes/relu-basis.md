\ifndef{reluBasis}
\define{reluBasis}
\editme

\subsection{Rectified Linear Units}

\setupcode{import numpy as np}
\loadcode{relu}{mlai}

\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_prediction(basis=mlai.relu, num_basis=4)}

\notes{Rectified linear units are popular in the current generation of multilayer perceptron models, or deep networks. These basis functions start flat, and then become linear functions at a certain threshold.}

\setupcode{import matplotlib.pyplot as plt
import teaching_plots as plot
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
		   diagrams='../slides/diagrams/ml',
		   num_basis=5)
}

\subsection{Functions Derived from Relu Basis}

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 xH(x+1.0) } + {\color{yellow}\mappingScalar_2 xH(x+0.33) } + {\color{magenta}\mappingScalar_3 xH(x-0.33)} +  {\color{red}\mappingScalar_4 xH(x-1.0)}
$$

\slides{
\define{width}{80%}
\startanimation{relu_function}{0}{4}
\newframe{\includediagram{../slides/diagrams/ml/relu_function000}{\width}}{relu_function}
\newframe{\includediagram{../slides/diagrams/ml/relu_function001}{\width}}{relu_function}
\newframe{\includediagram{../slides/diagrams/ml/relu_function002}{\width}}{relu_function}
\newframe{\includediagram{../slides/diagrams/ml/relu_function003}{\width}}{relu_function}
\newframe{\includediagram{../slides/diagrams/ml/relu_function004}{\width}}{relu_function}
\endanimation
}
\notes{\figure{\includediagram{../slides/diagrams/ml/relu_basis004}{80%}}{A rectified linear unit basis is made up of different rectified linear unit functions centered at different points.}{relu-basis-4}}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('relu_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
			    num_basis=IntSlider(0,0,4,1))}
\endif
