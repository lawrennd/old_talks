``` {#mycode .octave .numberLines startFrom="0"}

%}
  importLatest('GPmat')
  importLatest('netlab')
  randn('seed', 1e6)
  rand('seed', 1e6)
  textWidth = 13
  dirName = '../../../gplvm/tex/diagrams/';
  redColor = [1, 0, 0];
  greenColor = [0, 1, 0];
  blueColor = [0, 0, 1];
  magentaColor = [1, 0, 1];
  blackColor = [0, 0, 0];
  whiteColor = [1, 1, 1];
  negative = false;
  if blackBackground
    negative = true;
    redColor = 1-redColor;
    greenColor = 1-greenColor;
    blueColor =  1-blueColor;
    magentaColor = 1-magentaColor;
    blackColor = 1- blackColor;
    whiteColor = 1- whiteColor;
  end
%{
```

<!--frame start-->
\[fragile\]

### Gaussian Processes: Extremely Short Overview

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    t_train_ind = [15, 40, 80]';
    t = linspace(0,10, 100)';
    kern = kernCreate(t, 'rbf');
    K = kernCompute(kern, t);
    F = gsamp(zeros(1, 100), K, 1000);
    Ffew = gsamp(zeros(1, 100), K, 10);
    F_train = F(1, t_train_ind);
    F_post_ind = find(sqrt(dist2(F(:, t_train_ind), F_train))<0.5);
    a = plot(t, F');
    for i = 1:length(a)
      col = get(a(i), 'color');
      if negative
        set(a(i), 'color', 1-col);
      end
      set(a(i), 'visible', 'off');
    end
    hold on
    aFew = plot(t, Ffew');
    for i = 1:length(aFew)
      col = get(aFew(i), 'color');
      if negative
        set(aFew(i), 'color', 1-col);
      end
    end
    ylim = get(gca, 'ylim');
    xlim = get(gca, 'xlim');
    box off
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    printLatexPlot('gpPriorSamplesFew', dirName, 0.4*textWidth);
    for i = 1:length(a)
      set(a(i), 'visible', 'on');
    end
    aFew = plot(t, Ffew')
    for i = 1:length(aFew)
      set(aFew(i), 'visible', 'off');
    end
    printLatexPlot('gpPriorSamples', dirName, 0.4*textWidth);
    plot(t(t_train_ind), F_train, 'x', 'linewidth', 4, 'markersize', 10, 'color', whiteColor);
    printLatexPlot('gpPriorSamplesData', dirName, 0.4*textWidth);
    figure
    b = plot(t, F(F_post_ind, :)');
    for i = 1:length(F_post_ind)
       set(b(i), 'color', get(a(F_post_ind(i)), 'color'))
    end
    hold on
    plot(t(t_train_ind), F_train, 'x', 'linewidth', 4, 'markersize', 10, 'color', blackColor);
    set(gca, 'ylim', ylim)
    box off
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    printLatexPlot('gpRejectionSamples', dirName, 0.4*textWidth);
    
    %{
  
```

\only<1>{\inputdiagram{../../../gplvm/tex/diagrams/gpPriorSamplesFew}}
\only<2>{\inputdiagram{../../../gplvm/tex/diagrams/gpPriorSamples}}
\only<3->{\inputdiagram{../../../gplvm/tex/diagrams/gpPriorSamplesData}}\hfill
\only<4->{\inputdiagram{../../../gplvm/tex/diagrams/gpRejectionSamples}}

<!--frame end-->

