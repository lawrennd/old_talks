---
title: Modelling Things
abstract: >
  Machine learning solutions, in particular those based on deep
  learning methods, form an underpinning of the current revolution in
  “artificial intelligence” that has dominated popular press headlines
  and is having a significant influence on the wider tech agenda.
  
  In this talk I will give an overview of where we are now with
  machine learning solutions, and what challenges we face both in the
  near and far future. These include practical application of existing
  algorithms in the face of the need to explain decision making,
  mechanisms for improving the quality and availability of data,
  dealing with large unstructured datasets.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
venue: IEEE RO-MAN Conference Workshop
geometry: ['a4paper', 'margin=1in']
date: 2020-09-04
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

\include{_ml/includes/ml-and-statistics-interface.md}
\include{_data-science/includes/happenstance-data.md}

\notes{Professor Efron's paper does an excellent job a summarising the
range of predictive models that now lie at our disposal, but of
particular interest are deep neural networks. This is because they go
beyond the traditional notions of what generalisation is or rather,
what it has been, to practitioners on both the statistical and machine
learning sides of the fence.}

\include{_ml/includes/deep-models-and-generalization.md}

\notes{An excellent characterisation of generalization is normally
given by the bias-variance dilemma. The bias-variance decomposition
for regression models separates the generalization error into two
components [@Geman:biasvariance92].}

\include{_ml/includes/bias-variance-dilemma.md}

\include{_ml/includes/double-descent.md}

\notes{As Professor Efron points out, modern machine learning models
are often fitted using many millions of data points. The most extreme
example of late is known as GPT-3. This neural network model, known as
a Transformer, has in its largest form 175 billion parameters. The
model was trained on a data set containing 499 billion tokens (about 2
Terrabytes of text). Estimates suggest that the model costs around
$4.5 million dollars to train (see e.g. @Li:openai20).}

\include{_ml/includes/empirical-effectiveness-of-deep-learning.md}

\include{_ml/includes/new-methods-required.md}

\include{_ml/includes/massively-missing-data.md}

\notes{Machine learning involves taking data and combining it with a model in
order to make a prediction. The data consist of measurements recorded
about the world around us. A model consists of our assumptions about how
the data is likely to interrelate, typical assumptions include
smoothness. Our assumptions reflect some undelying belief about the
regularities of the universe that we expect to hold across a range of
data sets.}
$$
\text{data} + \text{model} \rightarrow \text{prediction}
$$
\notes{From my perspective, the model is where all the innovation in machine
learning goes. The etymology of the data indicates that it is given
(although in some cases, such as active learning, we have a choice as to
how it is gotten), our main control is over the model. This is the key
to making good predictions. The model is a mathematical abstraction of
the regularities of the universe that we believe underly the data as
collected. If the model is chosen well we will be able to interpolate
the data and precit likely values of future data points. If it is chosen
badly our predictions will be overconfident and wrong.}

\include{_ml/includes/model-vs-algorithm.md}

\include{_ml/includes/is-my-model-useful.md}

\include{_ml/includes/big-data-health-motivation.md}

\subsubsection{Uncertainty in Parameters}

