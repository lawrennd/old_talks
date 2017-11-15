### Non-linear $\mappingFunction(\latentVector)$

-   In linear case equivalence because
    $\mappingFunction(\latentVector) = \mappingVector^\top \latentVector$
    $$p(\mappingScalar_i) \sim \gaussianSamp{\zerosVector}{\alpha_i}$$

-   In non linear case, need to scale columns of $\latentMatrix$ in
    prior for $\mappingFunction(\latentVector)$.

-   This implies scaling columns of $\latentMatrix$ in covariance
    function
    $$\kernelScalar(\latentVector_{i, :}, \latentVector_{j, :}) = \exp\left( - \frac{1}{2}(\latentVector_{:, i} - \latentVector_{:, j})^\top \mathbf{A} (\latentVector_{:, i} - \latentVector_{:, j})\right)$$
    $\mathbf{A}$ is diagonal with elements $\alpha^2_{i}$. Now keep
    prior spherical
    $$p\left(\latentMatrix\right)=\prod_{j=1}^{\latentDim}\gaussianDist{\latentVector_{:,j}}{\zerosVector}{\eye}$$

-   Covariance functions of this type are known as ARD [see
    e.g. @Neal:book96; @MacKay:information03; @Rasmussen:book06].


