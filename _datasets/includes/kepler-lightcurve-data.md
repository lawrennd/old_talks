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


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai.mlai as ma}

\plotcode{num_stars = 3
count = 0
for star in data["data"]["Y"][0:num_stars]:
  for X in data["data"]["Y"][star]:
    count += 1
    fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
    ax.plot(X["TIME"], X["SAP_FLUX"])
    ax.set_xlabel("Barycentric Julian Date (d)")
    ax.set_ylabel("SAP Flux (instrumental units)")
    ax.set_title("Star {star}".format(star=star, dataset=dataset))
    ma.write_figure("kepler-lightcurve-data-{star}.svg".format(star=star), directory='./datasets')
    if count > num_stars:
        break
  if count > num_stars:
    break
}

\figure{\includediagram{\diagramsDir/datasets/kepler-lightcurve-data-001720554}{60%}}{Light curve from star 001720554.}{kepler-lightcurve-data-001720554}


\code{star0 = data["data"]["Y"].keys()[0]
star1 = data["data"]["Y"].keys()[1]

X0 = data["data"]["Y"][star0][0]
X1 = data["data"]["Y"][star1][0]}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X0["TIME"], X1["TIME"] - X0["TIME"], linewidth=3)
ax.set_xlabel("Barycentric Julian Date (d)")
ax.set_ylabel("Time differences (d)")
_ = ax.set_title("Barycentric time is freaky")
ma.write_figure("barycentric-time-difference.svg", directory='./datasets')}

\figure{\includediagram{\diagramsDir/datasets/barycentric-time-difference}{60%}}{Light curve from star 001720554.}{barycentric-time-difference}


\endif
