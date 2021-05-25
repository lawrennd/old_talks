\ifndef{keplerLightcurveDataCleaning}
\define{keplerLightcurveDataCleaning}


\include{_datasets/includes/kepler-lightcurve-data.md}

\editme

\subsection{Cleaning the Kepler Light Curve Data}

\notes{build a rectangular, normalized data block}

\code{stars = data["stars"]
star0 = data["Y"].columns[0]
n = len(data["Y"].columns)
p = len(data["Y"][star0][stars[star0][0]])}

\setupcode{import numpy as np}

\code{time = np.zeros((n, p))
flux = np.zeros((n, p))
for i, star in enumerate(stars):
  dd = data["Y"][star][stars[star0][0]]
  time[i] = dd["TIME"]
  flux[i] = dd["SAP_FLUX"] / np.nanmedian(dd["SAP_FLUX"])
flux.shape, time.shape}


\notes{identify missing data}

\code{good = np.isfinite(flux * time) # hack: They both have to be finite
bad = np.logical_not(good) # I love this line
reallybad = np.sum(bad, axis=0) > n / 2
acceptable = np.logical_not(reallybad)}


\notes{censor really bad stuff}

\code{time = time[:, acceptable]
flux = flux[:, acceptable]
bad = bad[:, acceptable]
flux.shape, time.shape}



\notes{interpolate missing data using a PCA?
NOTE: This PCA won't scale to huge data.
      For huge data, use the scikit-learn implementation of PCA.}

\code{flux[bad] = 1.
for iter in range(4): # magic 4
  u, s, v = np.linalg.svd(flux, full_matrices=False)
  k = 8 # arbitrarily use the first 8 components
  flux_svd = u[:, :k] * s[:k] @ v[:k]
  flux[bad] = flux_svd[bad]}



\plotcode{for star in data["Y"].columns[[6, 7, 8, 9, 10]]:
  fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
  ax.plot(data["Y"][star][stars[star]][0]["TIME"], data["Y"][star][stars[star]][0]["SAP_FLUX"] / np.nanmedian(data["Y"][star][stars[star]][0]["SAP_FLUX"]), linewidth=2)
  for badt, badf in zip(time[i, bad[i]], flux[i, bad[i]]):
    ax.axvline(badt, color="r", alpha=0.3)
    ax.plot(badt, badf, "rx")
  ma.write_figure("kepler-lightcurve-data-clean-{star}.svg".format(star=star), directory='./datasets')}



\subsection{Do some experiments!}

- Run astropy box least squares?
- Run astropy Lomb-Scargle periodograms or non-uniform FFTs?
- De-trend using PCA or other fits?
- Download a much bigger sample and run ICA or other quasi-causal methods.


\endif
