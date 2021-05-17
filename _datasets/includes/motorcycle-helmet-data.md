\ifndef{motorcycleHemletData}
\define{motorcycleHelmetData}
\editme

\setupcode{import pods}

\code{data = pods.datasets.mcycle()
x = data['X']
y = data['Y']
scale=np.sqrt(y.var())
offset=y.mean()
yhat = (y - offset)/scale}

\setupdisplaycode{import mlai.plot as plot
import mlai.mlai as ma
import matplotlib.pyplot as plt}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
_ = ax.set_xlabel('time', fontsize=20)
_ = ax.set_ylabel('acceleration', fontsize=20)
xlim = (-20, 80)
ylim = (-175, 125)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ma.write_figure(filename='motorcycle-helmet.svg', directory='\writeDiagramsDir/datasets/',
            transparent=True, frameon=True)}

\subsection{Motorcycle Helmet Data}

\figure{\includediagram{\diagramsDir/datasets/motorcycle-helmet}{80%}}{Motorcycle helmet data. The data consists of acceleration readings on a motorcycle helmet undergoing a collision. The data exhibits heteroschedastic (time varying) noise levles and non-stationarity.}{motorcycle-helment-data}

\endif
