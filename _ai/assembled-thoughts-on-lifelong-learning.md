title: "Assembled Thoughts on Lifelong Learning and Robotics"
abstract: >
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-09-04
venue: Naples or Zoom
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

https://sites.google.com/view/ll4lhri2020

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

\section{Conclusions}

\thanks

\references
