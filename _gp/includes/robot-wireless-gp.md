\ifndef{robotWirelessGp}
\define{robotWirelessGp}
\editme

\include{_ml/includes/robot-wireless-data.md}

\notes{Perform a Gaussian process fit on the data using GPy.}

\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, output_dim=output_dim, scale=scale, offset=offset, ax=ax, 
                  xlabel='time', ylabel='signal strength', fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='\writeDiagramsDir/gp/robot-wireless-gp-dim-' + str(output_dim)+ '.svg', 
            transparent=True, frameon=True)}

\subsection{Robot WiFi Data GP}

\figure{\includediagram{\diagramsDir/gp/robot-wireless-gp-dim-1}{80%}}{Gaussian process fit to the Robot Wireless dimension 1.}{robot-wireless-gp-dim-1}


\endif

