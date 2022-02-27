---
layout: talk
title: "Deep GPs"
abstract: >
  In this talk we introduce deep Gaussian processes, an approach to stochastic process modelling that relies on the composition of individual stochastic proceses.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
venue: Virtual Gaussian Process Summer School
ipynb: true
youtube: apq-hrzB-sM
date: 2020-09-16
transition: None
---

talk-macros.gpp}lk-macros.tex}


\section{Deep Gaussian Processes}

\setupcode{# Download some utilty files}
\downloadcode{mlai.plot}
\downloadcode{mlai}
\downloadcode{gp_tutorial}
\downloadcode{deepgp_tutorial}
\setupcode{import os
for path in ['gp', 'datasets', 'deepgp']:
    if not os.path.exists(path):
        os.mkdir(path)}
		
talk-macros.gpp}ata-science/includes/pods-install.md}
talk-macros.gpp}p/includes/gpy-install.md}
talk-macros.gpp}eepgp/includes/pydeepgp-include.md}


talk-macros.gpp}p/includes/planck-cmp-master-gp.md}

talk-macros.gpp}p/includes/approximate-gps-short.md}

\subsection{Modern Review}

* *A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation*
    @Thang:unifying17

* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
    @Damianou:thesis2015

talk-macros.gpp}eepgp/includes/deep-gaussian-processes.md}

\thanks

\references


