---
title: Introduction to Gaussian Processes
venue: "Gaussian Process Summer School, Sheffield"
abstract: >
  In this talk we introduce Gaussian process models. Motivating the representation of uncertainty through probability distributions we review Laplace's approach to understanding uncertainty and how uncertainty in functions can be represented through a multivariate Gaussian density.
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
published: 2018-09-03
reveal: 2018-09-03-gpss-session-1.slides.html
ipynb: 2018-09-03-gpss-session-1.ipynb
layout: talk
transition: None
date: 2018-09-03
---

<!-- To compile -->

\include{talk-macros.tex}

\include{_gp/includes/gp-book.md}
\include{_ml/includes/what-is-ml.md}

\include{_ml/includes/olympic-marathon-data.md}

\include{_ml/includes/overdetermined-inaugural.md}

\include{_ml/includes/univariate-gaussian.md}
\include{_ml/includes/univariate-gaussian-properties.md}
\include{_ml/includes/regression-examples.md}

\include{_ml/includes/underdetermined-system.md}

\newslide{Overdetermined System}
\slides{
* With two unknowns and two observations: 
    $$\begin{aligned}
          \dataScalar_1 = & m\inputScalar_1 + c\\
          \dataScalar_2 = & m\inputScalar_2 + c
        \end{aligned}$$

* Additional observation leads to *overdetermined* system.
    $$\dataScalar_3 =  m\inputScalar_3 + c$$
}

\newslide{Overdetermined System}
\slides{
* This problem is solved through a noise model
    $\noiseScalar \sim \gaussianSamp{0}{\dataStd^2}$ $$\begin{aligned}
          \dataScalar_1 = m\inputScalar_1 + c + \noiseScalar_1\\
          \dataScalar_2 = m\inputScalar_2 + c + \noiseScalar_2\\
          \dataScalar_3 = m\inputScalar_3 + c + \noiseScalar_3
        \end{aligned}$$
}

\newslide{Noise Models}
\slides{
* We aren’t modeling entire system.
* Noise model gives mismatch between model and data.
* Gaussian model justified by appeal to central limit theorem.
* Other models also possible (Student-$t$ for heavy tails).
* Maximum likelihood with Gaussian noise leads to *least squares*.
}

\newslide{Probability for Under- and Overdetermined}
\slides{
* To deal with overdetermined introduced probability distribution for
    ‘variable’, ${\noiseScalar}_i$.

. . .

* For underdetermined system introduced probability distribution for
    ‘parameter’, $c$.

. . .

* This is known as a Bayesian treatment.
}

\newslide{Different Types of Uncertainty}
\slides{
* The first type of uncertainty we are assuming is *aleatoric* uncertainty.
* The second type of uncertainty we are assuming is *epistemic* uncertainty.
}\notes{Classically, there are two types of uncertainty that we consider. The first is known as *aleatoric* uncertainty. This is uncertainty we couldn't resolve even if we wanted to. An example, would be the result of a football match before it's played, or where a sheet of paper lands on the floor. 

The second is known as *epistemic* uncertainty. This is uncertainty that we could, in principle, resolve. We just haven't yet made the observation. For example, the result of a football match *after* it is played, or the color of socks that a lecturer is wearing. 

Note, that there isn't a clean difference between the two. It is arguable, that if we knew enough about a football match, or the physics of a falling sheet of paper then we might be able to resolve the uncertainty. The reason we can't is because *chaotic* behaviour means that a very small change in any of the initial conditions we would need to resolve can have a large change in downstream effects. By this argument, the only truly aleatoric uncertainty might be quantum uncertainty. However, in practice the distinction is often applied. 

In classical statistics, the frequentist approach only treats *aleatoric* uncertainty with probability. The key philosophical difference in the *Bayesian* approach is to treat any unknowns through probability. This approach was formally justified seperately by @Cox:probability46 and @deFinetti:prevision37.}

