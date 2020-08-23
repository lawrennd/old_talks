\ifndef{makingParametersNonParametric}
\define{makingParametersNonParametric}

\editme

\subsection{Making Parameters non-Parametric}

\notes{We will start by introducing a set of variables, $\inducingVector$, that
are finite dimensional. These variables will eventually be used to
communicate information between the training and test data, i.e. across
the TT channel.}
$$
p(\dataVector^*|\dataVector) = \int p(\dataVector^*|\inducingVector) q(\inducingVector|\dataVector) \text{d}\inducingVector
$$
\notes{where we have introduced a distribution over $\inducingVector$,
$q(\inducingVector|\dataVector)$ which is not necessarily the true
posterior distribution.}

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[1, 3],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)

pgm.add_node(daft.Node("y", r"$\dataVector$", 0.5, 0.5, fixed=False))
pgm.add_node(daft.Node("u", r"$\inducingVector$", 0.5, 1.5, fixed=False))
pgm.add_edge("u", "y")

pgm.render().figure.savefig("\diagramsDir/ml/u-to-y.svg", transparent=True)}

\figure{\includediagram{\diagramsDir/ml/u-to-y.svg}{40%}}{Augmenting the variable space with a set of latent *inducing vectors*}{u-to-y}

\notes{Our simple graphical model augmented with $\inducingVector$ which we
refer to as inducing variables. Note that the model is still totally
general because $p(\dataVector, \inducingVector)$ is an augmented
variable model and the original $p(\dataVector)$ is easily recovered by
simple marginalization of $\inducingVector$. We haven't yet made any
assumptions about our data.}

\notes{The model we've introduced now seems remarkably like the parametric
model we argued against in the previous section. So what's going on
here, is there going to be some kind of parametric/non parametric 3 card
trick where with sleight of hand we are trying to introduce a parametric
model? Well clearly not, because I've just given the game away. But I
believe there are some important differences to the traditional approach
for parameterizing a model. Philosophically, our variables
$\inducingVector$ are variables that augment the the model. We have not
yet made any assumptions by introducing them. Normally the
parameterization of the model instantiates assumptions, but this is not
happening here. In particular note that we have *not* assumed that the
training data factorize given the inducing variables. Secondly, we are
not going to specify the dimensionality of $\inducingVector$ (i.e. the
size of the TT channel) at *design* time. We are going to allow it to
change at *run* time. We will do this by ensuring that the inducing
variables also obey Kolmogorov consistency. In particular we require
that If we build a joint density as follows:}
\begin{align*} 
p(\dataVector, \inducingVector|\numInducing^*,
\numData^*) = \int p(\dataVector^*, \dataVector,
\inducingVector^*, \inducingVector) \text{d}\dataVector^*
\text{d}\inducingVector^*,
\end{align*}
\notes{where $\inducingVector$ are the inducing variables we choose might
choose to instantiate at any given time (of dimensionality
$\numInducing$) and $\inducingVector^*$ is the $\numInducing^*$
dimensional pool of future inducing variables we have *not yet* chosen
to instantiate (where $\numInducing^*$ could be infinite). Our new
Kolmogorov consistency condition requires that}
$$
p(\dataVector, \inducingVector|\numInducing^*,\numData^*) = p(\dataVector, \inducingVector).
$$
\notes{It doesn't need to be predetermined at *design time* because we allow
for the presence of a (potentially infinite) number of inducing
variables $\inducingVector^*$ that we may wish to *later* instantiate to
improve the quality of our model. In other words, it is very similar to
the parametric approach, but now we have access to a future pool of
additional parameters, $\inducingVector^*$ that we can call upon to
increase the bandwidth of the TT channel as appropriate. In parametric
modelling, calling upon such parameters has a significant effect on the
likelihood of the model, but here these variables are auxiliary
variables that will *not* effect the likelihood of the model. They
merely effect our ability to approximate the true bandwidth of the TT
channel. The quality of this approximation can be varied at run time. It
is not necessary to specify it at design time. This gives us the
flexibility we need in terms of modeling, whilst keeping computational
complexity and memory demands manageable and appropriate to the task at
hand.}

\setupplotcode{import daft}
\plotcode{
%%tikz --scale 2 --size 200,200 -f svg
% Define nodes
\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$\dataVector$};
\draw node[latent, left=of y] (ystar) {$\dataVector^*$};
\draw node[latent, above=of y] (u) {$\inducingVector$};
\draw node[latent, above=of ystar] (ustar) {$\inducingVector^*$};
        
