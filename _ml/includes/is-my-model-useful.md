\ifndef{isMyModelUseful}
\define{isMyModelUseful}

\editme

\subsection{Is my Model Useful?}

\notes{In the first half of the 20th Century, the Bayesian approach was termed *inverse probability*. Fisher disliked the subjectivist nature of the approach [@Aldrich-fisher08] and introduced the term *Bayesian* in 1950 to distinguish these probabilities from the likelihood function [@Fisher-contributions50]. The word Bayesian has connotations of a strand of religious thinking or a cult.[^corfield] Whether Fisher was fully aware of this when he coined the term we cannot know, but Fisher ws certainly right that there is a tenet at the heart of most Bayesian work.}

[^corfield]: This was pointed out to me by Bernhard Sch\"olkopf, who by recollection credited the observation to the philosopher David Corfield. 

\notes{Many statisticians who criticise the Bayesian approach ask where the prior is coming from. But one might just as well ask, where does the likelihood come from? Or where does the link function come from? All of these are subjective modeling questions. The prior is not the problem. The challenge is providing modeling guarantees. The classical Bayesian approach provides guarantees, but only for the $\mathcal{M}$-closed domain [@Bernardo:bayesian94], where the *true* model is one of the models under consideration. This is the critical belief at the heart of the Church of Bayes: the doctrine of model correctness.}

\notes{The beauty of the Bayesian approach is that you don't have to have much imagination. You work as hard as possible with your models of probability distributions to represent the problem as best you understand it, then you work as hard as possible to approximate the posterior distributions of interest and estimate the marginal likelihoods and any corresponding Bayes's factors. If we have faith in the doctrine of model correctness, then we can pursue our modeling aims without the shadows of doubt to disturb us.

Bayesian approaches have a lot in common with more traditional regularization techniques. Ridge regression imposes L2 shrinkage on the model's weights and has an interpretation as the maximum a posteriori estimate of the Bayesian solution. For linear models the mathematics of the two approaches is strikingly similar, and they both assume stages of careful design of model/regularizer followed by either Bayesian inference or optimization. The situation with the new wave of overparameterized models is strikingly different.}

\subsubsection{Implicit Regularization}

\notes{The new wave of overparameterized machine learning methods are *not* making this conceptual separation between the model and the algorithm. Deep learning approaches are simple algorithmically, but highly complex mathematically. By this I mean that it is relatively simple to write code that creates algorithms for optimizing the neural network models, particularly with the wide availability of automatic differentiation software. But analyzing what these algorithms are doing mathematically is murch harder. Fortunately, insight can already be gained by considering overparameterized models in the *linear* paradigm.}

\notes{These analyses consider 'gradient flow' algorithms. A gradient flow is an idealization of the optimization where the usual stochastic gradient descent optimization [@Robbins:stoch51] is replaced with differential equations representing the idealized trajectory of a *batch* gradient descent approach. Under these analyses, highly overparameterized linear models can be shown to converge to the L2 norm solution (see e.g. @Soudry-implicit18). It seems that stacking layers of networks also has interesting effects, because even when *linear* models are stacked analysis of the learning algorithm indicates a tendency towards low rank linear solutions for the parameters [@Arora-convergence19]. These regularization approaches are known as *implicit* regularlization, because the regularization is implicit in the optimizer rather than explicitly declared by the model-designer. These theoretical insights have also proven useful in practice. @Arora-implicit19 show state-of-the-art performance for matrix factorization through exploiting implicit regularization in the domain of matrix factorization.}

\notes{Studying the implicit regularization of these modern overparameterized machine learning methods is likely to prove a fruitful avenue for theoretical investigation that will deliver deeper understanding of how we can design traditional statistical models. But the conflation of model and algorithm can make it hard to unpick what design choices are influencing which aspects of the model. }

\notes{While I've motivated much of this paper through the lens of happenstance data. But the training sets that are used with these deep learning models have striking similarities to classical data acquisition. The deep learning revolution is really a revolution of ambition in the scale of data which we are collecting. The data set which drove this paradigm shift in data collection was ImageNet (see e.g. @Russakovsky-imagenet15). It was only with the millions of labeled images available in the data that Fei-Fei Li's team assembled that these highly overparameterized models were able to significantly differentiate themselves from traditional approaches [@Krizhevsky:imagenet12]. Collection of such massive data is statistical design on a previously unprecedented scale requiring massive human effort for labeling. That doesn't sit well with the notion of happenstance data, which by its nature is accumulating fast and is only lightly curated if at all. So, while acknowledging the importance and benefits of implicit regularization we will revert to the conceptual separation between model and algorithm as we consider what approaches might be useful for this new data landscape.}

\subsubsection{Reviewing the Traditional Paradigm}

\notes{The modern Bayesian has a suite of different software available to make it easier for her to design models and perform inference in the resulting design. Given this extra time, it might depress her to reflect on the fact that the entire premise of the approach is mistaken unless you are in the $\mathcal{M}$-closed domain. So when do we fall outside this important domain? According to @Box:science76, all the time.}

> All models are wrong, but some are useful

\notes{This important quote has become worn by overuse (like a favorite
sweater). Indeed, I most often see it quoted at the beginning of a talk in a way that confuses correlation with causality. Presentations proceed in the following way. 1) Here is my model. 2) It is wrong. 3) Here is George Box's quote. 4) My model is wrong, but it might be  might be useful. Sometimes I feel at stage 4) a confusion about the arrow of causality occurs, it feels to me that people are almost saying "*Because* my model is wrong it *might* be useful."}

