### Radial Basis Functions

\notes{Another type of basis is sometimes known as a 'radial basis' because the effect basis functions are constructed on 'centres' and the effect of each basis function decreases as the radial distance from each centre increases.}
\slides{* Basis functions can be local e.g. radial (or Gaussian) basis}
  $$\basisFunc_j(\inputScalar) = \exp\left(-\frac{(\inputScalar-\mu_j)^2}{\lengthScale^2}\right)$$

\code{%load -s radial mlai.py}

\displaycode{pods.notebook.display_prediction(basis=radial, num_basis=4)}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('radial_basis{num_basis:0>3}.svg', directory='../slides/diagrams/ml', num_basis=IntSlider(1,1,3,1))}

### Functions Derived from Radial Basis

$$
\mappingFunction(\inputScalar) = \colorred{\mappingScalar_1 e^{-2(\inputScalar+1)^2}}  + \colormagenta{\mappingScalar_2e^{-2\inputScalar^2}} + \colorblue{\mappingScalar_3 e^{-2(\inputScalar-1)^2}}
$$

\slides{\includesvg{../slides/diagrams/ml/radial_function001.svg}}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('radial_function{func_num:0>3}.svg', directory='../slides/diagrams/ml', func_num=IntSlider(1,1,3,1))}
