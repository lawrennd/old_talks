
\slides{
### Empirical Risk Minimization
* If the loss is the *squared loss*}\notes{if $\dataScalar_i$ and $\inputScalar_i$ are independent samples from the true distribution $\mathbb{P}(\dataScalar, \inputScalar)$. Minimizing this sum directly is known as *empirical risk minimization*. The sum of squares error we have been using can be recovered for this case by considering a *squared loss*,}
$$
L(\dataScalar, \inputScalar, \mappingVector) = (\dataScalar-\mappingVector^\top\boldsymbol{\phi}(\inputScalar))^2,
$$
\notes{which gives an empirical risk of the form}\slides{* This recovers the *empirical risk*}
$$
R(\mappingVector) \approx \frac{1}{\numData} \sum_{i=1}^{\numData}
(\dataScalar_i - \mappingVector^\top \boldsymbol{\phi}(\inputScalar_i))^2
$$
\notes{which up to the constant $\frac{1}{\numData}$ is identical to the objective function we have been using so far.}

### Estimating Risk through Validation

\notes{Unfortuantely, minimising the empirial risk only guarantees something about our performance on the training data. If we don't have enough data for the approximation to the risk to be valid, then we can end up performing significantly worse on test data. Fortunately, we can also estimate the risk for test data through estimating the risk for unseen data. The main trick here is to 'hold out' a portion of our data from training and use the models performance on that sub-set of the data as a proxy for the true risk. This data is known as 'validation' data. It contrasts with test data, because its values are known at the model design time. However, in contrast to test date we don't use it to fit our model. This means that it doesn't exhibit the same bias that the empirical risk does when estimating the true risk.}
