### Performing Inference {data-transition="None"}

* Easy to write in probabilities

* But underlying this is a wealth of computational challenges.

* High dimensional integrals typically require approximation.

### Linear Models {data-transition="None"}

* In statistics, focussed more on *linear* model implied by 
    $$
    \mappingFunction(\inputVector) = \left.\mappingVector^{(2)}\right.^\top \activationVector(\mappingMatrix_1, \inputVector)
    $$

* Hold $\mappingMatrix_1$ fixed for given analysis.

* Gaussian prior for $\mappingMatrix$,
    $$
    \mappingVector^{(2)} \sim \gaussianSamp{\zerosVector}{\covarianceMatrix}.
    $$
    $$
    \dataScalar_i = \mappingFunction(\inputVector_i) + \noiseScalar_i,
    $$
    where 
    $$
    \noiseScalar_i \sim \gaussianSamp{0}{\dataStd^2}
    $$
 
### Linear Gaussian Models {data-transition="None"}

* Normally integrals are complex but for this Gaussian linear case they are trivial.

