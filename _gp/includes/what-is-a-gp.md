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

<!-- ### Two Dimensional Gaussian Distribution -->

<!-- include{../../_ml/includes/two_d_gaussian.md} -->

### Multivariate Gaussian Properties

\include{../../_gp/includes/multivariate_gaussian_properties.md}

### Distributions over Functions

\include{../../_gp/includes/gpdistfunc.md}

# Exponentiated Quadratic Covariance

$$k(\mathbf{x}, \mathbf{x}^\prime) 
= \alpha \exp\left(-\frac{\left\Vert \mathbf{x} - \mathbf{x}^\prime\right\Vert^2_2}{2\ell^2}\right)$$

<table>
  <tr><td><object class="svgplot" data="../slides/diagrams/eq_covariance.svg"></object></td>
  <td><img src="../slides/diagrams/eq_covariance.gif" align="center" style="background:none; border:none; box-shadow:none;"></td></tr>
</table>


\include{../../_gp/includes/olympic-marathon-gp.md}

###

<img src="../slides/diagrams/Planck_CMB.png" align="center" style="background:none; border:none; box-shadow:none;">
