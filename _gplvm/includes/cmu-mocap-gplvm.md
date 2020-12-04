\ifndef{cmuMocapGplvm}
\define{cmuMocapGplvm}

\include{_datasets/includes/cmu-mocap-data.md}

\editme

\notes{The original data has the figure moving across the floor during the motion capture sequence. We can make the figure walk 'in place', by setting the x, y, z positions of the root node to zero. This makes it easier to visualize the result.}

\code{# Make figure move in place.
data['Y'][:, 0:3] = 0.0}

\notes{We can also remove the mean of the data.}

\code{Y = data['Y']
Y_mean = Y.mean(0)
Y_std = Y.std(0)
Yhat = (Y-Y_mean)/Y_std}

\notes{Now we create the GP-LVM model.}

\setupcode{import GPy}

\code{model = GPy.models.GPLVM(Yhat, 2)}

\notes{Now we optimize the model.}

\code{model.optimize(messages=True, max_f_eval=10000)}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\setupplotcode{import numpy as np}

\plotcode{ax = model.plot_latent()}



\plotcode{y = model.Y[0, :]
data_show = GPy.plotting.matplot_dep.visualize.skeleton_show(y[np.newaxis, :], 
                                                             data['skel'])
lvm_visualizer = GPy.plotting.matplot_dep.visualize.lvm(model.X[0].copy(), 
                                                        model, 
                                                        data_show, 
														latent_axes=ax)
input('Press enter to finish')
lvm_visualizer.close()
data_show.close()}

\endif
