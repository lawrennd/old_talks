---
layout: lectures
title: Basis Functions
author: Neil D. Lawrence
date: 2015/10/20
transition: None
---

\include{talk-macros.tex}

\setupcode{
import numpy as np
import scipy as sp
%matplotlib inline}

### Review

* Last time: explored least squares for univariate and multivariate regression.
* Introduced matrices, linear algebra and derivatives.
* This time: introduce *basis functions* for non-linear regression models.

### Nonlinear Regression

* Problem with Linear Regression—$\inputVector$ may not be linearly related to $\dataVector$.
* Potential solution: create a feature space: define $\basisFunc(\inputVector)$ where $\basisFunc(\cdot)$ is a nonlinear function of $\inputVector$.
* Model for target is a linear combination of these nonlinear functions 
  $$\mappingFunction(\inputVector) = \sum_{j=1}^\numBasisFunc \mappingScalar_j \basisFunc_j(\inputVector)$$

\setupcode{from matplotlib import pyplot as plt
import mlai
import teaching_plots as plot}
\plotcode{f, ax = plt.subplots(figsize=plot.big_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =['$\phi(x) = 1$',
       '$\phi(x) = x$',
       '$\phi(x) = x^2$']
mlai.plot_basis(mlai.polynomial, x_min=-1.3, x_max=1.3, fig=f, ax=ax, loc=loc, text=text)
}

### Quadratic Basis

* Basis functions can be global. E.g. quadratic basis:
  $$\basisFuncVector = [1, \inputScalar, \inputScalar^2]$$

\setupcode{import pods}
\displaycode{pods.notebook.display_plots('polynomial_basis{num_basis:0>3}.svg', directory='../slides/diagrams/ml', num_basis=(1,3))}

### Functions Derived from Quadratic Basis

$$\mappingFunction(x) = \colorred{\mappingScalar_0} + \colormagenta{\mappingScalar_1\inputScalar} + \colorblue{\mappingScalar_2 \inputScalar^2}$$

\displaycode{pods.notebook.display_plots('polynomial_function{func_num:0>3}.svg', directory='../slides/diagrams/ml', func_num=(1,3))}

\plotcode{f, ax = plt.subplots(figsize=plot.big_figsize)

loc = [[-1.25, -0.4],
       [0., 1.25],
       [1.25, -0.4]]
text = ['$\phi_1(x) = e^{-(x + 1)^2}$',
        '$\phi_2(x) = e^{-2x^2}$', 
        '$\phi_3(x) = e^{-2(x-1)^2}$']
mlai.plot_basis(mlai.radial, x_min=-2, x_max=2, fig=f, ax=ax, loc=loc, text=text)}

### Radial Basis Functions

* Or they can be local. E.g. radial (or Gaussian)
basis
  $$\basisFunc_j(\inputScalar) = \exp\left(-\frac{(\inputScalar-\mu_j)^2}{\lengthScale^2}\right)$$

\displaycode{pods.notebook.display_plots('radial_basis{num_basis:0>3}.svg', directory='../slides/diagrams/ml', num_basis=(1,3))}

### Functions Derived from Radial Basis

$$\mappingFunction(\inputScalar) = \colorred{\mappingScalar_1 e^{-2(\inputScalar+1)^2}}  + \colormagenta{\mappingScalar_2e^{-2\inputScalar^2}} + \colorblue{\mappingScalar_3 e^{-2(\inputScalar-1)^2}}$$

\displaycode{pods.notebook.display_plots('radial_function{func_num:0>3}.svg', directory='../slides/diagrams/ml', func_num=(1,3))}

### Basis Function Models

* The *prediction function* is now defined as 
  $$\mappingFunction(\inputVector_i) = \sum_{j=1}^\numBasisFunc \mappingScalar_j \basisFunc_{i, j}$$

### Vector Notation

* Write in vector notation,
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \basisFuncVector_i$$

### Log Likelihood for Basis Function Model

* The likelihood of a single data point is
  $$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp
\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\basisFuncVector_i\right)^{2}}{2\dataStd^2}\right).$$

### Log Likelihood for Basis Function Model

* Leading to a log likelihood for
the data set of
  $$L(\mappingVector,\dataStd^2)= -\frac{\numData}{2}\log \dataStd^2-\frac{\numData}{2}\log 2\pi -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisFuncVector_i\right)^{2}}{2\dataStd^2}.$$

