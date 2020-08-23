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

\section{The Machine Learning and Statistics Interface}

\notes{Machine learning and Statistics are academic cousins, founded on the same mathematical princples, but often with different objectives in mind. But the differences can be as informative as the overlaps.

In [@Efron:prediction20] Efron rightly alludes to the fundamental differences to the new wave of predictive models that have arisen in the last decades of machine learning. And these cultures were also beautifully described by Leo Breiman [@Breiman:cultures00]. 

Although the prediction culture does not sit entirely in the machine learning domain, an excellent example of a prediction focussed approach would be Le Breiman's Bagging [@Breiman:bagging96]. Although it's notable when he chose to publish the outlet was a machine learning journal.

From my personal perspective, the strand of work that is most inspirational in prediction also comes from a statistician. Phil  Dawid's prequential ideas [Dawid:callibrated82,Dawid:prequential84], do provides some hope that a predictive approach can be reconciled with a scientific approach, in the sense that they allow us to falsify poorly calibrated models [@Lawrence:licsbintro10]. 

The quote, apocraphally credited to Disraeli by Mark Twain "There are three kinds of lies: lies, damned lies and statistics" stems from the late 19th century. After Laplace, Gauss, Legendre and Galton and made their forays into regression, but well before Fisher, Pearson and others had begun to formulate statistics on a mathematical basis. Today, the academic discipline of statistics is so widely understood to be underpinned by mathematical rigour that we no longer bother to give the domain its full title of *mathematical statistics*, but the challenges that Efron outlines in [@Efron:prediction20] are part of a new phenomenon, that which was briefly called "big data". In the modern world, we can see that there are still three types of lies: lies damned lies and big data. And the reason is the same as that which infected the late 19th century, the lack of a rigorous mathematical underpinning of this new domain.

Following the revolution of mathematical statistics, data became a carefully curated commodity. It was actively connected in response to a scientific hypothesis. While different approaches to statistical hypothesis testing have been the subject of longstanding debates, there is no controversy around the notion that in order to remove confounders you must have a well designed experiment, and randomization has been a mainstay of statistical data collection for a century now. Randomized trials are used today more so than ever before, in particular due to their widespread use in interface design by large tech companies. Social experiments involving randomization across many millions of users are trivially implementable in real time. These A/B tests dictate our modern user experience. 

Such experiments are still carefully designed to remain valid, but the modern data environment is not only about larger experimental data, but perhaps more so about what I term "happenstance data". Data that was not collected with a particular purpose in mind, but which is simply being recorded in the normal course of events due to increasing interconnection between portable digital devices and decreasing cost of storage. 

Happenstance data are the breadcrumbs of our trail through the forest of life. They may be being written for a particular purpose, but later we wish to consume them for a different purpose. For example, within the recent Covid-19 pandemic, the Royal Society DELVE initiative [@Delve:economics20] was able to draw on transaction data to give near-real time assessments on the effect on GDP[^payments] of the the pandemic and governmental response (see also @Carvalho:tracking20).

[^payments]: Although challenges with availability of payments data within the UK meant that the researchers were able to get good assessment of the Spanish and French economies, but struggled to assess their main target, the United Kingdom.

Historically, data was expensive. It was carefully collected according to a design. Statistical surveys are still expensive, but today there is a strong temptation to do it on the cheap. To use happenstance data to achieve what had been done in the past only through rigorous data-fieldwork. A Professor Efron points out, early attempts to achieve this, such as the Google flu predictor have been somewhat naive [Ginsberg:detecting09,@Halevy:unreasonable09], but as these methodologies are gaining traction in the social sciences [@Salganik:bibbybit18] and the field of Computational Social Science [@Alvarez:computational16] emerges we can expect more innovation and more ideas that may help us bridge the fundamentally different characters of qualitative and quantitative research. For the moment, one particularly promising approach is to use measures derived from happenstance data (such as searches for flu) as proxy indicators for statistics that are rigorously surveilled. With the Royal Society's DELVE initiative, examples of this approach include work of Peter Diggle to visualize the progression of the Covid-19 disease. Across the UK the "Zoe App" has been used for self reporting of Covid symptons [@Menni:tracking20], and by interconnecting this data with Office for National Statistics surveys [@ONS:covid19infection20], Peter has been able to calibrate the Zoe map of Covid-19 prevalence, allowing nowcasting of the diesease that was validated by the production of ONS surveys. These enriched surveys can already be done without innovation to our underlying mathematical 

So the statistical methodologies remain the gold-standard by which these new methodologies should be judged. The situation reminds me somewhat of the challenges Xerox faced with the advent of the computer revolution. With great prescience, Xerox realised that the advent of the computer meant that information was going to be shared more often on screens. As a company whose main revenue stream was coming from photocopying documents the notion of the paperless office represented something of a threat to Xerox. Xerox famously responded by funding their PARC research centre, where many of the innovations that underpin the modern computer were developed: the Xerox Alto (the first graphical user interface), the laser printer, ethernet. These inventions were commercial successes, although often for other companies, but as they propagated there was a greater need for paper. The computers produced more information, and much of it was still shared on paper. Per capita paper consumption continued to rise in the US until it peaked at around the turn of the millenium [@Andres:internet14]. A similar story should now applies with the advent of predictive models and data science. The increasing use of predictive methodologies does not obviate the need for classical statistical approaches, it makes them more important than ever before.

So, we may breathe easy that there is an ongoing role for the classical methodologies we have at our disposal, and historical precedent indicates the demand for those methodologies will likely increase before any fading. What about new mathematical theories? How can we come to a formalism for a new mathematical data science, just as early 20th century statisticians were able to reformulate statistics on a rigorous mathematical footing.

Professor Efron's paper does an excellent job a summarising the range of predictive models that now lie at our disposal, but of particular interest are deep neural networks. This is because they go beyond the traditional notions of what generalisation is or rather, what it has been, to practitioners on both the statistical and machine learning sides of the fence. Perhaps the paper that most clearly demonstrated something was amis was  [@Zhang:understanding17], who trained a large neural network via stochastic gradient descent to label an image data set. Within Professor Efron's categorization of regression model, such a model is a very complex regression model with a particular link function and highly structured adaptive basis functions, which are by tradition called neurons. Despite the structuring of these basis functions (known as convolutional layers), their adaptive nature means that the model contains many millions of parameters. Traditional approaches to generalisation suggest that the model should over fit and [@Zhang:understanding17] proved that such models can do just that. The data they used to fit the model, the training set, was modified. They flipped labels randomly, removing any information in the data. After training, the resulting model was able to classify the training data with 100% accuracy. The experiment clearly demonstrates that all our gravest doubts about overparameterised models are true. If this model has the capacity to fit data which is obviously nonsense, then it is clearly not regularised. Our classical theories suggest that such models should not generalize well on previously unseen data, or test data, but yet the empirical experience is that they do generalize well. So, what's going on?

During a period of deploying machine learning models at Amazon, I was indoctrinated in a set of Leadership Principles, fourteen different ideas to help individual Amazonians structure their thinking. One of them was called "Dive Deep", and a key trigger for a "Dive Deep" was when anecdote and data are in conflict. If there were to be a set of Academic leadership principles, then clearly "Dive Deep" should be triggered when empirical evidence and theory are in conflict. The purpose of the principle within Amazon was to ensure people don't depend overly on anecdotes *or* data when making their decisions, but to develop deeper understandings of their business. In academia, we are equally guilty of relying too much on empirical studies or theory without ensuring they are reconciled. The theoreticians disbelief of what the experimenter tells them is encapsulated in Kahnemann's idea of "theory induced blindness" [@Kahneman:fastslow11]. Fortunately, the evidence for good generalisation in these mammoth models is now large enough that the theory-blinders are falling away and a serious look is being taken and how and why these models can generalize well.

An in depth technical understanding that applies to all these cases is not yet available. But some key ideas are. Firstly, if the neural network model is over-capacity, and can fit nonsense data in the manner demonstrated by [@Zhang:understanding17] then that immediately implies that the good generalization is arising from how the model is fitted to the data. When the number of parameters is so large, the parameters are very badly determined. In machine learning, the concept of version space [@Mitchell:version77] is the subset of all the hypotheses that are consistent with the training examples. For a neural network, the version space is where the neural network parameters (or weights) give predictions for the training data 100% accuracy. A traditional statistical perspective would eschew this regime, convinced that the implication is that overfitting must have occurred. But the empirical evidence from the deep learning community is that these regimes produce classification algorithms with excellent generalization properties. The resolution to this dilemma is *where* in the version space the algorithm comes to rest. 

An excellent characterisation of generalization is normally given by the bias-variance dilemma. The bias-variance decomposition for regression models separates the generalization error into two components [@Geman:biasvariance92].}

\include{_ml/includes/bias-variance-dilemma.md}

One of Breiman's ideas for improving predictive performance is known as Bagging. The idea is to train a number of models on the data such that they overfit (high variance). Then average the predictions of these models. The models are trained on different bootstrap samples and their predictions are aggregated giving us the acronym, Bagging. By combining decision trees with Bagging we recover Random Forests

Bias and variance can be estimated through the Bootstrap, and the traditional view has been that there's a form of Goldilocks effect, where the best predictions are given by the model that is 'just right' for the amount of data available. Not to simple, not too complex. The idea is that bias decreases with increasing model complexity and variance increases with increasing model complexity. Typically plots begin with the Mummy bear on the left (too much bias) end with the Daddy bear on the right (too much variance) and show a dip in the middle where the Baby bear (just) right finds themselves. 

The Daddy bear is typically positioned at the point where the model is able to exactly interpolate the data. For a generalized linear model [@McCullagh:gen_linear89], this is the point at which the number of parameters is equal to the number of data[^assuming]. But the modern empirical finding is that when we move beyond Daddy bear, into the dark forest of the massively overparameterized model we can achieve good generalization.

[^assuming]: Assuming we are ignoring parameters in the link function and the distribution function.

