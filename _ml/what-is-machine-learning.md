---
layout: slides
title: What is Machine Learning?
venue: Data Science Africa Summer School
author: Neil D. Lawrence
abstract: >
  In this talk we will introduce the fundamental ideas in machine learning. We'll develop our exposition around the ideas of prediction function and the objective function. We don't so much focus on the derivation of particular algorithms, but more the general principles involved to give an idea of the machine learning *landscape*.
date: 2017-07-17
affiliation: Amazon and University of Sheffield
---

\include{../talk-macros.tex}

### Introduction

* General introduction to machine learning.

* Highlight technical challenges and current solutions.

* What is machine learning? And why is it important?

### Rise of Machine Learning

* Driven by data and computation

* Fundamentally dependent on models

$$
\text{data} + \text{model} + \text{compute} \rightarrow \text{prediction}
$$

### Data Revolution

\includesvg{../slides/diagrams/data-science-information-flow.svg}

*Large amounts of data and high interconnection bandwidth mean that we receive much of our information about the world around us through computers.*

\include{_ml/includes/process-automation.md}
\include{_ml/includes/process-emulation.md}
\include{_ml/includes/polynomial-fit.md}
\include{_ai/includes/ai-vs-data-science.md}

### Machine Learning

1. observe a system in practice

2. emulate its behavior with mathematics.

* Design challenge: where to put mathematical function.

* Where it's placed leads to different ML domains.

\include{../_ml/includes/supervised-learning.md}
\include{../_ml/includes/unsupervised-learning.md}
\include{../_ml/includes/reinforcement-learning.md}
\include{../_ml/includes/deployment.md}

