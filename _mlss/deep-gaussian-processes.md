---
title: Deep Gaussian Processes
abstract: >
  Gaussian process models provide a flexible, non-parametric approach to modelling that sustains uncertainty about the function. 
  
  However, computational demands and the joint Gaussian assumption make them inappropriate for some applications. In this talk we review low rank approximations for Gaussian processes and use stochastic process composition to create non-Gaussian processes. 
  
  We illustrate the models on simple regression tasks to give a sense of how uncertainty propagates through the model. We end will demonstrations on unsupervised learning of digits and motion capture data.
ipynb: 2019-01-11-deep-gaussian-processes.ipynb
reveal: 2019-01-11-deep-gaussian-processes.slides.html
youtube: b635kuSqLww
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
date: 2019-01-11
venue: MLSS, Stellenbosch, South Africa
transition: None
---
<!--define{draft}-->
\include{talk-macros.tex}

\section{Introduction}

\notes{In the previous session on Gaussian processes, we introduced the Gaussian process model and the covariance function. In this session we are going to address two challenges of the Gaussian process. Firstly, we look at the computational tractability and secondly we look at extending the nature of the process beyond Gaussian.}

\include{_gp/includes/planck-cmp-master-gp.md}

\section{Low Rank Gaussian Processes}

\include{_gp/includes/approximate-gps-short.md}
\include{_gp/includes/gp-big-data-technical.md}
\include{_gp/includes/gp-big-data.md}

\newslide{Modern Review}

* *A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation*
    @Thang:unifying17

* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
    @Damianou:thesis2015

\include{_deepgp/includes/deep-gaussian-processes.md}

\newslide{From NIPS 2017}

* *Gaussian process based nonlinear latent structure discovery in multivariate spike train data*
    @Anqi:gpspike2017
* *Doubly Stochastic Variational Inference for Deep Gaussian Processes*
    @Salimbeni:doubly2017
* *Deep Multi-task Gaussian Processes for Survival Analysis with Competing Risks*
    @Alaa:deep2017
* *Counterfactual Gaussian Processes for Reliable Decision-making and What-if Reasoning*
    @Schulam:counterfactual17


\newslide{Some Other Works}

* *Deep Survival Analysis*
    @Ranganath-survival16
* *Recurrent Gaussian Processes*
    @Mattos:recurrent15
* *Gaussian Process Based Approaches for Survival Analysis*
    @Saul:thesis2016

\include{_ml/includes/process-emulation.md}
\include{_uq/includes/emukit-playground.md}
\include{_uq/includes/uncertainty-quantification.md}
\include{_uq/includes/emukit-software.md}
\include{_ml/includes/mxfusion-software.md}

\subsection{Long term Aim}

* Simulate/Emulate the components of the system.
    * Validate with real world using multifidelity.
	* Interpret system using e.g. sensitivity analysis.
* Perform end to end learning to optimize.
    * Maintain interpretability.

\newslide{Acknowledgments}

Stefanos Eleftheriadis, John Bronskill, Hugh Salimbeni, Rich Turner, Zhenwen Dai, Javier Gonzalez, Andreas Damianou, Mark Pullin, Eric Meissner.


\newslide{Thanks!}

* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)

\subsection{References}

