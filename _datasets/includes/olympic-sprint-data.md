\ifndef{olympicSprintData}
\define{olympicSprintData}

\editme

\subsection{Olympic Sprint Data}

\columns{
* Gold medal times for Olympic Sprints for Men and Women
* 100m, 200m, 400m
* In early years of olympics not all events run.
}{
\includejpg{\diagramsDir/ml/100m_final_start}{100%}
\smalltext{Image from Wikimedia Commons <http://bit.ly/16kMKHQ> by [Darren Wilkinson](https://www.staff.ncl.ac.uk/d.j.wilkinson/)}
}{70%}{30%}

talk-macros.gpp}ata-science/includes/pods-install.md}

\notes{The first think we will look at is a multiple output model. Our aim is to jointly model all *sprinting* events from olympics since 1896. Data is provided by Rogers & Girolami's "First Course in Machine Learning". Firstly, let's load in the data.}

\setupcode{import pods
import numpy as np}

\code{data = pods.datasets.olympic_sprints()
X = data['X']
y = data['Y']
print(data['info'], data['details'])}

\notes{When using data sets it's good practice to cite the originators of the data, you can get information about the source of the data from `data['citation']`}

\code{print(data['citation'])}

\notes{The data consists of all the male and female sprinting data for 100m, 200m and 400m since 1896 (six outputs in total). The output information can be found from: `data['output_info']`}

\code{print(data['output_info'])}

\notes{In `GPy` we deal with multiple output data in a particular way. We specify the output we are interested in for modelling as an additional *input*. So whilst for this data, normally, the only input would be the year of the event. We additionally have an input giving the index of the output we are modelling. This can be seen from examining `data['X']`.}

\code{print('First column of X contains the olympic years.')
print(data['X'][:, 0])
print('Second column of X contains the event index.')
print(data['X'][:, 1])}

\notes{Now let's plot the data}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
markers = ['bo', 'ro', 'bx', 'rx', 'bs', 'rs']
for i in range(6):
    # extract the event 
    x_event = X[np.nonzero(X[:, 1]==i), 0]
    y_event = y[np.nonzero(X[:, 1]==i), 0]
    ax.plot(x_event, y_event, markers[i])
ax.set_title('Olympic Sprint Times')
ax.set_xlabel('year')
ax.set_ylabel('time/s')

mlai.write_figure('olympic-sprint-data.svg', directory='\writeDiagramsDir/datasets')}

\newslide{Olympic Sprint Data}

\figure{\includediagram{\diagramsDir/datasets/olympic-sprint-data}{80%}}{Olympic sprint gold medal winning times from @Rogers:book11.}{olympic-sprint-data}

\notes{In the plot above red is women's events, blue is men's. Squares are 400 m, crosses 200m and circles 100m. Not all events were run in all years, for example the women's 400 m only started in 1964.}


\endif
