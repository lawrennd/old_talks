frame start

### Notation

$\latentDim$— dimension of latent/embedded space\
$\dataDim$— dimension of data space\
$\numData$— number of data points

centred data,
$\dataMatrix=\left[\dataVector_{1,:},\dots,\dataVector_{\numData,:}\right]^{\top}=\left[\dataVector_{:,1},\dots,\dataVector_{:,\dataDim}\right]\in\Re^{\numData\times \dataDim}$\
latent variables,
$\latentMatrix=\left[\latentVector_{1,:},\dots,\latentVector_{\numData,:}\right]^{\top}=\left[\latentVector_{:,1},\dots,\latentVector_{:,\latentDim}\right]\in\Re^{\numData\times \latentDim}$\
mapping matrix, $\mappingMatrix\in\Re^{\dataDim\times \latentDim}$

$\mathbf{a}_{i,:}$ is a vector from the $i$th row of a given matrix
$\mathbf{A}$\
$\mathbf{a}_{:,j}$ is a vector from the $j$th row of a given matrix
$\mathbf{A}$

frame end

frame start

### Reading Notation

**$\latentMatrix$ and $\dataMatrix$ are *design matrices***

-   Covariance given by $\numData^{-1}\dataMatrix^{\top}\dataMatrix$.

-   Inner product matrix given by $\dataMatrix\dataMatrix^{\top}$.

frame end
