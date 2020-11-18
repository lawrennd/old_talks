
\ifndef{spectralMixtureKernel}
\define{spectralMixtureKernel}

\editme

\subsection{Spectral Mixture Kernel}


\include{_datasets/includes/box-jenkins-airline-data.md}


\setupcode{import GPy}

\code{num_comps = 10
kernel = GPy.kern.ExpQuadCosine(1)
for i in range(num_comps-1):
    kernel += GPy.kern.ExpQuadCosine(1)

kernel+=GPy.kern.Bias(1)
kernel.randomize()
model = GPy.models.GPRegression(X, y, kernel)
#model['.*lengthscale'] = np.random.uniform(0.0, 6.0, size=model['.*lengthscale'].shape)
#model['.*bandwidth'] = 2./np.sqrt(np.random.gamma(1.0, 0.5*(X.max()-X.min()), size=model['.*bandwidth'].shape))
#model['.*variance'] = 5.0
display(model)}


\code{model.optimize(messages=True)}

\code{display(model)}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

model.plot(ax=ax)

mlai.write_figure('box-jenkins-spectral-mixture-gp', directory='\writeDiagramsDir/gp')}

\figure{\includediagram{\diagramsDir/gp/box-jenkins-spectral-mixture-gp}{80%}}{Spectral mixture GP as applied to the Box-Jenkins airline data.}{box-jenkins-spectral-mixture-gp}


\include{_datasets/includes/mauna-loa-data.md}

\setupcode{import GPy}

\code{num_comps = 10
kernel = GPy.kern.ExpQuadCosine(1)
for i in range(num_comps-1):
    kernel += GPy.kern.ExpQuadCosine(1)
kernel+=GPy.kern.Bias(1)
kernel.randomize()
model = GPy.models.GPRegression(X, y, kernel)
#model['.*frequency'] = np.random.uniform(0.0, 6.0, size=model['.*frequency'].shape)
#model['.*bandwidth'] = 2./np.sqrt(np.random.gamma(1.0, 0.5*(X.max()-X.min()), size=model['.*bandwidth'].shape))
#model['.*variance'] = 5.0
#model['.*bias_variance'] = 90000
display(model)}

\notes{Now we optimize the model.}

\code{model.optimize(messages=True)}


\code{display(model)}

\setupplotcode{}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

model.plot(ax=ax)

mlai.write_figure('mauna-loa-spectral-mixture-gp', directory='\writeDiagramsDir/gp')}

\figure{\includediagram{\diagramsDir/gp/mauna-loa-spectral-mixture-gp}{80%}}{Spectral mixture GP as applied to the Mauna Loa Observatory carbon dioxide concentration data.}{mauna-loa-spectral-mixture-gp}

\endif
