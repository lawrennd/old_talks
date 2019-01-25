\ifndef{approximateGps}
\define{approximateGps}
\editme

\include{_gp/includes/sparse-gp-comic.md}

\newslide{Approximate Gaussian Processes}


\include{_gp/includes/low-rank-motivation.md}
\include{_gp/includes/gp-variational-complexity.md}
\include{_gp/includes/bottleneck.md}

\newslide{Information capture}

* Everything we want to do with a GP involves marginalising $\mappingFunctionVector$
  * Predictions
  * Marginal likelihood
  * Estimating covariance parameters
* The posterior of $\mappingFunctionVector$ is the central object. This
means inverting $\Kff$.

\include{_gp/includes/nystrom.md}
\include{_gp/includes/inducing-notation.md}
\include{_gp/includes/inducing-introduction.md}

\newslide{The alternative posterior}

[Instead of doing]{}
$$
p(\mappingFunctionVector\given\dataVector,\inputMatrix) = \frac{p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix)}{\int p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix){\text{d}\mappingFunctionVector}}
$$
[We’ll do]{}
$$
p(\inducingVector\given\dataVector,\inducingInputMatrix) = \frac{p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)}{\int p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix){\text{d}\inducingVector}}
$$
\centering\alert{but $p(\dataVector\given\inducingVector)$ involves inverting $\Kff$}

<!--Flexible Parametric Approximation-->

\include{_gp/includes/larger-graph-intro.md}
\include{_gp/includes/larger-variational.md}
\include{_gp/includes/larger-factorize.md}

\newslide{Inducing Variables}

* Choose to go a different way.
* Introduce a set of auxiliary variables, $\inducingVector$, which are $m$ in length.
* They are like "artificial data".
* Used to *induce* a distribution: $q(\inducingVector|\dataVector)$

\newslide{Making Parameters non-Parametric}

* Introduce variable set which is *finite* dimensional.
$$
p(\dataVector^*|\dataVector) \approx \int p(\dataVector^*|\inducingVector) q(\inducingVector|\dataVector) \text{d}\inducingVector
$$

* But dimensionality of $\inducingVector$ can be changed to improve approximation.

\newslide{Variational Compression}

* Model for our data, $\dataVector$
\columns{
$$p(\dataVector)$$
}{
\includediagram{../slides/diagrams/gp/py}
}

\newslide{Variational Compression}

* Prior density over $\mappingFunctionVector$. Likelihood relates data, $\dataVector$, to $\mappingFunctionVector$.
\columns{
$$p(\dataVector)=\int p(\dataVector|\mappingFunctionVector)p(\mappingFunctionVector)\text{d}\mappingFunctionVector$$
}{
\includediagram{../slides/diagrams/gp/pygfpf}
}

\newslide{Variational Compression}

* Prior density over $\mappingFunctionVector$. Likelihood relates data, $\dataVector$, to $\mappingFunctionVector$.
\columns{
$$p(\dataVector)=\int p(\dataVector|\mappingFunctionVector)p(\inducingVector|\mappingFunctionVector)p(\mappingFunctionVector)\text{d}\mappingFunctionVector\text{d}\inducingVector$$
}{
\includediagram{../slides/diagrams/gp/pygfpugfpf}
}

\newslide{Variational Compression}

\columns{
$$p(\dataVector)=\int \int p(\dataVector|\mappingFunctionVector)p(\mappingFunctionVector|\inducingVector)\text{d}\mappingFunctionVector p(\inducingVector)\text{d}\inducingVector$$
}{
\includediagram{../slides/diagrams/gp/pygfpfgupu}
}

\newslide{Variational Compression}

\columns{
$$p(\dataVector)=\int \int p(\dataVector|\mappingFunctionVector)p(\mappingFunctionVector|\inducingVector)\text{d}\mappingFunctionVector p(\inducingVector)\text{d}\inducingVector$$
}{
\includediagram{../slides/diagrams/gp/pygfpfgupu2}
}

\newslide{Variational Compression}

\columns{
$$p(\dataVector|\inducingVector)=\int p(\dataVector|\mappingFunctionVector)p(\mappingFunctionVector|\inducingVector)\text{d}\mappingFunctionVector$$
}{
\includediagram{../slides/diagrams/gp/pygfpfgu}
}

\newslide{Variational Compression}

\columns{
$$p(\dataVector|\inducingVector)$$
}{
\includediagram{../slides/diagrams/gp/pygu}
}

\newslide{Variational Compression}

\columns{
$$p(\dataVector|\paramVector)$$
}{
\includediagram{../slides/diagrams/gp/pygtheta}
}

\newslide{Compression}

* Replace true $p(\inducingVector|\dataVector)$ with approximation $q(\inducingVector|\dataVector)$.
* Minimize KL divergence between approximation and truth.
* This is similar to the Bayesian posterior distribution.
* But it's placed over a set of 'pseudo-observations'.


\newslide{}

\LARGE$$\mappingFunctionVector, \inducingVector \sim \gaussianSamp{\mathbf{0}}{\begin{bmatrix}\Kff & \Kfu\\\Kuf & \Kuu\end{bmatrix}}$$
$$\dataVector|\mappingFunctionVector = \prod_{i} \gaussianSamp{\mappingFunction}{\dataStd^2}$$

<!--Variational Compression-->

\include{_gp/includes/variational-compression.md}
\include{_gp/includes/low-rank-variational.md}
\include{_gplvm/includes/bayes-gplvm-intro.md}
\include{_gplvm/includes/variational-bayes-gplvm-long.md}
\include{_gplvm/includes/nested-variational-compression.md}
\include{_gp/includes/larger-gaussian.md}

\newslide{Efficient Computation}

* Thang and Turner paper

\newslide{Other Limitations}

* Joint Gaussianity is analytic, but not flexible.

\include{_gp/includes/inducing-variables-demo.md}

\endif
