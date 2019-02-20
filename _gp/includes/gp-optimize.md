\ifndef{gpOptimize}
\define{gpOptimize}
\editme

\plotcode{gpoptimizeInit}

\newslide{Learning Covariance Parameters}

Can we determine covariance parameters from the data?

\newslide{}

$$\gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\det{\kernelMatrix}^{\frac{1}{2}}}}{\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}$$

\newslide{}

$$\begin{aligned}
    \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\color{\blueColor} \det{\kernelMatrix}^{\frac{1}{2}}}}{\color{\redColor}\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}
\end{aligned}
$$ 

\newslide{}

$$
\begin{aligned}
    \log \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=&{\color{\blueColor}-\frac{1}{2}\log\det{\kernelMatrix}}{\color{\redColor}-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}} \\ &-\frac{\numData}{2}\log2\pi
\end{aligned}
$$ 

$$
\errorFunction(\parameterVector) = {\color{\blueColor} \frac{1}{2}\log\det{\kernelMatrix}} + {\color{\redColor} \frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}
$$

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

\newslide{$$\errorFunction(\parameterVector) = {\color{\blueColor}\frac{1}{2}\log\det{\kernelMatrix}}+{\color{\redColor}\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$}

\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import os}

\setupplotcode{import GPy
import teaching_plots as plot
import mlai
import gp_tutorial}

\plotcode{np.random.seed(125)
diagrams = '../slides/diagrams/gp'

black_color=[0., 0., 0.]
red_color=[1., 0., 0.]
blue_color=[0., 0., 1.]
magenta_color=[1., 0., 1.]
fontsize=18}

\plotcode{y_lim = [-2.2, 2.2]
y_ticks = [-2, -1, 0, 1, 2]
x_lim = [-2, 2]
x_ticks = [-2, -1, 0, 1, 2]
err_y_lim = [-12, 20]

linewidth=3
markersize=15
markertype='.'}

\plotcode{x = np.linspace(-1, 1, 6)[:, np.newaxis]
xtest = np.linspace(x_lim[0], x_lim[1], 200)[:, np.newaxis]

# True data
true_kern = GPy.kern.RBF(1) + GPy.kern.White(1)
true_kern.rbf.lengthscale = 1.0
true_kern.white.variance = 0.01
K = true_kern.K(x) 
y = np.random.multivariate_normal(np.zeros((6,)), K, 1).T}

