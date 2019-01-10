\ifndef{deepOlympic}
\define{deepOlympic}
\define{deepGpEnhanced}
\editme
\include{_gp/includes/olympic-marathon-gp.md}

\subsection{Deep GP Fit}

\slides{* Can a Deep Gaussian process help?

* Deep GP is one GP feeding into another.}


\notes{Let's see if a deep Gaussian process can help here. We will construct a deep Gaussian process with one hidden layer (i.e. one Gaussian process feeding into another). 

Build a Deep GP with an additional hidden layer (one dimensional) to fit the model.}

\setupcode{import GPy
import deepgp}
\code{hidden = 1
m = deepgp.DeepGP([y.shape[1],hidden,x.shape[1]],Y=yhat, X=x, inits=['PCA','PCA'], 
                  kernels=[GPy.kern.RBF(hidden,ARD=True),
                           GPy.kern.RBF(x.shape[1],ARD=True)], # the kernels for each layer
                  num_inducing=50, back_constraint=False)}
				  
\notes{Deep Gaussian process models also can require some thought in initialization. Here we choose to start by setting the noise variance to be one percent of the data variance.

Optimization requires moving variational parameters in the hidden layer representing the mean and variance of the expected values in that layer. Since all those values can be scaled up, and this only results in a downscaling in the output of the first GP, and a downscaling of the input length scale to the second GP. It makes sense to first of all fix the scales of the covariance function in each of the GPs.

Sometimes, deep Gaussian processes can find a local minima which involves increasing the noise level of one or more of the GPs. This often occurs because it allows a minimum in the KL divergence term in the lower bound on the likelihood. To avoid this minimum we habitually train with the likelihood variance (the noise on the output of the GP) fixed to some lower value for some iterations.

Let's create a helper function to initialize the models we use in the notebook.}

\setupcode{import deepgp}

\loadcode{initialize}{deepgp_tutorial}
\helpercode{# Bind the new method to the Deep GP object.
deepgp.DeepGP.initialize=initialize}

\code{# Call the initalization
m.initialize()}

\notes{Now optimize the model. The first stage of optimization is working on variational parameters and lengthscales only. 

\code{m.optimize(messages=False,max_iters=100)}

Now we remove the constraints on the scale of the covariance functions associated with each GP and optimize again.

\code{for layer in m.layers:
    pass #layer.kern.variance.constrain_positive(warning=False)
m.obslayer.kern.variance.constrain_positive(warning=False)
m.optimize(messages=False,max_iters=100)}

Finally, we allow the noise variance to change and optimize for a large number of iterations.

\code{for layer in m.layers:
    layer.likelihood.variance.constrain_positive(warning=False)
m.optimize(messages=True,max_iters=10000)}

For our optimization process we define a new function.}

\loadcode{staged_optimize}{deepgp_tutorial}
\code{# Bind the new method to the Deep GP object.
deepgp.DeepGP.staged_optimize=staged_optimize}

\code{m.staged_optimize(messages=(True,True,True))}

\notes{\subsection{Plot the prediction}

The prediction of the deep GP can be extracted in a similar way to the normal GP. Although, in this case, it is an approximation to the true distribution, because the true distribution is not Gaussian.}

\setupcode{import matplotlib.pyplot as plt}
\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, scale=scale, offset=offset, ax=ax, xlabel='year', ylabel='pace min/km', 
          fontsize=20, portion=0.2)
ax.set_xlim(xlim)

ax.set_ylim(ylim)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/olympic-marathon-deep-gp.svg', 
                transparent=True, frameon=True)}

\subsection{Olympic Marathon Data Deep GP}

\includesvg{../slides/diagrams/deepgp/olympic-marathon-deep-gp.svg}


\loadcode{posterior_sample}{deepgp_tutorial}
\helpercode{deepgp.DeepGP.posterior_sample = posterior_sample}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, 
                  xlabel='year', ylabel='pace min/km', portion = 0.225)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/olympic-marathon-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}


\subsection{Olympic Marathon Data Deep GP}

\includesvg{../slides/diagrams/deepgp/olympic-marathon-deep-gp-samples.svg}


\notes{\subsection{Fitted GP for each layer}

Now we explore the GPs the model has used to fit each layer. First of all, we look at the hidden layer.
}

\loadcode{visualize}{deepgp_tutorial}
\helpercode{# Bind the new method to the Deep GP object.
deepgp.DeepGP.visualize=visualize}

\displaycode{m.visualize(scale=scale, offset=offset, xlabel='year',
            ylabel='pace min/km',xlim=xlim, ylim=ylim,
            dataset='olympic-marathon',
            diagrams='../slides/diagrams/deepgp')}


\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_plots('olympic-marathon-deep-gp-layer-{sample:0>1}.svg', 
                            '../slides/diagrams/deepgp', sample=(0,1))}

\newslide{Olympic Marathon Data Latent 1}

\includesvg{../slides/diagrams/deepgp/olympic-marathon-deep-gp-layer-0.svg}

\newslide{Olympic Marathon Data Latent 2}

\includesvg{../slides/diagrams/deepgp/olympic-marathon-deep-gp-layer-1.svg}

\loadcode{visualize_pinball}{deepgp_tutorial}
\helpercode{# Bind the new method to the Deep GP object.
deepgp.DeepGP.visualize_pinball=visualize_pinball}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(ax=ax, scale=scale, offset=offset, points=30, portion=0.1,
                    xlabel='year', ylabel='pace km/min', vertical=True)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/olympic-marathon-deep-gp-pinball.svg', 
                  transparent=True, frameon=True)}

\subsection{Olympic Marathon Pinball Plot}

\includesvg{../slides/diagrams/deepgp/olympic-marathon-deep-gp-pinball.svg}

\notes{The pinball plot shows the flow of any input ball through the deep Gaussian process. In a pinball plot a series of vertical parallel lines would indicate a purely linear function. For the olypmic marathon data we can see the first layer begins to shift from input towards the right. Note it also does so with some uncertainty (indicated by the shaded backgrounds). The second layer has less uncertainty, but bunches the inputs more strongly to the right. This input layer of uncertainty, followed by a layer that pushes inputs to the right is what gives the heteroschedastic noise.}

\endif
