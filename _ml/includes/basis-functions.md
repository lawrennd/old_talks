### Basis Functions

\notes{Here's the idea, instead of working directly on the original input space, $\inputVector$, we build models in a new space, $\basisFuncVector(\inputVector)$ where $\basisFuncVector(\cdot)$ is a *vector valued* function that is defined on the space $\inputVector$.}

### Quadratic Basis

\slides{* Basis functions can be global. E.g. quadratic basis:
  $$\basisFuncVector = [1, \inputScalar, \inputScalar^2]$$}

\notes{Remember, that a vector valued function is just a vector that contains functions instead of values. Here's an example for a one dimensional input space, $x$, being projected to a *quadratic* basis. First we consider each basis function in turn, we can think of the elements of our vector as being indexed so that we have}
$$\begin{align*}
\basisFunc_1(\inputScalar) = 1, \\
\basisFunc_2(\inputScalar) = x, \\
\basisFunc_3(\inputScalar) = \inputScalar^2.
\end{align*}$$
\notes{Now we can consider them together by placing them in a vector,}
$$
\basisFuncVector(\inputScalar) = \begin{bmatrix} 1\\ x \\ \inputScalar^2\end{bmatrix}.
$$
\notes{This is the idea of the vector valued function, we have simply collected the different functions together in the same vector making them notationally easier to deal with in our mathematics.}

\notes{When we consider the vector valued function for each data point, then we place all the data into a matrix. The result is a matrix valued function,}
$$
\basisFuncVector(\inputVector) = 
\begin{bmatrix} 1 & \inputScalar_1 &
\inputScalar_1^2 \\
1 & \inputScalar_2 & \inputScalar_2^2\\
\vdots & \vdots & \vdots \\
1 & \inputScalar_n & \inputScalar_n^2
\end{bmatrix}
$$
\notes{where we are still in the one dimensional input setting so $\inputVector$ here represents a vector of our inputs with $\numData$ elements.}

\notes{Let's try constructing such a matrix for a set of inputs. First of all, we create a function that returns the matrix valued function}

\setupcode{import numpy as np}

\code{def quadratic(x):
    """Take in a vector of input values and return the design matrix associated 
    with the basis functions."""
    return np.hstack([np.ones((n, 1)), x, x**2])
}

### Functions Derived from Quadratic Basis

$$\mappingFunction(x) = \colorred{\mappingScalar_0} + \colormagenta{\mappingScalar_1\inputScalar} + \colorblue{\mappingScalar_2 \inputScalar^2}$$

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('polynomial_function{func_num:0>3}.svg', directory='../slides/diagrams/ml', func_num=IntSlider(1,1,3,1))}

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

\notes{This function takes in an $\numData \times 1$ dimensional vector and returns an $\numData \times 3$ dimensional *design matrix* containing the basis functions. We can plot those basis functions against there input as follows.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline}

\plotcode{# first let's generate some inputs
n = 100
x = np.zeros((n, 1))  # create a data set of zeros
x[:, 0] = np.linspace(-1, 1, n) # fill it with values between -1 and 1

Phi = quadratic(x)

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.set_ylim([-1.2, 1.2]) # set y limits to ensure basis functions show.
ax.plot(x[:,0], Phi[:, 0], 'r-', label = '$\phi=1$', linewidth=3)
ax.plot(x[:,0], Phi[:, 1], 'g-', label = '$\phi = x$', linewidth=3)
ax.plot(x[:,0], Phi[:, 2], 'b-', label = '$\phi = x^2$', linewidth=3)
ax.legend(loc='lower right')
_ = ax.set_title('Quadratic Basis Functions')}

\notes{The actual function we observe is then made up of a sum of these functions. This is the reason for the name basis. The term *basis* means 'the underlying support or foundation for an idea, argument, or process', and in this context they form the underlying support for our prediction function. Our prediction function can only be composed of a weighted linear sum of our basis functions.}

\setupcode{import matplotlib.pyplot as plt
import mlai
import teaching_plots as plot}

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

\setupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('polynomial_basis{num_basis:0>3}.svg', directory='../slides/diagrams/ml', num_basis=IntSlider(1,1,3,1))}


\include{_ml/includes/radial-basis.md}
\include{_ml/includes/fourier-basis.md}
\include{_ml/includes/relu-basis.md}
\include{_ml/includes/tanh-basis.md}




### Different Bases

\notes{Our choice of basis can be made based on what our beliefs about what is appropriate for the data. For example, the polynomial basis extends the quadratic basis to aribrary degree, so we might define the $j$th basis function associated with the model as}
$$
\basisFunc_j(\inputScalar_i) = \inputScalar_i^j
$$
\notes{which can be implemented as a function in code as follows}

\code{def polynomial(x, num_basis=4, data_limits=[-1., 1.]):
    Phi = np.zeros((x.shape[0], num_basis))
    for i in range(num_basis):
        Phi[:, i:i+1] = x**i
    return Phi}

\notes{To aid in understanding how a basis works, we've provided you with a small interactive tool for exploring this polynomial basis. The tool can be summoned with the following command.}

\setupcode{import pods}
\displaycode{pods.notebook.display_prediction(basis=polynomial, num_basis=4)}

\notes{Try moving the sliders around to change the weight of each basis function. Click the control box `display_basis` to show the underlying basis functions (in red). The prediction function is shown in a thick blue line. *Warning* the sliders aren't presented quite in the correct order. `w_0` is associated with the bias, `w_1` is the linear term, `w_2` the quadratic and here (because we have four basis functions) we have `w_3` for the *cubic* term. So the subscript of the weight parameter is always associated with the corresponding polynomial's degree.}

\writeassignment{Try increasing the number of basis functions (thereby increasing the *degree* of the resulting polynomial). Describe what you see as you increase number of basis up to 10. Is it easy to change the function in intiutive ways?{1}{15}



