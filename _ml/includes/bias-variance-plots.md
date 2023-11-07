\ifndef{biasVariancePlots}
\define{biasVariancePlots}

\editme

\notes{\subsection{Bias vs Variance Error Plots}}

\notes{Helper function for sampling data from two different classes.}

\setupcode{import numpy as np}

\helpercode{def create_data(per_cluster=30):
    """Create a randomly sampled data set
    
    :param per_cluster: number of points in each cluster
    """
    X = []
    y = []
    scale = 3
    prec = 1/(scale*scale)
    pos_mean = [[-1, 0],[0,0.5],[1,0]]
    pos_cov = [[prec, 0.], [0., prec]]
    neg_mean = [[0, -0.5],[0,-0.5],[0,-0.5]]
    neg_cov = [[prec, 0.], [0., prec]]
    for mean in pos_mean:
        X.append(np.random.multivariate_normal(mean=mean, cov=pos_cov, size=per_class))
        y.append(np.ones((per_class, 1)))
    for mean in neg_mean:
        X.append(np.random.multivariate_normal(mean=mean, cov=neg_cov, size=per_class))
        y.append(np.zeros((per_class, 1)))
    return np.vstack(X), np.vstack(y).flatten()}
		
\notes{Helper function for plotting the decision boundary of the SVM.}

\helpercode{def plot_contours(ax, cl, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    :param ax: matplotlib axes object
    :param cl: a classifier
    :param xx: meshgrid ndarray
    :param yy: meshgrid ndarray
    :param params: dictionary of params to pass to contourf, optional
    """
    Z = cl.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
	# Plot decision boundary and regions
    out = ax.contour(xx, yy, Z, 
	                 levels=[-1., 0., 1], 
	                 colors='black', 
	                 linestyles=['dashed', 'solid', 'dashed'])
	out = ax.contourf(xx, yy, Z, 
                     levels=[Z.min(), 0, Z.max()], 
                     colors=[[0.5, 1.0, 0.5], [1.0, 0.5, 0.5]])
    return out}

\downloadcode{mlai}


\setuphelpercode{import mlai
import os}
\helpercode{def decision_boundary_plot(models, X, y, axs, filename, directory, titles, xlim, ylim):
    """Plot a decision boundary on the given axes
    
    :param axs: the axes to plot on.
    :param models: the SVM models to plot
    :param titles: the titles for each axis
    :param X: input training data
    :param y: target training data"""
    for ax in axs.flatten():
        ax.clear()
    X0, X1 = X[:, 0], X[:, 1]
    if xlim is None:
        xlim = [X0.min()-1, X0.max()+1]
    if ylim is None:
        ylim = [X1.min()-1, X1.max()+1]
    xx, yy = np.meshgrid(np.arange(xlim[0], xlim[1], 0.02),
                         np.arange(ylim[0], ylim[1], 0.02))
    for cl, title, ax in zip(models, titles, axs.flatten()):
        plot_contours(ax, cl, xx, yy,
                      cmap=plt.cm.coolwarm, alpha=0.8)
        ax.plot(X0[y==1], X1[y==1], 'r.', markersize=10)
        ax.plot(X0[y==0], X1[y==0], 'g.', markersize=10)
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
        mlai.write_figure(filename,
                          directory=directory,
                          figure=fig,
                          transparent=True)
    return xlim, ylim}


\setupcode{import matplotlib
font = {'family' : 'sans',
        'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)
import matplotlib.pyplot as plt}


\setupcode{from sklearn import svm}

\code{# Create an instance of SVM and fit the data. 
C = 100.0  # SVM regularization parameter
gammas = [0.001, 0.01, 0.1, 1]


per_class=30
num_samps = 20
# Set-up 2x2 grid for plotting.
fig, ax = plt.subplots(1, 4, figsize=(10,3))
xlim=None
ylim=None
for samp in range(num_samps):
    X, y=create_data(per_class)
    models = []
    titles = []
    for gamma in gammas:
        models.append(svm.SVC(kernel='rbf', gamma=gamma, C=C))
        titles.append('$\gamma={}$'.format(gamma))
    models = (cl.fit(X, y) for cl in models)
    xlim, ylim = decision_boundary_plot(models, X, y, 
                           axs=ax, 
                           filename='bias-variance{samp:0>3}.svg'.format(samp=samp), 
						   directory='\writeDiagramsDir/ml'
                           titles=titles,
                          xlim=xlim,
                          ylim=ylim)}

\include{_data-science/includes/pods-install.md}


\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('bias-variance{samp:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
						    samp=IntSlider(0,0,10,1))}
							
\newslide{}


<!--\slides{
\define{width}{80%} 
\define{animationName}{bias-variance-plots}
\startanimation{\animationName}{0}{10} 
\newframe{\includepng{\diagramsDir/ml/bias-variance000}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance001}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance002}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance003}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance004}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance005}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance006}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance007}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance008}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance009}{\width}}{\animationName}
\newframe{\includepng{\diagramsDir/ml/bias-variance010}{\width}}{\animationName}

\endanimation
\caption{simple models on left complex models on right}
}-->

\slides{
\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance000}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance001}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance002}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance003}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance004}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance005}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance006}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance007}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance008}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance009}{\width}}{}{bias-variance}

\newslide{}

\figure{\includepng{\diagramsDir/ml/bias-variance010}{\width}}{}{bias-variance}
}

\notes{\figure{\includepng{\diagramsDir/ml/bias-variance000}{80%}\includepng{\diagramsDir/ml/bias-variance010}{80%}}{In each figure the simpler model is on the left, and the more complex model is on the right. Each fit is done to a different version of the data set. The simpler model is more consistent in its errors (bias error), whereas the more complex model is varying in its errors (variance error).}{bias-variance-errors}}

\endif
