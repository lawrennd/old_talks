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

### What is Machine Learning?

. . .

$$ \text{data} + \text{model} = \text{prediction}$$

. . .

-   $\text{data}$ : observations, could be actively or passively
    acquired (meta-data).

. . .

-   $\text{model}$ : assumptions, based on previous experience (other data!
    transfer learning etc), or beliefs about the regularities of
    the universe. Inductive bias.

. . .

-   $\text{prediction}$ : an action to be taken or a categorization or a
    quality score.

### The Gaussian density

\include{../ml/includes/univariate_gaussian.md}
\include{../ml/includes/univariate_gaussian_properties.md}
\include{../ml/includes/regression_examples.md}

### Olympic Marathon Data

<table>
<tr><td>
-   Gold medal times for Olympic Marathon since 1896.

-   Marathons before 1924 didn’t have a standardised distance.

-   Present results using pace per km.

-   In 1904 Marathon was badly organised leading to very slow times.
</td><td width="30%">
![image](../ml/diagrams/Stephen_Kiprotich.jpg)
<small>Image from Wikimedia Commons <http://bit.ly/16kMKHQ></small>
</td></tr>
</table>


### Olympic Marathon Data

<object data="../ml/diagrams/olympic_marathon.svg"  class="svgplot"></object> 

\include{../ml/includes/overdetermined_inaugural.md}
\include{../ml/includes/underdetermined_system.md}


### Probability for Under- and Overdetermined {.allowframebreaks}

-   To deal with overdetermined introduced probability distribution for
    ‘variable’, ${\epsilon}_i$.

. . .

-   For underdetermined system introduced probability distribution for
    ‘parameter’, $c$.

. . .

-   This is known as a Bayesian treatment.


### Bayesian Regression

\include{../ml/includes/bayesian_regression1d_short.md}


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

\include{../ml/includes/multivariate_bayesian_linear_short.md}

### Two Dimensional Gaussian Distribution

\include{../ml/includes/two_d_gaussian.md}

### Multivariate Gaussian Properties

\include{../gp/includes/multivariate_gaussian_properties.md}

### Distributions over Functions

\include{../gp/includes/gpdistfunc.md}

### References {.allowframebreaks}

\tiny

\bibliographystyle{pdf_abbrvnat}


