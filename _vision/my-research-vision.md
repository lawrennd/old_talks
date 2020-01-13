---
layout: slides
title: "My Research Vision"
subtitle: "End to End Data Science"
author: Neil D. Lawrence
transition: None
abstract: >
  In this talk I will give an overview of my research vision.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-01-25
venue: Imperial College, London
transition: None
incremental: True
---

\include{talk-macros.tex}

\include{_ml/includes/what-is-ml-2.md}
<!--include{_ai/includes/ai-vs-data-science-2.md}-->

\section{Data}

\include{_ml/includes/ml-three-primary-challenges.md}
\include{_data-science/includes/data-readiness-levels-short.md}
\include{_data-science/includes/data-trusts.md}

\section{Model}

\include{_ml/includes/deep-learning-as-pinball.md}
\include{_gp/includes/planck-cmp-master-gp.md}
\include{_deepgp/includes/process-composition.md}
<!-- in this short overview, don't introduce GPy or the data-->
\define{stepFunctionData} 
\define{gpySoftware}
\include{_deepgp/includes/deep-step-function.md}
\include{_health/includes/deep-health-model.md}

\section{End-to-End: Environment and Decision}

\newslide{Amazon: Bits and Atoms}

\include{_supply-chain/includes/supply-chain.md}
\include{_supply-chain/includes/ml-and-supply-chain.md}
\include{_data-science/includes/data-science-africa.md}
\include{_health/includes/malaria-gp.md}

\thanks

\references