### Objective Function

* And a corresponding *objective function* of the form
$$E(\mappingVector,\dataStd^2)= \frac{\numData}{2}\log
          \dataStd^2 + \frac{\sum
_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisFuncVector_i\right)^{2}}{2\dataStd^2}.$$

### Expand the Brackets

$$\begin{align}
  E(\mappingVector,\dataStd^2) =
&\frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i\mappingVector^{\top}\basisFuncVector_i\\ &+\frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\mappingVector^{\top}\basisFuncVector_i\basisFuncVector_i^{\top}\mappingVector+\text{const}.\end{align}$$

### Expand the Brackets

$$\begin{align} E(\mappingVector, \dataStd^2) = & \frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2} \mappingVector^\top\sum_{i=1}^{\numData}\basisFuncVector_i \dataScalar_i\\ & +\frac{1}{2\dataStd^2}\mappingVector^{\top}\left[\sum_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^{\top}\right]\mappingVector+\text{const}.\end{align}$$

### Multivariate Derivatives Reminder

* We will need some multivariate calculus.
  $$\frac{\text{d}\mathbf{a}^{\top}\mappingVector}{\text{d}\mappingVector}=\mathbf{a}$$
  and
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
  or if $\mathbf{A}$ is symmetric (*i.e.* $\mathbf{A}=\mathbf{A}^{\top}$)
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$

### Differentiate

Differentiating with respect to the vector $\mappingVector$ we
obtain
$$\frac{\text{d} E\left(\mappingVector,\dataStd^2 \right)}{\text{d}
\mappingVector}=-\frac{1}{\dataStd^2} \sum
_{i=1}^{\numData}\basisFuncVector_i\dataScalar_i+\frac{1}{\dataStd^2} \left[\sum
_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^{\top}\right]\mappingVector$$
Leading to
$$\mappingVector^{*}=\left[\sum
_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^{\top}\right]^{-1}\sum
_{i=1}^{\numData}\basisFuncVector_i\dataScalar_i,$$

### Matrix Notation

Rewrite in matrix notation:
$$\sum
_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^\top = \basisFuncVector^\top
\basisFuncVector$$
$$\sum _{i=1}^{\numData}\basisFuncVector_i\dataScalar_i =
\basisFuncVector^\top \dataVector$$

### Update Equations

* Update for $\mappingVector^{*}$.
  $$\mappingVector^{*} = \left(\basisFuncVector^\top \basisFuncVector\right)^{-1} \basisFuncVector^\top \dataVector$$

* The equation for $\left.\dataStd^2\right.^{*}$ may also be found
  $$\left.\dataStd^2\right.^{{*}}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\basisFuncVector_i\right)^{2}}{\numData}.$$

### Avoid Direct Inverse

* E.g. Solve for $\mappingVector$
  $$\left(\basisFuncVector^\top \basisFuncVector\right)\mappingVector = \basisFuncVector^\top \dataVector$$
  
* See `np.linalg.solve`

* In practice use $\mathbf{Q}\mathbf{R}$ decomposition (see lab class notes).

### Polynomial Fits to Olympic Data

\setupcode{import numpy as np
from matplotlib import pyplot as plt}

\code{basis = mlai.polynomial

data = pods.datasets.olympic_marathon_men()
f, ax = plt.subplots(1, 2, figsize=(10,5))
x = data['X']
y = data['Y']

data_limits = [1892, 2020]
max_basis = 27

ll = np.array([np.nan]*(max_basis))
sum_squares = np.array([np.nan]*(max_basis))}

\plotcode{for num_basis in range(1,max_basis):
    
    model = mlai.LM(x, y, basis, num_basis=num_basis, data_limits=data_limits)
    model.fit()
    sum_squares[num_basis-1] = model.objective() 
    ll[num_basis-1] = model.log_likelihood()
    plot.marathon_fit(model=model, data_limits=data_limits, 
                      objective=sum_squares, objective_ylim=[0,8],
                      title='Root Mean Square Training Error'
                      fig=f, ax=ax)
}

\displaycode{pods.notebook.display_plots('olympic_LM_polynomial{num_basis:0>3}.svg', directory='../slides/diagrams/ml', num_basis=(1,max_basis))}

### Reading

* Section 1.4 of @Rogers:book11.
* Chapter 1, pg 1-6 of @Bishop:book06.
* Chapter 3, Section 3.1 of @Bishop:book06 up to pg 143.



