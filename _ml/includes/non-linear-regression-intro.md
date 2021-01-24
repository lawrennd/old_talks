\ifndef{nonLinearRegressionIntro}
\define{nonLinearRegressionIntro}

\editme

\subsection{Nonlinear Regression}

\notes{We've now seen how we may perform linear regression. Now, we
are going to consider how we can perform *non-linear*
regression. However, before we get into the details of how to do that
we first need to consider in what ways the regression can be
non-linear. Multivariate linear regression allows us to build models
that take many features into account when making our prediction. In
this session we are going to introduce *basis functions*. The term
seems complicted, but they are actually based on rather a simple
idea. If we are doing a multivariate linear regression, we get extra
features that *might* help us predict our required response varible
(or target value), $\dataScalar$. But what if we only have one input value? We
can actually artificially generate more input values with basis
functions.}

\slides{* Problem with Linear Regression—$\inputVector$ may not be linearly related to $\dataVector$.
* Potential solution: create a feature space: define $\basisFunc(\inputVector)$ where $\basisFunc(\cdot)$ is a nonlinear function of $\inputVector$.
* Model for target is a linear combination of these nonlinear functions 
  $$\mappingFunction(\inputVector) = \sum_{j=1}^\numBasisFunc \mappingScalar_j \basisFunc_j(\inputVector)$$}

\subsection{Non-linear in the Inputs}

\notes{When we refer to non-linear regression, we are normally
referring to whether the regression is non-linear in the input space,
or non-linear in the *covariates*. The covariates are the observations
that move with the target (or *response*) variable. In our notation we
have been using $\inputVector_i$ to represent a vector of the
covariates associated with the $i$th observation. The coresponding
response variable is $\dataScalar_i$. If a model is non-linear in the
inputs, it means that there is a non-linear function between the
inputs and the response variable. Linear functions are functions that
only involve multiplication and addition, in other words they can be
represented through *linear algebra*. Linear regression involves
assuming that a function takes the form}
$$
\mappingFunction(\inputVector) = \mappingVector^\top \inputVector
$$
\notes{where $\mappingVector$ are our regression weights. A very easy way to make the linear regression non-linear is to introduce non-linear functions. When we are introducing non-linear regression these functions are known as *basis functions*.}

\endif
