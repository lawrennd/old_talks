---
title: "Machine Learning and the Physical World"
abstract: >
  Machine learning is a data driven endeavour, but real world systems are physical and mechanistic. In this talk we will review approaches to integrating machine learning with real world systems. Our focus will be on emulation (otherwise known as surrogate modeling). 
ipynb: 2018-11-06-the-three-ds-of-machine-learning.ipynb
reveal: 2018-11-06-the-three-ds-of-machine-learning.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2018-11-06
venue: Uber AI Labs
transition: None
---

\include{talk-macros.tex}

\include{_ai/includes/centrifugal-governor.md}

\include{_ml/includes/what-is-ml-2.md}
\include{_ml/includes/process-automation.md}
\include{_ai/includes/ai-vs-data-science-2.md}

\newslide{The Gap}

* There is a gap between the world of data science and AI.
* The mapping of the virtual onto the physical world.
* E.g. Causal understanding. 

\include{_ml/includes/ml-and-supply-chain.md}
<!--include{_ml/includes/or-control-econometrics-statistics-ml.md}-->

\newslide{UNCERTAINTY QUANTIFICATION}

\include{_ml/includes/process-emulation.md}
\include{_uq/includes/emukit-playground.md}
\include{_uq/includes/uncertainty-quantification.md}
\include{_uq/includes/emukit.md}
\include{_ml/includes/mxfusion.md}

\newslide{Long term Aim}

* Simulate/Emulate the components of the system.
    * Validate with real world using multifidelity.
	* Interpret system using e.g. sensitivity analysis.
* Perform end to end learning to optimize.
    * Maintain interpretability.


### References






