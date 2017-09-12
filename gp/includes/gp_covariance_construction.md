### Covariance between Two Points

-   The prior covariance between two points $\inputVector_i$ and
    $\inputVector_j$ is
    $$\kernelScalar\left(\inputVector_i,\inputVector_j\right)=\alpha \basisFunction_:\left(\inputVector_i\right)^\top\basisFunction_:\left(\inputVector_j\right), \label{eq:degenerateCovariance}$$
    or in sum notation
    $$\kernelScalar\left(\inputVector_i,\inputVector_j\right) = \alpha \sum_{k=1}^{\numBasisFunc} \basisFunction_k\left(\inputVector_i\right) \basisFunction_k\left(\inputVector_j\right)$$

-   For the radial basis used this gives
    $$\kernelScalar\left(\inputVector_i,\inputVector_j\right) = \alpha
        \sum_{k=1}^{\numBasisFunc} \exp\left( -\frac{\left\vert \inputVector_i -
              \locationVector_k\right\vert^2 + \left\vert \inputVector_j -
              \locationVector_k\right\vert^2}{2 \rbfWidth^2} \right).$$


