---
title: Introduction to Gaussian Processes
author: Neil D. Lawrence
slide-level: 3
blibliography: 
- lawrence.bib
  other.bib
  zbooks.bib
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

\include{_ml/includes/underdetermined_system.md}

### Overdetermined System

-   With two unknowns and two observations: 
    $$\begin{aligned}
          y_1 = & mx_1 + c\\
          y_2 = & mx_2 + c
        \end{aligned}$$

-   Additional observation leads to *overdetermined* system.
    $$y_3 =  mx_3 + c$$

-   This problem is solved through a noise model
    $\epsilon \sim \mathcal{N}(0,\sigma^2)$ $$\begin{aligned}
          y_1 = mx_1 + c + \epsilon_1\\
          y_2 = mx_2 + c + \epsilon_2\\
          y_3 = mx_3 + c + \epsilon_3
        \end{aligned}$$

### Noise Models

-   We aren’t modeling entire system.

-   Noise model gives mismatch between model and data.

-   Gaussian model justified by appeal to central limit theorem.

-   Other models also possible (Student-$t$ for heavy tails).

-   Maximum likelihood with Gaussian noise leads to *least squares*.

### Probability for Under- and Overdetermined {.allowframebreaks}

-   To deal with overdetermined introduced probability distribution for
    ‘variable’, ${\epsilon}_i$.

. . .

-   For underdetermined system introduced probability distribution for
    ‘parameter’, $c$.

. . .

-   This is known as a Bayesian treatment.

### Different Types of Uncertainty

-   The first type of uncertainty we are assuming is
    *aleatoric* uncertainty.

-   The second type of uncertainty we are assuming is
    *epistemic* uncertainty.

### Aleatoric Uncertainty

-   This is uncertainty we couldn’t know even if we wanted to. e.g. the
    result of a football match before it’s played.

-   Where a sheet of paper might land on the floor.

### Epistemic Uncertainty

-   This is uncertainty we could in principal know the answer too. We
    just haven’t observed enough yet, e.g. the result of a football
    match *after* it’s played.

-   What colour socks your lecturer is wearing.

### Bayesian Regression

\include{_ml/includes/bayesian-regression1d-short.md}


### Multivariate Analysis

-   For general Bayesian inference need multivariate priors.

. . .

-   E.g. for multivariate linear regression:

$${y}_i = \sum_i \weightScalar_j \inputScalar_{i, j} + \noiseScalar_i$$

$${y}_i = \weightVector^\top \inputVector_{i, :} + \noiseScalar_i$$

(where we’ve dropped $c$ for convenience), we need a prior over
$\weightVector$.

. . .

-   This motivates a *multivariate* Gaussian density.

. . .

-   We will use the multivariate Gaussian to put a prior *directly* on
    the function (a Gaussian process).

### Multivariate Bayesian Regression

\include{_ml/includes/multivariate-bayesian-linear-short.md}

### Two Dimensional Gaussian Distribution

\include{_ml/includes/two-d-gaussian.md}

### Multivariate Gaussian Properties

<!-- Also a version of this under _ml/-->
\include{_gp/includes/multivariate-gaussian-properties.md}

### Distributions over Functions

\include{_gp/includes/gpdistfunc.md}

\include{_kern/includes/computing-rbf-covariance.md}

\include{_kern/includes/poly-covariance.md}
\include{_kern/includes/brownian-covariance.md}
\include{_kern/includes/periodic-covariance.md}



### References {.allowframebreaks}

\tiny

\bibliographystyle{pdf_abbrvnat}


