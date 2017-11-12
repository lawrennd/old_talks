<!-- Introduction to GPs -->

\include{../../_ml/includes/what-is-ml.md}

### Model

* Mathematical Abstraction of Problem

* Two functions

    Prediction function $\mappingFunction(\cdot)$

	Objective function $\objectiveFunction(\cdot)$

### Probabilistic Inference

Data: $\dataVector$

Model: $p(\dataVector, \dataVector^*)$

Prediction: $p(\dataVector^*| \dataVector)$

### Gaussian Process

* Probabilistic model for functions

    $p(\mappingVector)$

* Relate to data through a likelihood

    $p(\dataVector | \mappingVector)$


\include{../../_gp/includes/gp-intro-very-short.md}
