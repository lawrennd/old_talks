---
layout: talk
title: "Deep Gaussian Processes: A Motivation and Introduction"
abstract: >
  Modern machine learning methods have driven significant advances in
  artificial intelligence, with notable examples coming from Deep
  Learning, enabling super-human performance in the game of Go and
  highly accurate prediction of protein folding e.g. AlphaFold. In
  this talk we look at deep learning from the perspective of Gaussian
  processes. Deep Gaussian processes extend the notion of deep
  learning to propagate uncertainty alongside function values. We’ll
  explain why this is important and show some simple examples.
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


<!--https://twitter.com/demishassabis/status/1453794436056502274?s=20 -->


\section{Introduction}

\include{_ai/includes/the-fourth-industrial-revolution-intro.md}
\installcode{mlai}
\include{_ml/includes/what-is-ml.md}
\include{_gp/includes/mackay-bathwater.md}
\include{_ml/includes/deep-learning-overview.md}
\include{_deepnn/includes/deep-neural-network.md}
\include{_ml/includes/why-uncertainty.md}
\include{_gp/includes/gp-intro-very-short.md}

\include{_deepgp/includes/overfitting-low-rank.md}
\include{_deepgp/includes/deep-gp.md}
\include{_deepgp/includes/stochastic-process-composition.md}
\include{_deepgp/includes/process-composition.md}

\section{Deep Gaussian Processes}
\centerdiv{\andreasDamianouPicture{15%}}
  @Damianou:thesis2015

\installcode{mlai}
\include{_gp/includes/planck-cmp-master-gp.md}

\subsection{Modern Review}

* *A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation*
  @Thang:unifying17

* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
  @Damianou:thesis2015

\include{_deepgp/includes/deep-gp-setup-code.md}
\include{_deepgp/includes/olympic-marathon-deep-gp.md}
\include{_deepgp/includes/step-function-deep-gp.md}
\include{_deepgp/includes/motorcycle-helmet-deep-gp.md}

\include{_deepgp/includes/mnist-digits-subsample-deep-gp.md}
\include{_health/includes/deep-health-model.md}

\thanks

\references

