---
layout: slides
title: "Introduction to Deep Gaussian Processes"
author: Neil D. Lawrence
abstract: >
  In this talk we introduce deep Gaussian processes, describe what they are and what they are good for. Deep Gaussian process models make use of stochastic process composition to combine Gaussian processes together to form new models which are non-Gaussian in structure. They serve both as a theoretical model for deep learning and a functional model for regression, classification and unsupervised learning. The challenge in these models is propagating the uncertainty through the process.
ipynb: True
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-09-10
venue: Gaussian Process Summer School, University of Sheffield, UK
transition: None
---

\include{talk-macros.tex}

\ifdef{SLIDES}
\define{pydeepgpInclude}
\endif
\define{deepRobotWireless}

\subsection{Deep Gaussian Processes}


* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
    @Damianou:thesis2015

\include{_deepgp/includes/deep-gaussian-processes.md}

\thanks

\references