\notes{If the parameters are badly determined, then small fluctuations in the
data set lead to larger fluctuations in prediction. One approach to this
problem is to build models in which the parameters are well determined.
For teh independence across data points case, this involves having many
observations (large $\numData$) relative to the number of parameters
(which often scales with $\dataDim$). This motivates the issues of the
large $\dataDim$ small $\numData$ domain, where the conditions are
reversed. Of course, from a modelling perspective this issue is
trivially solved by assuming independence across the $\dataDim$ data
dimensions and allowing the parameters to scale with the number of data
$\numData$. This is a characteristic exhibited, for example by the
Gaussian process latent variable model [@Lawrence:pnpca05] which in standard form assumes independence
arcross $\dataDim$ for high dimensional data and associates each data
point with a latent variable that is treated as a parameter. In
[@Lawrence:unifying12] I argued that the succesful class of *spectral*
approaches to dimensionality reduction (e.g.
 LLE @Roweis:lle00 and maximum variance unfolding @Weinberger:learning04, which are widely
applied in the large $\dataDim$ small $\numData$ domain, also have a
probabilistic intepretation where the underlying likelihood factorizes
across data dimensions. Regardless of our choice of factorization
though, we are still making the same claim: a particular vector, or
matrix, of parameters is suffcient for us to consider that the data
independent, either across features or data points.}


\subsubsection{Massively Missing Data}

\notes{I'd like to argue that the separation of the data into features and
data points is rather arbitrary. I believe it stems from the origin of
the field of statistics, where the intention was to make a strong
scientific claim based on numbers take from a *table* of data. A table
naturally lends itself towards a matrix form. In these data a
statistical design normally involved measuring a fixed number of
*features* for a perhaps variable number of *items*. The objective is to
find sufficient number of items so that you can make strong claims about
which features are important. For example, does smoking correlate with
lung cancer? This explains the desire to write down the data as a matrix
$\dataMatrix$. I think this view of data, whilst important at the time,
is outdated when considering modern big data problems.}


\notes{The modern data analysis challenge is very different. We receive
streaming data of varying provenance. If each number we receive is given
by an observation $\dataScalar_i$, where $\dataScalar_i$ could be in the
natural numbers, the real numbers or binary or in any processable form,
then $\dataScalar_{17}$ might be the price of a return rail fair from
Sheffield to Oxford on 6th February 2014, whilst $\dataScalar_{29}$
might be the number of people on the 8:20 train that day, but
$\dataScalar_{72,394}$ could be the temperature of the Atlantic ocean on
23rd August 2056 at a point on the artic circle midway between Greenland
and Norway. When we see data in this form, we realize that most of the
time we are missing most of the data. This leads to the idea of *massive
missing data*. Contrast this situation with that traditionally faced in
missing data where a table of values, $\dataMatrix$, might have 10%-50%
of the measurements missing, perhaps due to problems in data collection.
I'd argue that if we are to model complex processes (such as the brain,
or the cell, or human health) then almost all the data is missing.}

\setupplotcode{import daft}
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[1, 1],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)

pgm.add_node(daft.Node("y", r"$\dataVector$", 0.5, 0.5, fixed=False))

pgm.render().figure.savefig("\diagramsDir/ml/y-only-graph.svg", transparent=True)}

\plotcode{
% Define nodes
\draw node[obs] (y) {$\dataVector$};
\end{tikzpicture}
%\end{figure}
}

\figure{\includediagram{\diagramsDir/ml/y-only-graph.svg}{30%}}{The most general graphical model. It makes no assumptions about conditional probability relationships between variables in the vector $\dataVector$.}{y-only-graph}

\notes{A model that's not wrong, just not useful. I like graphical
representations of probabilistic models and this is my favourite graph.
It is the most simple but also the most general. It says that all the
data in our vector $\dataVector$ is governed by an unspecified
probability disribution $p(\dataVector)$. Graphical models normally
express the conditional independence relationships in the data, with
this graph we are not a priori considering any such relationships. This
is the most general model (it includes all factorized models as special
cases). It is not wrong, but since it doesn't suggest what the next
steps are or give us any handles on the problem it is also not useful.}


\notes{This is the nature of modern streaming data, what has been called big
data, although in the UK it looks like that term will gain a more
diffuse meaning now that the government has associated a putative 189
billion pounds of funding to it. But the characteristic of massive
missing data is particularly obvious when we look at clinical domains.
EMIS, a Yorkshire based provider of software to General Practitioners,
has 39 million patient records. When we consider clinical measurements,
we need to build models that not only take into account all current
clinical tests, but all tests that will be invented in the future. This
leads to the idea of massive missing data. The classical statistical
table of data is merely the special case where someone has filled in a
block of information.}


