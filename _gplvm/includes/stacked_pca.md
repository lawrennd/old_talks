``` {#mycode .octave .numberLines startFrom="0"}

%}
  importLatest('GPmat')
  gpmatToolboxes;
  randn('seed', 1e6);
  rand('seed', 1e6);
  textWidth = 13;
  dirName = '../../../health/tex/diagrams/';
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

\begin{frame}[fragile]\frametitle{Stacked PCA}

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
      kern{j} = kernCreate(X{j}, 'lin');
      kern{j}.variance = 0.2;
      K{j} = kernCompute(kern{j}, X{j});
      X{j+1} = gsamp(zeros(numTime, 1), K{j}, latentDims)';
    end
    figure
    subplot(length(latentDims), 1, 1)
    for j = 1:length(latentDims)
      a= subplot(length(latentDims), 1, j)
      pos = get(a, 'position');
      pos(3) = pos(3)/2;
      set(a, 'position', pos);
      if j == 1
        set(gca, 'xlim', 1.25*[-limVal limVal])
        set(gca, 'ylim', 1.25*[-limVal limVal])
      else 
        set(gca, 'xlim', 1.25*[-1 1]);
        set(gca, 'ylim', 1.25*[-1 1]);
      end
      plot(X{j}(:, 1), X{j}(:, 2), 'color', blueColor, 'linewidth', 2);
      axis off
    end
    fileName = ['stackPcaSample' num2str(i)];
    printLatexPlot(fileName, dirName, 0.6*textWidth);
    includeText = [includeText '\only<' num2str(1+2*(i-1)) '>{\inputdiagram{' dirName fileName '}}' char(13)];
    figure
    for j = 1:2
      a = subplot(2, 1, j);
      pos = get(a, 'position');
      pos(3) = pos(3)/2;
      set(a, 'position', pos);
      if j == 1
        set(gca, 'xlim', 1.25*[-limVal limVal])
        set(gca, 'ylim', 1.25*[-limVal limVal])
      else 
        set(gca, 'xlim', 1.25*[-1 1]);
        set(gca, 'ylim', 1.25*[-1 1]);
      end
      if j == 1
        plot(X{1}(:, 1), X{1}(:, 2), 'color', blueColor, 'linewidth', 2);
      else
        plot(X{end}(:, 1), X{end}(:, 2), 'color', blueColor, 'linewidth', 2);
      end
      axis off
    end
    fileName = ['stackPcaSampleSquash' num2str(i)];
    printLatexPlot(fileName, dirName, 0.6*textWidth);
    includeText = [includeText '\only<' num2str(2*i) '>{\inputdiagram{' dirName fileName '}}' char(13)];
  end
  printLatexText(includeText, 'stackPcaInclude.tex', dirName);
%{
\end{octave}
\begin{columns}[c]
  \column{5cm}
  \vspace{0.75cm}
  \PandocStartInclude{../../../health/tex/diagrams/stackPcaInclude.tex}\only<1>{\inputdiagram{../../../health/tex/diagrams/stackPcaSample1}}
\only<2>{\inputdiagram{../../../health/tex/diagrams/stackPcaSampleSquash1}}
\only<3>{\inputdiagram{../../../health/tex/diagrams/stackPcaSample2}}
\only<4>{\inputdiagram{../../../health/tex/diagrams/stackPcaSampleSquash2}}
\only<5>{\inputdiagram{../../../health/tex/diagrams/stackPcaSample3}}
\only<6>{\inputdiagram{../../../health/tex/diagrams/stackPcaSampleSquash3}}
\only<7>{\inputdiagram{../../../health/tex/diagrams/stackPcaSample4}}
\only<8>{\inputdiagram{../../../health/tex/diagrams/stackPcaSampleSquash4}}
\only<9>{\inputdiagram{../../../health/tex/diagrams/stackPcaSample5}}
\only<10>{\inputdiagram{../../../health/tex/diagrams/stackPcaSampleSquash5}}
\PandocEndInclude{input}{99}{59}
  \column{5cm}
  \def\layersep{1cm}
  \def\nodesep{1cm}

  \only<1,3,5,7,9>{\begin{tikzpicture}[node distance=\layersep]
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
    \end{tikzpicture}}
  \only<2,4,6,8,10>{\begin{tikzpicture}[node distance=\layersep]
      \tikzstyle{annot} = [text width=4em, text centered]    % Draw the input layer nodes
      \node[obs] (Y) at (0cm, 0) {$\dataVector$};

      
      % Draw the hidden layer nodes
      \node[latent] (X4) at (0cm, \layersep*4) {$\latentVector_4$};

      % Connect every node in the latent layer with every node in the
      % data layer.
      \draw

