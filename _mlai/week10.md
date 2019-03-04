---
layout: lectures
title: "Logistic Regression and GLMs"
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
venue: University of Sheffield
date: 2015-12-01
abstract: Naive Bayes assumptions allow us to specify class conditional densities through assuming that the data are conditionally independent given parameters. A logistic regression is an approach to classification which extends the linear basis function models we've already explored. Rather than modeling the output of the function directly the assumption is that we model the *log-odds* with the basis functions.
transition: None
---

\include{talk-macros.tex}

\subsection{Review}

\slides{
* Last week: Specified Class Conditional Distributions, $p(\inputVector_i|\dataScalar_i, \parameterVector)$.
* Used Bayes Classifier + naive Bayes model to specify joint distribution.
* Used Bayes rule to compute posterior probability of class membership.
* This week: 
  * direct estimation of probability of class membership.
  * introduction of generalised linear models.
}


\notes{The [naive Bayes assumption](./week9.ipynb) allowed us to
specify a class conditional density, $p(\inputVector_i|\dataScalar_i,
\parameterVector)$, through assuming that the features were
conditionally independent given the label.  Combined with our
assumption that the data points are conditionally independent given
the parameters, $\parameterVector$, this allowed us to specify a joint
density over the entire data set, $p(\dataVector, \inputMatrix)$. We
argued that modeling the joint density is a powerful approach because
we can answer any particular question we have about the data through
the sum rule and the product rule of probability. We can condition on
the training data and query the value of an unseen test point. If we
have missing data, then we can integrate over the missing point
(marginalise) and obtain our best prediction despite the absence of
some of the features for a point. However, it comes at the cost of a
particular modeling assumption. Namely, to make modeling practical we
assumed that the features were conditionally independent given the
feature label. In other words, for any given point, if we know its
class, then its features will be independent. This is a very strong
assumption. For example, if we were classifying the sex of an
individual given their height and weight, naive Bayes would assume
that if we knew their sex, then the height and weight would be
independent. This is clearly wrong, the dependence between height and
weight is not dictated only by the sex of an individual, there is a
natural correlation between them.}

\notes{Modeling the entire joint density allows us to deal with
different questions, that we may not have envisaged at the model
*design time*.  It contrasts with the approach we took for regression
where we specifically chose to model the conditional density for the
target values, $\dataVector$, given the input locations,
$\inputMatrix$. That density, $p(\dataVector|\inputMatrix)$,
effectively assumes that the question we'll be asked at *run time* is
known. In particular, we expect to be asked about the value of the
function, $y^*$, given a particular input location,
$\inputVector^*$. We don't expect to be asked about the value of an
input given a particular observation.  That would require placing an
additional prior over the input location for each point,
$p(\inputVector_i)$. Of course, it's possible to conceive of a model
like this, and indeed that is how we proceeded for
[dimensionality reduction](./week8.ipynb). However, if we know we will
always have all the inputs at run time, it may make sense to
*directly* model the conditional density,
$p(\dataVector|\inputMatrix)$.}

\include{_ml/includes/logistic-regression.md}

\newslide{Ad Matching for Facebook}

\slides{
* This approach used in many internet companies.
* Example: ad matching for Facebook.
  * Millions of advertisers
  * Billions of users
  * How do you choose who to show what?
* Logistic regression used in combination with [decision trees]()
* [Paper available here](http://www.herbrich.me/papers/adclicksfacebook.pdf)
}

\notes{
\subsection{Movie Body Count Data}

Let's recreate the movie body count example we used with naive
Bayes. We can load in the data from `pods` as follows.

\setupcode{import pods}
\code{# Change this example for 2016#data = pods.datasets.movie_body_count_r_classify()
data = pods.datasets.olivetti_glasses()
X = data['X']
y = data['Y']}

\subsection{Gradient Descent}

We will need to define some initial random values for our vector and then minimize the objective by descending the gradient.

\setupcode{import numpy as np}
\code{# gradient descent algorithm
w = np.random.normal(size=(X.shape[1]+1, 1), scale = 0.001)
eta = 1e-9
iters = 10000
for i in range(iters):
    g, Phi = predict(w, X, linear)
    w -= eta*gradient(g, Phi, y) + 0.001*w
    if not i % 100:
        print("Iter", i, "Objective", objective(g, y))}

Let's look at the weights and how they relate to the inputs.

\setupcode{import matplotlib.pyplot as plt}
\code{plt.matshow(X[40, :].reshape(64, 64).T)}

The weights are fairly small. This makes sense for year, and perhaps also body count, but given the genre only take the value of 0 or 1 it makes less sense for them. Why are the weights so small? What can you do to fix this?

\subsection{Stochastic Gradient Descent}

Now construct a stochastic gradient descent algorithm and run it on the data. Is it faster or slower than batch gradient descent? What can you do to improve convergence speed?

\subsection{Going Further: Optimization}

Other optimization techniques for generalized linear models include [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method), it requires you to compute the Hessian, or second derivative of the objective function.

Methods that are based on gradients only include [L-BFGS](http://en.wikipedia.org/wiki/Limited-memory_BFGS) and [conjugate gradients](http://en.wikipedia.org/wiki/Conjugate_gradient_method). Can you find these in python? Are they suitable for very large data sets?
}

\notes{
\subsection{Other GLMs}

We've introduced the formalism for generalized linear models. Have a think about how you might model count data using the [Poisson distribution](http://en.wikipedia.org/wiki/Poisson_distribution) and a log link function for the rate, $\lambda(\inputVector)$. If you want a data set you can try the `pods.datasets.google_trends()` for some count data.
}

\newslide{Other GLMs}

\slides{
* Logistic regression is part of a family known as *generalized linear models*
* They all take the form 
  $$g^{-1}(\mappingFunction_i(x)) = \mappingVector^\top \basisVector(\inputVector_i)$$
* As another example let's look at *Poisson regression*.}

\include{_ml/includes/poisson-regression.md}

\subsection{Bayesian Approaches}

\exercise{Can you place a prior density over the parameters $\mappingVector$ and marginalize them out like we did for linear regression? If not why not?}


\newslide{Reading}

* Section 5.2.2 of @Rogers:book11 up to pg 182.

\thanks

\references