\notes{To deal with massively missing data we need to think about the
*Kolmogorov consistency* of a process. Let me introduce Kolmogorov
consistency by way of an example heard from Tony O'Hagan, but one that
he credits originally to Michael Goldstein. Imagine you are on jury
duty. You are asked to adjudicate on the guilt or innocence of Lord
Safebury, and you are going to base your judgement on a model that is
weighing all the evidence. You are just about to pronounce your decision
when a maid comes running in and shouts \"He didn't do it! He didn't
do it!\". The maid wasn't on the witness list and isn't accounted for
in your model. How does this effect your inference? The pragmatists
answer might be: not at all, because the maid wasn't in the model. But
in the interests of justice we might want to include this information in
our inference process. If, as a result of the maid's entry, we now
think it is less likely that Lord Safebury committed the crime, then
necessarily every time that the (unannounced) maid doesn't enter the
room we have to assume that it is more likely that Safebury commited the
crime (to ensure that the conditional probability of guilt given the
maid's evidence normalizes. But we didn't know about the maid, so how
can we account for this? Further, how can we account for all possible
other surprise evidence, from the announced butlers, gardners,
chauffeurs and footmen? Kolmogorov consistency says that the net effect
of marginalizing for all these potential bits of new information is
null. It is a particular property of the model. Making it (only
slightly) more formal, we can consider Kolmogorov consistency as a
marginalization property of the model. We take the $\numData$
dimensional vector, $\dataVector$, to be an (indexed) vector of all our
instantiated observations of the world that we have *at the current
time*. Then we take the $\numData^*$ dimensional vector, $\dataVector^*$
to be the observations of the world that we are *yet to see*. From the
sum rule of probability we have}
\begin{align*} 
p(\dataVector|\numData^*) = \int p(\dataVector, \dataVector^*) \text{d}\dataVector^*,
\end{align*}
\notes{where the dependence of the marginal distribution for $\dataVector$
aries from the fact that we are forming an $\numData^*$ dimensional
integral over $\dataVector^*$. If our distribution is Kolmogorov
consistent, then we know that the distribution over $\dataVector$ is
*independent* of the value of $\numData^*$. So in other words
$p(\dataVector|\numData*)=p(\dataVector)$. So Kolmogorov consistency
says that the form of $p(\dataVector)$ remains the same *regardless* of
the number of observations of the world that are yet to come.}

\subsection{Parametric Models}

\notes{We can achieve Kolomogrov consistency almost trivially in a parametric
model if we assume that the probability distribution is independent
given the parameters. Then the property of being closed under
marginalization is trivially satisfied through the independence,}
\begin{align*}
p(\dataVector, \dataVector^*) = \int\prod_{i=1}^\numData p(\dataScalar_{i} |
\boldsymbol{\theta})\prod_{i=1}^{\numData^*}p(\dataScalar^*_i|\boldsymbol{\theta})
p(\paramVector) \text{d}\paramVector,
\end{align*}
\notes{which allows us to marginalize for all future data leaving a joint
distribution which isn't dependent on $\numData^*$ because each future
data point can be marginalized independently.}
\begin{align*}
p(\dataVector) = \int \prod_{i=1}^\numData
p(\dataScalar_{i} |
\boldsymbol{\theta})\prod_{i=1}^{\numData^*} \int
p(\dataScalar^*_i|\boldsymbol{\theta})
\text{d}\dataScalar^*_i p(\paramVector).
\text{d}\paramVector
\end{align*}
\notes{But, as we've already argued, this involves an assumption that is often
flawed in practice. It is unlikely that, in a complex model, we will be
able to determine the parameter vector well enough, given limited data,
for us to truly believe that all the information about the training data
that is required for predicting the test data could be passed through a
fixed length parameter vector. This is what this independence assumption
implies. If we consider that the model will also be acquiring new data
at run time, then there is the question of hot to update the parameter
vector in a consistent manner, accounting for new information, e.g. new
clinical results in the case of personalized health.}

\notes{Conversely, a general assumption about independence across *features*
would lead to models which *don't* exhibit *Komlogorov consistency*. In
these models the dimensionality of the test data, $\dataVector^*$,
denoted by $\numData^*$ would have to be fixed and each
$\dataScalar^*_i$ would require marginalization. So the nature of the
test data would need to be known at model *design* time.}

\subsection{Parametric Bottleneck}

\notes{In practice Bayesian methods suggest placing a prior over
$\boldsymbol{\theta}$ and using the posterior,
$p(\boldsymbol{\theta}|\dataVector)$ for making predictions.}
\begin{align*} 
p(\dataVector^*|\dataVector) = \int \prod_i p(\dataScalar_i^* | \boldsymbol{\theta})p(\boldsymbol{\theta}|\dataVector)\text{d}\boldsymbol{\theta}.
\end{align*}
\notes{We have a model that obeys Kolmogorov consistency, and is sophisticated
enough to represent the behaviour of a very: it may well require a large
number of parameters. One way of seeing the requirement for a large
number of parameters is to look at how we are storing information from
the training data to pass to the test data. The sum of all our knowledge
about the training data is stored in the conditional distribution of the
parameters given the training data, Uncertainty complex systA key design
time problem is the *parametric bottleneck*. If we choose the number of
parameters at design time, but the system turns out to be more
complicated that we expected, we need to design a new model to deal with
this complexity. The communication between the training data and the
test data is like an information channel. This TT channel has a
bandwidth that is restricted by our choice of the dimensionality of
$\boldsymbol{\theta}$ at *design* time. This seems foolish. Better to
ensure we choose a model that allows for that channel to be potentially
infinite. This implies a non-parametric approach. Our prior over
$\boldsymbol{\theta}$ should be *non parametric*.}
$$
p(\paramVector | \dataVector),
$$
\notes{which, as we argued above, allows us to retain the necessary sense of
uncertainty about the parameters that is required in a very complex
system when we have seen relatively little data. How much information
can we store, then, about the training data? The information gain from
the training data is given by the Kullback Leibler divergence between
our prior distribution and our posterior distribution.}
$$
\KL{p(\paramVector|\dataVector)}{p(\paramVector)}
$$
\notes{This is the information gained, measured in 'nats' if we use natural
logarithms, but it could equally be measured in bits, about our
parameters having observed the training data. In the case that our
likelihood is log concave[^3] then this information gain provably will increase, with every
observed data point. How much information we gain will depend on the
likelihood associated with each data $\dataScalar_i$. This Kullback
Leibler divernece has an infomration theoretic interpretation as a
communication channel passing information from the training data to the
test data. From an information theoretic perspective, the channel
bandwidth is controlled by the dimensionality of the parameter vector
$\dataVector$ and the form of the prior $p(\paramVector)$.

[^3]: This is a definite constraint on the
model, there are many very reasonable likelihoods that are not log
concave.}


\subsection{The Non-parametric Challenge}

\notes{We have argued that we want models that are unconstrained, at design
time, by a fixed bandwidth for the communication between the training
data, $\dataVector$, and the test data, $\dataVector^*$ and that the
answer is to be non parameteric. By non-parametric we are proposing
using classes of models for which the conditional distribution,
$p(\dataVector^*|\dataVector)$ is not decomposable into the expectation
of $p(\dataVector^*|\paramVector)$ under the posterior distribution of
the parameters, $p(\paramVector|\dataVector)$ for any fixed length
parameter vector $\paramVector$. We don't want to impose such a strong
constraint on our model at *design time*. Our model may be required to
be operational for many years and the true complexity of the system
being modeled may not even be well understood at *design time*. We must
turn to paradigms that allow us to be adaptable at *run time*. Non
parametrics provides just such a paradigm, because the effect parameter
vector increases in size as we observe more data. This seems ideal, but
it also presents a problem.}

\notes{Human beings, despite are large, interconnected brains, only have finite
storage. It is estimated that we have between 100 and 1000 trillion synapses in our brains. Similar for digital computers, even the GPT-3 model is restricted to 175 billion parameters. So we need to assume that we can
only store a finite number of things about the data $\dataVector$. This
seems to push us back towards non-parametric models. Here, though, we
choose to go a different way. We choose to introduce a set of auxiliary
variables, $\inducingVector$, which are $\numInducing$ in length. Rather
than representing the non parametric density directly, we choose to
focus on storing information about $\inducingVector$. By storing
information about these variables, rather than storing all the data
$\dataVector$ we hope to get around this problem. In order for us to be
non parametric about our predictions for $\dataVector*$ we must
condition on all the data, $\dataVector$. We can't any longer store an
intermediate distribution to represent our sum knowlege,
$p(\paramVector|\dataVector)$. Such an intermediate distribution is a
finite dimensional object, and non-parametrics implies that we cannot
store all the information in a finite dimensional distribution. This
presents a problem for real systems in practice. We are now faced with a
compromise, how can we have a distribution which is flexible enough to
respond at *run time* to unforeseen complexity in the training data?
Yet, simultaneously doesn't require unbounded storage to retain all the
information in the training data? We will now introduce a perspective on
variational inference that will allow us to retain the advantages of
both worlds. We will construct a parametric approximation to the true
non-parametric conditional distribution. But, importantly, whilst this
parametric approximation will suffer from the constraints on the
bandwidth of the TT channel that drove us to non-parametric models in
the first place, we will be able to change the number of parameters at
*run time* not simply at design time.}

\subsubsection{The Multivariate Gaussian: Closure Under Marginalization}

\notes{Being closed under marginalization is a remarkable property of our old
friend the multivariate Gaussian distribution (old friends often have
remarkable properties that we often take for granted, I think this is
particularly true for the multivariate Gaussian). In particular, if we
consider a joint distribution across $p(\dataVector, \dataVector^*)$,
then the covariance matrix of the marginal distribution for the subset
of variables, $\dataVector$, is unaffected by the length of
$\dataVector^*$. Taking this to its logical conclusion, if the length of
the data, $\dataVector$, is $\numData=2$. Then that implies that the
covariance between $\dataVector$, as defined by $\kernelMatrix$, is only
a $2\times 2$ matrix, and it can only depend on the indices of the two
data points in $\dataVector$. Since this covariance matrix must remain
the same for any two values *regardless* of the length of $\dataVector$
and $\dataVector^*$ then the value of the elements of this covariance
must depend only on the two indices associated with $\dataVector$.}

\notes{Since the covariance matrix is specified pairwise, this implies that the covariance matrix must be dependent only  on the index
of the two observations $\dataScalar_i$ and $\dataScalar_j$ for which
the covariance is being computed. In general we can also think of this
index as being infinite: it could be a spatial or temporal location.}
\begin{align*} 
p(\dataVector) = \int p(\dataVector, \dataVector^*)
\text{d}\dataVector^*=
\frac{\exp\left(\begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}^\top\begin{bmatrix}\kernelMatrix &
\kernelMatrix_*\ \kernelMatrix_*^\top &
\kernelMatrix_{**}\end{bmatrix}^{-1} \begin{bmatrix}\dataVector
\dataVector^*\end{bmatrix}\right)}{\int
\exp\left(\begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}^\top\begin{bmatrix}\kernelMatrix &
\kernelMatrix_*\ \kernelMatrix_*^\top &
\kernelMatrix_{**}\end{bmatrix}^{-1} \begin{bmatrix}\dataVector
\dataVector^*\end{bmatrix}\right) \text{d}\dataVector
\text{d}\dataVector^*} = \mathcal{N}(\mathbf{0} |\kernelMatrix),
\end{align*}
\notes{where each $\dataScalar_i$ is now defined across the real line, and the
dimensionality of $\dataVector*$ is irrelevant. Prediction consists of
conditioning the joint density on $\dataVector^*$. So for any new value
of $\dataVector^*$, given its index we compute
$p(\dataVector^* | \dataVector)$.}


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


