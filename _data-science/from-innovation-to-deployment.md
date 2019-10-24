---
title: "Data Oriented Architectures"
abstract: >
  There has been a great deal of interest in probabilistic programs:
  placing modeling at the heart of programming language. In this talk
  we set the scene for data oriented programming.
  
  Data is a fundamental component of machine learning, yet the
  availability, quality and discoverability of data are often ignored
  in formal computer science.
  
  While languages for data manipulation exist (for example SQL), they
  are not suitable for the modern world of machine learning
  data. Modern data oriented languages should place data at the center
  of modern digital systems design and provide an infrastructure in
  which monitoring of data quality and model decision making are
  automaticaly available.
  
  We provide the context for Modern Data Oriented Programming, and
  give some insight into our initial ideas in this space.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
blog: 
date: 2019-10-23
venue: Data Science Africa, Ashesi University
transition: None
---

\include{talk-macros.tex}

\include{_ai/includes/centrifugal-governor.md}

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

\subsection{Announcement}
\slides{
* Today [the Turing Institute announced](https://www.turing.ac.uk/news/welcoming-world-class-turing-ai-fellows-institute) that this work would be funded as the inaugural "Senior Artificial Intelligence Fellow". 
}

\subsection{Announcement}
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


\thanks

\references


