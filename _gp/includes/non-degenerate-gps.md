### Non-degenerate Gaussian Processes {data-transition="None"}

* This process is *degenerate*.


+ Covariance function is of rank at most $\numHidden$.


+ As $\numData \rightarrow \infty$, covariance matrix is not full rank.


+ Leading to $\det{\kernelMatrix} = 0$

### Infinite Networks {data-transition="None"}

* In ML Radford Neal [@Neal:bayesian94] asked "what would happen if you took  $\numHidden \rightarrow \infty$?"

[<img src="./diagrams/neal-infinite-priors.png" width="80%" class="negate"  style="background:none; border:none; box-shadow:none;" align="center">](http://www.cs.toronto.edu/~radford/ftp/thesis.pdf)

*Page 37 of Radford Neal's 1994 thesis*

### Roughly Speaking {data-transition="None"}

* Instead of 
$$\begin{align*}
\kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) & = \alpha \activationVector\left(\mappingMatrixTwo, \inputVector_i\right)^\top \activationVector\left(\mappingMatrixTwo, \inputVector_j\right)\\
& = \sum_k \activationScalar\left(\mappingVectorTwo_k, \inputVector_i\right) \activationScalar\left(\mappingVectorTwo_k, \inputVector_j\right)
\end{align*}$$

* Sample infinitely many from a prior density, $p(\mappingVectorTwo)$,
$$
\kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) = \int \activationScalar\left(\mappingVectorTwo, \inputVector_i\right) \activationScalar\left(\mappingVectorTwo, \inputVector_j\right) p(\mappingVectorTwo) \text{d}\mappingVectorTwo
$$

* Also applies for non-Gaussian $p(\mappingVectorTwo)$ because of the *central limit theorem*. 

### Simple Probabilistic Program {data-transition="None"}

* If
$$\begin{align*}
\mappingVectorTwo & \sim p(\cdot)\\
\phi_i & = \activationScalar\left(\mappingVectorTwo, \inputVector_i\right), 
\end{align*}$$
has finite variance.

* Then taking number of hidden units to infinity, is also a Gaussian process. 

### Further Reading

* Chapter 2 of Neal's thesis

* Rest of Neal's thesis.

* David MacKay's PhD thesis [@MacKay:bayesian92] 