\subsubsection{Modelling $\mappingFunctionVector$}

\notes{In conclusion, for a non parametric framework, our model for
$\mappingFunctionVector$ is predominantly in the covariance function
$\kernelMatrix_{\mappingFunctionVector\mappingFunctionVector}$. This is
our data model. We are assuming the inducing variables are drawn from a
joint Gaussian process with $\mappingFunctionVector$. The cross
covariance between $\inducingVector$ and $\mappingFunctionVector$ is
given by $\kernelMatrix_{\mappingFunctionVector\inducingVector}$. This
gives the relationship between the function and the inducing variables.
There are a range of ways in which the inducing variables can interelate
with the}


\subsubsection{Illustrative Example}

\notes{For this illustrative example, we'll consider a simple regression
problem. The example is based on one that James Hensman showed at the
January 2014 Gaussian process winter school in his talk is on low rank
Gaussian process approximations.}


\subsection{Back to a Simple Regression Problem}

\notes{Here we set up a simple one dimensional regression problem. The input
locations, $\inputMatrix$, are in two separate clusters. The response
variable, $\dataVector$, is sampled from a Gaussian process with an
exponentiated quadratic covariance.}

\setupcode{import numpy as np
import GPy
from scipy import optimize
np.random.seed(101)}

\code{N = 50
noise_var = 0.01
X = np.zeros((50, 1))
X[:25, :] = np.linspace(0,3,25)[:,None] # First cluster of inputs/covariates
X[25:, :] = np.linspace(7,10,25)[:,None] # Second cluster of inputs/covariates

xlim = (-2,12)
ylim = (-4, 0)

# Sample response variables from a Gaussian process with exponentiated quadratic covariance.
k = GPy.kern.RBF(1)
y = np.random.multivariate_normal(np.zeros(N),k.K(X)+np.eye(N)*np.sqrt(noise_var)).reshape(-1,1)
scale = np.sqrt(np.var(y))
offset = np.mean(y)}

