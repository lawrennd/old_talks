``` {#mycode .octave .numberLines startFrom="0"}

%}
  importTool('ndlutil');
  textWidth = 11;
  lineWidth = 4;
  markerLineWidth = 6;
  markerSize = 5;
  plotWidth = 5/13*textWidth;
  plotWidthTwo = 3.5/13*textWidth;
  directory = '../../ml/diagrams/';
  randn('seed', 1e5);
  rand('seed', 1e5);
  blueColor = [0, 0, 1];
  redColor = [1, 0, 0];
  magentaColor = [1, 0, 1];
  blackColor = [0, 0, 0];
  if blackBackground
    blueColor =  1-blueColor;
    redColor = 1-redColor;
    magentaColor = 1-magentaColor;
    blackColor = 1- blackColor;
  end
%{
```

<!--frame start-->
\[fragile\]

### Sampling Two Dimensional Variables

``` {#mycode .octave .numberLines startFrom="0"}

        muh = 1.7;
    varh = 0.0225;
    muw = 75;
    varw = 36;
    tau = 2*pi;
    h = linspace(1.25, 2.15, 100)';
    w = linspace(55, 95, 100)';
    ph = 1/sqrt(tau*varh)*exp(-1/(2*varh)*(h - muh).^2);
    pw = 1/sqrt(tau*varw)*exp(-1/(2*varw)*(w - muw).^2);
    cheightFig = figure(2); clf
    a = plot(h, ph, '-', 'color', redColor);
    set(gca, 'xtick', [1.25 1.7 2.15]);
    set(gca, 'ytick', [1 2 3]);
    set(a, 'linewidth', lineWidth);
    xlabel('$h/m$')
    ylabel('$p(h)$')
    axis off
    cweightFig = figure(3); clf
    a = plot(w, pw, '-', 'color', blueColor);
    set(a, 'linewidth', lineWidth);
    set(gca, 'xtick', [55 75 95]);
    set(gca, 'ytick', [0.02 0.04 0.06]);
    xlabel('$w/kg$')
    ylabel('$p(w)$')
    axis off

    covMat = [1 0.98; 0.98 1];
    covMat = [sqrt(varh) 0; 0 sqrt(varw)]*covMat*[sqrt(varh) 0; 0 sqrt(varw)];
    [R, void] = eig(covMat);
    numSamps = 7;
    twoDfig = figure(1); clf
    axes;
    a = plot(muh, muw, 'x', 'color', magentaColor);
    set(a, 'markersize', markerSize/2, 'linewidth', markerLineWidth);
    theta = linspace(0, tau, 100);
    xel = sin(theta)*sqrt(varh);    yel = cos(theta)*sqrt(varw);    vals = R*[xel; yel];
    hold on
    a = plot(vals(1, :)+muh, vals(2, :)+muw, '-', 'color', magentaColor);
    set(a, 'linewidth', 3);
    set(gca, 'xlim', [min(h) max(h)], 'ylim', [min(w) max(w)], 'xtick', [55 75 95], 'ytick', [1.25 1.7 2.15])
    xlabel('$h/m$')
    ylabel('$w/kg$')

    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off

    printLatexPlot('cheightWeightTwoD', directory, plotWidth)
    
    figure(cheightFig)
    set(gca, 'xticklabel', [])
    set(gca, 'yticklabel', [])
    xlabel('')

    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off

    printLatexPlot('cheightGaussianSmall', directory, plotWidthTwo)
    
    figure(cweightFig)
    set(gca, 'xticklabel', [])
    set(gca, 'yticklabel', [])
    xlabel('')

    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off

    printLatexPlot('cweightGaussianSmall', directory, plotWidthTwo)
    for i = 1:numSamps
      vecS = R*[sqrt(varh) 0; 0 sqrt(varw)]*randn(2, 1);

      hval = vecS(1) + muh;
      wval = vecS(2) + muw;

      figure(cheightFig)
      a = line(hval, 0.1, 'marker', 'x', 'linewidth', markerLineWidth, 'color', redColor);
      fileName = ['cheightGaussianSmall' num2str(i)];
      printLatexPlot(fileName, directory, plotWidthTwo)
      set(a, 'color', blackColor)
      fileName = ['cheightGaussianSmall' num2str(i) 'a'];
      printLatexPlot(fileName, directory, plotWidthTwo)

      figure(cweightFig)
      a = line(wval, 0.002, 'marker', 'x', 'linewidth', markerLineWidth, 'color', redColor);
      fileName = ['cweightGaussianSmall' num2str(i)];
      printLatexPlot(fileName, directory, plotWidthTwo)
      set(a, 'color', blackColor)
      fileName = ['cweightGaussianSmall' num2str(i) 'a'];
      printLatexPlot(fileName, directory, plotWidthTwo)
      figure(twoDfig)
      a = line(hval, wval, 'marker', 'x', 'linewidth', markerLineWidth, 'color', redColor);
      fileName = ['cheightWeightTwoD' num2str(i)];
      printLatexPlot(fileName, directory, plotWidth)
      set(a, 'color', blackColor)
      fileName = ['cheightWeightTwoD' num2str(i) 'a'];
      printLatexPlot(fileName, directory, plotWidth)


    end
      
```

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Joint Distribution\vspace{0.0cm}\only<1-3>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD}}\only<4>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD1}}\only<5-6>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD1a}}\only<7>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD2}}\only<8-9>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD2a}}\only<10>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD3}}\only<11-12>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD3a}}\only<13>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD4}}\only<14-15>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD4a}}\only<16>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD5}}\only<17-18>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD5a}}\only<19>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD6}}\only<20-21>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD6a}}\only<22>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD7}}\only<23>{\inputdiagram{../../ml/diagrams/cheightWeightTwoD7a}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Marginal Distributions\vspace{0.0cm}\only<1>{
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         \inputdiagram{../../ml/diagrams/cheightGaussianSmall}}\only<2-4>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall1}}\only<5-7>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall2}}\only<8-10>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall3}}\only<11-13>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall4}}\only<14-16>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall5}}\only<17-19>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall6}}\only<20-22>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall7}}\only<23>{\inputdiagram{../../ml/diagrams/cheightGaussianSmall7a}}\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       \only<1-2>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall}}\only<3-4>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall1}}\only<5>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall1a}}\only<6-7>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall2}}\only<8>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall2a}}\only<9-10>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall3}}\only<11>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall3a}}\only<12-13>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall4}}\only<14>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall4a}}\only<15-16>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall5}}\only<17>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall5a}}\only<18-19>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall6}}\only<20>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall6a}}\only<21-22>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall7}}\only<23>{\inputdiagram{../../ml/diagrams/cweightGaussianSmall7a}}
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!--frame end-->

