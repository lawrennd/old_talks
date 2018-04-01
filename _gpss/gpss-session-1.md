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

\include{../talk-macros.tex}

\include{../_gp/includes/gp-book.md}
\include{../_ml/includes/what-is-ml.md}

### The Gaussian density

\include{../_ml/includes/univariate_gaussian.md}
\include{../_ml/includes/univariate_gaussian_properties.md}
\include{../_ml/includes/regression_examples.md}

### Olympic Marathon Data

<table>
<tr><td>
-   Gold medal times for Olympic Marathon since 1896.

-   Marathons before 1924 didn’t have a standardised distance.

-   Present results using pace per km.

-   In 1904 Marathon was badly organised leading to very slow times.
</td><td width="30%">
![image](../_ml/diagrams/Stephen_Kiprotich.jpg)
<small>Image from Wikimedia Commons <http://bit.ly/16kMKHQ></small>
</td></tr>
</table>


### Olympic Marathon Data

<object data="../_ml/diagrams/olympic_marathon.svg"  class="svgplot"></object> 

\include{../_ml/includes/overdetermined_inaugural.md}
\include{../_ml/includes/underdetermined_system.md}


### Probability for Under- and Overdetermined {.allowframebreaks}

-   To deal with overdetermined introduced probability distribution for
    ‘variable’, ${\epsilon}_i$.

. . .

-   For underdetermined system introduced probability distribution for
    ‘parameter’, $c$.

. . .

-   This is known as a Bayesian treatment.


### Bayesian Regression

\include{../_ml/includes/bayesian_regression1d_short.md}


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

\include{../_ml/includes/multivariate_bayesian_linear_short.md}

### Two Dimensional Gaussian Distribution

\include{../_ml/includes/two_d_gaussian.md}

### Multivariate Gaussian Properties

\include{../_gp/includes/multivariate_gaussian_properties.md}

### Distributions over Functions

\include{../_gp/includes/gpdistfunc.md}

### References {.allowframebreaks}

\tiny

\bibliographystyle{pdf_abbrvnat}