\notes{First we perform a full Gaussian process regression on the data. We
create a GP model, `m_full`, and fit it to the data, plotting the
resulting fit.}

\setuphelpercode{import matplotlib.pyplot as plt
from gp_tutorial import ax_default, meanplot, gpplot}

\helpercode{def plot_model_output(model, output_dim=0, scale=1.0, offset=0.0, ax=None, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2):
    if ax is None:
        fig, ax = plt.subplots(figsize=plot.big_figsize)
    ax.plot(model.X.flatten(), model.Y[:, output_dim]*scale + offset, 'r.',markersize=10)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    xt = plot.pred_range(model.X, portion=portion)
    yt_mean, yt_var = model.predict(xt)
    yt_mean = yt_mean*scale + offset
    yt_var *= scale*scale
    yt_sd=np.sqrt(yt_var)
    if yt_sd.shape[1]>1:
        yt_sd = yt_sd[:, output_dim]

    _ = gpplot(xt.flatten(),
               yt_mean[:, output_dim],
               yt_mean[:, output_dim]-2*yt_sd.flatten(),
               yt_mean[:, output_dim]+2*yt_sd.flatten(), 
               ax=ax)}



\code{m_full = GPy.models.GPRegression(X,y)
m_full.optimize() # Optimize parameters of covariance function}

\setupplotcode{import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='$x', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-full-gp.svg', 
                  transparent=True, frameon=True)}
				  
