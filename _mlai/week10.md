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

\newslide{Review}

\slides{
* Last week: Specified Class Conditional Distributions, $p(\inputVector_i|\dataScalar_i, \parameterVector)$.
* Used Bayes Classifier + naive Bayes model to specify joint distribution.
* Used Bayes rule to compute posterior probability of class membership.
* This week: 
  * direct estimation of probability of class membership.
  * introduction of generalised linear models.
}


\notes{
The [naive Bayes assumption](./week9.ipynb) allowed us to specify a class conditional density, $p(\inputVector_i|\dataScalar_i, \parameterVector)$, through assuming that the features were conditionally independent given the label.  Combined with our assumption that the data points are conditionally independent given the parameters, $\parameterVector$, this allowed us to specify a joint density over the entire data set, $p(\dataVector, \inputMatrix)$. We argued that modeling the joint density is a powerful approach because we can answer any particular question we have about the data through the sum rule and the product rule of probability. We can condition on the training data and query the value of an unseen test point. If we have missing data, then we can integrate over the missing point (marginalise) and obtain our best prediction despite the absence of some of the features for a point. However, it comes at the cost of a particular modeling assumption. Namely, to make modeling practical we assumed that the features were conditionally independent given the feature label. In other words, for any given point, if we know its class, then its features will be independent. This is a very strong assumption. For example, if we were classifying the sex of an individual given their height and weight, naive Bayes would assume that if we knew their sex, then the height and weight would be independent. This is clearly wrong, the dependence between height and weight is not dictated only by the sex of an individual, there is a natural correlation between them.
}

\notes{
Modeling the entire joint density allows us to deal with different questions, that we may not have envisaged at the model *design time*.  It contrasts with the approach we took for regression where we specifically chose to model the conditional density for the target values, $\dataVector$, given the input locations, $\inputMatrix$. That density, $p(\dataVector|\inputMatrix)$, effectively assumes that the question we'll be asked at *run time* is known. In particular, we expect to be asked about the value of the function, $y^*$, given a particular input location, $\inputVector^*$. We don't expect to be asked about the value of an input given a particular observation.  That would require placing an additional prior over the input location for each point, $p(\inputVector_i)$. Of course, it's possible to conceive of a model like this, and indeed that is how we proceeded for [dimensionality reduction](./week8.ipynb). However, if we know we will always have all the inputs at run time, it may make sense to *directly* model the conditional density, $p(\dataVector|\inputMatrix)$.
}

\notes{
### Logistic Regression

A logistic regression is an approach to classification which extends the linear basis function models we've already explored. Rather than modeling the output of the function directly the assumption is that we model the *log-odds* with the basis functions.
}

\newslide{Logistic Regression and GLMs}

