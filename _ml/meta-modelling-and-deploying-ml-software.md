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
\include{_uq/includes/emulation.md}

\include{_uq/includes/uncertainty-quantification.md}

\include{_uq/includes/emukit-playground.md}
\include{_uq/includes/emukit-software.md}

\include{_deepgp/includes/deep-nn-gp.md}
\include{_deepgp/includes/deep-olympic.md}

\include{_ml/includes/mxfusion-intro.md}


\subsection{Conclusion}

\notes{Machine learning models are deployed as components in an interacting system to achieve modern AI. Some of those components are inspired by a mechanistic understanding of the world around us (e.g. economic or physical understanding).}

\notes{Meta modelling involves fiting machine learning models to existing systems to improve speed and interpretability.}

\notes{Deep Gaussian processes are a flexible approach to meta modelling.}

\slides{* ML deployed in interacting systems.
* Meta modelling fits statistical models to existing *mechanistic* models.
* Leads to speed and interpretability improvements.
* Deep GPs are a flexible approach to meta-modelling.}

\thanks

\references
