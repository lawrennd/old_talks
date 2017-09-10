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

\include{notation_def.tex}

\include{../gp/includes/gp-book.md}

### The Gaussian Density

\include{../ml/includes/univariate_gaussian.md}
\include{../gp/includes/univariate_gaussian_properties.md}
\include{../ml/includes/linear_function.md}
\include{../ml/includes/regression_examples.md}
\include{../ml/includes/overdetermined_inaugural.md}
\include{../ml/includes/underdetermined_system.md}


### Probability for Under- and Overdetermined {.allowframebreaks}

-   To deal with overdetermined introduced probability distribution for
    ‘variable’, ${\epsilon}_i$.

-   For underdetermined system introduced probability distribution for
    ‘parameter’, $c$.

-   This is known as a Bayesian treatment.


### Multivariate Analysis

-   For general Bayesian inference need multivariate priors.

-   E.g. for multivariate linear regression:

    <!--overprint start-->
    \onslide<1> $${y}_i = \sum_i {w}_j {x}_{i, j} + \epsilon_i$$
    \onslide<2>
    $${y}_i = {\mathbf{{w}}}^\top {{\bf {x}}}_{i, :} + \epsilon_i$$

    <!--overprint end-->
    (where we’ve dropped $c$ for convenience), we need a prior over
    ${\mathbf{{w}}}$.

-   This motivates a *multivariate* Gaussian density.

-   We will use the multivariate Gaussian to put a prior *directly* on
    the function (a Gaussian process).


### Bayesian Regression

\include{../ml/includes/bayesian_regression1d_short.md}

### Multivariate Bayesian Regression

\include{../ml/includes/multivariate_bayesian_linear_short.md}

### Two Dimensional Gaussian Distribution

\include{../ml/includes/two_d_gaussian.md}

### Multivariate Gaussian Properties

\include{../gp/includes/multivariate_gaussian_properties.md}

### Distributions over Functions

\include{../gp/includes/gpdistfunc.md}

### Two Point Marginals

\include{../gp/includes/gptwopointpred.md}

\include{../kern/includes/rbfcovariance.md}
\include{../kern/includes/computing_rbf_covariance.md}

### Covariance from Basis Functions

\include{../gp/includes/basis_functions.md}

###  An Alternative Analysis 

\include{../gp/includes/gp_covariance_construction.md}
\include{../kern/includes/rbfbasiscovariance.md}

### An Infinite Basis

\include{../gp/includes/infinite_basis.md}
\include{../kern/includes/rbfcovariance.md}
\include{../kern/includes/rbfbasiscovariance.md}

### References {.allowframebreaks}

\tiny

\bibliographystyle{pdf_abbrvnat}


