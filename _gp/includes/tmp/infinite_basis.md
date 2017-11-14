<!--frame start-->
\[fragile\]

### Selecting Number and Location of Basis

-   Need to choose

    1.  location of centers

    2.  number of basis functions

    Restrict analysis to 1-D input, ${x}$.

-   Consider uniform spacing over a region: \only<1>{\[
        {k}\left({x}_i, {x}_j\right) = \alpha {\boldsymbol{{\phi}}}_k({x}_i)^\top{\boldsymbol{{\phi}}}_k({x}_j)
        \]}\only<2>{\[
        {k}\left({x}_i, {x}_j\right) = \alpha \sum_{k=1}^{m}{\phi}_k({x}_i){\phi}_k({x}_j)
        \]}\only<3>{\[
        {k}\left({x}_i, {x}_j\right) = \alpha \sum_{k=1}^{m}\exp\left(-\frac{({x}_i -{\mu}_k)^2}{2{\ell}^2}\right)\exp\left(-\frac{({x}_j -{\mu}_k)^2}{2{\ell}^2}\right)
        \]}\only<4>{\[
        {k}\left({x}_i, {x}_j\right) = \alpha \sum_{k=1}^{m}\exp\left(-\frac{({x}_i -{\mu}_k)^2}{2{\ell}^2} -\frac{({x}_j -{\mu}_k)^2}{2{\ell}^2}\right)
        \]}\only<5>{\[
        {k}\left({x}_i,{x}_j\right) = \alpha \sum_{k=1}^{{m}} \exp\left(
          -\frac{{x}_i^2 + {x}_j^2 - 2{\mu}_k \left({x}_i+{x}_j\right) +
            2{\mu}_k^2}{2 {\ell}^2} \right),
        \]}

<!--frame end-->
<!--frame start-->
### Uniform Basis Functions

-   Set each center location to $${\mu}_k = a+\Delta{\mu}\cdot (k-1).$$
    \pause

-   Specify the basis functions in terms of their indices,
    $$\begin{aligned}
        {k}\left({x}_i,{x}_j\right) = &\alpha^\prime\Delta{\mu}\sum_{k=1}^{{m}} \exp\Bigg(
          -\frac{{x}_i^2 + {x}_j^2}{2
            {\ell}^2}\\ 
            & - \frac{2\left(a+\Delta{\mu}\cdot (k-1)\right)
            \left({x}_i+{x}_j\right) + 2\left(a+\Delta{\mu}\cdot (k-1)\right)^2}{2
            {\ell}^2} \Bigg).
        \end{aligned}$$ \pause

-   Here we’ve scaled variance of process by $\Delta{\mu}$.

<!--frame end-->
<!--frame start-->
### Infinite Basis Functions

-   Take
    $${\mu}_1=a \ \text{and}\  {\mu}_{m}=b \ \text{so}\ b= a+ \Delta{\mu}\cdot({m}-1)$$
    \pause

-   This implies $$b-a = \Delta{\mu}({m}-1)$$ \pauseand therefore
    $${m}= \frac{b-a}{\Delta {\mu}} + 1$$ \pause

-   Take limit as $
        \Delta{\mu}\rightarrow 0$ so ${m}\rightarrow \infty$
    \pause{\small\[
        {k}({x}_i,{x}_j) = \alpha^\prime \int_a^b \exp\Bigg( -\frac{{x}_i^2 +
            {x}_j^2}{2 {\ell}^2} + \frac{2\left({\mu}- \frac{1}{2}\left({x}_i + {x}_j\right)\right)^2
            -\frac{1}{2}\left({x}_i + {x}_j\right)^2}{2 {\ell}^2}
        \Bigg)\text{d}{\mu},
        \]} where we have used $a + k\cdot\Delta{\mu}\rightarrow {\mu}$.

<!--frame end-->
<!--frame start-->
### Result

-   Performing the integration leads to $$\begin{aligned}
        {k}({x}_i,&{x}_j) = \alpha^\prime \sqrt{\pi{\ell}^2}
        \exp\left( -\frac{\left({x}_i-{x}_j\right)^2}{4{\ell}^2}\right)\\ &\times
        \frac{1}{2}\left[\text{erf}\left(\frac{\left(b - \frac{1}{2}\left({x}_i +
                  {x}_j\right)\right)}{{\ell}} \right)-
          \text{erf}\left(\frac{\left(a - \frac{1}{2}\left({x}_i +
                  {x}_j\right)\right)}{{\ell}} \right)\right],
        \end{aligned}$$ \pause

-   Now take limit as $a\rightarrow -\infty$ and $b\rightarrow \infty$
    \pause$${k}\left({x}_i,{x}_j\right) = \alpha\exp\left(
          -\frac{\left({x}_i-{x}_j\right)^2}{4{\ell}^2}\right).$$ where
    $\alpha=\alpha^\prime \sqrt{\pi{\ell}^2}$.

<!--frame end-->
<!--frame start-->
### Infinite Feature Space

-   An RBF model with infinite basis functions is a Gaussian
    process.\pause

-   The covariance function is given by the \rbfKernelLong covariance
    function. $${k}\left({x}_i,{x}_j\right) = \alpha \exp\left(
          -\frac{\left({x}_i-{x}_j\right)^2}{4{\ell}^2}\right).$$

<!--frame end-->
<!--frame start-->
### Infinite Feature Space {#infinite-feature-space}

-   An RBF model with infinite basis functions is a Gaussian process.

-   The covariance function is the \rbfKernelLong.

-   **Note:** The functional form for the covariance function and basis
    functions are similar.

    -   this is a special case,

    -   in general they are very different

\only<1->{\begin{center}\textbf{Similar results
    can obtained for multi-dimensional input models \cite{Williams:computation98,Neal:book96}.}\end{center}}

<!--frame end-->

