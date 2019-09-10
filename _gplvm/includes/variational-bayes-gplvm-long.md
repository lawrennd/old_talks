\ifndef{variationalBayesGplvmLong}
\define{variationalBayesGplvmLong}
\editme

\subsection{Standard Variational Approach Fails}

- Standard variational bound has the form:
  $$
  \likelihoodBound = \expDist{\log p(\dataVector|\latentMatrix)}{q(\latentMatrix)} + \KL{q(\latentMatrix)}{p(\latentMatrix)}
  $$

\newslide{Standard Variational Approach Fails}
\notes{The standard variational approach would require the expectation of $\log p(\dataVector|\latentMatrix)$ under $q(\latentMatrix)$.}\slides{
* Requires expectation of $\log p(\dataVector|\latentMatrix)$ under $q(\latentMatrix)$.}
  $$
  \begin{align}
  \log p(\dataVector|\latentMatrix) = & -\frac{1}{2}\dataVector^\top\left(\kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector}+\dataStd^2\eye\right)^{-1}\dataVector \\ & -\frac{1}{2}\log \det{\kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector}+\dataStd^2 \eye} -\frac{\numData}{2}\log 2\pi
  \end{align}
  $$
  \slides{$\kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector}$ is dependent on $\latentMatrix$ and it appears in the inverse.}\notes{But this is extremely difficult to compute because $\kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector}$ is dependent on $\latentMatrix$ and it appears in the inverse.}

\subsection{Variational Bayesian GP-LVM}
\notes{The alternative approach is to consider the collapsed variational bound (used for low rank (sparse is a misnomer) Gaussian process approximations.}\slides{* Consider collapsed variational bound,}
  \fragmentindex{\slidesmall{$$
    p(\dataVector)\geq \prod_{i=1}^\numData c_i \int \gaussianDist{\dataVector}{\expSamp{\mappingFunctionVector}}{\dataStd^2\eye}p(\inducingVector) \text{d}\inducingVector
  $$}}{}{1} 
  \fragmentindex{\slidesmall{$$
    p(\dataVector|\latentMatrix )\geq \prod_{i=1}^\numData c_i \int \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye}p(\inducingVector) \text{d}\inducingVector
  $$}}{}{2}
  \fragmentindex{\slidesmall{$$
      \int p(\dataVector|\latentMatrix)p(\latentMatrix) \text{d}\latentMatrix \geq \int \prod_{i=1}^\numData c_i \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye} p(\latentMatrix)\text{d}\latentMatrix p(\inducingVector) \text{d}\inducingVector
  $$}}{}{3}
\newslide{Variational Bayesian GP-LVM}
\notes{To integrate across $\latentMatrix$ we apply the lower bound to the inner integral.}\slides{* Apply variational lower bound to the inner integral.}
  \slidesmall{$$
	\begin{align}
    \int & \prod_{i=1}^\numData c_i \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye} p(\latentMatrix)\text{d}\latentMatrix\\ \geq & \expDist{\sum_{i=1}^\numData\log  c_i}{q(\latentMatrix)}\\& +\expDist{\log\gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye}}{q(\latentMatrix)}\\& + \KL{q(\latentMatrix)}{p(\latentMatrix)}    
    \end{align}
  $$}
* Which is analytically tractable for Gaussian
    $q(\latentMatrix)$ and some covariance functions.

\newslide{Required Expectations}

* Need expectations under $q(\latentMatrix)$ of:
  $$\log c_i = \frac{1}{2\dataStd^2} \left[\kernelScalar_{i, i} - \kernelVector_{i, \inducingVector}^\top \kernelMatrix_{\inducingVector, \inducingVector}^{-1} \kernelVector_{i, \inducingVector}\right]$$
  and
  $$
  \log \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector,\dataMatrix)}}{\dataStd^2\eye} = -\frac{1}{2}\log 2\pi\dataStd^2 - \frac{1}{2\dataStd^2}\left(\dataScalar_i - \kernelMatrix_{\mappingFunctionVector, \inducingVector}\kernelMatrix_{\inducingVector,\inducingVector}^{-1}\inducingVector\right)^2
  $$

\newslide{Required Expectations}

* This requires the expectations
  $$
  \expDist{\kernelMatrix_{\mappingFunctionVector,\inducingVector}}{q(\latentMatrix)}
  $$
  and
  $$
  \expDist{\kernelMatrix_{\mappingFunctionVector,\inducingVector}\kernelMatrix_{\inducingVector,\inducingVector}^{-1}\kernelMatrix_{\inducingVector,\mappingFunctionVector}}{q(\latentMatrix)}
  $$
  which can be computed analytically for some covariance functions [@Damianou:variational15] or through sampling [@Damianou:thesis2015;@Salimbeni:doubly2017].

\endif

