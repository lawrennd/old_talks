\ifndef{multivariateGaussianProperties}
\define{multivariateGaussianProperties}
\editme
\newslide{Multivariate Gaussian Properties}

\slides{* If}\notes{
Let's first of all review the properties of the multivariate Gaussian distribution that make linear Gaussian models easier to deal with. We'll return to the, perhaps surprising, result on the parameters within the nonlinearity, $\parameterVector$, shortly.

To work with linear Gaussian models, to find the marginal likelihood all you need to know is the following rules. If}
$$
\dataVector = \mappingMatrix \inputVector + \noiseVector,
$$
\slides{
* Assume}\notes{where $\dataVector$, $\inputVector$ and $\noiseVector$ are vectors and we assume that $\inputVector$ and $\noiseVector$ are drawn from multivariate Gaussians,}
$$
\begin{align}
\inputVector & \sim \gaussianSamp{\meanVector}{\covarianceMatrix}\\
\noiseVector & \sim \gaussianSamp{\zerosVector}{\covarianceMatrixTwo}
\end{align}
$$
\notes{then we know that $\dataVector$ is also drawn from a multivariate Gaussian with,}\slides{* Then}
$$
\dataVector \sim \gaussianSamp{\mappingMatrix\meanVector}{\mappingMatrix\covarianceMatrix\mappingMatrix^\top + \covarianceMatrixTwo}.
$$
\slides{If $\covarianceMatrixTwo=\dataStd^2\eye$, this is Probabilistic PCA [@Tipping:probpca99].}
\notes{With appropriately defined covariance, $\covarianceMatrixTwo$, this is actually the marginal likelihood for Factor Analysis, or Probabilistic Principal Component Analysis [@Tipping:probpca99], because we integrated out the inputs (or *latent* variables they would be called in that case).}


\endif

