\ifndef{stepFunctionDeepGp}
\define{stepFunctionDeepGp}

talk-macros.gpp}p/includes/step-function-gp.md}
talk-macros.gpp}eepgp/includes/deepgp-enhance.md}

\editme

\subsection{Step Function Data Deep GP}

\notes{First we initialize a deep Gaussian process with three latent layers (four layers total). Within each layer we create a GP with an exponentiated quadratic covariance (```GPy.kern.RBF```).

At each layer we use 20 inducing points for the variational approximation.}

\code{layers = [y.shape[1], 1, 1, 1,x.shape[1]]
inits = ['PCA']*(len(layers)-1)
kernels = []
for i in layers[1:]:
    kernels += [GPy.kern.RBF(i)]
	
m = deepgp.DeepGP(layers,Y=yhat, X=x, 
                  inits=inits, 
                  kernels=kernels, # the kernels for each layer
                  num_inducing=20, back_constraint=False)}

\notes{Once the model is constructed we initialize the parameters, and perform the staged optimization which starts by optimizing variational parameters with a low noise and proceeds to optimize the whole model.}

\code{m.initialize()
m.staged_optimize()}

\displaynotes{We plot the output of the deep Gaussian process fitted to the step data as follows.}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='\writeDiagramsDir/deepgp/step-function-deep-gp.svg', 
            transparent=True, frameon=True)}

\notes{The deep Gaussian process does a much better job of fitting the data. It handles the discontinuity easily, and error bars drop to smaller values in the regions of data.}

\figure{\includediagram{\diagramsDir/deepgp/step-function-deep-gp}{80%}}{Deep Gaussian process fit to the step function data.}{step-function-deep-gp}

\subsection{Step Function Data Deep GP}

\displaynotes{The samples of the model can be plotted with the helper function from `mlai.plot`, `model_sample`}

\setupdisplaycode{import mlai.plot as plot}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)

plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, portion = 0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='\writeDiagramsDir/deepgp/step-function-deep-gp-samples.svg', 
                  transparent=True, frameon=True)}

\notes{The samples from the model show that the error bars, which are informative for Gaussian outputs, are less informative for this model. They make clear that the data points lie, in output mainly at 0 or 1, or occasionally in between.}

\figure{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-samples}{80%}}{Samples from the deep Gaussian process model for the step function fit.}{step-function-deep-gp-samples}
				
\displaynotes{The visualize code allows us to inspect the intermediate layers in the deep GP model to understand how it has reconstructed the step function.}

\displaycode{m.visualize(offset=offset, scale=scale, xlim=xlim, ylim=ylim,
            dataset='step-function',
            diagrams='\writeDiagramsDir/deepgp')}
			
\newslide{Step Function Data Latent 1}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-0}}

\newslide{Step Function Data Latent 2}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-1}}

\newslide{Step Function Data Latent 3}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-2}}

\newslide{Step Function Data Latent 4}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-3}}

\notes{
\figure{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-0}{60%} 
\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-1}{60%}
\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-2}{60%}
\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-3}{60%}}{From top to bottom, the Gaussian process mapping function that makes up each layer of the resulting deep Gaussian process.}{step-function-deep-gp-mappings}}

\newslide{Step Function Pinball Plot}

\displaynotes{A pinball plot can be created for the resulting model to understand how the input is being translated to the output across the different layers.}

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(offset=offset, ax=ax, scale=scale, xlim=xlim, ylim=ylim, portion=0.1, points=50)
mlai.write_figure(figure=fig, filename='\writeDiagramsDir/deepgp/step-function-deep-gp-pinball.svg', 
                  transparent=True, frameon=True, ax=ax)}
				  
\figure{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-pinball}{60%}}{Pinball plot of the deep GP fitted to the step function data. Each layer of the model pushes the 'ball' towards the left or right, saturating at 1 and 0. This causes the final density to be be peaked at 0 and 1. Transitions occur driven by the uncertainty of the mapping in each layer.}{step-function-deep-gp-pinball}


\endif
