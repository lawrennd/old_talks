---
title: "Modern Data Oriented Programming"
abstract: >
  There has been a great deal of interest in probabilistic programs: placing modeling at the heart of programming language. In this talk we set the scene for data oriented programming. 
	
  Data is a fundamental component of machine learning, yet the availability, quality and discoverability of data are often ignored in formal computer science. 
  
  While languages for data manipulation exist (for example SQL), they are not suitable for the modern world of machine learning data. Modern data oriented languages should place data at the center of modern digital systems design and provide an infrastructure in which monitoring of data quality and model decision making are automaticaly available. 
  
  We provide the context for Modern Data Oriented Programming, and give some insight into our initial ideas in this space.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
blog: 
date: 2019-05-21
venue: Advances and Challenges in Machine Learning Languages, Centre for Mathematical Sciences, Cambridge
transition: None
---

\include{talk-macros.tex}

\include{_data-science/includes/gartner-hype-cycle-ai-bd-dm-dl-ml.md}
\include{_ai/includes/centrifugal-governor.md}

\include{_ml/includes/what-is-ml-2.md}
\include{_ai/includes/ai-vs-data-science-2.md}

\subsection{Amazon: Bits and Atoms}
<!--
include{../_ai/includes/embodiment-factors.md}
include{_data-science/includes/evolved-relationship.md}
include{_ml/includes/what-does-machine-learning-do.md}

newslide{Deep Learning}

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition

include{_ml/includes/deep-learning-overview.md}-->
<!--include{_gp/includes/gp-intro-very-short.md}-->
<!--include{_deepgp/includes/deep-olympic.md}-->
<!--
include{_data-science/includes/a-time-for-professionalisation.md}
include{_data-science/includes/the-data-crisis.md} 

newslide{Rest of this Talk: Two Areas of Focus}

* Reusability of Data
* Deployment of Machine Learning Systems

newslide{Rest of this Talk: Two Areas of Focus}

* <s>Reusability of Data</s>
* Deployment of Machine Learning Systems

include{_data-science/includes/data-readiness-levels.md}

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

\include{_ml/includes/what-is-ml-2.md}
\include{_ai/includes/ai-vs-data-science-2.md}
-->

\include{_supply-chain/includes/ml-and-supply-chain.md}
<!--include{_ml/includes/or-control-econometrics-statistics-ml.md}-->
\subsection{The Three Ds of Machine Learning Systems Design}

\slides{
* Three primary challenges of Machine Learning Systems Design.
1. Decomposition
2. Data 
3. Deployment
}

\newslide{The Three Ds of Machine Learning Systems Design}

\slides{
* Three primary challenges of Machine Learning Systems Design.
1. <s>Decomposition</s>
2. Data 
3. <s>Deployment</s>
}


\notes{We can characterize the challenges for integrating machine learning within our systems as the three Ds. Decomposition, Data and Deployment.}

\notes{The first two components *decomposition* and *data* are interlinked, but we will first outline the decomposition challenge. Below we will mainly focus on *supervised learning* because this is arguably the technology that is best understood within machine learning.}

\include{_ml/includes/ml-data-challenge.md}
\include{_ml/includes/ml-combining-data-and-systems-design-challenge.md}
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

\thanks

\references


