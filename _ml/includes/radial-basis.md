### Radial Basis Functions

\notes{Another type of basis is sometimes known as a 'radial basis' because the effect basis functions are constructed on 'centres' and the effect of each basis function decreases as the radial distance from each centre increases.}
\slides{* Basis functions can be local e.g. radial (or Gaussian) basis}
  $$\basisFunc_j(\inputScalar) = \exp\left(-\frac{(\inputScalar-\mu_j)^2}{\lengthScale^2}\right)$$

\setupcode{import matplotlib.pyplot as plt
import mlai
import teaching_plots as plot}

\code{%load -s radial mlai.py}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)

loc = [[-1.25, -0.4],
       [0., 1.25],
       [1.25, -0.4]]
text = ['$\phi_1(x) = e^{-(x + 1)^2}$',
        '$\phi_2(x) = e^{-2x^2}$', 
        '$\phi_3(x) = e^{-2(x-1)^2}$']
plot.basis(mlai.radial, x_min=-2, x_max=2, 
           fig=f, ax=ax, loc=loc, text=text,
           diagrams='../slides/diagrams/ml')}

\displaycode{pods.notebook.display_prediction(basis=mlai.radial, num_basis=4)}

\setupcode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('radial_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(0,0,2,1))}

### Functions Derived from Radial Basis

$$
\mappingFunction(\inputScalar) = {\color{cyan}\mappingScalar_1 e^{-2(\inputScalar+1)^2}}  + {\color{green}\mappingScalar_2e^{-2\inputScalar^2}} + {\color{yellow}\mappingScalar_3 e^{-2(\inputScalar-1)^2}}
$$

\startslides{radial_function}{1}{3}
\includesvg{../slides/diagrams/ml/radial_function000.svg}{}{radial_function}
\includesvg{../slides/diagrams/ml/radial_function001.svg}{}{radial_function}
\includesvg{../slides/diagrams/ml/radial_function002.svg}{}{radial_function}

\setupcode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('radial_function{func_num:0>3}.svg', directory='../slides/diagrams/ml', func_num=IntSlider(0,0,2,1))}


