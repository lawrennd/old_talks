### Overfitting

\notes{One potential problem is that as the number of nodes in two adjacent layers increases, the number of parameters in the affine transformation between layers, $\mappingMatrix$, increases. If there are $k_{i-1}$ nodes in one layer, and $k_i$ nodes in the following, then that matrix contains $k_i k_{i-1}$ parameters, when we have layer widths in the 1000s that leads to millions of parameters.

One proposed solution is known as *dropout* where only a sub-set of the neural network is trained at each iteration.}
\slides{
* Potential problem: if number of nodes in two adjacent layers is big, corresponding $\mappingMatrix$ is also very big and there is the potential to overfit.

* Proposed solution: “dropout”.
}\notes{An alternative solution would be to reparameterize $\mappingMatrix$ with its *singular value decomposition*.}\slides{
* Alternative solution: parameterize $\mappingMatrix$ with its SVD.}
  $$
  \mappingMatrix = \eigenvectorMatrix\eigenvalueMatrix\eigenvectwoMatrix^\top
  $$
  or 
  $$
  \mappingMatrix = \eigenvectorMatrix\eigenvectwoMatrix^\top
  $$
  where if $\mappingMatrix \in \Re^{k_1\times k_2}$ then $\eigenvectorMatrix\in \Re^{k_1\times q}$ and $\eigenvectwoMatrix \in \Re^{k_2\times q}$, i.e. we have a low rank matrix factorization for the weights.

\setupcode{import teaching_plots as plot}
\plotcode{plot.low_rank_approximation(diagrams='../slides/diagrams')}

\newslide{Low Rank Approximation}

\includesvg{../slides/diagrams/wisuvt.svg}
\caption{Pictorial representation of the low rank form of the matrix $\mappingMatrix$}

