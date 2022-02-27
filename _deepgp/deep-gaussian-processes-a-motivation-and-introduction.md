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

talk-macros.gpp}i/includes/the-fourth-industrial-revolution-intro.md}
\installcode{mlai}
\installcode{notutils}
talk-macros.gpp}l/includes/what-is-ml.md}
talk-macros.gpp}l/includes/what-does-machine-learning-do.md}
talk-macros.gpp}l/includes/deep-learning-overview.md}
talk-macros.gpp}eepnn/includes/deep-neural-network.md}
talk-macros.gpp}i/includes/sedolian-voids.md}
talk-macros.gpp}l/includes/why-uncertainty.md}
talk-macros.gpp}p/includes/gp-intro-very-short.md}
talk-macros.gpp}p/includes/mackay-bathwater.md}

\newslide{Deep Neural Network}

\slides{\includediagram{\diagramsDir/deepgp/deep-nn2}{50%}}
talk-macros.gpp}eepgp/includes/overfitting-low-rank.md}
talk-macros.gpp}eepgp/includes/deep-gp.md}
talk-macros.gpp}eepgp/includes/stochastic-process-composition.md}
talk-macros.gpp}eepgp/includes/process-composition.md}

\section{Deep Gaussian Processes}
\centerdiv{\andreasDamianouPicture{15%}}
  @Damianou:thesis2015

\installcode{mlai}
talk-macros.gpp}p/includes/planck-cmp-master-gp.md}

\subsection{Modern Review}

* *A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation*
  @Thang:unifying17

* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
  @Damianou:thesis2015

talk-macros.gpp}eepgp/includes/deep-gp-setup-code.md}
talk-macros.gpp}eepgp/includes/olympic-marathon-deep-gp.md}
talk-macros.gpp}eepgp/includes/step-function-deep-gp.md}
talk-macros.gpp}eepgp/includes/motorcycle-helmet-deep-gp.md}

talk-macros.gpp}eepgp/includes/mnist-digits-subsample-deep-gp.md}

talk-macros.gpp}eepgp/includes/deep-neural-networks-as-point-estimates.md}
talk-macros.gpp}ealth/includes/deep-health-model.md}

\thanks

\references