% Connect the nodes
\draw [-] (u) to (y);%
\draw [-] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-] (ystar) to (y);%
\draw [-] (ustar) to (ystar);%
\draw [-] (u) to (ystar);%
\end{tikzpicture}}
 
\figure{}

\notes{Adding in the test data and the inducing variables we have not yet
chosen to instantiate. Here we see that we still haven't defined any
structure in the graph, and therefore we have not yet made any
assumptions about our data. Not shown in the graph is the additional
assumption that whilst $\dataVector$ has $\numData$ dimensions and
$\inducingVector$ has $\numInducing$ dimensions, $\dataVector^*$ and
$\inducingVector^*$ are potentially infinite dimensional.}

\subsubsection{Fundamental Variables}

\notes{To focus our model further, we assume that we observe observations,
$\dataVector$ that are derived from some underlying fundamental,
$\mappingFunctionVector$, through simple factorized likelihoods. The
idea of the fundamental variables is that they are sufficient to
describe the world around us, but we might not be able to observe them
directly. In particular we might observe relatively simple corruptions
of the fundamental variables such as independent addition of noise, or
thresholding. We might observe something relative about two fundamental
veriables. For example if we took $\mappingFunction_{12,345}$ to be the
height of Tom Cruise and $\mappingFunction_{23,789}$ to be the height of
Penelope Cruz then we might take for an observation a binary value
indicating the relative heights, so
$\datascalar_{72,394} = \mappingFunction_{12,345} < \mappingFunction_{23,789}$.
The fundamental variable is an artificial construct, but it can prove to
be a useful one. In particular we'd like to assume that the
relationship between our observations, $\dataVector$ and the fundamental
variables, $\mappingFunctionVector$ might factorize in some way. In the
framework we think of this relationship, given by
$p(\dataVector|\inducingVector)$ as the *likelihood*. We can ensure that
assuming the likelihood factorizes does not at all reduce the generality
of our model, by forcing the distribution over the fundamentals,
$p(\mappingFunctionVector)$ to also be Kolmogorov consistent. This
ensures that in the case where the the likelihood is fully factorized
over $\numData$ the model is still general if we allow the factors of
the likelihood to be Dirac delta functions suggesing that
$\dataScalar_i = \mappingFunction_i$. Since we haven't yet specified
any forms for the probability distributions this *is* allowed and
therefore the formulation is still totally general.}
$$
p(\dataVector|\numData^*) = \int p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector, \mappingFunctionVector^*)\text{d}\mappingFunctionVector \text{d}\mappingFunctionVector^*
$$
\notes{and since we enforce Kolmogorov consistency we have}
$$
p(\dataVector|\numData*) = p(\dataVector).
$$

\setupplotcode{import daft}
\plotcode{%%tikz --scale 2 --size 300,300 -f svg
% Define nodes
\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$\dataVector$};
\draw node[latent, above=of y] (f) {$\mappingFunctionVector$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\inducingVector^*$};
\draw node[latent, above=of f] (u) {$\inducingVector$};

        
% Connect the nodes
\draw [-, draw=gray] (ustar) to (u);%
\draw [-, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [-] (u) to (f);%
\end{tikzpicture}}
 
\figure{} 

\notes{Now we assume some form of factorization for our data observations,
$\dataVector$, given the fundamental variables,
$\mappingFunctionVector$, so that we have}
$$
p(\dataVector|\mappingFunctionVector) = \prod_{i} p(\dataVector^i| \mappingFunctionVector^i)
$$
\notes{so that we have subsets of the data $\dataVector^i$ which are dependent
on sub sets of the fundamental variables, $\mappingFunction$. For
simplicity of notation we will assume a factorization across the entire
data set, so each observation, $\dataScalar_i$, has a single underlying
fundamental variable, $\mappingFunction_i$, although more complex
factorizations are also possible and can be considered within the
analysis.}
$$
p(\dataVector|\mappingFunctionVector) = \prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i)
$$

\setupplotcode{import daft}
\plotcode{%%tikz --size 300,300 -f svg
% Define nodes
\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$\dataScalar_i$};
\draw node[latent, above=of y] (f) {$\mappingFunction_i$};
\draw node[latent, above=of f] (u) {$\inducingVector$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\inducingVector^*$};
        
% Connect the nodes
\draw [-, draw=gray] (ustar) to (u);%
\draw [-, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [-] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots\numData$} ;
\end{tikzpicture}}
        
\notes{We now decompose, without loss of generality, our joint distribution
over inducing variables and fundamentals into the following parts}
$$
p(\inducingVector, \mappingFunctionVector) = p(\mappingFunctionVector|\inducingVector)p(\inducingVector),
$$
\notes{where we assume that we have marginalised $\mappingFunctionVector^*$ and
$\inducingVector^*$.}


