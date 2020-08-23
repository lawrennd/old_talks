---
title: Deep Probabilistic Models with Gaussian Processes
author: Neil D. Lawrence
---

## Introduction

Machine learning involves taking data and combining it with a model in order to make a prediction. The data consist of measurements recorded about the world around us. A model consists of our assumptions about how the data is likely to interrelate, typical assumptions include smoothness. Our assumptions reflect some undelying belief about the regularities of the universe that we expect to hold across a range of data sets.

$$\text{data} + \text{model} \rightarrow \text{prediction}$$

From my perspective, the model is where all the innovation in machine learning goes. The etymology of the data indicates that it is given (although in some cases, such as active learning, we have a choice as to how it is gotten), our main control is over the model. This is the key to making good predictions. The model is a mathematical abstraction of the regularities of the universe that we believe underly the data as collected. If the model is chosen well we will be able to interpolate the data and precit likely values of future data points. If it is chosen badly our predictions will be overconfident and wrong.  

### Models vs Algorithms

Much of the technical focus in machine learning is on algorithms. In this document I want to retain a strong separation between the *model* and the *algorithm*. The model is a mathematical abstraction of the world that encapsulates our assumptions about the data. Normally it will depend on one or more parameters which are adaptable. The algorithm provides a procedure for adapting the model to different contexts, often through the provision of a set of data that is used for training the model. 

Despite the different role of model and algorithm, the two concepts are often conflated. This sometimes leads to a confused discussion. I was recently asked "Is it correct to remove the mean from the data before you do principal component analysis." This question is about an algorithmic procedure, but the correct answer depends on what modelling assumption you are seeking to make when you are constructing your principal component analysis. Principal component analysis was originally proposed by  a *model* for data by [@Hotelling:analysis33]. It is a latent variable model that was directly inspired by work in the social sciences on factor analysis. However, much of our discussion of PCA today focusses on PCA as an algorithm. The algorithm for fitting the PCA model is to seek the eigenvectors of the covariance matrix, and people often refer to this algorithm as principal component analysis. However, that algorithm also finds the linear directions of maximum variance in the data. Seeking directions of maximum variance in the data was not the objective of Hotelling, but it is related to a challenge posed by [@Pearson:01] who sought a variant of regression that predicted symmetrically regardless of which variable was considered to be the covariate and which variable the response. Coincidentally the algorithm for this model is also the eigenvector decomposition of the covariance matrix. However, the underlying model is different. The difference becomes clear when you begin to seek non-linear variants of principal component analysis. Depending on your interpretation (finding directions of maximum variance in the data or a latent variable model) the corresponding algorithm differs. For the Pearson model a valid non-linearization is kernel PCA [Scholkopf:nonlinear98], but for the Hotelling model this generalization doesn't make sense. The Hotelling model is difficult to generalize without approximations<!-- A valid generalization of the Hotelling model is provided by the Gaussian process latent variable model [@Lawrence:pnpca05] -->. This confusion is often unhelpful, so for the moment we will leave algorithmic considerations to one side and focus *only* on the model. 

## Is my Model Useful?

*All models are wrong, but some are useful* --- : [@Box:science76]

This important quote has become worn by overuse (like a favourite sweater). Worse still it is almost being bandied around to mean that *because* my model is wrong it *might* be useful. It seems that people almost equate the statement to meaning probobability of my model being wrong given that its useful is = 1. Which would be an incorrect model, but seems to be useful in practice when trying to justify poor assumptions.

Perhaps we should be more focussing on the quote

>... the scientist must be alert to what is importantly wrong. It is inappropriate to be concerned about mice when there are tigers abroad." from the same paper. Let's have a think about where the tigers might be in the domain of big data. To consider this, let's first see what we can write down about our data that isn't implicitly wrong. If we are interested in multivariate data we could first write down our data in the following form.

$$\text{data} = \mathbf{\mathbf{Y}} \in \Re^{n\times p},$$

where here we are assuming we have $n$ data points and $p$ features. However, as soon as we write down our data in this form it invites particular assumptions about your data that were valid, perhaps in the 1930s, when people were worried about tables of data. They collected tables of data with a specific purpose in mind and the data naturally sat in a matrix. Immediately we write down our data in a matrix form, $\mathbf{Y}\in \Re^{n\times p}$ it is somehow implicit that we are suggesting factorization assumptions across the $n$ data points. 

$$p(\mathbf{Y}) = \prod_{i=1}^n p(\mathbf{y}_{i, :} | \boldsymbol{\theta})$$

