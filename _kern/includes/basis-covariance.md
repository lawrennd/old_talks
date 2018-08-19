### Basis Function Covariance

\notes{The fixed basis function covariane just comes from the properties of a multivariate Gaussian, if we decide 
$$
\mappingFunctionVector=\basisMatrix\mappingVector
$$
and then we assume
$$
\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha\eye}
$$
then it follows from the properties of a multivariate Gaussian that
$$
\mappingFunctionVector \sim \gaussianSamp{\zerosVector}{\alpha\basisMatrix\basisMatrix^\top}
$$
meaning that the vector of observations from the function is jointly distributed as a Gaussian process and the covariance matrix is $\kernelMatrix = \alpha\basisMatrix \basisMatrix^\top$, each element of the covariance matrix can then be found as the inner product between two rows of the basis funciton matrix.}
$$
\kernel(\inputVector, \inputVector^\prime) = \basisVector(\inputVector)^\top \basisVector(\inputVector^\prime)
$$

\columns{\includesvg{../slides/diagrams/kern/basis_covariance.svg}}{\includeimg{../slides/diagrams/kern/basis_covariance.gif}{40%}{negate}{center}}{45%}{45%}