Naturally, as [@Zhang:understanding17] starkly illustrate with their random labels experiment, within the dark forest there are some terrible places, big bad wolves of overfitting that will gobble up your model. But, as empirical evidence shows there is also a safe and hospitable Grandma's house where these highly overparameterised models are safely consumed. Fundamentally, it must be about the route you take through the forest, and the precautions you take to ensure the wolf doesn't see where you're going and beat you to the door.

There are two implications of this empirical result. Firstly, that there is a great deal of new theory that needs to be developed. Secondly, that theory is now obliged to conflate two aspects to modelling that we generally like to keep separate: the model and the algorithm.

Classical statistical theory around predictive generalisation focusses specfically on the class of models that is being used for data fitting. Historically, whether that theory follows a Fisher-aligned estimation approach (see e.g. @Vapnik:book98) or model-based Bayesian approach (see e.g. @Ghahramani:probabilistic15), neither is fully equipped to deal with these new circumstances because, to continue our rather tortured analogy, these theories provide us with a characterisation of the *destination* of the algorithm, and seek to ensure that we reach that destination. Modern machine learning requires theories of the *journey* and what our route through the forest should be. 

Crucially, the destination is always associated with 100% accuracy on the training set. An objective that is always achievable for the overparameterized model.

Intuitively, it seems that a highly over-parameterised model places Grandma's house on the edge of the dark forest. Making it easily and quickly accessible to the algorithm. The larger the model, the more exposed Grandma's house becomes. Perhaps this is due to some form of blessing of dimensionality brings Grandma's house closer to the edge of the forest in a high dimensional stting. Really we should think of Grandma's house as a low dimensional manifold of destinations that are safe. A path through the forest where the wolf of overfitting doesn't venture. In the GLM case, we know already that when the number of parameters matches the number of data there is precisely one location in parameter space where accuracy on the training data is 100%. Our previous misunderstanding of generalization stemmed from the fact that (seemingly) it is highly unlikely that this single point is a good place to be from the perspective of generalization. Additionally, it is often difficult to find. Finding the precise polynomial coefficients in a least squares regression to exactly fit the basis to a small data set such as the Olympic marathon data requires careful consideration of the numerics and an orthogonalization of the design matrix [@Lawson:least95]. 

It seems that with a highly overparameterized model, these locations become easier to find and generalize well. In machine learning this is known as the "double descent phenomenon" (see e.g. @Belkin:reconciling19). 

As Professor Efron points out, modern machine learning models are often fitted using many millions of data points. The most extreme example of late is known as GPT-3. This neural network model, known as a Transformer, has in its largest form 175 billion parameters. The model was trained on a data set containing 499 billion tokens (about 2 Terrabytes of text). Estimates suggest that the model costs around $4.5 million dollars to train (see e.g. @Li:openai20). 


The OpenAI model represents just a recent example from a wave of *deep* neural network models has proved highly
performant across a range of challenges that were previously seen as being beyond our statistical modelling capabilities. 

They stem from the courage of a group of researchers who saw that methods were improving with increasing data and chose to collect and label data sets of ever increasing size, in particular the ImageNet team led by Fei-Fei Li [@Russakovsky-imagenet15] who collected a large data set of images for object detection (currently 14 million images)o. To make these neural network methods work on such large data sets new implementations were required. By deploying neural network training algorithms on graphics processing units (GPUs) breakthrough results were achieved on these large data sets [@Krizhevsky:imagenet12]. Similar capabilities have then been shown in the domains of face identification
[@Taigman:deepface14], and speech recognition [@Hinton:acoustic12], translation [@Sutskever:sequence14] and language modelling [@Radford:language19,@Devlin:bert19]. 

Impressive though these performances are, they are reliant on massive data and enormous costs of training. Yet they can be seen through the lense of regression, as  outlined by Professor Efron in his paper. They map from inputs to outputs. For language modelling, extensive use of auto-regression allows for sequences to be generated. 

## New Methods Required

The challenges of big data emerged due
to companies being able to rapidly interconnect multiple sources of
information. This leads to challenges in storage, distributed processing
and modeling. Google's search engine were at the forefront of this revolution. In
particular they were able to demonstrate that some tasks can be easily
resolved with fairly simple models and very large data sets [@Halevy:unreasonable09]. What we are now learning is that many tasks can be solved with complex models and even bigger data sets. 

While GPT-3 does an impressive job on language generation, it can do so because of the vast quantities of language data we have made available to it. What happens if we take a more complex system, for which such vast data is not available. Or, at least not available in the homogeneous form that language data can be found. Let's take human health. 

Consider we take a holistic view of health and the many ways in which
we can become unhealthy, through genomic and environmental affects. Firstly, let's remember that we don't have a full understanding, even on all the operations in a single eukaryotic cell. Indeed we don't even understand all the mechanisms by which transcription and translation occur in bacterial and archaeal cells. That is despite the wealth of gene expression and protein data
about these cells. Even if we were to pull all this information
together, would it be enough to develop that understanding? Health is an accumulation of 

There are large quantities of data, but the complexity of these systems iIn these
domains we'd argue that even big data is small. The volume of the data
is not large enough to determine the parameters of such complex models.

**Massively multimodal data and Massively Missing Data** Our
understanding of data still seems heavily influenced by the goals of
early statistics. In particular, early mathematical statistics was
heavily influenced by the need to overcome inductive biases in the
human. To do this they encouraged statisticians to collect tables of
data, with a focus on randomised control trials, to remove such
inductive biases and ensure any conclusions drawn were valid. These
developments were absolutely vital in ensuring rigorous evaluation of
statistical claims. Whether it is concious or unconcious we see myriad
examples from marketing and advertising which are designed to appeal to
the, apparently, irrational aspects\footnote{Whether they are
irrational or not depends on how we view them. They are the consequence
of millions of years of evolution and it is only within the last 250
years that we understood the rational basis of probability and companies
were able to exploit areas where people appear irrational to their own
benefit. A particularly depressing read is a section of Laplace's
''Philosophical Essay on Probabilities'' where he advocates a new
utopia based on rational thinking espousing that

> even the common man under the guidance of great minds will begin to
> understand ... [@] TODO check quote.

It is an inspiring quote, until you realise that the reality was more of
a dystopia where large (normally commercial) organisations have become
expert in exploiting those irrational aspects that Laplace began to
identify and individual people have little to no understanding of the
rational basis of uncertainty that Laplace was so convinced would become
endemic.} of humans and trick them to doing something which is not to
their individual benefit, but is profitable for the (normally corporate)
entity that is doing the marketing. This may not matter a great deal
when we are buying pet insurance or a new jacket, but is extremely
dangerous when we are making claims for a particular drug to patients.
Classical statistics acts as our final guardian against these claims,
and even then it is subject to manipulation through failure to report on
negative results.[^2]

[^2]: I was once railing against the limitations
of classical statistics to Darren Wilkinson and Joe Whittaker at a very
pleasant meeting in the Lorenz institute, organized by Ernst Wit. It was
Joe Whittaker that drove home this important point to me, although the
connection to the Laplace quote is my own. That came from reading his
Philosophical Essay on Probabilities, and for a moment I became carried
away with him, when he glorified in the new world of rationality, until
I was brought back to the present reality with an unpleasant jolt, in
particular due to the stories about 'Fixed Odds Betting Machines' that
were in the British media at the time. Laplace singles out games where
the odds are stacked against the player a 'particular evil' TODO
check. I'm not one for absolutes, but I think I'd agree with the idea
that a larger entity, which has a deep understanding of rational
behavior, exploiting a vulnerable smaller entity, who has little
understanding of it, does come close to such evils.

However, classical
statistics does seem to give us a peculiar bias to tables of data: data
where someone has carefully collected all the relevant features about
the particular entites we are focussed on. That is a very different
challenge to that of machine learning. In talks about this I like to
tell the audience that my mum drives an Humvee. I then ask them what the
audience thinks about that, what it makes them think about my mum.
Certainly they probably think she's unusual. Maybe it also affects what
they think about me. Of course, she actually drives a VW Golf, which
makes her much more of a normal mum. Importantly, the audience didn't
know I was going to say that before I started, but they were able to
assimilate new information about the entity (my mum) through a feature
they may have known existed, but they were unlikely to have predicted I
was going to use before the talk. If we think about clinical data, the
situation is even more extreme. If we are going to track someone's
health state throughout their life then we need to build models that
might need to take into account clinical tests that don't even exist
yet. This is not an unusual situation, in fact it is the normal
situation. The table of carefully collected statistical values is the
unusual (and valuable) situation. That's why so much attention is
normally given to experimental design in statistics. But if we don't
have those controls what should we do? First we should recognize that
missing data is the norm, not the exception: even when the table of data
we collected is full there are probably many more things we *could have*
collected but didn't. Secondly we should recognise that the missing
data normally dominates. It would be impossible to enumerate all the
different types of data we would be missing for any complex system. The
technique of imputation is suitable when missing data is only up to
around half of our data set. The real world presents the challenge of
massively missing data. Whenever you are doing analysis you are looking
only a very tiny fraction of the things you could know. Interestingly,
the visual and auditory systems present interesting counter examples to
this analysis. Ignoring context (and concepts like sensor fusion) we can
certainly think of the auditory and visual systems as presenting fixed
dimensional signals about the entities they observe. This may explain
why such success has been possible in these domains. But, from another
perspective, both visual and auditory systems are *just* a very complex
sensor. And in the type of intelligence we envisage we could have an
arbitary number of sensors, and new sensors could be developed at all
times. To understand the entire scene we must be able to incorporate
such sensors as they are produced. Computational researchers who have
worked in the biological sciences will know that over recent years
sensorics has developed at such a rate that the most success can be
garned by being the first to apply any method (typically PCA) to the
sensoring domain, and that we all barely have time to catch our breath
before the next generation of sensorics may render our work on the
previous generation obsolete. What doesn't change though, is the
validity of the underlying modelling techniques that attempt to
assimilate these data into a coherent whole.

