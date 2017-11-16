### Gaussian $p(\dataScalar_i|\mappingFunction_i)$

For Gaussian likelihoods: \only<1->{\[
  {\only<1>{\color{\blueColor}}\expDist{\log p(\dataScalar_i|\mappingFunction_i)}{p(\mappingFunction_i|\inducingVector)}} = -\frac{1}{2}\log 2\pi\dataStd^2 - \frac{1}{2\dataStd^2}\left(\dataScalar_i - \expSamp{\mappingFunction_i}\right)^2 - \frac{1}{2\dataStd^2} \left(\expSamp{\mappingFunction_i^2} - \expSamp{\mappingFunction_i}^2\right)
  \]} \only<2->{Implying:
    \[
  p(\dataScalar_i|\inducingVector) \geq \exp\expSamp{\log c_i}\gaussianDist{\dataScalar_i}{\expSamp{\mappingFunction_i}}{ \dataStd^2}
  \]}

### Gaussian Process Over $\mappingFunctionVector$ and $\inducingVector$

Define:
$$q_{i, i} = \varianceDist{\mappingFunction_i}{p(\mappingFunction_i|\inducingVector)} = \expDist{\mappingFunction_i^2}{p(\mappingFunction_i|\inducingVector)} - \expDist{\mappingFunction_i}{p(\mappingFunction_i|\inducingVector)}^2$$
We can write: $$c_i = \exp\left(-{\frac{q_{i,i}}{2\dataStd^2}}\right)$$
If joint distribution of $p(\mappingFunctionVector, \inducingVector)$ is
Gaussian then:
$$q_{i, i} = \kernelScalar_{i, i} - \kernelVector_{i, \inducingVector}^\top \kernelMatrix_{\inducingVector, \inducingVector}^{-1} \kernelVector_{i, \inducingVector}$$

$c_i$ is not a function of $\inducingVector$ but *is* a function of
$\inputMatrix_\inducingVector$.

<!--frame end-->
<!--frame start-->
### Total Conditional Variance

-   The sum of $q_{i,i}$ is the *total conditional variance*.

-   If conditional density $p(\mappingFunctionVector|\inducingVector)$
    is Gaussian then it has covariance
    $$\mathbf{Q} = \kernelMatrix_{\mappingFunctionVector\mappingFunctionVector} - \kernelMatrix_{\mappingFunctionVector \inducingVector}\kernelMatrix_{\inducingVector\inducingVector}^{-1} \kernelMatrix_{\inducingVector\mappingFunctionVector}$$

-   $\trace{\mathbf{Q}} = \sum_{i}q_{i,i}$ is known as total variance.

-   Because it is on conditional distribution we call it *total
    conditional variance*.

<!--frame end-->
<!--frame start-->
### Capacity of a Density

-   Measure the ’capacity of a density’.

-   Determinant of covariance represents ’volume’ of density.

-   log determinant is entropy: sum of *log* eigenvalues of covariance.

-   trace of covariance is total variance: sum of eigenvalues of
    covariance.

-   $\lambda > \log \lambda$ then total conditional variance upper
    bounds entropy.

<!--frame end-->
<!--frame start-->
### Alternative View

Exponentiated total variance bounds determinant.
$$\det{\mathbf{Q}} < \exp \trace{\mathbf{Q}}$$ Because
$$\prod_{i=1}^k \lambda_i < \prod_{i=1}^k \exp(\lambda_i)$$ where
$\{\lambda_i\}_{i=1}^k$ are the *positive* eigenvalues of $\mathbf{Q}$
This in turn implies
$$\det{\mathbf{Q}} < \prod_{i=1}^k \exp\left(q_{i,i}\right)$$

<!--frame end-->
<!--frame start-->
### Communication Channel

-   Conditional density $p(\mappingFunctionVector|\inducingVector)$ can
    be seen as a *communication channel*.

