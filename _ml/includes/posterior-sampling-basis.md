\ifndef{posteriorSamplingBasis}
\define{posteriorSamplingBasis}
\editme

\subsection{Sampling from the Posterior}

\notes{
Before we were able to sample the prior values for the mean *independently* from a Gaussian using `np.random.normal` and scaling the result. However, observing the data *correlates* the parameters. Recall this from the first lab where we had a correlation between the offset, $c$ and the slope $m$ which caused such problems with the coordinate ascent algorithm. We need to sample from a *correlated* Gaussian. For this we can use `np.random.multivariate_normal`.

\plotcode{w_sample = np.random.multivariate_normal(w_mean.flatten(), w_cov)
f_sample = np.dot(Phi_pred,w_sample)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_pred.flatten(), f_sample.flatten(), 'r-', linewidth=3)
ax.plot(x, y, 'r.', markersize=10) # plot data to show fit.}

Now let's sample several functions and plot them all to see how the predictions fluctuate.

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(num_samples):
    w_sample = np.random.multivariate_normal(w_mean.flatten(), w_cov)
    f_sample = np.dot(Phi_pred,w_sample)
    ax.plot(x_pred.flatten(), f_sample.flatten(), linewidth=2)
ax.plot(x, y, 'r.', markersize=10) # plot data to show fit.}

This gives us an idea of what our predictions are. These are the predictions that are consistent with data and our prior. Try plotting different numbers of predictions. You can also try plotting beyond the range of where the data is and see what the functions do there. 

Rather than sampling from the posterior each time to compute our predictions, it might be better if we just summarised the predictions by the expected value of the output funciton, $\mappingFunction(x)$, for any particular input. If we can get formulae for this we don't need to sample the values of $\mappingFunction(x)$ we might be able to compute the distribution directly. Fortunately, in the Gaussian case, we can use properties of multivariate Gaussians to compute both the mean and the variance of these samples.

\subsection{Properties of Gaussian Variables}

Gaussian variables have very particular properties, that many other densities don't exhibit. Perhaps foremost amoungst them is that the sum of any Gaussian distributed set of random variables also turns out to be Gaussian distributed. This property is much rarer than you might expect.

\subsection{Sum of Gaussian-distributed Variables}

The sum of Gaussian random variables is also Gaussian, so if we have a random variable $\dataScalar_i$ drawn from a Gaussian density with mean $\meanScalar_i$ and variance $\dataStd^2_i$, 
$$
\dataScalar_i \sim \gaussianSamp{\meanScalar_i}{\dataStd^2_i}
$$
Then the sum of $K$ independently sampled values of $\dataScalar_i$ will be drawn from a Gaussian with mean $\sum_{i=1}^K \mu_i$ and variance $\sum_{i=1}^K \dataStd_i^2$,
$$
\sum_{i=1}^K \dataScalar_i \sim \gaussianSamp{\sum_{i=1}^K \meanScalar_i}{\sum_{i=1}^K \dataStd_i^2}.
$$
Let's try that experimentally. First let's generate a vector of samples from a standard normal distribution, $z \sim \gaussianSamp{0}{1}$,  then we will scale and offset them, then keep adding them into a vector `y_vec`.

\subsection{Sampling from Gaussians and Summing Up}

\code{K = 10 # how many Gaussians to add.
num_samples = 1000 # how many samples to have in y_vec
mus = np.linspace(0, 5, K) # mean values generated linearly spaced between 0 and 5
sigmas = np.linspace(0.5, 2, K) # sigmas generated linearly spaced between 0.5 and 2
y_vec = np.zeros(num_samples)
for mu, sigma in zip(mus, sigmas):
    z_vec = np.random.normal(size=num_samples) # z is from standard normal
    y_vec += z_vec*sigma + mu # add to y z*sigma + mu

# now y_vec is the sum of each scaled and off set z.
print('Sample mean is ', y_vec.mean(), ' and sample variance is ', y_vec.var())
print('True mean should be ', mus.sum())
print('True variance should be ', (sigmas**2).sum(), ' standard deviation ', np.sqrt((sigmas**2).sum())) }

Of course, we can histogram `y_vec` as well.

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.hist(y_vec, bins=30, normed=True)
ax.legend('$y$')}

\subsection{Matrix Multiplication of Gaussian Variables}

