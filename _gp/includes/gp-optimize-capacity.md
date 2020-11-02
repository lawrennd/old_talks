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

\code{fill_color = [1., 1., 0.]
black_color = [0., 0., 0.]
blue_color = [0., 0., 1.]
magenta_color = [1., 0., 1.]}

\code{diagrams = './gp/'}

\plotcode{rotate_angle = np.pi/4
lambda1 = 0.5
lambda2 = 0.3

counter = 0

fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.set_axis_off()
cax = fig.add_axes([0., 0., 1., 1.])
cax.set_axis_off()

cax.set_xlim([0., 1.])
cax.set_ylim([0., 1.])

# Matrix label axes
tax2 = fig.add_axes([0, 0.47, 0.1, 0.1])
tax2.set_xlim([0, 1.])
tax2.set_ylim([0, 1.])
tax2.set_axis_off()
label_eigenvalue = tax2.text(0.5, 0.5, r'$\Lambda=$', fontsize=20)

ax = fig.add_axes([0.5, 0.25, 0.5, 0.5])
ax.set_xlim([-0.25, 0.6])
ax.set_ylim([-0.25, 0.6])
from matplotlib.patches import Polygon
pat_hand = ax.add_patch(Polygon(np.column_stack(([0, 0, lambda1, lambda1], 
                    [0, lambda2, lambda2, 0])), 
                    facecolor=fill_color, 
                    edgecolor=black_color, 
                    visible=False))
data = pat_hand.get_path().vertices
rotation_matrix = np.asarray([[np.cos(rotate_angle), -np.sin(rotate_angle)], 
                              [np.sin(rotate_angle),  np.cos(rotate_angle)]])
new = np.dot(rotation_matrix,data.T)
pat_hand = ax.add_patch(Polygon(np.column_stack(([0, 0, lambda1, lambda1], 
                                                 [0, lambda2, lambda2, 0])), 
                    facecolor=fill_color, 
                    edgecolor=black_color, 
                    visible=False))
pat_hand_rot = ax.add_patch(Polygon(new.T, 
                       facecolor=fill_color, 
                       edgecolor=black_color))
pat_hand_rot.set(visible=False)

# 3D box
pat_hand3 = [ax.add_patch(Polygon(np.column_stack(([0, -0.2*lambda1, 0.8*lambda1, lambda1], 
                                      [0, -0.2*lambda2, -0.2*lambda2, 0])), 
                     facecolor=fill_color, 
                     edgecolor=black_color))]
                  
pat_hand3.append(ax.add_patch(Polygon(np.column_stack(([0, -0.2*lambda1, -0.2*lambda1, 0], 
                                          [0, -0.2*lambda2, 0.8*lambda2, lambda2])), 
                         facecolor=fill_color, 
                         edgecolor=black_color)))

pat_hand3.append(ax.add_patch(Polygon(np.column_stack(([-0.2*lambda1, 0, lambda1, 0.8*lambda1], 
                                          [0.8*lambda2, lambda2, lambda2, 0.8*lambda2])), 
                         facecolor=fill_color,
                         edgecolor=black_color)))
pat_hand3.append(ax.add_patch(Polygon(np.column_stack(([lambda1, 0.8*lambda1, 0.8*lambda1, lambda1], 
                                          [lambda2, 0.8*lambda2, -0.2*lambda2, 0])), 
                         facecolor=fill_color, 
                         edgecolor=black_color)))

for hand in pat_hand3:
    hand.set(visible=False)

ax.set_aspect('equal')
ax.set_axis_off()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xspan = xlim[1] - xlim[0]
yspan = ylim[1] - ylim[0]
#ar_one = ax.arrow([0, lambda1], [0, 0])
ar_one = ax.arrow(x=0, y=0, dx=lambda1, dy=0, head_width=0.03)
#ar_two = ax.arrow([0, 0], [0, lambda2])
ar_two = ax.arrow(x=0, y=0, dx=0, dy=lambda2, head_width=0.03)
#ar_three = ax.arrow([0, -0.2*lambda1], [0, -0.2*lambda2])
ar_three = ax.arrow(x=0, y=0, dx=-0.2*lambda1, dy=-0.2*lambda2, head_width=0.03)
ar_one_text = ax.text(0.5*lambda1, -0.05*yspan, 
                      '$\lambda_1$', 
                      horizontalalignment='center',
                     fontsize=14)
ar_two_text = ax.text(-0.05*xspan, 0.5*lambda2, 
                      '$\lambda_2$', 
                      horizontalalignment='center',
                     fontsize=14)
ar_three_text = ax.text(-0.05*xspan-0.1*lambda1, -0.1*lambda2+0.05*yspan, 
                        '$\lambda_3$', 
                        horizontalalignment='center',
                       fontsize=14)
ar_one.set(linewidth=3, 
           visible=False, 
           color=blue_color)
ar_one_text.set(visible=False)

ar_two.set(linewidth=3, 
           visible=False, 
           color=blue_color)
ar_two_text.set(visible=False)

ar_three.set(linewidth=3, 
             visible=False, 
             color=blue_color)
ar_three_text.set(visible=False)


matrix_ax = fig.add_axes([0.2, 0.35, 0.3, 0.3])
matrix_ax.set_aspect('equal')
matrix_ax.set_axis_off()
eigenvals = [['$\lambda_1$', '$0$'],['$0$', '$\lambda_2$']]
plot.matrix(eigenvals, 
            matrix_ax, 
            bracket_style='square', 
            type='entries', 
            bracket_color=black_color)


# First arrow
matrix_ax.cla()
plot.matrix(eigenvals, 
            matrix_ax, 
            bracket_style='square', 
            type='entries',
            highlight=True,
            highlight_row=[0, 0],
            highlight_col=':',
            highlight_color=magenta_color,
            bracket_color=black_color)

ar_one.set(visible=True)
ar_one_text.set(visible=True)

file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams, transparent=True)
counter += 1

