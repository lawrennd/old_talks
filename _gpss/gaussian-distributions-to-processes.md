---
title: Gaussian Distributions to Processes
abstract: >
  In this sesson we go from the Gaussian distribution to the Gaussian process and in doing so we move from a finite system to an infinite system.
session: 2
---

\include{_gpss/includes/gpss-notebook-setup.md}

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
\include{_ml/includes/linear-model-overview.md}

\newslide{Distributions over Functions}

\include{_gp/includes/gp-intro-very-short.md}

\include{_gp/includes/gpdistfunc.md}

\include{_kern/includes/computing-rbf-covariance.md}

\include{_kern/includes/poly-covariance.md}
\include{_kern/includes/rbf-basis-covariance.md}
\include{_gp/includes/infinite-basis.md}

\thanks

\references
