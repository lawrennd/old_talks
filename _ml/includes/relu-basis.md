### Rectified Linear Units

\setupcode{import numpy as np}
\code{%load -s relu mlai.py}

\setupcode{import pods}
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

### Functions Derived from Relu Basis

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 xH(x+1.0) } + {\color{yellow}\mappingScalar_2 xH(x+0.33) } + {\color{magenta}\mappingScalar_3 xH(x-0.33)} +  {\color{red}\mappingScalar_4 xH(x-1.0)}
$$

\slides{
\startslides{relu_function}{1}{3}
\includesvg{../slides/diagrams/ml/relu_function000.svg}{}{relu_function}
\includesvg{../slides/diagrams/ml/relu_function001.svg}{}{relu_function}
\includesvg{../slides/diagrams/ml/relu_function002.svg}{}{relu_function}
}
\notesfigure{\includesvg{../slides/diagrams/ml/relu_function004.svg}}

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('relu_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(0,0,4,1))}