This assumption allows us to easily make predictions about new data points given a parameter vector that is derived from the training data. This assumptions will generally be wrong, and also leads to concerns about the parameters when $n<<p$, the so called `large $p$, small $n$' domain.  They also lead to concerns such as large $p$, small $n$ concerns. 

I think that this is a wrongheaded way of thinking about modern data, because in practice, $p$, doesn't really exist, at least not in the sense that the above model implies we should treat it. It doesn't exist as a static view of the data: $p$ is much more fluid than the model above implies. Indeed, I'll argue below that rather than increasing $p$ when we obtain a new feature about a data point, we should be increasing $n$. That adding writing down our data in matrix form, $\mathbf{Y}$, may even be constraining our thinking to these factorized models. And the fact that the factorization is strong: i.e. it assumes that all becomes independent given the parameters, it is very often wrong. That is not to say that these factorization assumptions are not useful, indeed we will make use of them below, but they should *not* be the first thing we write down. 

### A Motivating Big Data Example

Statisticians like Pearson, Fisher and Student worked with tables of data that they'd carefully collected, often with the specific purpose of answering a particular question. The decided at experiment *design* time what was to be measured $n$. The number of samples was determined by statistical power calculations *CHECK THIS*, this was something that could be varied.

One of my own interests is personalized health: what we can learn about patients' state of health and when we should make an interviention. In the big data era, we aren't only interested in what data we might collect for answering a specific question (although data of this type remains very important) but we are also interested in existing data that might be assimilated to improve our understanding of an individual's health. When imagining future systems that monitor our health status, we should not be restricted to the type of data that might be stored in a doctor's office or a hospital data base. Indeed, it might be argued that such data focusses on sickness rather than health, giving us an incomplete picture. 

Modern data availabilities means that we could build models that incorporate an individual's exercise regime (for example through websites such as Strava and Endomomndo). We could include information about an individual's dietary habits (e.g. through loyalty card information like the Nectar card). If we were monitoring potential degradation in health then we may also be interested in an individual's social network activity (Twitter, Facebook, Google+). Even musical tastes may feed in to our overall picture of the patient's well being through music services like spotify. For a full perspective on a patient's health, this data would need to be combined with more traditional sources phenotype and genotyp infomration. For example, high resolution scans of the genome providing a detailed characterization of genotype. Large scale gene expression measurements, giving detailed insights into phenotype at the cellular level. Images containing x-rays or biopsies. Doctor's notes, but handwritten and those that encode a diangosis. Clinical tests, for example in cardiovascular disease cholestorol level. To provide a full picture of health status all this information needs to be assimilated. In a traditional model, we might encode each piece of information as another element on a feature vector: in other words, all the above contributes to increasing $p$. However, for most patients, most of the information above is likely to be missing. The paradigm of missing data is often discussed, but in this domain we have a situation we might refer to as *massivelv missing data*. A situation where a missing value becomes the norm rather than an exception. 

Another facet of the personalized health problem will be the streaming nature of data. When acquiring data passively data doesn't arrive in blocks, it arrives in a haphazard fashion. Our model may need to update because patient 2,342 has just had the results of a blood test logged, or because patient 28,344,219 has just been for a run or because patient 12,012,345 just listened to a Leonard Cohen track or because patient 12,182 just gave birth.

One possible motivation for making independence assumptions across data points is the ease with which predictions can be made for a previously unseen vector $\mathbf{y}^*$. Given an estimate of a vector of parameters, $\hat{\boldsymbol{\theta}}$, perhaps obtained by optimizing the likelihood on the training data, then due to our assumption of independence across data then we can easily predict for the new point using the conditional distribution:

$$p(\mathbf{y}_*|\hat{\boldsymbol{\theta}})$$.

Perhaps, though, we should find this ease of prediction suspicious. Let's momentarily examine what we are really saying here. We are assuming that all the information we wish to store about the world, and communicate to a test data set is storable in a parameter vector, $\boldsymbol{\theta}$, the nature of which (for example its length) is set at design time, before we've seen the data. That is precisely the meaning of statistical *independence given the parameters*. 

For applications like the personalized health monitoring system described above, we need a model that will give well calibrated predictions from the first day of it being brought on line, and throughout its operational life. If the model is complex enough to represent the full spectrum of possible human ailments, then when the model is first brought on stream,  it is unlikely to have sufficient data to determine the parameters. In the standard modeling framework we are faced with the bias variance dilema [@Geman:bias92]. If the model is complex enough to represent the underlying data structure, the parameters will be badly determined for small, or badly designed data sets, and the model will exhibit a large error due to variance. A traditional solution is to err towards bias, by constructing a simpler model, but one where the parameters can be well determined by the data, we reduce variance at the expense of some bias. In the context of our medical application, there are three major problems with this approach. Firstly, the size and scope of the data is continually evolving: we do not have a fixed design. This means that even if we were to find a good initial compromise between bias and variance, this compromise may be rapidly invalidated. Secondly, the compromise we find would have to apply equally to all patients despite the diversity of data we have associated with those patients. Finally, we should fear the confidence of predictions from a model with well determined parameters unless we truly believe we have sufficient data to capture some underlying deterministic truth. Medical outcome is laced with uncertainty, and this uncertainty needs to be modeled correctly because its structure has a significant effect on treatment. 

A major challenge in the domain we've described is to build a model that is complex enough to represent the diversity of human health outcomes. For streaming data this necessarily means that some of those parameters will be badly determined. I'd also argue further that if the parameters are well determined this is actually a warning. If all parameters are well determined, then our assumption of statistical independence becomes a strong one: the residual uncertainty is only in the noise, which by its independent nature, is impossible to model. However, any uncertainty in the parameters gives a much more structured uncertainty distribution for the data.

### Uncertainty in Parameters

If the parameters are badly determined, then small fluctuations in the data set lead to larger fluctuations in prediction. One approach to this problem is to build models in which the parameters are well determined. For teh independence across data points case, this involves having many observations (large $n$) relative to the number of parameters (which often scales with $p$). This motivates the issues of the large $p$ small $n$ domain, where the conditions are reversed. Of course, from a modelling perspective this issue is trivially solved by assuming independence across the $p$ data dimensions and allowing the parameters to scale with the number of data $n$. This is a characteristic exhibited, for example by the Gaussian process latent variable model [@Lawrence:pnpca05] which in standard form assumes independence arcross $p$ for high dimensional data and associates each data point with a latent variable that is treated as a parameter. In [@Lawrence:unifying12] we argued that the succesful class of *spectral* approaches to dimensionality reduction (e.g. [@Roweis:lle00] and [@Weinberger:learning04]), which are widely applied in the large $p$ small $n$ domain, also have a probabilistic intepretation where the underlying likelihood factorizes across data dimensions. Regardless of our choice of factorization though, we are still making the same claim: a particular vector, or matrix, of parameters is suffcient for us to consider that the data independent, either across features or data points. 

### Massively Missing Data

I'd like to argue that the separation of the data into features and data points is rather arbitrary. I believe it stems from the origin of the field of statistics, where the intention was to make a strong scientific claim based on numbers take from a *table* of data. A table naturally lends itself towards a matrix form. In these data a statistical design normally involved measuring a fixed number of *features* for a perhaps variable number of *items*. The objective is to find sufficient number of items so that you can make strong claims about which features are important. For example, does smoking correlate with lung cancer? This explains the desire to write down the data as a matrix $\mathbf{Y}$. I think this view of data, whilst important at the time, is outdated when considering modern big data problems.

The modern data analysis challenge is very different. We receive streaming data of varying provenance. If each number we receive is given by an observation $y_i$, where $y_i$ could be in the natural numbers, the real numbers or binary or in any processable form, then $y_{17}$ might be the price of a return rail fair from Sheffield to Oxford on 6th February 2014, whilst $y_{29}$ might be the number of people on the 8:20 train that day, but $y_{72,394}$ could be the temperature of the Atlantic ocean on 23rd August 2056 at a point on the artic circle midway between Greenland and Norway. When we see data in this form, we realize that most of the time we are missing most of the data. This leads to the idea of *massive missing data*. Contrast this situation with that traditionally faced in missing data where a table of values, $\mathbf{Y}$, might have 10%-50% of the measurements missing, perhaps due to problems in data collection. I'd argue that if we are to model complex processes (such as the brain, or the cell, or human health) then almost all the data is missing. 

\begin{tikzpicture}[scale=2]
% Define nodes
\draw node[obs] (y) {$\mathbf{y}$};
\end{tikzpicture}

A model that's not wrong, just not useful. I like graphical representations of probabilistic models and this is my favourite graph. It is the most simple but also the most general. It says that all the data in our vector $\mathbf{y}$ is governed by an unspecified probability disribution $p(\mathbf{y})$. Graphical models normally express the conditional independence relationships in the data, with this graph we are not a priori considering any such relationships. This is the most general model (it includes all factorized models as special cases). It is not wrong, but since it doesn't suggest what the next steps are or give us any handles on the problem it is also not useful.

This is the nature of modern streaming data, what has been called big data, although in the UK it looks like that term will gain a more diffuse meaning now that the government has associated a putative 189 billion pounds of funding to it. But the characteristic of massive missing data is particularly obvious when we look at clinical domains. EMIS, a Yorkshire based provider of software to General Practitioners, has 39 million patient records. When we consider clinical measurements, we need to build models that not only take into account all current clinical tests, but all tests that will be invented in the future. This leads to the idea of massive missing data. The classical statistical table of data is merely the special case where someone has filled in a block of information. 

To deal with massively missing data we need to think about the *Kolmogorov consistency* of a process. Let me introduce Kolmogorov consistency by way of an example heard from Tony O'Hagan, but one that he credits originally to Michael Goldstein. Imagine you are on jury duty. You are asked to adjudicate on the guilt or innocence of Lord Safebury, and you are going to base your judgement on a model that is weighing all the evidence. You are just about to pronounce your decision when a maid comes running in and shouts "He didn't do it! He didn't do it!". The maid wasn't on the witness list and isn't accounted for in your model. How does this effect your inference? The pragmatists answer might be: not at all, because the maid wasn't in the model. But in the interests of justice we might want to include this information in our inference process. If, as a result of the maid's entry, we now think it is less likely that Lord Safebury committed the crime, then necessarily every time that the (unannounced) maid doesn't enter the room we have to assume that it is more likely that Safebury commited the crime (to ensure that the conditional probability of guilt given the maid's evidence normalizes. But we didn't know about the maid, so how can we account for this? Further, how can we account for all possible other surprise evidence, from the announced butlers, gardners, chauffeurs and footmen? Kolmogorov consistency says that the net effect of marginalizing for all these potential bits of new information is null. It is a particular property of the model. Making it (only slightly) more formal, we can consider Kolmogorov consistency as a marginalization property of the model. We take the $n$ dimensional vector, $\mathbf{y}$, to be an (indexed) vector of all our instantiated observations of the world that we have *at the current time*. Then we take the $n^*$ dimensional vector, $\mathbf{y}^*$ to be the observations of the world that we are *yet to see*. From the sum rule of probability we have

$$
p(\mathbf{y}|n^*) = \int p(\mathbf{y}, \mathbf{y}^*) \text{d}\mathbf{y}^*
$$

where the dependence of the marginal distribution for $\mathbf{y}$ aries from the fact that we are forming an $n^*$ dimensional integral over $\mathbf{y}^*$. If our distribution is Kolmogorov consistent, then we know that the distribution over $\mathbf{y}$ is *independent* of the value of $n^*$. So in other words $p(\mathbf{y}|n*)=p(\mathbf{y})$. So Kolmogorov consistency says that the form of $p(\mathbf{y})$ remains the same *regardless* of the number of observations of the world that are yet to come. 

## Parametric Models

We can achieve Kolomogrov consistency almost trivially in a parametric model if we assume that the probability distribution is independent given the parameters. Then the property of being closed under marginalization is trivially satisfied through the independence,

$$p(\mathbf{y}, \mathbf{y}^*) = \int \prod_{i=1}^n p(y_{i} | \boldsymbol{\theta})\prod_{i=1}^{n^*}p(y^*_i|\boldsymbol{\theta}) p(\boldsymbol{\theta}) \text{d}\boldsymbol{\theta}$$

which allows us to marginalize for all future data leaving a joint distribution which isn't dependent on $n^*$ because each future data point can be marginalized independently.

$$p(\mathbf{y}) = \int \prod_{i=1}^n p(y_{i} | \boldsymbol{\theta})\prod_{i=1}^{n^*} \int p(y^*_i|\boldsymbol{\theta}) \text{d}y^*_i p(\boldsymbol{\theta}) \text{d}\boldsymbol{\theta}$$

But, as we've already argued, this involves an assumption that is often flawed in practice. It is unlikely that, in a complex model, we will be able to determine the parameter vector well enough, given limited data, for us to truly believe that all the information about the training data that is required for predicting the test data could be passed through a fixed length parameter vector. This is what this independence assumption implies. If we consider that the model will also be acquiring new data at run time, then there is the question of hot to update the parameter vector in a consistent manner, accounting for new information, e.g. new clinical results in the case of personalized health. 

Conversely, a general assumption about independence across *features* would lead to models which *don't* exhibit *Komlogorov consistency*. In these models the dimensionality of the test data, $\mathbf{y}^*$, denoted by $n^*$ would have to be fixed and each $y^*_i$ would require marginalization. So the nature of the test data would need to be known at model *design* time. 

## Parametric Bottleneck

In practice Bayesian methods suggest placing a prior over $\boldsymbol{\theta}$ and using the posterior, $p(\boldsymbol{\theta}|\mathbf{y})$ for making predictions.

$$
p(\mathbf{y}^*|\mathbf{y}) = \int \prod_i p(y_i^* | \boldsymbol{\theta}) p(\boldsymbol{\theta}|\mathbf{y})\text{d}\boldsymbol{\theta} 
$$

We have a model that obeys Kolmogorov consistency, and is sophisticated enough to represent the behaviour of a very: it may well require a large number of parameters. One way of seeing the requirement for a large number of parameters is to look at how we are storing information from the training data to pass to the test data. The sum of all our knowledge about the training data is stored in the conditional distribution of the parameters given the training data, Uncertainty complex systA key design time problem is the *parametric bottleneck*. If we choose the number of parameters at design time, but the system turns out to be more complicated that we expected, we need to design a new model to deal with this complexity. The communication between the training data and the test data is like an information channel. This TT channel has a bandwidth that is restricted by our choice of the dimensionality of $\boldsymbol{\theta}$ at *design* time. This seems foolish. Better to ensure we choose a model that allows for that channel to be potentially infinite. This implies a non-parametric approach. Our prior over $\boldsymbol{\theta}$ should be *non parametric*.

$$p(\boldsymbol{\theta} | \mathbf{y})$$

which, as we argued above, allows us to retain the necessary sense of uncertainty about the parameters that is required in a very complex system when we have seen relatively little data. How much information can we store, then, about the training data? The information gain from the training data is given by the Kullback Leibler divergence between our prior distribution and our posterior distribution. 

$$\KL{p(\boldsymbol{\theta}|\mathbf{y})}{p(\boldsymbol{\theta})}$$

This is the information gained, measured in 'nats' if we use natural logarithms, but it could equally be measured in bits, about our parameters having observed the training data. In the case that our likelihood is log concave[^logconcave] then this information gain provably will increase, with every observed data point. How much information we gain will depend on the likelihood associated with each data $y_i$. This Kullback Leibler divernece has an infomration theoretic interpretation as a communication channel passing information from the training data to the test data. From an information theoretic perspective, the channel bandwidth is controlled by the dimensionality of the parameter vector $\mathbf{y}$ and the form of the prior $p(\boldsymbol{\theta})$. 

[^logconcave]: This is a definite constraint on the model, there are many very reasonable likelihoods that are not log concave.

## The Non-parametric Challenge

We have argued that we want models that are unconstrained, at design time, by a fixed bandwidth for the communication between the training data, $\mathbf{y}$, and the test data, $\mathbf{y}^*$ and that the answer is to be non parameteric. By non-parametric we are proposing using classes of models for which the conditional distribution, $p(\mathbf{y}^*|\mathbf{y})$ is not decomposable into the expectation of $p(\mathbf{y}^*|\boldsymbol{\theta})$ under the posterior distribution of the parameters, $p(\boldsymbol{\theta}|\mathbf{y})$ for any fixed length parameter vector $\boldsymbol{\theta}$. We don't want to impose such a strong constraint on our model at *design time*. Our model may be required to be operational for many years and the true complexity of the system being modeled may not even be well understood at *design time*. We must turn to paradigms that allow us to be adaptable at *run time*. Non parametrics provides just such a paradigm, because the effect parameter vector increases in size as we observe more data. This seems ideal, but it also presents a problem. 

Human beings, despite are large, interconnected brains, only have finite storage. Similar for digital computers. So we need to assume that we can only store a finite number of things about the data $\mathbf{y}$. This seems to push us back towards non-parametric models. Here, though, we choose to go a different way. We choose to introduce a set of auxiliary variables, $\mathbf{u}$, which are $m$ in length. Rather than representing the non parametric density directly, we choose to focus on storing information about $\mathbf{u}$. By storing information about these variables, rather than storing all the data $\mathbf{y}$ we hope to get around this problem. In order for us to be non parametric about our predictions for $\mathbf{y}*$ we must condition on all the data, $\mathbf{y}$. We can't any longer store an intermediate distribution to represent our sum knowlege, $p(\boldsymbol{\theta}|\mathbf{y})$. Such an intermediate distribution is a finite dimensional object, and non-parametrics implies that we cannot store all the information in a finite dimensional distribution. This presents a problem for real systems in practice. We are now faced with a compromise, how can we have a distribution which is flexible enough to respond at *run time* to unforeseen complexity in the training data? Yet, simultaneously doesn't require unbounded storage to retain all the information in the training data? We will now introduce a perspective on variational inference that will allow us to retain the advantages of both worlds. We will construct a parametric approximation to the true non-parametric conditional distribution. But, importantly, whilst this parametric approximation will suffer from the constraints on the bandwidth of the TT channel that drove us to non-parametric models in the first place, we will be able to change the number of parameters at *run time* not simply at design time.

### The Multivariate Gaussian: Closure Under Marginalization

Being closed under marginalization is a remarkable property of our old friend the multivariate Gaussian distribution (old friends often have remarkable properties that we often take for granted, I think this is particularly true for the multivariate Gaussian). In particular, if we consider a joint distribution across $p(\mathbf{y}, \mathbf{y}^*)$, then the covariance matrix of the marginal distribution for the subset of variables, $\mathbf{y}$, is unaffected by the length of $\mathbf{y}^*$. Taking this to its logical conclusion, if the length of the data, $\mathbf{y}$, is $n=2$. Then that implies that the covariance between $\mathbf{y}$, as defined by $\mathbf{K}$, is only a $2\times 2$ matrix, and it can only depend on the indices of the two data points in $\mathbf{y}$. Since this covariance matrix must remain the same for any two values *regardless* of the length of $\mathbf{y}$ and $\mathbf{y}^*$ then the value of the elements of this covariance must depend only on the two indices associated with $\mathbf{y}$. 

vec ihis implies that the covariance matrix must be dependent only Since the covariance matrix is specified pairwise, dependent only on the index of the two observations $y_i$ and $y_j$ for which the covariance is being computed. In general we can also think of this index as being infinite: it could be a spatial or temporal location.

$$
p(\mathbf{y}) = \int p(\mathbf{y}, \mathbf{y}^*) \text{d}\mathbf{y}^*= \frac{\exp\left(\begin{bmatrix}\mathbf{y}\\ \mathbf{y}^*\end{bmatrix}^\top\begin{bmatrix}\mathbf{K} & \mathbf{K}_*\\ \mathbf{K}_*^\top & \mathbf{K}_{**}\end{bmatrix}^{-1} \begin{bmatrix}\mathbf{y}\\ \mathbf{y}^*\end{bmatrix}\right)}{\int \exp\left(\begin{bmatrix}\mathbf{y}\\ \mathbf{y}^*\end{bmatrix}^\top\begin{bmatrix}\mathbf{K} & \mathbf{K}_*\\ \mathbf{K}_*^\top & \mathbf{K}_{**}\end{bmatrix}^{-1} \begin{bmatrix}\mathbf{y}\\ \mathbf{y}^*\end{bmatrix}\right) \text{d}\mathbf{y} \text{d}\mathbf{y}^*} = \mathcal{N}(\mathbf{0} |\mathbf{K})  
$$ 

where each $y_i$ is now defined across the real line, and the dimensionality of $\mathbf{y}*$ is irrelevant. 
Prediction consists of conditioning the joint density on $\mathbf{y}^*$. So for any new value of $\mathbf{y}^*$, given its index we compute $p(\mathbf{y}^* | \mathbf{y})$. 

## Making Parameters non-Parametric

We will start by introducing a set of variables, $\mathbf{u}$, that are finite dimensional. These variables will eventually be used to communicate information between the training and test data, i.e. across the TT channel. 

$$
p(\mathbf{y}^*|\mathbf{y}) = \int p(\mathbf{y}^*|\mathbf{u}) q(\mathbf{u}|\mathbf{y}) \text{d}\mathbf{u}
$$

where we have introduced a distribution over $\mathbf{u}$, $q(\mathbf{u}|\mathbf{y})$ which is not necessarily the true posterior distribution. 

\begin{tikzpicture}[scale=2]
% Define nodes
\draw node[obs] (y) {$\mathbf{y}$};
\draw node[latent, above=of y] (u) {$\mathbf{u}$};

\draw [-] (u) to (y);%
\end{tikzpicture}


Our simple graphical model augmented with $\mathbf{u}$ which we refer to as inducing variables. Note that the model is still totally general because $p(\mathbf{y}, \mathbf{u})$ is an augmented variable model and the original $p(\mathbf{y})$ is easily recovered by simple marginalization of $\mathbf{u}$. We haven't yet made any assumptions about our data. 

The model we've introduced now seems remarkably like the parametric model we argued against in the previous section. So what's going on here, is there going to be some kind of parametric/non parametric 3 card trick where with sleight of hand we are trying to introduce a parametric model? Well clearly not, because I've just given the game away. But I believe there are some important differences to the traditional approach for parameterizing a model. Philosophically, our variables $\mathbf{u}$ are variables that augment the the model. We have not yet made any assumptions by introducing them. Normally the parameterization of the model instantiates assumptions, but this is not happening here. In particular note that we have *not* assumed that the training data factorize given the inducing variables. Secondly, we are not going to specify the dimensionality of $\mathbf{u}$ (i.e. the size of the TT channel) at *design* time. We are going to allow it to change at *run* time. We will do this by ensuring that the inducing variables also obey Kolmogorov consistency. In particular we require that  If we build a joint density as follows:

$$
p(\mathbf{y}, \mathbf{u}|m^*, n^*) = \int p(\mathbf{y}^*, \mathbf{y}, \mathbf{u}^*, \mathbf{u}) \text{d}\mathbf{y}^*  \text{d}\mathbf{u}^*
$$

where $\mathbf{u}$ are the inducing variables we choose might choose to instantiate at any given time (of dimensionality $m$) and $\mathbf{u}^*$ is the $m^*$ dimensional pool of future inducing variables we have *not yet* chosen to instantiate (where $m^*$ could be infinite). Our new Kolmogorov consistency condition requires that

$$p(\mathbf{y}, \mathbf{u}|m^*,n^*) = p(\mathbf{y}, \mathbf{u}).$$

It doesn't need to be predetermined at *design time* because we allow for the presence of a (potentially infinite) number of inducing variables $\mathbf{u}^*$ that we may wish to *later* instantiate to improve the quality of our model. In other words, it is very similar to the parametric approach, but now we have access to a future pool of additional parameters, $\mathbf{u}^*$ that we can call upon to increase the bandwidth of the TT channel as appropriate. In parametric modelling, calling upon such parameters has a significant effect on the likelihood of the model, but here these variables are auxiliary variables that will *not* effect the likelihood of the model. They merely effect our ability to approximate the true bandwidth of the TT channel. The quality of this approximation can be varied at run time. It is not necessary to specify it at design time.  This gives us the flexibility we need in terms of modeling, whilst keeping computational complexity and memory demands manageable and appropriate to the task at hand.


\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$\mathbf{y}$};
\draw node[latent, left=of y] (ystar) {$\mathbf{y}^*$};
\draw node[latent, above=of y] (u) {$\mathbf{u}$};
\draw node[latent, above=of ystar] (ustar) {$\mathbf{u}^*$};
        
% Connect the nodes
\draw [-] (u) to (y);%
\draw [-] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-] (ystar) to (y);%
\draw [-] (ustar) to (ystar);%
\draw [-] (u) to (ystar);%
\end{tikzpicture}

Adding in the test data and the inducing variables we have not yet chosen to instantiate. Here we see that we still haven't defined any structure in the graph, and therefore we have not yet made any assumptions about our data. Not shown in the graph is the additional assumption that whilst $\mathbf{y}$ has $n$ dimensions and $\mathbf{u}$ has $m$ dimensions, $\mathbf{y}^*$ and $\mathbf{u}^*$ are potentially infinite dimensional.

### Fundamental Variables

To focus our model further, we assume that we observe observations, $\mathbf{y}$ that are derived from some underlying fundamental, $\mathbf{f}$, through simple factorized likelihoods. The idea of the fundamental variables is that they are sufficient to describe the world around us, but we might not be able to observe them directly. In particular we might observe relatively simple corruptions of the fundamental variables such as independent addition of noise, or thresholding. We might observe something relative about two fundamental veriables. For example if we took $f_12,345$ to be the height of Tom Cruise and $f_23,789$ to be the height of Penelope Cruz then we might take for an observation a binary value indicating the relative heights, so $y_72,394 = f_12,345 < f_23,789$. The fundamental variable is an artificial construct, but it can prove to be a useful one. In particular we'd like to assume that the relationship between our observations, $\mathbf{y}$ and the fundamental variables, $\mathbf{f}$ might factorize in some way. In the framework we think of this relationship, given by $p(\mathbf{y}|\mathbf{u})$ as the *likelihood*. We can ensure that assuming the likelihood factorizes does not at all reduce the generality of our model, by forcing the distribution over the fundamentals, $p(\mathbf{f})$ to also be Kolmogorov consistent. This ensures that in the case where the the likelihood is fully factorized over $n$ the model is still general if we allow the factors of the likelihood to be Dirac delta functions  suggesing that $y_i = f_i$. Since we haven't yet specified any forms for the probability distributions this *is* allowed and therefore the formulation is still totally general.

$$p(\mathbf{y}|n^*) = \int p(\mathbf{y}|\mathbf{f}) p(\mathbf{f},\mathbf{f}^*)\text{d}\mathbf{f} \text{d}\mathbf{f}^*$$

and since we enforce Kolmogorov consistency we have

$$p(\mathbf{y}|n*) = p(\mathbf{y})$$

\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$\mathbf{y}$};
\draw node[latent, above=of y] (f) {$\mathbf{f}$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\mathbf{u}^*$};
\draw node[latent, above=of f] (u) {$\mathbf{u}$};

        
% Connect the nodes
\draw [-, draw=gray] (ustar) to (u);%
\draw [-, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [-] (u) to (f);%
\end{tikzpicture}


Now we assume some form of factorization for our data observations, $\mathbf{y}$, given the fundamental variables, $\mathbf{f}$, so that we have

$$
p(\mathbf{y}|\mathbf{f}) = \prod_{i} p(\mathbf{y}^i| \mathbf{f}^i)
$$

so that we have subsets of the data $\mathbf{y}^i$ which are dependent on sub sets of the fundamental variables, $f$. For simplicity of notation we will assume a factorization across the entire data set, so each observation, $y_i$, has a single underlying fundamental variable, $f_i$, although more complex factorizations are also possible and can be considered within the analysis.

$$p(\mathbf{y}|\mathbf{f}) = \prod_{i=1}^n p(y_i|f_i)$$

\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$y_i$};
\draw node[latent, above=of y] (f) {$f_i$};
\draw node[latent, above=of f] (u) {$\mathbf{u}$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\mathbf{u}^*$};
        
% Connect the nodes
\draw [-, draw=gray] (ustar) to (u);%
\draw [-, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [-] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots n$} ;
\end{tikzpicture}
        
We now decompose, without loss of generality, our joint distribution over inducing variables and fundamentals into the following parts

$$p(\mathbf{u}, \mathbf{f}) = p(\mathbf{f}|\mathbf{u})p(\mathbf{u})$$

where we assume that we have marginalised $\mathbf{f}^*$ and $\mathbf{u}^*$. 



\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$y_i$};
\draw node[latent, above=of y] (f) {$f_i$};
\draw node[latent, above=of f] (u) {$\mathbf{u}$};
        
% Connect the nodes
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots n$} ;
\end{tikzpicture}


\begin{tikzpicture}[scale=2]
\draw node[obs] (y) {$\mathbf{y}$};
\draw node[latent, above=of y] (f) {$\mathbf{f}$};
\draw node[obs] (y) {$y_i$};
\draw node[latent, above=of y] (f) {$f_i$};
\draw node[latent, above=of y] (u) {$\mathbf{u}$};
\draw node[latent, above left=of y] (u) {$\mathbf{u}$};
\draw node[latent, above right=of y] (ustar) {$\mathbf{u}^*$};
\draw node[latent, above=of f] (u) {$\mathbf{u}$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\mathbf{u}^*$};
\draw node[const, above=of f] (u) {$\mathbf{u}$};
        
% Connect the nodes
\draw [->] (u) to (y);%
\draw [->] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-, draw=gray] (ustar) to (u);%
\draw [->, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots n$} ;
\end{tikzpicture}

\begin{tikzpicture}[scale=2]
\draw node[obs] (y) {$\mathbf{y}$};
\draw node[latent, above=of y] (f) {$\mathbf{f}$};
\draw node[obs] (y) {$y_i$};
\draw node[latent, above=of y] (f) {$f_i$};
\draw node[latent, above=of y] (u) {$\mathbf{u}$};
\draw node[latent, above left=of y] (u) {$\mathbf{u}$};
\draw node[latent, above right=of y] (ustar) {$\mathbf{u}^*$};
\draw node[latent, above=of f] (u) {$\mathbf{u}$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\mathbf{u}^*$};
\draw node[const, above=of f] (u) {$\mathbf{u}$};
        
% Connect the nodes
\draw [->] (u) to (y);%
\draw [->] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-, draw=gray] (ustar) to (u);%
\draw [->, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots n$} ;
\end{tikzpicture}



\begin{tikzpicture}[scale=2]
% Define nodes
\draw node[obs] (y) {$\mathbf{y}$};
\draw node[latent, above=of y] (f) {$\mathbf{f}$};
\draw node[obs] (y) {$y_i$};
\draw node[latent, above=of y] (f) {$f_i$};
\draw node[latent, above=of y] (u) {$\mathbf{u}$};
\draw node[latent, above left=of y] (u) {$\mathbf{u}$};
\draw node[latent, above right=of y] (ustar) {$\mathbf{u}^*$};
\draw node[latent, above=of f] (u) {$\mathbf{u}$};
\draw node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\mathbf{u}^*$};
\draw node[const, above=of f] (u) {$\mathbf{u}$};
        
% Connect the nodes
\draw [->] (u) to (y);%
\draw [->] (ustar) to (y);%
\draw [-] (ustar) to (u);%
\draw [-, draw=gray] (ustar) to (u);%
\draw [->, draw=gray,color=gray] (ustar) to (f);%
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots n$} ;
\end{tikzpicture}        
 



## Instantiating the Model

So far we haven't made any assumptions about the data in our model, other than a factorization assumption between the fundamental variables and the observations, $\mathbf{y}$. Even this assumption does not affect the generality of the model decomposition, because in the worst case the likelihood $p(\mathbf{y}|\mathbf{f})$ could be a Dirac $\delta$ function, implying $\mathbf{y}=\mathbf{f}$ and allowing us to include complex interelations between $\mathbf{y}$ directly in $p(\mathbf{f})$. We have specified that $p(\mathbf{f}, \mathbf{u})$ should be Kolmogorov consistent with $\mathbf{f}^*$ and $\mathbf{u}^*$ being marginalised and we have argued that non-parametric models are important in practice to ensure that all the information in our training data can be passed to the test data.

For a model to be useful, we need to specify relationships between our data variables. Of course, this is the point at which a model also typically becomes wrong. The following considerations should arise:

If our model is not correct, is it a useful abstraction given what we expect to observe about the data? For example, Brownian motion is modelled as a stochastic differential equation.

### Gaussian Processes

A flexible class of models that fulfils the constraints of being non-parametric and Kolmogorov consistent is Gaussian processes. Gaussian processes assume that the data is jointly Gaussian distributed. Each data point, $y_i$, is is jointly distributed with each other data point $y_j$ as a multivariate Gaussian. The covariance of this Gaussian is a function of the indices of the two data, in this case $i$ and $j$. But these indices are not just restricted to discrete values. The index can be a continuous value such as time, $t$, or spatial location, $\mathbf{x}$. The words index and indicate have a common etymology. This is appropriate because the index indicates the provenance of the data.  In effect we have multivariate indices to account for the full provenance, so that our observations of the world are given as a function of, for example, the when, the where and the what. When is given by time, where is given by spatial location and what is given by a (potentially discrete) index indicating the further provenance of the data. To define a joint Gaussian density, we need to define the mean of the density and the covariance. Both this mean and the covariance also need to be indexed by the when, the where and the what. 

### Augmenting with Inducing Variables in Gaussian Processes

To define our model we need to describe the relationship between the fundamental variables, $\dataMappingVector$, and the inducing variables, $\mathbf{u}$. This needs to be done in such a way that the inducing variables are also Kolmogorov consistent. A straightforward way of achieving this is through a joint Gaussian process model over the inducing variables and the data mapping variables, so in other words we define a Gaussian process prior over

$$\begin{bmatrix}\mathbf{f} \\ \mathbf{u}\end{bmatrix} \sim \gaussianDist{\mathbf{m}}{\mathbf{K}}$$

where the covariance matrix has a block form,

$$\mathbf{K} = \begin{bmatrix} \mathbf{K}_{\mathbf{f}\mathbf{f}} & \mathbf{K}_{\mathbf{f}\mathbf{u}} \\ \mathbf{K}_{\mathbf{u}\mathbf{f}} & \mathbf{K}_{\mathbf{u}\mathbf{u}}\end{bmatrix}$$

and $\mathbf{K}_{\mathbf{f}\mathbf{f}}$ gives the covariance between the fundamentals vector, $\mathbf{K}_{\mathbf{u}\mathbf{u}}$ gives the covariance matrix between the inducing variables and $\mathbf{K}_{\mathbf{u}\mathbf{f}} = \mathbf{K}_{\mathbf{f}\mathbf{u}}^\top$ gives the cross covariance between the inducing variables, $\mathbf{u}$ and the mapping function variables, $\mathbf{f}$. 

The elements of $\mathbf{K}_{\mathbf{f}\mathbf{f}}$ will be computed through a covariance function (or kernel) given by $\kernelScalar_f(\mathbf{x}, \mathbf{x}^\prime)$ where $\mathbf{x}$ is a vector representing the *provenance* of the data, which as we discussed earlier could involve a spatial location, a time, or something about the nature of the data. In a Gaussian process most of the modelling decisions take place in the construction of $\kernelScalar_f(\cdot)$.

### The Mean Function

The mean of the process is given by a vector $\mathbf{m}$ which is derived from a mean function $m(\mathbf{x})$. There are many occasions when it is useful to include a mean function, but normally the mean function will have a parametric form, $m(\mathbf{x};\boldsymbol{\theta})$, and be subject (in itself) to the same constraints that a standard parametric model has. Indeed, if we choose to model a function as a parametric form plus Gaussian noise, we can recast such a model as a simple Gaussian process with a covariance function $k_f(\mathbf{x}_i,\mathbf{x}_j) = \sigma^2 \delta_{i, j}$, where $\delta_{i, j}$ is the *Kronecker* delta-function and a mean function that is given by the standard parametric form. In this case we see that the covariance function is mopping up the *residuals* that are not captured by the mean function. If we genuinely were interested in the form of a parametric mean function, as we often are in statistics, where the mean function may include a set of covariates and potential effects, often denoted by

$$m(\mathbf{x}) = \boldsymbol{\beta}^\top \mathbf{x},$$

where here the provenance of the data is known as the covariates, and the variable associated with $\mathbf{y}$ is typically known as a *response* variable. In this case the particular influence of each of the covariates is being encoded in a vector $\boldsymbol{\beta}$. To a statistician, the relative values of the elements of this vector are often important in making a judgement about the influence of the covariates.  For example, in disease modelling the mean function might be used in a *generalised* linear model through a link function to represent a rate or risk of disease [@Diggle:somewhere]. The covariates should *co-vary* (or move together) with the response variable. Appropriate covariates for malaria incidence rate might include known influencers of the disease. For example if we are dealing with *malaria* then we might expect disease rates to be influenced by altitude, average temperature, average rainfall, local distribution of prophylactic measures (such as nets) etc. The covariance of the Gaussian process then has the role of taking care of the *residual* variance in the data: the data that is not explained by the mean function, i.e. the variance that cannot be explained by the parametric model. In a disease mapping model it makes sense to assume that these residuals may not be independent. An underestimate of disease at one spatial location, may imply an underestimate of disease rates at a nearby location. The mismatch between the observed disease rate and that predicted by modeling the relationship with the covariates through the mean function is then given by the covariance function.

The modeling philosophy in machine learning is somewhat different from that followed in traditional statistics. In machine learning the aim is often to be predictive, rather than explanatory. There is typically less need for an interpretable model, and so the mean function is much less rarely used. The objective is to predict the data entirely through the covariance function. From the arguments we developed earlier about the need for nonparametrics this makes a lot of sense. In particular if we rely on the mean function to make our predictions and assume that the covariance function is dealing with the residuals, then as we obtain more data the parameters of the mean function will become better determined. If the mean function does capture the majority of the variance of our observations, then the role of the covariance function will be reduced to capture only the variance of the residuals. But at this point we are left with a model that is dominated by is parametric part at the expense of its non parametric part. If the parameters have become well determined then the uncertainty about future predictions will be reduced. However, if we enter a novel domain (one where the provenance of the data differs significantly from the data we observed at training time) then we will still make very confident extrapolations when predicting for the new data. For this reason in machine learning we often prefer to leave out the mean function to ensure that the signal variance is explained through non parametric part of the model rather than the parametric mean function. In what follows we will drop the mean function and focus only on the covariance function.

\todo{Mention here an example of things going wrong? Or do a short run of a mauna loa data to demonstrate, with a mean function included?}


```python
%pylab inline
import GPy
data = GPy.util.datasets.mauna_loa()
kern = GPy.kern.Linear(1) + GPy.kern.RBF(1) + GPy.kern.Bias(1)
model = GPy.models.GPRegression(data['X'], data['Y'], kern)
#model.optimize()

