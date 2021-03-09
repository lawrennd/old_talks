---
title: "Interpretable Models"
subtitle: “AI and Intellectual Debt”
abstract: >
  The great AI fallacy is that we are building the first generation of automation that will adapt to humans rather than humans adapting to us. The more sobering reality is that we are building complex algorithmic decision making system that we are unable to explain.
  
  A FIT model is fair, interpretable and transparent. The machine learning community has placed effort into understanding how to improve interpretability into individual models, but the real challenge is how to build FIT systems. 

  At the heart of the development of machine learning is the notion of separation of concerns, but this can obscure the real challenge which is responding to the human.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2021-03-09
venue: Virtual Interaction with Machine Learning Course
transition: None
---

\include{talk-macros.gpp}

\include{_ai/includes/the-great-ai-fallacy.md}

\include{_software/includes/separation-of-concerns.md}
\include{_software/includes/mythical-man-month.md}
\include{_ai/includes/ml-system-decomposability.md}

\include{_ai/includes/embodiment-factors-celsius.md}
\include{_ai/includes/conversation-tedx.md}
\include{_ai/includes/heider-simmel.md}
\include{_ai/includes/conversation-computer.md}

\include{_ml/includes/data-science-vs-ai.md}

\include{_ai/includes/ride-allocation-prediction.md}

\include{_ai/includes/ml-systems-design-short.md}

\include{_business/includes/bezos-question-mark-email.md}

\include{_ai/includes/intellectual-debt-short.md}
\include{_ai/includes/fit-systems.md}
\include{_ai/includes/buying-system.md}
\include{_ai/includes/buying-to-banking.md}

\include{_governance/includes/how-gdpr-may-help.md}

\include{_uq/includes/statistical-emulation.md}

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


