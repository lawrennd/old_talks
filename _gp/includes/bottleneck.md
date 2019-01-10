\ifndef{bottleneck}
\define{bottleneck}
\editme

\newslide{Nonparametric Gaussian Processes}

\slides{
-   We’ve seen how we go from parametric to non-parametric.

-   The limit implies infinite dimensional $\mappingVector$.

-   Gaussian processes are generally non-parametric: combine data with
    covariance function to get model.

-   This representation *cannot* be summarized by a parameter vector of
    a fixed size.
}
\notes{We’ve seen how we go from parametric to non-parametric. The limit implies infinite dimensional $\mappingVector$. Gaussian processes are generally non-parametric: combine data with covariance function to get model. This representation *cannot* be summarized by a parameter vector of a fixed size.}

\newslide{The Parametric Bottleneck}

\slides{
-   Parametric models have a representation that does not respond to increasing training set size.

-   Bayesian posterior distributions over parameters contain the information about the training data.

    -   Use Bayes’ rule from training data,
        $p\left(\mappingVector|\dataVector, \inputMatrix\right)$,

    -   Make predictions on test data
        $$p\left(\dataScalar_*|\inputMatrix_*, \dataVector, \inputMatrix\right) = \int
              p\left(\dataScalar_*|\mappingVector,\inputMatrix_*\right)p\left(\mappingVector|\dataVector,
                \inputMatrix)\text{d}\mappingVector\right).$$

-   $\mappingVector$ becomes a bottleneck for information about the training set to pass to the test set.

-   Solution: increase $\numBasisFunc$ so that the bottleneck is so large that it no longer presents a problem.

-   How big is big enough for $\numBasisFunc$? Non-parametrics says $\numBasisFunc \rightarrow \infty$.
}
\notes{Parametric models have a representation that does not respond to increasing training set size. Bayesian posterior distributions over parameters contain the information about the training data, for example if we use use Bayes’ rule from training data,
$$
p\left(\mappingVector|\dataVector, \inputMatrix\right),
$$
to make predictions on test data
$$
p\left(\dataScalar_*|\inputMatrix_*, \dataVector, \inputMatrix\right) = \int
              p\left(\dataScalar_*|\mappingVector,\inputMatrix_*\right)p\left(\mappingVector|\dataVector,
                \inputMatrix)\text{d}\mappingVector\right)
$$ 
then $\mappingVector$ becomes a bottleneck for information about the training set to pass to the test set. The solution is to increase $\numBasisFunc$ so that the bottleneck is so large that it no longer presents a problem. How big is big enough for $\numBasisFunc$? Non-parametrics says $\numBasisFunc \rightarrow \infty$.
}

\newslide{The Parametric Bottleneck}

\slides{
-   Now no longer possible to manipulate the model through the standard parametric form.

. . .

-   However, it *is* possible to express *parametric* as GPs:
    $$\kernelScalar\left(\inputVector_i,\inputVector_j\right)=\basisFunction_:\left(\inputVector_i\right)^\top\basisFunction_:\left(\inputVector_j\right).$$

. . .

-   These are known as degenerate covariance matrices.

. . .

-   Their rank is at most $\numBasisFunc$, non-parametric models have full rank covariance matrices.

. . .

-   Most well known is the “linear kernel”, $\kernelScalar(\inputVector_i, \inputVector_j) = \inputVector_i^\top\inputVector_j$.
}
\newslide{Making Predictions}
\slides{
-   For non-parametrics prediction at new points $\mappingFunctionVector_*$ is made by conditioning on $\mappingFunctionVector$ in the joint distribution.

. . .

-   In GPs this involves combining the training data with the covariance function and the mean function.

. . .

-   Parametric is a special case when conditional prediction can be summarized in a *fixed* number of parameters.

. . .

-   Complexity of parametric model remains fixed regardless of the size of our training data set.

. . .

-   For a non-parametric model the required number of parameters grows with the size of the training data.
}

\notes{Now no longer possible to manipulate the model through the standard parametric form. However, it *is* possible to express *parametric* as GPs:
$$
\kernelScalar\left(\inputVector_i,\inputVector_j\right)=\basisFunction_:\left(\inputVector_i\right)^\top\basisFunction_:\left(\inputVector_j\right).
$$ 
These are known as degenerate covariance matrices. Their rank is at most $\numBasisFunc$, non-parametric models have full rank covariance matrices. Most well known is the “linear kernel”, 
$$
\kernelScalar(\inputVector_i, \inputVector_j) = \inputVector_i^\top\inputVector_j.
$$
For non-parametrics prediction at a new point, $\mappingFunctionVector_*$, is made by conditioning on $\mappingFunctionVector$ in the joint distribution. In GPs this involves combining the training data with the covariance function and the mean function. Parametric is a special case when conditional prediction can be summarized in a *fixed* number of parameters. Complexity of parametric model remains fixed regardless of the size of our training data set. For a non-parametric model the required number of parameters grows with the size of the training data.}

\endif
