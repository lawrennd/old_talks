---
layout: lecture
title: "Special Topics: Gaussian Processes"
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
venue: University of Sheffield
youtube: B2XhFoCehy8
week: 12
ipynb: True
date: 2015-12-15
abstract: 
postdir: ../../../mlatcl/mlai/_lectures/
slidedir: ../../../mlatcl/mlai/slides/
notedir: ../../../mlatcl/mlai/_notes/
notebookdir: ../../../mlatcl/mlai/_notebooks/
transition: None
---

\include{talk-macros.tex}

\subsection{Review}

* Last week: Logistic Regression and Generalised Linear Models
* Introduced link functions and different transformations.
* Showed examples in classification and mentioned possibilities for disease rate models.
* This week: 
    * Gaussian Processes: non parametric Bayesian modelling
}

\notes{Over the last two sessions we've begun considering classification models and logistic regresssion. In particular, for naive Bayes, we considered a set of assumptions that allowed us to build a joint model of our data set. In particular for naive Bayes we specified

1. Data conditional independence.
2. Feature conditional independence.
3. Marginal likelihood of labels was Bernoulli distributed.

This allowed us to specify the joint density of our labels and our input data, $p(\dataVector, \inputMatrix|\boldsymbol{\theta})$. And we conditioned on the training data to make predictions about the test data.}

\subsection{Generalized Linear Models}

