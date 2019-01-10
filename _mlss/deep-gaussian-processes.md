---
title: Deep Gaussian Processes
abstract: >
  Classical machine learning and statistical approaches to learning, such as neural networks and linear regression, assume a parametric form for functions. Gaussian process models are an alternative approach that assumes a probabilistic prior over functions. This brings benefits, in that uncertainty of function estimation is sustained throughout inference, and some challenges: algorithms for fitting Gaussian processes tend to be more complex than parametric models. 
  
  In these sessions I will introduce Gaussian processes and explain why sustaining uncertainty is important. We’ll then look at some extensions of Gaussian process models, in particular composition of Gaussian processes, or deep Gaussian processes.
ipynb: 2019-01-11-deep-gaussian-processes.ipynb
reveal: 2019-01-11-deep-gaussian-processes.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-01-11
venue: MLSS, Stellenbosch, South Africa
transition: None
---
\define{draft}
\include{talk-macros.tex}

\include{_gp/includes/planck-cmp-master-gp.md}

\newslide{Deep Gaussian Processes}

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
\include{_uq/includes/emukit.md}
\include{_ml/includes/mxfusion.md}

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

