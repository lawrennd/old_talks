---
layout: lectures
title: "Bayesian Regression"
abstract: "Bayesian formalisms deal with uncertainty in parameters, "
ipynb: 2015-11-03-week6.ipynb
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2015-11-03
venue: University of Sheffield
transition: None
---

\include{talk-macros.tex}

### Overdetermined System

\notes{We can motivate the introduction of probability by considering systems where there were more observations than unknowns. In particular we can consider the simple fitting of the gradient and an offset of a line,
$$ 
\dataScalar = m\inputScalar +c.
$$
What happens if we have three pairs of observations of $\inputScalar$ and $\dataScalar$, $\{\inputScalar_i, \dataScalar_i\}_{i=1}^3$. The issue can be solved by introducing a type of [slack variable](http://en.wikipedia.org/wiki/Slack_variable), $\noiseScalar_i$, known as noise, such that for each observation we had the equation,
$$
\dataScalar_i = m\inputScalar_i + c + \noiseScalar_i.
$$}

\slides{* With two unknowns and two observations:
  $$
  \begin{aligned}
  \dataScalar_1 = & m\inputScalar_1 + c\\
  \dataScalar_2 = & m\inputScalar_2 + c
  \end{aligned}
  $$
* Additional observation leads to *overdetermined* system.
  $$
  \dataScalar_3 =  m\inputScalar_3 + c
  $$
* This problem is solved through a noise model $\noiseScalar \sim \gaussianSamp{0}{\dataStd^2}$ 
  $$
  \begin{aligned}
  \dataScalar_1 = m\inputScalar_1 + c + \noiseScalar_1\\
          \dataScalar_2 = m\inputScalar_2 + c + \noiseScalar_2\\
          \dataScalar_3 = m\inputScalar_3 + c + \noiseScalar_3
  \end{aligned}
  $$}


<!-- \slides{A system of two simultaneous equations with two unknowns. -->

<!-- How do we deal with three simultaneous equations with only two unknowns? -->

<!-- $$ -->
<!-- \begin{aligned} -->
<!--   \dataScalar_1 = & m\inputScalar_1 + c\\ -->
<!--   \dataScalar_2 = & m\inputScalar_2 + c -->
<!-- \end{aligned} -->
<!-- $$  -->
      
<!-- $$ -->
<!-- \begin{aligned} -->
<!--   \dataScalar_1-\dataScalar_2 = & m(\inputScalar_1 - \inputScalar_2) -->
<!-- \end{aligned} -->
<!-- $$ -->
      
<!-- $$ -->
<!-- \begin{aligned} -->
<!--  \frac{\dataScalar_1-\dataScalar_2}{\inputScalar_1 - \inputScalar_2} = & m -->
<!-- \end{aligned} -->
<!-- $$  -->
      
<!-- $$ -->
<!-- \begin{aligned} -->
<!--   m & =\frac{\dataScalar_2-\dataScalar_1}{\inputScalar_2 - \inputScalar_1}\\ -->
<!--   c & = \dataScalar_1 - m \inputScalar_1 -->
<!-- \end{aligned} -->
<!-- $$ -->
<!-- $$ -->
<!-- \begin{aligned} -->
<!--   \dataScalar_1 = & m\inputScalar_1 + c\\ -->
<!--   \dataScalar_2 = & m\inputScalar_2 + c\\ -->
<!--   \dataScalar_3 = & m\inputScalar_3 + c -->
<!-- \end{aligned} -->
<!-- $$ -->
<!-- } -->

\include{_ml/includes/underdetermined-system.md}
\include{_ml/includes/types-of-uncertainty.md}

### Reading

* @Bishop:book06 Section 1.2.3 (pg 21–24).
* @Bishop:book06 Section 1.2.6 (start from just past eq 1.64 pg 30-32).
* Bayesian Inference
  - @Rogers:book11 use an example of a coin toss for introducing Bayesian inference Chapter 3, Sections 3.1-3.4 (pg 95-117). Although you also need the beta density which we haven’t yet discussed. This is also the example that @Laplace:memoire74 used.
  - @Bishop:book06 Section 1.2.3 (pg 21–24).
* @Bishop:book06 Section 1.2.6 (start from just past eq 1.64 pg 30-32).

\notes{
### Sum of Squares and Probability

In the overdetermined system we introduced a new set of slack variables, $\{\noiseScalar_i\}_{i=1}^\numData$, on top of our parameters $m$ and $c$. We dealt with the variables by placing a probability distribution over them. This gives rise to the likelihood and for the case of Gaussian distributed variables, it gives rise to the sum of squares error. It was Gauss who first made this connection in his volume on "Theoria Motus Corprum Coelestium" (written in Latin)

\setupcode{import pods}
\displaycode{pods.notebook.display_google_book(id='ORUOAAAAQAAJ', page='213')}

The relevant section roughly translates as

>... It is clear, that for the product $\Omega = h^\mu \pi^{-frac{1}{2}\mu} e^{-hh(vv + v^\prime v^\prime + v^{\prime\prime} v^{\prime\prime} + \dots)}$ to be maximised the sum $vv + v ^\prime v^\prime + v^{\prime\prime} v^{\prime\prime} + \text{etc}.$ ought to be minimized. *Therefore, the most probable values of the unknown quantities $p , q, r , s \text{etc}.$, should be that in which the sum of the squares of the differences between the functions $V, V^\prime, V^{\prime\prime} \text{etc}$, and the observed values is minimized*, for all observations of the same degree of precision is presumed.

It's on the strength of this paragraph that the density is known as the Gaussian, despite the fact that four pages later Gauss credits the necessary integral for the density to Laplace, and it was also Laplace that did a lot of the original work on dealing with these errors through probability. [Stephen Stigler's book on the measurement of uncertainty before 1900](http://www.hup.harvard.edu/catalog.php?isbn=9780674403413) has a nice chapter on this.

\code{pods.notebook.display_google_book(id='ORUOAAAAQAAJ', page='217')}

where the crediting to the Laplace is about halfway through the last paragraph. This book was published in 1809, four years after [Legendre presented least squares](./week3.ipynb) in an appendix to one of his chapters on the orbit of comets. Gauss goes on to make a claim for priority on the method on page 221 (towards the end of the first paragraph ...).

\code{pods.notebook.display_google_book(id='ORUOAAAAQAAJ', page='221')}
}

\include{_ml/includes/the-bayesian-approach.md}
\include{_ml/includes/bayesian-regression1d.md}
\include{_ml/includes/bayesian-1d-maths.md}

### The Joint Density

* Really want to know the *joint* posterior density over the parameters $c$ *and* $m$.
* Could now integrate out over $m$, but it’s easier to consider the multivariate case.

\include{_ml/includes/two-d-gaussian.md}

### The Prior Density

Let's assume that the prior density is given by a zero mean Gaussian, which is independent across each of the parameters, 
$$
\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}
$$ 
In other words, we are assuming, for the prior, that each element of the parameters vector, $\mappingScalar_i$, was drawn from a Gaussian density as follows
$$
\mappingScalar_i \sim \gaussianSamp{0}{\alpha}
$$
Let's start by assigning the parameter of the prior distribution, which is the variance of the prior distribution, $\alpha$.

