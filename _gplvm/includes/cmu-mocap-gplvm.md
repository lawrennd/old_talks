\ifndef{cmuMocapGplvm}
\define{cmuMocapGplvm}

talk-macros.gpp}atasets/includes/cmu-mocap-data.md}

\editme

\subsection{CMU Motion Capture GP-LVM}

\notes{The original data has the figure moving across the floor during the motion capture sequence. We can make the figure walk 'in place', by setting the x, y, z positions of the root node to zero. This makes it easier to visualize the result.}

\code{# Make figure move in place.
data['Y'][:, 0:3] = 0.0}

\notes{We can also remove the mean of the data.}

\code{Y = data['Y']}

\notes{Now we create the GP-LVM model.}

\setupcode{import GPy}

\code{model = GPy.models.GPLVM(Y, 2, normalizer=True)}

\notes{Now we optimize the model.}

\code{model.optimize(messages=True, max_f_eval=10000)}

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

y = model.Y[0, :]

data_show = GPy.plotting.matplot_dep.visualize.skeleton_show(y[None, :], data['skel'], viz_axes)

lvm_visualizer = GPy.plotting.matplot_dep.visualize.lvm(model.X[0].copy(), model, data_show, latent_axes=latent_axes, sense_axes=sense_axes)
mlai.write_figure(figure=fig,
                  filename='cmu-mocap-gplvm.svg', 
				  directory = '\writeDiagramsDir/gplvm')}


\newslide{CMU Mocap Visualisation}

\figure{\includediagram{\diagramsDir/gplvm/cmu-mocap-gplvm}{80%}}{Gaussian process latent variable model visualisation of CMU motion capture data set.}{cmu-mocap-data}


\endif
