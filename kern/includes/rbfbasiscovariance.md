
### Covariance Functions

**RBF Basis Functions**

$$\kernelScalar\left(\inputVals,\inputVals^{\prime}\right)=\alpha\basisVector(\inputVals)^\top \basisVector(\inputVals^\prime)$$

$$\basisFunction_k(\inputScalar) = \exp\left(-\frac{\ltwoNorm{\inputScalar-\meanScalar_k}^{2}}{\lengthScale^{2}}\right)$$
$$\meanVector = \begin{bmatrix} -1 \\ 0 \\ 1\end{bmatrix}$$

\include{../../kern/includes/basis_covariance.md}
