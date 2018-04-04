\slidenotes{}{
### Step Function

Next we consider a simple step function data set.
}

\code{num_low=25
num_high=25
gap = -.1
noise=0.0001
x = np.vstack((np.linspace(-1, -gap/2.0, num_low)[:, np.newaxis],
              np.linspace(gap/2.0, 1, num_high)[:, np.newaxis]))
y = np.vstack((np.zeros((num_low, 1)), np.ones((num_high,1))))
scale = np.sqrt(y.var())
offset = y.mean()
yhat = (y-offset)/scale}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
_ = ax.set_xlabel('$x$', fontsize=20)
_ = ax.set_ylabel('$y$', fontsize=20)
xlim = (-2, 2)
ylim = (-0.6, 1.6)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/datasets/step-function.svg', 
            transparent=True, frameon=True)}
			
### Step Function Data {data-transition="None"}

\includesvg{../slides/diagrams/datasets/step-function.svg} 


\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)

mlai.write_figure(figure=fig,filename='../../slides/diagrams/gp/step-function-gp.svg', 
            transparent=True, frameon=True)}
			

### Step Function Data GP {data-transition="None"}

\includesvg{../slides/diagrams/gp/step-function-gp.svg} 

\code{layers = [y.shape[1], 1, 1, 1,x.shape[1]]
inits = ['PCA']*(len(layers)-1)
kernels = []
for i in layers[1:]:
    kernels += [GPy.kern.RBF(i)]
m = deepgp.DeepGP(layers,Y=yhat, X=x, 
                  inits=inits, 
                  kernels=kernels, # the kernels for each layer
                  num_inducing=20, back_constraint=False)}
				  
\code{m.initialize()
m.staged_optimize()}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='../../slides/diagrams/deepgp/step-function-deep-gp.svg', 
            transparent=True, frameon=True)}

### Step Function Data Deep GP {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp.svg} 

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot_model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, portion = 0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/deepgp/step-function-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}

### Step Function Data Deep GP {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-samples.svg} 
				
\plotcode{m.visualize(offset=offset, scale=scale, xlim=xlim, ylim=ylim,
            dataset='step-function',
            diagrams='../../slides/diagrams/deepgp')}
			
### Step Function Data Latent 1 {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-0.svg} 

### Step Function Data Latent 2 {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-1.svg} 

### Step Function Data Latent 3 {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-2.svg} 

### Step Function Data Latent 4 {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-3.svg} 

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(offset=offset, ax=ax, scale=scale, xlim=xlim, ylim=ylim, portion=0.1, points=50)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/deepgp/step-function-deep-gp-pinball.svg', 
                  transparent=True, frameon=True, ax=ax)}
				  
### Step Function Pinball Plot {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-pinball.svg}


