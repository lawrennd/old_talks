---
title: "From Innovation to Deployment"
subtitle: "Auto AI and Machine Learning Systems Design"
abstract: >
  In this talk we introduce a five year project funded by the UK's Turing Institute to shift the focus from developing AI systems to deploying AI systems that are safe and reliable. 
  
  The AI systems we are developing and deploying are based on
  interconnected machine learning components. There is a need for 
  AI-assisted design and monitoring of these systems to ensure they perform
  robustly, safely and accurately in their deployed environment. We address 
  the entire pipeline of AI system development, from data acquisition to 
  decision making. 
  
  Data Oriented Architectures are an ecosystem that includes system monitoring for performance, 
  interpretability and fairness. The will enable us to move from individual component optimisation to full system monitoring and optimisation.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
pptx: False
docx: False
pdfnotes: False
ipynb: False
date: 2019-11-22
venue: AIDA Team, Alan Turing Institute
transition: None
---

talk-macros.gpp}lk-macros.tex}

\subsection{Introduction}

\notes{Artificial Intelligence (AI) solutions
are based on machine learning algorithms (ML), but each ML
solution is only capable of solving a restricted task, e.g. a
supervised learning problem. Consequently, any AI that we deploy today
takes the form of an ML System with interacting
components. As these ML systems become larger and more complex,
challenges in interpretation, explanation, accuracy and fairness
arise. This project addresses these issues. The challenges
include [@Lawrence:threeds19]: the *decomposition* of the system, the
*data* availability, and the performance of the system in
*deployment*. Collectively we refer to these challenges as the "Three
Ds of ML Systems Design".}

talk-macros.gpp}i/includes/turing-ai-fellowship.md}


\newslide{Announcement}
\slides{
* Five year program in collaboration with 


  \aligncenter{[Element AI](https://www.elementai.com/)}


  \aligncenter{[Open ML](https://openml.org)}


  \aligncenter{[Professor Sylvie Delacroix](https://www.birmingham.ac.uk/staff/profiles/law/delacroix-sylvie.aspx)}


  \aligncenter{and}


  \aligncenter{[Data Science Africa!](http://datascienceafrica.org)}
}
\notes{The [Turing Institute announced](https://www.turing.ac.uk/news/welcoming-world-class-turing-ai-fellows-institute) that this work has been funded through a Turing Institute Senior AI Fellowship. This is the first Senior AI fellowship and it provides funding for five years. 

The project partners are [Element AI](https://www.elementai.com/),  [Open ML](https://openml.org), [Professor Sylvie Delacroix](https://www.birmingham.ac.uk/staff/profiles/law/delacroix-sylvie.aspx) and [Data Science Africa](http://datascienceafrica.org).}

\subsection{Inclusive Project}

There is no way that the team we're building will be able to deliver on this agenda alone, so please join us in addressing these challenges! 

talk-macros.gpp}i/includes/ride-allocation-prediction.md}

talk-macros.gpp}i/includes/the-promise-of-ai.md}

\notes{This proposal is about addressing that gap, but to first understand the gap, let's look at comparisons between the approach we take to systems design, and the way that natural systems evolve.}

talk-macros.gpp}i/includes/artificial-vs-natural-systems-short.md}

\notes{Currently, our main approach to systems design involves designing a system in a component-wise manner. Attempts to replicate the capabilities of evolved systems through specifying the objective, rather than evolving behaviour.}

talk-macros.gpp}i/includes/ml-system-decomposability.md}
talk-macros.gpp}l/includes/ml-paradigm-shift.md}

\notes{This gives vulnerabilities that we are exposing to the natural environment. Many security problems that we face today are the result of bugs that mean that code and data are not separate in thee systems we deploy, imagine what will happen when we deploy systems that purposefully short-circuit this protection into uncontrolled environments.}

talk-macros.gpp}i/includes/intelligent-system-paolo.md}
talk-macros.gpp}i/includes/peppercorn.md}

\subsection{The Three Ds of Machine Learning Systems Design}

\slides{
* Three primary challenges of Machine Learning Systems Design.
1. Decomposition
2. Data 
3. Deployment
}
\notes{We can characterize the challenges for integrating machine learning within our systems as the three Ds. Decomposition, Data and Deployment.}

\addblog{The 3Ds of Machine Learning Systems Design}{2018/11/05/the-3ds-of-machine-learning-systems-design}

\notes{The first two components *decomposition* and *data* are interlinked, but we will first outline the decomposition challenge. Below we will mainly focus on *supervised learning* because this is arguably the technology that is best understood within machine learning.}

\newslide{The Three Ds of Machine Learning Systems Design}

\slides{
* Three primary challenges of Machine Learning Systems Design.
1. <s>Decomposition</s>
2. Data
3. <s>Deployment</s>
}
\notes{In this talk, we will focus on the second challenge, the data challenge.}

talk-macros.gpp}l/includes/ml-data-challenge.md}

talk-macros.gpp}i/includes/ml-system-decomposability.md}
talk-macros.gpp}i/includes/ride-allocation-prediction.md}

talk-macros.gpp}ata-science/includes/data-oriented-architectures.md}

talk-macros.gpp}q/includes/emulation.md}
talk-macros.gpp}q/includes/deep-emulation.md}
talk-macros.gpp}q/includes/bayesian-system-optimization.md}
talk-macros.gpp}q/includes/auto-ai.md}

talk-macros.gpp}ata-science/includes/data-oriented-conclusions.md}



\thanks

\references


