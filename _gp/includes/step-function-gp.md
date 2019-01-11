\ifndef{stepFunctionGp}
\define{stepFunctionGp}
\editme
\include{_ml/includes/step-function-data.md}

\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\plotcode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)

mlai.write_figure(figure=fig,filename='../../slides/diagrams/gp/step-function-gp.svg', 
            transparent=True, frameon=True)}
			
\subsection{Step Function Data GP}

\includesvg{../slides/diagrams/gp/step-function-gp.svg} 

\endif
