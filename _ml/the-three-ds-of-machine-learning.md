---
title: "The Three Ds of Machine Learning"
abstract: >
  Machine learning solutions, in particular those based on deep learning methods, form an underpinning of the current revolution in “artificial intelligence” that has dominated popular press headlines and is having a significant influence on the wider tech agenda.
  
  In this talk I will give an overview of where we are now with machine learning solutions, and what challenges we face both in the near and far future. These include practical application of existing algorithms in the face of the need to explain decision making, mechanisms for improving the quality and availability of data, dealing with large unstructured datasets.
reveal: 2018-11-15-the-three-ds-of-machine-learning.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2018-11-15
venue: Data Science Africa, Abuja
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

\include{_data-science/includes/lies-damned-lies.md}

<!--\include{_ai/includes/centrifugal-governor.md}-->

\include{_ai/includes/embodiment-factors.md}
\include{_data-science/includes/evolved-relationship.md}
\include{_data-science/includes/societal-effects.md}

\include{_ml/includes/what-does-machine-learning-do.md}

\include{_ml/includes/what-is-ml-2.md}
<!-- include{_ml/includes/process-automation.md} -->
<!-- include{_ai/includes/ai-vs-data-science-2.md} -->
\include{_supply-chain/includes/supply-chain.md}
\include{_ml/includes/or-control-econometrics-statistics-ml.md}


\todo{Analytics??? MBA based data science?}
\todo{Statisticians fail to scale}
\todo{Statisticians fail to code}
\todo{Statisticians ... sharing code R}
\todo{Can Do attitude vs Can't do attitude}

\include{_data-science/includes/data-science-challenges.md}


\newslide{THE THREE Ds of ML SYSTEMS DESIGN}

\include{_ml/includes/the-3ds-of-ml-systems-design.md}
\include{_ml/includes/the-3ds-enough-talk.md}
\include{_ml/includes/ml-outlook.md}

\subsection{Conclusion}
\slides{
* Technologically *evolving* environment.
* ML is a key component of decision making.
* Data is the key component of ML.
* ML is *critically* dependent on data.
* Challenges in system **decomposition**, **data** curation and model **deployment**. 
}
\notes{We operate in a technologically evolving environment. Machine learning is becoming a key component in our decision making capabilities. But the evolving nature of data driven systems means that new approaches to model deployment are necessary. We have characterized three parts of the machine learning systems design process. *Decomposition* of the problem into separate tasks that are addressable with a machine learning solution. Collection and curation of appropriate *data*. Verificaction of data quality through data readiness levels. Using *progression* testing in our *deployments*. Continuously updating models as appropriate to ensure performance and quality is maintained.}

\thanks

\references





