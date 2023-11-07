\ifndef{poissonRegression}
\define{poissonRegression}

\include{_ml/includes/poisson-distribution.md}

\editme

\subsection{Poisson Regression}

\slides{
* In a Poisson regression make rate a function of space/time.
  $$\log \lambda(\inputVector, t) = \mappingVector_x^\top
\basisVector_\inputScalar(\inputVector) + \mappingVector_t^\top \basisVector_t(t)$$
* This is known as a *log linear* or *log additive* model. 
* The link function is a logarithm.
* We can rewrite such a function as 
  $$\log \lambda(\inputVector, t) = \mappingFunction_x(\inputVector) + \mappingFunction_t(t)$$
}

\newslide{Multiplicative Model}

\slides{
* Be careful though ... a log additive model is really multiplicative.
  $$\log \lambda(\inputVector, t) = \mappingFunction_x(\inputVector) + \mappingFunction_t(t)$$
* Becomes $$\lambda(\inputVector, t) = \exp(\mappingFunction_x(\inputVector) + \mappingFunction_t(t))$$
* Which is equivalent to  $$\lambda(\inputVector, t) = \exp(\mappingFunction_x(\inputVector))\exp(\mappingFunction_t(t))$$
* Link functions can be deceptive in this way.
}

\endif
