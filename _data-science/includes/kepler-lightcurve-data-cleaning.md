\ifndef{keplerLightcurveDataCleaning}
\define{keplerLightcurveDataCleaning}


talk-macros.gpp}atasets/includes/kepler-lightcurve-data.md}

\editme

\subsection{Cleaning the Kepler Light Curve Data}

\notes{build a rectangular, normalized data block}

\code{n = len(data["Y"][dataset])
p = len(data["Y"][dataset][kepler_id0])}

\setupcode{import numpy as np}

\code{time = np.zeros((n, p))
flux = np.zeros((n, p))
for i, X in enumerate(data["Y"][dataset]):
  time[i] = X["TIME"]
  flux[i] = X["SAP_FLUX"] / np.nanmedian(X["SAP_FLUX"])
flux.shape, time.shape}


\notes{identify missing data}

\code{bad = np.logical_not(np.isfinite(flux) & np.isfinite(time))}

\code{acceptable = np.logical_not(np.sum(bad, axis=0) > n / 2)}

\notes{censor really bad stuff}

\code{time = time[:, acceptable]
flux = flux[:, acceptable]
bad = bad[:, acceptable]
flux.shape, time.shape}



\notes{Interpolate missing data using a PCA.

*Note*: This PCA won't scale to huge data.
For huge data, use the scikit-learn implementation of PCA.}

\code{flux[bad] = 1.
for iter in range(4): # magic 4
  u, s, v = np.linalg.svd(flux, full_matrices=False)
  k = 8 # arbitrarily use the first 8 components
  flux_svd = u[:, :k] * s[:k] @ v[:k]
  flux[bad] = flux_svd[bad]}



\plotcode{for i in [6, 7, 8, 9, 10]:
  kepler_id = data["datasets"][dataset][i]
  fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
  ax.plot(data["Y"][dataset][kepler_id]["TIME"], data["Y"][dataset][kepler_id]["SAP_FLUX"] / np.nanmedian(data["Y"][dataset][kepler_id]["SAP_FLUX"]), linewidth=2)
  ax.set_xlabel("Barycentric Julian Date (d)")
  ax.set_ylabel("SAP Flux (instrumental units)")
  ax.set_title("Cleaned Kepler ID {kepler_id}".format(kepler_id=kepler_id))
  
  for badt, badf in zip(time[i, bad[i]], flux[i, bad[i]]):
    ax.axvline(badt, color="r", alpha=0.3)
    ax.plot(badt, badf, "rx")
  ma.write_figure("kepler-lightcurve-data-clean-{kepler_id}.svg".format(kepler_id=kepler_id), directory='./datasets')}



\subsection{Do some experiments!}

- Run astropy box least squares?
- Run astropy Lomb-Scargle periodograms or non-uniform FFTs?
- De-trend using PCA or other fits?
- Download a much bigger sample and run ICA or other quasi-causal methods.


\endif
