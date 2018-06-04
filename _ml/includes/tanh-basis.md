### Hyperbolic Tangent Basis


\code{%load -s tanh mlai.py}

\setupcode{import pods}
\displaycode{pods.notebook.display_prediction(basis=mlai.tanh, num_basis=4)}

\notes{Sigmoid or hyperbolic tangent basis was popular in the original generation of multilayer perceptron models, or deep networks. These basis functions start flat, rise and then saturate.}

\setupcode{import matplotlib.pyplot as plt
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

### Functions Derived from Tanh Basis

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 } + {\color{yellow}\mappingScalar_3 }
$$

\slides{
\startslides{tanh_function}{1}{3}
\includesvg{../slides/diagrams/ml/tanh_function000.svg}{}{tanh_function}
\includesvg{../slides/diagrams/ml/tanh_function001.svg}{}{tanh_function}
\includesvg{../slides/diagrams/ml/tanh_function002.svg}{}{tanh_function}
}

\notesfigure{\includesvg{../slides/diagrams/ml/tanh_basis003.svg}{}{}}

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('tanh_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(0,0,4,1))}
