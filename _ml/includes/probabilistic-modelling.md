### Probabilistic Modelling {data-transition="None"}

* Probabilistically we want,
$$
p(\dataScalar_*|\dataVector, \inputMatrix, \inputVector_*),
$$
 $\dataScalar_*$ is a test output
 $\inputVector_*$ is a test input
 $\inputMatrix$ is a training input matrix
$\dataVector$ is training outputs

### Joint Model of World {data-transition="None"}

$$
p(\dataScalar_*|\dataVector, \inputMatrix, \inputVector_*) = \int p(\dataScalar_*|\inputVector_*, \parameterVector) p(\parameterVector | \dataVector, \inputMatrix) \text{d} \parameterVector
$$

. . .

$\parameterVector$  contains $\mappingMatrix$ and $\mappingMatrixTwo$

$p(\parameterVector | \dataVector, \inputMatrix)$ is posterior density

### Likelihood

$p(\dataScalar|\inputVector, \parameterVector)$ is the *likelihood* of data point

. . .

Normally assume independence:
$$
p(\dataVector|\inputMatrix, \parameterVector) \prod_{i=1}^\numData p(\dataScalar_i|\inputVector_i, \parameterVector),$$

### Likelihood and Prediction Function {data-transition="None"}

$$
p(\dataScalar_i | \mappingFunction(\inputVector_i)) = \frac{1}{\sqrt{2\pi \dataStd^2}} \exp\left(-\frac{\left(\dataScalar_i - \mappingFunction(\inputVector_i)\right)^2}{2\dataStd^2}\right)
$$

### Unsupervised Learning {data-transition="None"}

* Can also consider priors over latents
$$
p(\dataVector_*|\dataVector) = \int p(\dataVector_*|\inputMatrix_*, \parameterVector) p(\parameterVector | \dataVector, \inputMatrix) p(\inputMatrix) p(\inputMatrix_*) \text{d} \parameterVector \text{d} \inputMatrix \text{d}\inputMatrix_*
$$

* This gives *unsupervised learning*.

### Probabilistic Inference {data-transition="None"}

* Data: $\dataVector$

* Model: $p(\dataVector, \dataVector^*)$

* Prediction: $p(\dataVector^*| \dataVector)$
