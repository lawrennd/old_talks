frame start

### Continuous Character Control

\small

\begin{flushright}
\citep{Levine:control12}
\end{flushright}
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

frame end

frame start

### Character Control: Results

\includemedia[
  height=0.8\textheight,width=0.8\textwidth,
  activate=pageopen,
  flashvars={
    modestbranding=1 % no YT logo in control bar
   &autohide=1       % controlbar autohide
   &showinfo=0       % no title and other info before start
  }
]{}{https://youtube.googleapis.com/v/hr3pdDl5IAg?rel=0}

frame end