\notes{Perhaps we should be more focusing on the quote from the same paper[^rich]

[^rich]: This quote was first highlighted to me by Richard D. Wilkinson.}

> the scientist must be alert to what is importantly wrong. It is inappropriate to be concerned about mice when there are tigers abroad. 
>
> @Box:science76

\notes{Let's have a think about
where the tigers might be in the domain of big data. To consider this,
let's first see what we can write down about our data that isn't
implicitly wrong. If we are interested in multivariate data we could
first write down our data as a *design matrix*}
$$
\text{data} = \mathbf{\dataMatrix} \in \Re^{\numData\times \dataDim}.
$$
\notes{Here we are assuming we have $\numData$ data points and $\dataDim$
features. As soon as we write down our data in this form it
invites particular assumptions about the data that may have been valid
in the 1930s, when there was more focus on survey data. Experimental designs 
stipulated a table of data with a specific set of hypotheses in mind. The data
naturally sat in a matrix.}

\notes{The first thing that I was taught about probabilistic modeling was i.i.d. noise. And as soon as we see a matrix of data, I believe it is second nature for most of us to start writing down factorization assumptions. In particular, an independence assumption across the $\numData$ data points, giving the likelihood function,}
\begin{align*}
p(\dataMatrix|\parameterVector) = \prod_{i=1}^\numData p(\dataVector_{i, :} | \boldsymbol{\theta}).
\end{align*}
\notes{This factorization gives both practical and theoretical
advantages. It allows us to trivially show show that by optimizing the
likelihood function, we are minimizing a sample based approximation
to a Kullback-Leibler divergence between our model and the true data
generating density (see e.g. @Wasserman:all03).
\begin{align*}
\log p(\dataMatrix|\parameterVector) =& \sum_{i=1}^\numData \log p(\dataVector_{i, :} | \boldsymbol{\theta}) + \text{const}
\approx & \int \Pr(\dataMatrix) \log \frac{p(\dataMatrix|\parameterVector)}{\Pr(\dataMatrix)}
\end{align*}
\notes{where \Pr(\dataMatrix) is the true data generating distribution.}

\notes{From pragmatist's perspective, the assumption allows us to make predictions about new data points given a parameter vector that is derived from the training data. If the uncertainty in the system is truly independent between different data observations, then the information about the data is entirely stored in our model parameters, $\parameterVector$.}

\notes{Much of classical statistics focusses on encouraging the data to conform to this independence assumption, for example through randomizing the design to distribute the infulence of confounders and through selection of appropriate covariates. Or to methodologies that analyze the model fit to verify the validity of these assumptions, for example residual analysis.}

\notes{From a Bayesian perspective, this assumption *is* only an assumption about the nature of the residuals. It is *not* a model of the process of interest. The philosophical separation of aleatory uncertainty and epistemic uncertainty occurs here. Probability is being used only to deal with the aleatory uncertainty.}

\notes{In the world of happenstance data, there is insufficient influence from the model-designer on the way that the data is collected to rely on randomization. We find ourselves needing to explicitly model relationships between confounders. This requires us to be more imaginative about our probabilistic models than pure independence assumptions.}

An additional challenge arising from this independence assumption is the domain where the number of data features, $\dataDim$, is larger than the number of data points,  $\numData<<\dataDim$, the so called \`large
$\dataDim$, small $\numData$' domain. Classical methodologies fail in this domain because the parameters are poorly determined.}

\subsection{Getting Rid of $\dataDim$}

\notes{Despite the advantages of the classical statistical paradigm, I believe it has lured us into a trap. The trap is that $\dataDim$ exists. That there is a particular dimensionality associated with the features, or covariates, we associate with a typical response variable. As I think about happenstance data, I've increasingly become to believe that $\dataDim$ doesn't really exist. It is a convenience for us. Or, at least if it does exist, it is not fixed in dimension, it varies, just like the number of data.}

\notes{In programming language parlance, we treat $\dataDim$ as a 'static variable'. One which stays the same size for the lifetime of the model. We are prepared to accept that $\numData$ will change, we will be expected to make out of sample predictions, but we don't accept that we might need to make 'out of response-variable' predictions or 'out-of-covariate' predictions.}

\notes{So, below, I intend to conflate $\numData$ and $\dataDim$. Rather than considering a design matrix, $\dataMatrix$, I'd like us to think about a vector, $\dataVector$, where each element of the vector arises from a particular data point, but could contain one of a number of features from that data point. The data moves from being a table, to a vector of data snippets. Each element of the vector potentially coming from a different subject and possibly encoding a different aspect of that subject.}

\notes{Now that we've decided we'll consider the data in a vector (if do you have a design matrix, just stack the columns of the design matrix one on top of another to form the vector), let's also drop the independence assumption. Independence assumptions are very useful, and we will return to them later. But for the moment let's assume it is not the first thing we should write down.}

\endif
