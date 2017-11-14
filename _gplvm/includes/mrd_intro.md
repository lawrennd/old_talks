<!--frame failure start-->

  \frametitle{Manifold Relevance Determination}
  \begin{flushright}
    \andreasPicture{1.5cm}\\{\scriptsize \cite{Damianou:manifold12}}
  \end{flushright}
  
    \def\layersep{2cm}
    \begin{center}
      \begin{tikzpicture}[node distance=\layersep]
\tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
    \foreach \name / \x in {1,...,8}
    % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y-\name) at (\x, 0) {$\dataScalar_\x$};


    % Draw the hidden layer nodes
    \foreach \name / \x in {1,...,6}
        \path[xshift=1cm]
            node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};

    % Connect every node in the latent layer with every node in the
    % data layer.
    \foreach \source in {1,...,6}
        \foreach \dest in {1,...,8}
            \draw[->] (X-\source) -- (Y-\dest);



    %  Annotate the layers
    \node[annot,left of=X-1, node distance=1cm] (ls) {Latent space};
    \node[annot,left of=Y-1, node distance=1cm] (ds) {Data space};
  \end{tikzpicture}
\end{center}
  


<!--frame failure end-->
<!--frame failure start-->

\frametitle{Shared GP-LVM}
    \def\layersep{2cm}
    \begin{center}
      \begin{tikzpicture}[node distance=\layersep]
\tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
    \foreach \name / \x in {1,...,4}
    % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y-\name) at (\x, 0) {$\dataScalar^{(1)}_\x$};

    \foreach \name / \x in {1,...,4}
    % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Z-\name) at (\x+5, 0) {$\dataScalar^{(2)}_\x$};

    % Draw the hidden layer nodes
    \foreach \name / \x in {1,...,6}
        \path[xshift=2cm]
            node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};

    % Connect every node in the latent layer with every node in the
    % data layer.
    \foreach \source in {1,...,6}
        \foreach \dest in {1,...,4}
            \draw[->] (X-\source) -- (Y-\dest);

    \foreach \source in {1,...,6}
        \foreach \dest in {1,...,4}
            \draw[->] (X-\source) -- (Z-\dest);


    %  Annotate the layers
    \node[annot,left of=X-1, node distance=1cm] (ls) {Latent space};
    \node[annot,left of=Y-1, node distance=1cm] (ds) {Data space};
  \end{tikzpicture}
  Separate ARD parameters for mappings to $\dataMatrix^{(1)}$ and $\dataMatrix^{(2)}$.
\end{center}
  


<!--frame failure end-->

