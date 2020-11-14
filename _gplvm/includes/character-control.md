\ifndef{characterControl}
\define{characterControl}

\editme

\subsection{Example: Continuous Character Control}


\alignright{@Levine:control12}
-   Graph diffusion prior for enforcing connectivity between motions.
    $$\log p(\inputMatrix) = w_c \sum_{i,j} \log K_{ij}^d$$ with the
    graph diffusion kernel $\kernelMatrix^d$ obtain from
    $$K_{ij}^d = \exp(\beta \mathbf{H})
    \qquad \text{with} \qquad \mathbf{H} = -\mathbf{T}^{-1/2} \mathbf{L} \mathbf{T}^{-1/2}$$
    the graph Laplacian, and $\mathbf{T}$ is a diagonal matrix with
    $T_{ii} = \sum_j w(\inputVector_i, \inputVector_j)$,
    $$L_{ij} = \begin{cases} \sum_k w(\inputVector_i,\inputVector_k) & \text{if $i=j$}
    \\
    -w(\inputVector_i,\inputVector_j) &\text{otherwise.}
    \end{cases}$$ and
    $w(\inputVector_i,\inputVector_j) = || \inputVector_i -  \inputVector_j||^{-p}$
    measures similarity.

\subsection{Character Control: Results}

\figure{\includeyoutube{hr3pdDl5IAg}{600}{450}}{Character control in the latent space described the the GP-LVM @Levine:control12}{charcter-control-gplvm}

\endif
