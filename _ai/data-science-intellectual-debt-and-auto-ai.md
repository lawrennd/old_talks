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
Didn't have a chance to give you feedback during the call, so here goes:
- Saying that tech debt originated from Lean is just an insult to Lean. Lean isn't about developing prototypes and taking shortcuts. It can lead to tech debt, but so can other approaches! If you need one most common cause of tech debt, I would name time constraints and poor risk management, not Lean methodology.
- When introducing DOA, it isn't immediately obvious that streams are at a heart of it. And then Milan comes a bit of a surprise.
- It's probably worth spending a minute discussing how the ride booking system could be built using today's approaches, in service oriented way. Just saying "service A called service B with that input and got that answer, both of which are never stored" would make it immediately clear how the data is dissappearing.
- Emukit page looks really out of place, it's isn't as famous as we'd like to it be. So maybe just replace it with a quick intution about emulator are?
talk-macros.gpp}lk-macros.tex}

talk-macros.gpp}i/includes/ml-systems-design-short.md}
talk-macros.gpp}i/includes/ride-allocation-prediction.md}
talk-macros.gpp}i/includes/fit-systems.md}
talk-macros.gpp}i/includes/intellectual-debt.md}

talk-macros.gpp}i/includes/ml-system-decomposability.md}

talk-macros.gpp}i/includes/the-great-ai-fallacy.md}

talk-macros.gpp}ata-science/includes/data-oriented-architectures-short.md}
talk-macros.gpp}ata-science/includes/milan.md}
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







