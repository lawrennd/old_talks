\ifndef{multivariateGaussianClosure}
\define{multivariateGaussianClosure}

\editme

\subsubsection{The Multivariate Gaussian: Closure Under Marginalization}

\notes{Being closed under marginalization is a remarkable property of our old
friend the multivariate Gaussian distribution (old friends often have
remarkable properties that we often take for granted, I think this is
particularly true for the multivariate Gaussian). In particular, if we
consider a joint distribution across $p(\dataVector, \dataVector^*)$,
then the covariance matrix of the marginal distribution for the subset
of variables, $\dataVector$, is unaffected by the length of
$\dataVector^*$. Taking this to its logical conclusion, if the length of
the data, $\dataVector$, is $\numData=2$. Then that implies that the
covariance between $\dataVector$, as defined by $\kernelMatrix$, is only
a $2\times 2$ matrix, and it can only depend on the indices of the two
data points in $\dataVector$. Since this covariance matrix must remain
the same for any two values *regardless* of the length of $\dataVector$
and $\dataVector^*$ then the value of the elements of this covariance
must depend only on the two indices associated with $\dataVector$.}

\notes{Since the covariance matrix is specified pairwise, this implies that the covariance matrix must be dependent only  on the index
of the two observations $\dataScalar_i$ and $\dataScalar_j$ for which
the covariance is being computed. In general, we can also think of this
index as being infinite: it could be a spatial or temporal location.}
\begin{align*} 
p(\dataVector) = \int p(\dataVector, \dataVector^*)
\text{d}\dataVector^*=
\frac{\exp\left(\begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}^\top\begin{bmatrix}\kernelMatrix &
\kernelMatrix_*\ \kernelMatrix_*^\top &
\kernelMatrix_{**}\end{bmatrix}^{-1} \begin{bmatrix}\dataVector
\dataVector^*\end{bmatrix}\right)}{\int
\exp\left(\begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}^\top\begin{bmatrix}\kernelMatrix &
\kernelMatrix_*\ \kernelMatrix_*^\top &
\kernelMatrix_{**}\end{bmatrix}^{-1} \begin{bmatrix}\dataVector
\dataVector^*\end{bmatrix}\right) \text{d}\dataVector
\text{d}\dataVector^*} = \mathcal{N}(\mathbf{0} |\kernelMatrix),
\end{align*}
\notes{where each $\dataScalar_i$ is now defined across the real line, and the
dimensionality of $\dataVector*$ is irrelevant. Prediction consists of
conditioning the joint density on $\dataVector^*$. So, for any new value
of $\dataVector^*$, given its index we compute
$p(\dataVector^* | \dataVector)$.}

\endif
