\newslide{Recall Univariate Gaussian Properties}
\slides{
. . .

1.  Sum of Gaussian variables is also Gaussian.

$$\dataScalar_i \sim \gaussianSamp{\meanScalar_i}{\dataStd_i^2}$$

. . .

$$\sum_{i=1}^{\numData} \dataScalar_i \sim \gaussianSamp{\sum_{i=1}^\numData \meanScalar_i}{\sum_{i=1}^\numData\dataStd_i^2}$$
}

\newslide{Recall Univariate Gaussian Properties}
\slides{
2.  Scaling a Gaussian leads to a Gaussian. 

. . .

$$\dataScalar \sim \gaussianSamp{\meanScalar}{\dataStd^2}$$

. . .

$$\mappingScalar\dataScalar\sim \gaussianSamp{\mappingScalar\meanScalar}{\mappingScalar^2 \dataStd^2}$$


\newslide{Multivariate Consequence}
\slides{
\alignleft{If}}\notes{If a vector, $\inputVector$, is sampled from a multivariate Gaussian desity,}
$$\inputVector \sim \gaussianSamp{\meanVector}{\covarianceMatrix}$$
\slides{
. . .

\alignleft{And}}\notes{and a second vector, $\dataVector$, is related to the original vector through an affine transformation matrix, $\mappingMatrix,}
$$\dataVector= \mappingMatrix\inputVector$$
\slides{
. . .

\alignleft{Then}}\notes{The $\dataVector$ is also drawn from a multivariate Gaussian density, with a mean that is the affine transformation of the original mean, $\mappingMatrix\meanVector$ and a covariance that is given by applying the affine transformation either side of the original, $\mappingMatrix \covarianceMatrix\mappingMatrix^\top$,}
$$\dataVector \sim \gaussianSamp{\mappingMatrix\meanVector}{\mappingMatrix\covarianceMatrix\mappingMatrix^\top}$$

}
