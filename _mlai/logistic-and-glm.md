---
week: 10
title: "Logistic Regression and GLMs"
abstract: Naive Bayes assumptions allow us to specify class conditional densities through assuming that the data are conditionally independent given parameters. A logistic regression is an approach to classification which extends the linear basis function models we've already explored. Rather than modeling the output of the function directly the assumption is that we model the *log-odds* with the basis functions.
youtube: e-BWWidfbT4
---

talk-macros.gpp}lk-macros.tex}

talk-macros.gpp}lai/includes/mlai-notebook-setup.md}

\subsection{Review}

\slides{
* Last week: Specified Class Conditional Distributions, $p(\inputVector_i|\dataScalar_i, \parameterVector)$.
* Used Bayes Classifier + naive Bayes model to specify joint distribution.
* Used Bayes rule to compute posterior probability of class membership.
* This week: 
  * direct estimation of probability of class membership.
  * introduction of generalised linear models.
}


\notes{The \refnotes{naive Bayes assumption}{naive-bayes} allowed us to
specify a class conditional density, $p(\inputVector_i|\dataScalar_i,
\parameterVector)$, through assuming that the features were
conditionally independent given the label.  Combined with our
assumption that the data points are conditionally independent given
the parameters, $\parameterVector$, this allowed us to specify a joint
density over the entire data set, $p(\dataVector, \inputMatrix)$. We
argued that modeling the joint density is a powerful approach because
we can answer any particular question we have about the data through
the sum rule and the product rule of probability. We can condition on
the training data and query the value of an unseen test point. If we
have missing data, then we can integrate over the missing point
(marginalise) and obtain our best prediction despite the absence of
some of the features for a point. However, it comes at the cost of a
particular modeling assumption. Namely, to make modeling practical we
assumed that the features were conditionally independent given the
feature label. In other words, for any given point, if we know its
class, then its features will be independent. This is a very strong
assumption. For example, if we were classifying the sex of an
individual given their height and weight, naive Bayes would assume
that if we knew their sex, then the height and weight would be
independent. This is clearly wrong, the dependence between height and
weight is not dictated only by the sex of an individual, there is a
natural correlation between them.}

\notes{Modeling the entire joint density allows us to deal with
different questions, that we may not have envisaged at the model
*design time*.  It contrasts with the approach we took for regression
where we specifically chose to model the conditional density for the
target values, $\dataVector$, given the input locations,
$\inputMatrix$. That density, $p(\dataVector|\inputMatrix)$,
effectively assumes that the question we'll be asked at *run time* is
known. In particular, we expect to be asked about the value of the
function, $y^*$, given a particular input location,
$\inputVector^*$. We don't expect to be asked about the value of an
input given a particular observation.  That would require placing an
additional prior over the input location for each point,
$p(\inputVector_i)$. Of course, it's possible to conceive of a model
like this, and indeed that is how we proceeded for
\refnotes{dimensionality reduction}{dimensionality-reduction}. However, if we know we will
always have all the inputs at run time, it may make sense to
*directly* model the conditional density,
$p(\dataVector|\inputMatrix)$.}

talk-macros.gpp}l/includes/logistic-regression.md}

\newslide{Ad Matching for Facebook}

\slides{
* This approach used in many internet companies.
* Example: ad matching for Facebook.
  * Millions of advertisers
  * Billions of users
  * How do you choose who to show what?
* Logistic regression used in combination with [decision trees]()
* [Paper available here](http://www.herbrich.me/papers/adclicksfacebook.pdf)
}

\notes{
\subsection{Olivetti Glasses Data}

Let's classify images with logistic regression. We'll look at a data set of individuals with glasses. We can load in the data from `pods` as follows.

\setupcode{import pods}
\code{# Change this example for 2016#data = pods.datasets.movie_body_count_r_classify()
data = pods.datasets.olivetti_glasses()
X = data['X']
y = data['Y']}

talk-macros.gpp}l/includes/logistic-regression-gradient-descent.md}
talk-macros.gpp}l/includes/logistic-regression-going-further.md}


\subsection{Bayesian Approaches}

\exercise{Can you place a prior density over the parameters $\mappingVector$ and marginalize them out like we did for linear regression? If not why not?}

\reading

\thanks

\references


