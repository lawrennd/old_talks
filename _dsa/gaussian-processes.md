---
session: 4
title: Gaussian Processes
abstract: >
  Classical machine learning and statistical approaches to learning, such as neural networks and linear regression, assume a parametric form for functions. Gaussian process models are an alternative approach that assumes a probabilistic prior over functions. This brings benefits, in that uncertainty of function estimation is sustained throughout inference, and some challenges: algorithms for fitting Gaussian processes tend to be more complex than parametric models. 
  
  In this sessions I will introduce Gaussian processes and explain why sustaining uncertainty is important. 
date: 2020-11-13
venue: Virtual Data Science Nigeria
time: "15:00 (West Africa Standard Time)"
transition: None
---

\include{talk-macros.tex}
\include{_mlai/includes/mlai-notebook-setup.md}
\include{_gp/includes/gp-book.md}
<!--include{_gp/includes/what-is-a-gp.md}-->
\include{_gp/includes/gp-intro-lectures.md}
\include{_ml/includes/univariate-gaussian-properties.md}
\include{_ml/includes/two-d-gaussian.md}
\include{_ml/includes/multivariate-gaussian-properties.md}

\include{_ml/includes/basis-functions-intro.md}

\include{_gp/includes/gp-from-basis-functions.md}

\include{_gp/includes/non-degenerate-gps.md}
\include{_gp/includes/gp-function-space.md}

\include{_gp/includes/gptwopointpred.md}

\include{_gp/includes/gp-covariance-function-importance.md}
\include{_gp/includes/gp-numerics-and-optimization.md}

\include{_gp/includes/gp-optimize.md}
\include{_kern/includes/eq-covariance.md}
\include{_health/includes/malaria-gp.md}
\include{_gp/includes/gpy-software.md}
\include{_gp/includes/gpy-tutorial.md}
\include{_gp/includes/nigeria-covid-gp.md}


\subsection{Review}

\include{_gp/includes/gp-summer-school.md}
\include{_gp/includes/other-gp-software.md}

\reading

\thanks

\references



