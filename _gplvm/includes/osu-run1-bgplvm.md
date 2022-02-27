\ifndef{osuRun1Bgplvm}
\define{osuRun1Bgplvm}

talk-macros.gpp}atasets/includes/osu-run1-data.md}

\editme

\subsection{OSU Run 1 Motion Capture Data with Bayesian GP-LVM}

\setupcode{import GPy
from GPy.models import BayesianGPLVM
import numpy as np}


\code{q = 6
kernel = GPy.kern.RBF(q, lengthscale=np.repeat(.5, q), ARD=True)
model = BayesianGPLVM(data['Y'], q,
                      init="PCA",
                      num_inducing=20, kernel=kernel)

model.data = data}

\notes{Variational methods decompose the lower bound on the log likelihood (or ELBO) into a term which represents the expectation of the log likelihood under the approximation posterior and a KL divergence between the *prior* and the approximate posterior. A common local minimum is to ignore the log likelihood and set the approximate posterior equal to the prior. To avoid this we initialise with low Gaussian noise, which emphasises the expectation of the log likelihood under the posterior. Here it is set to a noise variance of 0.001.}

\code{model.likelihood.variance = 0.001}

\code{model.optimize('bfgs', messages=True, max_iters=5e3, bfgs_factor=10)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\setupplotcode{%matplotlib notebook}

\setupplotcode{import numpy as np}

\plotcode{fig, _ = plt.subplots(figsize=plot.big_wide_figsize)
latent_axes = fig.add_subplot(131)
sense_axes = fig.add_subplot(132)
viz_axes = fig.add_subplot(133, projection='3d')

model.plot_latent(ax=latent_axes)
latent_axes.set_aspect('equal')

y = model.Y[:1, :].copy()

data_show = GPy.plotting.matplot_dep.visualize.stick_show(y, connect=data['connect'], axes=viz_axes)
dim_select = GPy.plotting.matplot_dep.visualize.lvm_dimselect(model.X.mean[:1, :].copy(), 
                                                              model, 
							      data_show, 
							      latent_axes=latent_axes, 
							      sense_axes=sense_axes)

mlai.write_figure(figure=fig,
                  filename='osu-run1-bgplvm.svg', 
	           	  directory = '\writeDiagramsDir/gplvm')}


\newslide{OSU Run 1 Bayesian GP-LVM}

\figure{\includediagram{\diagramsDir/gplvm/osu-run1-bgplvm}{80%}}{Bayesian Gaussian process latent variable model visualisation of OSU motion capture data set.}{osu-run1-data}


\endif
