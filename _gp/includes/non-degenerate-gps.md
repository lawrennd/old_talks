### Non-degenerate Gaussian Processes

\slides{
* This process is *degenerate*.


+ Covariance function is of rank at most $\numHidden$.


+ As $\numData \rightarrow \infty$, covariance matrix is not full rank.


+ Leading to $\det{\kernelMatrix} = 0$
}\notes{
The process described above is degenerate. The covariance function is of rank at most $\numHidden$ and since the theoretical amount of data could always increase $\numData \rightarrow \infty$, the covariance function is not full rank. 
This means as we increase the amount of data to infinity, there will come a point where we can't normalize the process because the multivariate Gaussian has the form,
$$
\gaussianDist{\mappingFunctionVector}{\zerosVector}{\kernelMatrix} = \frac{1}{\left(2\pi\right)^{\frac{\numData}{2}}\det{\kernelMatrix}^\frac{1}{2}} \exp\left(-\frac{\mappingFunctionVector^\top\kernelMatrix \mappingFunctionVector}{2}\right)
$$
and a non-degenerate kernel matrix leads to $\det{\kernelMatrix} = 0$ defeating the normalization (it's equivalent to finding a projection in the high dimensional Gaussian where the variance of the the resulting univariate Gaussian is zero, i.e. there is a null space on the covariance, or alternatively you can imagine there are one or more directions where the Gaussian has become the delta function).
}

\slides{
### Infinite Networks

* In ML Radford Neal [@Neal:bayesian94] asked "what would happen if you took  $\numHidden \rightarrow \infty$?"
}\notes{In the machine learning field, it was Radford Neal [@Neal:bayesian94] that realized the potential of the next step. In his 1994 thesis, he was considering Bayesian neural networks, of the type we described above, and in considered what would happen if you took the number of hidden nodes, or neurons, to infinity, i.e. $\numHidden \rightarrow \infty$.}

[\includeimg{../slides/diagrams/neal-infinite-priors.png}{80%}](http://www.cs.toronto.edu/~radford/ftp/thesis.pdf)

*Page 37 of Radford Neal's 1994 thesis*

\slides{
### Roughly Speaking

* Instead of
}\notes{In loose terms, what Radford considers is what happens to the elements of the covariance function,}
  $$
  \begin{align*}
  \kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) & = \alpha \activationVector\left(\mappingMatrix_1, \inputVector_i\right)^\top \activationVector\left(\mappingMatrix_1, \inputVector_j\right)\\
  & = \alpha \sum_k \activationScalar\left(\mappingVector^{(1)}_k, \inputVector_i\right) \activationScalar\left(\mappingVector^{(1)}_k, \inputVector_j\right)
  \end{align*}
  $$
\slides{
* Sample infinitely many from a prior density, $p(\mappingVector^{(1)})$,
}\notes{if instead of considering a finite number you sample infinitely many of these activation functions, sampling parameters from a prior density, $p(\mappingVectorTwo)$, for each one,}
$$
\kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) = \alpha \int \activationScalar\left(\mappingVector^{(1)}, \inputVector_i\right) \activationScalar\left(\mappingVector^{(1)}, \inputVector_j\right) p(\mappingVector^{(1)}) \text{d}\mappingVector^{(1)}
$$
\slides{
* Also applies for non-Gaussian $p(\mappingVector^{(1)})$ because of the *central limit theorem*.
}\notes{And that's not *only* for Gaussian $p(\mappingVectorTwo)$. In fact this result holds for a range of activations, and a range of prior densities because of the *central limit theorem*.}

\slides{
### Simple Probabilistic Program

* If
  $$
  \begin{align*} 
  \mappingVector^{(1)} & \sim p(\cdot)\\ \phi_i & = \activationScalar\left(\mappingVector^{(1)}, \inputVector_i\right), 
  \end{align*}
  $$
has finite variance.

* Then taking number of hidden units to infinity, is also a Gaussian process.
}\notes{To write it in the form of a probabilistic program, as long as the distribution for $\phi_i$ implied by this short probabilistic program,
  $$
  \begin{align*}
  \mappingVectorTwo & \sim p(\cdot)\\
  \phi_i & = \activationScalar\left(\mappingVectorTwo, \inputVector_i\right), 
  \end{align*}
  $$
has finite variance, then the result of taking the number of hidden units to infinity, with appropriate scaling, is also a Gaussian process.}

### Further Reading
\slides{
* Chapter 2 of Neal's thesis [@Neal:bayesian94]

* Rest of Neal's thesis. [@Neal:bayesian94]

* David MacKay's PhD thesis [@MacKay:bayesian92] 
}
\notes{To understand this argument in more detail, I highly recommend reading chapter 2 of Neal's thesis, which remains easy to read and clear today. Indeed, for readers interested in Bayesian neural networks, both Raford Neal's and David MacKay's PhD thesis [@MacKay:bayesian92] remain essential reading. Both theses embody a clarity of thought, and an ability to weave together threads from different fields that was the business of machine learning in the 1990s. Radford and David were also pioneers in making their software widely available and publishing material on the web.}

