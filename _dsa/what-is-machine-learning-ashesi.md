---
layout: slides
title: What is Machine Learning?
venue: Data Science Africa Summer School, Ashesi, Ghana
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: University of Cambridge
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
abstract: >
  In this talk we will introduce the fundamental ideas in machine learning. We'll develop our exposition around the ideas of prediction function and the objective function. We don't so much focus on the derivation of particular algorithms, but more the general principles involved to give an idea of the machine learning *landscape*.
date: 2019-10-21
categories:
- notes
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

talk-macros.gpp}/talk-macros.tex}

\section{Introduction}

talk-macros.gpp}ata-science/includes/data-science-africa.md}
talk-macros.gpp}ealth/includes/malaria-gp.md}

\subsection{Machine Learning}
\notes{This talk is a general introduction to machine learning, we will highlight the technical challenges and the current solutions. We will give an overview of what is machine learning and why it is important.}

\subsection{Rise of Machine Learning}
\slides{
* Driven by data and computation
* Fundamentally dependent on models
}\notes{Machine learning is the combination of data and models, through computation, to make predictions.}
$$
\text{data} + \text{model} \stackrel{\text{compute}}{\rightarrow} \text{prediction}
$$

\subsection{Data Revolution}

\notes{Machine learning has risen in prominence due to the rise in data availability, and its interconnection with computers. The high bandwidth connection between data and computer leads to a new interaction between us and data via the computer. It is that channel that is being mediated by machine learning techniques.}
\figure{\includediagram{\diagramsDir/data-science/new-flow-of-information}{60%}}{Large amounts of data and high interconnection bandwidth mean that we receive much of our information about the world around us through computers.}{data-science-information-flow}

talk-macros.gpp}upply-chain/includes/supply-chain-africa.md}
talk-macros.gpp}l/includes/process-emulation.md}
talk-macros.gpp}l/includes/nigeria-nmis-data.md}
talk-macros.gpp}l/includes/what-does-machine-learning-do.md}
talk-macros.gpp}l/includes/what-is-ml-2.md}
talk-macros.gpp}i/includes/ai-vs-data-science-2.md}
talk-macros.gpp}l/includes/neural-networks.md}

\subsection{Machine Learning}
\slides{
1. observe a system in practice
2. emulate its behavior with mathematics.

* Design challenge: where to put mathematical function.
* Where it's placed leads to different ML domains.
}\notes{The key idea in machine learning is to observe the system in practice, and then emulate its behavior with mathematics. That leads to a design challenge as to where to place the mathematical function. The placement of the mathematical function leads to the different domains of machine learning.}

\newslide{Types of Machine Learning}

1. Supervised learning
2. Unsupervised learning
3. Reinforcement learning

\newslide{Types of Machine Learning}
\slides{
1. Supervised learning
2. <s>Unsupervised learning</s>
3. <s>Reinforcement learning</s>
}


talk-macros.gpp}l/includes/supervised-learning-intro.md}

talk-macros.gpp}l/includes/classification-intro.md}
talk-macros.gpp}l/includes/classification-examples.md}
talk-macros.gpp}l/includes/the-perceptron.md}
\notes{talk-macros.gpp}l/includes/logistic-regression.md}
talk-macros.gpp}l/includes/nigeria-nmis-data-logistic.md}}
talk-macros.gpp}l/includes/regression-intro.md}
talk-macros.gpp}l/includes/regression-examples.md}
talk-macros.gpp}l/includes/olympic-marathon-polynomial.md}

talk-macros.gpp}l/includes/supervised-learning-challenges.md}

<!-- Leave unsupervised and reinforcement learning in the notes -->
\notes{
talk-macros.gpp}l/includes/unsupervised-learning.md}
talk-macros.gpp}l/includes/reinforcement-learning.md}

\notes{We have introduced a range of machine learning approaches by focusing on their use of mathematical functions to replace manually coded systems of rules. The important characteristic of machine learning is that the form of these functions, as dictated by their parameters, is determined by acquiring data from the real world.}


talk-macros.gpp}l/includes/deployment.md}}

\reading

\thanks

\references
