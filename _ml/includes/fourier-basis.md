### Fourier Basis
\slides{* }
\notes{[Joseph Fourier](https://en.wikipedia.org/wiki/Joseph_Fourier) suggested that functions could be converted to a sum of sines and cosines. A Fourier basis is a linear weighted sum of these functions.}
  $$\basisFunc_j(\inputScalar) = $$

\code{%load -s fourier mlai.py}

\notes{In this code, basis functions with an *odd* index are sine and basis functions with an *even* index are cosine. The first basis function (index 0, so cosine) has a frequency of 0 and then frequencies increase every time a sine and cosine are included.}

\displaycode{pods.notebook.display_prediction(basis=fourier, num_basis=4)}

### Functions Derived from Fourier Basis

$$
\mappingFunction(\inputScalar) = \colorred{\mappingScalar_1 ..}  + \colormagenta{\mappingScalar_2 } + \colorblue{\mappingScalar_3 }
$$


\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('fourier_function{func_num:0>3}.svg', directory='../slides/diagrams/ml', func_num=IntSlider(1,1,3,1))}