\setupplotcode{import daft}

\plotcode{%%tikz --size 300,300 -f svg
% Define nodes
\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$\dataScalar_i$};
\draw node[latent, above=of y] (f) {$\mappingFunction_i$};
\draw node[latent, above=of f] (u) {$\inducingVector$};
        
% Connect the nodes
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots\numData$} ;
\end{tikzpicture}}

\setupplotcode{import daft}
\plotcode{%%tikz --scale 2 --size 300,300 -f svg
% Define nodes
\begin{tikzpicture}[scale=2]
\draw node[obs] (y) {$\dataVector$};
\draw node[latent, above=of y] (f) {$\mappingFunctionVector$};
\draw node[obs] (y) {$\dataScalar_i$};
\draw node[latent, above=of y] (f) {$\mappingFunction_i$};
\draw node[latent, above=of y] (u) {$\inducingVector$};
\draw node[latent, above left=of y] (u) {$\inducingVector$};
\draw node[latent, above right=of y] (ustar) {$\inducingVector^*$};
\draw node[latent, above=of f] (u) {$\inducingVector$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\inducingVector^*$};
\draw node[const, above=of f] (u) {$\inducingVector$};
        
% Connect the nodes
\draw [->] (u) to (y);%
\draw [->] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-, draw=gray] (ustar) to (u);%
\draw [->, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots\numData$} ;
\end{tikzpicture}}


\setupplotcode{import daft}

\plotcode{
%%tikz --size 300,300 -f svg
% Define nodes
\begin{tikzpicture}[scale=2]
\draw node[obs] (y) {$\dataVector$};
\draw node[latent, above=of y] (f) {$\mappingFunctionVector$};
\draw node[obs] (y) {$\dataScalar_i$};
\draw node[latent, above=of y] (f) {$\mappingFunction_i$};
\draw node[latent, above=of y] (u) {$\inducingVector$};
\draw node[latent, above left=of y] (u) {$\inducingVector$};
\draw node[latent, above right=of y] (ustar) {$\inducingVector^*$};
\draw node[latent, above=of f] (u) {$\inducingVector$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\inducingVector^*$};
\draw node[const, above=of f] (u) {$\inducingVector$};
        
% Connect the nodes
\draw [->] (u) to (y);%
\draw [->] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-, draw=gray] (ustar) to (u);%
\draw [->, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots\numData$} ;
\end{tikzpicture}}

\setupplotcode{import daft}
\plotcode{
%%tikz --scale 2 --size 300,300 -f svg
% Define nodes
\draw node[obs] (y) {$\dataVector$};
\draw node[latent, above=of y] (f) {$\mappingFunctionVector$};
\draw node[obs] (y) {$\dataScalar_i$};
\draw node[latent, above=of y] (f) {$\mappingFunction_i$};
\draw node[latent, above=of y] (u) {$\inducingVector$};
\draw node[latent, above left=of y] (u) {$\inducingVector$};
\draw node[latent, above right=of y] (ustar) {$\inducingVector^*$};
\draw node[latent, above=of f] (u) {$\inducingVector$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\inducingVector^*$};
\draw node[const, above=of f] (u) {$\inducingVector$};
        
% Connect the nodes
\draw [->] (u) to (y);%
\draw [->] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-, draw=gray] (ustar) to (u);%
\draw [->, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots\numData$} ;
}
 
\subsection{Instantiating the Model}

\notes{So far we haven't made any assumptions about the data in our model,
other than a factorization assumption between the fundamental variables
and the observations, $\dataVector$. Even this assumption does not
affect the generality of the model decomposition, because in the worst
case the likelihood $p(\dataVector|\mappingFunctionVector)$ could be a
Dirac $\delta$ function, implying $\dataVector=\mappingFunctionVector$
and allowing us to include complex interelations between $\dataVector$
directly in $p(\mappingFunctionVector)$. We have specified that
$p(\mappingFunctionVector, \inducingVector)$ should be Kolmogorov
consistent with $\mappingFunctionVector^*$ and $\inducingVector^*$ being
marginalised and we have argued that non-parametric models are important
in practice to ensure that all the information in our training data can
be passed to the test data.}

\notes{For a model to be useful, we need to specify relationships between our
data variables. Of course, this is the point at which a model also
typically becomes wrong. The following considerations should arise:}

\notes{If our model is not correct, is it a useful abstraction given what we
expect to observe about the data? For example, Brownian motion is
modelled as a stochastic differential equation.}


\subsubsection{Gaussian Processes}

