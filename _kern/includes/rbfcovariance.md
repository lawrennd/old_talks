### Covariance Functions

#### Where did this covariance matrix come from?

**Exponentiated Quadratic Kernel Function (RBF, Squared Exponential,
Gaussian)**

$$\kernelScalar\left(\inputVals,\inputVals^{\prime}\right)=\alpha\exp\left(-\frac{\ltwoNorm{\inputVals-\inputVals^{\prime}}^{2}}{2\lengthScale^{2}}\right)$$


-   Covariance matrix is built using the *inputs* to the function
    $\inputVals$.

-   For the example above it was based on Euclidean distance.

-   The covariance function is also know as a kernel.

