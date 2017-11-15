
### Structures for Extracting Information from Data

\begin{columns}[c]
\column{5cm}
\vspace{0.75cm}
  \inputdiagram{../../../gplvm/tex/diagrams/stackGpSample2}
\column{5cm}
\def\layersep{1cm}
\def\nodesep{1cm}

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
      \node[annot,right of=X4, node distance=2cm, text width=3cm] (ls) {Latent layer 4};
      \node[annot,right of=X3, node distance=2cm, text width=3cm] (ls) {Latent layer 3};
      \node[annot,right of=X2, node distance=2cm, text width=3cm] (ls) {Latent layer 2};
      \node[annot,right of=X1, node distance=2cm, text width=3cm] (ls) {Latent layer 1};
      \node[annot,right of=Y, node distance=2cm, text width=3cm] (ds) {Data space};
    \end{tikzpicture}

\end{columns}


### 

@Damianou:deepgp13\hfill\raggedleft{\andreasPicture{1.5cm}}\

[\includegraphics[page=1,trim=0cm 16cm 0cm 0.5cm, width=0.4\textwidth, clip=true, width=1.0\textwidth]{../../../gp/tex/diagrams/damianou13a.pdf}](http://jmlr.org/proceedings/papers/v31/damianou13a.pdf)