Consider the challenges of a highly multimodal domain like health data.
Whilst we have ensured through clever engineering that speech and

The wave of Developing the hypothesis that the main reason that these
models became neglected was because there was not enough data to justify
their implementation we advocate a return to tmotivate a return It is
arguable that the main reason that





Machine learning involves taking data and combining it with a model in
order to make a prediction. The data consist of measurements recorded
about the world around us. A model consists of our assumptions about how
the data is likely to interrelate, typical assumptions include
smoothness. Our assumptions reflect some undelying belief about the
regularities of the universe that we expect to hold across a range of
data sets.


$$\text{data} + \text{model} \rightarrow \text{prediction}$$


From my perspective, the model is where all the innovation in machine
learning goes. The etymology of the data indicates that it is given
(although in some cases, such as active learning, we have a choice as to
how it is gotten), our main control is over the model. This is the key
to making good predictions. The model is a mathematical abstraction of
the regularities of the universe that we believe underly the data as
collected. If the model is chosen well we will be able to interpolate
the data and precit likely values of future data points. If it is chosen
badly our predictions will be overconfident and wrong.

### Models vs Algorithms

Much of the technical focus in machine learning is on algorithms. In
this document I want to retain a strong separation between the *model*
and the *algorithm*. The model is a mathematical abstraction of the
world that encapsulates our assumptions about the data. Normally it will
depend on one or more parameters which are adaptable. The algorithm
provides a procedure for adapting the model to different contexts, often
through the provision of a set of data that is used for training the
model.


Despite the different role of model and algorithm, the two concepts are
often conflated. This sometimes leads to a confused discussion. I was
recently asked "Is it correct to remove the mean from the data before
you do principal component analysis." This question is about an
algorithmic procedure, but the correct answer depends on what modelling
assumption you are seeking to make when you are constructing your
principal component analysis. Principal component analysis was
originally proposed by a *model* for data by [@Hotelling:analysis33]. It is a latent variable model that was directly
inspired by work in the social sciences on factor analysis. However,
much of our discussion of PCA today focusses on PCA as an algorithm. The
algorithm for fitting the PCA model is to seek the eigenvectors of the
covariance matrix, and people often refer to this algorithm as principal
component analysis. However, that algorithm also finds the linear
directions of maximum variance in the data. Seeking directions of
maximum variance in the data was not the objective of Hotelling, but it
is related to a challenge posed by @Pearson:01
who sought a variant of regression that predicted symmetrically
regardless of which variable was considered to be the covariate and
which variable the response. Coincidentally the algorithm for this model
is also the eigenvector decomposition of the covariance matrix. However,
the underlying model is different. The difference becomes clear when you
begin to seek non-linear variants of principal component analysis.
Depending on your interpretation (finding directions of maximum variance
in the data or a latent variable model) the corresponding algorithm
differs. For the Pearson model a valid non-linearization is kernel PCA
`<cite nodata-cite="Schoelkopf:">`{=html}(Schoelkopf et al,
1999)`</cite>`{=html}, but for the Hotelling model this generalization
doesn't make sense. A valid generalization of the Hotelling model is
provided by the Gaussian process latent variable model
`<cite nodata-cite="Lawrence:pnpca05">`{=html}(Lawrence,
2005)`</cite>`{=html}. This confusion is often unhelpful, so for the
moment we will leave algorithmic considerations to one side and focus
*only* on the model.


## Is my Model Useful?


> All models are wrong, but some are useful
>
> @Box:science76


This important quote has become worn by overuse (like a favourite
sweater). Worse still it is almost being bandied around to mean that
*because* my model is wrong it *might* be useful. It seems that people
almost equate the statement to meaning probobability of my model being
wrong given that its useful is = 1. Which would be an incorrect model,
but seems to be useful in practice when trying to justify poor
assumptions.


Perhaps we should be more focussing on the quote \"\... the scientist
must be alert to what is importantly wrong. It is inappropriate to be
concerned about mice when there are tigers abroad.\" from the same
paper. Let's have a think about where the tigers might be in the domain
of big data. To consider this, let's first see what we can write down
about our data that isn't implicitly wrong. If we are interested in
multivariate data we could first write down our data in the following
form.


$$\text{data} = \mathbf{\dataMatrix} \in \Re^{\numData\times \dataDim},$$


where here we are assuming we have $\numData$ data points and $\dataDim$
features. However, as soon as we write down our data in this form it
invites particular assumptions about your data that were valid, perhaps
in the 1930s, when people were worried about tables of data. They
collected tables of data with a specific purpose in mind and the data
naturally sat in a matrix. Immediately we write down our data in a
matrix form, $\dataMatrix\in \Re^{\numData\times \dataDim}$ it is
somehow implicit that we are suggesting factorization assumptions across
the $\numData$ data points.

\begin{align*}
p(\dataMatrix) = \prod_{i=1}^\numData p(\dataVector_{i, :} \| \boldsymbol{\theta})
\end{align*}



This assumption allows us to easily make predictions about new data
points given a parameter vector that is derived from the training data.
This assumptions will generally be wrong, and also leads to concerns
about the parameters when $\numData<<\dataDim$, the so called \`large
$\dataDim$, small $\numData$' domain. They also lead to concerns such
as large $\dataDim$, small $\numData$ concerns.


I think that this is a wrongheaded way of thinking about modern data,
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
they should *not* be the first thing we write down.


### A Motivating Big Data Example


Statisticians like Pearson, Fisher and Student worked with tables of
data that they'd carefully collected, often with the specific purpose
of answering a particular question. The decided at experiment *design*
time what was to be measured $\numData$. The number of samples was
determined by statistical power calculations *CHECK THIS*, this was
something that could be varied.


One of my own interests is personalized health: what we can learn about
patients' state of health and when we should make an interviention. In
the big data era, we aren't only interested in what data we might
collect for answering a specific question (although data of this type
remains very important) but we are also interested in existing data that
might be assimilated to improve our understanding of an individual's
health. When imagining future systems that monitor our health status, we
should not be restricted to the type of data that might be stored in a
doctor's office or a hospital data base. Indeed, it might be argued
that such data focusses on sickness rather than health, giving us an
incomplete picture.


Modern data availabilities means that we could build models that
incorporate an individual's exercise regime (for example through
websites such as Strava and Endomomndo). We could include information
about an individual's dietary habits (e.g. through loyalty card
information like the Nectar card). If we were monitoring potential
degradation in health then we may also be interested in an individual's
social network activity (Twitter, Facebook, Google+). Even musical
tastes may feed in to our overall picture of the patient's well being
through music services like spotify. For a full perspective on a
patient's health, this data would need to be combined with more
traditional sources phenotype and genotyp infomration. For example, high
resolution scans of the genome providing a detailed characterization of
genotype. Large scale gene expression measurements, giving detailed
insights into phenotype at the cellular level. Images containing x-rays
or biopsies. Doctor's notes, but handwritten and those that encode a
diangosis. Clinical tests, for example in cardiovascular disease
cholestorol level. To provide a full picture of health status all this
information needs to be assimilated. In a traditional model, we might
encode each piece of information as another element on a feature vector:
in other words, all the above contributes to increasing $\dataDim$.
However, for most patients, most of the information above is likely to
be missing. The paradigm of missing data is often discussed, but in this
domain we have a situation we might refer to as *massivelv missing
data*. A situation where a missing value becomes the norm rather than an
exception.


Another facet of the personalized health problem will be the streaming
nature of data. When acquiring data passively data doesn't arrive in
blocks, it arrives in a haphazard fashion. Our model may need to update
because patient 2,342 has just had the results of a blood test logged,
or because patient 28,344,219 has just been for a run or because patient
12,012,345 just listened to a Leonard Cohen track or because patient
12,182 just gave birth.


One possible motivation for making independence assumptions across data
points is the ease with which predictions can be made for a previously
unseen vector $\dataVector^*$. Given an estimate of a vector of
parameters, $\hat{\paramVector}$, perhaps obtained by optimizing the
likelihood on the training data, then due to our assumption of
independence across data then we can easily predict for the new point
using the conditional distribution:
$$
p(\dataVector_*|\hat{\paramVector}).
$$
Perhaps, though, we should find this ease of prediction suspicious.
Let's momentarily examine what we are really saying here. We are
assuming that all the information we wish to store about the world, and
communicate to a test data set is storable in a parameter vector,
$\paramVector$, the nature of which (for example its length) is set at
design time, before we've seen the data. That is precisely the meaning
of statistical *independence given the parameters*.


For applications like the personalized health monitoring system
described above, we need a model that will give well calibrated
predictions from the first day of it being brought on line, and
throughout its operational life. If the model is complex enough to
represent the full spectrum of possible human ailments, then when the
model is first brought on stream, it is unlikely to have sufficient data
to determine the parameters. In the standard modeling framework we are
faced with the bias variance dilema 
`<cite data-cite=\"Geman:bias92\">`{=html}(Geman et al,
1992)`</cite>`{=html}. If the model is complex enough to represent the
underlying data structure, the parameters will be badly determined for
small, or badly designed data sets, and the model will exhibit a large
error due to variance. A traditional solution is to err towards bias, by
constructing a simpler model, but one where the parameters can be well
determined by the data, we reduce variance at the expense of some bias.
In the context of our medical application, there are three major
problems with this approach. Firstly, the size and scope of the data is
continually evolving: we do not have a fixed design. This means that
even if we were to find a good initial compromise between bias and
variance, this compromise may be rapidly invalidated. Secondly, the
compromise we find would have to apply equally to all patients despite
the diversity of data we have associated with those patients. Finally,
we should fear the confidence of predictions from a model with well
determined parameters unless we truly believe we have sufficient data to
capture some underlying deterministic truth. Medical outcome is laced
with uncertainty, and this uncertainty needs to be modeled correctly
because its structure has a significant effect on treatment.

