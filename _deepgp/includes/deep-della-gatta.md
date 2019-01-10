\ifndef{deepDellaGatta}
\define{deepDellaGatta}
\editme

\include{_gp/includes/della-gatta-gene-gp.md}
\include{_deepgp/includes/deepgp-enhance.md}

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
mlai.write_figure(filename='../slides/diagrams/deepgp/della-gatta-gene-deep-gp.svg', 
            transparent=True, frameon=True)}

\subsection{TP53 Gene Data Deep GP}

\includesvg{../slides/diagrams/deepgp/della-gatta-gene-deep-gp.svg} 

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, portion = 0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/della-gatta-gene-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}

\subsection{TP53 Gene Data Deep GP}

\includesvg{../slides/diagrams/deepgp/della-gatta-gene-deep-gp-samples.svg} 
				

\displaycode{m.visualize(offset=offset, scale=scale, xlim=xlim, ylim=ylim,
            dataset='della-gatta-gene',
            diagrams='../slides/diagrams/deepgp')}
			
\subsection{TP53 Gene Data Latent 1}

\includesvg{../slides/diagrams/deepgp/della-gatta-gene-deep-gp-layer-0.svg} 

\subsection{TP53 Gene Data Latent 2}

\includesvg{../slides/diagrams/deepgp/della-gatta-gene-deep-gp-layer-1.svg} 

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(offset=offset, ax=ax, scale=scale, xlim=xlim, ylim=ylim, portion=0.1, points=50)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/della-gatta-gene-deep-gp-pinball.svg', 
                  transparent=True, frameon=True, ax=ax)}
				  
\subsection{TP53 Gene Pinball Plot}

\includesvg{../slides/diagrams/deepgp/della-gatta-gene-deep-gp-pinball.svg}


\endif
