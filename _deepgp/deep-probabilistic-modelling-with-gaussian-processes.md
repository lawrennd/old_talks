---
layout: slides
title: "Deep Probabilistic Modelling with with Gaussian Processes"
abstract: >
  Neural network models are algorithmically simple, but mathematically complex. Gaussian process models are mathematically simple, but algorithmically complex. In this tutorial we will explore Deep Gaussian Process models. They bring advantages in their mathematical simplicity but are challenging in their algorithmic complexity. We will give an overview of Gaussian processes and highlight the algorithmic approximations that allow us to stack Gaussian process models: they are based on variational methods. In the last part of the tutorial will explore a use case exemplar: uncertainty quantification. We end with open questions.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
venue: NIPS Tutorial 2017
youtube: NHTGY8VCinY
transition: None
bibliography: deep-probabilistic-modelling-with-gaussian-processes.bib
---

\include{talk-macros.tex}
\include{_gp/includes/what-is-a-gp.md}


### Deep Gaussian Processes 

\include{_gp/includes/approximate-gps-short.md}

### Modern Review

* *A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation*
    @Thang:unifying17

* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
    @Damianou:thesis2015

\include{_deepgp/includes/deep-gaussian-processes.md}

### At this Year's NIPS

* *Gaussian process based nonlinear latent structure discovery in multivariate spike train data*
    @Anqi:gpspike2017
* *Doubly Stochastic Variational Inference for Deep Gaussian Processes*
    @Salimbeni:doubly2017
* *Deep Multi-task Gaussian Processes for Survival Analysis with Competing Risks*
    @Alaa:deep2017
* *Counterfactual Gaussian Processes for Reliable Decision-making and What-if Reasoning*
    @Schulam:counterfactual17


### Some Other Works

* *Deep Survival Analysis*
    @Ranganath-survival16
* *Recurrent Gaussian Processes*
    @Mattos:recurrent15
* *Gaussian Process Based Approaches for Survival Analysis*
    @Saul:thesis2016

\include{_uq/includes/uncertainty-quantification.md}

### Acknowledgments

Stefanos  Eleftheriadis, John Bronskill, Hugh Salimbeni, Rich Turner, Zhenwen Dai, Javier Gonzalez, Andreas Damianou, Mark Pullin.

### Ongoing Code

* Powerful framework but

* Software isn't there yet.

* Our focus: Gaussian Processes driven by MXNet

* Composition of GPs, Neural Networks, Other Models

### Thanks!

* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)

### References {.allowframebreaks}