A major challenge in the domain we've described is to build a model
that is complex enough to represent the diversity of human health
outcomes. For streaming data this necessarily means that some of those
parameters will be badly determined. I'd also argue further that if the
parameters are well determined this is actually a warning. If all
parameters are well determined, then our assumption of statistical
independence becomes a strong one: the residual uncertainty is only in
the noise, which by its independent nature, is impossible to model.
However, any uncertainty in the parameters gives a much more structured
uncertainty distribution for the data.


### Uncertainty in Parameters


If the parameters are badly determined, then small fluctuations in the
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
independent, either across features or data points.


### Massively Missing Data


I'd like to argue that the separation of the data into features and
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
is outdated when considering modern big data problems.


The modern data analysis challenge is very different. We receive
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
or the cell, or human health) then almost all the data is missing.

\plotcode{
% Define nodes
\draw node[obs] (y) {$\dataVector$};
\end{tikzpicture}
%\end{figure}
}


A model that's not wrong, just not useful. I like graphical
representations of probabilistic models and this is my favourite graph.
It is the most simple but also the most general. It says that all the
data in our vector $\dataVector$ is governed by an unspecified
probability disribution $p(\dataVector)$. Graphical models normally
express the conditional independence relationships in the data, with
this graph we are not a priori considering any such relationships. This
is the most general model (it includes all factorized models as special
cases). It is not wrong, but since it doesn't suggest what the next
steps are or give us any handles on the problem it is also not useful.


This is the nature of modern streaming data, what has been called big
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
block of information.


To deal with massively missing data we need to think about the
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
sum rule of probability we have


\begin{align*} p(\dataVector\|\numData^*) = \int p(\dataVector,
\dataVector^*) \text{d}\dataVector^* \end{align*}


where the dependence of the marginal distribution for $\dataVector$
aries from the fact that we are forming an $\numData^*$ dimensional
integral over $\dataVector^*$. If our distribution is Kolmogorov
consistent, then we know that the distribution over $\dataVector$ is
*independent* of the value of $\numData^*$. So in other words
$p(\dataVector|\numData*)=p(\dataVector)$. So Kolmogorov consistency
says that the form of $p(\dataVector)$ remains the same *regardless* of
the number of observations of the world that are yet to come.


Parametric Models
-----------------


We can achieve Kolomogrov consistency almost trivially in a parametric
model if we assume that the probability distribution is independent
given the parameters. Then the property of being closed under
marginalization is trivially satisfied through the independence,


\begin{align*}p(\dataVector, \dataVector^*) = \int
\prod_{i=1}^\numData p(\dataScalar_{i} \|
\boldsymbol{\theta})\prod_{i=1}^{\numData^*}p(\dataScalar^*_i\|\boldsymbol{\theta})
p(\paramVector) \text{d}\paramVector\end{align*}


which allows us to marginalize for all future data leaving a joint
distribution which isn't dependent on $\numData^*$ because each future
data point can be marginalized independently.


\begin{align*}p(\dataVector) = \int \prod_{i=1}^\numData
p(\dataScalar_{i} \|
\boldsymbol{\theta})\prod_{i=1}^{\numData^*} \int
p(\dataScalar^*_i\|\boldsymbol{\theta})
\text{d}\dataScalar^*_i p(\paramVector)
\text{d}\paramVector\end{align*}


But, as we've already argued, this involves an assumption that is often
flawed in practice. It is unlikely that, in a complex model, we will be
able to determine the parameter vector well enough, given limited data,
for us to truly believe that all the information about the training data
that is required for predicting the test data could be passed through a
fixed length parameter vector. This is what this independence assumption
implies. If we consider that the model will also be acquiring new data
at run time, then there is the question of hot to update the parameter
vector in a consistent manner, accounting for new information, e.g. new
clinical results in the case of personalized health.


Conversely, a general assumption about independence across *features*
would lead to models which *don't* exhibit *Komlogorov consistency*. In
these models the dimensionality of the test data, $\dataVector^*$,
denoted by $\numData^*$ would have to be fixed and each
$\dataScalar^*_i$ would require marginalization. So the nature of the
test data would need to be known at model *design* time.


Parametric Bottleneck
---------------------


In practice Bayesian methods suggest placing a prior over
$\boldsymbol{\theta}$ and using the posterior,
$p(\boldsymbol{\theta}|\dataVector)$ for making predictions.


\begin{align*} p(\dataVector^*\|\dataVector) = \int \prod_i
p(\dataScalar_i^* \| \boldsymbol{\theta})
p(\boldsymbol{\theta}\|\dataVector)\text{d}\boldsymbol{\theta}
\end{align*}


We have a model that obeys Kolmogorov consistency, and is sophisticated
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
$\boldsymbol{\theta}$ should be *non parametric*.


$$p(\paramVector | \dataVector)$$


which, as we argued above, allows us to retain the necessary sense of
uncertainty about the parameters that is required in a very complex
system when we have seen relatively little data. How much information
can we store, then, about the training data? The information gain from
the training data is given by the Kullback Leibler divergence between
our prior distribution and our posterior distribution.


$$\KL{p(\paramVector|\dataVector)}{p(\paramVector)}$$


This is the information gained, measured in 'nats' if we use natural
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
concave.


The Non-parametric Challenge
----------------------------

We have argued that we want models that are unconstrained, at design
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
it also presents a problem.


Human beings, despite are large, interconnected brains, only have finite
storage. Similar for digital computers. So we need to assume that we can
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
*run time* not simply at design time.


### The Multivariate Gaussian: Closure Under Marginalization


Being closed under marginalization is a remarkable property of our old
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
must depend only on the two indices associated with $\dataVector$.


vec ihis implies that the covariance matrix must be dependent only Since
the covariance matrix is specified pairwise, dependent only on the index
of the two observations $\dataScalar_i$ and $\dataScalar_j$ for which
the covariance is being computed. In general we can also think of this
index as being infinite: it could be a spatial or temporal location.


\begin{align*} p(\dataVector) = \int p(\dataVector, \dataVector^*)
\text{d}\dataVector^*=
\frac{\exp\left(\begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}^\top\begin{bmatrix}\kernelMatrix &
\kernelMatrix_*\ \kernelMatrix_*^\top &
\kernelMatrix_{**}\end{bmatrix}^{-1} \begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}\right)}{\int
\exp\left(\begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}^\top\begin{bmatrix}\kernelMatrix &
\kernelMatrix_*\ \kernelMatrix_*^\top &
\kernelMatrix_{**}\end{bmatrix}^{-1} \begin{bmatrix}\dataVector\
\dataVector^*\end{bmatrix}\right) \text{d}\dataVector
\text{d}\dataVector^*} = \mathcal{N}(\mathbf{0} \|\kernelMatrix)\
\end{align*}


where each $\dataScalar_i$ is now defined across the real line, and the
dimensionality of $\dataVector*$ is irrelevant. Prediction consists of
conditioning the joint density on $\dataVector^*$. So for any new value
of $\dataVector^*$, given its index we compute
$p(\dataVector^* | \dataVector)$.


Making Parameters non-Parametric
--------------------------------


We will start by introducing a set of variables, $\inducingVector$, that
are finite dimensional. These variables will eventually be used to
communicate information between the training and test data, i.e. across
the TT channel.


$$
p(\dataVector^*|\dataVector) = \int p(\dataVector^*|\inducingVector) q(\inducingVector|\dataVector) \text{d}\inducingVector
$$


where we have introduced a distribution over $\inducingVector$,
$q(\inducingVector|\dataVector)$ which is not necessarily the true
posterior distribution.
:::

::: {.cell .code execution_count="4"}
``` {.python}
%%tikz --size 180,180 -f svg
\begin{tikzpicture}[scale=2]
% Define nodes
\draw node[obs] (y) {$\dataVector$};
\draw node[latent, above=of y] (u) {$\inducingVector$};

\draw [-] (u) to (y);%
\end{tikzpicture}
```
:::

::: {.cell .code markdown}


Our simple graphical model augmented with $\inducingVector$ which we
refer to as inducing variables. Note that the model is still totally
general because $p(\dataVector, \inducingVector)$ is an augmented
variable model and the original $p(\dataVector)$ is easily recovered by
simple marginalization of $\inducingVector$. We haven't yet made any
assumptions about our data.


The model we've introduced now seems remarkably like the parametric
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
that If we build a joint density as follows:


\begin{align*} p(\dataVector, \inducingVector\|\numInducing^*,
\numData^*) = \int p(\dataVector^*, \dataVector,
\inducingVector^*, \inducingVector) \text{d}\dataVector^*
\text{d}\inducingVector^* \end{align*}


where $\inducingVector$ are the inducing variables we choose might
choose to instantiate at any given time (of dimensionality
$\numInducing$) and $\inducingVector^*$ is the $\numInducing^*$
dimensional pool of future inducing variables we have *not yet* chosen
to instantiate (where $\numInducing^*$ could be infinite). Our new
Kolmogorov consistency condition requires that
$$
p(\dataVector, \inducingVector|\numInducing^*,\numData^*) = p(\dataVector, \inducingVector).
$$
It doesn't need to be predetermined at *design time* because we allow
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
hand.
:::

::: {.cell .code execution_count="5"}
``` {.python}
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
\end{tikzpicture}
 
```

::: {.output .stream .stderr}
    pdf2svg terminated with signal -127
    No image generated.
:::


Adding in the test data and the inducing variables we have not yet
chosen to instantiate. Here we see that we still haven't defined any
structure in the graph, and therefore we have not yet made any
assumptions about our data. Not shown in the graph is the additional
assumption that whilst $\dataVector$ has $\numData$ dimensions and
$\inducingVector$ has $\numInducing$ dimensions, $\dataVector^*$ and
$\inducingVector^*$ are potentially infinite dimensional.


### Fundamental Variables


