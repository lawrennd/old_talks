\ifndef{isMyModelUseful}
\define{isMyModelUseful}

\editme

\subsection{Is my Model Useful?}

\notes{In the first half of the 20th Century, the Bayesian approach was termed *inverse probability*. Fisher disliked the subjectivist nature of the approach [@Aldrich-fisher08] and introduced the term *Bayesian* in 1950 to distinguish these probabilities from the likelihood function [@Fisher-contributions50]. The word Bayesian has connotations of a strand of religious thinking or a cult.[^corfield] Whether Fisher was fully aware of this when he coined the term we cannot know, but Fisher ws certainly right that there is a tenet at the heart of most Bayesian work.}

[^corfield]: This was pointed out to me by Bernhard Sch\"olkopf, who by recollection credited the observation to the philosopher David Corfield. 

\notes{Many statisticians who criticise the Bayesian approach ask where the prior is coming from. But one might just as well ask, where does the likelihood come from? Or where does the link function come from? All of these are subjective modeling questions. The prior is not the problem. The challenge is providing modeling guarantees. The classical Bayesian approach provides guarantees, but only for the $\mathcal{M}$-closed domain [@Bernardo:bayesian94], where the *true* model is one of the models under consideration. This is the critical belief at the heart of the Church of Bayes: the doctrine of model correctness.}

\notes{The beauty of the Bayesian approach is that you don't have to have much imagination. You work as hard as possible with your models of probability distributions to represent the problem as best you understand it, then you work as hard as possible to approximate the posterior distributions of interest and estimate the marginal likelihoods and any corresponding Bayes's factors. If we have faith in the doctrine of model correctness, then we can pursue our modeling aims without the shadows of doubt to disturb us.}

\notes{Of course, now that software is provided to make these tasks easier you have more time to reflect on the fact that the entire premise of your approach is mistaken if you are in the $\mathcal{M}$-closed domain. When are we in this domain? According to @Box:science76, all the time.}

> All models are wrong, but some are useful

\notes{This important quote has become worn by overuse (like a favorite
sweater). Indeed, I most often see it quoted at the beginning of a talk in a way that confuses correlation with causality. Presentations proceed in the following way. 1) Here is my model. 2) It is wrong. 3) Here is George Box's quote. 4) My model is wrong, but it might be  might be useful. Sometimes I feel at stage 4) a confusion about the arrow of causality occurs, it feels to me that people are almost saying "*Because* my model is wrong it *might* be useful."}

\notes{Perhaps we should be more focusing on the quote from the same paper}

> the scientist must be alert to what is importantly wrong. It is inappropriate to be concerned about mice when there are tigers abroad. 
>
> @Box:science76

\notes{This quote was first highlighted to me by Richard Wilkinson. Let's have a think about
where the tigers might be in the domain of big data. To consider this,
let's first see what we can write down about our data that isn't
implicitly wrong. If we are interested in multivariate data we could
first write down our data as a *design matrix*}
$$
\text{data} = \mathbf{\dataMatrix} \in \Re^{\numData\times \dataDim}.
$$
Here we are assuming we have $\numData$ data points and $\dataDim$
features. As soon as we write down our data in this form it
invites particular assumptions about the data that may have been valid
in the 1930s, when there was more focus on survey data. Experimental designs 
stipulated a table of data with a specific set of hypotheses in mind. The data
naturally sat in a matrix. 

As soon as we write down our data in a
matrix form, $\dataMatrix\in \Re^{\numData\times \dataDim}$ it almost second nature 
to begin making factorization assumptions. In particular, an independence assumption across
the $\numData$ data points.}
\begin{align*}
p(\dataMatrix|\parameterVector) = \prod_{i=1}^\numData p(\dataVector_{i, :} | \boldsymbol{\theta})
\end{align*}
\notes{This factorization gives several advantages. It has a theoretical framing, that easily allows us
to show that by optimizing the resulting lieklihood, we are minimizing a sample based approximation to a
Kullback-Leibler divergence between our model and the true data generating density (see e.g. @Wasserman:all03). 
\begin{align*}
\log p(\dataMatrix|\parameterVector) =& \sum_{i=1}^\numData \log p(\dataVector_{i, :} | \boldsymbol{\theta}) + \text{const}
\approx & \int \Pr(\dataMatrix) \log \frac{p(\dataMatrix|\parameterVector)}{\Pr(\dataMatrix)}
\end{align*}
where \Pr(\dataMatrix) is the true data generating distribution.

From pragmatist's perspective, the assumption allows us to easily make predictions about new data
points given a parameter vector that is derived from the training data.
This assumption will generally be wrong, and also leads to concerns
about the parameters when $\numData<<\dataDim$, the so called \`large
$\dataDim$, small $\numData$' domain.}

\notes{I think that this is a wrongheaded way of thinking about modern data,
because in practice, $\dataDim$, doesn't really exist, at least not in
the sense that the above model implies we should treat it. It doesn't
exist as a static view of the data: $\dataDim$ is much more fluid than
the model above implies. Indeed, I'll argue below that rather than
increasing $\dataDim$ when we obtain a new feature about a data point,
we should be increasing $\numData$. That adding writing down our data in
matrix form, $\dataMatrix$, may even be constraining our thinking to
these factorized models. And the fact that the factorization is strong:
i.e. it assumes that all becomes independent given the parameters, it is
very often wrong. That is not to say that these factorization
assumptions are not useful, indeed we will make use of them below, but
they should *not* be the first thing we write down.}

\endif
