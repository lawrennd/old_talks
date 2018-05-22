### Fourier Basis

\slides{* }
\notes{[Joseph Fourier](https://en.wikipedia.org/wiki/Joseph_Fourier) suggested that functions could be converted to a sum of sines and cosines. A Fourier basis is a linear weighted sum of these functions.}
  $$\basisFunc_j(\inputScalar) = $$

\setupcode{import matplotlib.pyplot as plt
import mlai
import teaching_plots as plot}

\code{%load -s fourier mlai.py}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = x$',
       '$\phi(x) = x^2$']
plot.basis(mlai.fourier, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text,
		   diagrams='../slides/diagrams/ml')
}

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('fourier_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1,1,3,1))}

\notes{In this code, basis functions with an *odd* index are sine and basis functions with an *even* index are cosine. The first basis function (index 0, so cosine) has a frequency of 0 and then frequencies increase every time a sine and cosine are included.}

\displaycode{pods.notebook.display_prediction(basis=fourier, num_basis=4)}

### Functions Derived from Fourier Basis

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_1 ..}  + {\color{green}\mappingScalar_2 } + {\color{yellow}\mappingScalar_3 }
$$

\startslides{fourier_function}
\includesvg{../slides/diagrams/ml/fourier_function001.svg}{}{fourier_function}
\includesvg{../slides/diagrams/ml/fourier_function002.svg}{}{fourier_function}
\includesvg{../slides/diagrams/ml/fourier_function003.svg}{}{fourier_function}

\setupcode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('fourier_function{func_num:0>3}.svg', directory='../slides/diagrams/ml', func_num=IntSlider(1,1,3,1))}


