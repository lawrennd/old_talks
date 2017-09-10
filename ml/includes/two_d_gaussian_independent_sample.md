```

<!--frame start-->

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
    heightFig = figure(2); clf
    a = plot(h, ph, '-', 'color', redColor);
    set(gca, 'xtick', [1.25 1.7 2.15]);
    set(gca, 'ytick', [1 2 3]);
    set(a, 'linewidth', lineWidth);
    xlabel('$h/m$')
    ylabel('$p(h)$')
    axis off

    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off

    weightFig = figure(3), clf
    a = plot(w, pw, '-', 'color', blueColor);
    set(a, 'linewidth', lineWidth);
    set(gca, 'xtick', [55 75 95]);
    set(gca, 'ytick', [0.02 0.04 0.06]);
    xlabel('$w/kg$')
    ylabel('$p(w)$')
    axis off
    
    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off
    
    numSamps = 10;
    twoDfig = figure(1); clf
    axes;
    a = plot(muh, muw, 'x', 'color', magentaColor, 'markersize', markerSize/2, 'linewidth', markerLineWidth);
    theta = linspace(0, tau, 100);
    xel = sin(theta)*sqrt(varh) + muh;
    yel = cos(theta)*sqrt(varw) + muw;
    hold on
    a = plot(xel, yel, '-', 'color', magentaColor);
    set(a, 'linewidth', 3);
    set(gca, 'xlim', [min(h) max(h)], 'ylim', [min(w) max(w)], 'xtick', [55 75 95], 'ytick', [1.25 1.7 2.15])
    xlabel('$h/m$')
    ylabel('$w/kg$')

    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off

    printLatexPlot('heightWeightTwoD', directory, plotWidth)
    
    figure(heightFig)
    set(gca, 'xticklabel', [])
    set(gca, 'yticklabel', [])
    xlabel('')

    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off

    printLatexPlot('heightGaussianSmall', directory, plotWidthTwo)
    
    figure(weightFig)
    set(gca, 'xticklabel', [])
    set(gca, 'yticklabel', [])
    xlabel('')

    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    box off

    printLatexPlot('weightGaussianSmall', directory, plotWidthTwo)

    includeTextOne = [];
    includeTextTwo = [];
    includeTextThree = [];
    for i = 1:numSamps
      hval = randn(1)*sqrt(varh) + muh;
      wval = randn(1)*sqrt(varw) + muw;

            figure(heightFig)
      a = line(hval, 0.1, 'marker', 'x', 'linewidth', markerLineWidth, 'color', redColor);
      fileName = ['heightGaussianSmall' num2str(i)];
      printLatexPlot(fileName, directory, plotWidthTwo)
      includeTextOne = [includeTextOne '\inputdiagram{' directory fileName '}'];
      set(a, 'color', blackColor)
      fileName = ['heightGaussianSmall' num2str(i) 'a'];
      printLatexPlot(fileName, directory, plotWidthTwo)
      includeTextOne = [includeTextOne '\inputdiagram{' directory fileName '}'];
      figure(weightFig)
      a = line(wval, 0.002, 'marker', 'x', 'linewidth', markerLineWidth, 'color', redColor);
      fileName = ['weightGaussianSmall' num2str(i)];
      printLatexPlot(fileName, directory, plotWidthTwo);
      includeTextTwo = [includeTextTwo '\inputdiagram{' directory fileName '}'];
      set(a, 'color', blackColor)
      fileName = ['weightGaussianSmall' num2str(i) 'a'];
      printLatexPlot(fileName, directory, plotWidthTwo);
      includeTextTwo = [includeTextTwo '\inputdiagram{' directory fileName '}'];
      figure(twoDfig)
      a = line(hval, wval, 'marker', 'x', 'linewidth', markerLineWidth, 'color', redColor);
      fileName = ['heightWeightTwoD' num2str(i)];
      printLatexPlot(fileName, directory, plotWidth);
      includeTextThree = [includeTextThree '\inputdiagram{' directory fileName '}'];
      set(a, 'color', blackColor)
      fileName = ['heightWeightTwoD' num2str(i) 'a'];
      printLatexPlot(fileName, directory, plotWidth);
      includeTextThree = [includeTextThree '\inputdiagram{' directory fileName '}'];
    end
      
```

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Joint Distribution\vspace{0.0cm}\only<1-3>{\inputdiagram{../../ml/diagrams/heightWeightTwoD}}\only<4>{\inputdiagram{../../ml/diagrams/heightWeightTwoD1}}\only<5-6>{\inputdiagram{../../ml/diagrams/heightWeightTwoD1a}}\only<7>{\inputdiagram{../../ml/diagrams/heightWeightTwoD2}}\only<8-9>{\inputdiagram{../../ml/diagrams/heightWeightTwoD2a}}\only<10>{\inputdiagram{../../ml/diagrams/heightWeightTwoD3}}\only<11-12>{\inputdiagram{../../ml/diagrams/heightWeightTwoD3a}}\only<13>{\inputdiagram{../../ml/diagrams/heightWeightTwoD4}}\only<14-15>{\inputdiagram{../../ml/diagrams/heightWeightTwoD4a}}\only<16>{\inputdiagram{../../ml/diagrams/heightWeightTwoD5}}\only<17-18>{\inputdiagram{../../ml/diagrams/heightWeightTwoD5a}}\only<19>{\inputdiagram{../../ml/diagrams/heightWeightTwoD6}}\only<20-21>{\inputdiagram{../../ml/diagrams/heightWeightTwoD6a}}\only<22>{\inputdiagram{../../ml/diagrams/heightWeightTwoD7}}\only<23>{\inputdiagram{../../ml/diagrams/heightWeightTwoD7a}}                                                                                                                                                                                                        Marginal Distributions\vspace{0.0cm}\only<1>{\inputdiagram{../../ml/diagrams/heightGaussianSmall}}\only<2-4>{\inputdiagram{../../ml/diagrams/heightGaussianSmall1}}\only<5-7>{\inputdiagram{../../ml/diagrams/heightGaussianSmall2}}\only<8-10>{\inputdiagram{../../ml/diagrams/heightGaussianSmall3}}\only<11-13>{\inputdiagram{../../ml/diagrams/heightGaussianSmall4}}\only<14-16>{\inputdiagram{../../ml/diagrams/heightGaussianSmall5}}\only<17-19>{\inputdiagram{../../ml/diagrams/heightGaussianSmall6}}\only<20-22>{\inputdiagram{../../ml/diagrams/heightGaussianSmall7}}\only<23>{\inputdiagram{../../ml/diagrams/heightGaussianSmall7a}}\
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        \only<1-2>{\inputdiagram{../../ml/diagrams/weightGaussianSmall}}\only<3-4>{\inputdiagram{../../ml/diagrams/weightGaussianSmall1}}\only<5>{\inputdiagram{../../ml/diagrams/weightGaussianSmall1a}}\only<6-7>{\inputdiagram{../../ml/diagrams/weightGaussianSmall2}}\only<8>{\inputdiagram{../../ml/diagrams/weightGaussianSmall2a}}\only<9-10>{\inputdiagram{../../ml/diagrams/weightGaussianSmall3}}\only<11>{\inputdiagram{../../ml/diagrams/weightGaussianSmall3a}}\only<12-13>{\inputdiagram{../../ml/diagrams/weightGaussianSmall4}}\only<14>{\inputdiagram{../../ml/diagrams/weightGaussianSmall4a}}\only<15-16>{\inputdiagram{../../ml/diagrams/weightGaussianSmall5}}\only<17>{\inputdiagram{../../ml/diagrams/weightGaussianSmall5a}}\only<18-19>{\inputdiagram{../../ml/diagrams/weightGaussianSmall6}}\only<20>{\inputdiagram{../../ml/diagrams/weightGaussianSmall6a}}\only<21-22>{\inputdiagram{../../ml/diagrams/weightGaussianSmall7}}\only<23>{\inputdiagram{../../ml/diagrams/weightGaussianSmall7a}}
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Samples of height and weight

<!--frame end-->

