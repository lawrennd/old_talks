---
title: "Intellectual Debt and Artificial Intelligence"
abstract: >
  With the advent of machine learning driven artificial intelligence systems we have developed the ability to deploy highly complex decision making processes.
  
  Unfortunately, our ability to maintain and explain these systems has not kept up with our deployment capability.
  
  The former challenge is known as technical debt, the latter has been termed *intellectual debt*. 
    
  In this talk we introduce the concept of Auto AI and give a road map to ensuring that we can address the limitations of current deployment.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-03-25
venue: "Mastercard Evening"
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

\figure{\includediagram{../slides/diagrams/uq/statistical-emulation004}{80%}}{A statistical emulator is a system that reconstructs the simulation with a statistical model. As well as reconstructing the simulation, a statistical emulator can be used to correlate with the real world.}{statistical-emulation-5}

\subsection{Conclusion}
\slides{
* AI is fundamentally ML System Design
* We are not ready to deploy automation in uncontrolled environments.
* Until we can monitoring and update will be key.
}
\notes{Today's artificial intelligence is fundamentally Machine Learning Systems design, but the systems we are building will not fulfill the promises we are making for them. We are not yet ready to deploy automation in fully uncontrolled environments. Until we modify our approaches we will not be able to deliver on the promise. Until then, monitoring and upadate of deployed systems will be key to practical and safe AI.}

\thanks

\references