\plotcode{
# Fitted model
kern = GPy.kern.RBF(1) + GPy.kern.White(1)
kern.rbf.lengthscale = 1.0
kern.white.variance = 0.01

lengthscales = np.asarray([0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 4, 8, 16, 100])

fig1, ax1 = plt.subplots(figsize=plot.one_figsize)    
fig2, ax2 = plt.subplots(figsize=plot.one_figsize)    
line = ax2.semilogx(np.NaN, np.NaN, 'x-', 
                    color=black_color)
ax.set_ylim(err_y_lim)
ax.set_xlim([0.025, 32])
ax.grid(True)
ax.set_xticks([0.01, 0.1, 1, 10, 100])
ax.set_xticklabels(['$10^{-2}$', '$10^{-1}$', '$10^0$', '$10^1$', '$10^2$'])


err = np.zeros_like(lengthscales)
err_log_det = np.zeros_like(lengthscales)
err_fit = np.zeros_like(lengthscales)

counter = 0
for i, ls in enumerate(lengthscales):
        kern.rbf.lengthscale=ls
        K = kern.K(x) 
        invK, L, Li, log_det_K = GPy.util.linalg.pdinv(K)
        err[i] = 0.5*(log_det_K + np.dot(np.dot(y.T,invK),y))
        err_log_det[i] = 0.5*log_det_K
        err_fit[i] = 0.5*np.dot(np.dot(y.T,invK), y)
        Kx = kern.K(x, xtest)
        ypred_mean = np.dot(np.dot(Kx.T, invK), y)
        ypred_var = kern.Kdiag(xtest) - np.sum((np.dot(Kx.T,invK))*Kx.T, 1)
        ypred_sd = np.sqrt(ypred_var)
        ax1.clear()
        _ = gp_tutorial.gpplot(xtest.flatten(),
                               ypred_mean.flatten(),
                               ypred_mean.flatten()-2*ypred_sd.flatten(),
                               ypred_mean.flatten()+2*ypred_sd.flatten(), 
                               ax=ax1)
        x_lim = ax1.get_xlim()
        ax1.set_ylabel('$f(x)$', fontsize=fontsize)
        ax1.set_xlabel('$x$', fontsize=fontsize)

        p = ax1.plot(x, y, markertype, color=black_color, markersize=markersize, linewidth=linewidth)
        ax1.set_ylim(y_lim)
        ax1.set_xlim(x_lim)                                    
        ax1.set_xticks(x_ticks)
        #ax.set(box=False)
           
        ax1.plot([x_lim[0], x_lim[0]], y_lim, color=black_color)
        ax1.plot(x_lim, [y_lim[0], y_lim[0]], color=black_color)

        file_name = 'gp-optimise{counter:0>3}.svg'.format(counter=counter)
        mlai.write_figure(os.path.join(diagrams, file_name),
                          figure=fig1,
                          transparent=True)
        counter += 1

        ax2.clear()
        t = ax2.semilogx(lengthscales[0:i+1], err[0:i+1], 'x-', 
                        color=magenta_color, 
                        markersize=markersize,
                        linewidth=linewidth)
        t2 = ax2.semilogx(lengthscales[0:i+1], err_log_det[0:i+1], 'x-', 
                         color=blue_color, 
                        markersize=markersize,
                        linewidth=linewidth)
        t3 = ax2.semilogx(lengthscales[0:i+1], err_fit[0:i+1], 'x-', 
                         color=red_color, 
                        markersize=markersize,
                        linewidth=linewidth)
        ax2.set_ylim(err_y_lim)
        ax2.set_xlim([0.025, 32])
        ax2.set_xticks([0.01, 0.1, 1, 10, 100])
        ax2.set_xticklabels(['$10^{-2}$', '$10^{-1}$', '$10^0$', '$10^1$', '$10^2$'])

        ax2.grid(True)

        ax2.set_ylabel('negative log likelihood', fontsize=fontsize)
        ax2.set_xlabel('length scale, $\ell$', fontsize=fontsize)
        file_name = 'gp-optimise{counter:0>3}.svg'.format(counter=counter)
        mlai.write_figure(os.path.join(diagrams, file_name),
                          figure=fig2,
                          transparent=True)
        counter += 1
        #ax.set_box(False)
        xlim = ax2.get_xlim()
        ax2.plot([xlim[0], xlim[0]], err_y_lim, color=black_color)
        ax2.plot(xlim, [err_y_lim[0], err_y_lim[0]], color=black_color)}

\slides{
\startanimation{gp-optimise}{0}{10}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise000}}{\includediagram{../slides/diagrams/gp/gp-optimise001}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise002}}{\includediagram{../slides/diagrams/gp/gp-optimise003}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise004}}{\includediagram{../slides/diagrams/gp/gp-optimise005}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise006}}{\includediagram{../slides/diagrams/gp/gp-optimise007}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise008}}{\includediagram{../slides/diagrams/gp/gp-optimise009}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise010}}{\includediagram{../slides/diagrams/gp/gp-optimise011}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise012}}{\includediagram{../slides/diagrams/gp/gp-optimise013}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise014}}{\includediagram{../slides/diagrams/gp/gp-optimise015}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise016}}{\includediagram{../slides/diagrams/gp/gp-optimise017}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise018}}{\includediagram{../slides/diagrams/gp/gp-optimise019}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{../slides/diagrams/gp/gp-optimise020}}{\includediagram{../slides/diagrams/gp/gp-optimise021}}{50%}{50%}}{gp-optimise}
\endanimation
}

\notesfigure{\columns{\includediagram{../slides/diagrams/gp/gp-optimise006}}{\includediagram{../slides/diagrams/gp/gp-optimise010}}{50%}{50%}
\columns{\includediagram{../slides/diagrams/gp/gp-optimise016}}{\includediagram{../slides/diagrams/gp/gp-optimise021}}{50%}{50%}}
\notes{\caption{Variation in the data fit term, the capacity term and the negative log likelihood for different lengthscales.}}



\endif
