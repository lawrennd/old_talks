\ifndef{priorSamplingBasis}
\define{priorSamplingBasis}
\editme

\newslide{Sampling the Prior}

\slides{
* Always useful to perform a ‘sanity check’ and sample from the prior before observing the data.
* Since $\dataVector = \basisMatrix \mappingVector + \noiseVector$ just need to sample
  $$
  \mappingVector \sim \gaussianSamp{0}{\alpha\eye}
  $$
  $$
  \noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2}
  $$ 
  with $\alpha=1$ and $\dataStd^2 = 0.01$.
}
\notes{
\subsection{Generating from the Model}

A very important aspect of probabilistic modelling is to *sample* from your model to see what type of assumptions you are making about your data. In this case that involves a two stage process.

1. Sample a candiate parameter vector from the prior.
2. Place the candidate parameter vector in the likelihood and sample functions conditiond on that candidate vector.
3. Repeat to try and characterise the type of functions you are generating.

Given a prior variance (as defined above) we can now  sample from the prior distribution and combine with a basis set to see what assumptions we are making about the functions *a priori* (i.e. before we've seen the data). Firstly we compute the basis function matrix. We will do it both for our training data, and for a range of prediction locations (`x_pred`).

\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']
num_data = x.shape[0]
num_pred_data = 100 # how many points to use for plotting predictions
x_pred = np.linspace(1890, 2016, num_pred_data)[:, None] # input locations for predictions}

now let's build the basis matrices. We define the polynomial basis as follows.

\code{def polynomial(x, num_basis=2, loc=0., scale=1.):
    degree=num_basis-1
    degrees = np.arange(degree+1)
	return ((x-loc)/scale)**degrees}

\setupcode{import mlai}

\code{loc=1950
scale=1
degree=4
basis = mlai.Basis(polynomial, number=degree+1, loc=loc, scale=scale)
Phi_pred = basis.Phi(x_pred)
Phi = basis.Phi(x)
}

\subsection{Sampling from the Prior}

Now we will sample from the prior to produce a vector $\mappingVector$ and use it to plot a function which is representative of our belief *before* we fit the data. To do this we are going to use the properties of the Gaussian density and a sample from a *standard normal* using the function `np.random.normal`.

\subsection{Scaling Gaussian-distributed Variables}

First, let's consider the case where we have one data point and one feature in our basis set. In otherwords $\mappingFunctionVector$ would be a scalar, $\mappingVector$ would be a scalar and $\basisMatrix$ would be a scalar. In this case we have 
$$
\mappingFunction = \basisScalar \mappingScalar
$$
If $\mappingScalar$ is drawn from a normal density, 
$$
\mappingScalar \sim \gaussianSamp{\meanScalar_\mappingScalar}{c_\mappingScalar}
$$
and $\basisScalar$ is a scalar value which we are given, then properties of the Gaussian density tell us that 
$$
\basisScalar \mappingScalar \sim \gaussianSamp{\basisScalar\meanScalar_\mappingScalar}{\basisScalar^2c_\mappingScalar}
$$
Let's test this out numerically. First we will draw 200 samples from a standard normal,

\code{w_vec = np.random.normal(size=200)}

We can compute the mean of these samples and their variance

\code{print('w sample mean is ', w_vec.mean())
print('w sample variance is ', w_vec.var())}

These are close to zero (the mean) and one (the variance) as you'd expect. Now compute the mean and variance of the scaled version,

\code{phi = 7
f_vec = phi*w_vec
print('True mean should be phi*0 = 0.')
print('True variance should be phi*phi*1 = ', phi*phi)
print('f sample mean is ', f_vec.mean())
print('f sample variance is ', f_vec.var())}

If you increase the number of samples then you will see that the sample mean and the sample variance begin to converge towards the true mean and the true variance. Obviously adding an offset to a sample from `np.random.normal` will change the mean. So if you want to sample from a Gaussian with mean `mu` and standard deviation `sigma` one way of doing it is to sample from the standard normal and scale and shift the result, so to sample a set of $\mappingScalar$ from a Gaussian with mean $\meanScalar$ and variance $\alpha$,
$$\mappingScalar \sim \gaussianSamp{\meanScalar}{\alpha}$$
We can simply scale and offset samples from the *standard normal*.

\code{mu = 4 # mean of the distribution
alpha = 2 # variance of the distribution
w_vec = np.random.normal(size=200)*np.sqrt(alpha) + mu
print('w sample mean is ', w_vec.mean())
print('w sample variance is ', w_vec.var())}

Here the `np.sqrt` is necesssary because we need to multiply by the standard deviation and we specified the variance as `alpha`. So scaling and offsetting a Gaussian distributed variable keeps the variable Gaussian, but it effects the mean and variance of the resulting variable. 

To get an idea of the overall shape of the resulting distribution, let's do the same thing with a histogram of the results.

\displaycode{%matplotlib inline}

\plotcode{import matplotlib.pyplot as plt
import mlai.plot}


\plotcode{# First the standard normal
z_vec = np.random.normal(size=1000) # by convention, in statistics, z is often used to denote samples from the standard normal
w_vec = z_vec*np.sqrt(alpha) + mu
# plot normalized histogram of w, and then normalized histogram of z on top
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.hist(w_vec, bins=30, density=True)
ax.hist(z_vec, bins=30, density=True)
_ = ax.legend(('$w$', '$z$'))}

Now re-run this histogram with 100,000 samples and check that the both histograms look qualitatively Gaussian.
}
\notes{
\subsection{Sampling from the Prior}

Let's use this way of constructing samples from a Gaussian to check what functions look like *a priori*. The process will be as follows. First, we sample a random vector $K$ dimensional from `np.random.normal`. Then we scale it by $\sqrt{\alpha}$ to obtain a prior sample of $\mappingVector$.

\code{K = degree + 1
z_vec = np.random.normal(size=K)
w_sample = z_vec*np.sqrt(alpha)
print(w_sample)}

Now we can combine our sample from the prior with the basis functions to create a function,

\plotcode{f_sample = np.dot(Phi_pred,w_sample)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x_pred.flatten(), f_sample.flatten(), 'r-', linewidth=3)}

This shows the recurring problem with the polynomial basis (note the scale on the left hand side!). Our prior allows relatively large coefficients for the basis associated with high polynomial degrees. Because we are operating with input values of around 2000, this leads to output functions of very high values. The fix we have used for this before is to rescale our data before we apply the polynomial basis to it. Above, we set the scale of the basis to 1. Here let's set it to 100 and try again.

\code{scale = 100.
basis = mlai.Basis(polynomial, number=degree+1, loc=loc, scale=scale)
Phi_pred = basis.Phi(x_pred)
Phi = basis.Phi(x)}

Now we need to recompute the basis functions from above,

\plotcode{f_sample = np.dot(Phi_pred, w_sample)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x_pred.flatten(), f_sample.flatten(), 'r-', linewidth=3)}

Now let's loop through some samples and plot various functions as samples from this system,

\plotcode{num_samples = 10
K = degree+1
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(num_samples):
    z_vec = np.random.normal(size=K)
    w_sample = z_vec*np.sqrt(alpha)
    f_sample = np.dot(Phi_pred,w_sample)
    _ = ax.plot(x_pred.flatten(), f_sample.flatten(), linewidth=2)
}

The predictions for the mean output can now be computed. We want the expected value of the predictions under the posterior distribution. In matrix form, the predictions can be computed as
$$
\mappingFunctionVector = \basisMatrix \mappingVector.
$$ 
This involves a matrix multiplication between a fixed matrix $\basisMatrix$ and a vector that is drawn from a distribution $\mappingVector$. Because $\mappingVector$ is drawn from a distribution, this imples that $\mappingFunctionVector$ should also be drawn from a distribution. There are two distributions we are interested in though. We have just been sampling from the *prior* distribution to see what sort of functions we get *before* looking at the data. In Bayesian inference, we need to computer the *posterior* distribution and sample from that density.
}

\endif
