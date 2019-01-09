\define{\blueColor}{yellow}
\define{\redColor}{cyan}
\define{\magentaColor}{green}


\code{gpoptimizeInit}

\newslide{Learning Covariance Parameters}

Can we determine covariance parameters from the data?

\newslide{}

$$\gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\det{\kernelMatrix}^{\frac{1}{2}}}}{\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}$$

\newslide{}

$$\begin{aligned}
    \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\color{\blueColor} \det{\kernelMatrix}^{\frac{1}{2}}}}{\color{\redColor}\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}
    \end{aligned}$$ 

\newslide{}

$$\begin{aligned}
    \log \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=&{\color{\blueColor}-\frac{1}{2}\log\det{\kernelMatrix}}{\color{\redColor}-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}} \\ &-\frac{\numData}{2}\log2\pi
    \end{aligned}$$ \onslide<4>
$$\errorFunction(\parameterVector) = {\color{\blueColor} \frac{1}{2}\log\det{\kernelMatrix}} + {\color{\redColor} \frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$

\newslide{}

The parameters are *inside* the covariance function (matrix).
\normalsize
$$\kernelScalar_{i, j} = \kernelScalar(\inputVals_i, \inputVals_j; \parameterVector)$$


\newslide{Eigendecomposition of Covariance}

[\Large
$$\kernelMatrix = \rotationMatrix \eigenvalueMatrix^2 \rotationMatrix^\top$$]{}

\code{gpoptimizePlot1}

\columns{\includepng{../slides/diagrams/gp/gp-optimize-eigen}{100%}{negate}}{$\eigenvalueMatrix$ represents distance on axes.
$\rotationMatrix$ gives rotation.}{50%}{50%}


\newslide{Eigendecomposition of Covariance}

* $\eigenvalueMatrix$ is *diagonal*, $\rotationMatrix^\top\rotationMatrix = \eye$. 
* Useful representation since $\det{\kernelMatrix} = \det{\eigenvalueMatrix^2} = \det{\eigenvalueMatrix}^2$.

\newslide{Capacity control: ${\color{\blueColor} \log \det{\kernelMatrix}}$}

\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
fill_color = [1., 1., 0.]
black_color = [0., 0., 0.]
blue_color = [0., 0., 1.]
magenta_color = [1., 0., 1.]}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.set_axis_off()
cax = fig.add_axes([0., 0., 1., 1.])
cax.set_axis_off()

counter = 1
lambda1 = 0.5
lambda2 = 0.3

cax.set_xlim([0., 1.])
cax.set_ylim([0., 1.])

# Matrix label axes
tax2 = fig.add_axes([0, 0.47, 0.1, 0.1])
tax2.set_xlim([0, 1.])
tax2.set_ylim([0, 1.])
tax2.set_axis_off()
label_eigenvalue = tax2.text(0.5, 0.5, "\Large $\eigenvalueMatrix=$")

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
rotation_matrix = np.asarray([[np.sqrt(2)/2, -np.sqrt(2)/2], 
                              [np.sqrt(2)/2,  np.sqrt(2)/2]])
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
ar_one = ax.arrow(x=0, y=0, dx=lambda1, dy=0)
#ar_two = ax.arrow([0, 0], [0, lambda2])
ar_two = ax.arrow(x=0, y=0, dx=0, dy=lambda2)
#ar_three = ax.arrow([0, -0.2*lambda1], [0, -0.2*lambda2])
ar_three = ax.arrow(x=0, y=0, dx=-0.2*lambda1, dy=-0.2*lambda2)
ar_one_text = ax.text(0.5*lambda1, -0.05*yspan, 
                      '$\eigenvalue_1$', 
                      horizontalalignment='center')
ar_two_text = ax.text(-0.05*xspan, 0.5*lambda2, 
                      '$\eigenvalue_2$', 
				      horizontalalignment='center')
ar_three_text = ax.text(-0.05*xspan-0.1*lambda1, -0.1*lambda2+0.05*yspan, 
                        '$\eigenvalue_3$', 
					    horizontalalignment='center')
ar_one.set(linewidth=3, visible=False, color=blue_color)
ar_one_text.set(visible=False)

ar_two.set(linewidth=3, visible=False, color=blue_color)
ar_two_text.set(visible=False)

ar_three.set(linewidth=3, visible=False, color=blue_color)
ar_three_text.set(visible=False)


matrix_ax = fig.add_axes([0.2, 0.35, 0.3, 0.3])
matrix_ax.set_aspect('equal')
matrix_ax.set_axis_off()
eigenvals = [['$\eigenvalue_1$', '$0$'],['$0$', '$\eigenvalue_2$']]
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