\notes{The term Bayesian was a mocking term promoted by Fisher, it comes from the use, by Bayes, of a billiard table formulation to justify the Bernoulli distribution. Bayes considers a ball landing uniform at random between two sides of a billiard table. He then considers the outcome of the Bernoulli as being whether a second ball comes to rest to the right or left of the original. In this way, the parameter of his Bernoulli distribution is a *stochastic variable* (the uncertainty in the parameter is aleatoric). In contrast, when Bernoulli formulates the distribution he considers a bag of red and black balls. The parameter of his Bernoulli is the ratio of red balls to total balls, a deterministic variable.

Note how this relates to Laplace's demon. Laplace describes the deterministic universe ("... for it nothing would be uncertain and the future, as the past, would be present in its eyes"), but acknowledges the impossibility of achieving this in practice, (" ... the curve described by a simple molecule of air or vapor is regulated in a manner just as certain as the planetary orbits; the only difference between them is that which comes from our ignorance. *Probability* is relative in part to this ignorance, in part to our knowledge ...)}

\newslide{Aleatoric Uncertainty}
\slides{
* This is uncertainty we couldn’t know even if we wanted to. e.g. the result of a football match before it’s played.
* Where a sheet of paper might land on the floor.
}

\newslide{Epistemic Uncertainty}
\slides{
* This is uncertainty we could in principle know the answer too. We just haven’t observed enough yet, e.g. the result of a football match *after* it’s played.
* What colour socks your lecturer is wearing.
}

\newslide{Bayesian Regression}

\include{_ml/includes/bayesian-regression1d-short.md}


\newslide{Multivariate System}
\slides{
* For general Bayesian inference need multivariate priors.

. . .

* E.g. for multivariate linear regression:
}\notes{For general Bayesian inference, over more than one parameter, we need *multivariate priors*. For example, consider the multivariate linear regression where an observation, $\dataScalar_i$ is related to a vector of features, $\inputVector_{i, :}$, through a vector of parameters, $\weightVector$,}
$$\dataScalar_i = \sum_j \weightScalar_j \inputScalar_{i, j} + \noiseScalar_i,$$
\notes{or in vector notation,}
$$\dataScalar_i = \weightVector^\top \inputVector_{i, :} + \noiseScalar_i.$$
\notes{Here we've dropped the intercpet for convenience, it can be reintroduced by augmenting the feature vector, $\inputVector_{i, :}$, with a constant valued feature.}\slides{ 
(where we’ve dropped $c$ for convenience), we need a prior over $\weightVector$.
}
\newslide{Multivariate System}
\slides{
* This motivates a *multivariate* Gaussian density.

. . .

* We will use the multivariate Gaussian to put a prior *directly* on the function (a Gaussian process).
}\notes{This motivates the need for a *multivariate* Gaussian density.}

\newslide{Multivariate Bayesian Regression}

\include{_ml/includes/multivariate-bayesian-linear-short.md}

\newslide{Two Dimensional Gaussian Distribution}

\include{_ml/includes/two-d-gaussian.md}

\newslide{Multivariate Gaussian Properties}

\include{_ml/includes/multivariate-gaussian-properties-summary.md}

\newslide{Linear Gaussian Models}
\slides{
Gaussian processes are initially of interest because
1. linear Gaussian models are easier to deal with 
2. Even the parameters *within* the process can be handled, by considering a particular limit.
}

\include{_ml/includes/multivariate-gaussian-properties.md}

\newslide{Distributions over Functions}

\include{_gp/includes/gp-intro-very-short.md}

\include{_gp/includes/gpdistfunc.md}

\include{_kern/includes/computing-rbf-covariance.md}

\include{_kern/includes/poly-covariance.md}
\include{_kern/includes/brownian-covariance.md}
\include{_kern/includes/periodic-covariance.md}

\include{_kern/includes/rbf-basis-covariance.md}

\include{_gp/includes/infinite-basis.md}

\include{_kern/includes/mlp-covariance.md}
<!--include{_kern/includes/relu-covariance.md}-->

\include{_kern/includes/sinc-covariance.md}


\newslide{References}

\tiny

\bibliographystyle{pdf_abbrvnat}


