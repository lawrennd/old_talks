\ifndef{boxJenkinsAirlineData}
\define{boxJenkinsAirlineData}

\editme

\subsection{Box Jenkins Airline Passenger Data}

\notes{This data is giving airline passenger numbers between 1948 and 1960. It was published by @Box-timeseries76.}


\include{_data-science/includes/pods-install.md}

\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.boxjenkins_airline()
x = data['X']
y = data['Y']
xtest = data['Xtest']
ytest = data['Ytest']

offset = y.mean()
scale = np.sqrt(y.var())}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{xlim = (1948,1958)
ylim = (50, 400)
yhat = (y-offset)/scale

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=2)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('Passenger numbers', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

ax.set_xlabel('year')
ax.set_ylabel('thousands of passengers')

mlai.write_figure(filename='box-jenkins-airline.svg', 
				  directory='\writeDiagramsDir/datasets')}

\newslide{Mauna Loa Data}

\figure{\includediagram{\diagramsDir/datasets/box-jenkins-airline}{80%}}{Box-Jenkins data set on airline passenger numbers.}{box-jenkins-airline}


\endif
