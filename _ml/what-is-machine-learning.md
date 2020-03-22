---
layout: slides
title: What is Machine Learning?
venue: Data Science Africa Summer School, Addis Ababa, Ethiopia
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
abstract: >
  In this talk we will introduce the fundamental ideas in machine learning. We'll develop our exposition around the ideas of prediction function and the objective function. We don't so much focus on the derivation of particular algorithms, but more the general principles involved to give an idea of the machine learning *landscape*.
date: 2019-06-03
categories:
- notes
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

\include{../talk-macros.gpp}

\section{Introduction}

\include{_data-science/includes/data-science-africa.md}
\include{_health/includes/malaria-gp.md}

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
\figure{\includediagram{../slides/diagrams/data-science/new-flow-of-information}{60%}}{Large amounts of data and high interconnection bandwidth mean that we receive much of our information about the world around us through computers.}{data-science-information-flow}

\include{_supply-chain/includes/supply-chain-africa.md}
\include{_ml/includes/process-emulation.md}

\newslide{Kapchorwa District}

\figure{\includediagramclass{../slides/diagrams/health/Kapchorwa_District_in_Uganda}{50%}}{The Kapchorwa District, home district of Stephen Kiprotich.}{kapchorwa-district-in-uganda}

\notes{Stephen Kiprotich, the 2012 gold medal winner from the London Olympics, comes from Kapchorwa district, in eastern Uganda, near the border with Kenya.}

\include{_ml/includes/olympic-marathon-polynomial.md}
\include{../_ml/includes/what-does-machine-learning-do.md}

\include{_ml/includes/what-is-ml-2.md}
\include{_ai/includes/ai-vs-data-science-2.md}
\include{_ml/includes/neural-networks.md}

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
\include{_ml/includes/supervised-learning.md}
<!-- Leave unsupervised and reinforcement learning in the notes -->
\notes{
\include{_ml/includes/unsupervised-learning.md}
\include{_ml/includes/reinforcement-learning.md}

\notes{We have introduced a range of machine learning approaches by focusing on their use of mathematical functions to replace manually coded systems of rules. The important characteristic of machine learning is that the form of these functions, as dictated by their parameters, is determined by acquiring data from the real world.}


\include{_ml/includes/deployment.md}}

\thanks

\references
