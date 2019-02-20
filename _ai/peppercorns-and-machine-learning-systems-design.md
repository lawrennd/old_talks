---
title: Peppercorns and Machine Learning System Design
abstract: "Machine learning is fundamental to two important
  technological domains, artificial intelligence and data science. In
  this talk we will attempt to make a simple definition to distinguish
  between the two, then we will focus on the challenges of machine
  learning in *application* to artificial intelligence particularly from 
  the perspective of systems design. We expect a particular challenge to 
  be the deployment of such systems in real environment, where 
  unforeseen consequences of interaction with real world environments
  will produce embarrassing failures. Because these failures are not
  bugs, in that the system will be performing as designed, but
  failures of imagination of the designers we introduce a new term for
  them: 'peppercorns'."
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2017-06-02
venue: Sheffield ML Research Retreat
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/data-science-vs-ai.md}
\include{_ai/includes/embodiment-factors.md}
\include{_ai/includes/deploying-ai.md}
\include{_ai/includes/ml-systems-design-long.md}
\include{_ai/includes/intelligent-system-paolo.md}

\section{Conclusion}
\newslide{Conclusion}

* Difference between Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our approaches to systems design are building powerful machines that
will be deployed in evolving environments.

\thanks

\references
