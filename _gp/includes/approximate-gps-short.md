
### Approximations {data-transition="None"}

\includeimg{../slides/diagrams/sparse-gps-1.png}{90%}

*Image credit: Kai Arulkumaran*

### Approximations {data-transition="None"}

\includeimg{../slides/diagrams/sparse-gps-2.png}{90%}

*Image credit: Kai Arulkumaran*

### Approximations {data-transition="None"}

\includeimg{../slides/diagrams/sparse-gps-3.png}{45%}

*Image credit: Kai Arulkumaran*

### Approximations {data-transition="None"}

\includeimg{../slides/diagrams/sparse-gps-4.png}{45%}

*Image credit: Kai Arulkumaran*

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import GPy

import mlai
import teaching_plots as plot 
from gp_tutorial import gpplot}

\setupcode{np.random.seed(101)}

\notes{
### A Simple Regression Problem

Here we set up a simple one dimensional regression problem. The input locations, $\inputMatrix$, are in two separate clusters. The response variable, $\dataVector$, is sampled from a Gaussian process with an exponentiated quadratic covariance.}

\helpercode{def plot_model_output(model, output_dim=0, ax=None, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=None, ylim=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=plot.big_figsize)
    ax.plot(model.X.flatten(), model.Y[:, output_dim], 'r.',markersize=10)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    xt = plot.pred_range(model.X, portion=portion)
    yt_mean, yt_var = model.predict(xt)
    yt_sd=np.sqrt(yt_var)
    if yt_sd.shape[1]>1:
        yt_sd = yt_sd[:, output_dim]

    _ = gpplot(xt.flatten(),
               yt_mean[:, output_dim],
               yt_mean[:, output_dim]-2*yt_sd.flatten(),
               yt_mean[:, output_dim]+2*yt_sd.flatten(), 
               ax=ax)
			   
    if xlim is not None:
        ax.set_xlim(xlim)
	else:
		ax.set_xlim([xt.min(), xt.max()])
    if ylim is not None: 
        ax.set_ylim(ylim)
			   
	if hasattr(model, 'Z'):
		ylim = ax.get_ylim()
		ax.plot(m.Z, np.ones(m.Z.shape)*ax.get_ylim()[0], marker='^', linestyle=None, markersize=20)}
		
\code{N = 50
noise_var = 0.01
X = np.zeros((50, 1))
X[:25, :] = np.linspace(0,3,25)[:,None] # First cluster of inputs/covariates
X[25:, :] = np.linspace(7,10,25)[:,None] # Second cluster of inputs/covariates

# Sample response variables from a Gaussian process with exponentiated quadratic covariance.
k = GPy.kern.RBF(1)
y = np.random.multivariate_normal(np.zeros(N),k.K(X)+np.eye(N)*np.sqrt(noise_var)).reshape(-1,1)}

\notes{First we perform a full Gaussian process regression on the data. We create a GP model, `m_full`, and fit it to the data, plotting the resulting fit.}

\code{m_full = GPy.models.GPRegression(X,y)
_ = m_full.optimize(messages=True) # Optimize parameters of covariance function}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-full-gp.svg', 
                  transparent=True, frameon=True)}

### Full Gaussian Process Fit {data-transition="None"}

\includesvg{../slides/diagrams/gp/sparse-demo-full-gp.svg}


\notes{Now we set up the inducing variables, $\mathbf{u}$. Each inducing variable has its own associated input index, $\mathbf{Z}$, which lives in the same space as $\inputMatrix$. Here we are using the true covariance function parameters to generate the fit.}

\code{kern = GPy.kern.RBF(1)
Z = np.hstack(
        (np.linspace(2.5,4.,3),
        np.linspace(7,8.5,3)))[:,None]
m = GPy.models.SparseGPRegression(X,y,kernel=kern,Z=Z)
m.noise_var = noise_var
m.inducing_inputs.constrain_fixed()
display(m)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-constrained-inducing-6-unlearned-gp.svg', 
                  transparent=True, frameon=True)}

### Inducing Variable Fit {data-transition="None"}

\includesvg{../slides/diagrams/gp/sparse-demo-constrained-inducing-6-unlearned-gp.svg}

\code{_ = m.optimize(messages=True)
display(m)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-constrained-inducing-6-learned-gp.svg', 
                  transparent=True, frameon=True)}

### Inducing Variable Param Optimize {data-transition="None"}

\includesvg{../slides/diagrams/gp/sparse-demo-constrained-inducing-6-learned-gp.svg}

\code{m.randomize()
m.inducing_inputs.unconstrain()
_ = m.optimize(messages=True)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2,xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-unconstrained-inducing-6-gp.svg', 
                  transparent=True, frameon=True)}

### Inducing Variable Full Optimize {data-transition="None"}

\includesvg{../slides/diagrams/gp/sparse-demo-unconstrained-inducing-6-gp.svg}


\notes{Now we will vary the number of inducing points used to form the approximation.}

\code{m.num_inducing=8
m.randomize()
M = 8
m.set_Z(np.random.rand(M,1)*12)

_ = m.optimize(messages=True)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-sparse-inducing-8-gp.svg', 
                  transparent=True, frameon=True)}

### Full Gaussian Process Fit {data-transition="None"}

\includesvg{../slides/diagrams/gp/sparse-demo-sparse-inducing-8-gp.svg}

\notes{And we can compare the probability of the result to the full model.}
\code{print(m.log_likelihood(), m_full.log_likelihood())}



