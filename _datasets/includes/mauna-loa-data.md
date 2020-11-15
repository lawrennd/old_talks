\ifndef{maunaLoaData}
\define{maunaLoaData}

\editme

\subsection{Mauna Loa Data}

\notes{The Mauna Loa data consists of monthly mean carbon dioxide measured at Mauna Loa Observatory, Hawaii. According to the website, <https://www.esrl.noaa.gov/gmd/ccgg/trends/>.

> The carbon dioxide data on Mauna Loa constitute the longest record of direct measurements of CO2 in the atmosphere. They were started by C. David Keeling of the Scripps Institution of Oceanography in March of 1958 at a facility of the National Oceanic and Atmospheric Administration [@Keeling-atmospheric76]. NOAA started its own CO2 measurements in May of 1974, and they have run in parallel with those made by Scripps since then [@Thoning-atmospheric89].}

\include{_data-science/includes/pods-install.md}

\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.mauna_loa()
x = data['X']
y = data['Y']

offset = y.mean()
scale = np.sqrt(y.var())}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{xlim = (1950,2020)
ylim = (310, 420)
yhat = (y-offset)/scale

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('CO2 ppm', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(figure=fig, 
                  filename='mauna-loa.svg', 
				  diagrams='\writeDiagramsDir/datasets')}

\newslide{Mauna Loa Data}

\figure{\includediagram{\diagramsDir/datasets/mauna-loa}{80%}}{Mauna Loa data shows carbon dioxide monthly average measurements from the Mauna Loa Observatory in Hawaii.}{mauna-loa}

\notes{The data set was used as a demonstration of model selection for Gaussian processes in @Rasmussen:book06 (Chapter 5).}

\addreading{@Rasmussen:book06}{Chapter 5}

\endif
