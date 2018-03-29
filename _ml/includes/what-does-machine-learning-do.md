
### What does Machine Learning do? {.slide: data-transition="none"}

* We scale by codifying processes and automating them.

    * Ensure components are compatible (Whitworth threads)

    * Then interconnect them as efficiently as possible.

    * cf Colt 45, Ford Model T


### Codify Through Mathematical Functions {.slide: data-transition="none"}

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ \text{odds} = \frac{\text{bought}}{\text{not bought}} $$

$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}$$


### Codify Through Mathematical Functions {.slide: data-transition="none"}

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ p(\text{bought}) =  \mappingFunction\left(\beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}\right)$$


### Codify Through Mathematical Functions {.slide: data-transition="none"}

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ p(\text{bought}) =  \mappingFunction\left(\boldsymbol{\beta}^\top \inputVector\right)$$

. . .

We call $\mappingFunction(\cdot)$ the *prediction function*

### Fit to Data {.slide: data-transition="none"}

* Use an objective function

$$\errorFunction(\boldsymbol{\beta}, \dataMatrix, \inputMatrix)$$

. . .

* E.g. least squares

$$\errorFunction(\boldsymbol{\beta}) = \sum_{i=1}^\numdata \left(\dataScalar_i - \mappingFunction(\inputVector_i)\right)^2$$

### Two Components {.slide: data-transition="none"}

* Prediction function, $\mappingFunction(\cdot)$

* Objective function, $\errorFunction(\cdot)$
