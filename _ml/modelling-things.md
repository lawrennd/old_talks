---
title: Modeling Things
layout: talk
abstract: >
  Machine learning solutions, in particular those based on deep
  learning methods, form an underpinning of the current revolution in
  “artificial intelligence” that has dominated popular press headlines
  and is having a significant influence on the wider tech agenda.
  
  In some ways the these deep learning methods are radically new: they
  raise questions about how we think of model
  regularization. Regularization arises implicitly through the
  optimization. Yet in others they remain rigidly traditional, and
  unsuited for an emerging world of unstructured, streaming data.
  
  In this paper we relate these new methods to traditional approaches
  and speculate on new directions that might take us beyond modeling
  structured data.
  
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
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

\notes{Machine learning and Statistics are academic cousins, founded
on the same mathematical princples, but often with different
objectives in mind. But the differences can be as informative as the
overlaps.}

\notes{@Efron:prediction20 rightly alludes to the
fundamental differences to the new wave of predictive models that have
arisen in the last decades of machine learning. And these cultures
were also beautifully described by @Breiman:cultures00. }

\notes{In the discussion of Professor Efron's paper @Friedman:discussion20 highlight the continuum between the classical approaches and the emphasis on prediction. Indeed, the prediction culture does not sit entirely in the
machine learning domain, an excellent example of a prediction-focused approach would be Leo Breiman's bagging of models [@Breiman:bagging96], although it's notable that Breiman, a statistician, chose to publish this paper in a machine
learning journal.}

\notes{From a personal perspective, a strand of work that is highly inspirational in prediction also comes from a statistician. The prequential formalism [@Dawid:callibrated82;@Dawid:prequential84] also emerges from statistics. It provides some hope that a predictive approach can be reconciled with attribution in the manner highlighted also by @Friedman:discussion20. The prequential approach is predictive but allows us to falsify
poorly calibrated models [@Lawrence:licsbintro10]. So while it doesn't give us truth, it does give as falsehood in line with Popper's vision of the philosophy of science [@Popper:conjectures63].}

\include{_ml/includes/ml-and-statistics-interface.md}

\include{_data-science/includes/happenstance-data.md}

\section{Generalization}

\notes{Machine Learning practicioners focus on out-of-sample predictive capability as their main objective. This is the ability of a model to generalize its learnings.}

\notes{Professor Efron's paper does an excellent job a summarizing the
range of predictive models that now lie at our disposal, but of
particular interest are deep neural networks. This is because they go
beyond the traditional notions of what generalization is or rather,
what it has been, to practitioners on both the statistical and machine
learning sides of the data sciences.}

\include{_ml/includes/deep-models-and-generalization.md}

\notes{An excellent characterization of generalization is normally
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
terabytes of text). Estimates suggest that the model costs around
$4.5 million dollars to train (see e.g. @Li:openai20).}

\include{_ml/includes/empirical-effectiveness-of-deep-learning.md}

\include{_ml/includes/new-methods-required.md}

<!--include{_ml/includes/massively-missing-data.md}-->

\notes{Machine learning involves taking data and combining it with a model in
order to make a prediction. The data consist of measurements recorded
about the world around us. A model consists of our assumptions about how
the data is likely to interrelate, typical assumptions include
smoothness. Our assumptions reflect some underlying belief about the
regularities of the universe that we expect to hold across a range of
data sets.}
$$
\text{data} + \text{model} \stackrel{\text{algorithm}}{\rightarrow}  \text{prediction}
$$
\notes{The data and the model are combined in computation through an
algorithm.  The etymology of the data indicates that it is given (data
comes from Latin *dare*). In some cases, for example an approach known
as active learning, we have a choice as to how the data is gotten. But
our main control is over the model and the algorithm.

\notes{This is true for both statisticians and machine learning scientists. Although there is a difference in the core motivating philosophy. The mathematical statisticians were motivated by a desire to remove subjectivity from the analysis, reducing the problem to rigorous statistical proof. The statistician is nervous of the inductive biases humans exhibit when drawing conclusions from data. Machine learning scientists, on the other hand, sit closer to the artificial intelligence community. Traditionally, they are inspired by human inductive biases to develop algorithms that allow computers to emulate human performance on tasks. In the past I've summarized the situation as}

> Statisticians want to turn humans into computers, machine learners want to turn computers into humans. Neither is possible so we meet somewhere in the middle.


\include{_ml/includes/model-vs-algorithm.md}

\include{_ml/includes/is-my-model-useful.md}

\include{_ml/includes/big-data-health-motivation.md}

\include{_ml/includes/not-useful-model.md}

\include{_ml/includes/big-data-consistency.md}

\include{_ml/includes/parameter-bottleneck.md}

\include{_ml/includes/non-parametric-challenge.md}

\include{_ml/includes/multivariate-gaussian-closure.md}

\include{_ml/includes/making-parameters-non-parametric.md}
\include{_ml/includes/instantiating-the-model.md}

\include{_ml/includes/making-parameters-non-parametric-illustration.md}


\section{Conclusion}

\notes{Modern machine learning methods for prediction are based on highly overparameterized models that have empirically performed well in tasks that were previously considered challenging or impossible such as machine translation, object detection in images, natural language generation. These models raise new questions for our thinking about how models generalize their predictions. In particular, the conflate the conceptual separation between model and algorithm and our best understanding is that they regularize themselves implicitly through their optimization algorithms.

Despite the range of questions these models raise for our classical view of generalization, in another sense, these models are very traditional. They operate on tables of data that have been curated through appropriate curation. These deep learning models operate on (very large) design matrices.

We've argued that the new frontiers for the data sciences lie in the domain of what we term "happenstance data". The data that hasn't been explicitly collected with a purpose in mind, but is laid down through the rhythms of our modern lives. We've claimed that the traditional view of data as sitting in a table is restrictive for this new domain, and outlined how we might model such data through nonparametrics. We illustrated these ideas with a very trivial example using Gaussian process regression.}

\subsection{Acknowledgments}

I've benefited over the years from conversations with a number of colleagues, among those I can identify that influenced the thinking in this paper are Tony O'Hagan, John Kent, David J. C. MacKay, Richard Wilkinson, Darren Wilkinson, Bernhard Schölkopf, Zoubin Ghahramani. Naturally, the responsibility for the sensible bits is theirs, the errors are all mine. 



\references
