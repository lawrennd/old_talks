<!--frame failure start-->
\frametitle{Modeling Multiple `Views'} \small
  \begin{itemize}
  \item Single space to model correlations between two different data sources, e.g., images \& text, image \& pose.
  \item Shared latent spaces: {\scriptsize \citep{Shon:learning05,Navaratnam:joint07,Ek:pose07}}
    \begin{center}
      \begin{tikzpicture}
        
        % Define nodes
        \draw node[obs] (Y1) {$\dataMatrix^{(1)}$};
        \draw node[latent, above right=of Y1] (X) {$\latentMatrix$};
        \draw node[obs, below right=of X] (Y2) {$\dataMatrix^{(2)}$};
        
        % Connect the nodes
        \draw [->] (X) to (Y1);%
        \draw [->] (X) to (Y2);%
        
      \end{tikzpicture}
    \end{center}
  \item Effective when the `views' are correlated.
  \item But not all information is shared between both `views'.
  \item PCA applied to concatenated data vs CCA applied to data.
  \end{itemize}

<!--frame failure end-->
<!--frame failure start-->
\frametitle{Shared-Private Factorization}\small
  \centering
  \begin{itemize}
  \item In real scenarios, the `views' are neither fully independent, nor fully correlated.
  \item Shared models 
    \begin{itemize}
    \item either allow information relevant to a single view to be mixed in the shared signal,
    \item or are unable to model such private information.
    \end{itemize}
  \item Solution: Model shared and private information {\scriptsize \citep{Klami:group11,Ek:ambiguity08,Leen:gplvmcca06,Klami:local07,Klami:probabilistic08,Tucker:battery58}}
    \begin{center}
      \begin{tikzpicture}
        % Define nodes
        \draw node[latent] (XS1) {$\mathbf{Z}^{(1)}$};
        \draw node[obs, below right=of XS1] (Y1) {$\dataMatrix^{(1)}$};
        \draw node[latent, above right=of Y1] (X) {$\latentMatrix$};
        \draw node[obs, below right=of X] (Y2) {$\dataMatrix^{(2)}$};
        \draw node[latent, above right=of Y2] (XS2) {$\mathbf{Z}^{(2)}$};
        
        % Connect the nodes
        \draw [->] (XS1) to (Y1);%
        \draw [->] (XS2) to (Y2);%
        \draw [->] (X) to (Y1);%
        \draw [->] (X) to (Y2);%
        
      \end{tikzpicture}
    \end{center}
    \item Probabilistic CCA is case when dimensionality of $\mathbf{Z}$ matches $\dataMatrix^{(i)}$ (cf Inter Battery Factor Analysis {\scriptsize \citep{Tucker:battery58}}).
  \end{itemize}

<!--frame failure end-->

