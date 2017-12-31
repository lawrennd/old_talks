---
layout: slides
title: "Deep Probabilistic Modelling with with Gaussian Processes"
author: Neil D. Lawrence
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

\include{notation_def.tex}

\include{../_gp/includes/what-is-a-gp.md}


### Deep Gaussian Processes {data-transition="None"}

### Approximations {data-transition="None"}

<img src="../slides/diagrams/sparse-gps-1.png" align="center" width="90%" style="background:none; border:none; box-shadow:none;">

*Image credit: Kai Arulkumaran*

### Approximations {data-transition="None"}

<img src="../slides/diagrams/sparse-gps-2.png" align="center" width="90%" style="background:none; border:none; box-shadow:none;">

*Image credit: Kai Arulkumaran*

### Approximations {data-transition="None"}

<img src="../slides/diagrams/sparse-gps-3.png" align="center" width="45%" style="background:none; border:none; box-shadow:none;">

*Image credit: Kai Arulkumaran*

### Approximations {data-transition="None"}

<img src="../slides/diagrams/sparse-gps-4.png" align="center" width="45%" style="background:none; border:none; box-shadow:none;">

*Image credit: Kai Arulkumaran*

### Full Gaussian Process Fit {data-transition="None"}

<object data="../slides/diagrams/gp-approx-full.svg" class="svgplot"></object>

### Inducing Variable Fit {data-transition="None"}

<object data="../slides/diagrams/gp-approx-sparse-init.svg" class="svgplot"></object>

### Inducing Variable Param Optimize {data-transition="None"}

<object data="../slides/diagrams/gp-approx-sparse-fit-1.svg" class="svgplot"></object>

### Inducing Variable Full Optimize {data-transition="None"}

<object data="../slides/diagrams/gp-approx-sparse-fit-2.svg" class="svgplot"></object>

### Full Gaussian Process Fit {data-transition="None"}

<object data="../slides/diagrams/gp-approx-full.svg" class="svgplot"></object>

### Modern Review {data-transition="None"}

* *A Unifying Framework for Gaussian Process Pseudo-Point Approximations using Power Expectation Propagation*
    @Thang:unifying17

* *Deep Gaussian Processes and Variational Propagation of Uncertainty*
    @Damianou:thesis2015



\include{../_deepgp/includes/deep-nn-gp.md}
\include{../_deepgp/includes/deeptheory.md}

\include{../_deepgp/includes/deep-olympic.md}
\include{../_deepgp/includes/deep-step-function.md}
\include{../_deepgp/includes/deep-motorcycle.md}
\include{../_deepgp/includes/deep-robot-wireless.md}

\include{../_deepgp/includes/deep-high-five.md}

\include{../_deepgp/includes/deep-usps-digits.md}




\include{../_health/includes/deep-health-model.md}


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

\include{../_deepgp/includes/multi-fidelity-modelling.md}

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


