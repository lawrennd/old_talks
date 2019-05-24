---
title: "Meta-Modelling and Deploying ML Software"
venue: "The Mathematics of Deep Learning and Data Science"
abstract: "Data is not so much the new oil, it is the new software. Data driven  algorithms are increasingly present in continuously deployed production software. What challenges does this present and how can the mathematical sciences help?"
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
date: 2019-05-23
categories:
- notes
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

\include{_ai/includes/intelligent-system-paolo.md}
\include{_ml/includes/deep-learning-overview.md}


\include{_supply-chain/includes/containerisation.md}
\include{_supply-chain/includes/supply-chain-motto.md}


\include{_uq/includes/emulation.md}

\notes{\include{_uq/includes/uq-intro.md}}
\include{_uq/includes/uncertainty-quantification.md}

\include{_uq/includes/emukit-playground.md}
\include{_uq/includes/emukit-software.md}

\notes{For monitoring systems in production, emulation needn't just be about simulator models. What we envisage, is that even data driven models could be emulated. This is important for understanding system behaviour, how the different components are interconnected. This drives the notion of the *information dynamics* of the machine learning system. What is the effect of one particular intervention in the wider system? One way of answering this is through emulation. But it requires that our machine learning models (and our simulators) are deployed in an environment where emulation can be automatically deployed. The resulting system would allow us to monitor the downstream effects of indivdiual decision making on the wider system. 

\addblog{New Directions in Kernels and Gaussian Processes}{2016/11/29/new-directions-in-kernels-and-gaussian-processes}

\section{Deep Gaussian Processes}

\notes{One challenge is developing flexible enough models to perform the emulation that also propagate uncertainty through the model. One candidate set of models for this challenge is *deep Gaussian processes* (DGPs). For the remainder of these notes we introduce the theory behind DGPs. 

While there are some difficulties in algorithmically implementing these algorithms at scale, they are mathematically far simpler than the equivalent neural network models, and perhaps as a result offer greater promise for theoretical understanding of deep learning [see e.g. @Dunlop:deep2017]. }

\include{_deepgp/includes/deep-gp.md}
\include{_deepgp/includes/deep-olympic.md}

\include{_ml/includes/mxfusion-intro.md}


\subsection{Conclusion}

\notes{Machine learning models are deployed as components in an interacting system to achieve modern AI. Some of those components are inspired by a mechanistic understanding of the world around us (e.g. economic or physical understanding).}

\notes{Meta modelling involves fiting machine learning models to existing systems to improve speed and interpretability.}

\notes{Deep Gaussian processes are a flexible approach to meta modelling, which provide the necessary uncertainty estimates and the potential for being more mathematically tractable.}

\slides{* ML deployed in interacting systems.
* Meta modelling fits statistical models to existing *mechanistic* models.
* Leads to speed and interpretability improvements.
* Deep GPs are a flexible approach to meta-modelling.}

\thanks

\references
