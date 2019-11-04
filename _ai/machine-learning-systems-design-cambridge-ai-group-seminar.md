---
title: "Machine Learning Systems Design"
abstract: >
  Machine learning solutions, in particular those based on deep learning methods, form an underpinning of the current revolution in “artificial intelligence” that has dominated popular press headlines and is having a significant influence on the wider tech agenda. In this talk I will give an overview of where we are now with machine learning solutions, and what challenges we face both in the near and far future. These include practical application of existing algorithms in the face of the need to explain decision-making, mechanisms for improving the quality and availability of data, dealing with large unstructured datasets.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-11-05
venue: Cambridge AI Group Seminar
transition: None
---

\include{talk-macros.tex}

\include{_ai/includes/ride-allocation-prediction.md}
\include{_ai/includes/the-promise-of-ai.md}

\subsection{Project Description}

> It used to be true that computers only did what we programmed them to do, but today AI systems are learning from our data. This introduces new problems in how these systems respond to their environment. 
>
>We need to better monitor how data is influencing decision making and take corrective action as required. 
>
>This project addresses that challenge.


\include{_ai/includes/artificial-vs-natural-systems.md}

\include{_ai/includes/ml-system-decomposability.md}
\include{_ai/includes/ride-allocation-prediction.md}

\include{_ai/includes/ml-systems-design-short.md}
\include{_data-science/includes/the-data-crisis.md}

\include{_ml/includes/ml-paradigm-shift.md}

\include{_ai/includes/intelligent-system-paolo.md}

\include{_ai/includes/peppercorn.md}

<!-- remove the data challenge -->
\define{mlDataChallenge}

\include{_ml/includes/the-3ds-of-machine-learning-systems-design.md}

\subsection{The Machine Learning Bit}

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