We've now seen how we may perform linear regression. Now, we are going to consider how we can perform *non-linear* regression. However, before we get into the details of how to do that we first need to consider in what ways the regression can be non-linear. Multivariate linear regression allows us to build models that take many features into account when making our prediction. In this session we are going to introduce *basis functions*. The term seems complicted, but they are actually based on rather a simple idea. If we are doing a multivariate linear regression, we get extra features that *might* help us predict our required response varible (or target value), $y$. But what if we only have one input value? We can actually artificially generate more input values with basis functions.

### Non-linear in the Inputs

When we refer to non-linear regression, we are normally referring to whether the regression is non-linear in the input space, or non-linear in the *covariates*. The covariates are the observations that move with the target (or *response*) variable. In our notation we have been using $\inputVector_i$ to represent a vector of the covariates associated with the $i$th observation. The coresponding response variable is $\dataScalar_i$. If a model is non-linear in the inputs, it means that there is a non-linear function between the inputs and the response variable. Linear functions are functions that only involve multiplication and addition, in other words they can be represented through *linear algebra*. Linear regression involves assuming that a function takes the form
$$
\mappingFunction(\inputVector) = \mappingVector^\top \inputVector
$$
where
$\mappingVector$ are our regression weights. A very easy way to make the linear regression non-linear is to introduce non-linear functions. When we are introducing non-linear regression these functions are known as *basis functions*.

### Basis Functions

Here's the idea, instead of working directly on the original input space, $\inputVector$, we build models in a new space, $\basisFuncVector(\inputVector)$ where $\basisFuncVector(\cdot)$ is a *vector valued* function that is defined on the space $\inputVector$. 

Remember, that a vector valued function is just a vector that contains functions instead of values. Here's an example for a one dimensional input space, $x$, being projected to a *quadratic* basis. First we consider each basis function in turn, we can think of the elements of our vector as being indexed so that we have
$$\begin{align*}
\basisFunc_1(\inputScalar) = 1, \\
\basisFunc_2(\inputScalar) = x, \\
\basisFunc_3(\inputScalar) = \inputScalar^2.
\end{align*}$$
Now we can consider them together by placing them in a vector,
$$
\basisFuncVector(\inputScalar) = \begin{bmatrix} 1\\ x \\ \inputScalar^2\end{bmatrix}.
$$
This is the idea of the vector valued function, we have simply collected the different functions together in the same vector making them notationally easier to deal with in our mathematics. 

When we consider the vector valued function for each data point, then we place all the data into a matrix. The result is a matrix valued function,
$$
\basisFuncVector(\inputVector) = 
\begin{bmatrix} 1 & \inputScalar_1 &
\inputScalar_1^2 \\
1 & \inputScalar_2 & \inputScalar_2^2\\
\vdots & \vdots & \vdots \\
1 & \inputScalar_n & \inputScalar_n^2
\end{bmatrix}
$$
where we are still in the one dimensional input setting so $\inputVector$ here represents a vector of our inputs with $\numData$ elements. 

Let's try constructing such a matrix for a set of inputs. First of all, we create a function that returns the matrix valued function

\setupcode{import numpy as np}

\code{def quadratic(x):
    """Take in a vector of input values and return the design matrix associated 
    with the basis functions."""
    return np.hstack([np.ones((n, 1)), x, x**2])
}

This function takes in an $n\times 1$ dimensional vector and returns an $\numData\times 3$ dimensional *design matrix* containing the basis functions. We can plot those basis functions against there input as follows.

\setupcode{# ensure plots appear in the notebook.
%matplotlib inline 
import pylab as plt}

\plotcode{# first let's generate some inputs
n = 100
x = np.zeros((n, 1))  # create a data set of zeros
x[:, 0] = np.linspace(-1, 1, n) # fill it with values between -1 and 1

Phi = quadratic(x)

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.set_ylim([-1.2, 1.2]) # set y limits to ensure basis functions show.
ax.plot(x[:,0], Phi[:, 0], 'r-', label = '$\phi=1$')
ax.plot(x[:,0], Phi[:, 1], 'g-', label = '$\phi = x$')
ax.plot(x[:,0], Phi[:, 2], 'b-', label = '$\phi = x^2$')
ax.legend(loc='lower right')
ax.set_title('Quadratic Basis Functions')}

