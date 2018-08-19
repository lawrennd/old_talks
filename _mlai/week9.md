---
layout: lectures
title: "Probabilistic Classification: Naive Bayes"
author: Neil D. Lawrence
date: 2015/11/24
transition: None
---

\include{talk-macros.tex}

\newslide{Review}

* Last time: Looked at unsupervised learning.
* Introduced latent variables, dimensionality reduction and clustering.
* This time: Classification with Naive Bayes

\include{_ml/includes/classification-intro.md}
\include{_ml/includes/classification-examples.md}
\include{_ml/includes/bayesian-reminder.md}

\notes{Machine learning problems normally involve a prediction function and an objective function. So far in the course we've mainly focussed on the case where the prediction function was over the real numbers, so the codomain of the functions, $\mappingFunction(\inputMatrix)$ was the real numbers or sometimes real vectors. The classification problem consists of predicting whether or not a particular example is a member of a particular class. So we may want to know if a particular image represents a digit 6 or if a particular user will click on a given advert. These are classification problems, and they require us to map to *yes* or *no* answers. That makes them naturally discrete mappings.}

\notes{In classification we are given an input vector, $\inputVector$, and an associated label, $\dataScalar$ which either takes the value $0$ or $1$.}

\newslide{Discrete Probability}

\slides{* Algorithms based on *prediction* function and *objective* function.
* For regression the *codomain* of the functions, $f(\inputMatrix)$ was the real numbers or sometimes real vectors. 
* In classification we are given an input vector, $\inputVector$, and an associated label, $\dataScalar$ which either takes the value $0$ or $1$.}

\include{_ml/includes/bernoulli-distribution.md}
\include{_ml/includes/bernoulli-maximum-likelihood.md}
\include{_ml/includes/bayes-rule-reminder.md}
\include{_ml/includes/naive-bayes.md}

### Reading

* Chapter 5 of @Rogers:book11 up to pg 179 (Section 5.1, and 5.2 up to 5.2.2).





