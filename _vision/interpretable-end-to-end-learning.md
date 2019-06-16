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

\newslide{Amazon: Bits and Atoms}

\include{_supply-chain/includes/supply-chain.md}

\section{End-to-End: Environment and Decision}

\include{_ml/includes/what-is-ml-end-to-end.md}

\include{_uq/includes/emulation.md}


<!--include{_ai/includes/ai-vs-data-science-2.md}-->

<!-- in this short overview, don't introduce GPy or the data-->
<!--\define{stepFunctionData} -->
\define{gpySoftware}
\include{_deepgp/includes/deep-motorcycle.md}


<!--\include{_data-science/includes/data-science-africa.md}
\include{_health/includes/malaria-gp.md}-->

\subsection{Conclusions}

\slides{* AI is algorithmic decision making.
* Machine learning systems are *not* decomposable.
* Deep emulation as a methodological solution.
* Bayesian Systems Optimization as a Decision Making Framework.}

\thanks

\references
