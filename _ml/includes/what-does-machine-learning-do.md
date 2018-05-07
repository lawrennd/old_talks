### What does Machine Learning do?
\slides{
* Automation scales by codifying processes and automating them.
* Need:
    * Interconnected components
	* Compatible components
* Early examples:
    * cf Colt 45, Ford Model T
}

\notes{Any process of automation allows us to scale what we do by codifying a process in some way that makes it efficient and repeatable. Machine learning automates by emulating human (or other actions) found in data. Machine learning codifies in the form of a mathematical function that is learnt by a computer. If we can create these mathematical functions in ways in which they can interconnect, then we can also build systems.}

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
