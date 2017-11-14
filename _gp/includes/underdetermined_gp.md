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
  markerSize = 8;
  markerLineWidth = 6;
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

frame start

\[plain,fragile\]

### Underdetermined System

columns start

\[c\] {column width=0.5\\textwidth}

overprint start

{onslide slideno=&lt;1&gt;} What about two unknowns and *one*
observation? $$\dataScalar_1 =  m\inputScalar_1 + c$$
{onslide slideno=&lt;2&gt;} Can compute $m$ given $c$.
$$m = \frac{\dataScalar_1 -c}{\inputScalar}$$
{onslide slideno=&lt;3&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval1.tex}c=1.75\Longrightarrow m=1.25\PandocEndInclude{input}{50}{53}$$
{onslide slideno=&lt;4&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval2.tex}c=-0.777\Longrightarrow m=3.78\PandocEndInclude{input}{55}{53}$$
{onslide slideno=&lt;5&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval3.tex}c=-4.01\Longrightarrow m=7.01\PandocEndInclude{input}{60}{53}$$
{onslide slideno=&lt;6&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval4.tex}c=-0.718\Longrightarrow m=3.72\PandocEndInclude{input}{65}{53}$$
{onslide slideno=&lt;7&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval5.tex}c=2.45\Longrightarrow m=0.545\PandocEndInclude{input}{70}{53}$$
{onslide slideno=&lt;8&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval6.tex}c=-0.657\Longrightarrow m=3.66\PandocEndInclude{input}{75}{53}$$
{onslide slideno=&lt;9&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval7.tex}c=-3.13\Longrightarrow m=6.13\PandocEndInclude{input}{80}{53}$$
{onslide slideno=&lt;10&gt;} Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval8.tex}c=-1.47\Longrightarrow m=4.47\PandocEndInclude{input}{85}{53}$$
{onslide slideno=&lt;11&gt;} Can compute $m$ given $c$.\
Assume $$c\sim \gaussianSamp{0}{4},$$ we find a distribution of
solutions.

overprint end

{column width=0.5\\textwidth}

``` {#mycode .octave .numberLines startFrom="0"}

      %}
      x = [1];
      y = [3];
      figure(1), clf
      a = plot(x, y, 'x');
      set(a, 'markersize', markerSize, 'linewidth', markerLineWidth, 'color', redColor)
      set(gca, 'xtick', [0 1 2 3])
      set(gca, 'ytick', [0 1 2 3 4 5])
      ylim = [0 5];
      xlim = [0 3];
      set(gca, 'ylim', ylim)
      set(gca, 'xlim', xlim)
      set(gca, 'box', 'off')
      line([xlim(1) xlim(1)], ylim, 'color', blackColor)
      line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
      
      xlabel('$\inputScalar$')
      ylabel('$\dataScalar$')
      printLatexPlot('onePoint', '../../../ml/tex/diagrams', 0.45*textWidth)

      
      xvals = linspace(0, 3, 2);
      for i = 1:100
        
        c = randn(1)*2;
        m = (y - c)/x;
        yvals = m*xvals+c;
        hold on
        a = plot(xvals, yvals, '-');
        set(a, 'linewidth', 2, 'color', blueColor)
        if i < 9 || i == 100
          if i < 9 
            printLatexText(['c=' numsf2str(c, 3) '\Longrightarrow m=' numsf2str(m, 3)], ['onePointCval' num2str(i)  '.tex'], '../../../ml/tex/diagrams')
          end
          printLatexPlot(['onePoint' num2str(i)], '../../../ml/tex/diagrams', 0.45*textWidth)
        end
        
      end
      %{
    
```

overprint start

{onslide slideno=&lt;1-2&gt;}![](../../../ml/tex/diagrams/one_point.png)
{onslide slideno=&lt;3&gt;}![](../../../ml/tex/diagrams/one_point1.png)
{onslide slideno=&lt;4&gt;}![](../../../ml/tex/diagrams/one_point2.png)
{onslide slideno=&lt;5&gt;}![](../../../ml/tex/diagrams/one_point3.png)
{onslide slideno=&lt;6&gt;}![](../../../ml/tex/diagrams/one_point4.png)
{onslide slideno=&lt;7&gt;}![](../../../ml/tex/diagrams/one_point5.png)
{onslide slideno=&lt;8&gt;}![](../../../ml/tex/diagrams/one_point6.png)
{onslide slideno=&lt;9&gt;}![](../../../ml/tex/diagrams/one_point7.png)
{onslide slideno=&lt;10&gt;}![](../../../ml/tex/diagrams/one_point8.png)
{onslide slideno=&lt;11&gt;}![](../../../ml/tex/diagrams/one_point100.png)

overprint end

columns end

frame end
