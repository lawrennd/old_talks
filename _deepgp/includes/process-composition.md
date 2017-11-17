### Mathematically

-   Composite *multivariate* function
    $$\mathbf{g}(\mathbf{x})=\mappingFunctionVector_5(\mappingFunctionVector_4(\mappingFunctionVector_3(\mappingFunctionVector_2(\mappingFunctionVector_1(\inputVector)))))$$

### Why Deep?

-   Gaussian processes give priors over functions.

-   Elegant properties:

    -   e.g. *Derivatives* of process are also Gaussian distributed (if
        they exist).

-   For particular covariance functions they are ‘universal
    approximators’, i.e. all functions can have support under the prior.

-   Gaussian derivatives might ring alarm bells.

-   E.g. a priori they don’t believe in function ‘jumps’.

### Process Composition

\raggedleft{\zhenwenPicture{1.5cm}}

-   From a process perspective: *process composition*.

-   A (new?) way of constructing more complex *processes* based on
    simpler components.

*Note*: To retain *Kolmogorov consistency* introduce IBP priors over
latent variables in each layer.

### Analysis of Deep GPs

-   [@Duvenaud:pathologies14] Duvenaud et al show that the derivative
    distribution of the process becomes more *heavy tailed* as number of
    layers increase.

-   [@Gal:dropout15] Gal and Ghahramani show that Drop Out is a
    variational approximation to a deep Gaussian process.


