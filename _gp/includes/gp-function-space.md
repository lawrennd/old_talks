\ifndef{gpFunctionSpace}
\define{gpFunctionSpace}

\editme

\subsection{Gaussian Process}

\notes{In our \refnotes{session on Bayesian regression}{bayesian-regression} we sampled from the prior over paraemters. Through the properties of multivariate Gaussian densities this prior over parameters implies a particular density for our data observations, $\dataVector$. In this session we sampled directly from this distribution for our data, avoiding the intermediate weight-space representation. This is the approach taken by *Gaussian processes*. In a Gaussian process you specify the *covariance function* directly, rather than *implicitly* through a basis matrix and a prior over parameters. Gaussian processes have the advantage that they can be *nonparametric*, which in simple terms means that they can have *infinite* basis functions. In the lectures we introduced the *exponentiated quadratic* covariance, also known as the RBF or the Gaussian or the squared exponential covariance function. This covariance function is specified by}
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left( -\frac{\left\Vert \inputVector-\inputVector^\prime\right\Vert^2}{2\ell^2}\right),
$$
\notes{where $\left\Vert\inputVector - \inputVector^\prime\right\Vert^2$ is the squared distance between the two input vectors}
$$
\left\Vert\inputVector - \inputVector^\prime\right\Vert^2 = (\inputVector - \inputVector^\prime)^\top (\inputVector - \inputVector^\prime) 
$$
\notes{Let's build a covariance matrix based on this function. First we define the form of the covariance function,}

\loadcode{eq_cov}{mlai}

\notes{We can use this to compute *directly* the covariance for $\mappingFunctionVector$ at the points given by `x_pred`. Let's define a new function `K()` which does this,}

\loadcode{Kernel}{mlai}

\notes{Now we can image the resulting covariance,}

\code{kernel = Kernel(function=eq_cov, variance=1., lengthscale=10.)
K = kernel.K(x_pred, x_pred)}

\notes{To visualise the covariance between the points we can use the `imshow` function in matplotlib.}

\displaycode{fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(K, interpolation='none')
fig.colorbar(im)}

\notes{Finally, we can sample functions from the marginal likelihood.}

\displaycode{fig, ax = plt.subplots(figsize=(8, 5))
for i in range(10):
    y_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    ax.plot(x_pred.flatten(), y_sample.flatten())}

\exercise{**Moving Parameters** Have a play with the parameters for this
covariance function (the lengthscale and the variance) and see what effects the
parameters have on the types of functions you observe.}

\include{_gp/includes/gp-intro-very-short.md}


\subsection{Gaussian Process}

\notes{The Gaussian process perspective takes the marginal likelihood
of the data to be a joint Gaussian density with a covariance given by
$\kernelMatrix$. So the model likelihood is of the form,}
$$
p(\dataVector|\inputMatrix) =
\frac{1}{(2\pi)^{\frac{\numData}{2}}|\kernelMatrix|^{\frac{1}{2}}}
\exp\left(-\frac{1}{2}\dataVector^\top \left(\kernelMatrix+\dataStd^2
\eye\right)^{-1}\dataVector\right)
$$
\notes{where the input data, $\inputMatrix$,
influences the density through the covariance matrix, $\kernelMatrix$ whose
elements are computed through the covariance function, $\kernelScalar(\inputVector, \inputVector^\prime)$.}

\notes{This means that the negative log likelihood (the objective
function) is given by,}
$$
\errorFunction(\boldsymbol{\theta}) = \frac{1}{2} \log |\kernelMatrix|
+ \frac{1}{2} \dataVector^\top \left(\kernelMatrix +
\dataStd^2\eye\right)^{-1}\dataVector
$$
\notes{where the *parameters* of the model are also embedded in the
covariance function, they include the parameters of the kernel (such
as lengthscale and variance), and the noise variance, $\dataStd^2$.
Let's create a set of classes in python for storing these variables.}

\loadcode{Model}{mlai}
\loadcode{MapModel}{mlai}
\loadcode{ProbModel}{mlai}
\loadcode{ProbMapModel}{mlai}
\loadcode{GP}{mlai}

\subsection{Making Predictions}

\notes{We now have a probability density that represents
functions. How do we make predictions with this density? The density
is known as a process because it is *consistent*. By consistency,
here, we mean that the model makes predictions for
$\mappingFunctionVector$ that are unaffected by future values of
$\mappingFunctionVector^*$ that are currently unobserved (such as test
points). If we think of $\mappingFunctionVector^*$ as test points, we
can still write down a joint probability density over the training
observations, $\mappingFunctionVector$ and the test observations,
$\mappingFunctionVector^*$. This joint probability density will be
Gaussian, with a covariance matrix given by our covariance function,
$\kernelScalar(\inputVector_i, \inputVector_j)$.}
$$
\begin{bmatrix}\mappingFunctionVector \\ \mappingFunctionVector^*\end{bmatrix} \sim \gaussianSamp{\zerosVector}{\begin{bmatrix} \kernelMatrix & \kernelMatrix_\ast \\
\kernelMatrix_\ast^\top & \kernelMatrix_{\ast,\ast}\end{bmatrix}}
$$
\notes{where here $\kernelMatrix$ is the covariance computed between all the
training points, $\kernelMatrix_\ast$ is the covariance matrix
computed between the training points and the test points and
$\kernelMatrix_{\ast,\ast}$ is the covariance matrix computed betwen
all the tests points and themselves. To be clear, let's compute these
now for our example, using `x` and `y` for the training data (although
`y` doesn't enter the covariance) and `x_pred` as the test locations.}

\code{# set covariance function parameters
variance = 16.0
lengthscale = 8
# set noise variance
sigma2 = 0.05

kernel = Kernel(eq_cov, variance=variance, lengthscale=lengthscale)
K = kernel.K(x, x)
K_star = kernel.K(x, x_pred)
K_starstar = kernel.K(x_pred, x_pred)}

\notes{Now we use this structure to visualise the covariance between
test data and training data. This structure is how information is
passed between test and training data. Unlike the maximum likelihood
formalisms we've been considering so far, the structure expresses
*correlation* between our different data points.  However, just like
the \refnotes{naive Bayes approach}{naive-bayes} we now have a *joint
density* between some variables of interest. In particular we have the
joint density over $p(\mappingFunctionVector,
\mappingFunctionVector^*)$. The joint density is *Gaussian* and *zero
mean*. It is specified entirely by the *covariance matrix*,
$\kernelMatrix$. That covariance matrix is, in turn, defined by a
covariance function. Now we will visualise the form of that covariance
in the form of the matrix,}
$$
\begin{bmatrix} \kernelMatrix & \kernelMatrix_\ast \\ \kernelMatrix_\ast^\top
& \kernelMatrix_{\ast,\ast}\end{bmatrix}
$$

\setupplotcode{import mlai}

\plotcode{fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(np.vstack([np.hstack([K, K_star]), np.hstack([K_star.T, K_starstar])]), interpolation='none')
# Add lines for separating training and test data
ax.axvline(x.shape[0]-1, color='w')
ax.axhline(x.shape[0]-1, color='w')
fig.colorbar(im)

mlai.write_figure('block-predictive-covariance.svg', diagrams='\writeDiagramsDir/gp')
}

\figure{\includediagram{\diagramsDir/gp/block-predictive-covariance}{80%}}{Different blocks of the covariance function. The upper left block is the covariance of the training data with itself, $\kernelMatrix$. The top right is the cross covariance between training data (rows) and prediction locations (columns). The lower left is the same matrix transposed. The bottom right is the covariance matrix of the test data with itself.}{block-predictive-covariance}

\notes{There are four blocks to this plot. The upper left block
is the covariance of the training data with itself,
$\kernelMatrix$. We see some structure here due to the missing data
from the first and second world wars. Alongside this covariance (to
the right and below) we see the cross covariance between the training
and the test data ($\kernelMatrix_*$ and $\kernelMatrix_*^\top$). This
is giving us the covariation between our training and our test
data. Finally the lower right block The banded structure we now
observe is because some of the training points are near to some of the
test points. This is how we obtain 'communication' between our
training data and our test data. If there is no structure in
$\kernelMatrix_*$ then our belief about the test data simply matches
our prior.}

\endif
