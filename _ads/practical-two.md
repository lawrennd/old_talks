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


\thanks

\references
