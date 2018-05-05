
### What does Machine Learning do?

* Automation scales by codifying processes and automating them.
* Need:
    * Interconnected components
	* Compatible components
* Early examples:
    * cf Colt 45, Ford Model T


### Codify Through Mathematical Functions

* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
$$ \text{odds} = \frac{\text{bought}}{\text{not bought}} $$
$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}$$


### Codify Through Mathematical Functions

* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
$$ p(\text{bought}) =  \mappingFunction\left(\beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}\right)$$


### Codify Through Mathematical Functions

* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
$$ p(\text{bought}) =  \mappingFunction\left(\boldsymbol{\beta}^\top \inputVector\right)$$

. . .

We call $\mappingFunction(\cdot)$ the *prediction function*

### Fit to Data

* Use an objective function
$$\errorFunction(\boldsymbol{\beta}, \dataMatrix, \inputMatrix)$$

. . .

* E.g. least squares
$$\errorFunction(\boldsymbol{\beta}) = \sum_{i=1}^\numData \left(\dataScalar_i - \mappingFunction(\inputVector_i)\right)^2$$

### Two Components

* Prediction function, $\mappingFunction(\cdot)$
* Objective function, $\errorFunction(\cdot)$
