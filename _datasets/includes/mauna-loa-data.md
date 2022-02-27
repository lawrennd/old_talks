\ifndef{maunaLoaData}
\define{maunaLoaData}

\editme

\subsection{Mauna Loa Data}

\notes{The Mauna Loa data consists of monthly mean carbon dioxide measured at Mauna Loa Observatory, Hawaii. According to the website, <https://www.esrl.noaa.gov/gmd/ccgg/trends/>.

> The carbon dioxide data on Mauna Loa constitute the longest record of direct measurements of CO2 in the atmosphere. They were started by C. David Keeling of the Scripps Institution of Oceanography in March of 1958 at a facility of the National Oceanic and Atmospheric Administration [@Keeling-atmospheric76]. NOAA started its own CO2 measurements in May of 1974, and they have run in parallel with those made by Scripps since then [@Thoning-atmospheric89].}

talk-macros.gpp}ata-science/includes/pods-install.md}

\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.mauna_loa()}

\notes{Here, if you've downloaded the data before you have a cached version. To download a fresh version of the data I can set `refresh_data=True`.}

\code{data = pods.datasets.mauna_loa(refresh_data=True)
x = data['X']
y = data['Y']

offset = y.mean()
scale = np.sqrt(y.var())}

\notes{The data dictionary contains the standard keys 'X' and 'Y' which give a unidimensional regression problem.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{xlim = (1950,2020)
ylim = (310, 420)
yhat = (y-offset)/scale

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=2)
ax.set_xlabel('year')
ax.set_ylabel('CO$_2$ concentration in ppm')
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(filename='mauna-loa.svg', 
				  directory='\writeDiagramsDir/datasets')}

\newslide{Mauna Loa Data}

\figure{\includediagram{\diagramsDir/datasets/mauna-loa}{80%}}{Mauna Loa data shows carbon dioxide monthly average measurements from the Mauna Loa Observatory in Hawaii.}{mauna-loa}


\notes{Additionally there are keys `Xtest` and `Ytest` which provide test data. The number of points considered to be *training data* is controlled by the argument `num_train` argument, which defaults to 545. This number is chosen as it matches that used in the [Gaussian Processes for Machine Learning](http://www.gaussianprocess.org/gpml/chapters/RW5.pdf) book [@Rasmussen:book06, Chapter 5]. Below we plot the test and training data.}

\code{xtest = data['Xtest']
ytest = data['Ytest']
ytesthat = (ytest-offset)/scale}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=2)
_ = ax.plot(xtest, ytest, 'g.',markersize=2)
ax.set_xlabel('year')
ax.set_ylabel('CO$_2$ concentration in ppm')
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(filename='mauna-loa-test.svg', 
				  directory='\writeDiagramsDir/datasets')}
				  
\newslide{Mauna Loa Test Data}

\figure{\includediagram{\diagramsDir/datasets/mauna-loa-test}{80%}}{Mauna Loa test data shows carbon dioxide monthly average measurements from the Mauna Loa Observatory in Hawaii.}{mauna-loa-test}

\notes{Of course we have included the citation information for the data.}

\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys `info` and `details`.}

\code{print(data['info'])
print()
print(data['details'])}

\notes{And, importantly, for reference you can also check the license for the data:}

\code{print(data['license'])}

\endif
