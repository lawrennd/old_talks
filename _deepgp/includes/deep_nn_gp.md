\include{../../_deepgp/includes/deep_nn.md}

### Mathematically

\begin{aligned}
    \hiddenVector_{1} &= \basisFunction\left(\weightMatrix_1 \inputVector\right)\\
    \hiddenVector_{2} &=  \basisFunction\left(\weightMatrix_2\hiddenVector_{1}\right)\\
    \hiddenVector_{3} &= \basisFunction\left(\weightMatrix_3 \hiddenVector_{2}\right)\\
    \dataVector &= \weightVector_4 ^\top\hiddenVector_{3}
\end{aligned}

### Overfitting

-   Potential problem: if number of nodes in two adjacent layers is big,
    corresponding $\weightMatrix$ is also very big and there is the
    potential to overfit.

-   Proposed solution: “dropout”.

-   Alternative solution: parameterize $\weightMatrix$ with its SVD.
    $$\weightMatrix = \eigenvectorMatrix\eigenvalueMatrix\eigenvectwoMatrix^\top$$
    or $$\weightMatrix = \eigenvectorMatrix\eigenvectwoMatrix^\top$$
    where if $\weightMatrix \in \Re^{k_1\times k_2}$ then
    $\eigenvectorMatrix\in \Re^{k_1\times q}$ and
    $\eigenvectwoMatrix \in \Re^{k_2\times q}$, i.e. we have a low rank
    matrix factorization for the weights.

\include{../../_deepgp/includes/deep_gp.md}

### Mathematically {#mathematically}

\begin{aligned}
    \latentVector_{1} &= \eigenvectwoMatrix^\top_1 \inputVector\\
    \hiddenVector_{1} &= \basisFunction\left(\eigenvectorMatrix_1 \latentVector_{1}\right)\\
    \latentVector_{2} &= \eigenvectwoMatrix^\top_2 \hiddenVector_{1}\\
    \hiddenVector_{2} &= \basisFunction\left(\eigenvectorMatrix_2 \latentVector_{2}\right)\\
    \latentVector_{3} &= \eigenvectwoMatrix^\top_3 \hiddenVector_{2}\\
    \hiddenVector_{3} &= \basisFunction\left(\eigenvectorMatrix_3 \latentVector_{3}\right)\\
    \dataVector &= \weightVector_4^\top\hiddenVector_{3}
\end{aligned}

### A Cascade of Neural Networks

\begin{aligned}
    \latentVector_{1} &= \eigenvectwoMatrix^\top_1 \inputVector\\
    \latentVector_{2} &= \eigenvectwoMatrix^\top_2 \basisFunction\left(\eigenvectorMatrix_1 \latentVector_{1}\right)\\
    \latentVector_{3} &= \eigenvectwoMatrix^\top_3 \basisFunction\left(\eigenvectorMatrix_2 \latentVector_{2}\right)\\
    \dataVector &= \weightVector_4 ^\top \latentVector_{3}
\end{aligned}

### Replace Each Neural Network with a Gaussian Process

\begin{align}
    \latentVector_{1} &= \mathbf{f}\left(\inputVector\right)\\
    \latentVector_{2} &= \mathbf{f}\left(\latentVector_{1}\right)\\
    \latentVector_{3} &= \mathbf{f}\left(\latentVector_{2}\right)\\
    \dataVector &= \mathbf{f}\left(\latentVector_{3}\right)
\end{align}

This is equivalent to Gaussian prior over weights and integrating out
all parameters and taking width of each layer to infinity.


