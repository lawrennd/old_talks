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

\notes{Revert `matplotlib` version on Google Colab due to bug mentioned [here](https://github.com/facebook/prophet/issues/1691).}

\code{%pip uninstall --yes matplotlib}
\code{%pip install matplotlib==3.1.3}

\include{_ads/includes/ads-notebook-setup.md}

\include{_maps/includes/mapping-intro.md}

\notes{With all of this in mind, mapping data seems an appropriate domain in which to explore how we can assess a data set for use in a particular data science domain.}

\notes{In this practical session, you will learn how to download data from OpenStreetMap, in particular we will focus on *points of interest* in OpenStreetMap. We will explore the utility of points of interest as a way of adding features into our models. We will introduce the notion of a basis function. In spatial data the basis functions we use will become features on the landscape.}

\notes{Before we start, we'll introduce a few other ideas to inspire how you think about the data you collage. In particular, a tool for creating "play data" and we'll introduce you to the interactive funcitonality of the notebook.}

\include{_data-science/includes/drawdata-play.md}
\include{_data-science/includes/dataframe-interact.md}

\include{_maps/includes/mapping-intro.md}
\include{_maps/includes/open-street-map.md}

\include{_ml/includes/radial-basis.md}

\thanks

\references
