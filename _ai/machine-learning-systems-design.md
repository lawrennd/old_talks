---
title: "Machine Learning Systems Design"
subtitle: "Making Amazon a Data First Company"
abstract: >
  Machine learning solutions, in particular those based on deep learning methods, form an underpinning of the current revolution in “artificial intelligence” that has dominated popular press headlines and is having a significant influence on the wider tech agenda.
  
  In this talk I will give an overview of where we are now with machine learning solutions, and what challenges we face both in the near and far future. These include practical application of existing algorithms in the face of the need to explain decision making, mechanisms for improving the quality and availability of data, dealing with large unstructured datasets.
ipynb: 2018-09-20-machine-learning-systems-design-data-first.ipynb
reveal: 2018-09-20-machine-learning-systems-design-data-first.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2018-09-20
venue: Analyticon
transition: None
---

\include{talk-macros.tex}


\newslide{}

\div{\includeimg{../slides/diagrams/2017-10-12 16.47.34.jpg}{50%}{rotateimg90}{center}}{}{text-align:center}

\newslide{}

\div{\includeimg{../slides/diagrams/SteamEngine_Boulton&Watt_1784_neg.png}{50%}{center}}{}{text-align:center}

\include{../_ai/includes/embodiment-factors.md}
<!--include{../_data-science/includes/evolved-relationship.md}
include{../_ml/includes/what-does-machine-learning-do.md}-->

\include{_ml/includes/what-is-ml-2.md}
\include{_ai/includes/ai-vs-data-science-2.md}


\include{_supply-chain/includes/ml-and-supply-chain.md}
\include{_amazon/includes/amazon-scot.md}
\include{_ml/includes/or-control-econometrics-statistics-ml.md}
\include{_ml/includes/general-ml-challenges.md}
\include{_amazon/includes/amazon-ml-zero.md}
\include{_ml/includes/ml-outlook.md}

\subsection{Conclusion}
\slides{
* Technologically *evolving* environment.
* ML is a key component of decision making.
* Data is the key component of ML.
* ML is *critically* dependent on data.
* Challenges in *design*, *data curation* and *model deployment* 
}
\notes{We operate in a technologically evolving environment.  Machine learning is becoming a key coponent in our decision making capabilities, our intelligence and strategic command. However, technology drove changes in battlefield strategy. From the stalemate of the first world war to the tank-dominated Blitzkrieg of the second, to the asymmetric warfare of the present. Our technology, tactics and strategies are also constantly evolving. Machine learning is part of that evolution solution, but the main challenge is not to become so fixated on the tactics of today that we miss the evolution of strategy that the technology is suggesting.}

### References