file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
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

file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1

matrix_ax.cla()
plot.matrix(eigenvals, matrix_ax, 
            bracket_style='square', 
			type='entries', 
            bracket_color=black_color)

file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1


tax = fig.add_axes([0.1, 0.1, 0.8, 0.1])
tax.set_axis_off()
tax.set_xlim([0, 1])
tax.set_ylim([0, 1])
det_text = text(0.5, 0.5,
                '\Large $\det{\eigenvalueMatrix} = \eigenvalue_1 \eigenvalue_2$', 
				horizontalalignment='center')
file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1

axes(ax)
pat_hand.set(visible=True)
file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1

det_text_plot = text(0.5*lambda1, 
                     0.5*lambda2, 
					 '\Large $\det{\eigenvalueMatrix}$', 
					 horizontalalignment='center')
					 
file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1


eigenvals2 = {'$\eigenvalue_1$', '$0$' '$0$'; '$0$', '$\eigenvalue_2$' '$0$'; '$0$', '$0$' '$\eigenvalue_3$'}
axes(matrix_ax)
matrix_ax.cla()
plot.matrix(eigenvals2, matrix_ax, 
            bracket_style='square', 
            type='entries',
			highlight=True,
			highlight_row=[2,2],
			highlight_col=':',
			highlight_color=magenta_color)

file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1


ar_three.set(visible=True)
ar_three_text.set(visible=True)
pat_hand3.set(visible=True)
det_text.set(string='\Large $\det{\eigenvalueMatrix} = \eigenvalue_1 \eigenvalue_2\eigenvalue_3$')

file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1

matrix_ax.cla()
plot.matrix(eigenvals, 
            matrix_ax, 
			bracket_style='square', 
			type='entries', 
			bracket_color=black_color)
			
ar_three.set(visible=False)
ar_three_text.set(visible=False)
pat_hand3.set(visible=False)
det_text.set(string='\Large $\det{\eigenvalueMatrix} = \eigenvalue_1 \eigenvalue_2$')

file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1



det_text.set(string='\Large $\det{\rotationMatrix\eigenvalueMatrix} = \eigenvalue_1 \eigenvalue_2$')
label_eigenvalue.set(string='\Large $\rotationMatrix\eigenvalueMatrix=$')



rotate_object(rotation_matrix, ar_one)
rotate_object(rotation_matrix, ar_one_text)
rotate_object(rotation_matrix, ar_two)
rotate_object(rotation_matrix, ar_two_text)
rotate_object(rotation_matrix, det_textPlot)
pat_hand_rot.set(visible=True)
pat_hand.set(visible=False)

W = [['$\mappingScalar_{1, 1}$', '$\mappingScalar_{1, 2}$'],[ '$\mappingScalar_{2, 1}$', '$\mappingScalar_{2, 2}$']]
plot.matrix(W, 
            matrix_ax, 
			bracket_style='square', 
			type='entries', 
			bracket_color=black_color)


file_name = 'gp-optimise-determinant{counter:>3}'.format(counter=counter)
mlai.write_figure(os.path.join(diagrams, file_name), transparent=True)
counter += 1
}

<!--
\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant3}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant4}}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant5}}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant6}}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant7}}\only<8>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant8}}\only<9>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant9}}\only<10>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant10}}-->

\newslide{Data Fit: ${\color{\redColor} \frac{\dataVector^\top\kernelMatrix^{-1}\dataVector}{2}}$}

<!--\code{gpoptimizePlot3}

\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic3}}-->

\newslide{Learning Covariance Parameters}

\slides{
\startanimation{gp-optimise}{0}{10}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise000.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise001.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise002.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise003.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise004.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise005.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise006.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise007.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise008.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise009.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise010.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise011.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise012.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise013.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise014.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise015.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise016.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise017.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise018.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise019.svg}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includesvg{../slides/diagrams/gp/gp-optimise020.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise021.svg}}{50%}{50%}}{gp-optimise}
\endanimation
}
\notesfigure{\columns{\includesvg{../slides/diagrams/gp/gp-optimise006.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise010.svg}}{50%}{50%}
\columns{\includesvg{../slides/diagrams/gp/gp-optimise016.svg}}{\includesvg{../slides/diagrams/gp/gp-optimise021.svg}}{50%}{50%}}
\notes{\caption{Variation in the data fit term, the capacity term and the negative log likelihood for different lengthscales.}


$$\errorFunction(\parameterVector) = {\color{\blueColor}\frac{1}{2}\log\det{\kernelMatrix}}+{\color{\redColor}\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$

