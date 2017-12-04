### Deep Models {data-transition="None"}

  \begin{center}
    \begin{tikzpicture}[node distance=\layersep]
      \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
      \foreach \name / \x in {1,...,8}
        % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y-\name) at (\x*\nodesep, 0) {$\dataScalar_\x$};


        % Draw the hidden layer nodes
      \foreach \name / \x in {1,...,6}
        \path[xshift=\nodesep]
          node[latent] (X1-\name) at (\x*\nodesep, \layersep) {$\latentScalar^{1}_\x$};

        % Draw the hidden layer nodes
      \foreach \name / \x in {1,...,6}
        \path[xshift=\nodesep]
          node[latent] (X2-\name) at (\x*\nodesep, \layersep*2) {$\latentScalar^{2}_\x$};

        % Draw the hidden layer nodes
      \foreach \name / \x in {1,...,4}
        \path[xshift=\nodesep*2]
          node[latent] (X3-\name) at (\x*\nodesep, \layersep*3) {$\latentScalar^{3}_\x$};

        % Draw the hidden layer nodes
      \foreach \name / \x in {1,...,4}
        \path[xshift=\nodesep*2]
          node[latent] (X4-\name) at (\x*\nodesep, \layersep*4) {$\latentScalar^{4}_\x$};

      % Connect every node in the latent layer with every node in the
      % data layer.
      \foreach \source in {1,...,6}
        \foreach \dest in {1,...,8}
          \draw[->] (X1-\source) -- (Y-\dest);

      \foreach \source in {1,...,6}
        \foreach \dest in {1,...,6}
          \draw[->] (X2-\source) -- (X1-\dest);

      \foreach \source in {1,...,4}
        \foreach \dest in {1,...,6}
          \draw[->] (X3-\source) -- (X2-\dest);

      \foreach \source in {1,...,4}
        \foreach \dest in {1,...,4}
          \draw[->] (X4-\source) -- (X3-\dest);



      % Annotate the layers
      \node[annot,right of=X4-4, node distance=2cm, text width=3cm] (ls) {Latent layer 4};
      \node[annot,right of=X3-4, node distance=2cm, text width=3cm] (ls) {Latent layer 3};
      \node[annot,right of=X2-6, node distance=2cm, text width=3cm] (ls) {Latent layer 2};
      \node[annot,right of=X1-6, node distance=2cm, text width=3cm] (ls) {Latent layer 1};
      \node[annot,right of=Y-8, node distance=2cm, text width=3cm] (ds) {Data space};
    \end{tikzpicture}
  \end{center}
  
### Deep Models {data-transition="None"}
  \def\layersep{1.5cm}
  \def\nodesep{1cm}
  \begin{center}
    \begin{tikzpicture}[node distance=\layersep]
      \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
      \node[obs] (Y) at (0cm, 0) {$\dataVector$};

      % Draw the hidden layer nodes
      \node[latent] (X1) at (0cm, \layersep) {$\latentVector_1$};

      % Draw the hidden layer nodes
      \node[latent] (X2) at (0cm, \layersep*2) {$\latentVector_2$};

      % Draw the hidden layer nodes
      \node[latent] (X3) at (0cm, \layersep*3) {$\latentVector_3$};
      
      % Draw the hidden layer nodes
      \node[latent] (X4) at (0cm, \layersep*4) {$\latentVector_4$};

      % Connect every node in the latent layer with every node in the
      % data layer.
      \draw[->] (X1) -- (Y);
      \draw[->] (X2) -- (X1);
      \draw[->] (X3) -- (X2);
      \draw[->] (X4) -- (X3);



      % Annotate the layers
      \only<1>{\node[annot,right of=X4, node distance=2cm, text width=3cm] (ls) {Latent layer 4};
      \node[annot,right of=X3, node distance=2cm, text width=3cm] (ls) {Latent layer 3};
      \node[annot,right of=X2, node distance=2cm, text width=3cm] (ls) {Latent layer 2};
      \node[annot,right of=X1, node distance=2cm, text width=3cm] (ls) {Latent layer 1};
      \node[annot,right of=Y, node distance=2cm, text width=3cm] (ds) {Data space};}
      \only<2>{\node[annot,right of=X4, node distance=2cm, text width=3cm] (ls) {Abstract features};
      \node[annot,right of=X3, node distance=2cm, text width=3cm] (ls) {More combination};
      \node[annot,right of=X2, node distance=2cm, text width=3cm] (ls) {Combination of low level features};
      \node[annot,right of=X1, node distance=2cm, text width=3cm] (ls) {Low level features};
      \node[annot,right of=Y, node distance=2cm, text width=3cm] (ds) {Data space};}
    \end{tikzpicture}
  \end{center}
  

### Deep Gaussian Processes

-   Deep architectures allow abstraction of features
    [@Bengio:deep09; @Hinton:fast06; @Salakhutdinov:quantitative08]

-   We use variational approach to stack GP models.


