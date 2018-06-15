### Neural Networks and Prediction Functions

\slides{
*  adaptive non-linear function models inspired by simple neuron models [@McCulloch:neuron43]

*  have become popular because of their ability to model data.

* can be composed to form highly complex functions

* start by focussing on one hidden layer
}
\notes{Neural networks are adaptive non-linear function models. Originally, they were studied (by McCulloch and Pitts [@McCulloch:neuron43]) as simple models for neurons, but over the last decade they have become popular because they are a flexible approach to modelling complex data. A particular characteristic of neural network models is that they can be composed to form highly complex functions which encode many of our expectations of the real world. They allow us to encode our assumptions about how the world works.}

\slides{
### Prediction Function of One Hidden Layer

$$
\mappingFunction(\inputVector) = \left.\mappingVector^{(2)}\right.^\top \activationVector(\mappingMatrix_{1}, \inputVector)
$$

$\mappingFunction(\cdot)$ is a scalar function with vector inputs,

$\activationVector(\cdot)$ is a vector function with vector inputs.

* dimensionality of the vector function is known as the number of hidden units, or the number of neurons.

* elements of $\activationVector(\cdot)$ are the *activation* function of the neural network

* elements of $\mappingMatrix_{1}$ are the parameters of the activation functions.
}

\notes{
We will return to composition later, but for the moment, let's focus on a one hidden layer neural network. We are interested in the prediction function, so we'll ignore the objective function (which is often called an error function) for the moment, and just describe the mathematical object of interest

$$
\mappingFunction(\inputVector) = \mappingMatrix^\top \activationVector(\mappingMatrixTwo, \inputVector)
$$

Where in this case $\mappingFunction(\cdot)$ is a scalar function with vector inputs, and $\activationVector(\cdot)$ is a vector function with vector inputs. The dimensionality of the vector function is known as the number of hidden units, or the number of neurons. The elements of this vector function are known as the *activation* function of the neural network and $\mappingMatrixTwo$ are the parameters of the activation functions.

}

### Relations with Classical Statistics

\slides{
* In statistics activation functions are known as *basis functions*.

*  would think of this as a *linear model*: not linear predictions, linear in the parameters

* $\mappingVector_{1}$ are *static* parameters.
}
\notes{In statistics activation functions are traditionally known as *basis functions*. And we would think of this as a *linear model*. It's doesn't make linear predictions, but it's linear because in statistics estimation focuses on the parameters, $\mappingMatrix$, not the parameters, $\mappingMatrixTwo$. The linear model terminology refers to the fact that the model is *linear in the parameters*, but it is *not* linear in the data unless the activation functions are chosen to be linear.}

### Adaptive Basis Functions

\slides{
* In machine learning we optimize $\mappingMatrix_{1}$ as well as  $\mappingMatrix_{2}$ (which would normally be denoted in statistics by $\boldsymbol{\beta}$).

* This tutorial: revisit that decision: follow the path of @Neal:bayesian94 and @MacKay:bayesian92.

* Consider the probabilistic approach.
}
\notes{The first difference in the (early) neural network literature to the classical statistical literature is the decision to optimize these parameters, $\mappingMatrixTwo$, as well as the  parameters, $\mappingMatrix$ (which would normally be denoted in statistics by $\boldsymbol{\beta}$)[^footnote1].

In this tutorial, we're going to go revisit that decision, and follow the path of Radford Neal [@Neal:bayesian94] who, inspired by work of David MacKay [@MacKay:bayesian92] and others did his PhD thesis on Bayesian Neural Networks. If we take a Bayesian approach to parameter inference (note I am using inference here in the classical sense, not in the sense of prediction of test data, which seems to be a newer usage), then we don't wish to fit parameters at all, rather we wish to integrate them away and understand the family of functions that the model describes.

[^footnote1]: In classical statistics we often interpret these parameters, $\beta$, whereas in machine learning we are normally more interested in the result of the prediction, and less in the prediction. Although this is changing with more need for accountability. In honour of this I normally use $\boldsymbol{\beta}$ when I care about the value of these parameters, and $\mappingVector$ when I care more about the quality of the prediction.
}
