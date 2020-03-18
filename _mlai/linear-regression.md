---
layout: lecture
title: Linear Algebra and Linear Regression
abstract: |
  In this session we combine the objective function perspective and the probabilistic perspective on *linear regression*. We motivate the importance of *linear algebra* by showing how much faster we can complete a linear regression using linear algebra.
date: 2015-10-13
week: 3
ipynb: True
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
venue: University of Sheffield
postdir: ../../../mlatcl/mlai/_lectures/
slidedir: ../../../mlatcl/mlai/slides/
notedir: ../../../mlatcl/mlai/_notes/
notebookdir: ../../../mlatcl/mlai/_notebooks/
youtube: 5VPr6NbHHjg
transition: None
---

\include{talk-macros.tex}

\subsection{Review}

* Last time: Looked at objective functions for movie recommendation.
* Minimized sum of squares objective by steepest descent and stochastic gradients.
* This time: explore least squares for regression.

\include{_ml/includes/regression-examples.md}

\subsection{Olympic 100m Data}

*  Gold medal times for Olympic 100 m runners since 1896.
\includeimg{../slides/diagrams/ml/100m_final_start.jpg}
\aligncenter{*Image from Wikimedia Commons*}<http://bit.ly/191adDC>

\subsection{Olympic 100m Data}

\setupplotcode{import pods
from matplotlib import pyplot as plt
%matplotlib inline}

\plotcode{data = pods.datasets.olympic_100m_men()
f, ax = plt.subplots(figsize=(7,7))
ax.plot(data['X'], data['Y'], 'ro', markersize=10)}

\include{_ml/includes/olympic-marathon-data.md}
\include{_ml/includes/what-is-ml.md}

\section{Sum of Squares Error}

\notes{Last week we considered a cost function for minimization of the error. We considered items (films) and users and assumed that each movie rating, $\dataScalar_{i,j}$ could be summarised by an inner product between a vector associated with the item, $\mathbf{v}_j$ and one associated with the user $\mathbf{u}_i$. We justified the inner product as a measure of similarity in the space of 'movie subjects', where both the users and the items lived, giving the analogy of a library.}

\notes{To make predictions we encouraged the similarity to be high if the movie rating was high using the quadratic error function,
$$
E_{i,j}(\mathbf{u}_i, \mathbf{v}_j) = \left(\mathbf{u}_i^\top \mathbf{v}_j -
\dataScalar_{i,j}\right)^2,
$$
which we then summed across all the observations to form the total error
$$
\errorFunction(\mathbf{U}, \mathbf{V}) =
\sum_{i,j}s_{i,j}\left(\mathbf{u}_i^\top \mathbf{v}_j - \dataScalar_{i,j}\right)^2,
$$
where $s_{i,j}$ is an indicator variable which is set to 1 if the rating of movie $j$ by user $i$ is provided in our data set. This is known as a sum of squares error.}

\notes{This week we will reinterpret the error as a *probabilistic model*. We will consider the difference between our data and our model to have come from unconsidered factors which exhibit as a probability density. This leads to a more principled definition of least squares error that is originally due to [Carl Friederich Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss), but is mainly inspired by the thinking of [Pierre-Simon Laplace](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace).}

\include{_ml/includes/linear-algebra-regression.md}

\thanks

\references
