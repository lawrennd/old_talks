\code{
randn('seed', 1e4);
rand('seed', 1e4);

importTool('kern');
kernToolboxes
importTool('drawing');

fillColor = [0.7 0.7 0.7];

blueColor = [1, 1, 0];
redColor = [0, 1, 1];
greenColor = [1 0 1];
magentaColor = [0, 1, 0];
blackColor = [1, 1, 1];

markerSize = 10;
markerWidth = 4;
markerType = 'kx';

lineWidth = 4;
textWidth = 13;

directory = '../../../ml/tex/diagrams/';
}

###

\code{
    close all

    yLim = [-2.2 2.2];
    yTick = [-2 -1 0 1 2];
    xLim = [-2 2];
    xTick = [-2 -1 0 1 2];
    errYlim = [-12 20];
    x = linspace(-1, 1, 6)';
    trueKern = kernCreate(x, {'rbf', 'white'});
    trueKern.comp{2}.variance = 0.01;
    K = kernCompute(trueKern, x);
    y = gsamp(zeros(1, 6), K, 1)';
    
    xtest = linspace(xLim(1), xLim(2), 200)';
    kern = trueKern;
    
    lengthScale = [0.05 0.1 0.25 0.5 1 2 4 8 16];
    counter = 0;
    
    % p = plot(x, y, markerType);
    % set(p, 'markersize', markerSize, 'lineWidth', markerWidth);
    % set(gca, 'ylim', [-2 1])
    % set(gca, 'xlim', [-1.5 1.5])
    
    % fileName = ['gpOptimise' num2str(counter)];
    % printLatexPlot(fileName, '../../../gp/tex/diagrams', 0.45*textWidth);
    
    clf
    
    void = semilogx(NaN, NaN, 'kx-');
    set(gca, 'fontname', 'times')
    set(gca, 'fontsize', 18)
    set(gca, 'ylim', errYlim)
    set(gca, 'xlim', [0.025 32]) 
    set(gca, 'xtick', [0.01 0.1 1 10 100])
    set(gca, 'xticklabel', {'$10^{-2}$', '$10^{-1}$', '$10^0$', '$10^1$', '$10^2$'})
    grid on
    ylabel('negative log likelihood')
    %fileName = ['gpOtimise' num2str(counter)];
    %printLatexPlot(fileName, '../../../gp/tex/diagrams', 0.4*textWidth);
    includeText = [];
    for i = 1:length(lengthScale)
      kern.comp{1}.inverseWidth = 1/(lengthScale(i)*lengthScale(i));
      K = kernCompute(kern, x);
      [invK, U] = pdinv(K);
      logDetK = logdet(K, U);
      err(i) = 0.5*(logDetK + y'*invK*y);
      errLogDet(i) = 0.5*(logDetK);
      errFit(i) = 0.5*y'*invK*y;
      Kx = kernCompute(kern, x, xtest);
      ypredMean = Kx'*invK*y;
      ypredVar = kernDiagCompute(kern, xtest) - sum((Kx'*invK).*Kx', 2);
      ypredSd = sqrt(ypredVar);
      counter = counter + 1;
      clf
      patch([xtest; xtest(end:-1:1)], ...
            [ypredMean; ypredMean(end:-1:1)] ...
            + 2*[ypredSd; -ypredSd], ...
            fillColor,'edgecolor',fillColor)
      hold on;
      t = plot(xtest, ypredMean, '-');
      set(t, 'color', blackColor);
%      ylabel('$\dataScalar(\inputScalar)$')
%      xlabel('$\inputScalar$')

      p = plot(x, y, 'x', 'color', blueColor);
      set(p, 'markersize', markerSize, 'lineWidth', markerWidth);
      set(t, 'linewidth', lineWidth);
      set(gca, 'ylim', yLim, 'ytick', yTick, 'xlim', xLim, 'xtick', xTick)
      xlim = get(gca, 'xlim');
      ylim = get(gca, 'ylim');
      line([xlim(1) xlim(1)], ylim, 'color', blackColor);
      line(xlim, [ylim(1) ylim(1)], 'color', blackColor);
      
      fileName = ['gpOptimise' num2str(counter)];
      printLatexPlot(fileName, directory, 0.8*textWidth);
      includeText = [includeText '\only<' num2str(i) '>{\inputdiagram{' directory fileName '}\hfill}'];

      counter = counter + 1;
      clf
      t = semilogx(lengthScale(1:i), err(1:i), 'x-', 'color', greenColor);
      hold on
      t = [t; semilogx(lengthScale(1:i), errLogDet(1:i), 'x-', 'color', blueColor)];
      t = [t; semilogx(lengthScale(1:i), errFit(1:i), 'x-', 'color', redColor)];
      set(t, 'markersize', markerSize, 'lineWidth', markerWidth);
      set(gca, 'ylim', errYlim)
      set(gca, 'xlim', [0.025 32]) 
      set(gca, 'xtick', [0.01 0.1 1 10 100])
      set(gca, 'xticklabel', {'$10^{-2}$', '$10^{-1}$', '$10^0$', '$10^1$', '$10^2$'})
  
      grid on
%      xlabel('length scale, $\lengthScale$')
      xlim = get(gca, 'xlim');
      ylim = get(gca, 'ylim');
      line([xlim(1) xlim(1)], ylim, 'color', blackColor);
      line(xlim, [ylim(1) ylim(1)], 'color', blackColor);

     % fileName = ['gpOptimise' num2str(counter)];
     %  printLatexPlot(fileName, directory, 0.45*textWidth);
     %  includeText = [includeText '\only<' num2str(i) '>{\inputdiagram{' directory fileName '}}'];
    end
    printLatexText(includeText, 'gpOptimiseIncludeText.tex', directory)

    }

\includeimg{../../../ml/tex/diagrams/gpOptimiseIncludeText}
