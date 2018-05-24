\setupcode{import matplotlib.pyplot as plt
import mlai
import teaching_plots as plot}

\code{%load -s polynomial mlai.py}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = x$',
       '$\phi(x) = x^2$']
plot.basis(mlai.polynomial, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text,
		   diagrams='../slides/diagrams/ml')
}

### Functions Derived from Polynomial Basis

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_0}   + {\color{green}\mappingScalar_1 \inputScalar} + {\color{yellow}\mappingScalar_3 \inputScalar^2}
$$

\startslides{polynomial_function}{1}{3}
\includesvg{../slides/diagrams/ml/polynomial_function001.svg}{}{polynomial_function}
\includesvg{../slides/diagrams/ml/polynomial_function002.svg}{}{polynomial_function}
\includesvg{../slides/diagrams/ml/polynomial_function003.svg}{}{polynomial_function}

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('polynomial_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(0,0,2,1))}
