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
* Integrate out *parameters*.}{\includegraphics<1-4>[width=0.5\textwidth]{../../../gplvm/tex/diagrams/gplvmGraph}
      {\scriptsize \only<1-4>{$$
 p\left(\dataMatrix|\latentMatrix,\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\mappingMatrix\latentVector_{i,:}}{\dataStd^{2}\eye}$$
        }\only<3-4>{$$
 p\left(\mappingMatrix\right)=\prod_{i=1}^{\dataDim}\gaussianDist{\mappingVector_{i,:}}{\zerosVector}{\eye}$$
        }\only<4->{$$
 p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{\dataDim}\gaussianDist{\dataVector_{:,j}}{\zerosVector}{\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye}$$
        }}
}{45%}{45%}


\newslide{Linear Latent Variable Model IV}

\fragmentdiv{**Dual**}{1}\fragmentdiv{**Dual**}{2} Probabilistic PCA Max. Likelihood Soln \fragmentdiv{[@Lawrence:gplvm03,Lawrence:pnpca05]}{1}\fragmentdiv{[@Lawrence:gplvm03,Lawrence:pnpca05]}{2}\fragmentdiv{[@Tipping:probpca99]}{3}

     \includegraphics<1>[width=0.25\textwidth]{../../../gplvm/tex/diagrams/gplvmGraph}
  
  \fragmentdiv{
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
       }{2}\fracmentdiv{$$
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
where $\rotationMatrix$ is an arbitrary rotation matrix.}{3}
     




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

\subsection{Gaussian Processes}



\newslide{Gaussian Process (GP)}

**Prior for Functions**
  
* Probability Distribution over Functions
* Functions are infinite dimensional.

    
  * Prior distribution over *instantiations* of the function: finite
      dimensional objects.
  * Can prove by induction that GP is 'consistent'.
  
* Mean and Covariance Functions
* Instead of mean and covariance matrix, GP is defined by mean function
    and covariance function.

    
  * Mean function often taken to be zero or constant.
  * Covariance function must be *positive definite*.
  * Class of valid covariance functions is the same as the class
      of *Mercer kernels*.
  




\newslide{Gaussian Processes II}

**Zero mean Gaussian Process**
  
* A (zero mean) Gaussian process likelihood is of the form$$
    p\left(\dataVector|\latentMatrix\right)=N\left(\dataVector|\mathbf{0},\kernelMatrix\right),$$
    where $\kernelMatrix$ is the covariance function or \emph{kernel}.
* The \emph{linear kernel} with noise has the form$$
    \kernelMatrix=\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye$$

* Priors over non-linear functions are also possible.

    
  * To see what functions look like, we can sample from the prior process.
  




\newslide{Covariance Samples}

  \texttt{demCovFuncSample}%
  \begin{figure}
    \includegraphics<2>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample1}
    \includegraphics<3>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample2}
    \includegraphics<4>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample3}
    \includegraphics<1>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample4}
    \includegraphics<5>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample5}
    \includegraphics<6>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample6}
    \includegraphics<7>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample7}
    \includegraphics<8>[width=0.5\textwidth]{../../../gp/tex/diagrams/demCovFuncSample8}

    \caption{\only<2>{RBF kernel with $\rbfWidth=0.3$, $\alpha=1$ }\only<3>{ RBF
        kernel with $\rbfWidth=1$, $\alpha=1$ }\only<4>{ RBF kernel with $\rbfWidth=0.3$,
        $\alpha=4$}\only<1>{linear kernel, $\kernelMatrix=\latentMatrix\latentMatrix^{\top}$}
      \only<5>{ MLP kernel with $\alpha=8$, $w=100$ and $b=100$}\only<6>{
        MLP kernel with $\alpha=8$, $b=0$ and $w=100$}\only<7>{bias kernel
        with $\alpha=1$ and }\only<8>{summed combination of: RBF kernel,
        $\alpha=1$, $\rbfWidth=0.3$; bias kernel, $\alpha=$1; and white noise kernel,
        $\beta=100$}\label{cap:kernelSamples}}

  \end{figure}





\newslide{Gaussian Process Regression}

**Posterior Distribution over Functions**
  
* Gaussian processes are often used for regression.
* We are given a known inputs $\latentMatrix$ and targets $\dataMatrix$.
* We assume a prior distribution over functions by selecting a kernel.
* Combine the prior with data to get a \emph{posterior} distribution
    over functions.




\newslide{Gaussian Process Regression}

  \texttt{demRegression}%
  \begin{figure}
    \includegraphics<1>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression1}
    \includegraphics<2>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression2}
    \includegraphics<3>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression3}
    \includegraphics<4>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression4}
    \includegraphics<5>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression5}
    \includegraphics<6>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression6}
    \includegraphics<7>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression7}
    \includegraphics<8>[width=0.5\textwidth]{../../../gp/tex/diagrams/demRegression8}

    \caption{Examples include WiFi localization, C14 callibration curve.}

  \end{figure}





