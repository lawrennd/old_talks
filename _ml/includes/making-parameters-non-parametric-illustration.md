\ifndef{makingParametersNonParametricIllustration}
\define{makingParametersNonParametricIllustration}

\editme

\subsubsection{Modelling $\mappingFunctionVector$}

\notes{In conclusion, for a non parametric framework, our model for
$\mappingFunctionVector$ is predominantly in the covariance function
$\kernelMatrix_{\mappingFunctionVector\mappingFunctionVector}$. This is
our data model. We are assuming the inducing variables are drawn from a
joint Gaussian process with $\mappingFunctionVector$. The cross
covariance between $\inducingVector$ and $\mappingFunctionVector$ is
given by $\kernelMatrix_{\mappingFunctionVector\inducingVector}$. This
gives the relationship between the function and the inducing variables.
There are a range of ways in which the inducing variables can interelate
with the}


\subsubsection{Illustrative Example}

\notes{For this illustrative example, we'll consider a simple regression
problem. The example is based on one that James Hensman showed at the
January 2014 Gaussian process winter school in his talk is on low rank
Gaussian process approximations.}


\subsection{Back to a Simple Regression Problem}

\notes{Here we set up a simple one dimensional regression problem. The input
locations, $\inputMatrix$, are in two separate clusters. The response
variable, $\dataVector$, is sampled from a Gaussian process with an
exponentiated quadratic covariance.}

\setupcode{import numpy as np
import GPy
from scipy import optimize
np.random.seed(101)}

\code{N = 50
noise_var = 0.01
X = np.zeros((50, 1))
X[:25, :] = np.linspace(0,3,25)[:,None] # First cluster of inputs/covariates
X[25:, :] = np.linspace(7,10,25)[:,None] # Second cluster of inputs/covariates

xlim = (-2,12)
ylim = (-4, 0)

# Sample response variables from a Gaussian process with exponentiated quadratic covariance.
k = GPy.kern.RBF(1)
y = np.random.multivariate_normal(np.zeros(N),k.K(X)+np.eye(N)*np.sqrt(noise_var)).reshape(-1,1)
scale = np.sqrt(np.var(y))
offset = np.mean(y)}

\notes{First we perform a full Gaussian process regression on the data. We
create a GP model, `m_full`, and fit it to the data, plotting the
resulting fit.}

\setuphelpercode{import matplotlib.pyplot as plt
from gp_tutorial import ax_default, meanplot, gpplot}

\helpercode{def plot_model_output(model, output_dim=0, scale=1.0, offset=0.0, ax=None, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2):
    if ax is None:
        fig, ax = plt.subplots(figsize=plot.big_figsize)
    ax.plot(model.X.flatten(), model.Y[:, output_dim]*scale + offset, 'r.',markersize=10)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    xt = plot.pred_range(model.X, portion=portion)
    yt_mean, yt_var = model.predict(xt)
    yt_mean = yt_mean*scale + offset
    yt_var *= scale*scale
    yt_sd=np.sqrt(yt_var)
    if yt_sd.shape[1]>1:
        yt_sd = yt_sd[:, output_dim]

    _ = gpplot(xt.flatten(),
               yt_mean[:, output_dim],
               yt_mean[:, output_dim]-2*yt_sd.flatten(),
               yt_mean[:, output_dim]+2*yt_sd.flatten(), 
               ax=ax)}



\code{m_full = GPy.models.GPRegression(X,y)
m_full.optimize() # Optimize parameters of covariance function}

\setupplotcode{import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='$x', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-full-gp.svg', 
                  transparent=True, frameon=True)}
				  
\figure{\includediagram{\diagramsDir/gp/sparse-demo-full-gp}{60%}}{A full Gaussian process fit to the simulated data set.}{sparse-demo-full-gp}

\notes{Now we set up the inducing variables, $\inducingVector$. Each inducing
variable has its own associated input index, $\mathbf{Z}$, which lives
in the same space as $\inputMatrix$. Here we are using the true
covariance function parameters to generate the fit.}

\code{kern = GPy.kern.RBF(1)
Z = np.hstack(
        (np.linspace(2.5,4.,3),
        np.linspace(7,8.5,3)))[:,None]
m = GPy.models.SparseGPRegression(X,y,kernel=kern,Z=Z)
m.noise_var = noise_var
m.inducing_inputs.constrain_fixed()
#m.tie_params('.*variance')
#m.ensure_default_constraints()}

\displaycode{print(m) # why is it not printing noise variance correctly?}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='$x', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-constrained-inducing-6-unlearned-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-constrained-inducing-6-unlearned-gp}{60%}}{Sparse Gaussian process with six constrained inducing variables and parameters learned.}{sparse-demo-constrained-inducing-6-unlearned-gp}

\code{m.optimize()}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-constrained-inducing-6-learned-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-constrained-inducing-6-learned-gp}{60%}}{Sparse Gaussian process with six constrained inducing variables and parameters learned.}{sparse-demo-constrained-inducing-6-learned-gp}

\displaycode{print(m)}



\code{m.randomize()
m.inducing_inputs.unconstrain()
m.optimize()}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-unconstrained-inducing-6-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-unconstrained-inducing-6-gp}{60%}}{Sparse Gaussian process with six unconstrained inducing variables, initialized randomly and then optimized.}{sparse-demo-unconstrained-inducing-6-gp}

\notes{Now we will vary the number of inducing points used to form the approximation.}

\displaycode{m.Z.values}

\code{m.num_inducing=8
m.randomize()
M = 8

m.set_Z(np.random.rand(M,1)*12)

m.optimize()}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-sparse-inducing-8-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-sparse-inducing-8-gp}{60%}}{Sparse Gaussian process with eight inducing variables, initialized randomly and then optimized.}{sparse-demo-sparse-inducing-8-gp}

\displaycode{print(m.log_likelihood(), m_full.log_likelihood())}

\endif
