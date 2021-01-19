---
title: "R250: Gaussian Processes Introduction"
abstract: >
  In this talk we give an introduction to Gaussian processes for students who are interested in working with GPs for the the R250 module. 
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
reveal: True
ipynb: True
date: 2020-01-24
venue: Computer Lab, University of Cambridge
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

\include{talk-macros.gpp}
\include{_physics/includes/laplace-portrait.md}
\include{_physics/includes/laplaces-determinism.md}
\include{_gp/includes/gp-intro-very-short.md}
\include{_gp/includes/what-is-a-gp.md}

\subsection{Extensions}
\slides{
* Approximate inference [e.g. @Nickisch:approximations08]
* Large Data [e.g. @Thang:unifying17;@Hensman:bigdata13]
* Multiple outputs [e.g. @Alvarez:vector12]
* Bayesian optimisation [e.g. @Snoek:practical12]
* Deep GPs [e.g. @Damianou:deepgp13]
}
\notes{We'll cover extensions to Gaussian processes including approximate inference in non Gaussian models, large data [@Thang:unifying17;@Hensman:bigdata13], multiple output GPs [@Alvarez:vector12], Bayesian optimisation [@Snoek:practical12] and Deep GPs [@Damianou:deepgp13].}

\thanks

\references

