\ifndef{approximateGpsShort}
\define{approximateGpsShort}
\editme

\subsection{Low Rank Gaussian Processes}

talk-macros.gpp}p/includes/sparse-gp-comic.md}
talk-macros.gpp}p/includes/low-rank-motivation.md}
talk-macros.gpp}p/includes/gp-variational-complexity.md}
<!--include{_gp/includes/larger-factorize.md}-->
talk-macros.gpp}p/includes/bottleneck.md}

\subsection{Augment Variable Space}

\notes{In inducing variable approximations, we augment the variable space with a set of inducing points, $\inducingVector$. These inducing points are jointly Gaussian distributed with the points from our function, $\mappingFunctionVector$. So we have a joint Gaussian process with covariance,}\slides{* Augment variable space with inducing observations, $\inducingVector$}
$$
\begin{bmatrix}
\mappingFunctionVector\\
\inducingVector
\end{bmatrix} \sim \gaussianSamp{\zerosVector}{\kernelMatrix}
$$
\notes{where the kernel matrix itself can be decomposed into}\slides{with}
$$
\kernelMatrix =
\begin{bmatrix}
\Kff & \Kfu \\
\Kuf & \Kuu
\end{bmatrix}
$$

\newslide{Joint Density}

\notes{This defines a joint density between the original function points, $\mappingFunctionVector$ and our inducing points, $\inducingVector$. This can be decomposed through the product rule to give.}
$$
p(\mappingFunctionVector, \inducingVector) = p(\mappingFunctionVector| \inducingVector) p(\inducingVector)
$$
\notes{The Gaussian process is (typically) given by a noise corrupted form of $\mappingFunctionVector$, i.e.,}\slides{to augment our model}
$$
\dataScalar(\inputVector) = \mappingFunction(\inputVector) + \noiseScalar,
$$
\notes{which can be written probabilisticlly as,}\slides{giving}
$$
p(\dataVector) = \int p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector) \text{d}\mappingFunctionVector,
$$
where for the independent case we have $p(\dataVector | \mappingFunctionVector) = \prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i)$.

\newslide{Auxilliary Variables}

\notes{Inducing variables are like auxilliary variables in Monte Carlo algorithms. We introduce the inducing variables by augmenting this integral with an additional integral over $\inducingVector$,}
$$
p(\dataVector) = \int p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector|\inducingVector)  p(\inducingVector)  \text{d}\inducingVector \text{d}\mappingFunctionVector.
$$
\notes{Now, conceptually speaking we are going to integrate out $\mappingFunctionVector$, initially leaving $\inducingVector$ in place. This gives,}\slides{Integrating over $\mappingFunctionVector$}
$$
p(\dataVector) = \int p(\dataVector|\inducingVector)   p(\inducingVector)  \text{d}\inducingVector.
$$

\newslide{Parametric Comparison}

\notes{Note the similarity between this form and our standard *parametric* form. If we had defined our model through standard basis functions we would have,}
$$
\dataScalar(\inputVector) = \weightVector^\top\basisVector(\inputVector) + \noiseScalar
$$
\notes{and the resulting probabilistic representation would be}
$$
p(\dataVector) = \int p(\dataVector|\weightVector) p(\weightVector) \text{d} \weightVector
$$
\notes{allowing us to predict}
$$
p(\dataVector^*|\dataVector) = \int p(\dataVector^*|\weightVector) p(\weightVector|\dataVector) \text{d} \weightVector
$$

\newslide{New Form}

\notes{The new prediction algorithm involves}
$$
p(\dataVector^*|\dataVector) = \int p(\dataVector^*|\inducingVector) p(\inducingVector|\dataVector) \text{d} \inducingVector
$$
\notes{but *importantly* the length of $\inducingVector$ is not fixed at *design* time like the number of parameters were. We can vary the number of inducing variables we use to give us the model capacity we require.}
\slides{* but $\inducingVector$ is not a *parameter*}

\notes{Unfortunately, computation of $p(\dataVector|\inducingVector)$ turns out to be intractable. As a result, we need to turn to approximations to make progress.}
\slides{* Unfortunately computing $p(\dataVector|\inducingVector)$ is intractable}

talk-macros.gpp}p/includes/larger-variational.md}
<!--include{_gp/includes/larger-graph-intro.md}-->
talk-macros.gpp}p/includes/inducing-variables-demo.md}

\endif
