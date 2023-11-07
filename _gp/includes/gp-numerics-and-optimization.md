\ifndef{gpNumericsAndOptimization}
\define{gpNumericsAndOptimization}

\editme

\subsection{Improving the Numerics}

In practice we shouldn't be using matrix inverse directly to solve the GP system. One more stable way is to compute the *Cholesky decomposition* of the kernel matrix. The log determinant of the covariance can also be derived from the Cholesky decomposition.

\loadcode{update_inverse}{mlai}

\code{GP.update_inverse = update_inverse}

\subsection{Capacity Control}

\notes{Gaussian processes are sometimes seen as part of a wider family of methods known as kernel methods. Kernel methods are also based around covariance functions, but in the field they are known as Mercer kernels. Mercer kernels have interpretations as inner products in potentially infinite dimensional Hilbert spaces. This interpretation arises because, if we take $\alpha=1$, then the kernel can be expressed as
$$
\kernelMatrix = \basisMatrix\basisMatrix^\top 
$$
which imples the elements of the kernel are given by,
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \basisVector(\inputVector)^\top \basisVector(\inputVector^\prime).
$$
So we see that the kernel function is developed from an inner product between the basis functions. Mercer's theorem tells us that any valid *positive definite function* can be expressed as this inner product but with the caveat that the inner product could be *infinite length*. This idea has been used quite widely to *kernelize* algorithms that depend on inner products. The kernel functions are equivalent to covariance functions and they are parameterized accordingly.  In the kernel modeling community it is generally accepted that kernel parameter estimation is a difficult problem and the normal solution is to cross validate to obtain parameters. This can cause difficulties when a large number of kernel parameters need to be estimated. In Gaussian process modelling kernel parameter estimation (in the simplest case proceeds) by maximum likelihood. This involves taking gradients of the likelihood with respect to the parameters of the covariance function.}


\subsection{Gradients of the Likelihood}

\notes{The easiest conceptual way to obtain the gradients is a two step process. The first step involves taking the gradient of the likelihood with respect to the covariance function, the second step involves considering the gradient of the covariance function with respect to its parameters.}

\subsection{Overall Process Scale}

\notes{In general we won't be able to find parameters of the covariance function through fixed point equations, we will need to do gradient based optimization.}

\subsection{Capacity Control and Data Fit}

\notes{The objective function can be decomposed into two terms, a capacity control term, and a data fit term. The capacity control term is the log determinant of the covariance. The data fit term is the matrix inner product between the data and the inverse covariance.}

\endif