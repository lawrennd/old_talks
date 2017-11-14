``` {#mycode .octave .numberLines startFrom="0"}

%}
  importLatest('GPmat')
  gpmatToolboxes;
  randn('seed', 1e6);
  rand('seed', 1e6);
  textWidth = 13;
  dirName = '../../../gplvm/tex/diagrams/';
  blueColor = [0, 0, 1];
  redColor = [1, 0, 0];
  magentaColor = [1, 0, 1];
  blackColor = [0, 0, 0];
  negative = false;
  if blackBackground
    negative = true;
    blueColor =  1-blueColor;
    redColor = 1-redColor;
    magentaColor = 1-magentaColor;
    blackColor = 1- blackColor;
  end
%{
```

\begin{frame}[fragile]\frametitle{Stacked GPs}
\begin{octave}
%}
  latentDims = [2, 2, 2, 2, 2]
  sideLength = 25;
  numTime = sideLength*4;
  limVal = 0.5;
  numSamps = 5;
  t = [limVal*ones(sideLength, 1) linspace(-limVal, limVal, sideLength)'];
  t = [t; [linspace(limVal, -limVal, sideLength)' limVal*ones(sideLength, 1)]];
  t = [t; [-limVal*ones(sideLength, 1) linspace(limVal, -limVal, sideLength)']];
  t = [t; [linspace(-limVal, limVal, sideLength)' -limVal*ones(sideLength, 1)]];
  includeText = [];
  for i = 1:numSamps;
    X{1} = t; %[repmat(x, numTime, 1) t];
    kern = {};
    K = {};
    for j = 1:length(latentDims)
      kern{j} = kernCreate(X{j}, 'rbf');
      kern{j}.variance = 0.5;
      K{j} = kernCompute(kern{j}, X{j});
      X{j+1} = gsamp(zeros(numTime, 1), K{j}, latentDims)';
    end
    figure
    subplot(length(latentDims), 1, 1)
    for j = 1:length(latentDims)
      subplot(length(latentDims), 1, j)
      if j == 1
        set(gca, 'xlim', 1.25*[-limVal limVal])
        set(gca, 'ylim', 1.25*[-limVal limVal])
      end
      plot(X{j}(:, 1), X{j}(:, 2), 'color', blueColor, 'linewidth', 2);
      axis image
      axis off
    end
    fileName = ['stackGpSample' num2str(i)];
    printLatexPlot(fileName, dirName, 0.6*textWidth);
    includeText = [includeText '\only<' num2str(i) '>{\inputdiagram{' dirName fileName '}}' char(13)];
  end
  printLatexText(includeText, 'stackGpInclude.tex', dirName);
%{
\end{octave}

\begin{columns}[c]
\column{5cm}
\vspace{0.75cm}
\PandocStartInclude{../../../gplvm/tex/diagrams/stackGpInclude.tex}\only<1>{\inputdiagram{../../../gplvm/tex/diagrams/stackGpSample1}}
\only<2>{\inputdiagram{../../../gplvm/tex/diagrams/stackGpSample2}}
\only<3>{\inputdiagram{../../../gplvm/tex/diagrams/stackGpSample3}}
\only<4>{\inputdiagram{../../../gplvm/tex/diagrams/stackGpSample4}}
\only<5>{\inputdiagram{../../../gplvm/tex/diagrams/stackGpSample5}}
\PandocEndInclude{input}{71}{55}
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
      \node

