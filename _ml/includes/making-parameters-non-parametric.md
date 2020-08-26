\ifndef{makingParametersNonParametric}
\define{makingParametersNonParametric}

\editme

\subsection{Making Parameters Nonparametric}

\notes{We will start by introducing a set of variables, $\inducingVector$, that
are finite dimensional. These variables will eventually be used to
communicate information between the training and test data, i.e. across
the TT channel.}
$$
p(\dataVector^*|\dataVector) = \int p(\dataVector^*|\inducingVector) q(\inducingVector|\dataVector) \text{d}\inducingVector
$$
\notes{where we have introduced a distribution over $\inducingVector$,
$q(\inducingVector|\dataVector)$ which is not necessarily the true
posterior distribution, indeed we typically derive it through a variational approximation (see e.g. @Titsias:variational09).}

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[2, 2],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)

pgm.add_node(daft.Node("y", r"$\dataVector$", 0.5, 0.5, fixed=False, observed=True))
pgm.add_node(daft.Node("u", r"$\inducingVector$", 0.5, 1.5, fixed=False))
pgm.add_edge("u", "y", directed=False)

pgm.render().figure.savefig("\diagramsDir/ml/u-to-y.svg", transparent=True)}

\figure{\includediagram{\diagramsDir/ml/u-to-y}{40%}}{Augmenting the variable space with a set of latent *inducing vectors*. The graphical model represents the factorization of the distribution into the form $\int p(\dataVector|\inducingVector)p(\inducingVector)\text{d}\inducingVector$}{u-to-y}

\notes{In Figure \ref{u-to-y} we have augmented our simple graphical model augmented with a vector $\inducingVector$ which we
refer to as inducing variables. Note that the model is still totally
general because $p(\dataVector, \inducingVector)$ is an augmented
variable model and the original $p(\dataVector)$ is easily recovered by
simple marginalization of $\inducingVector$. So we haven't yet made any
assumptions about our data, our model is still correct, but useless.}

\notes{The model we've introduced now looks somewhat like the
parametric model we argued against in the previous section,}
$$
p(\dataVector^* | \dataVector)=\int
p(\dataVector^*|\parameterVector)p(\parameterVector|\dataVector)\text{d}\parameterVector.
$$ 
\notes{What's going on here? Is there going to be some kind of
parametric/nonparametric 3 card trick where with sleight of hand we
are trying to introduce a parametric model? Well clearly not, because
I've just given the game away. But I believe there are some important
differences to the traditional approach for parameterizing a
model. Philosophically, our variables $\inducingVector$ are variables
that augment the model. We have not yet made any assumptions by
introducing them. Normally, parameterization of the model instantiates
assumptions, but this is not happening here. In particular note that
we have *not* assumed that the training data factorize given the
inducing variables. Secondly, have not specified the dimensionality of
$\inducingVector$ (i.e. the size of the TT channel) at *design*
time. We are going to allow it to change at *run* time. We will do
this by ensuring that the inducing variables also obey Kolmogorov
consistency. In particular we require that If we build a joint density
as follows:} \begin{align*} p(\dataVector,
\inducingVector|\numInducing^*, \numData^*) = \int p(\dataVector^*,
\dataVector, \inducingVector^*, \inducingVector) \text{d}\dataVector^*
\text{d}\inducingVector^*, \end{align*} \notes{where $\inducingVector$
are the inducing variables we choose might choose to instantiate at
any given time (of dimensionality $\numInducing$) and
$\inducingVector^*$ is the $\numInducing^*$ dimensional pool of future
inducing variables we have *not yet* chosen to instantiate (where
$\numInducing^*$ could be infinite). Our new Kolmogorov consistency
condition requires that} $$ p(\dataVector,
\inducingVector|\numInducing^*,\numData^*) = p(\dataVector,
\inducingVector).  $$ \notes{It doesn't need to be predetermined at
*design time* because we allow for the presence of a (potentially
infinite) number of inducing variables $\inducingVector^*$ that we may
wish to *later* instantiate to improve the quality of our model. In
other words, it is very similar to the parametric approach, but now we
have access to a future pool of additional parameters,
$\inducingVector^*$ that we can call upon to increase the bandwidth of
the TT channel as appropriate. In parametric modelling, calling upon
such parameters has a significant effect on the likelihood of the
model, but here these variables are auxiliary variables that will
*not* affect the likelihood of the model. They merely effect our
ability to approximate the true bandwidth of the TT channel. The
quality of this approximation can be varied at run time. It is not
necessary to specify it at design time. This gives us the flexibility
we need in terms of modeling, whilst keeping computational complexity
and memory demands manageable and appropriate to the task at hand.}

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[2, 2],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)

