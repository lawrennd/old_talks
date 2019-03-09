%{
\begin{matlab}
  %}
  % Comment/MATLAB set up code
  importTool('dimred')
  dimredToolboxes
  randn('seed', 1e6)
  rand('seed', 1e6)
  if ~isoctave
    colordef white
  end
  colorFigs = false;
  % Text width in cm.
  textWidth = 13
%{
\end{matlab}
\begin{frame}[fragile]
  \frametitle{Mixtures of Gaussians}

  \begin{figure}
    \begin{matlab}
    %}
    close all
    for j = 1:2
      model = dimredPlotMog(20, 200);
    
      if model.d>2
        model = mogProject(model, 2);
      end
    
      modelType = model.type;
      modelType(1) = upper(modelType(1));


      fileName = ['demArtificial' modelType num2str(j)];
    
      clf
      ax = axes('position', [0.05 0.05 0.9 0.9]);
      hold on
      mogTwoDPlot(model, []);
    

      piVals = linspace(-pi, pi, 200)';
      for i=1:model.m
        a = line(model.mean(i, 1), model.mean(i, 2), 'marker', 'o');
        set(a, 'linewidth', 2, 'markersize', 10)
        x = [sin(piVals) cos(piVals)];
        el = x*model.U{i};
        line(model.mean(i, 1) + el(:, 1), model.mean(i, 2) + el(:, 2), ...
           'linewidth', 2);
      end
      xLim = [min(model.Y(:, 1)) max(model.Y(:, 1))]*1.1;
      yLim = [min(model.Y(:, 2)) max(model.Y(:, 2))]*1.1;
      set(ax, 'xLim', xLim);
      set(ax, 'yLim', yLim);
      set(ax, 'xtick', [-2 -1 0 1 2]);
      set(ax, 'ytick', [-2 -1 0 1 2]);
      printLatexPlot([fileName '_slides'], '../../../dimred/tex/diagrams/', 0.4*textWidth)
    
      figure
      clf
      ax = axes('position', [0.05 0.05 0.9 0.9]);
      hold on
      mogTwoDPlot(model, []);
    
      set(ax, 'xLim', xLim);
      set(ax, 'yLim', yLim);
      set(ax, 'xtick', [-2 -1 0 1 2]);
      set(ax, 'ytick', [-2 -1 0 1 2]);
      printLatexPlot([fileName 'NoOvals_slides'], '../../../dimred/tex/diagrams/', 0.4*textWidth)
    end  
    %{
    \end{matlab}
    \begin{center}
      \only<1>{\inputdiagram{../../../dimred/tex/diagrams/demArtificialMog1NoOvals_slides}\hfill{}\inputdiagram{../../../dimred/tex/diagrams/demArtificialMog2NoOvals_slides}}    \only<2>{\inputdiagram{../../../dimred/tex/diagrams/demArtificialMog1_slides}\hfill{}\inputdiagram{../../../dimred/tex/diagrams/demArtificialMog2_slides}}
    \end{center}
    \caption{\only<1>{Two dimensional data sets.}  \only<2>{Complex
        structure not a problem for mixtures of Gaussians.}}
    
  \end{figure}

  % \begin{figure}
  %   \begin{centering}
  %     \includegraphics<1>[width=0.45\textwidth]{../../../dimred/tex/diagrams/demArtificialInterspeechMog1NoOvals}\only<1>{\hfill}\includegraphics<1>[width=0.45\textwidth]{../../../dimred/tex/diagrams/demArtificialInterspeechMog2NoOvals}
  %     \includegraphics<2>[width=0.45\textwidth]{../../../dimred/tex/diagrams/demArtificialInterspeechMog1}\only<2>{\hfill}\includegraphics<2>[width=0.45\textwidth]{../../../dimred/tex/diagrams/demArtificialInterspeechMog2}
  %   \end{centering}

  %   \caption{\only<1>{Two dimensional data sets.}  \only<2>{Complex
  %       structure not a problem for mixtures of Gaussians.}}
  % \end{figure}

\end{frame}

\subsection{High Dimensional Data}

\begin{frame}
  \frametitle{Thinking in High Dimensions}

  \begin{itemize}
  \item Two dimensional plots of Gaussians can be misleading.
  \item Our low dimensional intuitions can fail dramatically.
  \item Two major issues:

    \begin{enumerate}
    \item In high dimensions all the data moves to a `shell'. There is nothing
      near the mean!
    \item Distances between points become constant.
    \item These affects apply to many densities.
    \end{enumerate}
  \item Let's consider a Gaussian ``egg''.
  \end{itemize}
  
\end{frame}

\begin{frame}
  \frametitle{The Gaussian Egg}

  \begin{itemize}
  \item See also Exercise 1.4 in \citep{Bishop:book95}
  \end{itemize}
  % 
  \begin{figure}
    \begin{centering}
      \includegraphics<1>[width=0.4\textwidth]{../../../dimred/tex/diagrams/oneDgaussian_nobrown}
      \includegraphics<2>[width=0.4\textwidth]{../../../dimred/tex/diagrams/twoDgaussian_nobrown2}
      \includegraphics<3>[width=0.4\textwidth]{../../../dimred/tex/diagrams/threeDgaussian_nobrown.png}\\
      \vspace{0.5cm}
      \textbf{Volumes: }
      \only<1>{\colorbox{lightpurple}{
          \textcolor{yellow}{65.8\%}, \color{ironsulf}4.8\%
          \textcolor{white}{29.4\%}}}
      \only<2>{\colorbox{lightpurple}{\textcolor{yellow}{59.4\%},
          \color{ironsulf}7.4\% \textcolor{white}{33.2\%}}}
      \only<3>{\colorbox{lightpurple}{
          \textcolor{yellow}{56.1\%}, \color{ironsulf}9.2\%,
          \textcolor{white}{34.7\%}}}
    \end{centering}
    
    \caption{\only<1>{One dimensional Gaussian
        density.}\only<2>{Two dimensional Gaussian
        density.}\only<3>{Three dimensional Gaussian
        density.}}
  \end{figure}
\end{frame}



\begin{frame}
  \frametitle{Mathematics}

  \textbf{What is the density of probability mass?}
  \begin{columns}[c]
    \column{4cm}
    \only<1-3>{
      \[
      y_{i,k}\sim\gaussianSamp 0{\dataStd^{2}}
      \]
    }
    \only<1>{
      \[
      \Longrightarrow\dataScalar_{i,k}^{2}\sim\dataStd^{2}\chi_{1}^{2}
      \]
    }\only<2>{
      \[
      \Longrightarrow\dataScalar_{i,k}^{2}\sim\gammaSamp{\frac{1}{2}}{\frac{1}{2\dataStd^{2}}}
      \]
    }\only<3>{
      \[
      \Longrightarrow{\color{red}\dataScalar_{i,1}^{2}+\dataScalar_{i,2}^{2}}\sim\gammaSamp{\frac{2}{2}}{\frac{1}{2\dataStd^{2}}}
      \]
    }\only<4>{
      \[
      \sum_{k=1}^{\dataDim}y_{i,k}^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{1}{2\dataStd^{2}}}
      \]
      \[
      \Longrightarrow\left\langle \sum_{k=1}^{\dataDim}y_{i,k}^{2}\right\rangle =\dataDim\dataStd^{2}
      \]
    }\only<5>{
      \[
      \frac{1}{\dataDim}\sum_{k=1}^{\dataDim}y_{i,k}^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{\dataDim}{2\dataStd^{2}}}
      \]
      \[
      \Longrightarrow\left\langle \frac{1}{\dataDim}\sum_{k=1}^{\dataDim}y_{i,k}^{2}\right\rangle =\dataStd^{2}
      \]
    }


    \column{4cm}
    \includegraphics<1-2>[width=3cm]{../../../dimred/tex/diagrams/distance1}
    \includegraphics<3>[width=3cm]{../../../dimred/tex/diagrams/distance2}
    \includegraphics<4-5>[width=3cm]{../../../dimred/tex/diagrams/distance}
  \end{columns}

  \begin{center}
    \only<1>{Square of sample from Gaussian is scaled chi-squared
      density}
    \only<2>{Chi squared density is a variant of the gamma
      density with shape parameter $a=\frac{1}{2}$, rate parameter
      $b=\frac{1}{2\dataStd^{2}}$, $\gammaDist
      xab=\frac{b^{a}}{\Gamma\left(a\right)}x^{a-1}e^{-bx}$.}
    \only<3-4>{Addition
      of gamma random variables with the same rate is gamma with sum
      of shape parameters ($y_{i,k}$s are
      independent)}
    \only<5>{Scaling of gamma density scales the rate
      parameter}
  \end{center}

\end{frame}

\begin{frame}[fragile]
  \frametitle{Where is the Mass?}
  \begin{itemize}
  \item Squared distances are gamma distributed.
  \end{itemize}
  % 
\begin{figure}
  \begin{matlab}
    %}
    close all
    x = 0:1:10;
    D = 2.^x;
    lim1 = .95;
    lim2 = 1.05;
    lim3 = 100;

    % Compute values of cumulative gammas.
    y = cumGamma(lim1*lim1, D/2, D/2);
    y2 = cumGamma(lim2*lim2, D/2, D/2);
    y3 = cumGamma(lim3*lim3, D/2, D/2);

    % Compute patch outlines
    xp1 = [x(1) x x(end) x(1)];
    p1 = [0 y 0 0];
    xp2 = [x(1) x x(end:-1:1)];
    p2 = [y(1) y2 y(end:-1:1)];
    xp3 = [x(1) x x(end:-1:1)];
    p3 = [y2(1) y3 y2(end:-1:1)];

    % Draw patches
    patch(xp1, p1, [1 1 0]);
    patch(xp2, p2, [0 0.7 .5]);
    patch(xp3, p3, [1 1 1]);

    % Set exponentiated labels
    xtick = get(gca, 'xtick');
    for i = 1:length(xtick)
      xtickLabel{i} =  num2str(2^xtick(i));
    end
    set(gca, 'xticklabel', xtickLabel);

    set(gca, 'ytick', [0 0.25 0.5 0.75 1]);
    a = xlabel('dimension');

    set(a, 'fontsize', 12);
    set(gca, 'fontsize', 23)

    printLatexPlot('dimensionMass', '../../../dimred/tex/diagrams/', 0.5*textWidth)

    %{
  \end{matlab}
  \begin{center}
    \inputdiagram{../../../dimred/tex/diagrams/dimensionMass}
  \end{center}

  \caption{Plot of probability mass versus dimension. Plot shows the
    volume of density inside 0.95 of a standard deviation (yellow),
    between 0.95 and 1.05 standard deviations (green), over 1.05
    and standard deviations (white).}

\end{figure}



\end{frame}

\begin{frame}[fragile]
  \frametitle{Looking at Gaussian Samples}

  \begin{figure}
    \begin{matlab}
    %}
    close all
    a = randn(2);
    a = a*a';
    Y = gsamp([0, 0], a, 300);
    a = plot(Y(:, 1), Y(:, 2), 'rx');
    %set(a, 'markersize', 10);
    %set(gca, 'fontsize', 20)
    zeroAxes(gca);
    printLatexPlot('twoDGaussianSamples_slides', '../../../dimred/tex/diagrams/', 0.5*textWidth)
    %{
    \end{matlab}
    \begin{center}
      \inputdiagram{../../../dimred/tex/diagrams/twoDGaussianSamples_slides}
    \end{center}
  \end{figure}
\end{frame}


\begin{frame}
  \frametitle{Interpoint Distances}

  \begin{itemize}
  \item The other effect in high dimensions is all points become
    equidistant.
  \item Can show this for Gaussians with a similar proof to the
    above,
    \[ 
    \dataScalar_{i,k}\sim\gaussianSamp
    0{\sigma_{k}^{2}}\quad \quad \dataScalar_{j,k}\sim\gaussianSamp
    0{\sigma_{k}^{2}}
    \]
    \[
    y_{i,k}-y_{j,k}\sim\gaussianSamp 0{2\sigma_{k}^{2}}
    \]
    \[
    \left(y_{i,k}-y_{j,k}\right)^{2}\sim\gammaSamp{\frac{1}{2}}{\frac{1}{4\sigma_{k}^{2}}}
    \]
    For spherical Gaussian, $\sigma_{k}^{2}=\sigma^{2}$ 
    \[
    \sum_{k=1}^{\dataDim}\left(y_{i,k}-y_{j,k}\right)^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{1}{4\dataStd^{2}}}
    \]
    \[
    \frac{1}{\dataDim}\sum_{k=1}^{\dataDim}\left(y_{i,k}-y_{j,k}\right)^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{\dataDim}{4\dataStd^{2}}}
    \]
    Dimension normalized distance between points is drawn from a gamma.
    Mean is $2\sigma^{2}$. Variance is $\frac{8\dataStd^{2}}{\dataDim}$.
  \end{itemize}

\end{frame}

\begin{frame}
  \frametitle{Central Limit Theorem and Non-Gaussian Case}
  \begin{itemize}
  \item <1->We can compute the density of squared distance \emph{analytically}
    for spherical, independent Gaussian data.
  \item <2->More generally, for \emph{independent} data, the \emph{central
      limit theorem} applies.
    
    \begin{itemize}
    \item <3->The mean squared distance in high dimensional space is the mean
      of the variances.
    \item <4->The variance about the mean scales as $\dataDim^{-1}$.
    \end{itemize}
  \end{itemize}

\end{frame}

\begin{frame}
  \frametitle{Summary}
  \begin{itemize}
  \item In high dimensions if individual dimensions are \emph{independent}
    the distributions behave counter intuitively.
  \item All data sits at one standard deviation from the mean.
  \item The densities of squared distances can be analytically
    calculated for the Gaussian case.
  \item For non-Gaussian \emph{independent} systems we can invoke the central
    limit theorem.
  \item Next we will consider example data sets and see how their interpoint
    distances are distributed.
  \end{itemize}

\end{frame}

\subsection{Example Data Sets}

\begin{frame}[fragile]
  \frametitle{Sanity Check}

  \textbf{Data sampled from independent Gaussian distribution}
  \begin{itemize}
  \item If dimensions are independent, we expect low variance, Gaussian behavior
    for the distribution of squared distances.
  \end{itemize}
  \textbf{Distance distribution for a Gaussian with $\dataDim=1000$,
    $\numData=1000$}

  \begin{figure}
    \begin{matlab}
    %}
    close all
    Y = randn(1000, 1000);
    dimredPlotSquaredDistances(Y, 'gaussianDistances1000_slides', [], 0.4*textWidth);
    %{
    \end{matlab}
    \begin{center}
      \inputdiagram{../../../dimred/tex/diagrams/gaussianDistances1000_slides}
    \end{center}

    
    \caption{A good match betwen theory and the samples for a 1000 dimensional
      Gaussian distribution.}
    
  \end{figure}

\end{frame}



\begin{frame}[fragile]
  \frametitle{Sanity Check}

  \textbf{Same data generation, but fewer data points.}
  \begin{itemize}
  \item If dimensions are independent, we expect low variance, Gaussian behaviour
    for the distribution of squared distances.
  \end{itemize}
  \textbf{Distance distribution for a Gaussian with $\dataDim=1000$}, \emph{$\numData=100$}

  % 
  \begin{figure}
    \begin{matlab}
    %}
    close all
    Y = randn(100, 1000);
    dimredPlotSquaredDistances(Y, 'gaussianDistances100_slides', [], 0.4*textWidth);
    %{
    \end{matlab}
    \begin{center}
      \inputdiagram{../../../dimred/tex/diagrams/gaussianDistances100_slides}
    \end{center}

    \caption{A good match betwen theory and the samples for a 1000 dimensional
      Gaussian distribution.}

  \end{figure}

\end{frame}

\subsection{Oil Data}

\begin{frame}
  \frametitle{Oil Data}
  \begin{columns}
    \column{0.4\textwidth}
    \begin{itemize}
    \item Simulated measurements from an oil pipeline {\footnotesize \citep{Bishop:oil93}}.
    \item Pipleline contains oil, water and gas.
    \item Three phases of flow in pipeline---homogeneous, stratified and annular.
    \item <2->Gamma densitometry sensors arranged in a configuration around
      pipeline.
    \end{itemize}

    \column{0.3\textwidth}

    \begin{center}
      % 
      \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
        % 
        \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Homogeneous
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Stratified
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Annular
          \end{center}%
        \end{minipage}%
      \end{minipage}
      \end{center}
  \column{0.2\textwidth}
  \begin{center}
    \includegraphics<1>[height=0.8\textheight]{../../../dimred/tex/diagrams/oilData}
    \includegraphics<2>[height=0.8\textheight]{../../../dimred/tex/diagrams/oilDataSensors}
  \end{center}
  \end{columns}
\end{frame}

\begin{frame}[fragile]
  \frametitle{Oil Data}
  \begin{itemize}
  \item 12 simulated measurements of oil flow in a pipe.
  \item Nature of flow is dependent on relative proportion of oil, water and
    gas.
  \end{itemize}
  % 
  \begin{figure}
    \begin{matlab}
    %}
    close all
    Y = lvmLoadData('oil');
    v = dimredPlotSquaredDistances(Y, 'oilDistances_slides', [], 0.4*textWidth);
    %{
    \end{matlab}

  \begin{center}
    \inputdiagram{../../../dimred/tex/diagrams/oilDistances_slides}
  \end{center}
  \input{../../../dimred/tex/diagrams/oilDistances_slidesCaption}
  \caption{Interpoint squared distance distribution for oil data
    with \captionInfo.}
  \end{figure}

\end{frame}

\subsection{Stick Man Data}

\begin{frame}
  \frametitle{Stick Man Data}
  \begin{columns}
    \column{0.55\textwidth}
    \begin{itemize}
    \item $\numData=55$ frames of motion capture.
    \item $xyz$ locations of 34 points on the body.
    \item $\dataDim=102$ dimensional data.
    \item ``Run 1'' available from \url{http://accad.osu.edu/research/mocap/mocap_data.htm}.
    \end{itemize}

    \column{0.45\textwidth}

    \begin{center}
      % 
      \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Changing
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Angle
            \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            of Run
            \end{center}%
        \end{minipage}%
      \end{minipage}\movie[loop]{%
        \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../fgplvm/tex/diagrams/demStick3Angle1}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../fgplvm/tex/diagrams/demStick3Angle2}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../fgplvm/tex/diagrams/demStick3Angle3}
            \end{center}%
          \end{minipage}%
        \end{minipage}}{/home/neil/aaron/urtasun_cvpr06_tracking.avi}
    \end{center}
    
  \end{columns}

\end{frame}

\begin{frame}[fragile]
  \frametitle{Stick Man}
  \begin{itemize}
  \item Motion capture data inter point distance histogram.
  \end{itemize}
  % 
  \begin{figure}
    \begin{matlab}
    %}
    close all
    Y = lvmLoadData('stick');
    v = dimredPlotSquaredDistances(Y, 'stickDistances_slides', [], 0.4*textWidth);
    %{
    \end{matlab}

    \begin{center}
      \inputdiagram{../../../dimred/tex/diagrams/stickDistances_slides}
    \end{center}
    \input{../../../dimred/tex/diagrams/stickDistances_slidesCaption}
  
    \caption{Interpoint squared distance distribution for stick man data
    with \captionInfo.}\label{fig:stickManDistances}

  \end{figure}

\end{frame}

\subsection{Yeast Cell Cycle Data}

\begin{frame}
  \frametitle{Microarray Data}
  \begin{columns}
    \column{0.55\textwidth}
    \begin{itemize}
    \item Gene expression measurements reflecting the cell cycle in yeast {\footnotesize \citep{Spellman:yeastcellcy98}}. 
    \item $\dataDim=6,178$ Genes measured for $\numData=77$ experiments
    \item Data available from \url{http://genome-www.stanford.edu/cellcycle/data/rawdata/individual.htm}.
    \end{itemize}

    \column{0.45\textwidth}

    \begin{center}
      % 
      \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Yeast
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Cell
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Cycle
          \end{center}
        \end{minipage}
      \end{minipage}\includegraphics[height=0.8\textheight]{../../../dimred/tex/diagrams/spellman}
    \end{center}
    
  \end{columns}
  
\end{frame}

\begin{frame}[fragile]
  \frametitle{Microarray Data}
  \begin{itemize}
  \item Spellman yeast cell cycle.
  \end{itemize}
  \begin{figure}
    \begin{matlab}
    %}
    close all
    Y = lvmLoadData('spellman');
    v = dimredPlotSquaredDistances(Y, 'spellmanDistances_slides', [], 0.4*textWidth);
    %{
    \end{matlab}

    \begin{center}
      \inputdiagram{../../../dimred/tex/diagrams/spellmanDistances_slides}
    \end{center}
    \input{../../../dimred/tex/diagrams/spellmanDistances_slidesCaption}
    
    \caption{Interpoint squared distance distribution for Spellman
      microarray data with \captionInfo.}
    
  \end{figure}


\end{frame}

\subsection{Grid Corpus Vowels}

\begin{frame}
  \frametitle{Grid Corpus Vowels}
  \begin{columns}
    \column{0.55\textwidth}
    \begin{itemize}
    \item Grid corpus data modeled for synthesis by Jon Barker.
    \item 33 context dependent vowel phones from 34 (mixed male/female) subjects.
    \item Means and variances of synthesis HMM for subjects {\scriptsize \citep{Shichiri:eigenvoices02}}.
    \end{itemize}
    \column{0.45\textwidth}

    \begin{center}
      % 
      \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            34 Subjects'
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Vowel
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Phones 
          \end{center}
        \end{minipage}
      \end{minipage}\movie[loop]{%
        \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../dimred/tex/diagrams/gridCorpusNl}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../dimred/tex/diagrams/gridCorpusMc}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../dimred/tex/diagrams/gridCorpusJb}
            \end{center}%
          \end{minipage}%
        \end{minipage}}{/home/neil/aaron/urtasun_cvpr06_tracking.avi}
    \end{center}
    
  \end{columns}
  
\end{frame}

\begin{frame}[fragile]
  \frametitle{Grid Corpus Vowels}
  \begin{itemize}
    \item Grid Corpus: \url{http://www.dcs.shef.ac.uk/spandh/gridcorpus/}.
    \item For each context dependent phone: 5 state HMM, one Gaussian component
      per state. 25 MFCC channels, with deltas and accelerations. 
%$5 \times
 %     25 \times 3=375$ means per phone and 375 variances. 750 features
%      per phone, $750\times 33=24,750$ features per individual.
  \end{itemize}
  \begin{center}
    % 
  \begin{figure}
    \begin{matlab}
    %}
    close all
    Y = lvmLoadData('grid_vowels');
    
    [v, tv] = dimredPlotSquaredDistances(Y, 'grid_vowelsDistances_slides', [], 0.4*textWidth);
    %{
    \end{matlab}
  \begin{center}
    \inputdiagram{../../../dimred/tex/diagrams/grid_vowelsDistances_slides}
  \end{center}
  \input{../../../dimred/tex/diagrams/grid_vowelsDistances_slidesCaption}
  \caption{Interpoint squared distance distribution for Grid corpus vowel data with \captionInfo.}
  
\end{figure}

  \end{center}


\end{frame}


\begin{frame}
  \frametitle{Where does practice depart from our theory?}
  \begin{itemize}
  \item The situation for real data does not reflect what we expect.
  \item Real data exhibits greater variances on interpoint distances.

    \begin{itemize}
    \item Somehow the real data seems to have a smaller effective dimension.
    \end{itemize}
  \item Let's look at another $\dataDim=1000$.
  \end{itemize}

\end{frame}

\begin{frame}[fragile]
  \frametitle{1000-D Gaussian}

  \textbf{Distance distribution for a different Gaussian with $\dataDim=1000$}

  % 
  \begin{figure}
    \begin{matlab}
    %}
    close all;
    W = randn(1000, 2);
    covMat = W*W' +1e-2*eye(1000);
    Y = gsamp(zeros(1, 1000), covMat, 1000);
    dimredPlotSquaredDistances(Y, 'correlatedGaussianDistances1000_slides', [], 0.45*textWidth);

    % normalise data to be variance 1 for each dimension.
    varY = var(Y);
    stdY = sqrt(varY);
    Y = Y./repmat(stdY, size(Y, 1), 1);

    d = triu(dist2(Y, Y));
    v = d(find(d>eps));

    % Normalise distances to be 1.
    v = 2*v/mean(v);

    figure
    [vals, x] = hist(v, 50);
    vals = vals/(sum(vals)*mean(x(2:end) - x(1:end-1) ));

    bar(x, vals);
    hold on
    a = xlabel('squared distance');
    x = linspace(0, 6, 100);
    ha = plot(x, gammaPdf(x, size(W, 2)/2, size(W, 2)/4), 'k-');
    set(ha, 'linewidth', 3);
    set(gca, 'xlim', [0, 6]);
    printLatexPlot('correlatedGaussianDistances2_slides', '../../../dimred/tex/diagrams/', 0.45*textWidth)
    %{
    \end{matlab}

    \begin{center}
      \only<1-2>{\inputdiagram{../../../dimred/tex/diagrams/correlatedGaussianDistances1000_slides}}
      \only<3>{\inputdiagram{../../../dimred/tex/diagrams/correlatedGaussianDistances2_slides}}
    \end{center}
%    \caption{Interpoint squared distance distribution for Gaussian with $\dataDim=1000$.}

  \end{figure}


  \begin{enumerate}
  \item<2->Gaussian has a specific low rank covariance matrix $\covarianceMatrix=\mappingMatrix\mappingMatrix^{\top}+\dataStd^{2}\eye$.
    
  \item<2->Take $\dataStd^{2}=1e-2$ and sample $\mappingMatrix\in\Re^{1000\times2}$
     from $\gaussianSamp{0}{1}$.
  \only<3>{\item<3-> Theoretical curve taken assuming dimensionality of 2.}
  \end{enumerate}


\end{frame}

%}

%%% Local Variables: 
%%% mode: latex
%%% TeX-master: "../mlss2012/session1"
%%% End: 