We are interested in what our model is saying about the sort of functions we are observing. The fact that summing of Gaussian variables leads to new Gaussian variables, and scaling of Gaussian variables *also* leads to Gaussian variables means that matrix multiplication (which is just a series of sums and scales) also leads to Gaussian densities. Matrix multiplication is just adding and scaling together, in the formula, $\mappingFunctionVector = \basisMatrix \mappingVector$ we can extract the first element from $\mappingFunctionVector$ as
$$
\mappingFunction_i = \basisVector_i^\top \mappingVector
$$
where $\basisVector$ is a column vector from the $i$th row of $\basisMatrix$ and $\mappingFunction_i$ is the $i$th element of $\mappingFunctionVector$.This vector inner product itself merely implies that 
$$
\mappingFunction_i = \sum_{j=1}^K \mappingScalar_j \basisScalar_{i, j}
$$
and if we now say that $\mappingScalar_i$ is Gaussian distributed, then because a scaled Gaussian is also Gaussian, and because a sum of Gaussians is also Gaussian, we know that $\mappingFunction_i$ is also Gaussian distributed. It merely remains to work out its mean and covariance. We can do this by looking at the expectation under a Gaussian distribution. The expectation of the mean vector is given by 
$$
\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \int \mappingFunctionVector
\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}
\text{d}\mappingVector = \int \basisMatrix\mappingVector
\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}
\text{d}\mappingVector = \basisMatrix \int \mappingVector
\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}
\text{d}\mappingVector = \basisMatrix \meanVector
$$

Which is straightforward. The expectation of $\mappingFunctionVector=\basisMatrix\mappingVector$ under the Gaussian distribution for $\mappingFunctionVector$ is simply $\mappingFunctionVector=\basisMatrix\meanVector$, where $\meanVector$ is the *mean* of the Gaussian density for $\mappingVector$. Because our prior distribution was Gaussian with zero mean, the expectation under the prior is given by 
$$
\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\zerosVector}{\alpha\eye}} = \zerosVector
$$

The covariance is a little more complicated. A covariance matrix is defined as
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}
= \expDist{\mappingFunctionVector\mappingFunctionVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}
- \expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}^\top
$$
we've already computed
$\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}=\basisMatrix \meanVector$ so we can substitute that in to recover
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \expDist{\mappingFunctionVector\mappingFunctionVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} - \basisMatrix \meanVector \meanVector^\top \basisMatrix^\top
$$

So we need the expectation of $\mappingFunctionVector\mappingFunctionVector^\top$. Substituting in $\mappingFunctionVector = \basisMatrix \mappingVector$ we have
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \expDist{\basisMatrix\mappingVector\mappingVector^\top \basisMatrix^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} - \basisMatrix \meanVector \meanVector^\top \basisMatrix^\top
$$
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \basisMatrix\expDist{\mappingVector\mappingVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} \basisMatrix^\top - \basisMatrix \meanVector \meanVector^\top\basisMatrix^\top
$$
Which is dependent on the second moment of the Gaussian,
$$
\expDist{\mappingVector\mappingVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \covarianceMatrix + \meanVector\meanVector^\top
$$
that can be substituted in to recover, 
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \basisMatrix\covarianceMatrix \basisMatrix^\top
$$
so in the case of the prior distribution, where we have $\covarianceMatrix = \alpha \eye$ we can write 
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\zerosVector}{\alpha \eye}} = \alpha \basisMatrix \basisMatrix^\top
$$

This implies that the prior we have suggested for $\mappingVector$, which is Gaussian with a mean of zero and covariance of $\alpha \eye$ suggests that the distribution for $\mappingVector$ is also Gaussian with a mean of zero and covariance of $\alpha \basisMatrix\basisMatrix^\top$. Since our observed output, $\dataVector$, is given by a noise corrupted variation of $\mappingFunctionVector$, the final distribution for $\dataVector$ is given as 
$$
\dataVector = \mappingFunctionVector + \noiseVector
$$
where the noise, $\noiseVector$, is sampled from a Gaussian density: $\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$. So, in other words, we are taking a Gaussian distributed random value $\mappingFunctionVector$, 
$$
\mappingFunctionVector \sim \gaussianSamp{\zerosVector}{\alpha\basisMatrix\basisMatrix^\top}
$$
and adding to it another Gaussian distributed value, $\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$, to form our data observations, $\dataVector$. Once again the sum of two (multivariate) Gaussian distributed variables is also Gaussian, with a mean given by the sum of the means (both zero in this case) and the covariance given by the sum of the covariances. So we now have that the marginal likelihood for the data, $p(\dataVector)$ is given by
$$
p(\dataVector) = \gaussianDist{\dataVector}{\zerosVector}{\alpha \basisMatrix \basisMatrix^\top + \dataStd^2\eye}
$$
This is our *implicit* assumption for $\dataVector$ given our prior assumption for $\mappingVector$.
}

\slides{
* Now check samples by extracting $\mappingVector$ from the *posterior*.
* Now for $\dataVector = \basisMatrix \mappingVector + \noiseVector$ need
  $$
  \mappingVector \sim \gaussianSamp{\meanVector_w}{\covarianceMatrix_w}
  $$
  with $\covarianceMatrix_w = \left[\dataStd^{-2}\basisMatrix^\top \basisMatrix + \alpha^{-1}\eye\right]^{-1}$
  and $\meanVector_w =\covarianceMatrix_w \dataStd^{-2} \basisMatrix^\top \dataVector$
  $$
  \noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}
  $$ 
  with $\alpha=1$ and $\dataStd^2 = 0.01$.
}
\endif