The actual function we observe is then made up of a sum of these functions. This
is the reason for the name basis. The term *basis* means 'the underlying support
or foundation for an idea, argument, or process', and in this context they form
the underlying support for our prediction function. Our prediction function can
only be composed of a weighted linear sum of our basis functions.

### Different Basis

Our choice of basis can be made based on what our beliefs
about what is appropriate for the data. For example, the polynomial basis
extends the quadratic basis to aribrary degree, so we might define the $j$th
basis function associated with the model as
$$
\basisFunc_j(\inputScalar_i) = \inputScalar_i^j
$$
which can
be implemented as a function in code as follows

\code{def polynomial(x, num_basis=4, data_limits=[-1., 1.]):
    Phi = np.zeros((x.shape[0], num_basis))
    for i in range(num_basis):
        Phi[:, i:i+1] = x**i
    return Phi}

To aid in understanding how a basis works, we've provided you with a small
interactive tool for exploring this polynomial basis. The tool can be summoned
with the following command.

\setupcode{import pods}
\displaycode{pods.notebook.display_prediction(basis=polynomial, num_basis=4)}

\setupcode{import ipywidgets}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plt.close(fig)
from IPython.display import display
display(fig)}

Try moving the sliders around to change the weight of each basis function. Click the control box `display_basis` to show the underlying basis functions (in red). The prediction function is shown in a thick blue line. *Warning* the sliders aren't presented quite in the correct order. `w_0` is associated with the bias, w_1` is the linear term, `w_2` the quadratic and here (because we have four basis functions) we have `w_3` for the *cubic* term. So the subscript of the weight parameter is always associated with the corresponding polynomial's degree.

