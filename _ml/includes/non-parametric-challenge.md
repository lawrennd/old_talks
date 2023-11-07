\ifndef{nonParametricChallenge}
\define{nonParametricChallenge}

\editme


\subsection{The Nonparametric Challenge}

\notes{We have argued that we want models that are unconstrained, at
design time, by a fixed bandwidth for the communication between the
training data, $\dataVector$, and the test data, $\dataVector^*$ and
that the answer is to be nonparametric. By nonparametric we are
proposing using classes of models for which the conditional
distribution, $p(\dataVector^*|\dataVector)$ is not decomposable into
the expectation of $p(\dataVector^*|\paramVector)$ under the posterior
distribution of the parameters, $p(\paramVector|\dataVector)$ for any
fixed length parameter vector $\paramVector$. We don't want to impose
such a strong constraint on our model at *design time*. Our model may
be required to be operational for many years and the true complexity
of the system being modeled may not even be well understood at *design
time*. We must turn to paradigms that allow us to be adaptable at *run
time*. Nonparametrics provides just such a paradigm, because the
effect parameter vector increases in size as we observe more
data. This seems ideal, but it also presents a problem.}

\notes{Human beings, despite are large, interconnected brains, only have finite
storage. It is estimated that we have between 100 and 1000 trillion synapses in our brains. Similar for digital computers, even the GPT-3 model is restricted to 175 billion parameters. So, we need to assume that we can
only store a finite number of things about the data $\dataVector$. This
seems to push us back towards nonparametric models. Here, though, we
choose to go a different way. We choose to introduce a set of auxiliary
variables, $\inducingVector$, which are $\numInducing$ in length. Rather
than representing the nonparametric density directly, we choose to
focus on storing information about $\inducingVector$. By storing
information about these variables, rather than storing all the data
$\dataVector$ we hope to get around this problem. In order for us to be
nonparametric about our predictions for $\dataVector*$ we must
condition on all the data, $\dataVector$. We can't any longer store an
intermediate distribution to represent our sum knowlege,
$p(\paramVector|\dataVector)$. Such an intermediate distribution is a
finite dimensional object, and nonparametrics implies that we cannot
store all the information in a finite dimensional distribution. This
presents a problem for real systems in practice. We are now faced with a
compromise; how can we have a distribution which is flexible enough to
respond at *run time* to unforeseen complexity in the training data?
Yet, simultaneously doesn't require unbounded storage to retain all the
information in the training data. We will now introduce a perspective on
variational inference that will allow us to retain the advantages of
both worlds. We will construct a parametric approximation to the true
nonparametric conditional distribution. But, importantly, whilst this
parametric approximation will suffer from the constraints on the
bandwidth of the TT channel that drove us to nonparametric models in
the first place, we will be able to change the number of parameters at
*run time* not simply at design time.}

\endif
