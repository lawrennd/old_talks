\titlegraphic{\includegraphics[width=2cm]{../../../gp/tex/diagrams/logo}}

\frame{\maketitle}

\include{../../../gp/tex/talks/gpbook.md}

<!--frame start-->
### Outline

\tableofcontents[hideallsubsections] 

<!--frame end-->
\newsection{The Gaussian Density}{../../../ml/tex/talks/univariateGaussian}
\include{../../../gp/tex/talks/univariate_gaussian_properties.md}
\include{../../../ml/tex/talks/linear_function.md}
\include{../../../ml/tex/talks/regression_examples.md}
\include{../../../ml/tex/talks/overdetermined_inaugural.md}
\include{../../../ml/tex/talks/underdetermined_system.md}

<!--frame start-->
### Probability for Under- and Overdetermined

-   To deal with overdetermined introduced probability distribution for
    ‘variable’, $\noiseScalar_i$.

-   For underdetermined system introduced probability distribution for
    ‘parameter’, $c$.

-   This is known as a Bayesian treatment.

<!--frame end-->
<!--frame start-->
-   For general Bayesian inference need multivariate priors.

-   E.g. for multivariate linear regression:

    <!--overprint start-->
    \onslide<1>
    $$\dataScalar_i = \sum_i \mappingScalar_j \inputScalar_{i, j} + \epsilon_i$$
    \onslide<2>
    $$\dataScalar_i = \mappingVector^\top \inputVector_{i, :} + \epsilon_i$$

    <!--overprint end-->
    (where we’ve dropped $c$ for convenience), we need a prior over
    $\mappingVector$.

-   This motivates a *multivariate* Gaussian density.

-   We will use the multivariate Gaussian to put a prior *directly* on
    the function (a Gaussian process).

<!--frame end-->
\newsubsection{Bayesian Regression}{../../../ml/tex/talks/bayesianRegression1d_short.tex}

\newsubsection{Multivariate Bayesian Regression}{../../../ml/tex/talks/multivariateBayesianLinear_short}
\newsubsection{Two Dimensional Gaussian Distribution}{../../../ml/tex/talks/twoDGaussian}
\newsubsection{Multivariate Gaussian Properties}{../../../gp/tex/talks/multivariateGaussianProperties}
\newsubsection{Distributions over Functions}{../../../gp/tex/talks/gpdistfunc}
\newsubsection{Two Point Marginals}{../../../gp/tex/talks/gptwopointpred}

\include{../../../kern/tex/talks/rbfcovariance.md}
\include{../../../kern/tex/talks/computing_rbf_covariance.md}

\newsection{Covariance from Basis Functions}{../../../gp/tex/talks/basisFunctions}
\newsubsection{An Alternative Analysis}{../../../gp/tex/talks/gpCovarianceConstruction}
\include{../../../kern/tex/talks/rbfbasiscovariance.md}
\newsubsection{An Infinite Basis}{../../../gp/tex/talks/infiniteBasis}
\include{../../../kern/tex/talks/rbfcovariance.md}
\include{../../../kern/tex/talks/rbfbasiscovariance.md}

<!--frame start-->
\[allowframebreaks\]

### References

\tiny

\bibliographystyle{pdf_abbrvnat}
<!--frame end-->

