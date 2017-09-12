### Selecting Number and Location of Basis

-   Need to choose

    1.  location of centers

    2.  number of basis functions

    Restrict analysis to 1-D input, $\inputScalar$.

-   Consider uniform spacing over a region:

### Uniform Basis Functions

-   Set each center location to
    $$\locationScalar_k = a+\Delta\locationScalar\cdot (k-1).$$

-   Specify the basis functions in terms of their indices,
    $$\begin{aligned}
        \kernelScalar\left(\inputScalar_i,\inputScalar_j\right) = &\alpha^\prime\Delta\locationScalar \sum_{k=1}^{\numBasisFunc} \exp\Bigg(
          -\frac{\inputScalar_i^2 + \inputScalar_j^2}{2
            \rbfWidth^2}\\ 
            & - \frac{2\left(a+\Delta\locationScalar\cdot (k-1)\right)
            \left(\inputScalar_i+\inputScalar_j\right) + 2\left(a+\Delta\locationScalar \cdot (k-1)\right)^2}{2
            \rbfWidth^2} \Bigg).
        \end{aligned}$$

-   Here we’ve scaled variance of process by $\Delta\locationScalar$.

### Infinite Basis Functions

-   Take
    $$\locationScalar_1=a \ \text{and}\  \locationScalar_\numBasisFunc=b \ \text{so}\ b= a+ \Delta\locationScalar\cdot(\numBasisFunc-1)$$

-   This implies $$b-a = \Delta\locationScalar (\numBasisFunc -1)$$ and
    therefore $$\numBasisFunc = \frac{b-a}{\Delta \locationScalar} + 1$$

-   Take limit as $
        \Delta\locationScalar\rightarrow 0$ so
    $\numBasisFunc \rightarrow \infty$ where we have used
    $a + k\cdot\Delta\locationScalar\rightarrow \locationScalar$.

### Result

-   Performing the integration leads to $$\begin{aligned}
        \kernelScalar(\inputScalar_i,&\inputScalar_j) = \alpha^\prime \sqrt{\pi\rbfWidth^2}
        \exp\left( -\frac{\left(\inputScalar_i-\inputScalar_j\right)^2}{4\rbfWidth^2}\right)\\ &\times
        \frac{1}{2}\left[\text{erf}\left(\frac{\left(b - \frac{1}{2}\left(\inputScalar_i +
                  \inputScalar_j\right)\right)}{\rbfWidth} \right)-
          \text{erf}\left(\frac{\left(a - \frac{1}{2}\left(\inputScalar_i +
                  \inputScalar_j\right)\right)}{\rbfWidth} \right)\right],
        \end{aligned}$$

-   Now take limit as $a\rightarrow -\infty$ and $b\rightarrow \infty$
    $$\kernelScalar\left(\inputScalar_i,\inputScalar_j\right) = \alpha\exp\left(
          -\frac{\left(\inputScalar_i-\inputScalar_j\right)^2}{4\rbfWidth^2}\right).$$
    where $\alpha=\alpha^\prime \sqrt{\pi\rbfWidth^2}$.

### Infinite Feature Space

-   An RBF model with infinite basis functions is a Gaussian process.

-   The covariance function is given by the  covariance function.
    $$\kernelScalar\left(\inputScalar_i,\inputScalar_j\right) = \alpha \exp\left(
          -\frac{\left(\inputScalar_i-\inputScalar_j\right)^2}{4\rbfWidth^2}\right).$$

### Infinite Feature Space

-   An RBF model with infinite basis functions is a Gaussian process.

-   The covariance function is the exponentiated quadratic (squared exponential).

-   **Note:** The functional form for the covariance function and basis
    functions are similar.

    -   this is a special case,

    -   in general they are very different


