\ifndef{sharedIntro}
\define{sharedIntro}

\editme

\section{Modeling Multiple 'Views'}

* Single space to model correlations between two different data sources, e.g., images \& text, image \& pose.
* Shared latent spaces: @Shon:learning05;@Navaratnam:joint07;@Ek:pose07
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
* Effective when the `views' are correlated.
* But not all information is shared between both `views'.
* PCA applied to concatenated data vs CCA applied to data.

\section{Shared-Private Factorization}

* In real scenarios, the `views' are neither fully independent, nor fully correlated.
* Shared models 
    * either allow information relevant to a single view to be mixed in the shared signal,
    * or are unable to model such private information.
* Solution: Model shared and private information  @Klami:group11,@Ek:ambiguity08,@Leen:gplvmcca06,@Klami:local07,@Klami:probabilistic08,@Tucker:battery58

\plotcode{    \begin{center}
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
    \end{center}}
* Probabilistic CCA is case when dimensionality of $\mathbf{Z}$ matches $\dataMatrix^{(i)}$ (cf Inter Battery Factor Analysis @Tucker:battery58).

\endif