Logistic regression is part of a wider class of models known as *generalized linear models*. In these models we determine that some characteristic of the model is speicified by a function that is liniear in the parameters. So we might suggest that
$$
\log \frac{p(\inputVector)}{1-p(\inputVector)} = \mappingFunction(\inputVector; \mappingVector)
$$
where $\mappingFunction(\inputVector; \mappingVector)$ is a linear-in-the-parameters function (here the
parameters are $\mappingVector$, which is generally non-linear in the inputs. So far
we have considered basis function models of the form
$$
\mappingFunction(\inputVector) =
\mappingVector^\top \basisVector(\inputVector).
$$
\notes{When we form a Gaussian process we do something that is slightly more akin to the naive Bayes approach, but actually is closely related to the generalized linear model approach.}

\include{_gp/includes/gp-intro-lectures.md}
\include{_gp/includes/gptwopointpred.md}


\subsection{Marginal Likelihood}

\notes{To understand the Gaussian process we're going to build on our understanding of the marginal likelihood for Bayesian regression. In the session on \refnotes{Bayesian regression}{bayesian-regression} we sampled directly from the weight vector, $\mappingVector$ and applied it to the basis matrix $\basisMatrix$ to obtain a sample from the prior and a sample from the posterior. It is often helpful to think of modeling techniques as *generative* models. To give some thought as to what the process for obtaining data from the model is. From the perspective of Gaussian processes, we want to start by thinking of basis function models, where the parameters are sampled from a prior, but move to thinking about sampling from the marginal likelihood directly.}

\subsection{Sampling from the Prior}

\notes{The first thing we'll do is to set up the parameters of the model, these include the parameters of the prior, the parameters of the basis functions and the noise level.}

\code{# set prior variance on w
alpha = 4.
# set the order of the polynomial basis set
degree = 5
# set the noise variance
sigma2 = 0.01}

\notes{Now we have the variance, we can sample from the prior distribution to see what form we are imposing on the functions *a priori*.

Let's now compute a range of values to make predictions at, spanning the *new*
space of inputs,}

\setupcode{import numpy as np}
\code{def polynomial(x, degree, loc, scale):
    degrees = np.arange(degree+1)
    return ((x-loc)/scale)**degrees}

\notes{now let's build the basis matrices. First we load in the data}

\setupcode{import pods}
\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']}

\code{loc = 1950.
scale = 100.
num_data = x.shape[0]
num_pred_data = 100 # how many points to use for plotting predictions
x_pred = np.linspace(1880, 2030, num_pred_data)[:, None] # input locations for predictions
Phi_pred = polynomial(x_pred, degree=degree, loc=loc, scale=scale)
Phi = polynomial(x, degree=degree, loc=loc, scale=scale)}

\subsection{Weight Space View}

\notes{To generate typical functional predictions from the model, we need a set of model parameters. We assume that the parameters are drawn independently from a Gaussian density,}
$$
\weightVector \sim \gaussianSamp{\zerosVector}{\alpha\eye},
$$
\notes{then we can combine this with the
definition of our prediction function $\mappingFunction(\inputVector)$,}
$$
\mappingFunction(\inputVector) =
\weightVector^\top \basisVector(\inputVector).
$$
\notes{We can now sample from the
prior density to obtain a vector $\weightVector$ using the function
`np.random.normal` and combine these parameters with our basis to create some
samples of what $\mappingFunction(\inputVector)$ looks like,}

\setupdisplaycode{import matplotlib.pyplot as plt
%matplotlib inline}
\displaycode{num_samples = 10
K = degree+1
for i in range(num_samples):
    z_vec = np.random.normal(size=(K, 1))
    w_sample = z_vec*np.sqrt(alpha)
    f_sample = np.dot(Phi_pred,w_sample)
    plt.plot(x_pred, f_sample)}


\subsection{Function Space View}

\notes{The process we have used to generate the samples is a
two stage process. To obtain each function, we first generated a sample from the
prior,}
$$
\weightVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}
$$
\notes{then if we compose our basis matrix, $\basisMatrix$ from the basis
functions associated with each row then we get,}
$$
\basisMatrix = \begin{bmatrix}\basisVector(\inputVector_1) \\ \vdots \\
\basisVector(\inputVector_n)\end{bmatrix}
$$
\notes{then we can write down the vector of function values, as evaluated at}
$$
\mappingFunctionVector = \begin{bmatrix} \mappingFunction_1
\\ \vdots \mappingFunction_n\end{bmatrix}
$$
in the form
$$
\mappingFunctionVector = \basisMatrix
\weightVector.
$$}

\notes{Now we can use standard properties of multivariate Gaussians to
write down the probability density that is implied over $\mappingFunctionVector$. In particular we know that if $\weightVector$ is sampled from a multivariate normal (or multivariate Gaussian) with covariance $\alpha \eye$ and zero mean,
then assuming that $\basisMatrix$ is a deterministic matrix (i.e. it is not
sampled from a probability density) then the vector $\mappingFunctionVector$ will also be distributed according to a zero mean multivariate normal as follows,}
$$
\mappingFunctionVector \sim \gaussianSamp{\zerosVector}{\alpha \basisMatrix\basisMatrix^\top}.
$$

\notes{The question now is, what happens if we sample $\mappingFunctionVector$ directly from this density, rather than first sampling $\weightVector$ and then multiplying by $\basisMatrix$. Let's try this. First of all we define the covariance as}
$$
\kernelMatrix = \alpha
\basisMatrix\basisMatrix^\top.
$$

\code{K = alpha*np.dot(Phi_pred, Phi_pred.T)}

\notes{Now we can use the `np.random.multivariate_normal` command for
sampling from a multivariate normal with covariance given by
$\kernelMatrix$ and zero mean,}

\code{for i in np.arange(10):
    f_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    plt.plot(x_pred.flatten(), f_sample.flatten())}

\notes{The samples appear very similar to those which we obtained indirectly. That is no surprise because they are effectively drawn from the same mutivariate normal density. However, when sampling $\mappingFunctionVector$ directly we created the covariance for $\mappingFunctionVector$. We can visualise the form of this covaraince in an image in python with a colorbar to show scale.}

\code{fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(K, interpolation='none')
fig.colorbar(im)}

\notes{This image is the covariance expressed between different points on the function. In regression we normally also add independent Gaussian noise to obtain our observations $\dataVector$,
$$
\dataVector = \mappingFunctionVector + \boldsymbol{\epsilon}
$$
\notes{where the noise is sampled from an independent Gaussian distribution with
variance $\dataStd^2$,}
$$
\epsilon \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}.
$$
\notes{we can use properties of Gaussian variables, i.e. the fact that
sum of two Gaussian variables is also Gaussian, and that it's covariance is
given by the sum of the two covariances, whilst the mean is given by the sum of
the means, to write down the marginal likelihood,}
$$
\dataVector \sim \gaussianSamp{\zerosVector}{\basisMatrix\basisMatrix^\top +\dataStd^2\eye}.
$$
\notes{Sampling directly from this density gives us the noise
corrupted functions,}

\code{K = alpha*np.dot(Phi_pred, Phi_pred.T) + sigma2*np.eye(x_pred.size)
for i in range(10):
    y_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    plt.plot(x_pred.flatten(), y_sample.flatten())}

\notes{where the effect of our noise term is to roughen the sampled functions, we can also increase the variance of the noise to see a different effect,}

\code{sigma2 = 1.
K = alpha*np.dot(Phi_pred, Phi_pred.T) + sigma2*np.eye(x_pred.size)
for i in range(10):
    y_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    plt.plot(x_pred.flatten(), y_sample.flatten())}

\exercise{**Function Space Reflection** How do you include the noise term when sampling in the weight space point of view?}

\include{_gp/includes/non-degenerate-gps.md}

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

\displaycode{fig, ax = plt.subplots(figsize(8, 5))
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
Let's create a class in python for storing these variables.}

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

\displaycode{fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(np.vstack([np.hstack([K, K_star]), np.hstack([K_star.T, K_starstar])]), interpolation='none')
# Add lines for separating training and test data
ax.axvline(x.shape[0]-1, color='w')
ax.axhline(x.shape[0]-1, color='w')
fig.colorbar(im)}

\notes{There are four blocks to this color plot. The upper left block
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

\subsection{Conditional Density}

\notes{Just as in naive Bayes, we first defined the joint density
(although there it was over both the labels and the inputs,
$p(\dataVector, \inputMatrix)$ and now we need to define *conditional*
distributions that answer particular questions of interest. In
particular we might be interested in finding out the values of the
function for the prediction function at the test data given those at
the training data,
$p(\mappingFunctionVector_*|\mappingFunctionVector)$. Or if we include
noise in the training observations then we are interested in the
conditional density for the prediction function at the test locations
given the training observations,
$p(\mappingFunctionVector^*|\dataVector)$.}

\notes{As ever all the various questions we could ask about this density can
be answered using the *sum rule* and the *product rule*.  For the
multivariate normal density the mathematics involved is that of
*linear algebra*, with a particular emphasis on the *partitioned
inverse* or
[*block matrix inverse*](http://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion),
but they are beyond the scope of this course, so you don't need to
worry about remembering them or rederiving them. We are simply writing
them here because it is this *conditional* density that is necessary
for making predictions.}

\notes{The conditional density is also a multivariate normal,}
$$
\mappingFunctionVector^* | \mappingFunctionVector \sim \gaussianSamp{\meanVector_\mappingFunction}{\mathbf{C}_\mappingFunction}
$$
with a mean given by
$$
\meanVector_\mappingFunction = \kernelMatrix_*^\top \left[\kernelMatrix + \dataStd^2
\eye\right]^{-1} \dataVector
$$
and a covariance given by 
$$
\mathbf{C}_\mappingFunction
= \kernelMatrix_{*,*} - \kernelMatrix_*^\top \left[\kernelMatrix + \dataStd^2
\eye\right]^{-1} \kernelMatrix_\ast.
$$
\notes{Let's compute what those posterior predictions are for the olympic marathon data.}

\loadcode{posterior_f}{mlai}

\code{# attach the new method to class GP():
GP.posterior_f = posterior_f}

\code{model = GP(x, y, sigma2, exponentiated_quadratic, variance=variance, lengthscale=lengthscale)
mu_f, C_f = model.posterior_f(x_pred)
}

\notes{where for convenience we've defined}

$$
\mathbf{A} = \left[\kernelMatrix + \dataStd^2\eye\right]^{-1}\kernelMatrix_*.
$$ 

\notes{We can visualize the covariance of the *conditional*,}

\displaycode{fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(C_f, interpolation='none')
fig.colorbar(im)}

\notes{and we can plot the mean of the conditional}

\displaycode{plt.plot(x, y, 'rx')
plt.plot(x_pred, mu_f, 'b-')}

\notes{as well as the associated error bars. These are given
(similarly to the Bayesian parametric model from the last lab) by the
standard deviations of the marginal posterior densities. The marginal
posterior variances are given by the diagonal elements of the
posterior covariance,}

\code{var_f = np.diag(C_f)[:, None]
std_f = np.sqrt(var_f)}

\notes{They can be added to the underlying mean function to give the error bars,}

\displaycode{plt.plot(x, y, 'rx')
plt.plot(x_pred, mu_f, 'b-')
plt.plot(x_pred, mu_f+2*std_f, 'b--')
plt.plot(x_pred, mu_f-2*std_f, 'b--')}

\notes{This gives us a prediction from the Gaussian process. Remember machine learning is}
$$
\text{data} + \text{model} \rightarrow \text{prediction}.
$$
\notes{Here our data is from the olympics, and our model is a Gaussian
process with two parameters. The assumptions about the world are
encoded entirely into our Gaussian process covariance. The GP
covariance assumes that the function is highly smooth, and that
correlation falls off with distance (scaled according to the length
scale, $\ell$). The model sustains the uncertainty about the function,
this means we see an increase in the size of the error bars during
periods like the 1st and 2nd World Wars when no olympic marathon was
held. }

\exercise{Now try changing the parameters of the covariance function (and the
noise) to see how the predictions change.

Then try sampling from this conditional density to see what your predictions look like. What happens if you sample from the conditional density in regions a long way into the future or the past? How does this compare with the results from the polynomial model?}

\subsection{The Importance of the Covariance Function}

\notes{The covariance function encapsulates our assumptions about the data. The equations for the distribution of the prediction function, given the training observations, are highly sensitive to the covariation between the test locations and the training locations as expressed by the matrix $\kernelMatrix_*$. We defined a matrix $\mathbf{A}$ which allowed us to express our conditional mean in the form,}
$$
\meanVector_\mappingFunction = \mathbf{A}^\top \dataVector,
$$
\notes{where $\dataVector$ were our *training observations*. In other words our mean predictions are always a linear weighted combination of our *training data*. The weights are given by computing the covariation between the training and the test data ($\kernelMatrix_*$) and scaling it by the inverse covariance of the training data observations, $\left[\kernelMatrix + \dataStd^2 \eye\right]^{-1}$. This inverse is the main computational object that needs to be resolved for a Gaussian process. It has a computational burden which is $O(\numData^3)$ and a storage burden which is $O(\numData^2)$.  This makes working with Gaussian processes computationally intensive for the situation where $\numData>10,000$.}

\includeyoutube{ewJ3AxKclOg}

\subsection{Improving the Numerics}

In practice we shouldn't be using matrix inverse directly to solve the GP system. One more stable way is to compute the *Cholesky decomposition* of the kernel matrix. The log determinant of the covariance can also be derived from the Cholesky decomposition.

\loadcode{update_inverse}{mlai}

\code{GP.update_inverse = update_inverse}

\subsection{Capacity Control}

\notes{Gaussian processes are sometimes seen as part of a wider family of methods known as kernel methods. Kernel methods are also based around covariance functions, but in the field they are known as Mercer kernels. Mercer kernels have interpretations as inner products in potentially infinite dimensional Hilbert spaces. This interpretation arises because, if we take $\alpha=1$, then the kernel can be expressed as
$$
\kernelMatrix = \basisMatrix\basisMatrix^\top 
$$
which imples the elements of the kernel are given by,
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \basisVector(\inputVector)^\top \basisVector(\inputVector^\prime).
$$
So we see that the kernel function is developed from an inner product between the basis functions. Mercer's theorem tells us that any valid *positive definite function* can be expressed as this inner product but with the caveat that the inner product could be *infinite length*. This idea has been used quite widely to *kernelize* algorithms that depend on inner products. The kernel functions are equivalent to covariance functions and they are parameterized accordingly.  In the kernel modeling community it is generally accepted that kernel parameter estimation is a difficult problem and the normal solution is to cross validate to obtain parameters. This can cause difficulties when a large number of kernel parameters need to be estimated. In Gaussian process modelling kernel parameter estimation (in the simplest case proceeds) by maximum likelihood. This involves taking gradients of the likelihood with respect to the parameters of the covariance function.}


\subsection{Gradients of the Likelihood}

\notes{The easiest conceptual way to obtain the gradients is a two step process. The first step involves taking the gradient of the likelihood with respect to the covariance function, the second step involves considering the gradient of the covariance function with respect to its parameters.}

\subsection{Overall Process Scale}

\notes{In general we won't be able to find parameters of the covariance function through fixed point equations, we will need to do gradient based optimization.}

\subsection{Capacity Control and Data Fit}

\notes{The objective function can be decomposed into two terms, a capacity control term, and a data fit term. The capacity control term is the log determinant of the covariance. The data fit term is the matrix inner product between the data and the inverse covariance.}

\include{_gp/includes/gp-optimize.md}

\include{_kern/includes/eq-covariance.md}

\include{_gp/includes/olympic-marathon-gp.md}

\include{_gp/includes/della-gatta-gene-gp.md}
\include{_health/includes/malaria-gp.md}

\include{_kern/includes/add-covariance.md}
\include{_gp/includes/bda-forecasting.md}

\include{_kern/includes/basis-covariance.md}
\include{_kern/includes/brownian-covariance.md}
\include{_kern/includes/mlp-covariance.md}

\include{_gp/includes/gp-summer-school.md}
\include{_gp/includes/gpy-software.md}

\thanks

\references


