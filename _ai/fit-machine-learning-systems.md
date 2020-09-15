---
title: FIT Machine Learning Systems
layout: talk
abstract: >
  As machine learning becomes more widely deployed, it is important
  that we understand what we have deployed. There has been a lot of
  focus in machine learning research on the fairness and
  interpretability of individual models, but less attention paid to
  how this fits into a wider machine learning system. In this talk
  I’ll motivate the importance of fair, interpretable and transparent
  machine learning systems. I’ll outline the challenges and highlight
  some of the directions we are considering to address these
  challenges.
  
  This work is sponsored by an Alan Turing Institute Senior AI Fellowship.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
youtube: H99hXegNG-c
date: 2020-09-15
venue: Huawei-Cambridge Workshop
transition: None
---

\include{talk-macros.tex}

\include{_ai/includes/the-great-ai-fallacy.md}

\section{The Problem}
\include{_ai/includes/intellectual-debt-short.md}
\include{_ai/includes/buying-system.md}
\include{_ai/includes/buying-to-banking.md}
\include{_ai/includes/fit-systems.md}
\section{A Technology}
\include{_uq/includes/emulation.md}
\section{A Solution}
\include{_data-science/includes/data-oriented-architectures-short.md}
\include{_data-science/includes/milan.md}
\include{_uq/includes/deep-emulation.md}

\section{Conclusion}
\slides{
* AI Fallacy incorrectly suggests machines will adapt to us.
* Reality is a greater need for explanation of decision making.
* Roadmap to address this challenge involves:
  * The Milan IL Algebra
  * Meta modelling with e.g. Emukit
  }

\thanks
\references
