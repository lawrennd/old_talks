\ifndef{instantiatingTheModel}
\define{instantiatingTheModel}

\editme

\subsection{Instantiating the Model}

\notes{So far, we haven't made *any* assumptions about the data in our model,
other than a factorization assumption between the fundamental variables
and the observations, $\dataVector$. Even this assumption does not
affect the generality of the model decomposition, because in the worst
case the likelihood $p(\dataVector|\mappingFunctionVector)$ could be a
Dirac $\delta$ function, implying $\dataVector=\mappingFunctionVector$
and allowing us to include complex interelations between $\dataVector$
directly in $p(\mappingFunctionVector)$. We have specified that
$p(\mappingFunctionVector, \inducingVector)$ should be Kolmogorov
consistent with $\mappingFunctionVector^*$ and $\inducingVector^*$ being
marginalized and we have argued that nonparametric models are important
in practice to ensure that all the information in our training data can
be passed to the test data.}

\notes{For a model to be useful, we need to specify relationships between our
data variables. Of course, this is the point at which a model also
typically becomes wrong. At least if our model isn't correct, then it should be a useful abstraction of the system.}


\subsection{Gaussian Processes}

\notes{A flexible class of models that fulfils the constraints of being
non-parametric and Kolmogorov consistent is Gaussian processes. A Gaussian
process prior for our fundamental variables, $\mappingFunctionVector$ assumes that they are jointly Gaussian distributed. Each
data point, $\mappingFunction_i$, is is jointly distributed with each other
data point $\mappingFunction_j$ as a multivariate Gaussian. The covariance of
this Gaussian is a function of the indices of the two data, in this case
$i$ and $j$. But these indices are not just restricted to discrete
values. The index can be a continuous value such as time, $t$, or
spatial location, $\inputVector$. The words index and indicate have a
common etymology. This is appropriate because the index indicates the
provenance of the data. In effect we have multivariate indices to
account for the full provenance, so that our observations of the world
are given as a function of, for example, the when, the where and the
what. "When" is given by time, "where" is given by spatial location and "what"
is given by a (potentially discrete) index indicating the further
provenance of the data. To define a joint Gaussian density, we need to
define the mean of the density and the covariance. Both this mean and
the covariance also need to be indexed by the when, the where and the
what.}

\subsection{Augmenting with Inducing Variables in Gaussian Processes}

\notes{To define our model, we need to describe the relationship between the
fundamental variables, $\mappingFunctionVector$, and the inducing variables,
$\inducingVector$. This needs to be done in such a way that the inducing
variables are also Kolmogorov consistent. A straightforward way of
achieving this is through a joint Gaussian process model over the
inducing variables and the data mapping variables, so in other words we
define a Gaussian process prior over}
$$
\begin{bmatrix}
\mappingFunctionVector \\ 
\inducingVector
\end{bmatrix} \sim \gaussianSamp{\mathbf{m}}{\kernelMatrix}
$$
\notes{where the covariance matrix has a block form,}
$$
\kernelMatrix = \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector\mappingFunctionVector} & \kernelMatrix_{\mappingFunctionVector\inducingVector} \\ \kernelMatrix_{\inducingVector\mappingFunctionVector} & \kernelMatrix_{\inducingVector\inducingVector}\end{bmatrix}
$$
\notes{and $\kernelMatrix_{\mappingFunctionVector\mappingFunctionVector}$ gives
the covariance between the fundamentals vector,
$\kernelMatrix_{\inducingVector\inducingVector}$ gives the covariance
matrix between the inducing variables and
$\kernelMatrix_{\inducingVector\mappingFunctionVector} = \kernelMatrix_{\mappingFunctionVector\inducingVector}^\top$
gives the cross covariance between the inducing variables,
$\inducingVector$ and the mapping function variables,
$\mappingFunctionVector$.}

\notes{The elements of
$\kernelMatrix_{\mappingFunctionVector\mappingFunctionVector}$ will be
computed through a covariance function (or kernel) given by
$\kernelScalar_\mappingFunction(\inputVector, \inputVector^\prime)$
where $\inputVector$ is a vector representing the *provenance* of the
data, which as we discussed earlier could involve a spatial location, a
time, or something about the nature of the data. In a Gaussian process
most of the modelling decisions take place in the construction of
$\kernelScalar_\mappingFunction(\cdot)$.}



\endif
