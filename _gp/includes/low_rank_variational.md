<!--frame start-->
###  Variational marginalisation of $\mappingFunctionVector$

$$\log p(\dataVector\given\inducingVector) = \log\int p(\dataVector \given\mappingFunctionVector)p(\mappingFunctionVector\given\inducingVector,\inputMatrix)\text{d}\mappingFunctionVector$$

\pause

$$\log p(\dataVector\given\inducingVector) = \log \mathbb{E}_{p(\mappingFunctionVector\given \inducingVector,\inputMatrix)}\left[p(\dataVector \given\mappingFunctionVector)\right]$$
\pause
$$\log p(\dataVector\given\inducingVector) \geq  \mathbb{E}_{p(\mappingFunctionVector\given \inducingVector,\inputMatrix)}\left[\log p(\dataVector \given\mappingFunctionVector)\right]\triangleq \log\widetilde p(\dataVector\given \inducingVector)$$
\pause

[\color{MyDarkBlue} No inversion of $\Kff$ required]{}

<!--frame end-->
<!--frame start-->
### Variational marginalisation of $\mappingFunctionVector$ (another way)

\alignright{@Titsias:variational09}
$$p(\dataVector\given\inducingVector) = \frac{p(\dataVector \given\mappingFunctionVector)p(\mappingFunctionVector\given\inducingVector)}{p(\mappingFunctionVector\given\dataVector, \inducingVector)}$$
\pause
$$\log p(\dataVector\given\inducingVector) = \log p(\dataVector \given\mappingFunctionVector) + \log \frac{p(\mappingFunctionVector\given\inducingVector)}{p(\mappingFunctionVector\given\dataVector, \inducingVector)}$$
\pause
$$\log p(\dataVector\given\inducingVector) = \bbE_{p(\mappingFunctionVector\given\inducingVector)}\big[\log p(\dataVector \given\mappingFunctionVector)\big] + \bbE_{p(\mappingFunctionVector\given\inducingVector)}\big[\log \frac{p(\mappingFunctionVector\given\inducingVector)}{p(\mappingFunctionVector\given\dataVector, \inducingVector)}\big]$$
\pause
$$\log p(\dataVector\given\inducingVector) = \widetilde p(\dataVector\given\inducingVector) + \textsc{KL}[p(\mappingFunctionVector|\inducingVector)||p(\mappingFunctionVector\given\dataVector, \inducingVector)]$$

[\color{MyDarkBlue} No inversion of $\Kff$ required]{}

<!--frame end-->
<!--frame start-->
### A Lower Bound on the Likelihood

$$\widetilde p(\dataVector\given\inducingVector)  = \prod_{i=1}^\numData \widetilde p(\dataScalar_i\given\inducingVector)$$
$$\widetilde p(\dataScalar\given\inducingVector) = \gaussianDist{\dataScalar}{\kfu\Kuu^{-1}\inducingVector}{\dataStd^2} \,{\color{red}\exp\left\{-\tfrac{1}{2\dataStd^2}\left(\kff- \kfu\Kuu^{-1}\kuf\right)\right\}}$$

[A straightforward likelihood approximation, and a penalty term]{}

<!--frame end-->
<!--frame start-->
### Now we can marginalise $\inducingVector$

$$\widetilde p(\inducingVector\given\dataVector,\inducingInputMatrix) = \frac{\widetilde p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)}{\int \widetilde p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)\dif{\inducingVector}}$$

-   Computing the posterior costs $\bigO(\numData\numInducing^2)$

-   We also get a lower bound of the marginal likelihood

<!--frame end-->
<!--frame start-->
### What does the penalty term do?

$${\color{red}\sum_{i=1}^\numData-\tfrac{1}{2\dataStd^2}\left(\kff- \kfu\Kuu^{-1}\kuf\right)}$$

\begin{block}{It doesn't affect the posterior}
    \begin{multicols}{2}
      It appears on the top and bottom of Bayes' rule \columnbreak
      $$
      \widetilde p(\inducingVector\given\dataVector,\inducingInputMatrix) = \frac{\widetilde p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)}{\int \widetilde p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)\dif{\inducingVector}}
      $$
    \end{multicols}
  \end{block}
<!--frame end-->
<!--frame start-->
### What does the penalty term do? {#what-does-the-penalty-term-do}

