\ifndef{parametricBottleneck}
\define{parametricBottleneck}

\editme

\subsection{Parametric Bottleneck}

\notes{In practice Bayesian methods suggest placing a prior over
$\boldsymbol{\theta}$ and using the posterior,
$p(\boldsymbol{\theta}|\dataVector)$ for making predictions.}
\begin{align*} p(\dataVector^*|\dataVector) = \int \prod_i
p(\dataScalar_i^* |
\boldsymbol{\theta})p(\boldsymbol{\theta}|\dataVector)\text{d}\boldsymbol{\theta}.
\end{align*} 
\notes{We have a model that obeys Kolmogorov consistency,
and is sophisticated enough to represent the behavior of a very comlex
dataset, it may well require a large number of parameters, just like
those deep learning models. One way of seeing the requirement for a
large number of parameters is to look at how we are storing
information from the training data to pass to the test data. The sum
of all our knowledge about the training data is stored in the
conditional distribution of the parameters given the training data, the Bayesian *posterior* distribution, $p(\paramVector | \dataVector).$

A key design-time problem is the *parametric bottleneck*. If we choose
the number of parameters at design time, but the system turns out to
be more complicated that we expected, we need to design a new model to
deal with this complexity. The communication between the training data
and the test data is like an information channel. This TT channel has
a bandwidth that is restricted by our choice of the dimensionality of
$\boldsymbol{\theta}$ at *design* time. This seems foolish. It is the bonds of this constraint that deep learning models are breaking by being so over-parameterized. 

To deal with this challenge in a probabilistic model, we should allow for a communication channel that is very large, or potentially infinite. In mathematical terms this implies we should look at nonparametric approaches.}

\notes{If highly overparameterized models are the solution for deep learning, then extending to nonparametric could be the solution to retaining the necessary sense of indeterminedness that is required to cope with very complex systems when we have seen relatively little data.}



\endif
