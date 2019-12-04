---
title: "From Innovation to Deployment"
subtitle: "Auto AI and Machine Learning Systems Design"
abstract: >
  In this talk we introduce a five year project funded by the UK's Turing Institute to shift the focus from developing AI systems to deploying AI systems that are safe and reliable. 
  
  The AI systems we are developing and deploying are based on
  interconnected machine learning components. There is a need for 
  AI-assisted design and monitoring of these systems to ensure they perform
  robustly, safely and accurately in their deployed environment. We address 
  the entire pipeline of AI system development, from data acquisition to 
  decision making. 
  
  Data Oriented Architectures are an ecosystem that includes system monitoring for performance, 
  interpretability and fairness. The will enable us to move from individual component optimisation to full system monitoring and optimisation.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-12-04
venue: The Alan Turing Institute Fellows Welcome Event
transition: None
progress: False
---

\include{talk-macros.tex}


\include{_ai/includes/the-promise-of-ai.md}

\notes{This proposal is about addressing that gap, but to first understand the gap, let's look at comparisons between the approach we take to systems design, and the way that natural systems evolve.}

\notes{Artificial Intelligence (AI) solutions
are based on machine learning algorithms (ML), but each ML
solution is only capable of solving a restricted task, e.g. a
supervised learning problem. Consequently, any AI that we deploy today
takes the form of an ML System with interacting
components. As these ML systems become larger and more complex,
challenges in interpretation, explanation, accuracy and fairness
arise. This project addresses these issues. The challenges
include [@Lawrence:threeds19]: the *decomposition* of the system, the
*data* availability, and the performance of the system in
*deployment*. Collectively we refer to these challenges as the "Three
Ds of ML Systems Design".}

\include{_ai/includes/turing-ai-fellowship.md}



\include{_ai/includes/ride-allocation-prediction.md}

\include{_ai/includes/the-promise-of-ai.md}

\notes{Currently, our main approach to systems design involves designing a system in a component-wise manner. Attempts to replicate the capabilities of evolved systems through specifying the objective, rather than evolving behaviour.}

\notes{This gives vulnerabilities that we are exposing to the natural environment. Many security problems that we face today are the result of bugs that mean that code and data are not separate in thee systems we deploy, imagine what will happen when we deploy systems that purposefully short-circuit this protection into uncontrolled environments.}

\subsection{The Three Ds of Machine Learning Systems Design}

\slides{
* Three primary challenges of Machine Learning Systems Design.
1. Decomposition
2. Data 
3. Deployment
}
\notes{We can characterize the challenges for integrating machine learning within our systems as the three Ds. Decomposition, Data and Deployment.}

\addblog{The 3Ds of Machine Learning Systems Design}{2018/11/05/the-3ds-of-machine-learning-systems-design}

\include{_ml/includes/ml-paradigm-shift.md}
\include{_uq/includes/bayesian-system-optimization.md}
\include{_uq/includes/auto-ai.md}
\include{_data-science/includes/data-oriented-conclusions.md}

\thanks

\define{appendixOn}
\slides{

\subsection{APPENDIX} 

\include{_ml/includes/ml-three-primary-challenges.md}
\include{_ml/includes/ml-decomposition-challenge.md}
\include{_ml/includes/ml-data-challenge.md}
\include{_ml/includes/ml-combining-data-and-systems-design-challenge.md}
\include{_ml/includes/ml-deployment-challenge.md}

\include{_uq/includes/emulation.md}
\include{_uq/includes/deep-emulation.md}
\include{_uq/includes/bayesian-system-optimization.md}
\include{_uq/includes/auto-ai.md}}

\references


