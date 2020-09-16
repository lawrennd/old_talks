\ifndef{dellaGattaDeepGp}
\define{dellaGattaDeepGp}

\include{_gp/includes/della-gatta-gene-gp.md}
\include{_deepgp/includes/deepgp-enhance.md}

\editme

\code{layers = [y.shape[1], 1,x.shape[1]]
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

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='\writeDiagramsDir/deepgp/della-gatta-gene-deep-gp.svg', 
            transparent=True, frameon=True)}

\subsection{Della Gatta Gene Data Deep GP}

\figure{\includediagram{\diagramsDir/deepgp/della-gatta-gene-deep-gp}{80%}}{Deep Gaussian process fit to the Della Gatta gene expression data.}{della-gatta-gene-deep-gp}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, portion = 0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='\writeDiagramsDir/deepgp/della-gatta-gene-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}

\subsection{Della Gatta Gene Data Deep GP}

\figure{\includediagram{\diagramsDir/deepgp/della-gatta-gene-deep-gp-samples}}{Deep Gaussian process samples fitted to the Della Gatta gene expression data.}{della-gatta-gene-deep-gp-samples}
				

\displaycode{m.visualize(offset=offset, scale=scale, xlim=xlim, ylim=ylim,
            dataset='della-gatta-gene',
            diagrams='\writeDiagramsDir/deepgp')}
			
\subsection{Della Gatta Gene Data Latent 1}

\figure{\includediagram{\diagramsDir/deepgp/della-gatta-gene-deep-gp-layer-0}{50%}}{Gaussian process mapping from input to latent layer for the della Gatta gene expression data.}{della-gatta-gene-deep-gp-layer-0}

\subsection{Della Gatta Gene Data Latent 2}

\figure{\includediagram{\diagramsDir/deepgp/della-gatta-gene-deep-gp-layer-1}{50%}}{Gaussian process mapping from latent to output layer for the della Gatta gene expression data.}{della-gatta-gene-deep-gp-layer-1}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(offset=offset, ax=ax, scale=scale, xlim=xlim, ylim=ylim, portion=0.1, points=50)
mlai.write_figure(figure=fig, filename='\writeDiagramsDir/deepgp/della-gatta-gene-deep-gp-pinball.svg', 
                  transparent=True, frameon=True, ax=ax)}
				  
\subsection{TP53 Gene Pinball Plot}

\figure{\includediagram{\diagramsDir/deepgp/della-gatta-gene-deep-gp-pinball}{60%}}{\ifndef{pinballPlot}\define{pinBallPlot}A pinball plot shows the movement of the 'ball' as it passes through each layer of the Gaussian processes. Mean directions of movement are shown by lines. Shading gives one standard deviation of movement position. At each layer, the uncertainty is reset. The overal uncertainty is the cumulative uncertainty from all the layers.\endif Pinball plot of the della Gatta gene expression data.}{della-gatta-gene-deep-gp-pinball}


\endif