\slides{
* Modelling entire density allows any question to be answered (also missing data).
* Comes at the possible expense of *strong* assumptions about data generation distribution.
* In regression we model probability of $\dataScalar_i |\inputVector_i$ directly.
  * **Allows less flexibility in the question, but more flexibility in the model assumptions.**
* Can do this not just for regression, but classification.
* Framework is known as *generalized linear models*.
}
\notes{
The [odds](http://en.wikipedia.org/wiki/Odds) are defined as the ratio of the probability of a positive outcome, to the probability of a negative outcome. If the probability of a positive outcome is denoted by $\pi$, then the odds are computed as $\frac{\pi}{1-\pi}$. Odds are widely used by [bookmakers](http://en.wikipedia.org/wiki/Bookmaker) in gambling, although a bookmakers odds won't normalise: i.e. if you look at the equivalent probabilities, and sum over the probability of all outcomes the bookmakers are considering, then you won't get one. This is how the bookmaker makes a profit.  Because a probability is always between zero and one, the odds are always between $0$ and $\infty$. If the positive outcome is unlikely the odds are close to zero, if it is very likely then the odds become close to infinite. Taking the logarithm of the odds maps the odds from the positive half space to being across the entire real line. Odds that were between 0 and 1 (where the negative outcome was more likely) are mapped to the range between $-\infty$ and $0$. Odds that are greater than 1 are mapped to the range between $0$ and $\infty$. Considering the log odds therefore takes a number between 0 and 1 (the probability of positive outcome) and maps it to the entire real line. The function that does this is known as the [logit function](http://en.wikipedia.org/wiki/Logit), $g^{-1}(p_i) = \log\frac{p_i}{1-p_i}$. This function is known as a *link function*.
}

\newslide{Log Odds}

\slides{
* model the *log-odds* with the basis functions.
* [odds](http://en.wikipedia.org/wiki/Odds) are defined as the ratio of the
probability of a positive outcome, to the probability of a negative outcome. 
* Probability is between zero and one, odds are:
  $$ \frac{\pi}{1-\pi} $$
* Odds are between $0$ and $\infty$. 
* Logarithm of odds maps them to $-\infty$ to $\infty$.
}

\notes{
For a standard regression we take,
$$
\mappingFunction(\inputVector) = \mappingVector^\top
\basisVector(\inputVector),
$$
if we want to perform classification we perform a logistic regression.
$$
\log \frac{\pi}{(1-\pi)} = \mappingVector^\top
\basisVector(\inputVector)
$$
where the odds ratio between the positive class and the negative class is given by
$$
\frac{\pi}{(1-\pi)}
$$
The odds can never be negative, but can take any value from 0 to $\infty$. We have defined the link function as taking the form $g^{-1}(\cdot)$ implying that the inverse link function is given by $g(\cdot)$. Since we have defined,
$$
g^{-1}(\pi) =
\mappingVector^\top \basisVector(\inputVector)
$$
we can write $\pi$ in terms of
the *inverse link* function, $g(\cdot)$ as 
$$
\pi = g(\mappingVector^\top
\basisVector(\inputVector)).
$$
}

\newslide{Logit Link Function}

\slides{
* The [Logit function](http://en.wikipedia.org/wiki/Logit), $$g^{-1}(\pi_i) = \log\frac{\pi_i}{1-\pi_i}.$$ This function is known as a *link function*.
* For a standard regression we take,
  $$f(\inputVector_i) = \mappingVector^\top \basisVector(\inputVector_i),$$
* For classification we perform a logistic regression. 
  $$\log \frac{\pi_i}{1-\pi_i} = \mappingVector^\top \basisVector(\inputVector_i)$$
}

\newslide{Inverse Link Function}

\slides{
We have defined the link function as taking the form $g^{-1}(\cdot)$ implying that the inverse link function is given by $g(\cdot)$. Since we have defined,
$$
g^{-1}(\pi(\inputVector)) = \mappingVector^\top
\basisVector(\inputVector)
$$
we can write $\pi$ in terms of the *inverse link* function, $g(\cdot)$ as 
$$
\pi(\inputVector) = g(\mappingVector^\top
\basisVector(\inputVector)).
$$
}

\setupplotcode{import teaching_plots as plot}

\plotcode{plot.logistic('../slides/diagrams/ml/logistic.svg')}

\newslide{Logistic function}

\slides{
* [Logistic](http://en.wikipedia.org/wiki/Logistic_function) (or sigmoid) squashes
real line to between 0  & 1. Sometimes also called a 'squashing function'.

\includesvg{../slides/diagrams/ml/logistic.svg}
}

\notes{
### Basis Function

We'll define our prediction, objective and gradient functions below. But before we start, we need to define a basis function for our model. Let's start with the linear basis.

\setupcode{import numpy as np}
\loadcode{linear}{mlai}

### Prediction Function

Now we have the basis function let's define the prediction function.

\setupcode{import numpy as np}
\code{def predict(w, x, basis=linear, **kwargs):
    "Generates the prediction function and the basis matrix."
    Phi = basis(x, **kwargs)
    f = np.dot(Phi, w)
    return 1./(1+np.exp(-f)), Phi}

This inverse of the link function is known as the [logistic](http://en.wikipedia.org/wiki/Logistic_function) (thus the name logistic regression) or sometimes it is called the sigmoid function. For a particular value of the input to the link function, $\mappingFunction_i = \mappingVector^\top \basisVector(\inputVector_i)$ we can plot the value of the link function as below.


\setupplotcode{import teaching_plots as plot}

\plotcode{plot.logistic('../slides/diagrams/ml/logistic.svg')}

\includesvg{../slides/diagrams/ml/logistic.svg}


The function has this characeristic 's'-shape (from where the term sigmoid, as in sigma, comes from). It also takes the input from the entire real line and 'squashes' it into an output that is between zero and one. For this reason it is sometimes also called a 'squashing function'.

By replacing the inverse link with the sigmoid we can write $\pi$ as a function of the input and the parameter vector as,
$$
\pi(\inputVector,\mappingVector) = \frac{1}{1+
\exp\left(-\mappingVector^\top \basisVector(\inputVector)\right)}.
$$

The process for logistic regression is as follows. Compute the output of a standard linear basis function composition ($\mappingVector^\top \basisVector(\inputVector)$, as we did for linear regression) and then apply the inverse link function, $g(\mappingVector^\top \basisVector(\inputVector))$.  In logistic regression this involves *squashing* it with the logistic (or sigmoid) function. Use this value, which now has an interpretation as a *probability* in a Bernoulli distribution to form the likelihood. Then we can assume conditional independence of each data point given the parameters and develop a likelihod for the entire data set.

As we discussed last time, the Bernoulli likelihood is of the form,
$$
P(\dataScalar_i|\mappingVector, \inputVector) =
\pi_i^{\dataScalar_i} (1-\pi_i)^{1-\dataScalar_i}
$$
which we can think of as clever trick for mathematically switching between two probabilities if we were to write it as code it would be better described as

```python
def bernoulli(x, y, pi):
    if y == 1:
        return pi(x)
    else:
        return 1-pi(x)
```
but writing it mathematically makes it easier to write our objective function within a single mathematical equation.
}

\newslide{Prediction Function}

\slides{
* Can now write $\pi$ as a function of the input and the parameter vector as, 
  $$\pi(\inputVector,\mappingVector) = \frac{1}{1+
\exp\left(-\mappingVector^\top \basisVector(\inputVector)\right)}.$$
* Compute the output of a standard linear basis function composition ($\mappingVector^\top \basisVector(\inputVector)$, as we did for linear regression)
* Apply the inverse link function, $g(\mappingVector^\top \basisVector(\inputVector))$. 
* Use this value in a Bernoulli distribution to form the likelihood.
}

\newslide{Bernoulli Reminder}

\slides{
* From last time 
  $$P(\dataScalar_i|\mappingVector, \inputVector) = \pi_i^{\dataScalar_i} (1-\pi_i)^{1-\dataScalar_i}$$

* Trick for switching betwen probabilities

```python
def bernoulli(y, pi):
    if y == 1:
        return pi
    else:
return 1-pi
```
}

\notes{
### Maximum Likelihood

To obtain the parameters of the model, we need to maximize the likelihood, or minimize the objective function, normally taken to be the negative log likelihood. With a data conditional independence assumption the likelihood has the form,
$$
P(\dataVector|\mappingVector,
\inputMatrix) = \prod_{i=1}^\numData P(\dataScalar_i|\mappingVector, \inputVector_i). 
$$
which can be written as a log likelihood in the form
$$
\log P(\dataVector|\mappingVector,
\inputMatrix) = \sum_{i=1}^\numData \log P(\dataScalar_i|\mappingVector, \inputVector_i) = \sum_{i=1}^\numData
\dataScalar_i \log \pi_i + \sum_{i=1}^\numData (1-\dataScalar_i)\log (1-\pi_i)
$$
and if we take the probability of positive outcome for the $i$th data point to be given by
$$
\pi_i = g\left(\mappingVector^\top \basisVector(\inputVector_i)\right),
$$
where $g(\cdot)$ is the *inverse* link function, then this leads to an objective function of the form,
$$
E(\mappingVector) = -  \sum_{i=1}^\numData \dataScalar_i \log
g\left(\mappingVector^\top \basisVector(\inputVector_i)\right) -
\sum_{i=1}^\numData(1-\dataScalar_i)\log \left(1-g\left(\mappingVector^\top
\basisVector(\inputVector_i)\right)\right).
$$

\setupcode{import numpy as np}
\code{def objective(g, y):
    "Computes the objective function."
    posind = np.where(y.flatten()==1)
    negind = np.where(y.flatten()==0)
    return -np.log(g[posind, :]).sum() - np.log(1-g[negind, :]).sum()}

As normal, we would like to minimize this objective. This can be done by differentiating with respect to the parameters of our prediction function, $\pi(\inputVector;\mappingVector)$, for optimisation. The gradient of the likelihood with respect to $\pi(\inputVector;\mappingVector)$ is of the form,
$$
\frac{\text{d}E(\mappingVector)}{\text{d}\mappingVector} = -\sum_{i=1}^\numData
\frac{\dataScalar_i}{g\left(\mappingVector^\top
\basisVector(\inputVector)\right)}\frac{\text{d}g(\mappingFunction_i)}{\text{d}\mappingFunction_i}
\basisVector(\inputVector_i) +  \sum_{i=1}^\numData
\frac{1-\dataScalar_i}{1-g\left(\mappingVector^\top
\basisVector(\inputVector)\right)}\frac{\text{d}g(\mappingFunction_i)}{\text{d}\mappingFunction_i}
\basisVector(\inputVector_i)
$$
where we used the chain rule to develop the derivative in terms of $\frac{\text{d}g(\mappingFunction_i)}{\text{d}\mappingFunction_i}$, which is the gradient of the inverse link function (in our case the gradient of the sigmoid function).

So the objective function now depends on the gradient of the inverse link function, as well as the likelihood depends on the gradient of the inverse link function, as well as the gradient of the log likelihood, and naturally the gradient of the argument of the inverse link function with respect to the parameters, which is simply $\basisVector(\inputVector_i)$.
}

\newslide{Maximum Likelihood}

\slides{
* Conditional independence of data:
  $$P(\dataVector|\mappingVector, \inputMatrix) = \prod_{i=1}^\numData P(\dataScalar_i|\mappingVector,
\inputVector_i). $$
}

\newslide{Log Likelihood}

\slides{
$$\begin{align*}
  \log P(\dataVector|\mappingVector, \inputMatrix) = &
  \sum_{i=1}^\numData \log P(\dataScalar_i|\mappingVector, \inputVector_i) \\ = &\sum_{i=1}^\numData \dataScalar_i \log
  \pi_i \\ & + \sum_{i=1}^\numData (1-\dataScalar_i)\log (1-\pi_i)
\end{align*}$$
}

\newslide{Objective Function}

\slides{
* Probability of positive outcome for the $i$th data point 
  $$\pi_i = g\left(\mappingVector^\top \basisVector(\inputVector_i)\right),$$
  where $g(\cdot)$ is the *inverse* link function
* Objective function of the form 
  $$\begin{align*}
    E(\mappingVector) = & -  \sum_{i=1}^\numData \dataScalar_i \log
    g\left(\mappingVector^\top \basisVector(\inputVector_i)\right) \\& -
    \sum_{i=1}^\numData(1-\dataScalar_i)\log \left(1-g\left(\mappingVector^\top
    \basisVector(\inputVector_i)\right)\right).
   \end{align*}$$
}

\newslide{Minimize Objective}

\slides{
* Grdient wrt  $\pi(\inputVector;\mappingVector)$
  $$\begin{align*}
  \frac{\text{d}E(\mappingVector)}{\text{d}\mappingVector} = &
  -\sum_{i=1}^\numData \frac{\dataScalar_i}{g\left(\mappingVector^\top
  \basisVector(\inputVector)\right)}\frac{\text{d}g(\mappingFunction_i)}{\text{d}\mappingFunction_i}
  \basisVector(\inputVector_i) \\ & +  \sum_{i=1}^\numData
  \frac{1-\dataScalar_i}{1-g\left(\mappingVector^\top
  \basisVector(\inputVector)\right)}\frac{\text{d}g(\mappingFunction_i)}{\text{d}\mappingFunction_i}
  \basisVector(\inputVector_i)
  \end{align*}$$
}

\notes{
The only missing term is the gradient of the inverse link function. For the sigmoid squashing function we have,
$$\begin{align*}
g(\mappingFunction_i) &= \frac{1}{1+\exp(-\mappingFunction_i)}\\
&=(1+\exp(-\mappingFunction_i))^{-1}
\end{align*}$$
and the gradient can be computed as
$$\begin{align*}
\frac{\text{d}g(\mappingFunction_i)}{\text{d} \mappingFunction_i} & =
\exp(-\mappingFunction_i)(1+\exp(-\mappingFunction_i))^{-2}\\
& = \frac{1}{1+\exp(-\mappingFunction_i)}
\frac{\exp(-\mappingFunction_i)}{1+\exp(-\mappingFunction_i)} \\
& = g(\mappingFunction_i) (1-g(\mappingFunction_i))
\end{align*}$$
so the full gradient can be written down as
$$
\frac{\text{d}E(\mappingVector)}{\text{d}\mappingVector} = -\sum_{i=1}^\numData
\dataScalar_i\left(1-g\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i) +  \sum_{i=1}^\numData
(1-\dataScalar_i)\left(g\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i).
$$

\setupcode{import numpy as np}
\code{def gradient(g, Phi, y):
    "Generates the gradient of the parameter vector."
    posind = np.where(y.flatten()==1)
    dw = -(Phi[posind]*(1-g[posind])).sum(0)
    negind = np.where(y.flatten()==0 )
    dw += (Phi[negind]*g[negind]).sum(0)
    return dw[:, None]}

### Optimization of the Function

Reorganizing the gradient to find a stationary point of the function with respect to the parameters $\mappingVector$ turns out to be impossible. Optimization has to proceed by *numerical methods*. Options include the multidimensional variant of [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) or [gradient based optimization methods](http://en.wikipedia.org/wiki/Gradient_method) like we used for optimizing matrix factorization for the movie recommender system. We recall from matrix factorization that, for large data, *stochastic gradient descent* or the Robbins Munro [@Robbins:stoch51] optimization procedure worked best for function minimization.
}

\newslide{Link Function Gradient}

\slides{
* Also need gradient of inverse link function wrt parameters.
$$\begin{align*}
g(\mappingFunction_i) &= \frac{1}{1+\exp(-\mappingFunction_i)}\\
&=(1+\exp(-\mappingFunction_i))^{-1}
\end{align*}$$
and the gradient can be computed as
$$\begin{align*}
\frac{\text{d}g(\mappingFunction_i)}{\text{d} \mappingFunction_i} & =
\exp(-\mappingFunction_i)(1+\exp(-\mappingFunction_i))^{-2}\\
& = \frac{1}{1+\exp(-\mappingFunction_i)}
\frac{\exp(-\mappingFunction_i)}{1+\exp(-\mappingFunction_i)} \\
& = g(\mappingFunction_i) (1-g(\mappingFunction_i))
\end{align*}$$
}

\newslide{Objective Gradient}

\slides{
$$\begin{align*}
\frac{\text{d}E(\mappingVector)}{\text{d}\mappingVector} = & -\sum_{i=1}^\numData
\dataScalar_i\left(1-g\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i) \\ & + \sum_{i=1}^\numData
(1-\dataScalar_i)\left(g\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i).
\end{align*}$$
}

\newslide{Optimization of the Function}

\slides{
* Can't find a stationary point of the objective function analytically.
* Optimization has to proceed by *numerical methods*. 
    * [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) or 
    * [gradient based optimization methods](http://en.wikipedia.org/wiki/Gradient_method)
* Similarly to matrix factorization, for large data *stochastic gradient descent*  (Robbins Munro [@Robbins:stoch51] optimization procedure) works well.
}

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
### Movie Body Count Data

Let's recreate the movie body count example we used with naive Bayes. We can load in the data from `pods` as follows.

\setupcode{import pods}
\code{# Change this example for 2016#data = pods.datasets.movie_body_count_r_classify()
data = pods.datasets.olivetti_glasses()
X = data['X']
y = data['Y']}

### Gradient Descent

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

### Stochastic Gradient Descent

Now construct a stochastic gradient descent algorithm and run it on the data. Is it faster or slower than batch gradient descent? What can you do to improve convergence speed?

### Going Further: Optimization

Other optimization techniques for generalized linear models include [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method), it requires you to compute the Hessian, or second derivative of the objective function.

Methods that are based on gradients only include [L-BFGS](http://en.wikipedia.org/wiki/Limited-memory_BFGS) and [conjugate gradients](http://en.wikipedia.org/wiki/Conjugate_gradient_method). Can you find these in python? Are they suitable for very large data sets?
}

\notes{
### Other GLMs

We've introduced the formalism for generalized linear models. Have a think about how you might model count data using the [Poisson distribution](http://en.wikipedia.org/wiki/Poisson_distribution) and a log link function for the rate, $\lambda(\inputVector)$. If you want a data set you can try the `pods.datasets.google_trends()` for some count data.
}

\newslide{Other GLMs}

\slides{
* Logistic regression is part of a family known as *generalized linear models*
* They all take the form 
  $$g^{-1}(\mappingFunction_i(x)) = \mappingVector^\top \basisVector(\inputVector_i)$$
* As another example let's look at *Poisson regression*.}

\newslide{Poisson Distribution}

\slides{
* Poisson distribution is used for 'count data'. For non-negative integers, $y$, 
  $$P(y) = \frac{\lambda^y}{y!}\exp(-y)$$
* Here $\lambda$ is a *rate* parameter that can be thought of as the number of arrivals per unit time.
* Poisson distributions can be used for disease count data. E.g. number of incidence of malaria in a district.
}

\setupplotcode{import teaching_plots as plot}

\plotcode{plot.poisson('../slides/diagram/ml/')}

\newslide{Poisson Distribution}

\includesvg{../slides/diagrams/ml/poisson.svg}

\newslide{Poisson Regression}

\slides{
* In a Poisson regression make rate a function of space/time.
  $$\log \lambda(\inputVector, t) = \mappingVector_x^\top
\basisVector_\inputScalar(\inputVector) + \mappingVector_t^\top \basisVector_t(t)$$
* This is known as a *log linear* or *log additive* model. 
* The link function is a logarithm.
* We can rewrite such a function as 
  $$\log \lambda(\inputVector, t) = \mappingFunction_x(\inputVector) + \mappingFunction_t(t)$$
}

\newslide{Multiplicative Model}

\slides{
* Be careful though ... a log additive model is really multiplicative.
  $$\log \lambda(\inputVector, t) = \mappingFunction_x(\inputVector) + \mappingFunction_t(t)$$
* Becomes $$\lambda(\inputVector, t) = \exp(\mappingFunction_x(\inputVector) + \mappingFunction_t(t))$$
* Which is equivalent to  $$\lambda(\inputVector, t) = \exp(\mappingFunction_x(\inputVector))\exp(\mappingFunction_t(t))$$
* Link functions can be deceptive in this way.
}


### Bayesian Approaches

\exercise{Can you place a prior density over the parameters $\mappingVector$ and marginalize them out like we did for linear regression? If not why not?}


\newslide{Reading}

\slides{
* Section 5.2.2 of @Rogers:book11 up to pg 182.
}

### References


