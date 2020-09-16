\ifndef{motorcycleHelmetGp}
\define{motorcycleHelmetGp}

\include{_ml/includes/motorcycle-helmet-data.md}

\editme

\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='time', ylabel='acceleration/$g$', fontsize=20, portion=0.5)
xlim=(-20,80)
ylim=(-180,120)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig,filename='\writeDiagramsDir/gp/motorcycle-helmet-gp.svg', 
            transparent=True, frameon=True)}


\subsection{Motorcycle Helmet Data GP}

\figure{\includediagram{\diagramsDir/gp/motorcycle-helmet-gp}{80%}}{Gaussian process fit to the motorcycle helmet accelerometer data.}{motorcycle-helmet-gp}

\endif
