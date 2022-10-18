\ifndef{erichFriedmanPackingData}
\define{erichFriedmanPackingData}

\editme

\subsection{Erich Friedman Packing Data}

\include{_simulation/includes/packing-problems.md}

\include{_data-science/includes/pods-install.md}


\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.erich_friedman_packing_data()
x = data['X']
y = data['Y']}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\setupplotcode{import pods
from matplotlib import pyplot as plt}

\plotcode{
xlim = (0,100)
ylim = (0, 11)

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('n', fontsize=20)
ax.set_ylabel('s', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(filename='squares-in-squares.svg', 
				  directory='\writeDiagramsDir/datasets')}

\newslide{Erich Friedman Packing Data: Squares in Squares}

\figure{\includediagram{\diagramsDir/datasets/squares-in-squares}{80%}}{Plot of minimum side length known as a function of number of squares inside.}{squares-in-squares}

\endif
