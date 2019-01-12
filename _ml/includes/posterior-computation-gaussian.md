\ifndef{posteriorComputationGaussian}
\define{posteriorComputationGaussian}
\editme

\subsection{Computing the Posterior}

\notes{
We will now attampt to compute the *posterior distribution*. In the lecture we went through the maths that allows us to compute the posterior distribution for $\mappingVector$. This distribution is also Gaussian,}
$$
p(\mappingVector | \dataVector, \inputVector, \dataStd^2) = \gaussianDist{\mappingVector}{\meanVector_\mappingScalar}{\covarianceMatrix_\mappingScalar}
$$
\notes{with covariance, $\covarianceMatrix_\mappingScalar$, given by}\slides{with}
$$
\covarianceMatrix_\mappingScalar = \left(\dataStd^{-2}\basisMatrix^\top \basisMatrix + \alpha^{-1}\eye\right)^{-1}
$$ 
\notes{whilst the mean is given by}\slides{and}
$$
\meanVector_\mappingScalar = \covarianceMatrix_\mappingScalar \dataStd^{-2}\basisMatrix^\top \dataVector
$$ 
\notes{Let's compute the posterior covariance and mean, then we'll sample from these densities to have a look at the posterior belief about $\mappingVector$ once the data has been accounted for. Remember, the process of Bayesian inference involves combining the prior, $p(\mappingVector)$ with the likelihood, $p(\dataVector|\inputVector, \mappingVector)$ to form the posterior, $p(\mappingVector | \dataVector, \inputVector)$ through Bayes' rule,
$$
p(\mappingVector|\dataVector, \inputVector) = \frac{p(\dataVector|\inputVector, \mappingVector)p(\mappingVector)}{p(\dataVector)}
$$
We've looked at the samples for our function $\mappingFunctionVector = \basisMatrix\mappingVector$, which forms the mean of the Gaussian likelihood, under the prior distribution. I.e. we've sampled from $p(\mappingVector)$ and multiplied the result by the basis matrix. Now we will sample from the posterior density, $p(\mappingVector|\dataVector, \inputVector)$, and check that the new samples fit do correspond to the data, i.e. we want to check that the updated distribution includes information from the data set. First we need to compute the posterior mean and *covariance*.

\subsection{Bayesian Inference in the Univariate Case}

This video talks about Bayesian inference across the single parameter, the offset $c$, illustrating how the prior and the likelihood combine in one dimension to form a posterior.

\includeyoutube{AvlnFnvFw_0}{1024}{768}{15}

\subsection{Multivariate Bayesian Inference}

This section of the lecture talks about how we extend the idea of Bayesian inference for the multivariate case. It goes through the multivariate Gaussian and how to complete the square in the linear algebra as we managed below.

\includeyoutube{Os1iqgpelPw}{1024}{768}{1362}

The lecture informs us the the posterior density for $\mappingVector$ is given by a Gaussian density with covariance
$$
\covarianceMatrix_w = \left(\dataStd^{-2}\basisMatrix^\top \basisMatrix + \alpha^{-1}\eye\right)^{-1}
$$
and mean 
$$
\meanVector_w = \covarianceMatrix_w\dataStd^{-2}\basisMatrix^\top \dataVector.
$$
}

\codeassignment{Compute the covariance for $\mappingVector$ given the training data, call the resulting variable `w_cov`. Compute the mean for $\mappingVector$ given the training data. Call the resulting variable `w_mean`. Assume that $\dataStd^2 = 0.01$}{1}{10}{sigma2 = 
w_cov = 
w_mean = 
}


\endif