\writeassignment{Try increasing the number of basis functions (thereby increasing the *degree* of the resulting polynomial). Describe what you see as you increase number of basis up to 10. Is it easy to change the function in intiutive ways?{1}{15}

### Radial Basis Functions

Another type of basis is sometimes known as a 'radial basis' because the effect basis functions are constructed on 'centres' and the effect of each basis function decreases as the radial distance from each centre increases.

\code{%load -s radial mlai.py}

\displaycode{pods.notebook.display_prediction(basis=radial, num_basis=4)}

### Fourier Basis

Fourier noticed that any *stationary* function could be converted to a sum of sines and cosines. A Fourier basis is a linear weighted sum of these functions.

\code{%load -s fourier mlai.py}

In this code, basis functions with an *odd* index are sine and basis functions with an *even* index are cosine. The first basis function (index 0, so cosine) has a frequency of 0 and then frequencies increase to 1, 2, 3, 4 etc every time a sine and cosine are included.

\displaycode{pods.notebook.display_prediction(basis=fourier, num_basis=4)}

\code{%load -s relu mlai.py}

\displaycode{pods.notebook.display_prediction(basis=relu, num_basis=4)}

### Fitting to Data

Now we are going to consider how these basis functions can be adjusted to fit to
a particular data set. We will return to the olympic marathon data from last
time. First we will scale the output of the data to be zero mean and variance 1.

\code{data = pods.datasets.olympic_marathon_men()
y = data['Y']
x = data['X']
y -= y.mean()
y /= y.std()}

\writeassignment{Now we are going to redefine our polynomial basis. Have a careful look at the operations we perform on `x` to create `z`. We use `z` in the polynomial computation. What are we doing to the inputs? Why do you think we are changing `x` in this manner?}{2}{10}

\code{%load -s polynomial mlai.py}

\plotcode{#x[:, 0] = np.linspace(1888, 2020, 1000)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

ax.plot(x, y, 'rx')}


\displaycode{pods.notebook.display_prediction(basis=dict(radial=radial, polynomial=polynomial, fourier=fourier, relu=relu), 
                                 data_limits=(1888, 2020),
                                 fig=fig, ax=ax,
                                 offset=0.,
                                 wlim = (-4., 4., 0.001),
                                 num_basis=4)}

\writeassignment{Use the tool provided above to try and find the best
fit you can to the data. Explore the parameter space and give the weight values
you used for the 

(a) polynomial basis
(b) RBF basis
(c) Fourier basis

Write your answers in the code box below creating a new vector of parameters (in the correct order!) for each basis.}{3}{15}

\code{# Question 3 Answer Code
# provide the answers so that the code runs correctly otherwise you will loose marks!

# (a) polynomial
###### Edit these lines #####
w_0 =
w_1 = 
w_2 = 
w_3 =
##############################
w_polynomial = np.asarray([[w_0], [w_1], [w_2], [w_3]]) 

# (b) rbf
###### Edit these lines #####
w_0 =
w_1 = 
w_2 = 
w_3 =
##############################
w_rbf = np.asarray([[w_0], [w_1], [w_2], [w_3]]) 

# (c) fourier
###### Edit these lines #####
w_0 =
w_1 = 
w_2 = 
w_3 =
##############################
w_fourier = np.asarray([[w_0], [w_1], [w_2], [w_3]]) }

\code{np.asarray([[1, 2, 3, 4]]).shape}

We can We like to make use of *design* matrices for our data. Design matrices, as you will recall, involve placing the data points into rows of the matrix and data features into the columns of the matrix. By convention, we are referincing a vector with a bold lower case letter, and a matrix with a bold upper case letter. The design matrix is therefore given by
$$
\basisFuncVector = \begin{bmatrix} 1 & \inputVector & \inputVector^2\end{bmatrix}
$$


### Non-linear but Linear in the Parameters

One rather nice aspect of our model is that whilst it is non-linear in the inputs, it is still linear in the parameters $\mappingVector$. This means that our derivations from before continue to operate to allow us to work with this model. In fact, although this is a non-linear regression it is still known as a *linear model* because it is linear in the parameters, 
$$
\mappingFunction(\inputVector) = \mappingVector^\top \basisFuncVector(\inputVector)
$$
where the vector $\inputVector$ appears inside the basis functions, making our result, $\mappingFunction(\inputVector)$ non-linear in the inputs, but $\mappingVector$ appears outside our basis function, making our result *linear* in the parameters. In practice, our basis function itself may contain its own set of parameters,
$$
\mappingFunction(\inputVector) = \mappingVector^\top \basisFuncVector(\inputVector;
\boldsymbol{\theta}),
$$
that we've denoted here as $\boldsymbol{\theta}$. If
these parameters appear inside the basis function then our model is *non-linear*
in these parameters.

\writeassignment{For the following prediction functions state whether
the model is linear in the inputs, the parameters or both.

(a) $\mappingFunction(\inputScalar) = \mappingScalar_1\inputScalar_1 + \mappingScalar_2$

(b) $\mappingFunction(\inputScalar) = \mappingScalar_1\exp(\inputScalar_1) + \mappingScalar_2\inputScalar_2 + \mappingScalar_3$

(c) $\mappingFunction(\inputScalar) =
\log(\inputScalar_1^{\mappingScalar_1}) + \mappingScalar_2\inputScalar_2^2 + \mappingScalar_3$

(d) $\mappingFunction(\inputScalar) = \exp(-\sum_i(\inputScalar_i - \mappingScalar_i)^2)$

(e) $\mappingFunction(\inputScalar) = \exp(-\mappingVector^\top \inputVector)$}{4}{25}

### Fitting the Model Yourself

You now have everything you need to fit a non-
linear (in the inputs) basis function model to the marathon data.

\codeassignment{Choose one of the basis functions you have explored
above. Compute the design matrix on the covariates (or input data), `x`. Use the
design matrix and the response variable `y` to solve the following linear system
for the model parameters `w`.
$$
\basisFuncVector^\top\basisFuncVector\mappingVector = \basisFuncVector^\top
\dataVector
$$
Compute the corresponding error on the training data. How does it
compare to the error you were able to achieve fitting the basis above? Plot the
form of your prediction function from the least squares estimate alongside the
form of you prediction function you fitted by hand.}{5}{35}

### Lecture on Basis Functions from GPRS Uganda

\includeyoutube{PoNbOnUnOao}

### Use of QR Decomposition for Numerical Stability

In the last session we showed how rather than computing $\inputMatrix^\top\inputMatrix$ as an intermediate step to our solution, we could compute the solution to the regressiond directly through [QR-decomposition](http://en.wikipedia.org/wiki/QR_decomposition). Now we will consider an example with non linear basis functions where such computation is critical for forming the right answer. 

*TODO* example with polynomials.

\setupcode{import numpy as np}

\code{x = np.random.normal(size=(10, 1))}

\code{Phi = fourier(x, 5)}

\code{(np.dot(Phi.T,Phi))}

\code{Phi*Phi}
