---
layout: talk
title: "Deep Gaussian Processes: A Motivation and Introduction"
title: "Deep GPs"
abstract: >
  Modern machine learning methods have driven significant advances in
  artificial intelligence, with notable examples coming from Deep
  Learning, enabling super-human performance in the game of Go and
  highly accurate prediction of protein folding e.g. AlphaFold. In
  this talk we look at deep learning from the perspective of Gaussian
  processes. Deep Gaussian processes extend the notion of deep
  learning to propagate uncertainty alongside function values. We’ll
  explain why this is important and show som simple examples.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
venue: LG Distinguished Talk
ipynb: true
date: 2021-11-04
transition: None
---


https://twitter.com/demishassabis/status/1453794436056502274?s=20

\section{Deep Gaussian Processes}

\setupcode{# Download some utilty files}
\downloadcode{teaching_plots}
\downloadcode{mlai}
\downloadcode{gp_tutorial}
\downloadcode{deepgp_tutorial}
\setupcode{import os
for path in ['gp', 'datasets', 'deepgp']:
    if not os.path.exists(path):
        os.mkdir(path)}
		
\include{_data-science/includes/pods-install.md}
\include{_gp/includes/gpy-install.md}
\include{_deepgp/includes/pydeepgp-include.md}


\include{_gp/includes/planck-cmp-master-gp.md}

\include{_gp/includes/approximate-gps-short.md}

\subsection{Modern Review}

* *A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation*
    @Thang:unifying17

* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
    @Damianou:thesis2015

\include{_deepgp/includes/deep-gaussian-processes.md}

\thanks

\references