pgm.add_node(daft.Node("y", r"$\dataVector$", 0.5, 0.5, fixed=False, observed=True))
pgm.add_node(daft.Node("u", r"$\inducingVector$", 0.5, 1.5, fixed=False))
pgm.add_node(daft.Node("ystar", r"$\dataVector^*$", 1.5, 0.5, fixed=False))
pgm.add_node(daft.Node("ustar", r"$\inducingVector^*$", 1.5, 1.5, fixed=False))

pgm.add_edge("u", "y", directed=False)
pgm.add_edge("ustar", "y", directed=False)
pgm.add_edge("u", "ustar", directed=False)
pgm.add_edge("ystar", "y", directed=False)
pgm.add_edge("ustar", "ystar", directed=False)
pgm.add_edge("u", "ystar", directed=False)

pgm.render().figure.savefig("\diagramsDir/ml/u-to-y-ustar-to-y.svg", transparent=True)}
 
\figure{\includediagram{\diagramsDir/ml/u-to-y-ustar-to-y}{30%}}{We can also augment the graphical model with data that is only seen at 'run time', or 'test data'. In this case we use the superscript of $*$ to indicate the test data. This graph represents the interaction between data we've seen, $\dataVector$, and data we've yet to see, $\dataVector^*$ as well as the augmented variables $\inducingVector$ and $\inducingVector$, $p(\dataVector) = \int p(\dataVector, \dataVector^*, \inducingVector, \inducingVector^*) \text{d}\dataVector^* \text{d}\inducingVector \text{d}\inducingVector^*$. As the fully connected graph implies we are making no assumptions about the data.}{u-to-y-ustar-to-y}

\notes{Adding in the test data and the inducing variables we have not yet
chosen to instantiate (Figure \ref{u-to-y-ustar-to-y}). Here we see that we still haven't defined any
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
variables. For example if we took $\mappingFunction_{12,345}$ to be the
height of Tom Cruise and $\mappingFunction_{23,789}$ to be the height of
Penelope Cruz then we might take for an observation a binary value
indicating the relative heights, so
$\dataScalar_{72,394} = \mappingFunction_{12,345} < \mappingFunction_{23,789}$.
The fundamental variable is an artificial construct, but it can prove to
be a useful one. In particular we'd like to assume that the
relationship between our observations, $\dataVector$ and the fundamental
variables, $\mappingFunctionVector$ might factorize in some way. In the
framework we think of this relationship, given by
$p(\dataVector|\inducingVector)$ as the *likelihood*. We can ensure that
assuming the likelihood factorizes does not at all reduce the generality
of our model, by forcing the distribution over the fundamentals,
$p(\mappingFunctionVector)$ to also be Kolmogorov consistent. This
ensures that in the case where the likelihood is fully factorized
over $\numData$ the model is still general if we allow the factors of
the likelihood to be Dirac delta functions suggesing that
$\dataScalar_i = \mappingFunction_i$. Since we haven't yet specified
any forms for the probability distributions this *is* allowed and
therefore the formulation is still totally general.}
$$
p(\dataVector|\numData^*) = \int p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector, \mappingFunctionVector^*)\text{d}\mappingFunctionVector \text{d}\mappingFunctionVector^*
$$
\notes{and since we enforce Kolmogorov consistency, we have}
$$
p(\dataVector|\numData^*) = p(\dataVector).
$$

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}
\plotcode{pgm = daft.PGM(shape=[2, 3],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)

pgm.add_node(daft.Node("y", r"$\dataVector$", 0.5, 0.5, fixed=False, observed=True))
pgm.add_node(daft.Node("f", r"$\mappingFunctionVector$", 0.5, 1.5, fixed=False))
pgm.add_node(daft.Node("u", r"$\inducingVector$", 0.5, 2.5, fixed=False))
pgm.add_node(daft.Node("ustar", r"$\inducingVector^*$", 1.5, 2.5, fixed=False))

pgm.add_edge("u", "f", directed=False)
pgm.add_edge("f", "y")
pgm.add_edge("ustar", "f", directed=False)
pgm.add_edge("u", "ustar", directed=False)

pgm.render().figure.savefig("\diagramsDir/ml/u-to-f-to-y-ustar-to-f.svg", transparent=True)}
 
