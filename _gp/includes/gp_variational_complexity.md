
### Variational Compression {#variational-compression data-transition="None"}

-   Inducing variables are a compression of the real observations.

-   They are like pseudo-data. They can be in space of
    $\mappingFunctionVector$ or a space that is related through a linear
    operator [@Alvarez:efficient10] — e.g. a gradient or convolution.

### Variational Compression II

-   Introduce *inducing* variables.

-   Compress information into the inducing variables and avoid the need to store all the data.

-   Allow for scaling e.g. stochastic variational @Hensman:bigdata13 or parallelization @Gal:Distributed14,@Dai:gpu14, @Seeger:auto17

