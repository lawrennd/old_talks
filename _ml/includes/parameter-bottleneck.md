\ifndef{parametricBottleneck}
\define{parametricBottleneck}

\editme

\subsection{Parametric Bottleneck}

\notes{In practice Bayesian methods suggest placing a prior over
$\boldsymbol{\theta}$ and using the posterior,
$p(\boldsymbol{\theta}|\dataVector)$ for making predictions.}
\begin{align*} 
p(\dataVector^*|\dataVector) = \int \prod_i p(\dataScalar_i^* | \boldsymbol{\theta})p(\boldsymbol{\theta}|\dataVector)\text{d}\boldsymbol{\theta}.
\end{align*}
\notes{We have a model that obeys Kolmogorov consistency, and is sophisticated
enough to represent the behaviour of a very: it may well require a large
number of parameters. One way of seeing the requirement for a large
number of parameters is to look at how we are storing information from
the training data to pass to the test data. The sum of all our knowledge
about the training data is stored in the conditional distribution of the
parameters given the training data, Uncertainty complex systA key design
time problem is the *parametric bottleneck*. If we choose the number of
parameters at design time, but the system turns out to be more
complicated that we expected, we need to design a new model to deal with
this complexity. The communication between the training data and the
test data is like an information channel. This TT channel has a
bandwidth that is restricted by our choice of the dimensionality of
$\boldsymbol{\theta}$ at *design* time. This seems foolish. Better to
ensure we choose a model that allows for that channel to be potentially
infinite. This implies a non-parametric approach. Our prior over
$\boldsymbol{\theta}$ should be *non parametric*.}
$$
p(\paramVector | \dataVector),
$$
\notes{which, as we argued above, allows us to retain the necessary sense of
uncertainty about the parameters that is required in a very complex
system when we have seen relatively little data. How much information
can we store, then, about the training data? The information gain from
the training data is given by the Kullback Leibler divergence between
our prior distribution and our posterior distribution.}
$$
\KL{p(\paramVector|\dataVector)}{p(\paramVector)}
$$
\notes{This is the information gained, measured in 'nats' if we use natural
logarithms, but it could equally be measured in bits, about our
parameters having observed the training data. In the case that our
likelihood is log concave[^3] then this information gain provably will increase, with every
observed data point. How much information we gain will depend on the
likelihood associated with each data $\dataScalar_i$. This Kullback
Leibler divernece has an infomration theoretic interpretation as a
communication channel passing information from the training data to the
test data. From an information theoretic perspective, the channel
bandwidth is controlled by the dimensionality of the parameter vector
$\dataVector$ and the form of the prior $p(\paramVector)$.

[^3]: This is a definite constraint on the
model, there are many very reasonable likelihoods that are not log
concave.}


\endif
