---
title: "The Future of AI"
subtitle: "Systems, Data Science, Biology, Medicine"
venue: "Autumn Data Science School, Cambridge"
abstract: >
  Waves of automation have driven human advance, and each wave requires humans to The promise of AI is to launch new systems of automated intellectual endeavour that will be the first systems to adapt to us. 
  
  In reality, the systems we have will not achieve this, and it is the biological sciences that teach us this lesson most starkly. 
  
  In this talk I will review some of the successes and challenges of AI and its deployment and propose practical visions for the future based on approaches that have worked in the past. 
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: University of Sheffield
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
date: 2019-09-26
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
categories:
- health
---

\include{talk-macros.tex}

\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/data-science-vs-ai.md}
\include{_supply-chain/includes/supply-chain.md}
\include{_supply-chain/includes/ml-and-supply-chain.md}
\include{_supply-chain/includes/arthur-christmas.md}
\include{_ml/includes/deep-learning-overview.md}
\include{_deepgp/includes/deep-olympic.md}
\include{_deepgp/includes/deep-step-function.md}
\include{_deepgp/includes/deep-della-gatta.md}
\include{_ai/includes/deploying-ai.md}
\include{_health/includes/malaria-gp.md}
\include{_health/includes/deep-health-model.md}


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