$${\color{red}\sum_{i=1}^\numData-\tfrac{1}{2\dataStd^2}\left(\kff - \kfu\Kuu^{-1}\kuf\right)}$$

\begin{block}{It affects the marginal likelihood}
    $$
    \widetilde p(\dataVector\given\inducingInputMatrix) = \int \widetilde p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)\dif{\inducingVector}
    $$
  \end{block}
<!--frame end-->
<!--frame start-->
### What does the penalty term do? {#what-does-the-penalty-term-do}

![image](../../../gp/tex/diagrams/cov_approx){width="60.00000%"}

![image](../../../gp/tex/diagrams/cov_approx_opt){width="60.00000%"}

<!--frame end-->
<!--frame start-->
### How good is the inducing approximation?

[It’s easy to show that as $\inducingInputMatrix \to \inputMatrix$:]{}

-   $\inducingVector \to \mappingFunctionVector$ (and the posterior is
    exact)

-   The penalty term is zero.

-   The cost returns to $\bigO(\numData^3)$

\pause

-   \alert{We're okay if we have sufficient coverage with $\mathbf{Z}$}\

-   \alert{We can optimize $\mathbf{Z}$ along with the hyperparameters}

<!--frame end-->
<!--frame start-->
### Predictions

\begin{block}{In a `full' GP, we did}
    \[
    p(\mappingFunction_\star\given\dataVector) = \int p(\mappingFunction_\star\given \mappingFunctionVector)p(\mappingFunctionVector\given \dataVector)\text{d} \mappingFunctionVector
    \]
  \end{block}
\begin{block}{In a induced GP, we do}
    \[
    p(\mappingFunction_\star\given\dataVector) = \int p(\mappingFunction_\star\given \inducingVector)\widetilde p(\inducingVector\given \dataVector)\text{d} \inducingVector
    \]
  \end{block}
<!--frame end-->
<!--frame start-->
### Recap

[\color{MyDarkBlue}So far we:]{}

-   introduced $\inducingInputMatrix, \inducingVector$

-   approximated the intergral over $\mappingFunctionVector$
    variationally

-   captured the information in
    $\widetilde p(\inducingVector\given \dataVector)$

-   obtained a lower bound on the marginal likeihood

-   saw the effect of the penalty term

-   prediction for new points

[\color{MyDarkBlue}Omitted details:]{}

-   optimization of the covariance parameters using the bound

-   optimization of Z (simultaneously)

-   the form of $\widetilde p(\inducingVector\given \dataVector)$

-   historical approximations

<!--frame end-->
<!--frame start-->
### Other approximations

[Subset selection]{} \alignright{@Lawrence:ivm02}

-   Random or systematic

-   Set $\inducingInputMatrix$ to subset of $\inputMatrix$

-   Set $\inducingVector$ to subset of $\mappingFunctionVector$

-   Approximation to $p(\dataVector\given \inducingVector)$:

    -   $ p(\dataVector_i\given \inducingVector) = p(\dataVector_i\given\mappingFunctionVector_i) \qquad i\in \text {selection}$

    -   $ p(\dataVector_i\given \inducingVector) = 1  \qquad
              \qquad i\notin \text {selection}$

<!--frame end-->
<!--frame start-->
### Other approximations {#other-approximations}

\alignright{@Quinonero:unifying05}
  {Deterministic Training Conditional (DTC)}

-   Approximation to $p(\dataVector\given \inducingVector)$:

    -   $ \widetilde p(\dataVector_i\given \inducingVector) = \delta(\dataVector_i, \mathbb{E}[\mappingFunctionVector_i\given\inducingVector])$

-   As our variational formulation, but without penalty

Optimization of $\inducingInputMatrix$ is difficult

<!--frame end-->
<!--frame start-->
### Other approximations {#other-approximations}

[Fully Independent Training Conditional]{}
\alignright{@Snelson:pseudo05}

-   Approximation to $p(\dataVector\given \inducingVector)$:

-   $   p(\dataVector\given \inducingVector)  = \prod_i p(\dataVector_i\given \inducingVector) $

Optimization of $\inducingInputMatrix$ is still difficult, and there are
some weird heteroscedatic effects

<!--frame end-->

