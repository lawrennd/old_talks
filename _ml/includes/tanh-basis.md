\ifndef{tanhBasis}
\define{tanhBasis}
\editme

\subsection{Hyperbolic Tangent Basis}

\code{%load -s tanh mlai.py}

\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_prediction(basis=mlai.tanh, num_basis=4)}

\notes{Sigmoid or hyperbolic tangent basis was popular in the original generation of multilayer perceptron models, or deep networks. These basis functions start flat, rise and then saturate.}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
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
plot.basis(mlai.tanh, x_min=-2.0, x_max=2.0,
           fig=f, ax=ax, loc=loc, text=text,
           diagrams='../slides/diagrams/ml',
           num_basis=5)
}

\subsection{Functions Derived from Tanh Basis}

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 } + {\color{yellow}\mappingScalar_3 }
$$

\slides{
\define{width}{80%}
\startanimation{tanh_function}{0}{4}
\newframe{\includediagram{../slides/diagrams/ml/tanh_function000}{\width}}{tanh_function}
\newframe{\includediagram{../slides/diagrams/ml/tanh_function001}{\width}}{tanh_function}
\newframe{\includediagram{../slides/diagrams/ml/tanh_function002}{\width}}{tanh_function}
\newframe{\includediagram{../slides/diagrams/ml/tanh_function003}{\width}}{tanh_function}
\newframe{\includediagram{../slides/diagrams/ml/tanh_function004}{\width}}{tanh_function}
\endanimation
}

\notes{\figure{\includediagram{../slides/diagrams/ml/tanh_basis004}{80%}}{A hyperbolic tangent basis is made up of s-shaped basis functions centered at different points.}{tanh-basis-4}}

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('tanh_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(0,0,4,1))}
\endif
