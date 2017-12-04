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


### Deep Gaussian Processes

\include{../_deepgp/includes/deep-nn-gp.md}
\include{../_deepgp/includes/deeptheory.md}

\include{../_deepgp/includes/stack-gp-intro.md}
\include{../_deepgp/includes/stacked-pca.md}
\include{../_deepgp/includes/stacked-gp.md}

\include{../_deepgp/includes/deep-olympic.md}
\include{../_deepgp/includes/deep-robot-wireless.md}

\include{../_deepgp/includes/deep-high-five.md}
\include{../_deepgp/includes/deep-usps-digits.md}




\include{../_health/includes/deep-health-model.md}


### 

* @Anqi:gpspike2017
* @Salimbeni:doubly2017
* @Alaa:deep2017
* @Schulam:counterfactual17


###

* @Ranganath-survival16
* @Mattos:recurrent15
* @Damianou:thesis2015
* @Saul:thesis2016

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


