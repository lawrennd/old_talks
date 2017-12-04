<!-- Introduction to GPs -->

\include{../../_ml/includes/what-is-ml.md}

### Artificial Intelligence {data-transition="none"}

* Machine learning is a mainstay because of importance of prediction.

### What is Machine Learning? {data-transition="none"}

$$\text{data} + \text{model} \rightarrow \text{prediction}$$

. . .

* To combine data with a model need:

. . .

* **a prediction function** $\mappingFunction(\cdot)$ includes our beliefs about the regularities of the universe

. . .

* **an objective function** $\errorFunction(\cdot)$ defines the cost of misprediction.


### Uncertainty {data-transition="none"}

* Uncertainty in prediction arises from:

* scarcity of training data and 

* mismatch between the set of prediction functions we choose and all possible prediction functions.

* Also uncertainties in objective, leave those for another day.

\include{../../_ml/includes/neural-networks.md}
\include{../../_ml/includes/probabilistic-modelling.md}
\include{../../_ml/includes/graphical-models.md}
\include{../../_ml/includes/performing-inference.md}

### Multivariate Gaussian Properties {data-transition="none"}

\include{../../_gp/includes/multivariate_gaussian_properties.md}
\include{../../_ml/includes/multivariate-gaussian-properties.md}
\include{../../_gp/includes/non-degenerate-gps.md}
\include{../../_gp/includes/gp-intro-very-short.md}

<!-- ### Two Dimensional Gaussian Distribution -->

<!-- include{../../_ml/includes/two_d_gaussian.md} -->


### Distributions over Functions {data-transition="none"}

\include{../../_gp/includes/gpdistfunc.md}

\include{../../_kern/includes/eq-covariance.md}

\include{../../_gp/includes/olympic-marathon-gp.md}

\include{../../_kern/includes/basis-covariance.md}

\include{../../_kern/includes/brownian-covariance.md}

\include{../../_kern/includes/mlp-covariance.md}

### {data-transition="none"}

<img src="../slides/diagrams/Planck_CMB.png" align="center" style="background:none; border:none; box-shadow:none;">
