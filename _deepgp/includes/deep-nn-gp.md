\include{../../_deepgp/includes/deep-nn.md}

### Mathematically {data-transition="None"}

$$
\begin{align}
    \hiddenVector_{1} &= \basisFunction\left(\mappingMatrix_1 \inputVector\right)\\
    \hiddenVector_{2} &=  \basisFunction\left(\mappingMatrix_2\hiddenVector_{1}\right)\\
    \hiddenVector_{3} &= \basisFunction\left(\mappingMatrix_3 \hiddenVector_{2}\right)\\
    \dataVector &= \mappingVector_4 ^\top\hiddenVector_{3}
\end{align}
$$

### Overfitting {data-transition="None"}

-   Potential problem: if number of nodes in two adjacent layers is big,
    corresponding $\mappingMatrix$ is also very big and there is the
    potential to overfit.

-   Proposed solution: “dropout”.

-   Alternative solution: parameterize $\mappingMatrix$ with its SVD.
    $$\mappingMatrix = \eigenvectorMatrix\eigenvalueMatrix\eigenvectwoMatrix^\top$$
    or $$\mappingMatrix = \eigenvectorMatrix\eigenvectwoMatrix^\top$$
    where if $\mappingMatrix \in \Re^{k_1\times k_2}$ then
    $\eigenvectorMatrix\in \Re^{k_1\times q}$ and
    $\eigenvectwoMatrix \in \Re^{k_2\times q}$, i.e. we have a low rank
    matrix factorization for the weights.

### Low Rank Approximation {data-transition="None"}

<object data="../slides/diagrams/wisuvt.svg" class="svgplot"></object>

\include{../../_deepgp/includes/deep-gp.md}

### Mathematically {data-transition="None"}

$$
\begin{align}
    \latentVector_{1} &= \eigenvectwoMatrix^\top_1 \inputVector\\
    \hiddenVector_{1} &= \basisFunction\left(\eigenvectorMatrix_1 \latentVector_{1}\right)\\
    \latentVector_{2} &= \eigenvectwoMatrix^\top_2 \hiddenVector_{1}\\
    \hiddenVector_{2} &= \basisFunction\left(\eigenvectorMatrix_2 \latentVector_{2}\right)\\
    \latentVector_{3} &= \eigenvectwoMatrix^\top_3 \hiddenVector_{2}\\
    \hiddenVector_{3} &= \basisFunction\left(\eigenvectorMatrix_3 \latentVector_{3}\right)\\
    \dataVector &= \mappingVector_4^\top\hiddenVector_{3}
\end{align}
$$

### A Cascade of Neural Networks {data-transition="None"}

$$\begin{align}
    \latentVector_{1} &= \eigenvectwoMatrix^\top_1 \inputVector\\
    \latentVector_{2} &= \eigenvectwoMatrix^\top_2 \basisFunction\left(\eigenvectorMatrix_1 \latentVector_{1}\right)\\
    \latentVector_{3} &= \eigenvectwoMatrix^\top_3 \basisFunction\left(\eigenvectorMatrix_2 \latentVector_{2}\right)\\
    \dataVector &= \mappingVector_4 ^\top \latentVector_{3}
\end{align}
$$

### Cascade of Gaussian Processes {data-transition="None"}

* Replace each neural network with a Gaussian process
$$
\begin{align}
    \latentVector_{1} &= \mappingFunctionVector_1\left(\inputVector\right)\\
    \latentVector_{2} &= \mappingFunctionVector_2\left(\latentVector_{1}\right)\\
    \latentVector_{3} &= \mappingFunctionVector_3\left(\latentVector_{2}\right)\\
    \dataVector &= \mappingFunctionVector_4\left(\latentVector_{3}\right)
\end{align}
$$

* Equivalent to prior over parameters, take width of each layer to infinity.




