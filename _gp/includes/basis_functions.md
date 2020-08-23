### Basis Function Form

*Radial basis functions* commonly have the form
$$
\basisFunction_k\left(\latentVector_i\right) = \exp\left( -\frac{\left\vert \latentVector_i - \locationVector_k\right\vert^2}{2\rbfWidth^2}\right).
$$

* Basis function maps data into a “feature space” in which a linear sum is a non linear function.


### Basis Function Representations

* Represent a function by a linear sum over a basis,
  $$\mappingFunction(\inputVector_{i,:};\mappingVector) = \sum_{k=1}^\numBasisFunc \mappingScalar_k \basisFunction_k(\inputVector_{i,:}),\label{eq:parametricMapping}$$

* Here: $\numBasisFunc$ basis functions and $\basisFunction_k(\cdot)$ is $k$th basis function and     
  $$
  \mappingVector=\left[\mappingScalar_1,\dots,\mappingScalar_\numBasisFunc\right]^\top.
  $$
* For standard linear model: $\basisFunction_k(\inputVector_{i, :}) = \inputScalar_{i, k}$.

### Random Functions

\alignleft{Functions derived using:}
$$
\mappingFunction(\latentScalar) = \sum_{k=1}^\numBasisFunc \mappingScalar_{k}\basisFunction_k(\latentScalar),$$ where elements of $\mappingVector$ are independently sampled from a Gaussian density, $$\mappingScalar_{k} \sim \gaussianSamp{0}{\alpha}.
$$

