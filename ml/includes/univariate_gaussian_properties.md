### Two Important Gaussian Properties

### Sum of Gaussians

. . .

<div align="left">Sum of Gaussian variables is also Gaussian.</div>

$$\dataScalar_i \sim \gaussianSamp{\meanScalar_i}{\sigma_i^2}$$

. . .

<div align="left">And the sum is distributed as</div>

$$\sum_{i=1}^{\numData} \dataScalar_i \sim \gaussianSamp{\sum_{i=1}^\numData \meanScalar_i}{\sum_{i=1}^\numData \sigma_i^2}$$

. . .
	
<small>(*Aside*: As sum increases, sum of non-Gaussian, finite
variance variables is also Gaussian because of [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem).)</small>


### Scaling a Gaussian

. . .

<div align="left">Scaling a Gaussian leads to a Gaussian.</div>

. . .

$$\dataScalar \sim \gaussianSamp{\meanScalar}{\sigma^2}$$

. . .

<div align="left">And the scaled density is distributed as</div>

$$ \mappingScalar \dataScalar \sim \gaussianSamp{\mappingScalar\meanScalar}{\mappingScalar^2 \sigma^2}$$

