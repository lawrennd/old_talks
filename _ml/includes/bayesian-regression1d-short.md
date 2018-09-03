\subsection{Prior Distribution}
\slides{
* Bayesian inference requires a prior on the parameters.
* The prior represents your belief *before* you see the data of the likely value of the parameters.
* For linear regression, consider a Gaussian prior on the intercept:
}\notes{The tradition in Bayesian inference is to place a probability density over the parameters of interest in your model. This choice is made regardless of whether you generally believe those parameters to be stochastic or deterministic in origin. In other words, to a Bayesian, the modelling treatment does not differentiate between epistemic and aleatoric uncertainty. For linear regression we could consider the following Gaussian prior on the intercept parameter,}
  $$c \sim \gaussianSamp{0}{\alpha_1}$$
\notes{where $\alpha_1$ is the variance of the prior distribution, its mean being zero.}

\subsection{Posterior Distribution}
\slides{
* Posterior distribution is found by combining the prior with the likelihood.
* Posterior distribution is your belief *after* you see the data of the likely value of the parameters.
* The posterior is found through **Bayes’ Rule**}\notes{The prior distribution is combined with the likelihood of the data given the parameters $p(\dataScalar|c)$ to give the posterior via *Bayes' rule*,}
  $$
  p(c|\dataScalar) = \frac{p(\dataScalar|c)p(c)}{p(\dataScalar)}
  $$
  \notes{where $p(\dataScalar)$ is the marginal probability of the data, obtained through integration over the joint density, $p(\dataScalar, c)=p(\dataScalar|c)p(c)$. Overall the equation can be summarized as,}
  $$
  \text{posterior} = \frac{\text{likelihood}\times \text{prior}}{\text{marginal likelihood}}.
  $$



\newslide{Bayes Update}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.bayes_update(diagrams='../slides/diagrams/ml')}

\setupdisplaycode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('dem_gaussian{stage:0>2}.svg', 
                            diagrams='../slides/diagrams/ml', 
							stage=IntSlider(1, 1, 3, 1))}
\slides{
\startslides{dem_gaussian}{1}{3}
\includesvg{../slides/diagrams/ml/dem_gaussian001.svg}{}{dem_gaussian}
\includesvg{../slides/diagrams/ml/dem_gaussian002.svg}{}{dem_gaussian}
\includesvg{../slides/diagrams/ml/dem_gaussian003.svg}{}{dem_gaussian}
}
\notesfigure{\includesvg{../slides/diagrams/ml/dem_gaussian003.svg}}
\notes{\caption{Combining a Gaussian likelihood with a Gaussian prior to form a Gaussian posterior}}

\notes{Another way of seeing what's going on is to note that the numerator of Bayes' rule merely multiplies the likelihood by the prior. The denominator, is not a function of $c$. So the functional form is entirely determined by the multiplication of prior and likelihood. This has the effect of ensuring that the posterior only has probability mass in regions where both the prior and the likelihood have probability mass.}

\notes{The marginal likelihood, $p(\dataScalar)$, operates to ensure that the distribution is normalised.}

\newslide{Stages to Derivation of the Posterior}
\slides{
* Multiply likelihood by prior
  * they are “exponentiated quadratics”, the answer is always also an exponentiated quadratic because $\exp(a^2)\exp(b^2) = \exp(a^2 + b^2)$.
* Complete the square to get the resulting density in the form of a Gaussian.
* Recognise the mean and (co)variance of the Gaussian. This is the estimate of the posterior.
}\notes{For the Gaussian case, the normalisation of the posterior can be performed analytically. This is because both the prior and the likelihood have the form of an *exponentiated quadratic*,
$$
\exp(a^2)\exp(b^2) = \exp(a^2 + b^2),
$$
and the properties of the exponential mean that the product of two exponentiated quadratics is also an exponentiated quadratic. That implies that the posterior is also Gaussian, because a normalized exponentiated quadratic is a Gaussian distribution.[^normalize-gaussian]

[^normalize-gaussian]: Note not all exponentiated quadratics can be normalized, to do so, the coefficient associated with the variable squared, $\dataScalar^2$, must be strictly positive.}