To focus our model further, we assume that we observe observations,
$\dataVector$ that are derived from some underlying fundamental,
$\mappingFunctionVector$, through simple factorized likelihoods. The
idea of the fundamental variables is that they are sufficient to
describe the world around us, but we might not be able to observe them
directly. In particular we might observe relatively simple corruptions
of the fundamental variables such as independent addition of noise, or
thresholding. We might observe something relative about two fundamental
veriables. For example if we took $\mappingFunction_12,345$ to be the
height of Tom Cruise and $\mappingFunction_23,789$ to be the height of
Penelope Cruz then we might take for an observation a binary value
indicating the relative heights, so
$\datascalar_72,394 = \mappingFunction_12,345 < \mappingFunction_23,789$.
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
therefore the formulation is still totally general.


$$p(\dataVector|\numData^*) = \int p(\dataVector|\mappingFunctionVector) p(\mappingFunctionVector, \mappingFunctionVector^*)\text{d}\mappingFunctionVector \text{d}\mappingFunctionVector^*$$


and since we enforce Kolmogorov consistency we have


$$p(\dataVector|\numData*) = p(\dataVector)$$
:::

::: {.cell .code execution_count="6"}
``` {.python}
%%tikz --scale 2 --size 300,300 -f svg
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
\end{tikzpicture}
 
```

::: {.output .stream .stderr}
    pdf2svg terminated with signal -127
    No image generated.
:::


Now we assume some form of factorization for our data observations,
$\dataVector$, given the fundamental variables,
$\mappingFunctionVector$, so that we have
$$
p(\dataVector|\mappingFunctionVector) = \prod_{i} p(\dataVector^i| \mappingFunctionVector^i)
$$
so that we have subsets of the data $\dataVector^i$ which are dependent
on sub sets of the fundamental variables, $\mappingFunction$. For
simplicity of notation we will assume a factorization across the entire
data set, so each observation, $\dataScalar_i$, has a single underlying
fundamental variable, $\mappingFunction_i$, although more complex
factorizations are also possible and can be considered within the
analysis.
$$
p(\dataVector|\mappingFunctionVector) = \prod_{i=1}^\numData p(\dataScalar_i|\mappingFunction_i)
$$
:::

::: {.cell .code execution_count="7"}
``` {.python}
%%tikz --size 300,300 -f svg
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
\end{tikzpicture}
        
 
```

::: {.output .stream .stderr}
    pdf2svg terminated with signal -127
    No image generated.
:::


We now decompose, without loss of generality, our joint distribution
over inducing variables and fundamentals into the following parts


$$p(\inducingVector, \mappingFunctionVector) = p(\mappingFunctionVector|\inducingVector)p(\inducingVector)$$


where we assume that we have marginalised $\mappingFunctionVector^*$ and
$\inducingVector^*$.


:::

::: {.cell .code execution_count="8"}
``` {.python}
%%tikz --size 300,300 -f svg
% Define nodes
\begin{tikzpicture}[scale=1]
\draw node[obs] (y) {$\dataScalar_i$};
\draw node[latent, above=of y] (f) {$\mappingFunction_i$};
\draw node[latent, above=of f] (u) {$\inducingVector$};
        
% Connect the nodes
\draw [->] (f) to (y);%
\draw [->] (u) to (f);%

\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots\numData$} ;
\end{tikzpicture}
```

::: {.output .stream .stderr}
    pdf2svg terminated with signal -127
    No image generated.
:::
:::

::: {.cell .code execution_count="9"}
``` {.python}
%%tikz --scale 2 --size 300,300 -f svg
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
\end{tikzpicture}
 
```

::: {.output .stream .stderr}
    pdf2svg terminated with signal -127
    No image generated.
:::
:::

::: {.cell .code execution_count="10"}
``` {.python}
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
\end{tikzpicture}
```

::: {.output .stream .stderr}
    pdf2svg terminated with signal -127
    No image generated.
:::
:::

::: {.cell .code execution_count="11"}
``` {.python}
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
        
 
```

::: {.output .stream .stderr}
    LaTeX terminated with signal -1
    pdf2svg terminated with signal -127
    No image generated.
:::

