\ifndef{nigeriaNmisData}
\define{nigeriaNmisData}
\editme

\section{Nigeria NMIS Data}

\newslide{Nigeria NMIS Data: Notebook}

\notes{As an example data set we will use Nigerian Millennium Development Goals Information System Health Facility [@Nigeria-nmis14]. It can be found here <https://energydata.info/dataset/nigeria-nmis-education-facility-data-2014>.}

\notes{Taking from the information on the site, 

>The Nigeria MDG (Millennium Development Goals) Information System – NMIS health facility data is collected by the Office of the Senior Special Assistant to the President on the Millennium Development Goals (OSSAP-MDGs) in partner with the Sustainable Engineering Lab at Columbia University. A rigorous, geo-referenced baseline facility inventory across Nigeria is created spanning from 2009 to 2011 with an additional survey effort to increase coverage in 2014, to build Nigeria’s first nation-wide inventory of health facility. The database includes 34,139 health facilities info in Nigeria.
>
>The goal of this database is to make the data collected available to planners, government officials, and the public, to be used to make strategic decisions for planning relevant interventions.
>
>For data inquiry, please contact Ms. Funlola Osinupebi, Performance Monitoring & Communications, Advisory Power Team, Office of the Vice President at funlola.osinupebi@aptovp.org
>
>To learn more, please visit <http://csd.columbia.edu/2014/03/10/the-nigeria-mdg-information-system-nmis-takes-open-data-further/>
>
>Suggested citation: Nigeria NMIS facility database (2014), the Office of the Senior Special Assistant to the President on the Millennium Development Goals (OSSAP-MDGs) & Columbia University
}

\notes{For ease of use we've packaged this data set in the `pods` library}

\include{_software/includes/pods-software.md}

\code{data = pods.datasets.nigeria_nmis()['Y']
data.head()}

\notes{Alternatively, you can access the data directly with the following commands.

```{.python}
import urllib.request
urllib.request.urlretrieve('https://energydata.info/dataset/f85d1796-e7f2-4630-be84-79420174e3bd/resource/6e640a13-cab4-457b-b9e6-0336051bac27/download/healthmopupandbaselinenmisfacility.csv', 'healthmopupandbaselinenmisfacility.csv')

import pandas as pd
data = pd.read_csv('healthmopupandbaselinenmisfacility.csv')
```
}

\define{\nmisdatadownloaded}

\notes{Once it is loaded in the data can be summarized using the `describe` method in pandas.}

\code{data.describe()}

\notes{In python and the Jupyter notebook it is possible to see a list of all possible functions and attributes by typing the name of the object followed by `.<Tab>` for example in the above case if we type `data.<Tab>` it show the columns available (these are attributes in pandas dataframes) such as `num_nurses_fulltime`, and also functions, such as `.describe()`.}

\notes{For functions we can also see the documentation about the function by following the name with a question mark. This will open a box with documentation at the bottom which can be closed with the x button.}

\code{data.describe?}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(data.longitude, data.latitude, 'ro', alpha=0.01)
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')

mlai.write_figure('nigerian-health-facilities.png', directory='\writeDiagramsDir/ml')}

\figure{\includepng{\diagramsDir/ml/nigerian-health-facilities}{60%}}{Location of the over thirty-four thousand health facilities registered in the NMIS data across Nigeria. Each facility plotted according to its latitude and longitude.}{nigerian-health-facilities}

\endif
