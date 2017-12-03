---
layout: slides
title: "DRAFT SLIDES: Deep Probabilistic Modelling with with Gaussian Processes"
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

Suchi and Peter Counterfactual GPs

[@Schulam:counterfactual17]

\include{../_deepgp/includes/deep-nn-gp.md}
\include{../_deepgp/includes/deeptheory.md}

### Samples from a Deep GP

\include{../_deepgp/includes/deep-step-function.md}
\include{../_deepgp/includes/deep-loop-detection.md}
\include{../_deepgp/includes/deep-results.md}

###

Papers to cite on deep health:

[@Ranganath-survival16]
[@Mattos:recurrent15]

[@Damianou:thesis2015]

[@Saul:thesis2016]

This conference:

[@Anqi:gpspike2017]

[Salimbeni:doubly2017]

[@Alaa:deep2017]


\include{../_health/includes/deep-health-model.md}

\include{../_deepgp/includes/multi-fidelity-modelling.md}

acknowledgements: suggestions from Stefano  Eleftheriadis, John Bronskill, Hugh Salembeni, Rich Turner.



### Ongoing Code

### Thanks!

* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)

### References {.allowframebreaks data-background="../slides/diagrams/pres_bg.png"}
