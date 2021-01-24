---
week: 5
title: Basis Functions
abstract: |
  In the last session we explored least squares for univariate and multivariate *regression*. We introduced *matrices*, *linear algebra* and *derivatives*. 
  
  In this session we will introduce *basis functions* which allow us to implement *non-linear regression models*.
---

\include{talk-macros.gpp}

\include{_mlai/includes/mlai-notebook-setup.md}
\include{_ml/includes/non-linear-regression-intro.md}

\include{_ml/includes/basis-functions.md}
\include{_ml/includes/basis-function-models.md}

\addreading{@Rogers:book11}{Section 1.4}
\addreading{@Bishop:book06}{Chapter 1, pg 1-6}
\addreading{@Bishop:book06}{Chapter 3, Section 3.1 up to pg 143}

\reading

\subsection{Lecture on Basis Functions from GPRS Uganda}

\figure{\includeyoutube{PoNbOnUnOao}{600}{450}}{Lecture on Basis functions from GPRS in Uganda in 2013.}{basis-functions-gprs-uganda}

\subsection{Use of QR Decomposition for Numerical Stability}

\notes{In the last session we showed how rather than computing $\inputMatrix^\top\inputMatrix$ as an intermediate step to our solution, we could compute the solution to the regressiond directly through [QR-decomposition](http://en.wikipedia.org/wiki/QR_decomposition). Now we will consider an example with non linear basis functions where such computation is critical for forming the right answer.}

*TODO* example with polynomials.

\setupcode{import numpy as np}

\code{x = np.random.normal(size=(10, 1))}

\code{Phi = mlai.fourier(x, 5)}

\code{(np.dot(Phi.T,Phi))}

\code{Phi*Phi}

\thanks

\references
