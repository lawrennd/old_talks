---
title: Modelling Things
layout: talk
abstract: >
  Machine learning solutions, in particular those based on deep
  learning methods, form an underpinning of the current revolution in
  “artificial intelligence” that has dominated popular press headlines
  and is having a significant influence on the wider tech agenda.
  
  In this talk I will give an overview of where we are now with
  machine learning solutions, and what challenges we face both in the
  near and far future. These include practical application of existing
  algorithms in the face of the need to explain decision making,
  mechanisms for improving the quality and availability of data,
  dealing with large unstructured datasets.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
venue: IEEE RO-MAN Conference Workshop
geometry: ['a4paper', 'margin=1in']
date: 2020-09-04
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
date: 2020-08-23
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

\include{_data-science/includes/pods-install.md}
\include{_gp/includes/gpy-install.md}


\include{_ml/includes/ml-and-statistics-interface.md}
\include{_data-science/includes/happenstance-data.md}

\notes{Professor Efron's paper does an excellent job a summarising the
range of predictive models that now lie at our disposal, but of
particular interest are deep neural networks. This is because they go
beyond the traditional notions of what generalisation is or rather,
what it has been, to practitioners on both the statistical and machine
learning sides of the fence.}

\include{_ml/includes/deep-models-and-generalization.md}

\notes{An excellent characterisation of generalization is normally
given by the bias-variance dilemma. The bias-variance decomposition
for regression models separates the generalization error into two
components [@Geman:biasvariance92].}

\include{_ml/includes/bias-variance-dilemma.md}

\include{_ml/includes/double-descent.md}

\notes{As Professor Efron points out, modern machine learning models
are often fitted using many millions of data points. The most extreme
example of late is known as GPT-3. This neural network model, known as
a Transformer, has in its largest form 175 billion parameters. The
model was trained on a data set containing 499 billion tokens (about 2
Terrabytes of text). Estimates suggest that the model costs around
$4.5 million dollars to train (see e.g. @Li:openai20).}

\include{_ml/includes/empirical-effectiveness-of-deep-learning.md}

\include{_ml/includes/new-methods-required.md}

\include{_ml/includes/massively-missing-data.md}

\notes{Machine learning involves taking data and combining it with a model in
order to make a prediction. The data consist of measurements recorded
about the world around us. A model consists of our assumptions about how
the data is likely to interrelate, typical assumptions include
smoothness. Our assumptions reflect some undelying belief about the
regularities of the universe that we expect to hold across a range of
data sets.}
$$
\text{data} + \text{model} \rightarrow \text{prediction}
$$
\notes{From my perspective, the model is where all the innovation in machine
learning goes. The etymology of the data indicates that it is given
(although in some cases, such as active learning, we have a choice as to
how it is gotten), our main control is over the model. This is the key
to making good predictions. The model is a mathematical abstraction of
the regularities of the universe that we believe underly the data as
collected. If the model is chosen well we will be able to interpolate
the data and precit likely values of future data points. If it is chosen
badly our predictions will be overconfident and wrong.}

\include{_ml/includes/model-vs-algorithm.md}

\include{_ml/includes/is-my-model-useful.md}

\include{_ml/includes/big-data-health-motivation.md}

\include{_ml/includes/not-useful-model.md}

\include{_ml/includes/big-data-consistency.md}

\include{_ml/includes/parameter-bottleneck.md}

\include{_ml/includes/non-parametric-challenge.md}

\include{_ml/includes/multivariate-gaussian-closure.md}

\include{_ml/includes/making-parameters-non-parametric.md}

\include{_ml/includes/making-parameters-non-parametric-illustration.md}



\subsubsection{Uncertainty about the Provenance of the Data}

\notes{Provenance could include the time that the data was acquired, the
location that the data was acquired, even the 'type' of data that is
acquired. For example, in computer vision pixels are arriving from
different objects. We are uncertain about the provenance of the pixels
in terms of which *object* they are arriving from. The spatial location
of the object in the image. This uncertainty relates to uncertainty
about the covariance function. Unfortunately, it is not directly on the
covariance function itself, but relates to values through which the
covariance is nonlinearly related.}
\begin{align*} 
k(\dataVector, \dataVector^\prime) = \exp(-||\dataVector-\dataVector^\prime||^2) 
\end{align*}
\notes{These variables become *latent* or *confounders*.}

\notes{**Not sure about this**: Provenance of data is often finite. Consider a
diseased person. That person consists of a finite (if very large) state
vector. Of course the number of measurements we can make about that
person is infinite. But there are a set of fundamental limitations to
what can go wrong with the individual.}


\subsection{Ethics}


\notes{Ownership of data, returning it to the individual. In healthcare the
danger of confusing it with marketing, Laplace, and the utopian view of
data. Invalidity of insurance. How the results are presented to the
patient.}


\thanks

\references
