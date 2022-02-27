---
title: "AI and Intellectual Debt"
subtitle: “FIT Models must become FIT Systems”
abstract: >
  The great AI fallacy is that we are building the first generation of automation that will adapt to humans rather than humans adapting to us. The more sobering reality is that we are building complex algorithmic decision making system that we are unable to explain.
  
  A FIT model is fair, interpretable and transparent. The machine learning community has placed effort into understanding how to improve interpretability into individual models, but the real challenge is how to build FIT systems. 
  
  The core of this challenge comes from the phenomenon I refer to as the “Death of the Programmer”, where once your code is deployed you no longer control the uses to which it’s put. As a result a particular model designed for a specific context can be used differently from how it is intended. This leads to a phenomenon known as “Intellectual Debt” where a deployed system can be operational but its functioning cannot be explained by the designer.
  
  These challenges are particularly important in health applications, and they can be addressed, but it requires a fundamental reassessment of our approach to designing and deploying large scale software systems. 
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-03-22
venue: "Downing College"
transition: None
---

talk-macros.gpp}lk-macros.tex}

talk-macros.gpp}i/includes/artificial-vs-natural-systems.md}

talk-macros.gpp}i/includes/ml-system-decomposability.md}
talk-macros.gpp}i/includes/ride-allocation-prediction.md}

talk-macros.gpp}i/includes/ml-systems-design-short.md}
talk-macros.gpp}ata-science/includes/the-data-crisis.md}

talk-macros.gpp}l/includes/ml-paradigm-shift.md}
talk-macros.gpp}i/includes/peppercorn.md}


talk-macros.gpp}q/includes/emulation.md}
talk-macros.gpp}p/includes/gp-intro-very-short.md}
talk-macros.gpp}q/includes/deep-emulation.md}


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






