<!--frame start-->
### Graphical Representations of GP-LVM

\def\layersep{2cm}

\only<1>{\begin{tikzpicture}[node distance=\layersep]
        \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
        \node[obs] (Y-1) at (1, 0) {$\dataMatrix$};


        % Draw the hidden layer nodes
        \node[latent] (X-1) at (1 cm, \layersep) {$\latentMatrix$};
        
        % Connect every node in the latent layer with every node in the
        % data layer.
        \draw[->] (X-1) -- (Y-1);

        % Annotate the layers
        \node[annot,right of=X-1, node distance=1cm] (ls) {latent space};
        \node[annot,right of=Y-1, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<3>{\begin{tikzpicture}[node distance=\layersep]
        \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
        \node[obs] (Y-1) at (1, 0) {$\dataScalar_1$};
        \foreach \name / \x in {2,...,8}
        % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
            \node (void-\x) at (\x, 0) {};
        
        
        % Draw the hidden layer nodes
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};
        
        % Connect every node in the latent layer with every node in the
        % data layer.
        \foreach \source in {1,...,6}
            \draw[->] (X-\source) -- (Y-1);
        
        
        
        % Annotate the layers
        \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
        \node[annot,right of=void-8, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<2>{\begin{tikzpicture}[node distance=\layersep]
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
        
        
        
        % Annotate the layers
        \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
        \node[annot,right of=Y-8, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<4>{\begin{tikzpicture}[node distance=\layersep]
        \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
        % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y) at (4.5, 0) {$\dataScalar$};
        
        
        % Draw the hidden layer nodes
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};
        
        \node[latent, right=of Y] (w)  {$\mappingVector$};
        \node[const, left=of Y] (sigma)  {$\dataStd^2$};
        % Connect every node in the latent layer with every node in the
        % data layer.
        \foreach \source in {1,...,6}
            \draw[->] (X-\source) -- (Y);
        
        \draw[->] (w) -- (Y);
        \draw[->] (sigma) -- (Y);
        
        
        % Annotate the layers
        \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
        \node[annot,right of=Y-8, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<5>{\begin{tikzpicture}[node distance=\layersep]
        \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
        % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y) at (4.5, 0) {$\dataScalar$};
        
        
        % Draw the hidden layer nodes
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};

        
        \node[latent, right=of Y] (w)  {$\mappingVector$};
        \node[const, right=of w] (alpha) {$\alpha$};
        \node[const, left=of Y] (sigma)  {$\dataStd^2$};
        % Connect every node in the latent layer with every node in the
        % data layer.
        \foreach \source in {1,...,6}
            \draw[->] (X-\source) -- (Y);

        \draw[->] (alpha) -- (w);
        
        \draw[->] (w) -- (Y);
        \draw[->] (sigma) -- (Y);
        
        
        % Annotate the layers
        \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
        \node[annot,right of=Y-8, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<6>{\begin{tikzpicture}[node distance=\layersep]
        \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
        % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y) at (4.5, 0) {$\dataScalar$};
        
        
        % Draw the hidden layer nodes
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};

        % Draw the variance on x
        \path[xshift=1cm]
        node[const] (alpha) at (3.5 cm, \layersep*2) {$\alpha$};
        
        \node[latent, right=of Y] (w)  {$\mappingVector$};
        \node[const, left=of Y] (sigma)  {$\dataStd^2$};
        % Connect every node in the latent layer with every node in the
        % data layer.
        \foreach \source in {1,...,6}
            \draw[->] (X-\source) -- (Y);

        \foreach \dest in {1,...,6}
            \draw[->] (alpha) -- (X-\dest);
        
        \draw[->] (w) -- (Y);
        \draw[->] (sigma) -- (Y);
        
        
        % Annotate the layers
        \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
        \node[annot,right of=Y-8, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<7>{\begin{tikzpicture}[node distance=\layersep]
        \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
        % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y) at (4.5, 0) {$\dataScalar$};
        
        
        % Draw the hidden layer nodes
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[latent] (X-\name) at (\x cm, \layersep) {$\latentScalar_\x$};

        % Draw the variance on x
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[const] (alpha-\name) at (\x cm, \layersep*2) {$\alpha_\x$};
        
        \node[latent, right=of Y] (w)  {$\mappingVector$};
        \node[const, left=of Y] (sigma)  {$\dataStd^2$};
        % Connect every node in the latent layer with every node in the
        % data layer.
        \foreach \source in {1,...,6}
            \draw[->] (X-\source) -- (Y);

        \foreach \source in {1,...,6}
            \draw[->] (alpha-\source) -- (X-\source);
        
        \draw[->] (w) -- (Y);
        \draw[->] (sigma) -- (Y);
        
        
        % Annotate the layers
        \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
        \node[annot,right of=Y-8, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<8>{\begin{tikzpicture}[node distance=\layersep]
        \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
        % This is the same as writing \foreach \name / \x in {1/1,2/2,3/3,4/4}
        \node[obs] (Y) at (4.5, 0) {$\dataScalar$};
        
        
        % Draw the hidden layer nodes
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[latent] (W-\name) at (\x cm, \layersep) {$\mappingScalar_\x$};

        % Draw the variance on x
        \foreach \name / \x in {1,...,6}
            \path[xshift=1cm]
            node[const] (alpha-\name) at (\x cm, \layersep*2) {$\alpha_\x$};
        
        \node[latent, right=of Y] (x)  {$\latentVector$};
        \node[const, left=of Y] (sigma)  {$\dataStd^2$};
        % Connect every node in the latent layer with every node in the
        % data layer.
        \foreach \source in {1,...,6}
            \draw[->] (X-\source) -- (Y);

        \foreach \source in {1,...,6}
            \draw[->] (alpha-\source) -- (W-\source);
        
        \draw[->] (x) -- (Y);
        \draw[->] (sigma) -- (Y);
        
        
        % Annotate the layers
        \node[annot,right of=X-6, node distance=1cm] (ls) {latent space};
        \node[annot,right of=Y-8, node distance=1cm] (ds) {data space};
      \end{tikzpicture}}
\only<5>{\[\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha \eye} \quad \latentVector \sim \gaussianSamp{0}{\eye}\]}
\only<6>{\[\mappingVector \sim \gaussianSamp{\zerosVector}{\eye} \quad \latentVector \sim \gaussianSamp{0}{\alpha\eye}\]}
\only<7>{\[\mappingVector \sim \gaussianSamp{\zerosVector}{\eye} \quad \latentScalar_i \sim \gaussianSamp{0}{\alpha_i}\]}
\only<8>{ \[\mappingScalar_i \sim \gaussianSamp{0}{\alpha_i} \quad \latentVector \sim \gaussianSamp{\zerosVector}{\eye}\]}
\only<5->{$\dataScalar \sim \gaussianSamp{\latentVector^\top \mappingVector}{\dataStd^2}$}

<!--frame end-->

