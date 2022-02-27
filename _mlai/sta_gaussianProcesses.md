# Week 12: Gaussian Processes

### Neil D. Lawrence

### 15th December 2015

```{.python .input}
## Replace with material from GPSS (in prep)
```

```{.python .input}
import numpy as np
import pandas as pd
import pods
import matplotlib.pyplot as plt
import mlai
%matplotlib inline
```

\newslide{Review}

* Last week: Logistic Regression and Generalised Linear Models
* Introduced link functions and different transformations.
* Showed examples in classification and mentioned possibilities for disease rate models.
* This week: 
    * Gaussian Processes: non parametric Bayesian modelling

\newslide{Gaussian Processes}

* Basis function models give non-linear predictions.
* Need to choose number and location of basis functions. 
* Gaussian processes is a general framework (basis functions special case)
* Within the framework you can consider models with infinite basis functions.

talk-macros.gpp}p/includes/gptwopointpred.md}
\newslide{Sampling a Function}

**Multi-variate Gaussians**


\newslide{Gaussian Distribution Sample}

**Log Odds**

* model the *log-odds* with the basis functions.
* [odds](http://en.wikipedia.org/wiki/Odds) are defined as the ratio of the
probability of a positive outcome, to the probability of a negative outcome. 
* Probability is between zero and one, odds are:
  $$\frac{\pi}{1-\pi} $$
* Odds are between $0$ and $\infty$. 
* Logarithm of odds maps them to $-\infty$ to $\infty$.

\newslide{Logit Link Function}

* The [Logit function](http://en.wikipedia.org/wiki/Logit), 
  $$g^{-1}(\pi_i) = \log\frac{\pi_i}{1-\pi_i}.$$ This function is known as a *link function*.
* For a standard regression we take,
  $$
  f(\mathbf{x}_i) = \mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x}_i),
  $$
* For classification we perform a logistic regression. 
  $$
  \log \frac{\pi_i}{1-\pi_i} = \mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x}_i)
  $$

\newslide{Inverse Link Function}

We have defined the link function as taking the form $g^{-1}(\cdot)$ implying that the inverse link function is given by $g(\cdot)$.

Since we have defined,
$$
g^{-1}(\pi(\mathbf{x})) = \mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})
$$
we can write $\pi$ in terms of the *inverse
link* function, $g(\cdot)$ as 
$$
\pi(\mathbf{x}) = g(\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})).
$$


\newslide{Logistic function

* [Logistic](http://en.wikipedia.org/wiki/Logistic_function) (or sigmoid) squashes
real line to between 0   & 1. Sometimes also called a 'squashing function'.

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.logistic(diagrams='\writeDiagramsDir/ml')}

\includediagram{\diagramsDir/ml/logistic}


\newslide{Prediction Function}
* Can now write $\pi$ as a function of the input and the parameter vector as, $$\pi(\mathbf{x},\mathbf{w}) = \frac{1}{1+ \exp\left(-\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x})\right)}.$$

* Compute the output of a standard linear basis function composition ($\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})$, as we did for linear regression)

* Apply the inverse link function, $g(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}))$. 

* Use this value in a Bernoulli distribution to form the likelihood.

\newslide{Bernoulli Reminder}

* From last time $$P(y_i|\mathbf{w}, \mathbf{x}) = \pi_i^{y_i} (1-\pi_i)^{1-y_i}$$

* Trick for switching betwen probabilities
```python
def bernoulli(y, pi):
    if y == 1:
        return pi
    else:
return 1-pi
```

\newslide{Maximum Likelihood}


* Conditional independence of
data:$$P(\mathbf{y}|\mathbf{w}, \mathbf{X}) = \prod_{i=1}^n P(y_i|\mathbf{w},
\mathbf{x}_i). $$

\newslide{Log Likelihood}

\begin{align*}
\log P(\mathbf{y}|\mathbf{w}, \mathbf{X}) = &
\sum_{i=1}^n \log P(y_i|\mathbf{w}, \mathbf{x}_i) \\ = &\sum_{i=1}^n y_i \log
\pi_i \\ & + \sum_{i=1}^n (1-y_i)\log (1-\pi_i)
\end{align*}

\newslide{Objective Function}

* Probability of positive outcome for the $i$th data
point $$\pi_i = g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}_i)\right),$$
where $g(\cdot)$ is the *inverse* link function

* Objective function of the
form \begin{align*}
E(\mathbf{w}) = & -  \sum_{i=1}^n y_i \log
g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}_i)\right) \\& -
\sum_{i=1}^n(1-y_i)\log \left(1-g\left(\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x}_i)\right)\right).
\end{align*}