\notes{A flexible class of models that fulfils the constraints of being
non-parametric and Kolmogorov consistent is Gaussian processes. Gaussian
processes assume that the data is jointly Gaussian distributed. Each
data point, $\dataScalar_i$, is is jointly distributed with each other
data point $\dataScalar_j$ as a multivariate Gaussian. The covariance of
this Gaussian is a function of the indices of the two data, in this case
$i$ and $j$. But these indices are not just restricted to discrete
values. The index can be a continuous value such as time, $t$, or
spatial location, $\inputVector$. The words index and indicate have a
common etymology. This is appropriate because the index indicates the
provenance of the data. In effect we have multivariate indices to
account for the full provenance, so that our observations of the world
are given as a function of, for example, the when, the where and the
what. When is given by time, where is given by spatial location and what
is given by a (potentially discrete) index indicating the further
provenance of the data. To define a joint Gaussian density, we need to
define the mean of the density and the covariance. Both this mean and
the covariance also need to be indexed by the when, the where and the
what.}

\subsubsection{Augmenting with Inducing Variables in Gaussian Processes}

\notes{To define our model we need to describe the relationship between the
fundamental variables, $\dataMappingVector$, and the inducing variables,
$\inducingVector$. This needs to be done in such a way that the inducing
variables are also Kolmogorov consistent. A straightforward way of
achieving this is through a joint Gaussian process model over the
inducing variables and the data mapping variables, so in other words we
define a Gaussian process prior over}
$$
\begin{bmatrix}\mappingFunctionVector \inducingVector\end{bmatrix} \sim \gaussianDist{\mathbf{m}}{\kernelMatrix}
$$
\notes{where the covariance matrix has a block form,}
$$
\kernelMatrix = \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector\mappingFunctionVector} & \kernelMatrix_{\mappingFunctionVector\inducingVector} \ \kernelMatrix_{\inducingVector\mappingFunctionVector} & \kernelMatrix_{\inducingVector\inducingVector}\end{bmatrix}
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


\subsubsection{The Mean Function}


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
used in a *generalised* linear model through a link function to
represent a rate or risk of disease [@Diggle:somewhere]. The
covariates should *co-vary* (or move together) with the response
variable. Appropriate covariates for malaria incidence rate might
include known influencers of the disease. For example if we are dealing
with *malaria* then we might expect disease rates to be influenced by
altitude, average temperature, average rainfall, local distribution of
prophylactic measures (such as nets) etc. The covariance of the Gaussian
process then has the role of taking care of the *residual* variance in
the data: the data that is not explained by the mean function, i.e. the
variance that cannot be explained by the parametric model. In a disease
mapping model it makes sense to assume that these residuals may not be
independent. An underestimate of disease at one spatial location, may
imply an underestimate of disease rates at a nearby location. The
mismatch between the observed disease rate and that predicted by
modeling the relationship with the covariates through the mean function
is then given by the covariance function.}

\notes{The modeling philosophy in machine learning is somewhat different from
that followed in traditional statistics. In machine learning the aim is
often to be predictive, rather than explanatory. There is typically less
need for an interpretable model, and so the mean function is much less
rarely used. The objective is to predict the data entirely through the
covariance function. From the arguments we developed earlier about the
need for nonparametrics this makes a lot of sense. In particular if we
rely on the mean function to make our predictions and assume that the
covariance function is dealing with the residuals, then as we obtain
more data the parameters of the mean function will become better
determined. If the mean function does capture the majority of the
variance of our observations, then the role of the covariance function
will be reduced to capture only the variance of the residuals. But at
this point we are left with a model that is dominated by is parametric
part at the expense of its non parametric part. If the parameters have
become well determined then the uncertainty about future predictions
will be reduced. However, if we enter a novel domain (one where the
provenance of the data differs significantly from the data we observed
at training time) then we will still make very confident extrapolations
when predicting for the new data. For this reason in machine learning we
often prefer to leave out the mean function to ensure that the signal
variance is explained through non parametric part of the model rather
than the parametric mean function. In what follows we will drop the mean
function and focus only on the covariance function.}

\todo{Mention here an example of things going wrong? Or do a short run
of a mauna loa data to demonstrate, with a mean function included?}

\setupcode{import GPy
import pods}

\code{data = pods.util.datasets.mauna_loa()
kern = GPy.kern.Linear(1) + GPy.kern.RBF(1) + GPy.kern.Bias(1)
model = GPy.models.GPRegression(data['X'], data['Y'], kern)
#model.optimize()}


\plotcode{pb.plot(xlim}


\notes{So we *could* interpret Gaussian process models as approaches to dealing
with residuals}

\endif