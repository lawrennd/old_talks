<!--frame start-->
### Variational Compression

\raggedleft{\scriptsize \citep{Snelson:pseudo05,Quinonero:unifying05,Lawrence:larger07,Titsias:variational09}}

-   Complexity of standard GP:

    -   $\bigO(\numData^3)$ in computation.

    -   $\bigO(\numData^2)$ in storage.

    \pause

-   Via low rank representations of covariance:

    -   $\bigO(\numData \numInducing^2)$ in computation.

    -   $\bigO(\numData \numInducing)$ in storage.

-   Where $\numInducing$ is user chosen number of *inducing* variables.
    They give the rank of the resulting covariance. \pause

<!--frame end-->
<!--frame start-->
### Variational Compression {#variational-compression}

-   Inducing variables are a compression of the real observations.

-   They are like pseudo-data. They can be in space of
    $\mappingFunctionVector$ or a space that is related through a linear
    operator [@Alvarez:efficient10] — e.g. a gradient or convolution.

<!--frame end-->
<!--frame start-->
### Variational Compression II

-   **Importantly** conditioning on inducing variables renders the
    likelihood independent across the data.

-   It turns out that this allows us to variationally handle uncertainty
    on the kernel (including the inputs to the kernel).

-   It also allows standard scaling approaches: stochastic variational
    inference @Hensman:bigdata13, parallelization @Gal:Distributed14 and
    work by Zhenwen Dai on GPUs to be applied: an *engineering*
    challenge?

<!--frame end-->

