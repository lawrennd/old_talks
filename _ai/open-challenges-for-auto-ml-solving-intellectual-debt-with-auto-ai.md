---
title: Open Challenges for Automated Machine Learning: Solving Intellectual Debt with Auto AI
abstract: Machine learning models are deployed as part of wider systems where outputs of one model are consumed by other models. This composite structure for machine learning systems is the dominant approach for deploying artificial intelligence. Such deployed systems can be complex to understand, they bring with them intellectual debt. In this talk we'll argue that the next frontier for automated machine learning is to move to automation of the systems design, going from AutoML to AutoAI.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-07-18
venue: ICML Workshop on Automated Machine Learning
transition: None
---

\include{talk-macros.tex}

\include{_ai/includes/artificial-vs-natural-systems.md}

\include{_ai/includes/ml-system-decomposability.md}
\include{_ai/includes/ride-allocation-prediction.md}

\include{_ai/includes/ml-systems-design-short.md}
\include{_data-science/includes/the-data-crisis.md}

\include{_ml/includes/ml-paradigm-shift.md}
\include{_ai/includes/peppercorn.md}


\include{_uq/includes/emulation.md}
\include{_gp/includes/gp-intro-very-short.md}
\include{_uq/includes/deep-emulation.md}


\newslide{Emulation}

\figure{\includediagram{\diagramsDir/uq/statistical-emulation004}{80%}}{A statistical emulator is a system that reconstructs the simulation with a statistical model. As well as reconstructing the simulation, a statistical emulator can be used to correlate with the real world.}{statistical-emulation-5}

\subsection{Conclusion}
\slides{
* AI is fundamentally ML System Design
* We are not ready to deploy automation in uncontrolled environments.
* Until we can monitoring and update will be key.
}
\notes{Today's artificial intelligence is fundamentally Machine Learning Systems design, but the systems we are building will not fulfill the promises we are making for them. We are not yet ready to deploy automation in fully uncontrolled environments. Until we modify our approaches we will not be able to deliver on the promise. Until then, monitoring and upadate of deployed systems will be key to practical and safe AI.}

\thanks

\references







