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

\setupcode{import pods}

\code{data = pods.datasets.kepler_lightcurves()}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai.mlai as ma}

\plotcode{num_stars = 3
for star in stars[0:num_stars]:
  for dataset in stars[star]:
    fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
    data = pd.DataFrame(Y)[star][dataset]
    ax.plot(data["TIME"], data["SAP_FLUX"])
    ax.set_xlabel("Barycentric Julian Date (d)")
    ax.set_ylabel("SAP Flux (instrumental units)")
    ax.set_title("Star {star}, Dataset {dataset}".format(star=star, dataset=dataset))
	ma.write_figure("kepler-lightcurve-data-{star}-{dataset}.svg".format(star=star,dataset=dataset), directory='\writeDiagramsDir/datasets')
}

\figure{\includediagram{\diagramsDir/datasets/kepler-lightcurve-data-001720554-2009350155506}{60%}}{Light curve from star 001720554.}{kepler-lightcurve-data-001720554}


\endif
