<!--frame failure start-->

\frametitle{Deep Health}
  \def\layersep{1.2cm}
  \def\nodesep{0.8cm}
  \begin{center}
    \vspace{-1cm}
    \pgfdeclarelayer{background}
    \pgfdeclarelayer{foreground}
    \pgfsetlayers{background,main,foreground}
    \begin{tikzpicture}[node distance=\layersep]
      \tikzstyle{annot} = [text width=4em, text centered, scale=0.9]    % Draw the input layer nodes
      % \foreach \name / \x in {1,...,8}
      %   % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
      %   \node[obs] (Y-\name) at (\x*\nodesep, \layersep) {$\dataScalar_\x$};

      

      \begin{pgfonlayer}{foreground}
      \node[obs] (Xray) at (5*\nodesep, \layersep*2) {$\mathbf{I}_1$};
      \node[obs] (Biopsy) at (3*\nodesep, \layersep*2) {$\mathbf{I}_2$};
        % Draw the hidden layer nodes
      % \foreach \name / \x in {1,...,8}
      %   \path[xshift=\nodesep]
      %     node[latent] (Y-\name) at (\x*\nodesep, \layersep*2) {$\latentScalar^{1}_\x$};

        % Draw the hidden layer nodes
      \foreach \name / \x in {1,...,5}
        \path[xshift=-0.5*\nodesep]
          node[latent] (X1-\name) at (\nodesep+\x*\nodesep, \layersep*3) {$\latentScalar^{1}_\x$};
      \node[obs] (Clinical-1) at (7*\nodesep, \layersep*3) {$\dataScalar_2$};
      \node[obs] (Clinical-2) at (8*\nodesep, \layersep*3) {$\dataScalar_3$};

      \node[obs] (Notes-1) at (0.25*\nodesep, \layersep*3) {$\dataScalar_5$};
      \node[obs] (Social-1) at (-1.5*\nodesep, \layersep*3) {$\dataScalar_4$};
      % Draw the hidden layer nodes
      \foreach \name / \x in {1,...,4}
        \path[xshift=\nodesep]
          node[latent] (X2-\name) at (\x*\nodesep, \layersep*4) {$\latentScalar^{2}_\x$};
      \node[obs] (Survival) at (8*\nodesep, \layersep*4) {$\dataScalar_1$};
      \node[obs] (Expression) at (0*\nodesep, \layersep*4) {$\dataScalar_6$};
        % Draw the hidden layer nodes
      \foreach \name / \x in {1,...,4}
        \path[xshift=\nodesep]
          node[latent] (X3-\name) at (\x*\nodesep, \layersep*5) {$\latentScalar^{3}_\x$};

      \node[obs] (Genotype) at (0, \layersep*6) {$\mathbf{G}$} 
      node[obs] (Environment) at (3*\nodesep, \layersep*6) {$\mathbf{E}$} 
      node[obs] (Epigenotype) at (6*\nodesep, \layersep*6) {$\mathbf{EG}$};

      % Annotate the layers
      \node[annot,right of=X3-4, node distance=3cm, text width=6cm] (ls) {latent representation of disease stratification};
      \node[annot,right of=Survival, node distance=1.5cm, text width=2cm] (ls) {survival analysis};
      \node[annot,left of=Expression, node distance=1.5cm, text width=1.5cm] (ls) {gene expression};
      \node[annot,right of=Clinical-2, node distance=1.5cm, text width=2.45cm] (ls) {clinical measurements and treatment};
      \node[annot,below of=Notes-1, node distance=1.5cm, text width=1.5cm] (ls) {clinical notes};
      \node[annot,below of=Social-1, node distance=1.5cm, text width=1.5cm] (ls) {social network, music data};
      \node[annot,below of=Xray, node distance=0.75cm, text width=3cm] (ls) {X-ray};
      \node[annot,below of=Biopsy, node distance=0.75cm, text width=3cm] (ls) {biopsy};
      \node[annot,above of=Environment, node distance=0.75cm] (ls) {environment};
      \node[annot,above of=Epigenotype, node distance=0.75cm] (ls) {epigenotype};
      \node[annot,above of=Genotype, node distance=0.75cm] (ls) {genotype};
      % \node[annot,left of=X3-1, node distance=1cm] (ls) {Latent layer 3};
      % \node[annot,left of=X2-1, node distance=1cm] (ls) {Latent layer 2};
      % \node[annot,left of=X1-1, node distance=1cm] (ls) {Latent layer 1};
      % \node[annot,left of=Y-1, node distance=1cm] (ds) {Data space};

      \end{pgfonlayer}
      \begin{pgfonlayer}{background}

      % Connect every node in the latent layer with every node in the
      % data layer.
        \foreach \dest in {1,...,4}
          \draw[->] (Genotype) -- (X3-\dest);
        \foreach \dest in {1,...,4}
          \draw[->] (Environment) -- (X3-\dest);
        \foreach \dest in {1,...,4}
          \draw[->] (Epigenotype) -- (X3-\dest);
      \foreach \source in {1,...,5}
          \draw[->] (X1-\source) -- (Xray);

      \foreach \source in {1,...,5}
          \draw[->] (X1-\source) -- (Biopsy);

      \foreach \source in {1,...,4}
        \foreach \dest in {1,...,5}
          \draw[->] (X2-\source) -- (X1-\dest);

      \foreach \source in {1,...,4}
        \foreach \dest in {1,...,2}
         \draw[->] (X2-\source) -- (Clinical-\dest);

      \foreach \source in {1,...,4}
         \draw[->] (X2-\source) -- (Notes-1);

      \foreach \source in {1,...,4}
         \draw[->] (X2-\source) -- (Social-1);


      \foreach \source in {1,...,4}
        \foreach \dest in {1,...,4}
          \draw[->] (X3-\source) -- (X2-\dest);

      \foreach \source in {1,...,4}
         \draw[->] (X3-\source) -- (Survival);
      \foreach \source in {1,...,4}
         \draw[->] (X3-\source) -- (Expression);

      \end{pgfonlayer}

    \end{tikzpicture}
  \end{center}


<!--frame failure end-->

