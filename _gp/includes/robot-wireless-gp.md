\ifndef{robotWirelessGp}
\define{robotWirelessGp}

\editme

talk-macros.gpp}atasets/includes/robot-wireless-data.md}

\subsection{Gaussian Process Fit to Robot Wireless Data}

\notes{Perform a Gaussian process fit on the data using GPy.}

\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\subsection{Robot WiFi Data GP}

\setupplotcode{from matplotlib import pyplot as plt
import mlai
import mlai.plot as plot}

\plotycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, output_dim=output_dim, scale=scale, offset=offset, ax=ax, 
                  xlabel='time', ylabel='signal strength', fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(filename='robot-wireless-gp-dim-' + str(output_dim)+ '.svg',
                  directory='\writeDiagramsDir/gp')}


\figure{\includediagram{\diagramsDir/gp/robot-wireless-gp-dim-1}{80%}}{Gaussian process fit to the Robot Wireless dimension 1.}{robot-wireless-gp-dim-1}


\endif

