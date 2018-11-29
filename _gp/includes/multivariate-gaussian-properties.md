\slides{
### Recall Univariate Gaussian Properties

. . .

1.  Sum of Gaussian variables is also Gaussian.

$$\dataScalar_i \sim \gaussianSamp{\mu_i}{\dataStd_i^2}$$

. . .

$$\sum_{i=1}^{\numData} \dataScalar_i \sim \gaussianSamp{\sum_{i=1}^\numData \mu_i}{\sum_{i=1}^\numData\dataStd_i^2}$$

. . .

2.  Scaling a Gaussian leads to a Gaussian. 

. . .

$$\dataScalar \sim \gaussianSamp{\mu}{\dataStd^2}$$

. . .

$$\mappingScalar\dataScalar\sim \gaussianSamp{\mappingScalar\mu}{\mappingScalar^2 \dataStd^2}$$


### Multivariate Consequence

\alignleft{If}

$$\inputVector \sim \gaussianSamp{\boldsymbol{\mu}}{\boldsymbol{\Sigma}}$$

. . .

\alignleft{And}
$$\dataVector= \mappingMatrix\inputVector$$

. . .

\alignleft{Then}
$$\dataVector \sim \gaussianSamp{\mappingMatrix\boldsymbol{\mu}}{\mappingMatrix\boldsymbol{\Sigma}\mappingMatrix^\top}$$

}
