---
title: "Auto AI"
subtitle: "Resolving Intellectual Debt in Complex Systems"
abstract: >
  Machine learning solutions, in particular those based on deep learning methods, form an underpinning of the current revolution in “artificial intelligence” that has dominated popular press headlines and is having a significant influence on the wider tech agenda. 
  
  Our capability to deploy complex decision-making systems has improved, but our ability to explain them has reduced. This phenomenon is known as intellectual debt.
  
  The reality of deployed systems is they are constructed from interacting components of individual models. While a lot of focus has been on the explainability and reliability of an individual model, the real challenge is explainability and reliability of the entire system. 
    
  In this talk we introduce the concept of Auto AI and give a road map to achieving fair, explainable and transparent AI systems. 
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2021-03-23
venue: "The Turing Presents: AI UK"
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






