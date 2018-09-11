\setupcode{import numpy as np
np.random.seed(4949)}

\setupcode{import teaching_plots as plot
import pods}

\include{_gp/includes/gaussian-predict-index-one-and-two.md}

\newslide{Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$}

\slidesmall{
* The single contour of the Gaussian density represents the \colorred{joint distribution, $p(\mappingFunction_1, \mappingFunction_2)$}

. . .

* We observe that \colorgreen{$\mappingFunction_1=?$}

. . .

* Conditional density: \colorred{$p(\mappingFunction_2|\mappingFunction_1=?)$}
}
	
\newslide{Prediction with Correlated Gaussians}

* Prediction of $\mappingFunction_2$ from $\mappingFunction_1$ requires *conditional density*.

* Conditional density is *also* Gaussian.
  $$
  p(\mappingFunction_2|\mappingFunction_1) = {\mathcal{N}\left(\mappingFunction_2|\frac{\kernelScalar_{1, 2}}{\kernelScalar_{1, 1}}\mappingFunction_1,\kernelScalar_{2, 2} - \frac{\kernelScalar_{1,2}^2}{\kernelScalar_{1,1}}\right)}
  $$
  where covariance of joint density is given by
  $$
  \kernelMatrix= \begin{bmatrix} \kernelScalar_{1, 1} & \kernelScalar_{1, 2}\\ \kernelScalar_{2, 1} & \kernelScalar_{2, 2}\end{bmatrix}
  $$

\include{../../_gp/includes/gaussian-predict-index-one-and-eight.md}

\newslide{Details}

* The single contour of the Gaussian density represents the \colorblue{joint distribution, $p(\mappingFunction_1, \mappingFunction_8)$}

. . .

* We observe a value for \colorgreen{$\mappingFunction_1=-?$}

. . .
	
* Conditional density: \colorred{$p(\mappingFunction_5|\mappingFunction_1=?)$}.

\newslide{Prediction with Correlated Gaussians}

* Prediction of $\mappingFunctionVector_*$ from $\mappingFunctionVector$ requires
    multivariate *conditional density*.

* Multivariate conditional density is *also* Gaussian. 
  <large>
  $$
  p(\mappingFunctionVector_*|\mappingFunctionVector) = {\mathcal{N}\left(\mappingFunctionVector_*|\kernelMatrix_{*,\mappingFunctionVector}\kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\mappingFunctionVector,\kernelMatrix_{*,*}-\kernelMatrix_{*,\mappingFunctionVector} \kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\kernelMatrix_{\mappingFunctionVector,*}\right)}
  $$
  </large>

* Here covariance of joint density is given by
  $$
  \kernelMatrix= \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector} & \kernelMatrix_{*, \mappingFunctionVector}\\ \kernelMatrix_{\mappingFunctionVector, *} & \kernelMatrix_{*, *}\end{bmatrix}
  $$

\newslide{Prediction with Correlated Gaussians}

* Prediction of $\mappingFunctionVector_*$ from $\mappingFunctionVector$ requires multivariate *conditional density*.

* Multivariate conditional density is *also* Gaussian. 
  <large>
  $$
  p(\mappingFunctionVector_*|\mappingFunctionVector) = {\mathcal{N}\left(\mappingFunctionVector_*|{\boldsymbol{{\mu}}},\boldsymbol{\Sigma}\right)}
  $$
  $$
  {\boldsymbol{{\mu}}}= \kernelMatrix_{*,\mappingFunctionVector}\kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\mappingFunctionVector
  $$
  $$\boldsymbol{\Sigma} = \kernelMatrix_{*,*}-\kernelMatrix_{*,\mappingFunctionVector} \kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\kernelMatrix_{\mappingFunctionVector,*}
  $$
  </large>

* Here covariance of joint density is given by
  $$
  \kernelMatrix= \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector} & \kernelMatrix_{*, \mappingFunctionVector}\\ \kernelMatrix_{\mappingFunctionVector, *} & \kernelMatrix_{*, *}\end{bmatrix}
  $$


