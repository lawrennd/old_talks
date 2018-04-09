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

\plotcode{plot.bayes_update(diagrams='../../slides/diagrams/ml')}

\displaycode{pods.notebook.display_plots('dem_gaussian{stage:0>3}.svg', 
                            '../slides/diagrams/ml', stage=(1, 3))}

\slides{
### Bayes Update {data-transition="none"}

\includesvg{../slides/diagrams/ml/dem_gaussian001.svg}

### Bayes Update {data-transition="none"}

\includesvg{../slides/diagrams/ml/dem_gaussian002.svg}

### Bayes Update {data-transition="none"}

\includesvg{../slides/diagrams/ml/dem_gaussian003.svg}
}

### Stages to Derivation of the Posterior

-   Multiply likelihood by prior

    -   they are “exponentiated quadratics”, the answer is always also
        an exponentiated quadratic because
        $\exp(a^2)\exp(b^2) = \exp(a^2 + b^2)$.

-   Complete the square to get the resulting density in the form of a
    Gaussian.

-   Recognise the mean and (co)variance of the Gaussian. This is the
    estimate of the posterior.


