\ifndef{gplvm}
\define{gplvm}

\editme

\section{Dual Probabilistic PCA and GP-LVM}

\subsection{Dual Probabilistic PCA}

**Probabilistic PCA**
  
* We have seen that PCA has a probabilistic interpretation [@Tipping:probpca99].
* It is difficult to `non-linearise' directly.
* GTM and Density Networks are an attempt to do so.

**Dual Probabilistic PCA**
  
* There is an alternative probabilistic interpretation of PCA [@Lawrence:pnpca05].
* This interpretation can be made non-linear.
* The result is non-linear probabilistic PCA.




\newslide{Linear Latent Variable Model III}
 
\columns{**Dual Probabilistic PCA**
    
* Define *linear-Gaussian relationship* between latent variables and data.
* **Novel** Latent variable approach:
* Define Gaussian prior over \emph{parameters}, $\mappingMatrix$.
* Integrate out *parameters*.}{\includepng{\diagramsDir/dimred/gplvm_graph}{50%}
$$
p\left(\dataMatrix|\latentMatrix,\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\mappingMatrix\latentVector_{i,:}}{\dataStd^{2}\eye}
$$
$$
 p\left(\mappingMatrix\right)=\prod_{i=1}^{\dataDim}\gaussianDist{\mappingVector_{i,:}}{\zerosVector}{\eye}$$
$$
 p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{\dataDim}\gaussianDist{\dataVector_{:,j}}{\zerosVector}{\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye}$$}{45%}{45%}

\notes{
\newslide{Linear Latent Variable Model IV}

\fragmentdiv{**Dual**}{1} Probabilistic PCA Max. Likelihood Soln \fragmentdiv{[@Lawrence:gplvm03,@Lawrence:pnpca05]}{1}
\includepng{\diagramsDir/dimred/gplvm_graph}{25%}
\slidesmall{\fragmentdiv{
$$
p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{\dataDim}\gaussianDist{\dataVector_{:,j}}{\zerosVector}{\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye}
$$
}{1}\fragmentdiv{
$$
p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{\dataDim}\gaussianDist{\dataVector_{:,j}}{\zerosVector}{\kernelMatrix},\quad\quad\kernelMatrix=\latentMatrix\mathbf{\latentMatrix}^{\top}+\dataStd^{2}\eye
$$
$$
\log p\left(\dataMatrix|\latentMatrix\right)=-\frac{\dataDim}{2}\log\left|\kernelMatrix\right|-\frac{1}{2}\tr{\kernelMatrix^{-1}\dataMatrix\dataMatrix^{\top}}+\mbox{const.}
$$
If $\eigenvectorMatrix_{\latentDim}^{\prime}$ are first $\latentDim$
principal eigenvectors of $\dataDim^{-1}\dataMatrix\dataMatrix^{\top}$
and the corresponding eigenvalues are $\Lambda_{\latentDim}$,
$$
\latentMatrix=\mathbf{U^{\prime}}_{\latentDim}\mathbf{L}\rotationMatrix^{\top},\quad\quad\mathbf{L}=\left(\Lambda_{\latentDim}-\dataStd^{2}\eye\right)^{\frac{1}{2}}
$$
where $\rotationMatrix$ is an arbitrary rotation matrix.
       }{2}\fragmentdiv{$$
p\left(\dataMatrix|\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\zerosVector}{\covarianceMatrix},\quad\quad\covarianceMatrix=\mappingMatrix\mappingMatrix^{\top}+\dataStd^{2}\eye$$
$$
\log p\left(\dataMatrix|\mappingMatrix\right)=-\frac{\numData}{2}\log\left|\covarianceMatrix\right|-\frac{1}{2}\tr{\covarianceMatrix^{-1}\dataMatrix^{\top}\dataMatrix}+\mbox{const.}
$$
If $\eigenvectorMatrix_{\latentDim}$ are first $\latentDim$ principal
eigenvectors of $\numData^{-1}\dataMatrix^{\top}\dataMatrix$
and the corresponding eigenvalues are $\Lambda_{\latentDim}$,
$$
\mappingMatrix=\eigenvectorMatrix_{\latentDim}\mathbf{L}\rotationMatrix^{\top},\quad\quad\mathbf{L}=\left(\Lambda_{\latentDim}-\dataStd^{2}\eye\right)^{\frac{1}{2}}
$$
where $\rotationMatrix$ is an arbitrary rotation matrix.}{3}}}




\newslide{Equivalence of Formulations}

**The Eigenvalue Problems are equivalent**
  
* Solution for Probabilistic PCA (solves for the mapping)
  $$
\dataMatrix^{\top}\dataMatrix\eigenvectorMatrix_{\latentDim}=\eigenvectorMatrix_{\latentDim}\Lambda_{\latentDim}\quad\quad\quad\mappingMatrix=\eigenvectorMatrix_{\latentDim}\mathbf{L}\mathbf{V}^{\top}
      $$

* Solution for Dual Probabilistic PCA (solves for the latent positions)
  $$
\dataMatrix\dataMatrix^{\top}\eigenvectorMatrix_{\latentDim}^{\prime}=\eigenvectorMatrix_{\latentDim}^{\prime}\Lambda_{\latentDim}\quad\quad\quad\latentMatrix=\eigenvectorMatrix_{\latentDim}^{\prime}\mathbf{L}\mathbf{V}^{\top}
    $$
    
* Equivalence is from
$$
\eigenvectorMatrix_{\latentDim}=\dataMatrix^{\top}\eigenvectorMatrix_{\latentDim}^{\prime}\Lambda_{\latentDim}^{-\frac{1}{2}}
    $$

talk-macros.gpp}p/includes/gp-intro-very-short.md}


\newslide{Gaussian Process (GP)}

**Prior for Functions**
  
* Probability Distribution over Functions
* Functions are infinite dimensional.

    
  * Prior distribution over *instantiations* of the function: finite
      dimensional objects.
  * Can prove by induction that GP is 'consistent'.
 
\newslide{Gaussian Process (GP) II}

* Mean and Covariance Functions
* Instead of mean and covariance matrix, GP is defined by mean function
    and covariance function.

    
  * Mean function often taken to be zero or constant.
  * Covariance function must be *positive definite*.
  * Class of valid covariance functions is the same as the class
      of *Mercer kernels*.
  




\newslide{Gaussian Processes III}

**Zero mean Gaussian Process**
  
* A (zero mean) Gaussian process likelihood is of the form$$
    p\left(\dataVector|\latentMatrix\right)=N\left(\dataVector|\mathbf{0},\kernelMatrix\right),$$
    where $\kernelMatrix$ is the covariance function or \emph{kernel}.
* The \emph{linear kernel} with noise has the form$$
    \kernelMatrix=\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye$$

* Priors over non-linear functions are also possible.

    
  * To see what functions look like, we can sample from the prior process.
  










\newslide{Gaussian Process Regression}

**Posterior Distribution over Functions**
  
* Gaussian processes are often used for regression.
* We are given a known inputs $\latentMatrix$ and targets $\dataMatrix$.
* We assume a prior distribution over functions by selecting a kernel.
* Combine the prior with data to get a \emph{posterior} distribution
    over functions.




talk-macros.gpp}ern/includes/eq-covariance.md}
talk-macros.gpp}p/includes/gp-optimize.md}


\newslide{Non-Linear Latent Variable Model}
  
\columns{\slidesmall{**Dual Probabilistic PCA**
* Define *linear-Gaussian relationship* between latent variables
and data.
* **Novel** Latent variable approach:
  * Define Gaussian prior over *parameteters*, $\mappingMatrix$.
  * Integrate out *parameters*.
  
* Inspection of the marginal likelihood shows ...
  * The covariance matrix is a covariance function.
  * We recognise it as the 'linear kernel'.
}}{\includepng{\diagramsDir/dimred/gplvm_graph}{50%}
\slidesmall{\fragmentdiv{$$
 p\left(\dataMatrix|\latentMatrix,\mappingMatrix\right)=\prod_{i=1}^{n}N\left(\dataVector_{i,:}|\mappingMatrix\latentVector_{i,:},\dataStd^{2}\eye\right)$$
 $$
 p\left(\mappingMatrix\right)=\prod_{i=1}^{d}N\left(\mappingVector_{i,:}|\mathbf{0},\eye\right)$$
        }{1}
$$
 p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{d}N\left(\dataVector_{:,j}|\mathbf{0},\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye\right)$$
 $$
 p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{d}N\left(\dataVector_{:,j}|\mathbf{0},\kernelMatrix\right)$$
$$
\kernelMatrix=\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye$$
This is a product of Gaussian processes with linear kernels.
$$
\kernelMatrix=?
$$
Replace linear kernel with non-linear kernel for non-linear model.}}{45%}{45%}



\newslide{Non-Linear Latent Variable Model}

**EQ Kernel**
  
* The RBF kernel has the form $\kernelScalar_{i,j}=\kernelScalar\left(\latentVector_{i,:},\latentVector_{j,:}\right),$
where
$$
\kernelScalar\left(\latentVector_{i,:},\latentVector_{j,:}\right)=\alpha\exp\left(-\frac{\left(\latentVector_{i,:}-\latentVector_{j,:}\right)^{\top}\left(\latentVector_{i,:}-\latentVector_{j,:}\right)}{2\rbfWidth^{2}}\right).
$$


* No longer possible to optimise wrt $\latentMatrix$ via an eigenvalue problem.

* Instead find gradients with respect to $\latentMatrix,\alpha,\rbfWidth$
 and $\dataStd^{2}$ and optimise using gradient methods.


\subsection{Oil Data}

\subsection{Stick Man Data}

\subsection{Applications}
  
* Style based inverse kinematics [@Grochow:styleik04].
* Prior distributions for tracking [@Urtasun:3dpeople06,Urtasun:priors05].
* Assisted drawing [@Baxter:doodle06].


\newslide{Summary}
  
* GPLVM based on a dual probabilistic interpretation of PCA.
* Straightforward to non-linearise it using Gaussian processes.
* Result is a non-linear probabilistic PCA.
* *Optimise latent variables* rather than integrate them out.

\endif
