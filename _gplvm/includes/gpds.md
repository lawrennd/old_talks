<!--frame failure start-->

  \frametitle{Gaussian Process Dynamical Systems}
  \begin{flushright}
    {\scriptsize \citep{Damianou:vgpds11}}
  \end{flushright}
  \def\layersep{2cm}
  \begin{tikzpicture}[node distance=\layersep]
    \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
    % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
    \foreach \name / \x in {1,...,8}
    % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
       \node[obs] (Y-\name) at (\x, 0) {$\dataScalar_\x$};
    
    
    % Draw the hidden layer nodes
    \foreach \name / \x in {1,...,6}
        \path[xshift=1cm]
        node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};

    % Draw the variance on x
    \path[xshift=1cm]
    node[const] (t) at (3.5 cm, \layersep*2) {$t$};
        
    % Connect every node in the latent layer with every node in the
    % data layer.
    \foreach \source in {1,...,6}
        \foreach \dest in {1,...,8}
            \draw[->] (X-\source) -- (Y-\dest);

    \foreach \dest in {1,...,6}
        \draw[->] (t) -- (X-\dest);
        
        
        
    % Annotate the layers
    \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
    \node[annot,right of=t, node distance=1cm] (time) {time};
    \node[annot,right of=Y-8, node distance=1cm] (ds) {data space};
  \end{tikzpicture}

<!--frame failure end-->
<!--frame start-->
### Gaussian Process over Latent Space

-   Assume a GP prior for $p(\latentMatrix)$.

-   Input to the process is time, $p(\latentMatrix|t)$.

<!--frame end-->
<!--frame start-->
### Interpolation of HD Video

\includeyoutube{i9TEoYxaBxQ}

<!--frame end-->

