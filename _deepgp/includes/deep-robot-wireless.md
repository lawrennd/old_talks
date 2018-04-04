\notes{
### Robot Wireless Data

The robot wireless data is taken from an experiment run by Brian Ferris at University of Washington. It consists of the measurements of WiFi access point signal strengths as Brian walked in a loop.}

\code{data=pods.datasets.robot_wireless()

x = np.linspace(0,1,215)[:, np.newaxis]
y = data['Y']
offset = y.mean()
scale = np.sqrt(y.var())
yhat = (y-offset)/scale}

\notes{The ground truth is recorded in the data, the actual loop is given in the plot below.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
plt.plot(data['X'][:, 1], data['X'][:, 2], 'r.', markersize=5)
ax.set_xlabel('x position', fontsize=20)
ax.set_ylabel('y position', fontsize=20)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/datasets/robot-wireless-ground-truth.svg', transparent=True, frameon=True)}

### Robot Wireless Ground Truth {data-transition="None"}

\includesvg{../slides/diagrams/datasets/robot-wireless-ground-truth.svg}

\notes{We will ignore this ground truth in making our predictions, but see if the model can recover something similar in one of the latent layers.}

\plotcode{output_dim=1
xlim = (-0.3, 1.3)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x.flatten(), y[:, output_dim], 
            'r.', markersize=5)

ax.set_xlabel('time', fontsize=20)
ax.set_ylabel('signal strength', fontsize=20)
xlim = (-0.2, 1.2)
ylim = (-0.6, 2.0)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(figure=fig, filename='../../slides/diagrams/datasets/robot-wireless-dim-' + str(output_dim) + '.svg', 
            transparent=True, frameon=True)}


### Robot WiFi Data {data-transition="None"}
			
\includesvg{../slides/diagrams/datasets/robot-wireless-dim-1.svg}

\notes{Perform a Gaussian process fit on the data using GPy.}

\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, output_dim=output_dim, scale=scale, offset=offset, ax=ax, 
                  xlabel='time', ylabel='signal strength', fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='../../slides/diagrams/gp/robot-wireless-gp-dim-' + str(output_dim)+ '.svg', 
            transparent=True, frameon=True)}

### Robot WiFi Data GP {data-transition="None"}

\includesvg{../slides/diagrams/gp/robot-wireless-gp-dim-1.svg}

\code{layers = [y.shape[1], 10, 5, 2, 2, x.shape[1]]
inits = ['PCA']*(len(layers)-1)
kernels = []
for i in layers[1:]:
    kernels += [GPy.kern.RBF(i, ARD=True)]}
	
\code{m = deepgp.DeepGP(layers,Y=y, X=x, inits=inits, 
                  kernels=kernels,
                  num_inducing=50, back_constraint=False)
m.initialize()}

\code{m.staged_optimize(messages=(True,True,True))}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, output_dim=output_dim, scale=scale, offset=offset, ax=ax, 
                  xlabel='time', ylabel='signal strength', fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/deepgp/robot-wireless-deep-gp-dim-' + str(output_dim)+ '.svg', 
                  transparent=True, frameon=True)}
				  
### Robot WiFi Data Deep GP {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/robot-wireless-deep-gp-dim-1.svg}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_sample(m, output_dim=output_dim, scale=scale, offset=offset, samps=10, ax=ax,
                  xlabel='time', ylabel='signal strength', fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/deepgp/robot-wireless-deep-gp-samples-dim-' + str(output_dim)+ '.svg', 
                  transparent=True, frameon=True)}

### Robot WiFi Data Deep GP {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/robot-wireless-deep-gp-samples-dim-1.svg}

### Robot WiFi Data Latent Space {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/robot-wireless-ground-truth.svg}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(m.layers[-2].latent_space.mean[:, 0], 
        m.layers[-2].latent_space.mean[:, 1], 
        'r.-', markersize=5)

ax.set_xlabel('latent dimension 1', fontsize=20)
ax.set_ylabel('latent dimension 2', fontsize=20)

mlai.write_figure(figure=fig, filename='../../slides/diagrams/deepgp/robot-wireless-latent-space.svg', 
            transparent=True, frameon=True)}
			
### Robot WiFi Data Latent Space {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/robot-wireless-latent-space.svg}


