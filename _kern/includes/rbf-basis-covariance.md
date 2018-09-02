\newslide{Covariance Functions}
\slides{**RBF Basis Functions**}
\notes{Any linear basis function can also be incorporated into a covariance function. For example, an RBF network is a type of neural network with a set of radial basis functions. Meaning, the basis funciton is radially symmetric. These basis functions take the form,}
$$
\basisFunction_k(\inputScalar) = \exp\left(-\frac{\ltwoNorm{\inputScalar-\meanScalar_k}^{2}}{\lengthScale^{2}}\right).
$$
\notes{Given a set of parameters,}
$$
\meanVector = \begin{bmatrix} -1 \\ 0 \\ 1\end{bmatrix},
$$
\notes{we can construct the corresponding covariance function, which has the form,}
$$
\kernelScalar\left(\inputVals,\inputVals^{\prime}\right)=\alpha\basisVector(\inputVals)^\top \basisVector(\inputVals^\prime).
$$

\include{_kern/includes/basis-covariance.md}
