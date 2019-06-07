\ifndef{polynomialMarginalLikelihood}
\define{polynomialMarginalLikelihood}
\editme

\subsection{Marginal Likelihood}

* The marginal likelihood can also be computed, it has the form:
  $$
  p(\dataVector|\inputMatrix, \dataStd^2, \alpha) = \frac{1}{(2\pi)^\frac{n}{2}\left|\kernelMatrix\right|^\frac{1}{2}} \exp\left(-\frac{1}{2} \dataVector^\top \kernelMatrix^{-1} \dataVector\right)
  $$
  where $\kernelMatrix = \alpha \basisMatrix\basisMatrix^\top + \dataStd^2 \eye$.

* So it is a zero mean $\numData$-dimensional Gaussian with covariance matrix $\kernelMatrix$.
\endif
