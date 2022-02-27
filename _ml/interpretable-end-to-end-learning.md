---
layout: slides
title: "Interpretable End-to-End Learning"
subtitle: 
author: Neil D. Lawrence
transition: None
abstract: >
  Practical artificial intelligence systems can be seen as algorithmic decision makers. The fractal nature of decision making implies that this involves interacting systems of components where decisions are made multiple times across different time frames. This affects the decomposability of an artificial intelligence system. Classical systems design relies on decomposability for efficient maintenance and deployment of machine learning systems, in this talk we consider the challenges of optimizing and maintaining such systems.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-06-26
venue: Sheffield ML Group Research Retreat
transition: None
incremental: True
---

talk-macros.gpp}lk-macros.tex}

\section{Introduction}

talk-macros.gpp}i/includes/the-fourth-industrial-revolution.md}

\section{End-to-End: Environment and Decision}

talk-macros.gpp}l/includes/what-is-ml-end-to-end.md}

talk-macros.gpp}ata-science/includes/experiment-analyze-design.md}

talk-macros.gpp}ata-science/includes/data-oriented-architectures.md}

\newslide{Autonomous Vehicles}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-pedestrian000}{80%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

talk-macros.gpp}q/includes/emulation.md}
talk-macros.gpp}q/includes/deep-emulation.md}
talk-macros.gpp}q/includes/bayesian-system-optimization.md}

talk-macros.gpp}q/includes/auto-ai.md}

\newslide{Technology: Deep Emulation}

talk-macros.gpp}l/includes/deep-face.md}
<!--talk-macros.gpp}l/includes/deep-learning-as-pinball.md}-->

talk-macros.gpp}eepnn/includes/deep-neural-networks.md}
talk-macros.gpp}eepgp/includes/overfitting-low-rank.md}
talk-macros.gpp}eepgp/includes/deep-gp.md}
talk-macros.gpp}eepgp/includes/stochastic-process-composition.md}

<!--include{_ai/includes/ai-vs-data-science-2.md}-->

<!-- in this short overview, don't introduce GPy or the data-->
<!--\define{stepFunctionData} -->
\define{gpySoftware}
talk-macros.gpp}eepgp/includes/deep-motorcycle.md}
talk-macros.gpp}l/includes/graphical-models.md}

talk-macros.gpp}ata-science/includes/data-oriented-conclusions.md}

<!--talk-macros.gpp}ealth/includes/malaria-gp.md}-->

\subsection{Related Papers}

* *Deep Gaussian Processes*
    @Damianou:deepgp13

* *Latent Force Models*
  @Alvarez:llfm13

* *Gaussian Process Latent Force Models for Learning and Stochastic Control of Physical Systems*
  @Sarkka:control18

* *The Emergence of Organizing Structure in Conceptual Representation*
  @Lake:emergence18

\subsection{Other's Work}

* *How Deep Are Deep Gaussian Processes?*
  @Dunlop:deep2017
* *Doubly Stochastic Variational Inference for Deep Gaussian Processes*
  @Salimbeni:doubly2017
* *Deep Multi-task Gaussian Processes for Survival Analysis with Competing Risks*
  @Alaa:deep2017
* *Counterfactual Gaussian Processes for Reliable Decision-making and What-if Reasoning*
  @Schulam:counterfactual17

\subsection{Conclusions and Directions}

\slides{* Mechanistic modelling
* Automated Abstraction
* Deep emulation
* Bayesian Systems Optimization
* Auto AI
}

\notes{We've introduce some of the challenges of real-world systems and outlined how to address them. The new ideas we are focussing on extend the field of uncertainty quantification and surrogate modelling to four different areas.

1. **Automated Abstraction** is the automated deployment of surrogate models, or emulators, for summarizing the underlying components in the system. It relies on *data oriented architectures* to be possible.

2. **Deep emulation** is the combination of chains of different emulators across the system to assess downstream performance.

3. **Bayesian System Optimization** is the resulting optimization of the entire system, end-to-end, in a manner that doesn't destroy interpretability because end-to-end signals are propagted down to the system components through the deep emulator.

4. **Auto AI** is the result, moving beyond Auto ML, we will be able to develop systems that identify problems in deployment and assess the appropriate system responses.}

\thanks

\references
