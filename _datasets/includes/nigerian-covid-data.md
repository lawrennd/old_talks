\ifndef{nigerianCovidData}
\define{nigerianCovidData}
\editme

\section{Nigerian COVID Data}

\newslide{Nigerian COVID Data: Notebook}

\notes{At the beginning of the COVID-19 outbreak, the Consortium for African COVID-19 Data formed to bring together data from across the African continent on COVID-19 cases [@Marivate-covid20]. These cases are recorded in the following GitHub repository: <https://github.com/dsfsi/covid19africa>.}

\notes{For ease of use we've packaged this data set in the `pods` library}

\include{_software/includes/pods-software.md}

\setupcode{import pods}
\code{data = pods.datasets.nigerian_covid()['Y']
data.head()}

\notes{Alternatively, you can access the data directly with the following commands.

```{.python}
import urllib.request
import pandas as pd

urllib.request.urlretrieve('https://raw.githubusercontent.com/dsfsi/covid19africa/master/data/line_lists/line-list-nigeria.csv', 'line-list-nigeria.csv')
data = pd.read_csv('line-list-nigeria.csv', parse_dates=['date', 
                                                         'date_confirmation', 
														 'date_admission_hospital', 
														 'date_onset_symptoms',
														 'death_date'])
```
}


\notes{Once it is loaded in the data can be summarized using the `describe` method in pandas.}

\code{data.describe()}


\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
data['count_column'] = True
fig.autofmt_xdate(rotation=45)
ax.plot(data.date, data.count_column.cumsum())

ax.plot()
ax.set_xlabel('date')
ax.set_ylabel('case counts')

mlai.write_figure('nigerian-covid-data.svg', directory='\writeDiagramsDir/datasets')}

\figure{\includediagram{\diagramsDir/datasets/nigerian-covid-data}{80%}}{Evolution of COVID-19 cases in Nigeria.}{nigerian-covid-data}

\endif
