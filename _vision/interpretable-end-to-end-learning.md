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
date: 2019-06-18
venue: Department of Computer Science and Technology, University of Cambridge
transition: None
incremental: True
---

\include{talk-macros.tex}

\section{Introduction}

\notes{The fourth industrial revolution bears the particular hallmark of being the first revolution that has been named before it has happened. This is particularly unfortunate, because it is not in fact an industrial revolution at  all. Nor is it necessarily a distinct phenomenon. It is part of a revolution in information, one that goes back to digitisation and the invention of the silicon chip.}

\notes{Or to put it more precisely, it is a revolution in how information can affect the physical world. The interchange between information and the physical world.}

\include{_ai/includes/amazon-delivery-drone.md}

\newslide{Bits and Atoms}

\figure{\includejpg{../slides/diagrams/supply-chain/container-2539942_1920}{80%}}{The container is one of the major drivers of globalization, and arguably the largest agent of social change in the last 100 years. It reduces the cost of transportation, significantly changing the appropriate topology of distribution networks. The container makes it possible to ship goods halfway around the world for cheaper than it costs to process those goods, leading to an extended distribution topology.}{container-2539942_1920}

\section{End-to-End: Environment and Decision}

\include{_ml/includes/what-is-ml-end-to-end.md}

\newslide{}

\figure{\includediagram{../slides/diagrams/ai/ride-allocation-prediction}{60%}}{Some software components in a ride allocation system. Circled components are hypothetical, rectangles represent actual data.}{ride-allocation-system}

\newslide{}

\figure{\includediagram{../slides/diagrams/ai/ml-system-downstream-pedestrian000}{80%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

\include{_uq/includes/emulation.md}

\newslide{}

\figure{\includediagram{../slides/diagrams/ai/ml-system-downstream-pedestrian000}{80%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}


\newslide{}

\figure{\includediagram{../slides/diagrams/ai/ml-system-downstream-pedestrian001}{80%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

\newslide{}

\figure{\includediagram{../slides/diagrams/ai/ml-system-downstream-pedestrian}{80%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

\newslide{Bayesian *System* Optimization}

* Aim: maintain interpretable compoents.
* Monitor downstream/upstream effects through emulation.
* Optimize individual components considering upstream and downstream.

\newslide{Technology: Deep Emulation}

\include{_ml/includes/deep-face.md}
<!--\include{_ml/includes/deep-learning-as-pinball.md}-->

\include{_deepgp/includes/deep-nn.md}
\include{_deepgp/includes/overfitting-low-rank.md}
\include{_deepgp/includes/deep-gp.md}

\newslide{Stochastic Process Composition}

$$\dataVector = \mappingFunctionVector_4\left(\mappingFunctionVector_3\left(\mappingFunctionVector_2\left(\mappingFunctionVector_1\left(\inputVector\right)\right)\right)\right)$$
<!--include{_ai/includes/ai-vs-data-science-2.md}-->

<!-- in this short overview, don't introduce GPy or the data-->
<!--\define{stepFunctionData} -->
\define{gpySoftware}
\include{_deepgp/includes/deep-motorcycle.md}
\include{_ml/includes/graphical-models.md}


\include{_health/includes/malaria-gp.md}-->

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



\subsection{Directions}

\slides{* Mechanistic modelling
* Automated Abstraction
* Deep emulation
* Bayesian Systems Optimization
}

\include{_data-science/includes/data-science-africa.md}

\newslide{ML in Cambridge}

\slides{* ML Systems Design
* Challenges in Optimization, Monitoring, Deployment
* Application Areas: Comp Bio, Health, **Developing Economies**
}

\thanks

\references
