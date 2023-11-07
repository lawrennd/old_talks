\ifndef{ceresData}
\define{ceresData}

\editme

\notes{This data set consists of obervations of the [dwarf planet Ceres](http://en.wikipedia.org/wiki/Ceres_(dwarf_planet)) collected by [Guiseppe Piazzi](http://en.wikipedia.org/wiki/Giuseppe_Piazzi) from 1st January 1801 to 11th February 1801. The data was published in the September 1801 edition of [Monatliche Correspondenz](http://de.wikipedia.org/wiki/Monatliche_Correspondenz), a volume of astronomical correspondence edited by [Franz Xaver von Zach](http://en.wikipedia.org/wiki/Franz_Xaver_von_Zach), the Hungarian astronomer who, with the aid of orbital predictions from a 24 year old [Carl Friederich Gauss](http://en.wikipedia.org/wiki/Carl_Friedrich_Gauss), was able to recover the 'lost planet' in early 1802.}

\subsection{Monatliche Correspondenz}

\notes{First, here is the volume where the data was originally published [@Piazzi:monatliche1801].}

\includegooglebook{JBw4AAAAMAAJ}{GBS.PA280}

\notes{The data can be accessed as a `pandas` data frame through}

\setupcode{import pods}

\code{data = pods.datasets.ceres()['data']
data.describe()}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax =plt.subplots(figsize=plt.big_figsize)
right_ascension = data['Gerade Aufstiegung in Graden']
declination = data['Geocentrische Laenger']

ax.plot(right_ascension, declination, 'rx')
ax.set_xlabel('right ascension')
ax.set_ylabel('declination')

mlai.write_figure('ceres-data.svg', directory='\writeDiagramsDir/datasets')}

\figure{\includediagram{\diagramsDir/datasets/ceres-data}{60%}}{The observations that Giuseppe Piazzi made of Ceres.}{ceres-data}

\subsection{Gauss's Prediction}

\notes{And you can now attempt to make a prediction, as Gauss did, of the orbital position of the dwarf planet in late 1801 [@Gauss:monatliche1801].}

\includegooglebook{JBw4AAAAMAAJ}{GBS.PA647}

\notes{The [Dawn Mission](http://en.wikipedia.org/wiki/Dawn_%28spacecraft%29) arrived at at Ceres in April 2015. [Here](http://astronomynow.com/2015/05/11/ceres-mysterious-white-spots-resolved-in-latest-dawn-images/) is a report from Astronomy Now showing a set of images from May 2015.}

\endif
