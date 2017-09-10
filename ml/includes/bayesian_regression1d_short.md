### Prior Distribution

-   Bayesian inference requires a prior on the parameters.

-   The prior represents your belief *before* you see the data of the
    likely value of the parameters.

-   For linear regression, consider a Gaussian prior on the intercept:
    $$c \sim \gaussianSamp{0}{\alpha_1}$$

### Posterior Distribution

-   Posterior distribution is found by combining the prior with the
    likelihood.

-   Posterior distribution is your belief *after* you see the data of
    the likely value of the parameters.

-   The posterior is found through **Bayes’ Rule**
    $$p(c|{y}) = \frac{p({y}|c)p(c)}{p({y})}$$

### Bayes Update {data-transition="none"}

<object class="svgplot" data="../ml/diagrams/dem_gaussian001.svg">
</object>

### Bayes Update {data-transition="none"}

<object class="svgplot" data="../ml/diagrams/dem_gaussian002.svg">
</object>

### Bayes Update {data-transition="none"}

<object class="svgplot" data="../ml/diagrams/dem_gaussian003.svg">
</object>


### Stages to Derivation of the Posterior

-   Multiply likelihood by prior

    -   they are “exponentiated quadratics”, the answer is always also
        an exponentiated quadratic because
        $\exp(a^2)\exp(b^2) = \exp(a^2 + b^2)$.

-   Complete the square to get the resulting density in the form of a
    Gaussian.

-   Recognise the mean and (co)variance of the Gaussian. This is the
    estimate of the posterior.

