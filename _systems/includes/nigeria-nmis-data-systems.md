\ifndef{nigeriaNmisDataSystems}
\define{nigeriaNmisDataSystems}

\editme

\notes{
\subsection{Hospital Data}

The first and primary dataset we use is the NMIS health facility dataset, which contains data on the location, type, and staffing of health facilities across Nigeria. }

\notes{
\setupcode{import urllib.request
import pandas as pd}

\code{urllib.request.urlretrieve('https://energydata.info/dataset/f85d1796-e7f2-4630-be84-79420174e3bd/resource/6e640a13-cab4-457b-b9e6-0336051bac27/download/healthmopupandbaselinenmisfacility.csv', 'healthmopupandbaselinenmisfacility.csv')
hospital_data = pd.read_csv('healthmopupandbaselinenmisfacility.csv')}
}

\notes{It's always a good idea to inspect your data once it's downloaded to check it contains what you expect. In ```pandas``` you can do this with the ```.head()``` method. That allows us to see the first few entries of the ```pandas``` data structure.}

\notes{
\code{hospital_data.head()}
}

\notes{We can also check in ```pandas``` what the different columns of the data frame are to see what it contains. }

\notes{
\code{hospital_data.columns}
}

\notes{We can immiediately see that there are facility names, dates, and some characteristics of each health center such as number of doctors etc. As well as all that, we have two fields, ```latitude``` and ```longitude``` that likely give us the hospital locaiton. Let's plot them to have a look. }

\notes{
\setupcode{import matplotlib.pyplot as plt}

\code{plt.plot(hospital_data.longitude, hospital_data.latitude,'ro', alpha=0.01)}
}

\notes{There we have the location of these different hospitals. We set alpha in the plot to 0.01 to make the dots transparent, so we can see the locations of each health center.}


\endif
