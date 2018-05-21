### Expected Loss

\notes{Our objective function so far has been the negative log likelihood, which we have minimized (via the sum of squares error) to obtain our model. However, there is an alternative perspective on an objective function, that of a *loss function*. A loss function is a cost function associated with the penalty you might need to pay for a particular incorrect decision. One approach to machine learning involves specifying a loss function and considering how much a particular model is likely to cost us across its lifetime. We can represent this with an expectation. If our loss function is given as $L(\dataScalar, \inputScalar, \mappingVector)$ for a particular model that predicts $\dataScalar$ given $\inputScalar$ and $\mappingVector$ then we are interested in minimizing the expected loss under the likely distribution of $\dataScalar$ and $\inputScalar$. To understand this formally we define the *true* distribution of the data samples, $\dataScalar$, $\inputScalar$. This is a particularl distribution that we don't have access to very often, and to represent that we define it with a variant of the letter 'P', $\mathbb{P}(\dataScalar, \inputScalar)$. If we genuinely pay $L(\dataScalar, \inputScalar, \mappingVector)$ for every mistake we make, and the future test data is genuinely drawn from $\mathbb{P}(\dataScalar, \inputScalar)$ then we can define our expected loss, or risk, to be,}
$$
R(\mappingVector) = \int L(\dataScalar, \inputScalar, \mappingVector) \mathbb{P}(\dataScalar, \inputScalar) \text{d}\dataScalar
\text{d}\inputScalar.
$$
\notes{Of course, in practice, this value can't be computed *but* it serves as a reminder of what it is we are aiming to minimize and under certain circumstances it can be approximated.
}

### Sample Based Approximations
\notes{A sample based approximation to an expectation involves replacing the true expectation with a sum over samples from the distribution.}\slides{* Sample based approximation: replace true expectation with sum over samples.}
  $$
  \int \mappingFunction(z) p(z) \text{d}\dataScalar
  \text{d}z\approx \frac{1}{s}\sum_{i=1}^s \mappingFunction(z_i).
  $$
\notes{if $\{z_i\}_{i=1}^s$ are a set of $s$ independent and identically distributed samples from the distribution $p(z)$. This approximation becomes better for larger $s$, although the *rate of convergence* to the true integral will be very dependent on the distribution $p(z)$ *and* the function $\mappingFunction(z)$.

That said, this means we can approximate our true integral with the sum,}\slides{* Allows us to approximate true integral with sum}
  $$
  R(\mappingVector) \approx \frac{1}{\numData}\sum_{i=1}^{\numData} L(\dataScalar_i, \inputScalar_i, \mappingVector),
  $$
