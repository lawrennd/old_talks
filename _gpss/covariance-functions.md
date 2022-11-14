---
title: Covariance Functions and Hyperparameter Optimization
week: 3
featured_image: slides/diagrams/kern/sinc_covariance.gif
abstract: >
  In this talk we review covariance functions and optimization of the GP log likelihoood.
author: 
- given: Neil D. 
  family: Lawrence
affiliation: University of Cambridge
transition: None
---

<!-- To compile -->


\include{_gpss/includes/gpss-notebook-setup.md}

\include{_gp/includes/gp-covariance-function-importance.md}
\include{_gp/includes/gp-numerics-and-optimization.md}
\include{_gp/includes/gp-optimize.md}

\include{_kern/includes/eq-covariance.md}
\include{_kern/includes/computing-rbf-covariance.md}

\comment{Markov property}
\include{_kern/includes/brownian-covariance.md}
\include{_kern/includes/precision-matrices.md}
\include{_kern/includes/ou-covariance.md}

\comment{Basis functions}
\include{_kern/includes/basis-covariance.md}
\include{_kern/includes/rbf-basis-covariance.md}

\comment{Fourier space}
\include{_kern/includes/boechners-theorem.md}
\include{_kern/includes/sinc-covariance.md}
\include{_kern/includes/matern32-covariance.md}
\include{_kern/includes/matern52-covariance.md}

\comment{Scale mixture}
\include{_kern/includes/ratquad-covariance.md}

\comment{Polynomial}
\include{_kern/includes/poly-covariance.md}

\comment{Periodic}
\include{_kern/includes/periodic-covariance.md}

\comment{Infinite Neural Networks}
\include{_kern/includes/mlp-covariance.md}
\include{_kern/includes/relu-covariance.md}

\comment{Combining Covariances}
\include{_kern/includes/add-covariance.md}
\include{_kern/includes/prod-covariance.md}

\comment{Examples of Deploying Kernels}
\include{_gp/includes/mauna-loa-gp.md}
\include{_gp/includes/box-jenkins-airline-gp.md}


\comment{Spectral Mixture Kernel}
\include{_kern/includes/spectral-mixture-kernel.md}

\thanks

\references



