\ifndef{deepStepFunction}
\define{deepStepFunction}
\include{_gp/includes/step-function-gp.md}
\include{_deepgp/includes/deepgp-enhance.md}

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

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='../slides/diagrams/deepgp/step-function-deep-gp.svg', 
            transparent=True, frameon=True)}

\subsection{Step Function Data Deep GP}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp.svg} 

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)

plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, portion = 0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/step-function-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}

\subsection{Step Function Data Deep GP}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-samples.svg} 
				

\displaycode{m.visualize(offset=offset, scale=scale, xlim=xlim, ylim=ylim,
            dataset='step-function',
            diagrams='../slides/diagrams/deepgp')}
			
\subsection{Step Function Data Latent 1}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-0.svg} 

\subsection{Step Function Data Latent 2}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-1.svg} 

\subsection{Step Function Data Latent 3}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-2.svg} 

\subsection{Step Function Data Latent 4}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-layer-3.svg} 

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(offset=offset, ax=ax, scale=scale, xlim=xlim, ylim=ylim, portion=0.1, points=50)
mlai.write_figure(figure=fig, filename='../slides/diagrams/deepgp/step-function-deep-gp-pinball.svg', 
                  transparent=True, frameon=True, ax=ax)}
				  
\subsection{Step Function Pinball Plot}

\includesvg{../slides/diagrams/deepgp/step-function-deep-gp-pinball.svg}

\endif