-   Normally we have: [\Large
    $$\text{Transmitter} \xrightarrow{\inducingVector} \begin{smallmatrix}p(\mappingFunctionVector|\inducingVector) \\ \text{Channel}\end{smallmatrix} \xrightarrow{\mappingFunctionVector} \text{Receiver}$$]{}
    and we control $p(\inducingVector)$ (the source density).

-   *Here* we can also control the transmission channel
    $p(\mappingFunctionVector|\inducingVector)$.

<!--frame end-->
<!--frame start-->
### Lower Bound on Likelihood

Substitute variational bound into marginal likelihood:
$$p(\dataVector)\geq \prod_{i=1}^\numData c_i \int \gaussianDist{\dataVector}{\expSamp{\mappingFunctionVector}}{\dataStd^2\eye}p(\inducingVector) \text{d}\inducingVector$$
Note that:
$$\expDist{\mappingFunctionVector}{p(\mappingFunctionVector|\inducingVector)} = \kernelMatrix_{\mappingFunctionVector, \inducingVector} \kernelMatrix_{\inducingVector, \inducingVector}^{-1}\inducingVector$$
is *linearly* dependent on $\inducingVector$.

<!--frame end-->
<!--frame start-->
### Deterministic Training Conditional

Making the marginalization of $\inducingVector$ straightforward. In the
Gaussian case:
$$p(\inducingVector) = \gaussianDist{\inducingVector}{\zerosVector}{\kernelMatrix_{\inducingVector,\inducingVector}}$$
\only<1>{\[
    \int p(\dataVector|\inducingVector) p(\inducingVector) \text{d}\inducingVector  \geq \prod_{i=1}^\numData c_i {\color{\blueColor}\int \gaussianDist{\dataVector}{\kernelMatrix_{\mappingFunctionVector, \inducingVector} \kernelMatrix^{-1}_{\inducingVector, \inducingVector}\inducingVector }{\dataStd^2} \gaussianDist{\inducingVector}{\zerosVector}{\kernelMatrix_{\inducingVector,\inducingVector}} \text{d}\inducingVector} \]}
\only<2->{\[
    \int p(\dataVector|\inducingVector) p(\inducingVector) \text{d}\inducingVector \geq \prod_{i=1}^\numData c_i {\color{\blueColor}\gaussianDist{\dataVector}{\zerosVector}{\dataStd^2\eye + \kernelMatrix_{\mappingFunctionVector, \inducingVector}\kernelMatrix^{-1}_{\inducingVector, \inducingVector}\kernelMatrix_{\inducingVector, \mappingFunctionVector}}} \]}
\only<3->{Maximize log of the bound to find covariance function parameters,}
\only<3-4>{\[
    \likelihoodFunction \geq \sum_{i=1}^\numData \log c_i + \log \gaussianDist{\dataVector}{\zerosVector}{\dataStd^2\eye + \kernelMatrix_{\mappingFunctionVector, \inducingVector}\kernelMatrix^{-1}_{\inducingVector, \inducingVector}\kernelMatrix_{\inducingVector, \mappingFunctionVector, } }
    \]} \only<5>{\[
    \likelihoodFunction \approx \log \gaussianDist{\dataVector}{\zerosVector}{\dataStd^2\eye + \kernelMatrix_{\mappingFunctionVector, \inducingVector}\kernelMatrix^{-1}_{\inducingVector, \inducingVector}\kernelMatrix_{\inducingVector, \mappingFunctionVector, } }
    \]} \only<5->{
    \begin{itemize}
      \item<5->If the bound is normalized, the $c_i$ terms are removed.
      \item<6->This results in the projected process approximation {\scriptsize \citep{Rasmussen:book06}} or DTC {\scriptsize \citep{Quinonero:unifying05}}. Proposed by {\scriptsize \citep{Smola:sparsegp00,Seeger:fast03,Csato:sparse02,Csato:thesis02}}.
      \end{itemize}}

<!--frame end-->

