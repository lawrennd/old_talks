\ifndef{bigDataConsistency}
\define{bigDataConsistency}

\editme

\subsection{Big Data Consistency}

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
answer might be: "not at all, because the maid wasn't in the model." But
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
$\dataScalar^*_i$ would require marginalization. So, the nature of the
test data would need to be known at model *design* time.}

\endif
