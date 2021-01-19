\ifndef{theMeanFunction}
\define{theMeanFunction}

\editme
\subsection{The Mean Function}


\notes{The mean of the process is given by a vector $\mathbf{m}$ which is
derived from a mean function $m(\inputVector)$. There are many occasions
when it is useful to include a mean function, but normally the mean
function will have a parametric form, $m(\inputVector;\paramVector)$,
and be subject (in itself) to the same constraints that a standard
parametric model has. Indeed, if we choose to model a function as a
parametric form plus Gaussian noise, we can recast such a model as a
simple Gaussian process with a covariance function
$k_\mappingFunction(\inputVector_i,\inputVector_j) = \dataStd^2 \delta_{i, j}$,
where $\delta_{i, j}$ is the *Kronecker* delta-function and a mean
function that is given by the standard parametric form. In this case we
see that the covariance function is mopping up the *residuals* that are
not captured by the mean function. If we genuinely were interested in
the form of a parametric mean function, as we often are in statistics,
where the mean function may include a set of covariates and potential
effects, often denoted by}
$$
m(\inputVector) = \boldsymbol{\beta}^\top \inputVector,
$$
\notes{where here the provenance of the data is known as the covariates, and
the variable associated with $\dataVector$ is typically known as a
*response* variable. In this case the particular influence of each of
the covariates is being encoded in a vector $\boldsymbol{\beta}$. To a
statistician, the relative values of the elements of this vector are
often important in making a judgement about the influence of the
covariates. For example, in disease modelling the mean function might be
used in a *generalized* linear model through a link function to
represent a rate or risk of disease (e.g. @Saul:chained16). The
covariates should *co-vary* (or move together) with the response
variable. Appropriate covariates for malaria incidence rate might
include known influencers of the disease. For example, if we are dealing
with *malaria* then we might expect disease rates to be influenced by
altitude, average temperature, average rainfall, local distribution of
prophylactic measures (such as nets) etc. The covariance of the Gaussian
process then has the role of taking care of the *residual* variance in
the data: the data that is not explained by the mean function, i.e. the
variance that cannot be explained by the parametric model. In a disease
mapping model, it makes sense to assume that these residuals may not be
independent. An underestimate of disease at one spatial location, may
imply an underestimate of disease rates at a nearby location. The
mismatch between the observed disease rate and that predicted by
modeling the relationship with the covariates through the mean function
is then given by the covariance function.}

\notes{The machine learner's focus on prediction means that within that community the mean function is more often removed, with all the predictive power being incorporated within the Gaussian process covariance.
}

\todo{Mention here an example of things going wrong? Or do a short run
of a mauna loa data to demonstrate, with a mean function included?}

\setupcode{import GPy
import pods}

\code{data = pods.datasets.mauna_loa()
kern = GPy.kern.Linear(1) + GPy.kern.RBF(1) + GPy.kern.Bias(1)
model = GPy.models.GPRegression(data['X'], data['Y'], kern)
#model.optimize()}


\plotcode{pb.plot(xlim}


\notes{So we *could* interpret Gaussian process models as approaches to dealing
with residuals \tk{FIXME}}

\endif
