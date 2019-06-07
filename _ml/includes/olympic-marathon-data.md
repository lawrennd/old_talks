\ifndef{olympicMarathonData}
\define{olympicMarathonData}
\subsection{Olympic Marathon Data}

\columns{
* Gold medal times for Olympic Marathon since 1896.
* Marathons before 1924 didn’t have a standardised distance.
* Present results using pace per km.
* In 1904 Marathon was badly organised leading to very slow times.
}{
\includejpg{../slides/diagrams/Stephen_Kiprotich}{100%}
\smalltext{Image from Wikimedia Commons <http://bit.ly/16kMKHQ>}
}{70%}{30%}

\notes{
The first thing we will do is load a standard data set for regression modelling. The data consists of the pace of Olympic Gold Medal Marathon winners for the Olympics from 1896 to present. First we load in the data and plot.
}

\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']

offset = y.mean()
scale = np.sqrt(y.var())}

\setupdisplaycode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\displaycode{
xlim = (1875,2030)
ylim = (2.5, 6.5)
yhat = (y-offset)/scale

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(figure=fig, 
                  filename='../slides/diagrams/datasets/olympic-marathon.svg', 
				  transparent=True, 
				  frameon=True)}

\newslide{Olympic Marathon Data}

\figure{\includediagram{../slides/diagrams/datasets/olympic-marathon}}{Olympic marathon pace times since 1892.}{olympic-marathon}

\notes{Things to notice about the data include the outlier in 1904, in this year, the olympics was in St Louis, USA. Organizational problems and challenges with dust kicked up by the cars following the race meant that participants got lost, and only very few participants completed. 

More recent years see more consistently quick marathons.}

\endif
