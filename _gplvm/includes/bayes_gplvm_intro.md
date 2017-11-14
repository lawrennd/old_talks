<!--frame start-->
\[label=bayesGplvm\]

### Selecting Data Dimensionality

-   GP-LVM Provides probabilistic non-linear dimensionality reduction.

-   How to select the dimensionality?

-   Need to estimate marginal likelihood.

-   In standard GP-LVM it increases with increasing $\latentDim$.

<!--frame end-->
<!--frame failure start-->

  \frametitle{Integrate Mapping Function and Latent Variables}
  \begin{columns}[c]
    \column{5cm}
    \textbf{Bayesian GP-LVM}
    \begin{itemize}
    \item <1->Start with a standard GP-LVM.
    \item <2->Apply standard latent variable approach:
      
      \begin{itemize}
      \item <2->Define Gaussian prior over \emph{latent space}, $\latentMatrix$.
      \item <3->Integrate out \emph{latent variables}.
      \item <4->Unfortunately integration is intractable. 
      \end{itemize}
    \end{itemize}
    \column{5cm}
    
    \begin{center}
      % \includegraphics<1-4>[width=0.5\textwidth]{../../../gplvm/tex/diagrams/ppcaGraph}
      \only<1->{\begin{tikzpicture}
          
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
    \end{center}
    
    
    
    \begin{center}
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
      }
    \end{center}
  \end{columns}

<!--frame failure end-->

