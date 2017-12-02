<!-- Introduction to GPs -->

\include{../../_ml/includes/what-is-ml.md}

### Artificial Intelligence

* Machine learning is a mainstay because of importance of prediction.

### What is Machine Learning?

* Simple description

    $$\text{data} + \text{model} \rightarrow \text{prediction}$$

* To combine data with a model need:

    * **a prediction function** $\mappingFunction(\cdot)$ includes our beliefs about the regularities of the universe

    * **an objective function** $\errorFunction(\cdot)$ defines the cost of misprediction.


### Uncertainty

* Uncertainty in prediction arises from:

    1. scarcity of training data and 
    2. mismatch between the set of prediction functions we choose and all possible prediction functions.

* Also uncertainties in objective, leave those for another day.

\include{../../_ml/includes/neural-networks.md}
\include{../../_ml/includes/probabilistic-modelling.md}
\include{../../_ml/includes/graphical-models.md}
\include{../../_ml/includes/performing-inference.md}
\include{../../_ml/includes/multivariate-gaussian-properties.md}
\include{../../_gp/includes/non-degenerate-gps.md}
\include{../../_gp/includes/gp-intro-very-short.md}
