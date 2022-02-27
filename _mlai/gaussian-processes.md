---
week: 11
title: "Special Topics: Gaussian Processes"
abstract: 
youtube: B2XhFoCehy8
---

talk-macros.gpp}lk-macros.tex}

talk-macros.gpp}lai/includes/mlai-notebook-setup.md}

\subsection{Review}

* Last week: Logistic Regression and Generalised Linear Models
* Introduced link functions and different transformations.
* Showed examples in classification and mentioned possibilities for disease rate models.
* This week: 
    * Gaussian Processes: non parametric Bayesian modelling
}

\notes{Over the last two sessions we've begun considering classification models and logistic regresssion. In particular, for naive Bayes, we considered a set of assumptions that allowed us to build a joint model of our data set. In particular for naive Bayes we specified

1. Data conditional independence.
2. Feature conditional independence.
3. Marginal likelihood of labels was Bernoulli distributed.

This allowed us to specify the joint density of our labels and our input data, $p(\dataVector, \inputMatrix|\boldsymbol{\theta})$. And we conditioned on the training data to make predictions about the test data.}

\subsection{Generalized Linear Models}

Logistic regression is part of a wider class of models known as *generalized linear models*. In these models we determine that some characteristic of the model is speicified by a function that is liniear in the parameters. So we might suggest that
$$
\log \frac{p(\inputVector)}{1-p(\inputVector)} = \mappingFunction(\inputVector; \mappingVector)
$$
where $\mappingFunction(\inputVector; \mappingVector)$ is a linear-in-the-parameters function (here the
parameters are $\mappingVector$, which is generally non-linear in the inputs. So far
we have considered basis function models of the form
$$
\mappingFunction(\inputVector) =
\mappingVector^\top \basisVector(\inputVector).
$$
\notes{When we form a Gaussian process we do something that is slightly more akin to the naive Bayes approach, but actually is closely related to the generalized linear model approach.}

talk-macros.gpp}p/includes/gp-intro-lectures.md}
talk-macros.gpp}p/includes/gptwopointpred.md}
talk-macros.gpp}p/includes/gp-from-basis-functions.md}

talk-macros.gpp}p/includes/non-degenerate-gps.md}
talk-macros.gpp}p/includes/gp-function-space.md}
talk-macros.gpp}p/includes/gp-covariance-function-importance.md}
talk-macros.gpp}p/includes/gp-numerics-and-optimization.md}

talk-macros.gpp}p/includes/gp-optimize.md}

talk-macros.gpp}ern/includes/eq-covariance.md}

talk-macros.gpp}p/includes/olympic-marathon-gp.md}

talk-macros.gpp}p/includes/della-gatta-gene-gp.md}
talk-macros.gpp}ealth/includes/malaria-gp.md}

talk-macros.gpp}ern/includes/add-covariance.md}
talk-macros.gpp}p/includes/bda-forecasting.md}

talk-macros.gpp}ern/includes/basis-covariance.md}
talk-macros.gpp}ern/includes/brownian-covariance.md}
talk-macros.gpp}ern/includes/mlp-covariance.md}

talk-macros.gpp}p/includes/gp-summer-school.md}
talk-macros.gpp}p/includes/gpy-software.md}

\thanks

\references


