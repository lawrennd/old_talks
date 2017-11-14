<!--frame start-->
### Variational Bound on $p(\dataVector |\inducingVector)$

$$\begin{aligned}
    \log p(\dataVector|\inducingVector) & = \log \int p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector|\inducingVector) \text{d}\mappingFunctionVector\\ & = \int q(\mappingFunctionVector) \log \frac{p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector|\inducingVector)}{q(\mappingFunctionVector)}\text{d}\mappingFunctionVector + \KL{q(\mappingFunctionVector)}{p(\mappingFunctionVector|\dataVector, \inducingVector)}
  \end{aligned}$$

\pause \raggedleft{\scriptsize \citep{Titsias:variational09}}

-   Example, set
    $q(\mappingFunctionVector)=p(\mappingFunctionVector|\inducingVector)$,
    $$\log p(\dataVector|\inducingVector) \geq \log \int p(\mappingFunctionVector|\inducingVector) \log p(\dataVector|\mappingFunctionVector)\text{d}\mappingFunctionVector.$$
    $$p(\dataVector|\inducingVector) \geq \exp \int p(\mappingFunctionVector|\inducingVector) \log p(\dataVector|\mappingFunctionVector)\text{d}\mappingFunctionVector.$$

<!--frame end-->
<!--frame start-->
### Optimal Compression in Inducing Variables

-   Maximizing lower bound minimizes the KL divergence (information
    gain):
    $$\KL{p(\mappingFunctionVector|\inducingVector)}{p(\mappingFunctionVector|\dataVector, \inducingVector)} = \int p(\mappingFunctionVector|\inducingVector) \log \frac{p(\mappingFunctionVector|\inducingVector)}{p(\mappingFunctionVector|\dataVector, \inducingVector)}\text{d}\inducingVector$$

-   This is minimized when the information stored about $\dataVector$ is
    stored already in $\inducingVector$.

-   The bound seeks an *optimal compression* from the *information gain*
    perspective.

-   If $\inducingVector = \mappingFunctionVector$ bound is exact
    ($\mappingFunctionVector$ $d$-separates $\dataVector$ from
    $\inducingVector$).

<!--frame end-->
<!--frame start-->
### Choice of Inducing Variables

-   Optimizing the bound directly not always practical.

-   Free to choose whatever heuristics for the inducing variables.

-   Can quantify which heuristics perform better through checking lower
    bound.

<!--frame end-->

