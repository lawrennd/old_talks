### Approximate Gaussian Processes


\include{../../_gp/includes/low_rank_motivation.md}
\include{../../_gp/includes/gp_variational_complexity.md}
\include{../../_gp/includes/bottleneck.md}

### Information capture {data-transition="None"}

-   Everything we want to do with a GP involves marginalising
$\mappingFunctionVector$

    -   Predictions

    -   Marginal likelihood

    -   Estimating covariance parameters

-   The posterior of $\mappingFunctionVector$ is the central object. This
means inverting $\Kff$.

\include{../../_gp/includes/nystrom.md}
\include{../../_gp/includes/inducing_notation.md}
\include{../../_gp/includes/inducing_introduction.md}

### The alternative posterior

[Instead of doing]{}
$$p(\mappingFunctionVector\given\dataVector,\inputMatrix) = \frac{p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix)}{\int p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix){\text{d}\mappingFunctionVector}}$$
[We’ll do]{}
$$p(\inducingVector\given\dataVector,\inducingInputMatrix) = \frac{p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)}{\int p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix){\text{d}\inducingVector}}$$
\pause
\centering\alert{but $p(\dataVector\given\inducingVector)$ involves inverting $\Kff$}

<!--Flexible Parametric Approximation-->

\include{../../_gp/includes/larger_graph_intro.md}
\include{../../_gp/includes/larger_variational.md}
\include{../../_gp/includes/larger_factorize.md}


###

\LARGE$$\mappingFunctionVector, \inducingVector \sim \gaussianSamp{\mathbf{0}}{\begin{bmatrix}\Kff & \Kfu\\\Kuf & \Kuu\end{bmatrix}}$$
$$\dataVector|\mappingFunctionVector = \prod_{i} \gaussianSamp{\mappingFunction}{\dataStd^2}$$

<!--Variational Compression-->

\include{../../_gp/includes/variational_compression.md}
\include{../../_gp/includes/low_rank_variational.md}
\include{../../_gplvm/includes/bayes_gplvm_intro.md}
\include{../../_gplvm/includes/variational_bayes_gplvm_long.md}
\include{../../_gplvm/includes/nested_variational_compression.md}
\include{../../_gp/includes/larger_gaussian.md}

### Efficient Computation

* Thang and Turner paper

### Other Limitations 

* Joint Gaussianity is analytic, but not flexible.