# Second arrow
matrix_ax.cla()
plot.matrix(eigenvals, 
            matrix_ax, 
            bracket_style='square', 
            type='entries', 
            highlight=True,
            highlight_row=[1,1],
            highlight_col=':',
            highlight_color=magenta_color,
            bracket_color=black_color)

ar_two.set(visible=True)
ar_two_text.set(visible=True)

file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1

matrix_ax.cla()
plot.matrix(eigenvals, matrix_ax, 
            bracket_style='square', 
            type='entries', 
            bracket_color=black_color)

file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1


tax = fig.add_axes([0.1, 0.1, 0.8, 0.1])
tax.set_axis_off()
tax.set_xlim([0, 1])
tax.set_ylim([0, 1])
det_text = tax.text(0.5, 0.5,
                '$\det{\Lambda} = \lambda_1 \lambda_2$', 
                horizontalalignment='center',
                   fontsize=20)
file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1

pat_hand.set(visible=True)
file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1

det_text_plot = ax.text(0.5*lambda1, 
                              0.5*lambda2, 
                              '$\det{\Lambda}$', 
                              horizontalalignment='center', fontsize=20)
                     
file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1


eigenvals2 = [['$\lambda_1$', '$0$', '$0$'],
              ['$0$', '$\lambda_2$', '$0$'],
              ['$0$', '$0$', '$\lambda_3$']]

matrix_ax.cla()
plot.matrix(eigenvals2, matrix_ax, 
            bracket_style='square', 
            type='entries',
            highlight=True,
            highlight_row=[2,2],
            highlight_col=':',
            highlight_color=magenta_color)

file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1


ar_three.set(visible=True)
ar_three_text.set(visible=True)
for hand in pat_hand3:
    hand.set(visible=True)
det_text.set(text='$\det{\Lambda} = \lambda_1 \lambda_2\lambda_3$', 
             fontsize=20, 
             horizontalalignment='center')

file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1

matrix_ax.cla()
plot.matrix(eigenvals, 
            matrix_ax, 
            bracket_style='square', 
            type='entries', 
            bracket_color=black_color)
            
ar_three.set(visible=False)
ar_three_text.set(visible=False)
for hand in pat_hand3:
    hand.set(visible=False)
det_text.set(text='$\det{\Lambda} = \lambda_1 \lambda_2$')

file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1

det_text.set(text='$\det{\mathbf{R}\Lambda} = \lambda_1 \lambda_2$')
label_eigenvalue.set(label='\Large $\mathbf{R}\Lambda=$')

import matplotlib.transforms as mtransforms

det_text.set(text='$\det{\mathbf{R}\Lambda} = \lambda_1 \lambda_2$')
label_eigenvalue.set(text='$\mathbf{R}\Lambda=$')

trans_data =  mtransforms.Affine2D().rotate_deg(rotate_angle*180/np.pi) + ax.transData

ar_one.set_transform(trans_data)
ar_one_text.set_transform(trans_data)
ar_two.set_transform(trans_data)
ar_two_text.set_transform(trans_data)
det_text_plot.set_transform(trans_data)
pat_hand_rot.set(visible=True)
pat_hand.set(visible=False)

pat_hand_rot.set(visible=True)
pat_hand.set(visible=False)

W = [['$w_{1, 1}$', '$w_{1, 2}$'],[ '$w_{2, 1}$', '$w_{2, 2}$']]
plot.matrix(W, 
            matrix_ax, 
            bracket_style='square', 
            type='entries', 
            bracket_color=black_color)


file_name = 'gp-optimise-determinant{counter:0>3}.svg'.format(counter=counter)
mlai.write_figure(file_name, directory=diagrams)
counter += 1}

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
