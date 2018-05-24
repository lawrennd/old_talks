### Rectified Linear Units

\code{%load -s relu mlai.py}

\displaycode{pods.notebook.display_prediction(basis=relu, num_basis=4)}

\notes{Rectified linear units are popular in the current generation of multilayer perceptron models, or deep networks. These basis functions start flat, and then become linear functions at a certain threshold.}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =['$\phi(x) = $',
       '$\phi(x) = $',
       '$\phi(x) = $']
plot.basis(mlai.relu, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text,
		   diagrams='../slides/diagrams/ml')
}

### Functions Derived from Relu Basis

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 } + {\color{yellow}\mappingScalar_3 }
$$

\startslides{relu_function}{1}{3}
\includesvg{../slides/diagrams/ml/relu_function000.svg}{}{relu_function}
\includesvg{../slides/diagrams/ml/relu_function001.svg}{}{relu_function}
\includesvg{../slides/diagrams/ml/relu_function002.svg}{}{relu_function}

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('relu_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(0,0,2,1))}