\figure{\includediagram{\diagramsDir/ml/u-to-f-to-y-ustar-to-f}{30%}}{We introduce the fundamental variable $\mappingFunctionVector$ which sits between $\inducingVector$ and $\dataVector$.}{u-to-f-to-y-ustar-to-f} 

\notes{Now we assume some form of factorization for our data observations,
$\dataVector$, given the fundamental variables,
$\mappingFunctionVector$, so that we have}
$$
p(\dataVector|\mappingFunctionVector) = \prod_{i} p(\dataVector^i| \mappingFunctionVector^i)
$$
\notes{so that we have subsets of the data $\dataVector^i$ which are dependent
on subsets of the fundamental variables, $\mappingFunction$. For
simplicity of notation we will assume a factorization across the entire
data set, so each observation, $\dataScalar_i$, has a single underlying
fundamental variable, $\mappingFunction_i$, although more complex
factorizations are also possible and can be considered within the
analysis.}
$$
p(\dataVector|\mappingFunctionVector) = \prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i)
$$

\setupplotcode{import daft

from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[2, 3],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)
reduce_alpha={"alpha": 0.3}
pgm.add_node(daft.Node("y", r"$\dataScalar_i$", 0.5, 0.5, fixed=False, observed=True))
pgm.add_node(daft.Node("f", r"$\mappingFunction_i$", 0.5, 1.5, fixed=False))
pgm.add_node(daft.Node("u", r"$\inducingVector$", 0.5, 2.5, fixed=False))
pgm.add_node(daft.Node("ustar", r"$\inducingVector^*$", 1.5, 1.5, fixed=False, plot_params=reduce_alpha))
pgm.add_plate([0.125, 0.125, 0.75, 1.75], label=r"$i=1\dots N$", fontsize=18)

pgm.add_edge("u", "f", directed=False)
pgm.add_edge("f", "y")
pgm.add_edge("ustar", "f", directed=False, plot_params=reduce_alpha)
pgm.add_edge("u", "ustar", directed=False, plot_params=reduce_alpha)

pgm.render().figure.savefig("\diagramsDir/ml/u-to-f_i-to-y_i-ustar-to-f.svg", transparent=True)}
        

\figure{\includediagram{\diagramsDir/ml/u-to-f_i-to-y_i-ustar-to-f}{30%}}{The relationship between $\mappingFunctionVector$ and $\dataVector$ is assumed to be factorized, which we indicate here using plate notation, $p(\dataVector) = \int \prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i) p(\mappingFunctionVector | \inducingVector, \inducingVector^*) p(\inducingVector, \inducingVector^*)\text{d}\inducingVector \text{d}\inducingVector^*$.}{u-to-f_i-to-y_i-ustar-to-f} 

\notes{We now decompose, without loss of generality, our joint distribution
over inducing variables and fundamentals into the following parts}
$$
p(\inducingVector, \mappingFunctionVector) = p(\mappingFunctionVector|\inducingVector)p(\inducingVector),
$$
\notes{where we assume that we have marginalized $\mappingFunctionVector^*$ and
$\inducingVector^*$.}


