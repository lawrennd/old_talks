\ifndef{bayesGplvmIntro}
\define{bayesGplvmIntro}
\editme

\newslide{Selecting Data Dimensionality}

* GP-LVM Provides probabilistic non-linear dimensionality reduction.
* How to select the dimensionality?
* Need to estimate marginal likelihood.
* In standard GP-LVM it increases with increasing $\latentDim$.

\newslide{Integrate Mapping Function and Latent Variables}

\columns{**Bayesian GP-LVM**

* Start with a standard GP-LVM.
* Apply standard latent variable approach:
    * Define Gaussian prior over \emph{latent space}, $\latentMatrix$.
    * Integrate out \emph{latent variables}.
    * Unfortunately integration is intractable. 
}{      \only<1->{\begin{tikzpicture}
          
          % Define nodes
          \node[obs]                               (Y) {$\dataMatrix$};
          \node[latent, above=of Y] (X) {$\latentMatrix$};
          \node[const, right=1cm of Y]            (sigma) {$\dataStd^2$};
          
          % Connect the nodes
          \edge {X,sigma} {Y} ; %
          
          % Plates
          % \plate {YX} {(Y)} {$i=1\dots\numData$} ;
          % \plate {} {(W)(Y)(YX.north west)(YX.south west)} {$j=1\dots\dataDim$} ;
          
        \end{tikzpicture}
      }
	\aligncenter{
      {\scriptsize \only<1->{\[
          p\left(\dataMatrix|\latentMatrix\right)=\prod_{j=1}^{\dataDim}\gaussianDist{\dataVector_{:,j}}{\zerosVector}{\kernelMatrix}
          \]
        }\only<3->{\[
          p\left(\latentMatrix\right)=\prod_{j=1}^{\latentDim}\gaussianDist{\latentVector_{:,j}}{\zerosVector}{\alpha_i^{-2}\eye}
          \]
        }\only<4->{\[ 
          p\left(\dataMatrix|\boldsymbol{\alpha}\right)= ??
          \]
        }
      }}
}{40%}{60%}
\endif
