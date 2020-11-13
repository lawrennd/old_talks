\ifndef{nigerianCovidData}
\define{nigerianCovidData}
\editme

\section{Nigerian COVID Data}

\newslide{Nigerian COVID Data: Notebook}

\notes{At the beginning of the COVID-19 outbreak, the Consortium for Arican COVID-19 Data formed to bring together data from across the African continent on COVID-19 cases [@Marivate-covid20]. These cases are recorded in the following github repository: <https://github.com/dsfsi/covid19africa>.}

\notes{For ease of use we've packaged this data set in the `pods` library}

\include{_data-science/includes/pods-software.md}

\code{data = pods.datasets.nigerian_covid()['Y']
data.head()}

\notes{Alternatively you can access the data directly with the following commands.

```{.python}
import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/dsfsi/covid19africa/master/data/line_lists/line-list-nigeria.csv')
data = pd.read_csv('line-list-nigeria.csv'))
```
}


\notes{Once it is loaded in the data can be summarized using the `describe` method in pandas.}

\code{data.describe()}


\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plt.big_wide_figsize)
ax.plot()
ax.set_xlabel()
ax.set_ylabel()

mlai.write_figure('nigerian-covid-data.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/nigerian-covid-data}{80%}}{Evolution of COVID-19 cases in Nigeria.}{nigerian-covid-data}

\endif
