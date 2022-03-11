---
title: "R250: Unsupervised Learning with Gaussian Processes I"
abstract: >
  In this talk we give an introduction to Unsupervised Learning and Gaussian processes for students who are interested in working with Unsupervised GPs for the the R250 module. 
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
reveal: True
ipynb: True
week: 1
session: 1
youtube: UNjOr0zwmTo
date: 2021-01-21
venue: Virtual (Zoom)
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
time: "10:00"
start: "10:00"
end: "11:00"
---

\include{talk-macros.gpp}

\include{_notebooks/includes/notebook-setup.md}
\include{_dimred/includes/high-dimensional-data.md}
\include{_dimred/includes/dimensionality-reduction-intro.md}

\subsection{Gaussian Variables and Linear Dimensionality Reduction}

\slides{* Return to non-linear shortly.
* Now: Linear dimensionality reduction.
* First: Review Gaussian density properties.}

\notes{We will return to non-linear dimensionality reduction approaches shortly, but first we're going to consider *linear* approaches to dimensionality reduction. To do so, we'll first review some characteristics of the Gaussian density.}

\include{_ml/includes/univariate-gaussian-properties.md}
\section{Linear Latent Variable Models}
\include{_ml/includes/multivariate-gaussian-properties.md}

\include{_dimred/includes/latent-variables.md}

\thanks

\references

