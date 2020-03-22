\ifndef{olympicMarathonValidationFit}
\define{olympicMarathonValidationFit}

\include{_ml/includes/olympic-marathon-data.md}

\editme

\subsection{Validation on the Olympic Marathon Data}

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

Fit a linear model to the olympic data using these functions and plot the resulting prediction between 1890 and 2020. Set the title of the plot to be the error of the fit on the *training data*.}{}{15}

\subsection{Polynomial Fit: Training Error}

\slides{The next thing we'll do is consider a quadratic fit. We will compute the training error for the two fits.}

\codeassignment{In this question we extend the code above to a non-
linear basis (a quadratic function).

Start by creating a python-function called `quadratic`. It should compute the quadratic basis.
$$
\basisMatrix = \begin{bmatrix} \mathbf{1} & \dataVector & \dataVector^2\end{bmatrix}
$$
It should be called in the following form:

```Phi = quadratic(x)```

Use this to compute the quadratic fit for the model, again plotting the result titled by the error.}{}{10}

\subsection{Polynomial Fits to Olympics Data}

\setupplotcode{import pods
import mlai}

\plotcode{max_basis = 26
basis = mlai.Basis(mlai.polynomial, number=1, data_limits=data_limits)
data_limits = [1892, 2020]
num_data = x.shape[0]}

\setupplotcode{import teaching_plots as plot
%matplotlib inline}

\plotcode{plot.rmse_fit(x, y, param_name='number', param_range=(1, max_basis+1), 
              model=mlai.LM, basis=basis, 
              xlim=data_limits, objective_ylim=[0, 0.8],
			  diagrams='\diagramsDir/ml')}

\setupdisplaycode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_LM_polynomial_number{num_basis:0>3}.svg', 
                            directory='\diagramsDir/ml', 
							num_basis=IntSlider(1, 1, max_basis, 1))}

\slides{
\define{\width}{80%}
\define{animationName}{olympic_LM_polynomial_number}
\startanimation{\animationName}{1}{26}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number001}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number002}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number003}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number004}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number005}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number006}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number007}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number008}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number009}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number010}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number011}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number012}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number013}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number014}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number015}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number016}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number017}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number018}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number019}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number020}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number021}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number022}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number023}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number024}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number025}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number026}{\width}}{\animationName}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number026}{80%}}{Polynomial fit to olympic data with 26 basis functions.}{olympic-lm-polynomial-num-basis-26}}

\endif
