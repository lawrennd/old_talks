\ifndef{basisFunctionModels}
\define{basisFunctionModels}

\editme

\subsection{Fitting to Data}

Now we are going to consider how these basis functions can be adjusted to fit to
a particular data set. We will return to the olympic marathon data from last
time. First we will scale the output of the data to be zero mean and variance 1.

talk-macros.gpp}atasets/includes/olympic-marathon-data.md}


\comment{\writeassignment{Now we are going to redefine our polynomial basis. Have a careful look at the operations we perform on `x` to create `z`. We use `z` in the polynomial computation. What are we doing to the inputs? Why do you think we are changing `x` in this manner?}{10}}



\setupdisplaycode{import matplotlib.pyplot as plt
import notutils as nu}
\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
yhat = (y - offset)/scale

_ = ax.plot(x, yhat, 'r.',markersize=10)
nu.display_prediction(basis=dict(radial=mlai.radial, 
	                                        polynomial=mlai.polynomial, 
											tanh=mlai.hyperbolic_tangent, 
											fourier=mlai.fourier, 
											relu=mlai.relu), 
                                 data_limits=(1888, 2020),
                                 fig=fig, ax=ax,
                                 offset=0.,
                                 wlim = (-4., 4.),
                                 num_basis=4)}

\codeassignment{Use the tool provided above to try and find the best
fit you can to the data. Explore the parameter space and give the weight values
you used for the 

(a) polynomial basis
(b) Radial basis
(c) Fourier basis

Write your answers in the code box below creating a new vector of parameters (in the correct order!) for each basis.}{
# (a) polynomial
###### Edit these lines #####
# w_0 =
# w_1 = 
# w_2 = 
# w_3 =
##############################
# w_polynomial = np.asarray([[w_0], [w_1], [w_2], [w_3]]) 

# (b) radial
###### Edit these lines #####
# w_0 =
# w_1 = 
# w_2 = 
# w_3 =
##############################
# w_rbf = np.asarray([[w_0], [w_1], [w_2], [w_3]]) 

# (c) fourier
###### Edit these lines #####
# w_0 =
# w_1 = 
# w_2 = 
# w_3 =
##############################
# w_fourier = np.asarray([[w_0], [w_1], [w_2], [w_3]])}{15}

\code{np.asarray([[1, 2, 3, 4]]).shape}

\subsection{Basis Function Models}

\slides{* The *prediction function* is now defined as }
  $$
  \mappingFunction(\inputVector_i) = \sum_{j=1}^\numBasisFunc \mappingScalar_j \basisFunc_{i, j}
  $$

\newslide{Vector Notation}
\slides{
* Write in vector notation,}
  $$
  \mappingFunction(\inputVector_i) = \mappingVector^\top \basisVector_i
  $$

\subsection{Log Likelihood for Basis Function Model}

\notes{The likelihood of a single data point given the model parameters is given by}\slides{* The likelihood of a single data point is}
  $$
  p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\basisVector_i\right)^{2}}{2\dataStd^2}\right).
  $$
\notes{and making an assumption of *conditional independence* given the parameters we can write} 
\newslide{Log Likelihood for Basis Function Model}
\slides{
* Leading to a log likelihood for the data set of}
  $$
  L(\mappingVector,\dataStd^2)= -\frac{\numData}{2}\log \dataStd^2-\frac{\numData}{2}\log 2\pi -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisVector_i\right)^{2}}{2\dataStd^2}.
  $$
\notes{to give us the likelihood for the whole data set.}

\subsection{Objective Function}

\notes{Traditionally in optimization, we choose to minmize an object function (or loss function, or cost function) rather than maximizing a likelihood. For these models we *minimize the negative log likelihood*. This function takes the form,}
\slides{* And a corresponding *objective function* of the form}
$$
\errorFunction(\mappingVector,\dataStd^2)= \frac{\numData}{2}\log\dataStd^2 + \frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisVector_i\right)^{2}}{2\dataStd^2}.
$$

\newslide{Expand the Brackets}
\notes{To minimize this objective, we first expand the brackets as follows,}
$$
\begin{align}
  \errorFunction(\mappingVector,\dataStd^2) = &\frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i\mappingVector^{\top}\basisVector_i\\ &+\frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\mappingVector^{\top}\basisVector_i\basisVector_i^{\top}\mappingVector+\text{const}.
\end{align}
$$

\newslide{Expand the Brackets}
\notes{Now we pull out the vectors, $\mappingVector$, to highlight that what we have is a multivariate quadratic form in $\mappingVector$.}
$$\begin{align} \errorFunction(\mappingVector, \dataStd^2) = & \frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2} \mappingVector^\top\sum_{i=1}^{\numData}\basisVector_i \dataScalar_i\\ & +\frac{1}{2\dataStd^2}\mappingVector^{\top}\left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector+\text{const}.\end{align}$$

\subsection{Design Matrices}

\notes{We like to make use of *design* matrices for our data. Design matrices involve placing the data points into rows of the matrix and data features into the columns of the matrix. By convention, we are referincing a vector with a bold lower case letter, and a matrix with a bold upper case letter. The design matrix is therefore given by}\slides{* Design matrix notation}
  $$
  \basisMatrix = \begin{bmatrix} \mathbf{1} & \inputVector & \inputVector^2\end{bmatrix}
  $$
  so that
  $$
  \basisMatrix \in \Re^{\numData \times \dataDim}.
  $$
  
\subsubsection{Multivariate Derivatives Reminder}

