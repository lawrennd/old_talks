---
week: 4
session: 2
title: "The Challenges of Data Science"
featured_image: assets/images/the-challenges-of-data-science.png
abstract:  >
  In the first lecture, we laid out the underpinning phenomena that give us the landscape of data science. In this lecture we unpick the challenges that landscape presents us with. The material gives you context for why data science is very different from standard software engineering, and how data science problems need to be approached including the many different aspects that need to be considered. We will look at the challenges of deploying data science solutions in practice. We categorize them into three groups.
layout: lecture
venue: LT2, William Gates Building
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
oldyoutube: 
- code: BQKfIJHPiCQ
  year: 2022
- code: KXnZ4nj-ahA
  year: 2021
youtube: BQKfIJHPiCQ
time: "10:00"
date: 2023-10-30
transition: None
ipynb: false
---

\section{Introduction}

\notes{Data science is an emerging discipline. That makes it harder to make clean decisions about what any given individual will need to know to become a data scientist. Those of you who are studying now will be those that define the discipline. As we deploy more data driven decision making in the world, the role will be refined. Until we achieve that refinement, your knowledge needs to be broad based.}

\notes{In this lecture we will first continue our theme of how our limitations as humans mean that our analysis of data can be affected, and I will introduce an analogy that should help you understand *how* data science differs significantly from traditional software engineering. We'll then contextualize some of the challenges the domain into three different groups.}

\newslide{Background: Big Data}
\slides{
* Data is Pervasive phenomenon that affects all aspects of our activities

* Data diffusiveness is both a challenge and an opportunity
}
\include{_data-science/includes/gartner-hype-cycle-ai-bd-dm-dl-ml.md}
\include{_ml/includes/what-is-ml.md}

\subsection{Classical Statistical Analysis}

\slides{* Remain more important than ever.
* Provide sanity checks for our ideas and code.
* Enable us to visualize our analysis bugs.}

\notes{Despite the shift of emphasis, traditional statistical techniques are more important than ever. One of the few ways we have to validate the analyses we create is to make use of visualizations, randomized testing and other forms of statistical analysis. You will have explored some of these ideas in earlier courses in machine learning. In this unit we provide some review material in a practical sheet to bring some of those ideas together in the context of data science.}


\include{_ml/includes/what-does-machine-learning-do.md}
\include{_ml/includes/data-science-vs-ai.md}

\include{_data-science/includes/data-science-as-debugging.md}
\include{_ai/includes/conversation-probability.md}

\include{_ai/includes/the-ai-bogeyman.md}
\include{_ai/includes/conversation-llm.md}
\include{_ai/includes/human-analogue-machines.md}

\subsection{Conclusions}

\notes{In today's lecture we've drilled down further on a difficult aspect of data science. By focusing too much on the data and the technical challenges we face, we can forget the context. But to do data science well, we must not forget the context of the data. We need to pay attention to domain experts and introduce their understanding to our analysis. Above all we must not forget that data is almost always (in the end) about people.}

\slides{* By focussing on the technical side of data science
* We tend to forget about the context of the data.
* Don't forget that data is almost always about people.}

\references

\thanks
