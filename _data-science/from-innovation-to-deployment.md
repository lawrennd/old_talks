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
blog: 
date: 2019-10-24
venue: Data Science Africa, Ashesi University
transition: None
---

\include{talk-macros.tex}

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

\subsection{Aim}

\notes{Our aim is to scale our ability to deploy safe and reliable AI
solutions. Our technical approach is to do this through *data-oriented
software engineering* practices and *deep system emulation*. We will do this through  a
significant extension of the notion of Automated ML
(AutoML) to Automated AI (AutoAI), this relies on a shift from Bayesian Optimisation to *Bayesian System Optimisation*. The project will
develop a toolkit for automating the deployment, maintenance and
monitoring of artificial intelligence systems.}

\slides{
* Scale safe and reliable AI solutions. 
* Move from Auto ML to Auto AI
* Bayesian Optimisation to Bayesian System Optimisation
}


\section{Motivating Example}

\include{_ai/includes/safe-boda.md}

\subsection{Announcement}
\slides{
* Today [the Turing Institute announced](https://www.turing.ac.uk/news/welcoming-world-class-turing-ai-fellows-institute) that this work would be funded as the inaugural "Senior Artificial Intelligence Fellow". 
}

\newslide{Announcement}
\slides{
* Five year program in collaboration with 

. . .

  \aligncenter{[Element AI](https://www.elementai.com/)}

. . .

  \aligncenter{[Open ML](https://openml.org)}

. . .

  \aligncenter{[Professor Sylvie Delacroix](https://www.birmingham.ac.uk/staff/profiles/law/delacroix-sylvie.aspx)}

. . .

  \aligncenter{and}

. . .

  \aligncenter{[Data Science Africa!](http://datascienceafrica.org)}
}
\notes{As of 24th October 2019, the [Turing Institute announced](https://www.turing.ac.uk/news/welcoming-world-class-turing-ai-fellows-institute) that this work has been funded through a Turing Institute Senior AI Fellowship. This is the first Senior AI fellowship and it provides funding for five years. 

The project partners are [Element AI](https://www.elementai.com/),  [Open ML](https://openml.org), [Professor Sylvie Delacroix](https://www.birmingham.ac.uk/staff/profiles/law/delacroix-sylvie.aspx) and [Data Science Africa!](http://datascienceafrica.org).}

\include{_ai/includes/ride-allocation-prediction.md}

\include{_ai/includes/artificial-vs-natural-systems.md}
\include{_ai/includes/ml-system-decomposability.md}
\include{_ml/includes/ml-paradigm-shift.md}

\include{_ai/includes/intelligent-system-paolo.md}
\include{_ai/includes/peppercorn.md}

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
2. <s>Data</s>
3. Deployment
}
\notes{In this talk, we will focus on the third challenge, the deployment challenge.}

\include{_ml/includes/ml-deployment-challenge.md}

\include{_ai/includes/ml-system-decomposability.md}
\include{_ai/includes/ride-allocation-prediction.md}

\include{_data-science/includes/data-oriented-architectures.md}

\include{_uq/includes/emulation.md}
\include{_uq/includes/deep-emulation.md}
\include{_uq/includes/bayesian-system-optimization.md}
\include{_uq/includes/auto-ai.md}

\include{_data-science/includes/data-oriented-conclusions.md}



\thanks

\references