\figure{\includediagram{\diagramsDir/gp/sparse-demo-full-gp.svg}{60%}}{A full Gaussian process fit to the simulated data set.}{sparse-demo-full-gp}

\notes{Now we set up the inducing variables, $\inducingVector$. Each inducing
variable has its own associated input index, $\mathbf{Z}$, which lives
in the same space as $\inputMatrix$. Here we are using the true
covariance function parameters to generate the fit.}

\code{kern = GPy.kern.RBF(1)
Z = np.hstack(
        (np.linspace(2.5,4.,3),
        np.linspace(7,8.5,3)))[:,None]
m = GPy.models.SparseGPRegression(X,y,kernel=kern,Z=Z)
m.noise_var = noise_var
m.inducing_inputs.constrain_fixed()
#m.tie_params('.*variance')
#m.ensure_default_constraints()}

\displaycode{print(m) # why is it not printing noise variance correctly?}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='$x', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-constrained-inducing-6-unlearned-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-constrained-inducing-6-unlearned-gp}{60%}}{Sparse Gaussian process with six constrained inducing variables and parameters learned.}{sparse-demo-constrained-inducing-6-unlearned-gp}

\code{m.optimize()}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-constrained-inducing-6-learned-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-constrained-inducing-6-learned-gp}{60%}}{Sparse Gaussian process with six constrained inducing variables and parameters learned.}{sparse-demo-constrained-inducing-6-learned-gp}

\displaycode{print(m)}



\code{m.randomize()
m.inducing_inputs.unconstrain()
m.optimize()}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-unconstrained-inducing-6-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-unconstrained-inducing-6-gp}{60%}}{Sparse Gaussian process with six unconstrained inducing variables, initialized randomly and then optimized.}{sparse-demo-unconstrained-inducing-6-gp}

\notes{Now we will vary the number of inducing points used to form the approximation.}

\displaycode{m.Z.values}

\code{m.num_inducing=8
m.randomize()
M = 8

m.set_Z(np.random.rand(M,1)*12)

m.optimize()}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\diagramsDir/gp/sparse-demo-sparse-inducing-8-gp.svg', 
                  transparent=True, frameon=True)}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-sparse-inducing-8-gp}{60%}}{Sparse Gaussian process with eight inducing variables, initialized randomly and then optimized.}{sparse-demo-sparse-inducing-8-gp}

\displaycode{print(m.log_likelihood(), m_full.log_likelihood())}


\subsubsection{Uncertainty about the Provenance of the Data}

\notes{Provenance could include the time that the data was acquired, the
location that the data was acquired, even the 'type' of data that is
acquired. For example, in computer vision pixels are arriving from
different objects. We are uncertain about the provenance of the pixels
in terms of which *object* they are arriving from. The spatial location
of the object in the image. This uncertainty relates to uncertainty
about the covariance function. Unfortunately, it is not directly on the
covariance function itself, but relates to values through which the
covariance is nonlinearly related.}
\begin{align*} 
k(\dataVector, \dataVector^\prime) = \exp(-||\dataVector-\dataVector^\prime||^2) 
\end{align*}
\notes{These variables become *latent* or *confounders*.}

\notes{**Not sure about this**: Provenance of data is often finite. Consider a
diseased person. That person consists of a finite (if very large) state
vector. Of course the number of measurements we can make about that
person is infinite. But there are a set of fundamental limitations to
what can go wrong with the individual.}


\subsection{Ethics}


\notes{Ownership of data, returning it to the individual. In healthcare the
danger of confusing it with marketing, Laplace, and the utopian view of
data. Invalidity of insurance. How the results are presented to the
patient.}
