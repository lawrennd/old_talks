---
layout: lecture
title: "Bayesian Regression"
abstract: "Bayesian formalisms deal with uncertainty in parameters, "
week: 6
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2015-11-03
ipynb: True
venue: University of Sheffield
postdir: ../../../mlatcl/mlai/_lectures/
slidedir: ../../../mlatcl/mlai/slides/
notedir: ../../../mlatcl/mlai/_notes/
notebookdir: ../../../mlatcl/mlai/_notebooks/
transition: None
youtube: 17zr5dGcUzE
---

\include{talk-macros.tex}

\subsection{Overdetermined System}

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

\addreading{@Bishop:book06}{Section 1.2.3 (pg 21–24)}
\addreading{@Rogers:book11}{Sections 3.1-3.4 (pg 95-117)}
\addreading{@Bishop:book06}{Section 1.2.3 (pg 21–24)}
\addreading{@Bishop:book06}{Section 1.2.6 (start from just past eq 1.64 pg 30-32)}

\reading

\include{_physics/includes/gauss-least-squares.md}
\include{_ml/includes/the-bayesian-approach.md}
\include{_ml/includes/bayesian-regression1d.md}
\include{_ml/includes/bayesian-1d-maths.md}

\subsection{The Joint Density}

* Really want to know the *joint* posterior density over the parameters $c$ *and* $m$.
* Could now integrate out over $m$, but it’s easier to consider the multivariate case.

\include{_ml/includes/two-d-gaussian.md}

\subsection{The Prior Density}

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


\addreading{@Bishop:book06}{Multivariate Gaussians: Section 2.3 up to top of pg 85}
\addreading{@Bishop:book06}{Section 3.3 up to 159 (pg 152–159)}

\reading

\newslide{Revisit Olympics Data}
\slides{
* Use Bayesian approach on olympics data with polynomials.

* Choose a prior $\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}$ with $\alpha = 1$.

* Choose noise variance $\dataStd^2 = 0.01$
}

\include{_ml/includes/prior-sampling-basis.md}
\include{_ml/includes/posterior-computation-gaussian.md}
\include{_ml/includes/olympic-bayesian-polynomials.md}

\newslide{Model Fit}

\slides{
* Marginal likelihood doesn’t always increase as model order increases.
* Bayesian model always has 2 parameters, regardless of how many basis functions (and here we didn’t even fit them).
* Maximum likelihood model over fits through increasing number of parameters.
* Revisit maximum likelihood solution with validation set.
}

\newslide{Regularized Mean}

\slides{
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

\addreading{@Rogers:book11}{Section 3.7–3.8 (pg 122–133)}
\addreading{@Bishop:book06}{Section 3.4 (pg 161–165)}

\reading

\thanks

\references






