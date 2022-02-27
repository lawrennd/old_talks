\ifndef{olympic100mData}
\define{olympic100mData}

\editme

\subsection{Olympic 100m Data}

\columns{
*  Gold medal times for Olympic 100 m runners since 1896.
* One of a number of Olypmic data sets collected by @Rogers:book11.}{
\figure{\includejpg{\diagramsDir/ml/100m_final_start}{100%}}{Start of the 2012 London 100m race. *Image from Wikimedia Commons* <http://bit.ly/191adDC>}{100m-final-start}}{50%}{50%}


\notes{
The first thing we will do is load a standard data set for regression modelling. The data consists of the pace of Olympic Gold Medal 100m winners for the Olympics from 1896 to present. First we load in the data and plot.
}

talk-macros.gpp}ata-science/includes/pods-install.md}



\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.olympic_100m_men()
x = data['X']
y = data['Y']

offset = y.mean()
scale = np.sqrt(y.var())}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\setupplotcode{import pods
from matplotlib import pyplot as plt
%matplotlib inline}

\plotcode{
xlim = (1875,2030)
ylim = (9, 12)
yhat = (y-offset)/scale

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(filename='olympic-100m.svg', 
				  directory='\writeDiagramsDir/datasets')}

\newslide{Olympic 100m Data}

\figure{\includediagram{\diagramsDir/datasets/olympic-100m}{80%}}{Olympic 100m wining times since 1896.}{olympic-100m}

\endif
