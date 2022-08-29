\ifndef{maunaLoaSpectralMixture}
\define{maunaLoaSpectralMixture}

\editme

\subsection{Mauna Loa Spectral Mixture}

\ifndef{maunaLoaData}
\include{_datasets/includes/mauna-loa-data.md}
\else
\setupcode{import pods}
\code{data = pods.datasets.mauna_loa()
x = data['X']
y = data['Y']
}

\setupcode{import GPy}

\code{num_comps = 10
kernel = GPy.kern.ExpQuadCosine(1)
for i in range(num_comps-1):
    kernel += GPy.kern.ExpQuadCosine(1)
kernel+=GPy.kern.Bias(1)
kernel.randomize()
model = GPy.models.GPRegression(x, y, kernel)
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
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

model.plot(ax=ax)

mlai.write_figure('mauna-loa-spectral-mixture-gp', directory='\writeDiagramsDir/gp')}

\figure{\includediagram{\diagramsDir/gp/mauna-loa-spectral-mixture-gp}{80%}}{Spectral mixture GP as applied to the Mauna Loa Observatory carbon dioxide concentration data.}{mauna-loa-spectral-mixture-gp}

\endif
