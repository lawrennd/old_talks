---
layout: slides
title: "Deep Probabilistic Modelling with with Gaussian Processes"
author: Neil D. Lawrence
transition: None
bibliography: deep-probabilistic-modelling-with-gaussian-processes.bib
---

<!--Notes from Stefanos: Hey Neil, 

Just realised that there was no comment on the fact that a DGP is not a GP, only the current layer conditioned on all previous ones.

I don't know if you want to clarify that. I believe that the majority of the audience won't have that knowledge and they may leave with the wrong impression.

Although, I don't know where is the right time to introduce that in the talk.

Hope that's helpful.

Cheers,
Stefanos

Comments from Rich!


CMB samples -> Life
-->
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


