\subsection{Basis Function Covariance}

\notes{The fixed basis function covariance just comes from the properties of a multivariate Gaussian, if we decide 
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

\define{\formula}{\kernel(\inputVector, \inputVector^\prime) = \basisVector(\inputVector)^\top \basisVector(\inputVector^\prime)}

\loadcode{basis_cov}{mlai}
\loadcode{radial}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{
basis = mlai.Basis(function=radial, 
                   number=3,
	               data_limits=[-0.5, 0.5], 
                   width=0.125)
kernel = mlai.Kernel(function=basis_cov,
                     name='Basis',
                     shortname='basis',					 
                     formula='\formula',
					 basis=basis)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/kern/')}


\includecovariance{basis}{\formula}
\notes{\caption{A covariance function based on a non-linear basis given by $\basisVector(\inputVector)$.}