::: {.output .display_data}
    This is pdfTeX, Version 3.1415926-2.5-1.40.14 (TeX Live 2013) (format=pdflatex 2014.2.5)  9 OCT 2014 07:01
    entering extended mode
     \write18 enabled.
     %&-line parsing enabled.
    **tikz.tex
    (./tikz.tex
    LaTeX2e <2011/06/27>
    Babel <3.9f> and hyphenation patterns for 78 languages loaded.
    (/usr/local/texlive/2013/texmf-dist/tex/latex/standalone/standalone.cls
    Document Class: standalone 2012/09/15 v1.1b Class to compile TeX sub-files stan
    dalone
    (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/ifluatex.sty
    Package: ifluatex 2010/03/01 v1.3 Provides the ifluatex switch (HO)
    Package ifluatex Info: LuaTeX not detected.
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/ifpdf.sty
    Package: ifpdf 2011/01/30 v2.3 Provides the ifpdf switch (HO)
    Package ifpdf Info: pdfTeX in PDF mode is detected.
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/ifxetex/ifxetex.sty
    Package: ifxetex 2010/09/12 v0.6 Provides ifxetex conditional
    )
    (/usr/local/texlive/2013/texmf-dist/tex/latex/xkeyval/xkeyval.sty
    Package: xkeyval 2012/10/14 v2.6b package option processing (HA)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/xkeyval/xkeyval.tex
    \XKV@toks=\toks14
    \XKV@tempa@toks=\toks15
    \XKV@depth=\count79
    File: xkeyval.tex 2012/10/14 v2.6b key=value parser (HA)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/xkeyval/keyval.tex)))
    \sa@internal=\count80

    (/usr/local/texlive/2013/texmf-dist/tex/latex/standalone/standalone.cfg
    File: standalone.cfg 2012/09/15 v1.1b Default configuration file for 'standalon
    e' class
    )
    (/usr/local/texlive/2013/texmf-dist/tex/latex/base/article.cls
    Document Class: article 2007/10/19 v1.4h Standard LaTeX document class
    (/usr/local/texlive/2013/texmf-dist/tex/latex/base/size10.clo
    File: size10.clo 2007/10/19 v1.4h Standard LaTeX file (size option)
    )
    \c@part=\count81
    \c@section=\count82
    \c@subsection=\count83
    \c@subsubsection=\count84
    \c@paragraph=\count85
    \c@subparagraph=\count86
    \c@figure=\count87
    \c@table=\count88
    \abovecaptionskip=\skip41
    \belowcaptionskip=\skip42
    \bibindent=\dimen102
    )
    \sa@box=\box26
    runsystem(pdflatex  -shell-escape  -jobname 'tikz' '\expandafter\def\csname sa@
    internal@run\endcsname{1}\input{tikz}')...executed.

    runsystem(convert -density 300 tikz.pdf -resize 300x300 -quality 90 tikz.png)..
    .executed.



    Class standalone Warning: Conversion unsuccessful!
    (standalone)              There might be something wrong with your
    (standalone)              conversation software or the file permissions!

    ) (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/frontendlayer/tikz.sty
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/basiclayer/pgf.sty
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/utilities/pgfrcs.sty
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/utilities/pgfutil-common.te
    x
    \pgfutil@everybye=\toks16
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/utilities/pgfutil-latex.def
    \pgfutil@abb=\box27
    (/usr/local/texlive/2013/texmf-dist/tex/latex/ms/everyshi.sty
    Package: everyshi 2001/05/15 v3.00 EveryShipout Package (MS)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/utilities/pgfrcs.code.tex
    Package: pgfrcs 2010/10/25 v2.10 (rcs-revision 1.24)
    ))
    Package: pgf 2008/01/15 v2.10 (rcs-revision 1.12)
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/basiclayer/pgfcore.sty
    (/usr/local/texlive/2013/texmf-dist/tex/latex/graphics/graphicx.sty
    Package: graphicx 1999/02/16 v1.0f Enhanced LaTeX Graphics (DPC,SPQR)

    (/usr/local/texlive/2013/texmf-dist/tex/latex/graphics/graphics.sty
    Package: graphics 2009/02/05 v1.0o Standard LaTeX Graphics (DPC,SPQR)

    (/usr/local/texlive/2013/texmf-dist/tex/latex/graphics/trig.sty
    Package: trig 1999/03/16 v1.09 sin cos tan (DPC)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/latex/latexconfig/graphics.cfg
    File: graphics.cfg 2010/04/23 v1.9 graphics configuration of TeX Live
    )
    Package graphics Info: Driver file: pdftex.def on input line 91.

    (/usr/local/texlive/2013/texmf-dist/tex/latex/pdftex-def/pdftex.def
    File: pdftex.def 2011/05/27 v0.06d Graphics/color for pdfTeX

    (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/infwarerr.sty
    Package: infwarerr 2010/04/08 v1.3 Providing info/warning/error messages (HO)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/ltxcmds.sty
    Package: ltxcmds 2011/11/09 v1.22 LaTeX kernel commands for general use (HO)
    )
    \Gread@gobject=\count89
    ))
    \Gin@req@height=\dimen103
    \Gin@req@width=\dimen104
    )
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/systemlayer/pgfsys.code.tex
    Package: pgfsys 2010/06/30 v2.10 (rcs-revision 1.37)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex
    \pgfkeys@pathtoks=\toks17
    \pgfkeys@temptoks=\toks18

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/utilities/pgfkeysfiltered.c
    ode.tex
    \pgfkeys@tmptoks=\toks19
    ))
    \pgf@x=\dimen105
    \pgf@y=\dimen106
    \pgf@xa=\dimen107
    \pgf@ya=\dimen108
    \pgf@xb=\dimen109
    \pgf@yb=\dimen110
    \pgf@xc=\dimen111
    \pgf@yc=\dimen112
    \w@pgf@writea=\write3
    \r@pgf@reada=\read1
    \c@pgf@counta=\count90
    \c@pgf@countb=\count91
    \c@pgf@countc=\count92
    \c@pgf@countd=\count93

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/systemlayer/pgf.cfg
    File: pgf.cfg 2008/05/14  (rcs-revision 1.7)
    )
    Package pgfsys Info: Driver file for pgf: pgfsys-pdftex.def on input line 900.

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-pdftex.d
    ef
    File: pgfsys-pdftex.def 2009/05/22  (rcs-revision 1.26)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/systemlayer/pgfsys-common-p
    df.def
    File: pgfsys-common-pdf.def 2008/05/19  (rcs-revision 1.10)
    )))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/systemlayer/pgfsyssoftpath.
    code.tex
    File: pgfsyssoftpath.code.tex 2008/07/18  (rcs-revision 1.7)
    \pgfsyssoftpath@smallbuffer@items=\count94
    \pgfsyssoftpath@bigbuffer@items=\count95
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/systemlayer/pgfsysprotocol.
    code.tex
    File: pgfsysprotocol.code.tex 2006/10/16  (rcs-revision 1.4)
    )) (/usr/local/texlive/2013/texmf-dist/tex/latex/xcolor/xcolor.sty
    Package: xcolor 2007/01/21 v2.11 LaTeX color extensions (UK)

    (/usr/local/texlive/2013/texmf-dist/tex/latex/latexconfig/color.cfg
    File: color.cfg 2007/01/18 v1.5 color configuration of teTeX/TeXLive
    )
    Package xcolor Info: Driver file: pdftex.def on input line 225.
    Package xcolor Info: Model `cmy' substituted by `cmy0' on input line 1337.
    Package xcolor Info: Model `hsb' substituted by `rgb' on input line 1341.
    Package xcolor Info: Model `RGB' extended on input line 1353.
    Package xcolor Info: Model `HTML' substituted by `rgb' on input line 1355.
    Package xcolor Info: Model `Hsb' substituted by `hsb' on input line 1356.
    Package xcolor Info: Model `tHsb' substituted by `hsb' on input line 1357.
    Package xcolor Info: Model `HSB' substituted by `hsb' on input line 1358.
    Package xcolor Info: Model `Gray' substituted by `gray' on input line 1359.
    Package xcolor Info: Model `wave' substituted by `hsb' on input line 1360.
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcore.code.tex
    Package: pgfcore 2010/04/11 v2.10 (rcs-revision 1.7)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmath.code.tex
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathcalc.code.tex
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathutil.code.tex)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathparser.code.tex
    \pgfmath@dimen=\dimen113
    \pgfmath@count=\count96
    \pgfmath@box=\box28
    \pgfmath@toks=\toks20
    \pgfmath@stack@operand=\toks21
    \pgfmath@stack@operation=\toks22
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.code.
    tex
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.basic
    .code.tex)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.trigo
    nometric.code.tex)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.rando
    m.code.tex)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.compa
    rison.code.tex)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.base.
    code.tex)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.round
    .code.tex)
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfunctions.misc.
    code.tex)))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/math/pgfmathfloat.code.tex
    \c@pgfmathroundto@lastzeros=\count97
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepoints.co
    de.tex
    File: pgfcorepoints.code.tex 2010/04/09  (rcs-revision 1.20)
    \pgf@picminx=\dimen114
    \pgf@picmaxx=\dimen115
    \pgf@picminy=\dimen116
    \pgf@picmaxy=\dimen117
    \pgf@pathminx=\dimen118
    \pgf@pathmaxx=\dimen119
    \pgf@pathminy=\dimen120
    \pgf@pathmaxy=\dimen121
    \pgf@xx=\dimen122
    \pgf@xy=\dimen123
    \pgf@yx=\dimen124
    \pgf@yy=\dimen125
    \pgf@zx=\dimen126
    \pgf@zy=\dimen127
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathconst
    ruct.code.tex
    File: pgfcorepathconstruct.code.tex 2010/08/03  (rcs-revision 1.24)
    \pgf@path@lastx=\dimen128
    \pgf@path@lasty=\dimen129
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathusage
    .code.tex
    File: pgfcorepathusage.code.tex 2008/04/22  (rcs-revision 1.12)
    \pgf@shorten@end@additional=\dimen130
    \pgf@shorten@start@additional=\dimen131
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorescopes.co
    de.tex
    File: pgfcorescopes.code.tex 2010/09/08  (rcs-revision 1.34)
    \pgfpic=\box29
    \pgf@hbox=\box30
    \pgf@layerbox@main=\box31
    \pgf@picture@serial@count=\count98
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcoregraphicst
    ate.code.tex
    File: pgfcoregraphicstate.code.tex 2008/04/22  (rcs-revision 1.9)
    \pgflinewidth=\dimen132
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretransform
    ations.code.tex
    File: pgfcoretransformations.code.tex 2009/06/10  (rcs-revision 1.11)
    \pgf@pt@x=\dimen133
    \pgf@pt@y=\dimen134
    \pgf@pt@temp=\dimen135
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorequick.cod
    e.tex
    File: pgfcorequick.code.tex 2008/10/09  (rcs-revision 1.3)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreobjects.c
    ode.tex
    File: pgfcoreobjects.code.tex 2006/10/11  (rcs-revision 1.2)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepathproce
    ssing.code.tex
    File: pgfcorepathprocessing.code.tex 2008/10/09  (rcs-revision 1.8)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorearrows.co
    de.tex
    File: pgfcorearrows.code.tex 2008/04/23  (rcs-revision 1.11)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreshade.cod
    e.tex
    File: pgfcoreshade.code.tex 2008/11/23  (rcs-revision 1.13)
    \pgf@max=\dimen136
    \pgf@sys@shading@range@num=\count99
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreimage.cod
    e.tex
    File: pgfcoreimage.code.tex 2010/03/25  (rcs-revision 1.16)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcoreexternal.
    code.tex
    File: pgfcoreexternal.code.tex 2010/09/01  (rcs-revision 1.17)
    \pgfexternal@startupbox=\box32
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorelayers.co
    de.tex
    File: pgfcorelayers.code.tex 2010/08/27  (rcs-revision 1.2)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcoretranspare
    ncy.code.tex
    File: pgfcoretransparency.code.tex 2008/01/17  (rcs-revision 1.2)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/basiclayer/pgfcorepatterns.
    code.tex
    File: pgfcorepatterns.code.tex 2009/07/02  (rcs-revision 1.3)
    )))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/modules/pgfmoduleshapes.cod
    e.tex
    File: pgfmoduleshapes.code.tex 2010/09/09  (rcs-revision 1.13)
    \pgfnodeparttextbox=\box33
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/modules/pgfmoduleplot.code.
    tex
    File: pgfmoduleplot.code.tex 2010/10/22  (rcs-revision 1.8)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version
    -0-65.sty
    Package: pgfcomp-version-0-65 2007/07/03 v2.10 (rcs-revision 1.7)
    \pgf@nodesepstart=\dimen137
    \pgf@nodesepend=\dimen138
    )
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/compatibility/pgfcomp-version
    -1-18.sty
    Package: pgfcomp-version-1-18 2007/07/23 v2.10 (rcs-revision 1.1)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/utilities/pgffor.sty
    (/usr/local/texlive/2013/texmf-dist/tex/latex/pgf/utilities/pgfkeys.sty
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/utilities/pgfkeys.code.tex)
    ) (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/utilities/pgffor.code.tex
    Package: pgffor 2010/03/23 v2.10 (rcs-revision 1.18)
    \pgffor@iter=\dimen139
    \pgffor@skip=\dimen140
    \pgffor@stack=\toks23
    \pgffor@toks=\toks24
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/tikz.cod
    e.tex
    Package: tikz 2010/10/13 v2.10 (rcs-revision 1.76)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/pgflibraryplothan
    dlers.code.tex
    File: pgflibraryplothandlers.code.tex 2010/05/31 v2.10 (rcs-revision 1.15)
    \pgf@plot@mark@count=\count100
    \pgfplotmarksize=\dimen141
    )
    \tikz@lastx=\dimen142
    \tikz@lasty=\dimen143
    \tikz@lastxsaved=\dimen144
    \tikz@lastysaved=\dimen145
    \tikzleveldistance=\dimen146
    \tikzsiblingdistance=\dimen147
    \tikz@figbox=\box34
    \tikz@tempbox=\box35
    \tikztreelevel=\count101
    \tikznumberofchildren=\count102
    \tikznumberofcurrentchild=\count103
    \tikz@fig@count=\count104

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/modules/pgfmodulematrix.cod
    e.tex
    File: pgfmodulematrix.code.tex 2010/08/24  (rcs-revision 1.4)
    \pgfmatrixcurrentrow=\count105
    \pgfmatrixcurrentcolumn=\count106
    \pgf@matrix@numberofcolumns=\count107
    )
    \tikz@expandcount=\count108

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibrarytopaths.code.tex
    File: tikzlibrarytopaths.code.tex 2008/06/17 v2.10 (rcs-revision 1.2)
    )))
    (/Users/neil/SheffieldML/publications/tex_inputs/definitions.tex
    (/usr/local/texlive/2013/texmf-dist/tex/latex/tools/verbatim.sty
    Package: verbatim 2003/08/22 v1.5q LaTeX2e package for verbatim enhancements
    \every@verbatim=\toks25
    \verbatim@line=\toks26
    \verbatim@in@stream=\read2
    ))
    (/Users/neil/SheffieldML/publications/tex_inputs/notationDef.tex)
    (/Users/neil/SheffieldML/publications/tex_inputs/graphicalModels.tex
    (/Users/neil/SheffieldML/publications/tex_inputs/tikz-bayesnet/tikzlibrarybayes
    net.code.tex
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryshapes.code.tex
    File: tikzlibraryshapes.code.tex 2008/01/09 v2.10 (rcs-revision 1.1)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryshapes.geometric.code.tex
    File: tikzlibraryshapes.geometric.code.tex 2008/01/09 v2.10 (rcs-revision 1.1)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibrary
    shapes.geometric.code.tex
    File: pgflibraryshapes.geometric.code.tex 2008/06/26 v2.10 (rcs-revision 1.1)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryshapes.misc.code.tex
    File: tikzlibraryshapes.misc.code.tex 2008/01/09 v2.10 (rcs-revision 1.1)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibrary
    shapes.misc.code.tex
    File: pgflibraryshapes.misc.code.tex 2008/10/07 v2.10 (rcs-revision 1.3)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryshapes.symbols.code.tex
    File: tikzlibraryshapes.symbols.code.tex 2008/01/09 v2.10 (rcs-revision 1.1)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibrary
    shapes.symbols.code.tex
    File: pgflibraryshapes.symbols.code.tex 2009/10/27 v2.10 (rcs-revision 1.3)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryshapes.arrows.code.tex
    File: tikzlibraryshapes.arrows.code.tex 2008/01/09 v2.10 (rcs-revision 1.1)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibrary
    shapes.arrows.code.tex
    File: pgflibraryshapes.arrows.code.tex 2008/06/26 v2.10 (rcs-revision 1.1)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryshapes.callouts.code.tex
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibrary
    shapes.callouts.code.tex))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryshapes.multipart.code.tex
    File: tikzlibraryshapes.multipart.code.tex 2008/01/09 v2.10 (rcs-revision 1.1)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/shapes/pgflibrary
    shapes.multipart.code.tex
    File: pgflibraryshapes.multipart.code.tex 2010/01/07 v2.10 (rcs-revision 1.2)
    \pgfnodepartlowerbox=\box36
    \pgfnodeparttwobox=\box37
    \pgfnodepartthreebox=\box38
    \pgfnodepartfourbox=\box39
    \pgfnodeparttwentybox=\box40
    \pgfnodepartnineteenbox=\box41
    \pgfnodeparteighteenbox=\box42
    \pgfnodepartseventeenbox=\box43
    \pgfnodepartsixteenbox=\box44
    \pgfnodepartfifteenbox=\box45
    \pgfnodepartfourteenbox=\box46
    \pgfnodepartthirteenbox=\box47
    \pgfnodeparttwelvebox=\box48
    \pgfnodepartelevenbox=\box49
    \pgfnodeparttenbox=\box50
    \pgfnodepartninebox=\box51
    \pgfnodeparteightbox=\box52
    \pgfnodepartsevenbox=\box53
    \pgfnodepartsixbox=\box54
    \pgfnodepartfivebox=\box55
    )))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryfit.code.tex
    File: tikzlibraryfit.code.tex 2008/06/21 v2.10 (rcs-revision 1.3)
    )
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibrarychains.code.tex
    File: tikzlibrarychains.code.tex 2008/02/27 v2.10 (rcs-revision 1.5)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibrarypositioning.code.tex
    File: tikzlibrarypositioning.code.tex 2008/10/06 v2.10 (rcs-revision 1.7)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/frontendlayer/tikz/librarie
    s/tikzlibraryarrows.code.tex
    File: tikzlibraryarrows.code.tex 2008/01/09 v2.10 (rcs-revision 1.1)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/pgf/libraries/pgflibraryarrows.
    code.tex
    File: pgflibraryarrows.code.tex 2008/10/27 v2.10 (rcs-revision 1.9)
    \arrowsize=\dimen148
    )))) (./tikz.aux)
    \openout1 = `tikz.aux'.

    LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 7.
    LaTeX Font Info:    ... okay on input line 7.
    LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 7.
    LaTeX Font Info:    ... okay on input line 7.
    LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 7.
    LaTeX Font Info:    ... okay on input line 7.
    LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 7.
    LaTeX Font Info:    ... okay on input line 7.
    LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 7.
    LaTeX Font Info:    ... okay on input line 7.
    LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 7.
    LaTeX Font Info:    ... okay on input line 7.
     ABD: EveryShipout initializing macros
    (/usr/local/texlive/2013/texmf-dist/tex/context/base/supp-pdf.mkii
    [Loading MPS to PDF converter (version 2006.09.02).]
    \scratchcounter=\count109
    \scratchdimen=\dimen149
    \scratchbox=\box56
    \nofMPsegments=\count110
    \nofMParguments=\count111
    \everyMPshowfont=\toks27
    \MPscratchCnt=\count112
    \MPscratchDim=\dimen150
    \MPnumerator=\count113
    \makeMPintoPDFobject=\count114
    \everyMPtoPDFconversion=\toks28
    ) (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/pdftexcmds.sty
    Package: pdftexcmds 2011/11/29 v0.20 Utility functions of pdfTeX for LuaTeX (HO
    )
    Package pdftexcmds Info: LuaTeX not detected.
    Package pdftexcmds Info: \pdf@primitive is available.
    Package pdftexcmds Info: \pdf@ifprimitive is available.
    Package pdftexcmds Info: \pdfdraftmode found.
    )
    (/usr/local/texlive/2013/texmf-dist/tex/latex/oberdiek/epstopdf-base.sty
    Package: epstopdf-base 2010/02/09 v2.5 Base part for package epstopdf

    (/usr/local/texlive/2013/texmf-dist/tex/latex/oberdiek/grfext.sty
    Package: grfext 2010/08/19 v1.1 Manage graphics extensions (HO)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/kvdefinekeys.sty
    Package: kvdefinekeys 2011/04/07 v1.3 Define keys (HO)
    ))
    (/usr/local/texlive/2013/texmf-dist/tex/latex/oberdiek/kvoptions.sty
    Package: kvoptions 2011/06/30 v3.11 Key value format for package options (HO)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/kvsetkeys.sty
    Package: kvsetkeys 2012/04/25 v1.16 Key value parser (HO)

    (/usr/local/texlive/2013/texmf-dist/tex/generic/oberdiek/etexcmds.sty
    Package: etexcmds 2011/02/16 v1.5 Avoid name clashes with e-TeX commands (HO)
    Package etexcmds Info: Could not find \expanded.
    (etexcmds)             That can mean that you are not using pdfTeX 1.50 or
    (etexcmds)             that some package has redefined \expanded.
    (etexcmds)             In the latter case, load this package earlier.
    )))
    Package grfext Info: Graphics extension search list:
    (grfext)             [.png,.pdf,.jpg,.mps,.jpeg,.jbig2,.jb2,.PNG,.PDF,.JPG,.JPE
    G,.JBIG2,.JB2,.eps]
    (grfext)             \AppendGraphicsExtensions on input line 452.

    (/usr/local/texlive/2013/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg
    File: epstopdf-sys.cfg 2010/07/13 v1.3 Configuration of (r)epstopdf for TeX Liv
    e
    ))
    ! Undefined control sequence.
    l.8 \draw
              node[obs] (y) {$\dataVector$};
    ? 
    ! Emergency stop.
    l.8 \draw
              node[obs] (y) {$\dataVector$};
    End of file on the terminal!

     
    Here is how much of TeX's memory you used:
     12714 strings out of 493315
     261271 string characters out of 6137905
     332853 words of memory out of 5000000
     15908 multiletter control sequences out of 15000+600000
     3640 words of font info for 14 fonts, out of 8000000 for 9000
     957 hyphenation exceptions out of 8191
     56i,0n,56p,417b,83s stack positions out of 5000i,500n,10000p,200000b,80000s
    !  ==> Fatal error occurred, no output PDF file produced!
:::


Instantiating the Model
-----------------------


So far we haven't made any assumptions about the data in our model,
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
be passed to the test data.


For a model to be useful, we need to specify relationships between our
data variables. Of course, this is the point at which a model also
typically becomes wrong. The following considerations should arise:


If our model is not correct, is it a useful abstraction given what we
expect to observe about the data? For example, Brownian motion is
modelled as a stochastic differential equation.


### Gaussian Processes


A flexible class of models that fulfils the constraints of being
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
what.


### Augmenting with Inducing Variables in Gaussian Processes


To define our model we need to describe the relationship between the
fundamental variables, $\dataMappingVector$, and the inducing variables,
$\inducingVector$. This needs to be done in such a way that the inducing
variables are also Kolmogorov consistent. A straightforward way of
achieving this is through a joint Gaussian process model over the
inducing variables and the data mapping variables, so in other words we
define a Gaussian process prior over


$$\begin{bmatrix}\mappingFunctionVector \ \inducingVector\end{bmatrix} \sim \gaussianDist{\mathbf{m}}{\kernelMatrix}$$


where the covariance matrix has a block form,


$$\kernelMatrix = \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector\mappingFunctionVector} & \kernelMatrix_{\mappingFunctionVector\inducingVector} \ \kernelMatrix_{\inducingVector\mappingFunctionVector} & \kernelMatrix_{\inducingVector\inducingVector}\end{bmatrix}$$


and $\kernelMatrix_{\mappingFunctionVector\mappingFunctionVector}$ gives
the covariance between the fundamentals vector,
$\kernelMatrix_{\inducingVector\inducingVector}$ gives the covariance
matrix between the inducing variables and
$\kernelMatrix_{\inducingVector\mappingFunctionVector} = \kernelMatrix_{\mappingFunctionVector\inducingVector}^\top$
gives the cross covariance between the inducing variables,
$\inducingVector$ and the mapping function variables,
$\mappingFunctionVector$.


The elements of
$\kernelMatrix_{\mappingFunctionVector\mappingFunctionVector}$ will be
computed through a covariance function (or kernel) given by
$\kernelScalar_\mappingFunction(\inputVector, \inputVector^\prime)$
where $\inputVector$ is a vector representing the *provenance* of the
data, which as we discussed earlier could involve a spatial location, a
time, or something about the nature of the data. In a Gaussian process
most of the modelling decisions take place in the construction of
$\kernelScalar_\mappingFunction(\cdot)$.


### The Mean Function


The mean of the process is given by a vector $\mathbf{m}$ which is
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
effects, often denoted by


$$m(\inputVector) = \boldsymbol{\beta}^\top \inputVector,$$


where here the provenance of the data is known as the covariates, and
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
is then given by the covariance function.


The modeling philosophy in machine learning is somewhat different from
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
function and focus only on the covariance function.


\todo{Mention here an example of things going wrong? Or do a short run
of a mauna loa data to demonstrate, with a mean function included?}
:::

::: {.cell .code execution_count="12"}
``` {.python}
%pylab inline
import GPy
data = GPy.util.datasets.mauna_loa()
kern = GPy.kern.Linear(1) + GPy.kern.RBF(1) + GPy.kern.Bias(1)
model = GPy.models.GPRegression(data['X'], data['Y'], kern)
#model.optimize()
```

::: {.output .stream .stdout}
    Populating the interactive namespace from numpy and matplotlib
:::

::: {.output .error ename="IndentationError" evalue="unexpected indent (coregionalize.py, line 154)"}
      File "/Users/neil/SheffieldML/GPy/GPy/kern/_src/coregionalize.py", line 154
        def _gradient_reduce_numpy(self, dL_dK, index, index2):
        ^
    IndentationError: unexpected indent
:::
:::

::: {.cell .code collapsed="true"}
``` {.python}
```
:::

::: {.cell .code collapsed="true"}
``` {.python}
pb.plot(xlim
```


So we *could* interpret Gaussian process models as approaches to dealing
with residuals


### Modelling $\mappingFunctionVector$


In conclusion, for a non parametric framework, our model for
$\mappingFunctionVector$ is predominantly in the covariance function
$\kernelMatrix_{\mappingFunctionVector\mappingFunctionVector}$. This is
our data model. We are assuming the inducing variables are drawn from a
joint Gaussian process with $\mappingFunctionVector$. The cross
covariance between $\inducingVector$ and $\mappingFunctionVector$ is
given by $\kernelMatrix_{\mappingFunctionVector\inducingVector}$. This
gives the relationship between the function and the inducing variables.
There are a range of ways in which the inducing variables can interelate
with the


### Illustrative Example


For this illustrative example, we'll consider a simple regression
problem. The example is based on one that James Hensman showed at the
January 2014 Gaussian process winter school in his talk is on low rank
Gaussian process approximations.
:::

::: {.cell .code execution_count="36" collapsed="true" slideshow="{\"slide_type\":\"slide\"}"}
``` {.python}
%matplotlib inline
import GPy
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import teaching_plots as plot
from gp_tutorial import ax_default, meanplot, gpplot
import mlai
np.random.seed(101)
```


A Simple Regression Problem
---------------------------


Here we set up a simple one dimensional regression problem. The input
locations, $\inputMatrix$, are in two separate clusters. The response
variable, $\dataVector$, is sampled from a Gaussian process with an
exponentiated quadratic covariance.
:::

::: {.cell .code execution_count="37" collapsed="true"}
``` {.python}
N = 50
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
offset = np.mean(y)
```


First we perform a full Gaussian process regression on the data. We
create a GP model, `m_full`, and fit it to the data, plotting the
resulting fit.
:::

::: {.cell .code execution_count="38" collapsed="true"}
``` {.python}
def plot_model_output(model, output_dim=0, scale=1.0, offset=0.0, ax=None, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2):
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
               ax=ax)