\notes{To find the minimum of the objective function, we need to make use of multivariate calculus. The two results we need from multivariate calculus have the following form.}
\slides{* We will need some multivariate calculus.}
  $$\frac{\text{d}\mathbf{a}^{\top}\mappingVector}{\text{d}\mappingVector}=\mathbf{a}$$
  and
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
  or if $\mathbf{A}$ is symmetric (*i.e.* $\mathbf{A}=\mathbf{A}^{\top}$)
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$

\subsection{Differentiate}

\notes{Differentiating with respect to the vector $\mappingVector$ we obtain}\slides{Differentiate wrt $\mappingVector$}
$$\frac{\text{d} E\left(\mappingVector,\dataStd^2 \right)}{\text{d}\mappingVector}=-\frac{1}{\dataStd^2} \sum_{i=1}^{\numData}\basisVector_i\dataScalar_i+\frac{1}{\dataStd^2} \left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector$$
Leading to
$$\mappingVector^{*}=\left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]^{-1}\sum_{i=1}^{\numData}\basisVector_i\dataScalar_i,$$

\newslide{Matrix Notation}

\notes{Rewriting this result in matrix notation we obtain:}
$$
\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^\top = \basisMatrix^\top \basisMatrix$$
$$\sum _{i=1}^{\numData}\basisVector_i\dataScalar_i = \basisMatrix^\top \dataVector
$$

\newslide{Update Equations}
\notes{Setting the derivative to zero we obtain update equations for the parameter vector and the noise variance.}
\slides{* Update for $\mappingVector^{*}$}
  $$
  \mappingVector^{*} = \left(\basisMatrix^\top \basisMatrix\right)^{-1} \basisMatrix^\top \dataVector
  $$
\slides{* The equation for $\left.\dataStd^2\right.^{*}$ may also be found}
  $$
  \left.\dataStd^2\right.^{{*}}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\basisVector_i\right)^{2}}{\numData}.
  $$

\newslide{Avoid Direct Inverse}
\notes{In practice we should avoid solving these equations through direct use of the inverse. Instead we solve for $\mappingVector$ in the following linear system.}
\slides{* E.g. Solve for $\mappingVector$}
  $$
  \left(\basisMatrix^\top \basisMatrix\right)\mappingVector = \basisMatrix^\top \dataVector
$$
\notes{Compare this system with *solve for* $\mathbf{x}$ in} 
$$
\mathbf{A}\mathbf{x} = \mathbf{b}.
$$
\notes{For example see the `numpy.linalg.solve` or `torch.linalg.solve`.}
\slides{* See `np.linalg.solve`
* In practice use $\mathbf{Q}\mathbf{R}$ decomposition (see lab class notes).}
\notes{But the correct and more stable approach is to make use of the QR decomposition.}

talk-macros.gpp}l/includes/qr-decomposition-regression.md}

talk-macros.gpp}l/includes/olympic-marathon-all-polynomial.md}

\subsection{Non-linear but Linear in the Parameters}

\notes{One rather nice aspect of our model is that whilst it is non-linear in the inputs, it is still linear in the parameters $\mappingVector$. This means that our derivations from before continue to operate to allow us to work with this model. In fact, although this is a non-linear regression it is still known as a *linear model* because it is linear in the parameters,}
\slides{* Model is non-linear, but linear in parameters}
$$
\mappingFunction(\inputVector) = \mappingVector^\top \basisVector(\inputVector)
$$
\slides{* $\inputVector$ is inside the non-linearity, but $\mappingVector$ is outside.}\notes{where the vector $\inputVector$ appears inside the basis functions, making our result, $\mappingFunction(\inputVector)$ non-linear in the inputs, but $\mappingVector$ appears outside our basis function, making our result *linear* in the parameters. In practice, our basis function itself may contain its own set of parameters,}
$$
\mappingFunction(\inputVector) = \mappingVector^\top \basisVector(\inputVector;
\boldsymbol{\theta}),
$$
\notes{that we've denoted here as $\boldsymbol{\theta}$. If these parameters appear inside the basis function then our model is *non-linear* in these parameters.}

\writeassignment{For the following prediction functions state whether
the model is linear in the inputs, the parameters or both.

(a) $\mappingFunction(\inputScalar) = \mappingScalar_1\inputScalar_1 + \mappingScalar_2$

(b) $\mappingFunction(\inputScalar) = \mappingScalar_1\exp(\inputScalar_1) + \mappingScalar_2\inputScalar_2 + \mappingScalar_3$

(c) $\mappingFunction(\inputScalar) =
\log(\inputScalar_1^{\mappingScalar_1}) + \mappingScalar_2\inputScalar_2^2 + \mappingScalar_3$

(d) $\mappingFunction(\inputScalar) = \exp(-\sum_i(\inputScalar_i - \mappingScalar_i)^2)$

(e) $\mappingFunction(\inputScalar) = \exp(-\mappingVector^\top \inputVector)$}{25}

\notes{
\subsection{Fitting the Model Yourself}

You now have everything you need to fit a non- linear (in the inputs) basis function model to the marathon data.}

\codeassignment{Choose one of the basis functions you have explored
above. Compute the design matrix on the covariates (or input data), `x`. Use the
design matrix and the response variable `y` to solve the following linear system
for the model parameters `w`.
$$
\basisVector^\top\basisVector\mappingVector = \basisVector^\top \dataVector
$$
Compute the corresponding error on the training data. How does it
compare to the error you were able to achieve fitting the basis above? Plot the
form of your prediction function from the least squares estimate alongside the
form of you prediction function you fitted by hand.}{}{35}

\endif
