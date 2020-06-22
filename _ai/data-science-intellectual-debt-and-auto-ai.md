---
layout: talk
title: "Data Science, Intellectual Debt and Auto AI"
abstract: Machine learning models are deployed as part of wider systems where outputs of one model are consumed by other models. This composite structure for machine learning systems is the dominant approach for deploying artificial intelligence. Such deployed systems can be complex to understand, they bring with them intellectual debt. In this talk we'll argue that the next frontier for automated machine learning is to move to automation of the systems design, going from AutoML to AutoAI.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-06-23
venue: Advances in Data Science
transition: None
---

25 mins + 10 mins for quests

\include{talk-macros.tex}

\include{_ai/includes/the-great-ai-fallacy.md}
\include{_ai/includes/ml-systems-design-short.md}
\include{_ai/includes/intellectual-debt.md}

\include{_ai/includes/ml-system-decomposability.md}
\include{_ai/includes/ride-allocation-prediction.md}

\include{_ai/includes/fit-systems.md}
\include{_data-science/includes/data-oriented-architectures-short.md}
\include{_data-science/includes/milan.md}
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







