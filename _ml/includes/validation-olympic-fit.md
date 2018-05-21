\notes{The first thing we'll do is fit a standard linear model to the data. We recall from previous lectures and lab classes that to do this we need to solve the system
$$
\basisMatrix^\top \basisMatrix \mappingVector = \basisMatrix^\top \dataVector
$$
for $\mappingVector$  and use the resulting vector to make predictions at the training points and test points,
$$
\mappingFunctionVector = \basisMatrix \mappingVector.
$$
The prediction function can be used to compute the objective function,
$$
E(\mappingVector) = \sum_{i}^{\numData} (\dataScalar_i - \mappingVector^\top\phi(\dataVector_i))^2
$$
by substituting in the prediction in vector form we have
$$
E(\mappingVector) =  (\dataVector - \mappingFunctionVector)^\top(\dataVector - \mappingFunctionVector)
$$}

\codeassignment{In this question you will construct some flexible general code for fitting linear models.

Create a python function that computes $\basisMatrix$ for the linear basis,
$$\basisMatrix = \begin{bmatrix} \dataVector & \mathbf{1}\end{bmatrix}$$
Name your function `linear`. `Phi` should be in the form of a *design matrix* and `x` should be in the form of a `numpy` two dimensional array with $\numData$ rows and 1 column Calls to your function should be in the following form:

```Phi = linear(x)```

Create a python function that accepts, as arguments, a python function that defines a basis (like the one you've just created called `linear`) as well as a set of inputs and a vector of parameters. Your new python function should return a prediction. Name your function `prediction`. The return value `f` should be a two dimensional `numpy` array with $\numData$ rows and $1$ column, where $\numData$ is the number of data points. Calls to your function should be in the following form:

```f = prediction(w, x, linear)```

Create a python function that computes the sum of squares objective function (or error function). It should accept your input data (or covariates) and target data (or response variables) and your parameter vector `w` as arguments. It should also accept a python function that represents the basis. Calls to your function should be in the following form:

```e = objective(w, x, y, linear)```

Create a function that solves the linear system for the set of parameters that minimizes the sum of squares objective. It should accept input data, target data and a python function for the basis as the inputs. Calls to your function should be in the following form:

```w = fit(x, y, linear)```

Fit a linear model to the olympic data using these functions and plot the resulting prediction between 1890 and 2020. Set the title of the plot to be the error of the fit on the *training data*.}{1}{15}

### Polynomial Fit: Training Error

\slides{The next thing we'll do is consider a quadratic fit. We will compute the training error for the two fits.}

\codeassignment{In this question we extend the code above to a non-
linear basis (a quadratic function).

Start by creating a python-function called `quadratic`. It should compute the quadratic basis.
$$
\basisMatrix = \begin{bmatrix} \mathbf{1} & \dataVector & \dataVector^2\end{bmatrix}
$$
It should be called in the following form:

```Phi = quadratic(x)```

Use this to compute the quadratic fit for the model, again plotting the result titled by the error.}{2}{10}

### Polynomial Fits to Olympics Data

\setupcode{import pods
import mlai}

\code{max_basis = 8
basis = mlai.polynomial

data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']

data_limits = [1892, 2020]
num_data = x.shape[0]}

\setupcode{import teaching_plots as plot
%matplotlib inline}

\plotcode{plot.rmse_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1), 
              model=mlai.LM, basis=basis, data_limits=data_limits, 
              xlim=data_limits, objective_ylim=[0, 0.8],
			  diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_LM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1, 1, max_basis, 1))}
