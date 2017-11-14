\ifdefined\blackBackground\global\long\def\redColor{cyan}
\global\long\def\magentaColor{green} \global\long\def\blueColor{yellow}
\else\global\long\def\redColor{red}
\global\long\def\magentaColor{magenta} \global\long\def\blueColor{blue}
\fi

``` {#mycode .octave .numberLines startFrom="0"}

%}
  importTool('ndlutil');
  textWidth = 13;
  randn('seed', 1e6);
  rand('seed', 1e6);
  markerSize = 16;
  markerLineWidth = 6;
  redColor = [1, 0, 0];
  greenColor = [0, 1, 0];
  blueColor = [0, 0, 1];
  magentaColor = [1, 0, 1];
  blackColor = [0, 0, 0];
  cyanColor = [0, 1, 1];
  yellowColor = [1, 1, 0];
  negative = false;
  if blackBackground
    negative = true;
    redColor = 1-redColor;
    greenColor = 1-greenColor;
    blueColor =  1-blueColor;
    magentaColor = 1-magentaColor;
    cyanColor = 1-cyanColor;
    yellowColor = 1-yellowColor;
    blackColor = 1- blackColor;
  end
%{
```

frame start

\[plain\]

\Huge $$y = mx + c$$

frame end

frame start

\[plain,fragile\]

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    x = [1; 3];
    y = [3; 1];
    figure(1), clf
    ylim = [0 5];
    xlim = [0 5];
    xvals = linspace(xlim(1), xlim(2), 2);
    m = (y(2)-y(1))/(x(2)-x(1));
    c = y(1)-m*x(1);
    yvals = m*xvals+c;
    hold on
    a = plot(xvals, yvals, '-');
    set(a, 'linewidth', 2, 'color', blueColor)
    set(gca, 'xtick', [0 1 2 3 4 5])
    set(gca, 'ytick', [0 1 2 3 4 5])
    set(gca, 'ylim', ylim)
    set(gca, 'xlim', xlim)
    set(gca, 'box', 'off')
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    xlabel('$\inputScalar$')
    ylabel('$\dataScalar$')
    text(4, 4, '\Huge $y=mx+c$',  'horizontalalignment', 'center', 'verticalalignment', 'bottom')
    printLatexPlot('straightLine1', '../../../ml/tex/diagrams', 0.75*textWidth)
    
    ctext = text(0.15, c+0.15, '\large $c$',  'horizontalalignment', 'center', 'verticalalignment', 'bottom')
    xl = [1.5 2.5];
    yl = xl*m + c;
    mhand = line([xl(1) xl(2)], [min(yl) min(yl)], 'color', blackColor);
    mhand = [mhand line([min(xl) min(xl)], [yl(1) yl(2)], 'color', blackColor)];
    mtext = text(mean(xl), min(yl)-0.2, '\large $m$',  'horizontalalignment', 'center', 'verticalalignment', 'bottom');
    printLatexPlot('straightLine2', '../../../ml/tex/diagrams', 0.75*textWidth)
    a2 = plot(x, y, 'x');
    set(a2, 'markersize', markerSize, 'linewidth', markerLineWidth, 'color', redColor)
    printLatexPlot('straightLine3', '../../../ml/tex/diagrams', 0.75*textWidth)
    xs = 2;
    ys = m*xs + c + randn(1)*0.5;
    as = plot(xs, ys, 'x');
    set(as, 'markersize', markerSize, 'linewidth', markerLineWidth, 'color', greenColor)
    printLatexPlot('straightLine4', '../../../ml/tex/diagrams', 0.75*textWidth)
    m = (y(2)-ys(1))/(x(2)-xs(1));
    c = ys(1)-m*xs(1);
    yvals = m*xvals+c;
    hold on
    set(a, 'visible', false)
    set(mhand, 'visible', false)
    set(mtext, 'visible', false)
    set(ctext, 'visible', false)
    a3 = plot(xvals, yvals, '-');
    set(a3, 'linewidth', 2, 'color', blueColor)
    set(as, 'color', redColor)
    printLatexPlot('straightLine5', '../../../ml/tex/diagrams', 0.75*textWidth)
    m = (ys(1)-y(1))/(xs(1)-x(1));
    c = y(1)-m*x(1);
    yvals = m*xvals+c;
    hold on
    set(a3, 'visible', false)
    a4 = plot(xvals, yvals, '-');
    set(a4, 'linewidth', 2, 'color', blueColor)
    set(as, 'color', redColor)
    printLatexPlot('straightLine6', '../../../ml/tex/diagrams', 0.75*textWidth)
    set(a, 'visible', true)
    set(a3, 'visible', true)
    printLatexPlot('straightLine7', '../../../ml/tex/diagrams', 0.75*textWidth)
    %{
  
```

overprint start

\onslide<1> ![](../../../ml/tex/diagrams/straight_line1.png) \onslide<2>
![](../../../ml/tex/diagrams/straight_line2.png) \onslide<3>
![](../../../ml/tex/diagrams/straight_line3.png) \onslide<4>
![](../../../ml/tex/diagrams/straight_line4.png) \onslide<5>
![](../../../ml/tex/diagrams/straight_line5.png) \onslide<6>
![](../../../ml/tex/diagrams/straight_line6.png) \onslide<7>
![](../../../ml/tex/diagrams/straight_line7.png)

overprint end

frame end

frame start

\[plain\]

### $y = mx + c$

\huge point 1: $x = 1$, $y=3$ $$3 = m + c$$ point 2: $x = 3$, $y=1$
$$1 = 3m + c$$ point 3: $x = 2$, $y=2.5$ $$2.5 = 2m + c$$

frame end

frame start

\[plain,t\]

![image](../../../ml/tex/diagrams/Pierre-Simon_Laplace.png){height="\textheight"}

frame end

frame start

\[plain,t\]

![image](../../../ml/tex/diagrams/laplacesDeterminismFrench.png){height="\textheight"}

frame end

frame start

\[plain\]

![image](../../../ml/tex/diagrams/laplacesDeterminismEnglish.png){height="\textheight"}

frame end

frame start

\[plain,t\]

![image](../../../ml/tex/diagrams/philosophicaless00lapliala.pdf){height="\textheight"}

frame end

frame start

### $y = mx + c + \epsilon$

\huge point 1: $x = 1$, $y=3$ $$3 = m + c + \epsilon_1$$ point 2:
$x = 3$, $y=1$ $$1 = 3m + c + \epsilon_2$$ point 3: $x = 2$, $y=2.5$
$$2.5 = 2m + c + \epsilon_3$$

frame end
