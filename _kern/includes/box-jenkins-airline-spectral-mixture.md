\ifndef{boxJenkinsAirlineSpectralMixture}
\define{boxJenkinsAirlineSpectralMixture}

\editme

\subsection{Box-Jenkins Airline Spectral Mixture}

\ifndef{boxJenkinsAirlineData}
\include{_datasets/includes/box-jenkins-airline-data.md}
\else
\setupcode{import pods}
\code{data = pods.datasets.boxjenkins_airline()
x = data['X']
y = data['Y']}

\setupcode{import GPy}

\code{num_comps = 10
kernel = GPy.kern.ExpQuadCosine(1)
for i in range(num_comps-1):
    kernel += GPy.kern.ExpQuadCosine(1)

kernel+=GPy.kern.Bias(1)
kernel.randomize()
model = GPy.models.GPRegression(x, y, kernel)
#model['.*lengthscale'] = np.random.uniform(0.0, 6.0, size=model['.*lengthscale'].shape)
#model['.*bandwidth'] = 2./np.sqrt(np.random.gamma(1.0, 0.5*(X.max()-X.min()), size=model['.*bandwidth'].shape))
#model['.*variance'] = 5.0
display(model)}


\code{model.optimize(messages=True)}

\code{display(model)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

model.plot(ax=ax)

mlai.write_figure('box-jenkins-spectral-mixture-gp.svg', directory='\writeDiagramsDir/gp')}

\figure{\includediagram{\diagramsDir/gp/box-jenkins-spectral-mixture-gp}{80%}}{Spectral mixture GP as applied to the Box-Jenkins airline data.}{box-jenkins-spectral-mixture-gp}

\endif
