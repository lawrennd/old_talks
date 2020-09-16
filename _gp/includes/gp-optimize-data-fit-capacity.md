\ifndef{gpOptimizeDataFitCapacity}
\define{gpOptimizeDataFitCapacity}

\editme

\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import os}

\setupplotcode{import GPy
import teaching_plots as plot
import mlai
import gp_tutorial}

\plotcode{np.random.seed(125)
diagrams = '\writeDiagramsDir/gp'

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
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise000}}{\includediagram{\diagramsDir/gp/gp-optimise001}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise002}}{\includediagram{\diagramsDir/gp/gp-optimise003}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise004}}{\includediagram{\diagramsDir/gp/gp-optimise005}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise006}}{\includediagram{\diagramsDir/gp/gp-optimise007}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise008}}{\includediagram{\diagramsDir/gp/gp-optimise009}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise010}}{\includediagram{\diagramsDir/gp/gp-optimise011}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise012}}{\includediagram{\diagramsDir/gp/gp-optimise013}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise014}}{\includediagram{\diagramsDir/gp/gp-optimise015}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise016}}{\includediagram{\diagramsDir/gp/gp-optimise017}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise018}}{\includediagram{\diagramsDir/gp/gp-optimise019}}{50%}{50%}}{gp-optimise}
\newframe{\columns{\includediagram{\diagramsDir/gp/gp-optimise020}}{\includediagram{\diagramsDir/gp/gp-optimise021}}{50%}{50%}}{gp-optimise}
\endanimation
}

\notes{\figure{\columns{\includediagram{\diagramsDir/gp/gp-optimise006}{100%}}{\includediagram{\diagramsDir/gp/gp-optimise010}{100%}}{50%}{50%}
\columns{\includediagram{\diagramsDir/gp/gp-optimise016}{100%}}{\includediagram{\diagramsDir/gp/gp-optimise021}{100%}}{50%}{50%}}{Variation in the data fit term, the capacity term and the negative log likelihood for different lengthscales.}{gp-optimise}}

\endif
