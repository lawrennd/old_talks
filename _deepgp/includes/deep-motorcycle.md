\code{import pods
data = pods.datasets.mcycle()
x = data['X']
y = data['Y']
scale=np.sqrt(y.var())
offset=y.mean()
yhat = (y - offset)/scale}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
_ = ax.set_xlabel('time', fontsize=20)
_ = ax.set_ylabel('acceleration', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(filename='../../slides/diagrams/datasets/motorcycle-helmet.svg', 
            transparent=True, frameon=True)}

### Motorcycle Helmet Data {data-transition="None"}

\includesvg{../slides/diagrams/datasets/motorcycle-helmet.svg}

\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='time', ylabel='acceleration/$g$', fontsize=20, portion=0.5)
xlim=(-20,80)
ylim=(-180,120)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig,filename='../../slides/diagrams/gp/motorcycle-helmet-gp.svg', 
            transparent=True, frameon=True)}


### Motorcycle Helmet Data GP {data-transition="None"}

\includesvg{../slides/diagrams/gp/motorcycle-helmet-gp.svg}


\code{layers = [y.shape[1], 1, x.shape[1]]
inits = ['PCA']*(len(layers)-1)
kernels = []
for i in layers[1:]:
    kernels += [GPy.kern.RBF(i)]
m = deepgp.DeepGP(layers,Y=yhat, X=x, 
                  inits=inits, 
                  kernels=kernels, # the kernels for each layer
                  num_inducing=20, back_constraint=False)



m.initialize()}

\code{m.staged_optimize(iters=(1000,1000,10000), messages=(True, True, True))}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='time', ylabel='acceleration/$g$', fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='../../slides/diagrams/deepgp/motorcycle-helmet-deep-gp.svg', 
            transparent=True, frameon=True)}

### Motorcycle Helmet Data Deep GP {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/motorcycle-helmet-deep-gp.svg}


\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, xlabel='time', ylabel='acceleration/$g$', portion = 0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)

mlai.write_figure(figure=fig, filename='../../slides/diagrams/deepgp/motorcycle-helmet-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}

### Motorcycle Helmet Data Deep GP {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/motorcycle-helmet-deep-gp-samples.svg}

\plotcode{m.visualize(xlim=xlim, ylim=ylim, scale=scale,offset=offset, 
            xlabel="time", ylabel="acceleration/$g$", portion=0.5,
            dataset='motorcycle-helmet',
            diagrams='../../slides/diagrams/deepgp')}

### Motorcycle Helmet Data Latent 1 {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/motorcycle-helmet-deep-gp-layer-0.svg}

### Motorcycle Helmet Data Latent 2 {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/motorcycle-helmet-deep-gp-layer-1.svg}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(ax=ax, xlabel='time', ylabel='acceleration/g', 
                    points=50, scale=scale, offset=offset, portion=0.1)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/deepgp/motorcycle-helmet-deep-gp-pinball.svg', 
                  transparent=True, frameon=True)}

### Motorcycle Helmet Pinball Plot {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/motorcycle-helmet-deep-gp-pinball.svg}