\newslide{Learning Kernel Parameters}


  \framesubtitle{Can we determine length scales and noise levels from the data?}

  \texttt{demOptimiseGp}

  \includegraphics<1>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp1}
  \includegraphics<2>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp3}
  \includegraphics<3>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp5}
  \includegraphics<4>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp7}
  \includegraphics<5>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp9}
  \includegraphics<6>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp11}
  \includegraphics<7>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp13}
  \includegraphics<8>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp15}
  \includegraphics<9>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp17}\hfill
  \includegraphics<1>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp2}
  \includegraphics<2>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp4}
  \includegraphics<3>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp6}
  \includegraphics<4>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp8}
  \includegraphics<5>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp10}
  \includegraphics<6>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp12}
  \includegraphics<7>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp14}
  \includegraphics<8>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp16}
  \includegraphics<9>[width=0.45\textwidth]{../../../gp/tex/diagrams/demOptimiseGp18}




\newslide{Non-Linear Latent Variable Model}
  \begin{columns}[c]


    \column{5cm}

  **Dual Probabilistic PCA**

    \only<1>{
      
    * Define \emph{linear-Gaussian relationship} between latent variables
        and data.
    * **Novel** Latent variable approach:

        
      * Define Gaussian prior over \emph{parameteters}, $\mappingMatrix$.
      * Integrate out \emph{parameters}.
      
    
    }\only<2->{
      
    * <2->Inspection of the marginal likelihood shows ...

        
      * <3->The covariance matrix is a covariance function.
      * <4->We recognise it as the `linear kernel'.
      
    
    }


    \column{5cm}

      \includegraphics<1->[width=0.5\textwidth]{../../../gplvm/tex/diagrams/gplvmGraph}

    \vspace{-1cm}


\fragmentdiv{$$
 p\left(\dataMatrix|\latentMatrix,\mappingMatrix\right)=\prod_{i=1}^{n}N\left(\dataVector_{i,:}|\mappingMatrix\latentVector_{i,:},\dataStd^{2}\eye\right)$$
 $$
 p\left(\mappingMatrix\right)=\prod_{i=1}^{d}N\left(\mappingVector_{i,:}|\mathbf{0},\eye\right)$$
        }{1}\only<1-2>{$$
 p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{d}N\left(\dataVector_{:,j}|\mathbf{0},\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye\right)$$
        }\only<3->{$$
 p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{d}N\left(\dataVector_{:,j}|\mathbf{0},\kernelMatrix\right)$$
        }\only<3-4>{$$
 \kernelMatrix=\latentMatrix\latentMatrix^{\top}+\dataStd^{2}\eye$$
        }\only<4>{This is a product of Gaussian processes with linear kernels.}\only<5>{$$
 \kernelMatrix=?$$
 Replace linear kernel with non-linear kernel for non-linear model.}



\newslide{Non-Linear Latent Variable Model}

**RBF Kernel**
  
* The RBF kernel has the form $\kernelScalar_{i,j}=\kernelScalar\left(\latentVector_{i,:},\latentVector_{j,:}\right),$
where
$$
\kernelScalar\left(\latentVector_{i,:},\latentVector_{j,:}\right)=\alpha\exp\left(-\frac{\left(\latentVector_{i,:}-\latentVector_{j,:}\right)^{\top}\left(\latentVector_{i,:}-\latentVector_{j,:}\right)}{2\rbfWidth^{2}}\right).
$$


* No longer possible to optimise wrt $\latentMatrix$ via an eigenvalue problem.

* Instead find gradients with respect to $\latentMatrix,\alpha,\rbfWidth$
 and $\dataStd^{2}$ and optimise using gradient methods.









\subsection{Oil Data}

\newslide{Oil Data Set}

\figure{\includegraphics[width=0.8\textwidth]{../../../fgplvm/tex/diagrams/demOilFull}{}{}





\newslide{Oil Data Set II}

**Nearest Neighbour error in $\latentMatrix$**
  
* Nearest neighbour classification in latent space.

\begin{tabular}{|c|c|c|c|c|}
    \hline 
    Method & PCA & LLE & GTM & GP-LVM\tabularnewline
    \hline
    Errors & 162 & 18 & 11 (best) & 1 \tabularnewline
    \hline
\end{tabular}

*cf* 2 errors in data space.





\subsection{Stick Man Data}

`demStick1`

  % 
  \begin{figure}
      \only<1>{\vspace{4cm}
      }\only<2>{\includegraphics[width=0.5\textwidth]{../../../fgplvm/tex/diagrams/demStick1Connected}}

    \caption{The latent space for the stick man motion capture data. \vspace{-1cm}
    }
    
\end{figure}



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
