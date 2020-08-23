<!--frame start-->
### Standard Variational Approach Fails

-   &lt;1-&gt; Standard variational bound has the form:
    $$\likelihoodBound = \expDist{\log p(\dataVector|\latentMatrix)}{q(\latentMatrix)} + \KL{q(\latentMatrix)}{p(\latentMatrix)}$$

-   &lt;2-&gt; Requires expectation of
    $\log p(\dataVector|\latentMatrix)$ under $q(\latentMatrix)$.
    $$\log p(\dataVector|\latentMatrix) = -\frac{1}{2}\dataVector^\top\left(\kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector}+\dataStd^2\eye\right)^{-1}\dataVector -\frac{1}{2}\log \det{\kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector}+\dataStd^2 \eye} -\frac{\numData}{2}\log 2\pi$$

-   &lt;3-&gt; Extremely difficult to compute because
    $\kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector}$ is
    dependent on $\latentMatrix$ and appears in the inverse.

<!--frame end-->
<!--frame start-->
### Variational Bayesian GP-LVM

-   &lt;1-&gt;Consider collapsed variational bound, \only<1>{\[
              p(\dataVector)\geq \prod_{i=1}^\numData c_i \int \gaussianDist{\dataVector}{\expSamp{\mappingFunctionVector}}{\dataStd^2\eye}p(\inducingVector) \text{d}\inducingVector
              \]} \only<2>{\[
              p(\dataVector|\latentMatrix )\geq \prod_{i=1}^\numData c_i \int \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye}p(\inducingVector) \text{d}\inducingVector
              \]} \only<3->{\[
              \int p(\dataVector|\latentMatrix)p(\latentMatrix) \text{d}\latentMatrix \geq \int \prod_{i=1}^\numData c_i \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye} p(\latentMatrix)\text{d}\latentMatrix p(\inducingVector) \text{d}\inducingVector   
              \]}

-   &lt;4-&gt; Apply variational lower bound to the inner integral.
    \only<5->{\small\begin{align*}
              \int \prod_{i=1}^\numData c_i \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye}& p(\latentMatrix)\text{d}\latentMatrix\\ \geq & \expDist{\sum_{i=1}^\numData\log  c_i}{q(\latentMatrix)}\\& +\expDist{\log\gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector, \latentMatrix)}}{\dataStd^2\eye}}{q(\latentMatrix)}\\& + \KL{q(\latentMatrix)}{p(\latentMatrix)}    
              \end{align*}}

-   &lt;6-&gt; Which is analytically tractable for Gaussian
    $q(\latentMatrix)$ and some covariance functions.

<!--frame end-->
<!--frame start-->
### Required Expectations

-   Need expectations under $q(\latentMatrix)$ of:
    $$\log c_i = \frac{1}{2\dataStd^2} \left[\kernelScalar_{i, i} - \kernelVector_{i, \inducingVector}^\top \kernelMatrix_{\inducingVector, \inducingVector}^{-1} \kernelVector_{i, \inducingVector}\right]$$
    and
    $$\log \gaussianDist{\dataVector}{\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector,\dataMatrix)}}{\dataStd^2\eye} = -\frac{1}{2}\log 2\pi\dataStd^2 - \frac{1}{2\dataStd^2}\left(\dataScalar_i - \kernelMatrix_{\mappingFunctionVector, \inducingVector}\kernelMatrix_{\inducingVector,\inducingVector}^{-1}\inducingVector\right)^2$$

-   This requires the expectations
    $$\expDist{\kernelMatrix_{\mappingFunctionVector,\inducingVector}}{q(\latentMatrix)}$$
    and
    $$\expDist{\kernelMatrix_{\mappingFunctionVector,\inducingVector}\kernelMatrix_{\inducingVector,\inducingVector}^{-1}\kernelMatrix_{\inducingVector,\mappingFunctionVector}}{q(\latentMatrix)}$$
    which can be computed analytically for some covariance functions.

<!--frame end-->