```
:::

::: {.cell .code execution_count="63"}
``` {.python}
m.plot
```

::: {.output .error ename="AttributeError" evalue="'function' object has no attribute '__file__'"}
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-63-da31fe6ce98f> in <module>()
    ----> 1 m.plot.__file__

    AttributeError: 'function' object has no attribute '__file__'
:::
:::

::: {.cell .code execution_count="39"}
``` {.python}
m_full = GPy.models.GPRegression(X,y)
m_full.optimize() # Optimize parameters of covariance function
```

::: {.output .execute_result execution_count="39"}
    <paramz.optimization.optimization.opt_lbfgsb at 0x120d63f28>
:::
:::

::: {.cell .code execution_count="40"}
``` {.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='$x', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='../../slides/diagrams/gp/sparse-demo-full-gp.svg', 
                  transparent=True, frameon=True)
```

::: {.output .display_data}
![](fa9e88c44f609dad691ce5416d005212c7afcc07.png)
:::


Now we set up the inducing variables, $\mathbf{u}$. Each inducing
variable has its own associated input index, $\mathbf{Z}$, which lives
in the same space as $\inputMatrix$. Here we are using the true
covariance function parameters to generate the fit.
:::

::: {.cell .code execution_count="49"}
``` {.python}
kern = GPy.kern.RBF(1)
Z = np.hstack(
        (np.linspace(2.5,4.,3),
        np.linspace(7,8.5,3)))[:,None]
