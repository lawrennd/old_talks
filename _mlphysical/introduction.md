---
week: 1
session: 1
title: "Introduction: ML and the Physical World"
abstract:  >
  This lecture will introduce the course and provide a motivation and a historical account of machine learning and mathematical modelling. It will further detail the special challenges associated with the application of machine learning to physical systems. We will also outline the objectives of the course and how it will be structured over the term.
layout: lecture
time: "10:00"
date: 2020-10-08
transition: None
ipynb: true
---


\include{talk-macros.tex}

\include{_mlphysical/includes/overview-2020.md}
\include{_physics/includes/ceres-discovery.md}

\notes{Let's have a look at how Gauss determined the orbit of Ceres and how (taking ideas from Pierre Simon Laplace) he used approaches that would prove to be conceptually fundamental to machine learning and statistical approaches.}
\include{_ml/includes/overdetermined-inaugural.md}
\include{_physics/includes/entropy-intro.md}
\include{_ml/includes/underdetermined-system.md}
\include{_physics/includes/brownian-wiener.md}
\newslide{}

\subsection{Conclusions}

\slides{* Potted journey through history of physical models and uncertainty.
* Challenge we now face is *partial* uncertainty.
* This module will equip you with the skills to balance uncertainty, computation and observation in answering scientific questions.
}
\notes{In this introduction to the course, we've provided a potted journey through the history of science and our models of the physical world. In particular, we started with the deterministic world of Newton and moved towards a less certain, stochastic world, beautifully described by Laplace.}

\notes{Within statistical mechanics and electrical engineering the ideas of Laplace were rendered into mathematical reality. In particular through the use of probabilistic processes such as Gaussian processes.}

\notes{The challenge we face is one of partial ignorance. Not the total ignorance of Maxwell/Gibbs/Boltzmann or the determinism of Newton. But something in between.}

\notes{In this course, that ignorance won't only arise from lack of observation, but also from the need to run a (potentially) expensive simulation. Our aim will be to introduce you to the ideas of surrogate modeling, that allow us to trade off our current knowledge, with our possible knowledge, where data can be acquired through observation or simulation to render an answer to a question.}

\notes{In the next set of lectures you will obtain a more rigorous grounding in uncertainty and the mathematics and creation of Gaussian process models. We will then use these tools to show how a range of decisions can be made through combination of these surrogate models with simulations.}


\references

