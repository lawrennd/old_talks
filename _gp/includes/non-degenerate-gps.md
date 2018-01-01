### Non-degenerate Gaussian Processes {data-transition="None"}

* This process is *degenerate*.


+ Covariance function is of rank at most $\numHidden$.


+ As $\numData \rightarrow \infty$, covariance matrix is not full rank.


+ Leading to $\det{\kernelMatrix} = 0$

### Infinite Networks {data-transition="None"}

* In ML Radford Neal [@Neal:bayesian94] asked "what would happen if you took  $\numHidden \rightarrow \infty$?"

[\includeimg{./diagrams/neal-infinite-priors.png}{80%}](http://www.cs.toronto.edu/~radford/ftp/thesis.pdf)

*Page 37 of Radford Neal's 1994 thesis*

### Roughly Speaking {data-transition="None"}

* Instead of 
$$\begin{align*}
\kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) & = \alpha \activationVector\left(\mappingMatrix_1, \inputVector_i\right)^\top \activationVector\left(\mappingMatrix_1, \inputVector_j\right)\\
& = \alpha \sum_k \activationScalar\left(\mappingVector^{(1)}_k, \inputVector_i\right) \activationScalar\left(\mappingVector^{(1)}_k, \inputVector_j\right)
\end{align*}$$

* Sample infinitely many from a prior density, $p(\mappingVector^{(1)})$,
$$
\kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) = \alpha \int \activationScalar\left(\mappingVector^{(1)}, \inputVector_i\right) \activationScalar\left(\mappingVector^{(1)}, \inputVector_j\right) p(\mappingVector^{(1)}) \text{d}\mappingVector^{(1)}
$$

* Also applies for non-Gaussian $p(\mappingVector^{(1)})$ because of the *central limit theorem*. 

### Simple Probabilistic Program {data-transition="None"}

* If
$$\begin{align*}
\mappingVector^{(1)} & \sim p(\cdot)\\
\phi_i & = \activationScalar\left(\mappingVector^{(1)}, \inputVector_i\right), 
\end{align*}$$
has finite variance.

* Then taking number of hidden units to infinity, is also a Gaussian process. 

### Further Reading {data-transition="None"}

* Chapter 2 of Neal's thesis

* Rest of Neal's thesis.

* David MacKay's PhD thesis [@MacKay:bayesian92] 