\code{# set prior variance on w
alpha = 4.
# set the order of the polynomial basis set
order = 5
# set the noise variance
sigma2 = 0.01}


### Reading

* Section 2.3 of @Bishop:book06 up to top of pg 85 (multivariate Gaussians).

* Section 3.3 of @Bishop:book06 up to 159 (pg 152–159).

\slides{
### Revisit Olympics Data

* Use Bayesian approach on olympics data with polynomials.

* Choose a prior $\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}$ with $\alpha = 1$.

* Choose noise variance $\dataStd^2 = 0.01$
}

\include{_ml/includes/prior-sampling-basis.md}
\include{_ml/includes/posterior-computation-gaussian.md}
\include{_ml/includes/olympic-bayesian-polynomials.md}

\slides{
### Model Fit

* Marginal likelihood doesn’t always increase as model order increases.
* Bayesian model always has 2 parameters, regardless of how many basis functions (and here we didn’t even fit them).
* Maximum likelihood model over fits through increasing number of parameters.
* Revisit maximum likelihood solution with validation set.

### Regularized Mean

* Validation fit here based on mean solution for $\mappingVector$ only.
* For Bayesian solution
  $$
  \meanVector_w = \left[\dataStd^{-2}\basisMatrix^\top\basisMatrix + \alpha^{-1}\eye\right]^{-1} \dataStd^{-2} \basisMatrix^\top \dataVector
  $$
  instead of
  $$
  \mappingVector^* = \left[\basisMatrix^\top\basisMatrix\right]^{-1} \basisMatrix^\top \dataVector
  $$
* Two are equivalent when $\alpha \rightarrow \infty$.
* Equivalent to a prior for $\mappingVector$ with infinite variance.
* In other cases $\alpha \eye$ *regularizes* the system (keeps parameters smaller).
}
\include{_ml/includes/posterior-sampling-basis.md}
\include{_ml/includes/polynomial-marginal-likelihood.md}
\include{_ml/includes/compute-output-expectations.md}

### Reading

*   Section 3.7–3.8 of @Rogers:book11 (pg 122–133).

*   Section 3.4 of @Bishop:book06 (pg 161–165).







