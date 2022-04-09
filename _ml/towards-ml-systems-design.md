---
title: "Towards Machine Learning Systems Design"
venue: "Department of Computing Science, University of Glasgow"
abstract: >
  Machine learning solutions, in particular those based on deep learning 
  methods, form an underpinning for the modern artificial intelligence 
  revolution that has dominated popular press headlines and is having a 
  strong influence on the wider tech agenda.

  In this talk I will give an overview of where we are now with machine 
  learning solutions, and what challenges we face both in the near and far 
  future. These include practical application of existing algorithms in 
  the face of the need to explain decision making, mechanisms for improving 
  the quality and availability of data, and dealing with large unstructured 
  datasets.
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: University of Sheffield and Amazon Cambridge
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
date: 2019-02-22
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
categories:
- glasgow2019
---

\include{talk-macros.tex}

\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/data-science-vs-ai.md}
\include{_ai/includes/embodiment-factors.md}
\include{_data-science/includes/evolved-relationship.md}
\include{_ml/includes/what-does-machine-learning-do.md}
\include{_ml/includes/deep-learning-overview.md}
\include{_gp/includes/gp-intro-very-short.md}
\include{_deepgp/includes/deep-olympic.md}
\include{_supply-chain/includes/supply-chain.md}
\include{_supply-chain/includes/ml-and-supply-chain.md}
\include{_ai/includes/deploying-ai.md}
\include{_ai/includes/ml-systems-design-long.md}
\include{_uq/includes/emukit-software.md}

\editme
\section{Conclusion}
\newslide{Conclusion}
\slides{
* Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our approaches to systems design are building powerful machines that
will be deployed in evolving environments.
}

\notes{Artificial intelligence and data science are fundamentally different. In one you are dealing with data collecte by happenstance, in the other you are trying to build systems in the real world, often by actively collecting data. Our approaches to systems design are building powerful machines that will be deployed in evolving environments. But this is presenting key challenges in how we maintain and manage our machine learning systems.}

\thanks

\references
