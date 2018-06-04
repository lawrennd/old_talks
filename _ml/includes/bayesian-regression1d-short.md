\slides{
### Prior Distribution

* Bayesian inference requires a prior on the parameters.

* The prior represents your belief *before* you see the data of the
    likely value of the parameters.

* For linear regression, consider a Gaussian prior on the intercept:
    $$c \sim \gaussianSamp{0}{\alpha_1}$$
}

\slides{
### Posterior Distribution

* Posterior distribution is found by combining the prior with the likelihood.
* Posterior distribution is your belief *after* you see the data of the likely value of the parameters.
* The posterior is found through **Bayes’ Rule**
  $$
  p(c|\dataScalar) = \frac{p(\dataScalar|c)p(c)}{p(\dataScalar)}
  $$
}

\slides{
### Bayes Update 

\plotcode{import teaching_plots as plot}
\plotcode{plot.bayes_update(diagrams='../slides/diagrams/ml')}

\displaycode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('dem_gaussian{stage:0>2}.svg', 
                            diagrams='../slides/diagrams/ml', 
							stage=IntSlider(1, 1, 3, 1))}

\startslides{dem_gaussian}{1}{3}
\includesvg{../slides/diagrams/ml/dem_gaussian001.svg}{}{dem_gaussian}
\includesvg{../slides/diagrams/ml/dem_gaussian002.svg}{}{dem_gaussian}
\includesvg{../slides/diagrams/ml/dem_gaussian003.svg}{}{dem_gaussian}
}
\notesfigure{\includesvg{../slides/diagrams/ml/dem_gaussian003.svg}}
\notes{\caption{Combining a Gaussian likelihood with a Gaussian prior to form a Gaussian posterior}}

\slides{
### Stages to Derivation of the Posterior

* Multiply likelihood by prior
  * they are “exponentiated quadratics”, the answer is always also an exponentiated quadratic because $\exp(a^2)\exp(b^2) = \exp(a^2 + b^2)$.
* Complete the square to get the resulting density in the form of a Gaussian.
* Recognise the mean and (co)variance of the Gaussian. This is the estimate of the posterior.
}
