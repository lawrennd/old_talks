\ifndef{entropyBilliards}
\define{entropyBilliards}

\editme

\newslide{}

\figure{<div>
<canvas id="billiardsCanvas" width="900" height="500" style="border:1px solid black;display: block; "></canvas>
<script src="../scripts/ballworld/constructors.js"></script>
<script src="../scripts/ballworld/script2.js"></script>
<script src="../scripts/ballworld/ballworld.js"></script>
<script src="../scripts/ballworld/multiball.js"></script>
</div>}{Bernoulli's simple kinetic models of gases assume that the molecules of air operate like billiard balls.}{entropy-billiards-js}


\newslide{}

\figure{\includepng{\diagramsDir/ml/entropy-billiards}}{Bernoulli's simple kinetic models of gases assume that the molecules of air operate like billiard balls.}{entropy-billiards}

\newslide{}

\code{
    a = randn(10000, 1);
    [heights, centres] = hist(a, 20);
    a = bar(centres, heights/sum(heights)/(centres(2)-centres(1)));
    set(a, 'facecolor', blueColor);
    xlim = [-4 4];
    set(gca, 'xlim', xlim);
    ylim = get(gca, 'ylim');
    
    x = linspace(xlim(1), xlim(2), 200);
    y = 1/sqrt(2*pi)*exp(-1/2*x.*x);
    line(x, y, 'color', redColor, 'linewidth', 3);
    line([xlim(1) xlim(1)], ylim, 'color', blackColor);
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor);
    printLatexPlot('gaussian-histogram', '\writeDiagramsDir/ml', 0.75*textWidth)}

\endif
