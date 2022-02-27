---
title: "AutoAI: Systems, Machine Learning and Mathematics"
abstract: >
  Deployed artificial intelligence solutions consist of interacting components often trained as the result of *supervised machine learning*. Automatic training of these sub-components is known as AutoML. But the real world challenges of deployment consist of the monitoring of system performance in the real world, in terms of accuracy but also for fairness and bias. 
  
  To make such systems easily maintainable there is a need for automation of the process of monitoring and redeploying models as well as checking the quality of the overall system decomposition. 
  
  In contrast to AutoML, we call this system-wide approach "Auto AI". This is the subject of my Turing Fellowship 
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
blog: 
date: 2020-12-16
venue: Isaac Newton Institute Virtual Christmas Dinner
transition: None
---

talk-macros.gpp}lk-macros.gpp}

talk-macros.gpp}i/includes/the-great-ai-fallacy.md}

\slides{
\newslide{Intellectual Debt}

\figure{\includepng{\diagramsDir/ai/2020-02-12-intellectual-debt}{70%}}{Jonathan Zittrain's term to describe the challenges of explanation that come with AI is Intellectual Debt.}{intellectual-debt}

}
\notes{talk-macros.gpp}i/includes/intellectual-debt-short.md}}
talk-macros.gpp}i/includes/fit-systems.md}
talk-macros.gpp}i/includes/buying-system.md}
talk-macros.gpp}i/includes/buying-to-banking.md}
talk-macros.gpp}q/includes/emulation.md}

talk-macros.gpp}l/includes/neil-newton-institute.md}

\notes{The first tutorial I saw on Gaussian processes was given by [Chris Williams](https://homepages.inf.ed.ac.uk/ckiw/) at the Newton Institute in August 1997. The school was part of a program on Generalisation in Neural Networks and Machine Learning organised by my PhD supervisor, [Chris Bishop](https://www.microsoft.com/en-us/research/people/cmbishop/) (now Director of Microsoft Research in Cambridge).}

talk-macros.gpp}p/includes/gp-intro-very-short.md}

talk-macros.gpp}q/includes/deep-emulation.md}



\slides{\newslide{Mathematically}

* Composite *multivariate* function
  $$
  \mathbf{g}(\inputVector)=\mappingFunctionVector_5(\mappingFunctionVector_4(\mappingFunctionVector_3(\mappingFunctionVector_2(\mappingFunctionVector_1(\inputVector))))).
  $$

\newslide{Equivalent to Markov Chain}
* Composite *multivariate* function
  $$
  p(\dataVector|\inputVector)= p(\dataVector|\mappingFunctionVector_5)p(\mappingFunctionVector_5|\mappingFunctionVector_4)p(\mappingFunctionVector_4|\mappingFunctionVector_3)p(\mappingFunctionVector_3|\mappingFunctionVector_2)p(\mappingFunctionVector_2|\mappingFunctionVector_1)p(\mappingFunctionVector_1|\inputVector)
  $$

\figure{\includediagram{\diagramsDir/deepgp/deep-markov}{80%}}{Probabilistically the deep Gaussian process can be represented as a Markov chain. Indeed they can even be analyzed in this way [@Dunlop:deep2017].}{deep-markov}


}



\notes{talk-macros.gpp}eepgp/includes/process-composition.md}}

\newslide{}

\figure{\includediagram{\diagramsDir/gp/step-function-gp}{80%}}{Gaussian process fit to the step function data. Note the large error bars and the over-smoothing of the discontinuity. Error bars are shown at two standard deviations.}{step-function-gp}

\notes{talk-macros.gpp}eepgp/includes/step-function-deep-gp.md}}

\newslide{}

\slides{\figure{\includediagram{\diagramsDir/deepgp/step-function-deep-gp}{80%}}{Deep Gaussian process fit to the step function data.}{step-function-deep-gp}}

\newslide{}

\slides{\figure{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-samples}{80%}}{Samples from the deep Gaussian process model for the step function fit.}{step-function-deep-gp-samples}}

\slides{
\newslide{Step Function Data Latent 1}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-0}}

\newslide{Step Function Data Latent 2}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-1}}

\newslide{Step Function Data Latent 3}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-2}}

\newslide{Step Function Data Latent 4}

\slides{\includediagram{\diagramsDir/deepgp/step-function-deep-gp-layer-3}}}



\newslide{Operational Science}

* Automate the process of *explaining* and maintaining ML Systems.
* Challenge is these systems are highly complex:
   * Flaws need rapid addressing.
* This becomes apparent in operational science

\newslide{Pandemic}

* Been working with the DELVE Group 
* One perspective on challenge facing government:
   * Intellectual Debt for the whole country
   * Ideas about *explaining* a complex system much wider applicability.
* Implications for *digital twins*

\thanks

\references


