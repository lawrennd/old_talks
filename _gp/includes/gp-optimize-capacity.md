\ifndef{gpOptimizeCapacity}
\define{gpOptimizeCapacity}

\editme

\plotcode{      clf
      lambda1 = 3;
      lambda2 = 1;
      t = linspace(-pi, pi, 200);
      R = [sqrt(2)/2 -sqrt(2)/2; sqrt(2)/2 sqrt(2)/2];
      xy = R*[lambda1*sin(t); lambda2*cos(t)];
      line(xy(1, :), xy(2, :), 'linewidth', 3, 'color', blackColor);
      axis off, axis equal
      a = arrow([0 lambda1*R(1, 1)], [0 lambda1*R(2, 1)]);
      set(a, 'linewidth', 3, 'color', blueColor);
      a = arrow([0 lambda2*R(1, 2)], [0 lambda2*R(2, 2)]);
      set(a, 'linewidth', 3, 'color', blueColor);
      xlim = get(gca, 'xlim');
      xspan = xlim(2) - xlim(1);
      ylim = get(gca, 'ylim');
      yspan = ylim(2) - ylim(1);
      text(lambda1*0.5*R(1, 1)-0.05*xspan, lambda1*0.5*R(2, 1)-yspan*0.05, '$\eigenvalue_1$')
      text(lambda2*0.5*R(1, 2)-0.05*xspan, lambda2*0.5*R(2, 2)-yspan*0.05, '$\eigenvalue_2$')
      fileName = 'gpOptimiseEigen';
      printLatexPlot(fileName, directory, 0.45*textWidth)}

\subsection{Capacity Control through the Determinant}

The parameters are *inside* the covariance function (matrix).
\normalsize
$$\kernelScalar_{i, j} = \kernelScalar(\inputVals_i, \inputVals_j; \parameterVector)$$


\newslide{Eigendecomposition of Covariance}

[\Large
$$\kernelMatrix = \rotationMatrix \eigenvalueMatrix^2 \rotationMatrix^\top$$]{}

\code{gpoptimizePlot1}

\columns{\includepng{\diagramsDir/gp/gp-optimize-eigen}{100%}{negate}}{$\eigenvalueMatrix$ represents distance on axes.
$\rotationMatrix$ gives rotation.}{50%}{50%}


\newslide{Eigendecomposition of Covariance}

* $\eigenvalueMatrix$ is *diagonal*, $\rotationMatrix^\top\rotationMatrix = \eye$. 
* Useful representation since $\det{\kernelMatrix} = \det{\eigenvalueMatrix^2} = \det{\eigenvalueMatrix}^2$.

\newslide{Capacity control: $\color{\blueColor}{\log \det{\kernelMatrix}}$}


\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai
import teaching_plots as plot}


\code{diagrams = './gp/'}

\plotcode{plot.covariance_capacity(rotate_angle=np.pi/4, lambda1 = 0.5, lambda2 = 0.3, diagrams = '\writeDiagramsDir/gp/')
}

\slides{\define{width}{80%}
\startanimation{gp-optimise-determinant}{0}{10}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant000}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant001}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant002}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant003}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant004}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant005}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant006}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant007}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant008}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant009}{\width}}{gp-optimise-determinant}
\endanimation}

\notes{\figure{\includediagram{\diagramsDir/gp/gp-optimise-determinant009}{80%}}{The determinant of the covariance is dependent only on the eigenvalues. It represents the 'footprint' of the Gaussian.}{gp-optimise-determinant-figure}}

\newslide{Data Fit: $\color{\redColor}{\frac{\dataVector^\top\kernelMatrix^{-1}\dataVector}{2}}$}