m = GPy.models.SparseGPRegression(X,y,kernel=kern,Z=Z)
m.noise_var = noise_var
m.inducing_inputs.constrain_fixed()
#m.tie_params('.*variance')
#m.ensure_default_constraints()
print(m) # why is it not printing noise variance correctly?
```

::: {.output .stream .stdout}

    Name : sparse_gp
    Objective : 70.4565562039284
    Number of Parameters : 9
    Number of Optimization Parameters : 3
    Updates : True
    Parameters:
      sparse_gp.               |   value  |  constraints  |  priors
      inducing_inputs          |  (6, 1)  |     fixed     |        
      rbf.variance             |     1.0  |      +ve      |        
      rbf.lengthscale          |     1.0  |      +ve      |        
      Gaussian_noise.variance  |     1.0  |      +ve      |        
:::
:::

::: {.cell .code execution_count="42"}
``` {.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='$x', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='../../slides/diagrams/gp/sparse-demo-constrained-inducing-6-unlearned-gp.svg', 
                  transparent=True, frameon=True)
```

::: {.output .display_data}
![](bdcd29134b35c5e3867bc75207a06127163d8255.png)
:::
:::

::: {.cell .code execution_count="43"}
``` {.python}
m.optimize()
```

::: {.output .execute_result execution_count="43"}
    <paramz.optimization.optimization.opt_lbfgsb at 0x120f7bf98>
:::
:::

::: {.cell .code execution_count="44"}
``` {.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='../../slides/diagrams/gp/sparse-demo-constrained-inducing-6-learned-gp.svg', 
                  transparent=True, frameon=True)
```

::: {.output .display_data}
![](acf18cf6069c80db2a8bd1db286c6411b846e1ce.png)
:::
:::

::: {.cell .code execution_count="45"}
``` {.python}
print(m)
```

::: {.output .stream .stdout}

    Name : sparse_gp
    Objective : 33.070783992616896
    Number of Parameters : 9
    Number of Optimization Parameters : 3
    Updates : True
    Parameters:
      sparse_gp.               |           value  |  constraints  |  priors
      inducing_inputs          |          (6, 1)  |     fixed     |        
      rbf.variance             |    2.2954561541  |      +ve      |        
      rbf.lengthscale          |   5.02432986416  |      +ve      |        
      Gaussian_noise.variance  |  0.161887276492  |      +ve      |        
:::
:::

::: {.cell .code execution_count="46"}
``` {.python}
m.randomize()
m.inducing_inputs.unconstrain()
m.optimize()
```

::: {.output .execute_result execution_count="46"}
    <paramz.optimization.optimization.opt_lbfgsb at 0x120f9df98>
:::
:::

::: {.cell .code execution_count="47"}
``` {.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='../../slides/diagrams/gp/sparse-demo-unconstrained-inducing-6-gp.svg', 
                  transparent=True, frameon=True)
```

::: {.output .display_data}
![](c5337db27a5b3b9ade7ec483995507344bdb81fd.png)
:::


Now we will vary the number of inducing points used to form the
approximation.
:::

::: {.cell .code execution_count="52"}
``` {.python}
m.Z.values
```

::: {.output .execute_result execution_count="52"}
    array([[ 2.5 ],
           [ 3.25],
           [ 4.  ],
           [ 7.  ],
           [ 7.75],
           [ 8.5 ]])
:::
:::

::: {.cell .code execution_count="59"}
``` {.python}
m.num_inducing=8
m.randomize()
M = 8

m.set_Z(np.random.rand(M,1)*12)

m.optimize()
```

::: {.output .execute_result execution_count="59"}
    <paramz.optimization.optimization.opt_lbfgsb at 0x120de54a8>
:::
:::

::: {.cell .code execution_count="60"}
``` {.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_model_output(m, scale=scale, offset=offset, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='../../slides/diagrams/gp/sparse-demo-sparse-inducing-8-gp.svg', 
                  transparent=True, frameon=True)

print(m.log_likelihood(), m_full.log_likelihood())
```

::: {.output .stream .stdout}
    [[-29.86773317]] -29.8277529184
:::

::: {.output .display_data}
![](0e1cab5c7c6ff29e254f62b63a72b233d036b722.png)
:::

### Uncertainty about the Provenance of the Data

Provenance could include the time that the data was acquired, the
location that the data was acquired, even the 'type' of data that is
acquired. For example, in computer vision pixels are arriving from
different objects. We are uncertain about the provenance of the pixels
in terms of which *object* they are arriving from. The spatial location
of the object in the image. This uncertainty relates to uncertainty
about the covariance function. Unfortunately, it is not directly on the
covariance function itself, but relates to values through which the
covariance is nonlinearly related.


\begin{align*} 
k(\dataVector, \dataVector^\prime) = \exp(-\|\|\dataVector-\dataVector^\prime\|\|^2) 
\end{align*}

These variables become *latent* or *confounders*.


**Not sure about this**: Provenance of data is often finite. Consider a
diseased person. That person consists of a finite (if very large) state
vector. Of course the number of measurements we can make about that
person is infinite. But there are a set of fundamental limitations to
what can go wrong with the individual.


Ethics
------


Ownership of data, returning it to the individual. In healthcare the
danger of confusing it with marketing, Laplace, and the utopian view of
data. Invalidity of insurance. How the results are presented to the
patient.
