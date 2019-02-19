---
title: "Data Science and Digital Systems"
subtitle: "The Three Ds of ML Systems Design"
abstract: >
  Machine learning solutions, in particular those based on deep learning methods, form an underpinning of the 
  current revolution in “artificial intelligence” that has dominated popular press headlines and is having a 
  significant influence on the wider tech agenda.
  
  In this talk I will give an overview of where we are now with machine learning solutions, and what challenges 
  we face both in the near and far future. These include practical application of existing algorithms in the 
  face of the need to explain decision making, mechanisms for improving the quality and availability of data, 
  dealing with large unstructured datasets.
reveal: 2019-02-19-data-science-and-digital-systems.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-02-19
venue: Stu Hunter Resesearch Conference, Milan
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

\include{_data-science/includes/gartner-hype-cycle-ai-bd-dm-dl-ml.md}

\include{_data-science/includes/lies-damned-lies.md}

\include{_ml/includes/what-is-ml-2.md}
\include{_ai/includes/ai-vs-data-science-2.md}

\include{_ai/includes/embodiment-factors.md}
\include{_data-science/includes/evolved-relationship.md}
\include{_data-science/includes/societal-effects.md}

\include{_ml/includes/what-does-machine-learning-do.md}

\newslide{Deep Learning}

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition

\include{_ml/includes/deep-learning-overview.md}
\include{_data-science/includes/a-time-for-professionalisation.md}

<!--
<!--include{_gp/includes/gp-intro-very-short.md}-->
<!--include{_deepgp/includes/deep-olympic.md}-->

\subsection{Thoughts from Willis's Talk}
\slides{
* Analytics: Data Science for Business Graduates
* We are entering a golden era for statistics.
* To take advantage:
    * Statisticians need to learn to *scale*.
	* Statisticians need to learn to *code* (properly!).
* Can do attitude vs Can't do attitude.
}
\notes{Before moving on some thoughts triggered by the discussion of Willis's talk.}

\notes{Names are evolving, and should be allowed to evolve, let's not pin down new terms to closely yet. But when it comes to analytics, that feels like it is the education of decision makers (MBA graduates, managers, civil servants) about the limits and capabilities of data driven technologies.}

\notes{It's true that the world of data is changing, but this should be leading to a golden era for statistics. But to take advantage statisticians need to learn to scale. That means sharing their expertise and empowering domain experts. That means learning to *code properly*. I.e. to work with software engineers in deployment of solutions. The world is changing around statistics, and these changes require a *can do* attitude. Data science is a garden in which Computer Scientists and Statisticians can finally play together, undoing years of institutional and cultural barriers between the fields.}

\include{_data-science/includes/data-science-challenges.md}

\include{_ai/includes/centrifugal-governor.md}

\subsection{Amazon: Bits and Atoms}

\newslide{Artificial Intelligence}

* Challenges in deploying AI.
* Currently this is in the form of "machine learning systems"

\newslide{Internet of People}

* Fog computing: barrier between cloud and device blurring.
    * Computing on the Edge
* Complex feedback between algorithm and implementation
  
\newslide{Deploying ML in Real World: Machine Learning Systems Design}

* Major new challenge for systems designers.
* Internet of Intelligence but currently:
	* AI systems are *fragile*

\include{_supply-chain/includes/ml-and-supply-chain.md}
\include{_ml/includes/or-control-econometrics-statistics-ml.md}

\newslide{THE THREE Ds of ML SYSTEMS DESIGN}

\include{_ml/includes/the-3ds-of-ml-systems-design.md}
<!--\include{_ml/includes/the-3ds-enough-talk.md}-->
\include{_ml/includes/ml-outlook.md}

\subsection{Conclusion}
\slides{
* Technologically *evolving* environment.
* ML is a key component of decision making.
* Data is the key component of ML.
* ML is *critically* dependent on data.
* Challenges in *problem Decomposition*, *Data curation* and *model Deployment* 
}
\notes{We operate in a technologically evolving environment.  Machine learning is becoming a key component in our decision making capabilities, our intelligence and strategic command. However, technology drove changes in battlefield strategy. From the stalemate of the first world war to the tank-dominated Blitzkrieg of the second, to the asymmetric warfare of the present. Our technology, tactics and strategies are also constantly evolving. Machine learning is part of that evolution solution, but the main challenge is not to become so fixated on the tactics of today that we miss the evolution of strategy that the technology is suggesting.}

\thanks

\references




