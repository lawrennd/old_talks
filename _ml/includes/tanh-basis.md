### Hyperbolic Tangent Basis

\code{%load -s tanh mlai.py}

\displaycode{pods.notebook.display_prediction(basis=tanh, num_basis=4)}

\notes{Sigmoid or hyperbolic tangent basis was popular in the original generation of multilayer perceptron models, or deep networks. These basis functions start flat, rise and then saturate.}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = \tanh(x-)$',
       '$\phi(x) = \tanh(x-)$']
plot.basis(mlai.tanh, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text,
		   diagrams='../slides/diagrams/ml')
}

### Functions Derived from Tanh Basis

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 } + {\color{yellow}\mappingScalar_3 }
$$

\startslides{tanh_function}{1}{3}
\includesvg{../slides/diagrams/ml/tanh_function000.svg}{}{tanh_function}
\includesvg{../slides/diagrams/ml/tanh_function001.svg}{}{tanh_function}
\includesvg{../slides/diagrams/ml/tanh_function002.svg}{}{tanh_function}

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('tanh_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(0,0,2,1))}
