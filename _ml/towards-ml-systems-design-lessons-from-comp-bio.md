---
title: "Towards Machine Learning Systems Design"
subtitle: "Lessons from Computational Biology"
venue: "Mathematical Genomics Away Day"
abstract: >
  Machine learning solutions, in particular those based on deep learning 
  methods, form an underpinning for the modern artificial intelligence 
  revolution that has dominated popular press headlines and is having a 
  strong influence on the wider tech agenda.

  In this talk I will give an overview of where we are now with machine 
  learning solutions, and what challenges we face both in the near and far 
  future. 
  
  Many of these lessons were first formed in computational biology, throughout the talk I'll highlight connections I see, emphasizing the relevance of biological data analysis to real world data analysis.
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: University of Sheffield and Amazon Cambridge
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
date: 2019-05-14
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
categories:
- genoimics
---

\include{talk-macros.tex}

\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/data-science-vs-ai.md}
\include{_ml/includes/what-does-machine-learning-do.md}
\include{_supply-chain/includes/supply-chain.md}
\include{_ai/includes/deploying-ai.md}
\include{_ai/includes/ml-systems-design-long.md}

\editme
\section{Conclusion}
\newslide{Conclusion}
\slides{
* The Cell is a Micro Supply Chain. 
    * Analyzing cell data has a lot in common with analyzing supply chain data.
    * In Biology you are fortunate to have many cells (destructive testing).

* In Supply Chain we find it easier to deploy modificiations for the system.
    * Downstream effects are complex and need monitoring.
	* Life is really good at dealing with evolving environments ... our designs not so much.
}

\notes{I'm very often struck by the relations between supply chain systems and cellular systems. A particular point to remember, is that both systems are *evolved*, not *designed*. In Supply Chain this is because the infrastructure is built over a period of time that has a time constant longer than the timeframe over which businesses move. In life it is similar, but the infrastructure is biochemical in form and the business problem is the environment.}

\thanks

\references