\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[2, 3],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)
reduce_alpha={"alpha": 0.3}
pgm.add_node(daft.Node("y", r"$\dataScalar_i$", 0.5, 0.5, fixed=False, observed=True))
pgm.add_node(daft.Node("f", r"$\mappingFunction_i$", 0.5, 1.5, fixed=False))
pgm.add_node(daft.Node("u", r"$\inducingVector$", 0.5, 2.5, fixed=False))
pgm.add_node(daft.Node("ustar", r"$\inducingVector^*$", 1.5, 1.5, fixed=False, plot_params=reduce_alpha))
pgm.add_plate([0.125, 0.125, 0.75, 1.75], label=r"$i=1\dots N$", fontsize=18)

pgm.add_edge("f", "y")
pgm.add_edge("u", "f")
pgm.add_edge("ustar", "f", plot_params=reduce_alpha)

pgm.render().figure.savefig("\diagramsDir/ml/u-to-f_i-to-y_i.svg", transparent=True)}

\figure{\includediagram{\diagramsDir/ml/u-to-f_i-to-y_i}{30%}}{The model with future inducing points marginalized $p(\dataVector) = \int \prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i) p(\mappingFunctionVector | \inducingVector) p(\inducingVector)\text{d}\inducingVector$.}{u-to-f_i-to-y_i}

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[2, 3],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)
reduce_alpha={"alpha": 0.3}
pgm.add_node(daft.Node("y", r"$\dataScalar_i$", 0.5, 0.5, fixed=False, observed=True))
pgm.add_node(daft.Node("f", r"$\mappingFunction_i$", 0.5, 1.5, fixed=False))
pgm.add_node(daft.Node("u", r"$\inducingVector$", 0.5, 2.5, fixed=True))
pgm.add_node(daft.Node("ustar", r"$\inducingVector^*$", 1.5, 1.5, fixed=True, plot_params=reduce_alpha))
pgm.add_plate([0.125, 0.125, 0.75, 1.75], label=r"$i=1\dots N$", fontsize=18)

pgm.add_edge("f", "y")
pgm.add_edge("u", "f")
pgm.add_edge("ustar", "f", plot_params=reduce_alpha)

pgm.render().figure.savefig("\diagramsDir/ml/given-u-to-f_i-to-y_i.svg", transparent=True)}

\figure{\includediagram{\diagramsDir/ml/given-u-to-f_i-to-y_i}{30%}}{The model conditioned on the inducing variables $p(\dataVector|\inducingVector, \inducingVector^*) = \int\prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i) p(\mappingFunctionVector|\inducingVector, \inducingVector^*)\text{d}\mappingFunctionVector$.}{given-u-to-f_i-to-y_i}

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[2, 3],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)
reduce_alpha={"alpha": 0.3}
pgm.add_node(daft.Node("y", r"$\dataScalar_i$", 0.5, 0.5, fixed=False, observed=True))
pgm.add_node(daft.Node("f", r"$\mappingFunction_i$", 0.5, 1.5, fixed=False))
pgm.add_node(daft.Node("theta", r"$\parameterVector$", 0.5, 2.5, fixed=True))
e, plot_params=reduce_alpha))
pgm.add_plate([0.125, 0.125, 0.75, 1.75], label=r"$i=1\dots N$", fontsize=18)

pgm.add_edge("f", "y")
pgm.add_edge("theta", "f")

pgm.render().figure.savefig("\diagramsDir/ml/given-theta-to-f_i-to-y_i.svg", transparent=True)}

\figure{\includediagram{\diagramsDir/ml/given-theta-to-f_i-to-y_i}{30%}}{The model as a classical parametric model with independence across data points indexed by $i$ that is conditional on parameters $\parameterVector$, $p(\dataVector|\parameterVector) = \int\prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i) p(\mappingFunctionVector|\parameterVector)\text{d}\mappingFunctionVector$. The model is graphically the same as the nonparametric variant but here the dimension of $\parameterVector$ has to be fixed for Kolmogorov consistency, in the inducing vector variant the dimension of $\inducingVector$ can vary.}{given-theta-to-f_i-to-y_i}

In Figure \ref{given-theta-to-f_i-to-y_i} we visualise the graphical model of a classical parametric form. This model is very general, the deep neural network models for supervised learning tasks can be seen as variants of this model with very large dimensions for the parameter vector $\parameterVector$. 

\endif
