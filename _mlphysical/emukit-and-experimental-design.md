---
week: 4
session: 2
layout: lecture
title: "Emukit and Experimental Design"
abstract: >
  We have introduced you to the sequential process by which we decide to evaluation points in a simulation through Bayesian optimization. In this lecture we introduce Emukit. Emukit is a software framework for decision programming via surrogage modelling and emulation. It formalizes the process of selecting a point via an acquisition function and provides a general framework for incorporating surrogate models and the acquisition function of your choice.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
layout: lecture
time: "10:00"
date: 2021-11-02
ipynb: true
reveal: true
youtube: 0nxa8TOmWB0
transition: None
---


\include{_mlphysical/includes/mlphysical-notebook-setup.md}
\include{_uq/includes/uq-sampling-history-doe.md}
\include{_software/includes/emukit-software.md}
\include{_uq/includes/emukit-vision.md}
\include{_uq/includes/emukit-tutorial.md}


\notes{This introduction is based on [An Introduction to Experimental Design with Emukit](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-experimental-design-introduction.ipynb) written by Andrei Paleyes and Maren Mahsereci.}

\include{_uq/includes/model-free-experimental-design.md}

\include{_uq/includes/emukit-experimental-design.md}

\subsection{Conclusions}

\notes{We've introduced the Emukit software and outlined its design philosophy. We've then performed some simple examples using Emukit to perform *experimental design* as a task. In particular we saw how we could define the task as an acquisition funciton, a loop, an emulator model and a target function.

You can compare the design of this software with its predecessor, `GPyOpt`, which is less modular in its design, and more focussed on Bayesian optimization.}

\slides{* Emukit software.
* Example around experimental design.
* Sequential decision making with acquisiton functions.
* Generalizes from the BayesOpt process (e.g. `GPyOpt`)
}

\thanks

\reading

\references