```

    Populating the interactive namespace from numpy and matplotlib



      File "/Users/neil/SheffieldML/GPy/GPy/kern/_src/coregionalize.py", line 154
        def _gradient_reduce_numpy(self, dL_dK, index, index2):
        ^
    IndentationError: unexpected indent




```python

```


```python
pb.plot(xlim
```

So we *could* interpret Gaussian process models as approaches to dealing with residuals

### Modelling $\mathbf{f}$

In conclusion, for a non parametric framework, our model for $\mathbf{f}$ is predominantly in the covariance function $\mathbf{K}_{\mathbf{f}\mathbf{f}}$. This is our data model. We are assuming the inducing variables are drawn from a joint Gaussian process with $\mathbf{f}$. The cross covariance between $\mathbf{u}$ and $\mathbf{f}$ is given by $\mathbf{K}_{\mathbf{f}\mathbf{u}}$. This gives the relationship between the function and the inducing variables. There are a range of ways in which the inducing variables can interelate with the 

### Illustrative Example

For this illustrative example, we'll consider a simple regression problem. The example is based on one that James Hensman showed at the January 2014 Gaussian process winter school in his talk is on low rank Gaussian process approximations. 


```python
%pylab inline
import GPy
import numpy as np
import pylab as pb
from scipy import optimize
np.random.seed(101)
```

## A Simple Regression Problem

Here we set up a simple one dimensional regression problem. The input locations, $\mathbf{X}$, are in two separate clusters. The response variable, $\mathbf{y}$, is sampled from a Gaussian process with an exponentiated quadratic covariance. 


```python
N = 50
noise_var = 0.01
X = np.zeros((50, 1))
X[:25, :] = np.linspace(0,3,25)[:,None] # First cluster of inputs/covariates
X[25:, :] = np.linspace(7,10,25)[:,None] # Second cluster of inputs/covariates

# Sample response variables from a Gaussian process with exponentiated quadratic covariance.
k = GPy.kern.RBF(1)
y = np.random.multivariate_normal(np.zeros(N),k.K(X)+np.eye(N)*np.sqrt(noise_var)).reshape(-1,1)
```

First we perform a full Gaussian process regression on the data. We create a GP model, `m_full`, and fit it to the data, plotting the resulting fit.


```python
m_full = GPy.models.GPRegression(X,y)
m_full.optimize() # Optimize parameters of covariance function
m_full.plot() # plot the regression

```

Now we set up the inducing variables, $\mathbf{u}$. Each inducing variable has its own associated input index, $\mathbf{Z}$, which lives in the same space as $\mathbf{X}$. Here we are using the true covariance function parameters to generate the fit.


```python
kern = GPy.kern.RBF(1)
Z = np.hstack(
        (np.linspace(2.5,4.,3),
        np.linspace(7,8.5,3)))[:,None]
m = GPy.models.SparseGPRegression(X,y,kernel=kern,Z=Z)
m.noise_var = noise_var
m.inducing_inputs.constrain_fixed()
#m.tie_params('.*variance')
#m.ensure_default_constraints()
print m # why is it not printing noise variance correctly?
```


```python
m.plot()
```


```python
m.optimize()
m.plot()
```


```python
print m
```


```python
m.randomize()
m.inducing_inputs.unconstrain()
m.optimize()
m.plot()
```

Now we will vary the number of inducing points used to form the approximation. 


```python
m.num_inducing=8
m.randomize()
M = 8
m.Z = np.random.rand(M,1)*12

m.optimize()
m.plot()
m_full.plot()
print m.log_likelihood(), m_full.log_likelihood()
```


```python

```

### Uncertainty about the Provenance of the Data

Provenance could include the time that the data was acquired, the location that the data was acquired, even the 'type' of data that is acquired. For example, in computer vision pixels are arriving from different objects. We are uncertain about the provenance of the pixels in terms of which *object* they are arriving from. The spatial location of the object in the image. This uncertainty relates to uncertainty about the covariance function. Unfortunately, it is not directly on the covariance function itself, but relates to values through which the covariance is nonlinearly related.

$$
k(\mathbf{y}, \mathbf{y}^\prime) = \exp(-||\mathbf{y}-\mathbf{y}^\prime||^2)
$$

These variables become *latent* or *confounders*.

**Not sure about this**: Provenance of data is often finite. Consider a diseased person. That person consists of a finite (if very large) state vector. Of course the number of measurements we can make about that person is infinite. But there are a set of fundamental limitations to what can go wrong with the individual.

## Ethics

Ownership of data, returning it to the individual. In healthcare the danger of confusing it with marketing, Laplace, and the utopian view of data. Invalidity of insurance. How the results are presented to the patient. 

