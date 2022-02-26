\ifndef{quadraticBasis}
\define{quadraticBasis}

\editme

\notes{Let's try constructing such a matrix for a set of inputs. First of all, we create a function that returns the matrix valued function.}

\setupcode{import numpy as np}

\code{def quadratic(x, **kwargs):
    """Take in a vector of input values and return the design matrix associated 
    with the basis functions."""
    return np.hstack([np.ones((x.shape[0], 1)), x, x**2])
}

\subsection{Functions Derived from Quadratic Basis}

$$
\mappingFunction(\inputScalar) = {\color{\redColor}{\mappingScalar_0}} + {\color{\magentaColor}{\mappingScalar_1 \inputScalar}} + {\color{\blueColor}{\mappingScalar_2 \inputScalar^2}}
$$

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = x$',
       '$\phi(x) = x^2$']

plot.basis(quadratic, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text,
		   diagrams='\writeDiagramsDir/ml')

}

\define{\basisfunction}{quadratic_basis}
\slides{
\define{\width}{80%}
\startanimation{\basisfunction}{0}{2}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{000}}{\width}}{\basisfunction}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{001}}{\width}}{\basisfunction}
\newframe{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{002}}{\width}}{\basisfunction}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/\concat{\basisfunction}{002}}{80%}}{The set of functions which are combined to form a *quadratic* basis.}{quadratic-basis-2}}

\displaycode{import pods
from ipywidgets import IntSlider}

\displaycode{pods.notebook.display_plots('\basisfunction{num_basis:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							num_basis=IntSlider(0,0,2,1))}


\notes{This function takes in an $\numData \times 1$ dimensional vector and returns an $\numData \times 3$ dimensional *design matrix* containing the basis functions. We can plot those basis functions against there input as follows.}

\plotcode{# first let's generate some inputs
n = 100
x = np.zeros((n, 1))  # create a data set of zeros
x[:, 0] = np.linspace(-1, 1, n) # fill it with values between -1 and 1

Phi = quadratic(x)

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.set_ylim([-1.2, 1.2]) # set y limits to ensure basis functions show.
ax.plot(x[:,0], Phi[:, 0], 'r-', label = '$\phi=1$', linewidth=3)
ax.plot(x[:,0], Phi[:, 1], 'g-', label = '$\phi=x$', linewidth=3)
ax.plot(x[:,0], Phi[:, 2], 'b-', label = '$\phi=x^2$', linewidth=3)
ax.legend(loc='lower right')
_ = ax.set_title('Quadratic Basis Functions')}

\notes{The actual function we observe is then made up of a sum of these functions. This is the reason for the name basis. The term *basis* means 'the underlying support or foundation for an idea, argument, or process', and in this context they form the underlying support for our prediction function. Our prediction function can only be composed of a weighted linear sum of our basis functions.}

\subsection{Quadratic Functions}
\slides{$$
\mappingFunction(\inputScalar) = {\color{\redColor}{\mappingScalar_0}}   + {\color{\magentaColor}{\mappingScalar_1 \inputScalar}} + {\color{\blueColor}{\mappingScalar_2 \inputScalar^2}}
$$}
\slides{
\define{\width}{80%}
\startanimation{quadratic_function}{0}{2}
\newframe{\includediagram{\diagramsDir/ml/quadratic_function000}{\width}}{quadratic_function}
\newframe{\includediagram{\diagramsDir/ml/quadratic_function001}{\width}}{quadratic_function}
\newframe{\includediagram{\diagramsDir/ml/quadratic_function002}{\width}}{quadratic_function}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/quadratic_function002}{80%}}{Functions constructed by weighted sum of the components of a quadratic basis.}{quadratic-function-2}}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}

\displaycode{pods.notebook.display_plots('quadratic_function{num_function:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							num_function=IntSlider(0,0,2,1))}

\endif
