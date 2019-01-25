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

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
_ = ax.set_xlabel('time', fontsize=20)
_ = ax.set_ylabel('acceleration', fontsize=20)
xlim = (-20, 80)
ylim = (-175, 125)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(filename='../slides/diagrams/datasets/motorcycle-helmet.svg', 
            transparent=True, frameon=True)}

\subsection{Motorcycle Helmet Data}

\includediagram{../slides/diagrams/datasets/motorcycle-helmet}

\endif
