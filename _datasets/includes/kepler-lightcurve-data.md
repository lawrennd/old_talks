\ifndef{keplerLightCurveData}
\define{keplerLightCurveData}

\editme

\subsection{Kepler Lightcurve Data}


\notes{This data set is from the Kepler Telescope. it was used by David W. Hogg and Kate Storey-Fisher in their NeurIPS Tutorial "Machine Learning for Astrophysics and Astrophysics Problems for Machine Learning".}

\notes{Their notebook associated with the tutorial can be found here: <https://colab.research.google.com/drive/1TimsiQhhcK6qX_lD951H-WJDHd92my61>.}

\notes{From their tutorial:

* This is an introduction to working with time-series data.
* Here we obtain a set of stellar photometry (light curves) from the NASA Kepler Mission.
* This is just a tiny teaser: There are more than a hundred thousand stars observed, and most light curves span 4 years!}

\setupcode{import pandas as pd
import pods}

\code{data = pods.datasets.kepler_lightcurves()}

\notes{In `pods` the data is returned with the usual additional information, and also the field "stars" which includes which stars are in the data set.}

\code{print(data["scans"])}

\notes{We can plot the first few stars for visualization.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai.mlai as ma}

\plotcode{num_stars_plot = 3
count = 0
scan = data["Y"].columns[0]
for star, X in data["Y"][scan].items():
    count += 1
    fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
    ax.plot(X["TIME"], X["SAP_FLUX"])
    ax.set_xlabel("Barycentric Julian Date (d)")
    ax.set_ylabel("SAP Flux (instrumental units)")
    ax.set_title("Star {star}".format(star=star))
    ma.write_figure("kepler-lightcurve-data-{star}.svg".format(star=star), directory='./datasets')
    if count > num_stars_plot:
        break}

\figure{\includediagram{\diagramsDir/datasets/kepler-lightcurve-data-001720554}{60%}}{Light curve from star 001720554.}{kepler-lightcurve-data-001720554}


\notes{In the notebook associated with their tutorial, Storey-Fisher and Hogg note that barycentric time is different from earth centric time, to illustrate, the plot the differences between time values for two different stars in the same data set, showing that over time, despite the Earth-centric time staying the same, the barycentric time is varying for the two different stars.}

\code{star0 = data["scans"][scan][0]
star1 = data["scans"][scan][1]

X0 = data["Y"][scan][star0]
X1 = data["Y"][scan][star1]}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X0["TIME"], X1["TIME"] - X0["TIME"], linewidth=3)
ax.set_xlabel("Barycentric Julian Date (d)")
ax.set_ylabel("Time differences (d)")
_ = ax.set_title("Barycentric time is freaky")
ma.write_figure("barycentric-time-difference.svg", directory='./datasets')}

\figure{\includediagram{\diagramsDir/datasets/barycentric-time-difference}{60%}}{Difference between Barycentric time values for stars 001720554 and star.}{barycentric-time-difference}


\endif