\plotcode{    clf
    includeText = [];
    counter = 0;
    plotWidth = 0.6*textWidth;
    lambda1 = 3;
    lambda2 = 1;
    t = linspace(-pi, pi, 200);
    R = [sqrt(2)/2 -sqrt(2)/2; sqrt(2)/2 sqrt(2)/2];
    xy = [lambda1*sin(t); lambda2*cos(t)];
    contourHand = line(xy(1, :), xy(2, :), 'color', blackColor);
    xy = [lambda1*sin(t); lambda2*cos(t)]*2;
    lim = [-1 1]*max([lambda1 lambda2])*2.2;
    set(gca, 'xlim', lim, 'ylim', lim)
    axis equal


    contourHand = [contourHand line(xy(1, :), xy(2, :), 'color', blackColor)];
    set(contourHand, 'linewidth', 2, 'color', redColor)
    arrowHand = arrow([0 lambda1], [0 0]);
    arrowHand = [arrowHand arrow([0 0], [0 lambda2])];
    set(arrowHand, 'linewidth', 3, 'color', blackColor);
    xlim = get(gca, 'xlim');
    xspan = xlim(2) - xlim(1);
    ylim = get(gca, 'ylim');
    yspan = ylim(2) - ylim(1);
    eigLabel = text(lambda1*0.5, -yspan*0.05, '$\eigenvalue_1$', 'horizontalalignment', 'center');
    eigLabel = [eigLabel text(-0.05*xspan, lambda2*0.5, '$\eigenvalue_2$', 'horizontalalignment', 'center')];
    xlabel('$\dataScalar_1$')
    ylabel('$\dataScalar_2$')
    
    box off
    xlim = get(gca, 'xlim');
    ylim = get(gca, 'ylim');
    line([xlim(1) xlim(1)], ylim, 'color', blackColor)
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
    
    fileName = ['gpOptimiseQuadratic' num2str(counter)];
    printLatexPlot(fileName, directory, plotWidth);
    includeText = [includeText '\only<' num2str(counter) '>{\inputdiagram{' directory fileName '}}'];
    counter = counter + 1;

    y = [1.2 1.4];
    dataHand = line(y(1), y(2), 'marker', 'x', 'markersize', markerSize, 'linewidth', markerWidth, 'color', blackColor);
    
    fileName = ['gpOptimiseQuadratic' num2str(counter)];
    printLatexPlot(fileName, directory, plotWidth);
    includeText = [includeText '\only<' num2str(counter) '>{\inputdiagram{' directory fileName '}}'];
    counter = counter + 1;

    
    rotateObject(rotationMatrix, arrowHand);
    rotateObject(rotationMatrix, contourHand);
    rotateObject(rotationMatrix, eigLabel);
    
    fileName = ['gpOptimiseQuadratic' num2str(counter)];
    printLatexPlot(fileName, directory, plotWidth);
    includeText = [includeText '\only<' num2str(counter) '>{\inputdiagram{' directory fileName '}}'];
    counter = counter + 1;
    
    printLatexText(includeText, 'gpOptimiseQuadraticIncludeText.tex', directory)
}

\slides{\define{width}{80%}
\startanimation{gp-optimise-quadratic}{0}{2}
\newframe{\includediagram{\diagramsDir/gp/diagrams/gp-optimise-quadratic000}{\width}}{gp-optimise-quadratic}
\newframe{\includediagram{\diagramsDir/gp/diagrams/gp-optimise-quadratic001}{\width}}{gp-optimise-quadratic}
\newframe{\includediagram{\diagramsDir/gp/diagrams/gp-optimise-quadratic002}{\width}}{gp-optimise-quadratic}
\endanimation}

\figure{\includediagram{\diagramsDir/gp/diagrams/gp-optimise-quadratic002}{80%}}{The data fit term of the Gaussian process is a quadratic loss centered around zero. This has eliptical contours, the principal axes of which are given by the covariance matrix.}{gp-optimise-quadratic}

\newslide{$$\errorFunction(\parameterVector) = \color{\blueColor}{\frac{1}{2}\log\det{\kernelMatrix}}+\color{\redColor}{\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$}

\endif
