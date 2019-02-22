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
				  
\notes{}

\setupcode{import deepgp}

\code{# Call the initalization
m.initialize()}

\notes{Now optimize the model.}

\code{for layer in m.layers:
    layer.likelihood.variance.constrain_positive(warning=False)
m.optimize(messages=True,max_iters=10000)}



\code{m.staged_optimize(messages=(True,True,True))}


\setupplotcode{import matplotlib.pyplot as plt}
\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, scale=scale, offset=offset, ax=ax, xlabel='year', ylabel='pace min/km', 
          fontsize=20, portion=0.2)
ax.set_xlim(xlim)

ax.set_ylim(ylim)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/olympic-marathon-deep-gp.svg', 
                transparent=True, frameon=True)}

\subsection{Olympic Marathon Data Deep GP}

\figure{
\includediagram{../slides/diagrams/deepgp/olympic-marathon-deep-gp}
\notes{\caption{Deep GP fit to the Olympic marathon data. Error bars now change as the prediction evolves.}}
}
\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, 
                  xlabel='year', ylabel='pace min/km', portion = 0.225)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/olympic-marathon-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}


\subsection{Olympic Marathon Data Deep GP}

\figure{
\includediagram{../slides/diagrams/deepgp/olympic-marathon-deep-gp-samples}
\notes{\caption{Point samples run through the deep Gaussian process show the distribution of output locations.}}
}

\notes{\subsection{Fitted GP for each layer}

Now we explore the GPs the model has used to fit each layer. First of all, we look at the hidden layer.
}

\displaycode{m.visualize(scale=scale, offset=offset, xlabel='year',
            ylabel='pace min/km',xlim=xlim, ylim=ylim,
            dataset='olympic-marathon',
            diagrams='../slides/diagrams/deepgp')}


\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_plots('olympic-marathon-deep-gp-layer-{sample:0>1}.svg', 
                            '../slides/diagrams/deepgp', sample=(0,1))}

\newslide{Olympic Marathon Data Latent 1}

\figure{
\includediagram{../slides/diagrams/deepgp/olympic-marathon-deep-gp-layer-0}
\notes{\caption{The mapping from input to the latent layer is broadly linear.}}
}

\newslide{Olympic Marathon Data Latent 2}

\figure{
\includediagram{../slides/diagrams/deepgp/olympic-marathon-deep-gp-layer-1}
\notes{\caption{}}
}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(ax=ax, scale=scale, offset=offset, points=30, portion=0.1,
                    xlabel='year', ylabel='pace km/min', vertical=True)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/olympic-marathon-deep-gp-pinball.svg', 
                  transparent=True, frameon=True)}

\subsection{Olympic Marathon Pinball Plot}

\figure{
\includediagram{../slides/diagrams/deepgp/olympic-marathon-deep-gp-pinball}
\notes{\caption{\ifndef{pinballPlot}\define{pinBallPlot}A pinball plot shows the movement of the 'ball' as it passes through each layer of the Gaussian processes. Mean directions of movement are shown by lines. Shading gives one standard deviation of movement position. At each layer, the uncertainty is reset. The overal uncertainty is the cumulative uncertainty from all the layers.\endif There is some grouping of later points towards the right in the first layer, which also injects a large amount of uncertainty. Due to flattening of the curve in the second layer towards the right the uncertainty is reduced in final output.}}
}
\notes{The pinball plot shows the flow of any input ball through the deep Gaussian process. In a pinball plot a series of vertical parallel lines would indicate a purely linear function. For the olypmic marathon data we can see the first layer begins to shift from input towards the right. Note it also does so with some uncertainty (indicated by the shaded backgrounds). The second layer has less uncertainty, but bunches the inputs more strongly to the right. This input layer of uncertainty, followed by a layer that pushes inputs to the right is what gives the heteroschedastic noise.}

\endif
