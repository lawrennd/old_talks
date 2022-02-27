---
title: "Deploying Machine Learning: Intellectual Debt and AutoAI"
abstract: >
  From the dawn of cybernetics, and across the last eight decades, we’ve worked to make machine learning methods successful. But now that these methods are being widely adopted we need to deal with the consequences of success. Many of those consequences can only be understood when a holistic approach to the machine learning problem is considered: the deployment of a method within a context for a particular objective. In this circumstance, it’s easy to see that questions of interpretability, fairness and transparency are all contextual. In this talk we summarize this challenge using Jonathan Zittrain’s term of “intellectual debt”, we discuss how it pans out in reality and how this challenge could be addressed using machine learning techniques to give us “Auto AI”.
  
  This work is sponsored by an ATI Senior AI Fellowship.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
youtube: 5PdHgR6zz1o
date: 2020-10-06
venue: Virtual Advances in Data Science Seminar, Manchester
transition: None
---

talk-macros.gpp}lk-macros.tex}

talk-macros.gpp}i/includes/the-great-ai-fallacy.md}

talk-macros.gpp}i/includes/artificial-vs-natural-systems-short.md}

talk-macros.gpp}i/includes/intellectual-debt-short.md}
talk-macros.gpp}i/includes/buying-system.md}
talk-macros.gpp}i/includes/buying-to-banking.md}
talk-macros.gpp}i/includes/safe-boda.md}
talk-macros.gpp}i/includes/fit-systems.md}

talk-macros.gpp}i/includes/ride-allocation-prediction.md}

\section{A Solution}
talk-macros.gpp}ata-science/includes/data-oriented-architectures-short.md}
talk-macros.gpp}ata-science/includes/milan.md}

talk-macros.gpp}i/includes/fit-models-to-fit-systems.md}
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
\notes{Today's artificial intelligence is fundamentally Machine Learning Systems design, but the systems we are building will not fulfill the promises we are making for them (The Great AI Fallacy). We are not yet ready to deploy automation in fully uncontrolled environments due to major issues around *intellectual debt*. Until we modify our approaches we will not be able to deliver on the promise. Until then, monitoring and upadate of deployed systems will be key to practical and safe AI.}

\thanks

\references



