\ifndef{largerVariational}
\define{largerVariational}
\editme

\subsection{Variational Bound on $p(\dataVector |\inducingVector)$}

\notes{The conditional density of the data given the inducing points can be *lower* bounded variationally}
$$
\begin{aligned}
    \log p(\dataVector|\inducingVector) & = \log \int p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector|\inducingVector) \text{d}\mappingFunctionVector\\ & = \int q(\mappingFunctionVector) \log \frac{p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector|\inducingVector)}{q(\mappingFunctionVector)}\text{d}\mappingFunctionVector + \KL{q(\mappingFunctionVector)}{p(\mappingFunctionVector|\dataVector, \inducingVector)}.
\end{aligned}
$$


\newslide{Choose form for $q(\cdot)$}

\notes{The key innovation from @Titsias:variational09 was to then make a particular choice for $q(\mappingFunctionVector)$. If we set}
\slides{* Set} $q(\mappingFunctionVector)=p(\mappingFunctionVector|\inducingVector)$,
  $$
  \log p(\dataVector|\inducingVector) \geq \int p(\mappingFunctionVector|\inducingVector) \log p(\dataVector|\mappingFunctionVector)\text{d}\mappingFunctionVector.
  $$
  $$
  p(\dataVector|\inducingVector) \geq \exp \int p(\mappingFunctionVector|\inducingVector) \log p(\dataVector|\mappingFunctionVector)\text{d}\mappingFunctionVector.
  $$
\slides{\alignright{\small [@Titsias:variational09]}}

\subsection{Optimal Compression in Inducing Variables}

\notes{Maximizing the lower bound minimizes the Kullback-Leibler divergence (or *information gain*) between our approximating density, $p(\mappingFunctionVector|\inducingVector)$ and the true posterior density, $p(\mappingFunctionVector|\dataVector, \inducingVector)$.}
\slides{* Maximizing lower bound minimizes the KL divergence (information gain):}
  $$
  \KL{p(\mappingFunctionVector|\inducingVector)}{p(\mappingFunctionVector|\dataVector, \inducingVector)} = \int p(\mappingFunctionVector|\inducingVector) \log \frac{p(\mappingFunctionVector|\inducingVector)}{p(\mappingFunctionVector|\dataVector, \inducingVector)}\text{d}\inducingVector
  $$

\slides{* This is minimized when the information stored about $\dataVector$ is stored already in $\inducingVector$.}
\notes{This bound is minimized when the information stored about $\dataVector$ is already stored in $\inducingVector$. In other words, maximizing the bound seeks an *optimal compression* from the *information gain* perspective.}
\slides{* The bound seeks an *optimal compression* from the *information gain* perspective.
* If $\inducingVector = \mappingFunctionVector$ bound is exact ($\mappingFunctionVector$ $d$-separates $\dataVector$ from $\inducingVector$).}

\notes{For the case where $\inducingVector = \mappingFunctionVector$ the bound is exact ($\mappingFunctionVector$ $d$-separates $\dataVector$ from $\inducingVector$).}

\subsection{Choice of Inducing Variables}

\slides{
* Free to choose whatever heuristics for the inducing variables.
* Can quantify which heuristics perform better through checking lower bound.
}
\notes{The quality of the resulting bound is determined by the choice of the inducing variables. You are free to choose whichever heuristics you like for the inducing variables, as long as they are drawn jointly from a valid Gaussian process, i.e. such that}
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
\notes{Choosing the inducing variables amounts to specifying $\Kfu$ and $\Kuu$ such that $\kernelMatrix$ remains positive definite. The typical choice is to choose $\inducingVector$ in the same domain as $\mappingFunctionVector$, associating each inducing output, $\inducingScalar_i$ with a corresponding input location $\inducingInputVector$. However, more imaginative choices are absolutely possible. In particular, if $\inducingVector$ is related to $\mappingFunctionVector$ through a linear operator (see e.g. @Alvarez:efficient10), then valid $\Kuu$ and $\Kuf$ can be constructed. For example we could choose to store the gradient of the function at particular points or a value from the frequency spectrum of the function [@Lazaro:spectrum10].}

\newslide{Variational Compression}
\slides{
* Inducing variables are a compression of the real observations.
* They are like pseudo-data. They can be in space of $\mappingFunctionVector$ or a space that is related through a linear operator [@Alvarez:efficient10] — e.g. a gradient or convolution.
}

\subsection{Variational Compression II}

\slides{
* Resulting algorithms reduce computational complexity.
* Also allow deployment of more standard scaling techniques. 
* E.g. Stochastic variational inference @Hoffman:stochastic12
* Allow for scaling e.g. stochastic variational @Hensman:bigdata13 or parallelization [@Gal:distributed14;@Dai:gpu14;@Seeger:auto17]
}
\notes{Inducing variables don't only allow for the compression of the non-parameteric information into a reduced data set but they also allow for computational scaling of the algorithms through, for example stochastic variational approaches[@Hoffman:stochastic12; @Hensman:bigdata13] or parallelization [@Gal:Distributed14;@Dai:gpu14;@Seeger:auto17].}


\endif
