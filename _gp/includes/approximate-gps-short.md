\slides{
### Approximations

\includeimg{../slides/diagrams/sparse-gps-1.png}{90%}{}{center}
\caption{Image credit: Kai Arulkumaran}

### Approximations

\includeimg{../slides/diagrams/sparse-gps-2.png}{90%}{}{center}
\caption{Image credit: Kai Arulkumaran}

### Approximations

\includeimg{../slides/diagrams/sparse-gps-3.png}{45%}{}{center}
\caption{Image credit: Kai Arulkumaran}

### Approximations

\includeimg{../slides/diagrams/sparse-gps-4.png}{45%}{}{center}
\caption{Image credit: Kai Arulkumaran}
}

\notesfigure{\includeimg{../slides/diagrams/sparse-gps.jpg}{45%}{}{center}}
\notes{\caption{Image credit: Kai Arulkumaran}}

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
plot.model_output(m_full, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
xlim = ax.get_xlim()
ylim = ax.get_ylim()
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-full-gp.svg', 
                  transparent=True, frameon=True)}

\newslide{Full Gaussian Process Fit}

\includesvg{../slides/diagrams/gp/sparse-demo-full-gp.svg}
\notes{\caption{Full Gaussian process fitted to the data set.}}

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
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-constrained-inducing-6-unlearned-gp.svg', 
                  transparent=True, frameon=True)}

\newslide{Inducing Variable Fit}

\includesvg{../slides/diagrams/gp/sparse-demo-constrained-inducing-6-unlearned-gp.svg}
\notes{\caption{Sparse Gaussian process fitted with six inducing variables, no optimization of parameters or inducing variables.}}

\code{_ = m.optimize(messages=True)
display(m)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-full-gp.svg', 
                  transparent=True, frameon=True)}

\newslide{Inducing Variable Param Optimize}

\includesvg{../slides/diagrams/gp/sparse-demo-constrained-inducing-6-learned-gp.svg}
\notes{\caption{Gaussian process fitted with inducing variables fixed and parameters optimized}}

\code{m.randomize()
m.inducing_inputs.unconstrain()
_ = m.optimize(messages=True)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2,xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-unconstrained-inducing-6-gp.svg', 
                  transparent=True, frameon=True)}

\newslide{Inducing Variable Full Optimize}

\includesvg{../slides/diagrams/gp/sparse-demo-unconstrained-inducing-6-gp.svg}
\notes{\caption{Gaussian process fitted with location of inducing variables and parameters both optimized}}

\notes{Now we will vary the number of inducing points used to form the approximation.}

\code{m.num_inducing=8
m.randomize()
M = 8
m.set_Z(np.random.rand(M,1)*12)

_ = m.optimize(messages=True)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/sparse-demo-sparse-inducing-8-gp.svg', 
                  transparent=True, frameon=True)}

\slides{
### Eight Optimized Inducing Variables

\includesvg{../slides/diagrams/gp/sparse-demo-sparse-inducing-8-gp.svg}

### Full Gaussian Process Fit

\includesvg{../slides/diagrams/gp/sparse-demo-full-gp.svg}
}

\notesfigure{\includesvg{../slides/diagrams/gp/sparse-demo-sparse-inducing-8-gp.svg}
\includesvg{../slides/diagrams/gp/sparse-demo-full-gp.svg}}
\notes{\caption{Comparison of the full Gaussian process fit with a sparse Gaussian process using eight inducing varibles. Both inducing variables and parameters are optimized.}}


\notes{And we can compare the probability of the result to the full model.}
\code{print(m.log_likelihood(), m_full.log_likelihood())}



