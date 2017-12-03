### Neural Networks and Prediction Functions

*  adaptive non-linear function models inspired by simple neuron models [@McCulloch:neuron43]

*  have become popular because of their ability to model data.

* can be composed to form highly complex functions

* start by focussing on one hidden layer

### Prediction Function of One Hidden Layer

$$
\mappingFunction(\inputVector) = \mappingMatrix^\top \activationVector(\mappingMatrixTwo, \inputVector)
$$

$\mappingFunction(\cdot)$ is a scalar function with vector inputs,

$\activationVector(\cdot)$ is a vector function with vector inputs.

* dimensionality of the vector function is known as the number of hidden units, or the number of neurons.

* elements of $\activationVector(\cdot)$ are the *activation* function of the neural network

* elements of $\mappingMatrixTwo$ are the parameters of the activation functions.

### Relations with Classical Statistics

* In statistics activation functions are known as *basis functions*.

*  would think of this as a *linear model*: not linear predictions, linear in the parameters

* $\mappingMatrixTwo$ are *static* parameters.


### Adaptive Basis Functions

* In machine learning we optimize $\mappingMatrixTwo$ as well as  $\mappingMatrix$ (which would normally be denoted in statistics by $\boldsymbol{\beta}$).

* This tutorial: revisit that decision: follow the path of Radford Neal [@Neal:bayesian94] and David MacKay [@MacKay:bayesian92].

* Consider the probabilistic approach.