\newslide{Minimize Objective}

* Grdient wrt  $\pi(\mathbf{x};\mathbf{w})$
\begin{align*}
\frac{\text{d}E(\mathbf{w})}{\text{d}\mathbf{w}} = &
-\sum_{i=1}^n \frac{y_i}{g\left(\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x})\right)}\frac{\text{d}g(f_i)}{\text{d}f_i}
\boldsymbol{\phi(\mathbf{x}_i)} \\ & +  \sum_{i=1}^n
\frac{1-y_i}{1-g\left(\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x})\right)}\frac{\text{d}g(f_i)}{\text{d}f_i}
\boldsymbol{\phi(\mathbf{x}_i)}
\end{align*}

\newslide{Link Function Gradient}

* Also need gradient of inverse link function wrt
parameters.
\begin{align*}
g(f_i) &= \frac{1}{1+\exp(-f_i)}\\
&=(1+\exp(-f_i))^{-1}
\end{align*}
and the gradient can be computed as
\begin{align*}
\frac{\text{d}g(f_i)}{\text{d} f_i} & =
\exp(-f_i)(1+\exp(-f_i))^{-2}\\
& = \frac{1}{1+\exp(-f_i)}
\frac{\exp(-f_i)}{1+\exp(-f_i)} \\
& = g(f_i) (1-g(f_i))
\end{align*}

\newslide{Objective Gradient}

\begin{align*}
\frac{\text{d}E(\mathbf{w})}{\text{d}\mathbf{w}} = & -\sum_{i=1}^n
y_i\left(1-g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x})\right)\right)
\boldsymbol{\phi(\mathbf{x}_i)} \\ & + \sum_{i=1}^n
(1-y_i)\left(g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x})\right)\right)
\boldsymbol{\phi(\mathbf{x}_i)}.
\end{align*}

\newslide{Optimization of the Function}

* Can't find a stationary point of the objective function analytically.

* Optimization has to proceed by *numerical methods*. 
    * [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) or 
    * [gradient based optimization methods](http://en.wikipedia.org/wiki/Gradient_method)
* Similarly to matrix factorization, for large data *stochastic gradient descent*  (Robbins Munroe optimization procedure) works well.

\newslide{Ad Matching for Facebook}

* This approach used in many internet companies.
* Example: ad matching for Facebook.
  * Millions of advertisers
  * Billions of users
  * How do you choose who to show what?
    
* Logistic regression used in combination with [decision trees]()

* [Paper available here](http://www.herbrich.me/papers/adclicksfacebook.pdf)

\newslide{Other GLMs}

* Logistic regression is part of a family known as *generalized linear models*

* They all take the form $$g^{-1}(f_i(x)) = \mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}_i)$$

* As another example let's look at *Poisson regression*.

\newslide{Poisson Distribution}

* Poisson distribution is used for 'count data'. For
non-negative integers, $y$, $$P(y) = \frac{\lambda^y}{y!}\exp(-y)$$

* Here $\lambda$ is a *rate* parameter that can be thought of as the number of arrivals per unit time.

* Poisson distributions can be used for disease count data. E.g. number of incidence of malaria in a district.

\plotcode{plot.poisson(diagrams='\writeDiagramsDir/ml')}

\newslide{Poisson Distribution

\includediagram{\diagramsDir/ml/poisson}

\newslide{Poisson Regression}

* In a Poisson regression make rate a function of space/time.$$\log \lambda(\mathbf{x}, t) = \mathbf{w}_x^\top \boldsymbol{\phi_x(\mathbf{x})} + \mathbf{w}_t^\top \boldsymbol(\phi_t(t))$$

* This is known as a *log linear* or *log additive* model. 

* The link function is a logarithm.

* We can rewrite such a function as 
  $$
  \log \lambda(\mathbf{x},t) = f_x(\mathbf{x}) + f_t(t)
  $$

\newslide{Multiplicative Model}

* Be careful though ... a log additive model is really multiplicative.
  $$
  \log \lambda(\mathbf{x}, t) = f_x(\mathbf{x}) + f_t(t)
  $$

* Becomes $$\lambda(\mathbf{x}, t) = \exp(f_x(\mathbf{x}) + f_t(t))$$

* Which is equivalent to  
  $$
  \lambda(\mathbf{x}, t) = \exp(f_x(\mathbf{x}))\exp(f_t(t))
  $$

* Link functions can be deceptive in this way.

\newslide{Reading}

- Section 5.2.2 of @Rogers:book11 up to pg 182.
