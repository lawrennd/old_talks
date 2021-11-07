---
week: 6
title: "Practical Two"
abstract:  >
  In this practical session we look at the second aspect of the Fynesse data science process, *assess*. In particular, we are going to download data from OpenStreetMap and verify its quality and utility.
layout: notebook
venue: Intel Lab, William Gates Building
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
time: "15:00"
date: 2021-11-16
transition: None
reveal: false
ipynb: true
---
 
\subsection{Revert Matplotlib Version}

\notes{Revert `matplotlib` version on colab due to bug mentioned [here](https://github.com/facebook/prophet/issues/1691).}
\code{%pip uninstall --yes matplotlib}
\code{%pip install matplotlib==3.1.3}
\include{_maps/includes/mapping-intro.md}

\include{_maps/includes/open-street-map.md}


\notes{Next we convert the geodataframe of tourist places we've downloaded to a DataFrame}

\include{_ml/includes/basis-functions.md}

\addreading{@Rogers:book11}{Section 1.4}
\addreading{@Bishop:book06}{Chapter 1, pg 1-6}
\addreading{@Bishop:book06}{Chapter 3, Section 3.1 up to pg 143}

\subsection{Lecture on Basis Functions from GPRS Uganda}

\figure{\includeyoutube{PoNbOnUnOao}{600}{450}}{Lecture on Basis functions from GPRS in Uganda in 2013.}{basis-functions-gprs-uganda}


\notes{Then we create basis functions of different widths on the map, and look at tourist hotspots.}



\thanks

\references
