---
week: 5
session: 2
title: "The Challenges of Data Science"
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
time: "10:00"
date: 2021-11-08
transition: None
ipynb: false
---

\section{Introduction}

\notes{Data science is an emerging discipline. That makes it harder to make clean decisions about what any given individual will need to know to become a data scientist. Those of you who are studying now will be those that define the discipline. As we deploy more data driven decision making in the world, the role will be refined. Until we achieve that refinement, your knowledge needs to be broad based.}

\notes{In this lecture we will first continue our theme of how our limitations as humans mean that our analysis of data can be effected, and I will introduce an analogy that should help you understand *how* data science differs significantly from traditional software engineering. We'll then contextualize some of the challenges the domain into three different groups.}


\include{_ml/includes/what-does-machine-learning-do.md}
\include{_ml/includes/data-science-vs-ai.md}

\include{_data-science/includes/data-science-as-debugging.md}

\include{_psychology/includes/selective-attention-bias.md}
\define{bmiStepsAnalysis}
\include{_data-science/includes/data-inattention-bias.md}

\include{_data-science/includes/three-data-science-challenges.md}
\notes{You can also check this \addblog{Three Data Science Challenges}{2016/07/01/data-science-challenges}.}
\include{_data-science/includes/societal-effects.md}
\include{_data-science/includes/big-data-paradox.md}
\include{_data-science/includes/breadth-or-depth.md}
\include{_data-science/includes/big-model-paradox.md}
\include{_data-science/includes/value-of-data.md}
\include{_data-science/includes/privacy-intro.md}
\include{_data-science/includes/hate-speech-or-political-dissent.md}
\include{_data-science/includes/marketing-and-free-will.md}
\include{_data-science/includes/digital-revolution-and-inequality.md}
\include{_data-science/includes/privacy-amelioration.md}
\include{_data-science/includes/data-science-africa.md}
\include{_governance/includes/data-governance-toolkit.md}
\include{_governance/includes/data-trusts.md}

\subsection{Conclusions}

\notes{In today's lecture we've drilled down further on a difficult aspect of data science. By focussing to much on the data and the technical challenges we face, we can forget the context. But to do data science well, we must not forget the context of the data. We need to pay attention to domain experts introduce their understanding to our analysis. Above all we must not forget that data is almost always (in the end) about people.}

\notes{We separated the challenges we face into three groups: (1) paradoxes of the odern data society, (2) quantifying the value of data and (3) privacy loss of control and marginalization. We've noted the origins of the paradoxes, speculating that it is based in a form of data (or modelling) inattention bias demonstrated through the Gorilla. We've drawn parallels between challenges of rewarding the addition of value and the credit assignment problem in reinforecement learning and we've looked at approaches to introduce the voice of marginalized societies and people into the conversation.}

\slides{* Must not forget *context* of data.
* Three challenges:
  1. Paradoxes of Data Society
  2. Quantifying value of data
  3. Privacy, loss of control and marginalization
  * Place *people* at the heart.}


\references

\thanks
