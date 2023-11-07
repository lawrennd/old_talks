\ifndef{motorcycleHelmetDeepGp}
\define{motorcycleHelmetDeepGp}

\include{_gp/includes/motorcycle-helmet-gp.md}
\include{_deepgp/includes/deepgp-enhance.md}

\editme

\subsection{Motorcycle Helmet Data Deep GP}

\setupcode{import deepgp}
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

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}
\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, scale=scale, offset=offset, ax=ax, xlabel='time', ylabel='acceleration/$g$', fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='\writeDiagramsDir/deepgp/motorcycle-helmet-deep-gp.svg', 
            transparent=True, frameon=True)}


\figure{\includediagram{\diagramsDir/deepgp/motorcycle-helmet-deep-gp}{80%}}{Deep Gaussian process fit to the motorcycle helmet accelerometer data.}{motorcycle-helmet-deep-gp}

\setupdisplaycode{import mlai.plot as plot
import mlai}
\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, xlabel='time', ylabel='acceleration/$g$', portion = 0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)

mlai.write_figure(figure=fig, filename='\writeDiagramsDir/deepgp/motorcycle-helmet-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}

\subsection{Motorcycle Helmet Data Deep GP}

\figure{\includediagram{\diagramsDir/deepgp/motorcycle-helmet-deep-gp-samples}{80%}}{Samples from the deep Gaussian process as fitted to the motorcycle helmet accelerometer data.}{motorcycle-helmet-deep-gp-samples}

\displaycode{m.visualize(xlim=xlim, ylim=ylim, scale=scale,offset=offset, 
            xlabel="time", ylabel="acceleration/$g$", portion=0.5,
            dataset='motorcycle-helmet',
            diagrams='\writeDiagramsDir/deepgp')}

\subsection{Motorcycle Helmet Data Latent 1}

\figure{\includediagram{\diagramsDir/deepgp/motorcycle-helmet-deep-gp-layer-0}{60%}}{Mappings from the input to the latent layer for the motorcycle helmet accelerometer data.}{motorcycle-helmet-deep-gp-layer-0}

\subsection{Motorcycle Helmet Data Latent 2}

\figure{\includediagram{\diagramsDir/deepgp/motorcycle-helmet-deep-gp-layer-1}{60%}}{Mappings from the latent layer to the output layer for the motorcycle helmet accelerometer data.}{motorcycle-helmet-deep-gp-layer-1}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(ax=ax, xlabel='time', ylabel='acceleration/g', 
                    points=50, scale=scale, offset=offset, portion=0.1)
mlai.write_figure(figure=fig, filename='\writeDiagramsDir/deepgp/motorcycle-helmet-deep-gp-pinball.svg', 
                  transparent=True, frameon=True)}

\subsection{Motorcycle Helmet Pinball Plot}

\figure{\includediagram{\diagramsDir/deepgp/motorcycle-helmet-deep-gp-pinball}{60%}}{Pinball plot for the mapping from input to output layer for the motorcycle helmet accelerometer data.}{motorcycle-helmet-deep-gp-pinball}
\endif
