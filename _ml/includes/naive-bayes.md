\subsection{Naive Bayes Classifiers}

\notes{*Note*: Everything we do below is possible using standard packages like `scikit-learn`, our purpose in this session is to help you understand how those engines are constructed. In practice for an application you should use a library like `scikit-learn`.}

\notes{In probabilistic machine learning we place probability distributions (or densities) over all the variables of interest, our first classification algorithm will do just that. We will consider how to form a classification by making assumptions about the *joint* density of our observations. We need to make assumptions to reduce the number of parameters we need to optimise.}\slides{
* Probabilistic Machine Learning: place probability distributions (or densities) over all the variables of interest.
* In *naive Bayes* this is exactly what we do.}

\notes{In the ideal world, given label data $\dataVector$ and the inputs $\inputMatrix$ we should be able to specify the joint density of all potential values of $\dataVector$ and $\inputMatrix$, $p(\dataVector, \inputMatrix)$.  If $\inputMatrix$ and $\dataVector$ are our training data, and we can somehow extend our density to incorporate future test data (by augmenting $\dataVector$ with a new observation $\dataScalar^*$ and $\inputMatrix$ with the corresponding inputs, $\inputVector^*$), then we can answer any given question about a future test point $\dataScalar^*$ given its covariates $\inputVector^*$ by conditioning on the training variables to recover,
$$
p(\dataScalar^*|\inputMatrix, \dataVector, \inputVector^*),
$$} 
\slides{* Form a classification algorithm by modelling the *joint* density of our observations. }\notes{
We can compute this distribution using the product and sum rules. However, to specify this density we must give the probability associated with all possible combinations of $\dataVector$ and $\inputMatrix$. There are $2^{\numData}$ possible combinations for the vector $\dataVector$ and the probability for each of these combinations must be jointly specified along with the joint density of the matrix $\inputMatrix$, as well as being able to *extend* the density for any chosen test location $\inputVector^*$.}

\notes{In naive Bayes we make certain simplifying assumptions that allow us to perform all of the above in practice.}\slides{
* Need to make assumption about joint density.}

\newslide{Assumptions about Density}

\slides{* Make assumptions to reduce the number of parameters we need to optimise. 
* Given label data $\dataVector$ and the inputs $\inputMatrix$ could specify joint density of all potential values of $\dataVector$
and $\inputMatrix$, $p(\dataVector, \inputMatrix)$. 
* If $\inputMatrix$ and $\dataVector$ are training data.
* If $\inputVector^*$ is a test input and $\dataScalar^*$ a test location we want
  $$
  p(\dataScalar^*|\inputMatrix, \dataVector, \inputVector^*),
  $$}

\newslide{Answer from Rules of Probability}

\slides{* Compute this distribution using the product and sum rules. 
* Need the probability associated with all possible combinations of $\dataVector$ and $\inputMatrix$. 
* There are $2^{\numData}$ possible combinations for the vector $\dataVector$
* Probability for each of these combinations must be jointly specified along with the joint density of the matrix $\inputMatrix$, 
* Also need to *extend* the density for any chosen test location $\inputVector^*$.}

\newslide{Naive Bayes Assumptions}

\slides{* In *naive Bayes* we make certain simplifying assumptions that allow us to perform all of the above in practice. 
1. Data Conditional Independence
2. Feature conditional independence
3. Marginal density for $\dataScalar$.}

\subsection{Data Conditional Independence}

\notes{If we are given model parameters $\paramVector$ we assume that conditioned on all these parameters that all data points in the model are independent. In other words we have,}\slides{
* Given model parameters $\paramVector$ we assume that all data points in the model are independent. }
  $$
  p(\dataScalar^*, \inputVector^*, \dataVector, \inputMatrix|\paramVector) = p(\dataScalar^*, \inputVector^*|\paramVector)\prod_{i=1}^{\numData} p(\dataScalar_i, \inputVector_i | \paramVector).
  $$
\notes{This is a conditional independence assumption because we are not assuming our data are purely independent. If we were to assume that, then there would be nothing to learn about our test data given our training data. We are assuming that they are independent *given* our parameters, $\paramVector$.}\slides{
* This is a conditional independence assumption.}
\notes{We made similar assumptions for regression, where our parameter set included $\mappingVector$ and $\dataStd^2$. Given those parameters we assumed that the density over $\dataVector, \dataScalar^*$ was *independent*.}\slides{
* We also make similar assumptions for regression (where $\paramVector =
\left\{\mappingVector,\dataStd^2\right\}$).}
\notes{Here we are going a little further with that assumption because we are assuming the *joint* density of $\dataVector$ and $\inputMatrix$ is independent across the data given the parameters.}\slides{
* Here we assume *joint* density of $\dataVector$ and $\inputMatrix$ is independent across the data given the parameters.}

\newslide{Bayes Classifier}

Computing posterior distribution in this case becomes easier, this is known as the 'Bayes classifier'.

\subsection{Feature Conditional Independence}

\notes{$$
p(\inputVector_i | \dataScalar_i, \paramVector) = \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)
$$
where $\dataDim$ is the dimensionality of our inputs.}

\notes{The assumption that is particular to naive Bayes is to now consider that the *features* are also conditionally independent, but not only given the parameters. We assume that the features are independent given the parameters *and* the label. So for each data point we have}\slides{
* Particular to naive Bayes: assume *features* are also conditionally independent, given param *and* the label.}
  $$p(\inputVector_i | \dataScalar_i, \paramVector) = \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i,\paramVector)$$
  where $\dataDim$ is the dimensionality of our inputs.\slides{
* This is known as the *naive Bayes* assumption.
* Bayes classifier + feature conditional independence.
}

\subsection{Marginal Density for $\dataScalar_i$}

\notes{$$
p(\inputScalar_{i,j},\dataScalar_i| \paramVector) = p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i).
$$}

\notes{We now have nearly all of the components we need to specify the full joint density. However, the feature conditional independence doesn't yet give us the joint density over $p(\dataScalar_i, \inputVector_i)$ which is required to subsitute in to our data conditional independence to give us the full density. To recover the joint density given the conditional distribution of each feature, $p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)$, we need to make use of the product rule and combine it with a marginal density for $\dataScalar_i$,
}\slides{
* To specify the joint distribution we also need the marginal for $p(\dataScalar_i)$}
  $$p(\inputScalar_{i,j},\dataScalar_i| \paramVector) = p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i).$$
\notes{Because $\dataScalar_i$ is binary the *Bernoulli* density makes a suitable choice for our prior over $\dataScalar_i$,}\slides{
* Because $\dataScalar_i$ is binary the *Bernoulli* density makes a suitable choice for our prior over $\dataScalar_i$,}
  $$p(\dataScalar_i|\pi) = \pi^{\dataScalar_i} (1-\pi)^{1-\dataScalar_i}$$
  where $\pi$ now has the interpretation as being the *prior* probability that the classification should be positive.

\subsection{Joint Density for Naive Bayes}

\notes{This allows us to write down the full joint density of the training data,}\slides{
* This allows us to write down the full joint density of the training data,}
  $$
  p(\dataVector, \inputMatrix|\paramVector, \pi) = \prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi)
  $$
\slides{which can now be fit by maximum likelihood.}
\notes{which can now be fit by maximum likelihood. As normal we form our objective as the negative log likelihood,}
\newslide{Objective Function}
$$\begin{align*}
\errorFunction(\paramVector, \pi)& =  -\log p(\dataVector, \inputMatrix|\paramVector, \pi) \\ &= -\sum_{i=1}^{\numData} \sum_{j=1}^{\dataDim} \log p(\inputScalar_{i, j}|\dataScalar_i, \paramVector) -  \sum_{i=1}^{\numData} \log p(\dataScalar_i|\pi),
\end{align*}$$
\notes{which we note *decomposes* into two objective functions, one which is dependent on $\pi$ alone and one which is dependent on $\paramVector$ alone so we have,
$$
\errorFunction(\pi, \paramVector) = \errorFunction(\paramVector) + \errorFunction(\pi).
$$
Since the two objective functions are separately dependent on the parameters $\pi$ and $\paramVector$ we can minimize them independently. Firstly, minimizing the Bernoulli likelihood over the labels we have, 
$$
\errorFunction(\pi) = -\sum_{i=1}^{\numData}\log p(\dataScalar_i|\pi) = -\sum_{i=1}^{\numData} \dataScalar_i \log \pi - \sum_{i=1}^{\numData} (1-\dataScalar_i) \log (1-\pi)
$$
which we already minimized above recovering 
$$
\pi = \frac{\sum_{i=1}^{\numData} \dataScalar_i}{\numData}.
$$
}

\newslide{Maximum Likelihood}

\notes{We now need to minimize the objective associated with the conditional distributions for the features,
$$
\errorFunction(\paramVector) = -\sum_{i=1}^{\numData} \sum_{j=1}^{\dataDim} \log p(\inputScalar_{i, j} |\dataScalar_i, \paramVector),
$$
which necessarily implies making some assumptions about the form of the conditional distributions. The right assumption will depend on the nature of our input data. For example, if we have an input which is real valued, we could use a Gaussian density and we could allow the mean and variance of the Gaussian to be different according to whether the class was positive or negative and according to which feature we were measuring. That would give us the form,
$$
p(\inputScalar_{i, j} | \dataScalar_i,\paramVector) = \frac{1}{\sqrt{2\pi \dataStd_{\dataScalar_i,j}^2}} \exp \left(-\frac{(\inputScalar_{i,j} - \mu_{\dataScalar_i, j})^2}{\dataStd_{\dataScalar_i,j}^2}\right),
$$
where $\dataStd_{1, j}^2$ is the variance of the density for the $j$th output and the class $\dataScalar_i=1$ and $\dataStd_{0, j}^2$ is the variance if the class is 0. The means can vary similarly. Our parameters, $\paramVector$ would consist of all the means and all the variances for the different dimensions.}

\notes{As normal we form our objective as the negative log likelihood,
$$
\errorFunction(\paramVector, \pi) = -\log p(\dataVector, \inputMatrix|\paramVector, \pi) = -\sum_{i=1}^{\numData} \sum_{j=1}^{\dataDim} \log p(\inputScalar_{i, j}|\dataScalar_i, \paramVector) - \sum_{i=1}^{\numData} \log p(\dataScalar_i|\pi),
$$
which we note *decomposes* into two objective functions, one which is dependent on $\pi$ alone and one which is dependent on $\paramVector$ alone so we have,
$$
\errorFunction(\pi, \paramVector) = \errorFunction(\paramVector) + \errorFunction(\pi).
$$}

\newslide{Fit Prior}
\slides{
* We can minimize prior. For Bernoulli likelihood over the labels we have, 
  $$\begin{align*}
  \errorFunction(\pi) & = - \sum_{i=1}^{\numData}\log p(\dataScalar_i|\pi)\\ & = -\sum_{i=1}^{\numData} \dataScalar_i \log \pi - \sum_{i=1}^{\numData} (1-\dataScalar_i) \log (1-\pi)
  \end{align*}$$
* Solution from above is 
  $$
  \pi = \frac{\sum_{i=1}^{\numData} \dataScalar_i}{\numData}.
  $$}

\newslide{Fit Conditional}

\slides{
* Minimize conditional distribution:
  $$
  \errorFunction(\paramVector) = -\sum_{i=1}^{\numData} \sum_{j=1}^{\dataDim} \log p(\inputScalar_{i, j} |\dataScalar_i, \paramVector),
  $$
* Implies making an assumption about it's form.
* The right assumption will depend on the data. 
* E.g. for real valued data, use a Gaussian
  $$
  p(\inputScalar_{i, j} | \dataScalar_i,\paramVector) =
\frac{1}{\sqrt{2\pi \dataStd_{\dataScalar_i,j}^2}} \exp \left(-\frac{(\inputScalar_{i,j} - \mu_{\dataScalar_i,
j})^2}{\dataStd_{\dataScalar_i,j}^2}\right),
  $$
}

\include{_ml/includes/nigerian-nmis-data-naive-bayes.md}

\newslide{Compute Posterior for Test Point Label}
\slides{
* We know that
  $$
  P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector)p(\dataVector,\inputMatrix, \inputVector^*|\paramVector) = p(\dataScalar*, \dataVector, \inputMatrix,\inputVector^*| \paramVector)
  $$
* This implies
  $$
  P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector) = \frac{p(\dataScalar*, \dataVector, \inputMatrix, \inputVector^*| \paramVector)}{p(\dataVector, \inputMatrix, \inputVector^*|\paramVector)}
  $$
}
\newslide{Compute Posterior for Test Point Label}
\slides{
* From conditional independence assumptions
  $$
  p(\dataScalar^*, \dataVector, \inputMatrix, \inputVector^*| \paramVector) = \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi)
  $$
* We also need
  $$
  p(\dataVector, \inputMatrix, \inputVector^*|\paramVector)$$ which can be
found from $$p(\dataScalar^*, \dataVector, \inputMatrix, \inputVector^*| \paramVector)
  $$
* Using the *sum rule* of probability,
  $$
  p(\dataVector, \inputMatrix, \inputVector^*|\paramVector) = \sum_{\dataScalar^*=0}^1 p(\dataScalar^*, \dataVector, \inputMatrix, \inputVector^*| \paramVector).
  $$
}
\newslide{Independence Assumptions}
\slides{
* From independence assumptions
  $$
  p(\dataVector, \inputMatrix, \inputVector^*| \paramVector) = \sum_{\dataScalar^*=0}^1 \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi).
  $$
* Substitute both forms to recover,
  $$
  P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector)  = \frac{\prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi)}{\sum_{\dataScalar^*=0}^1 \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi)}
  $$
}
\newslide{Cancelation}
\slides{
* Note training data terms cancel.
  $$
  p(\dataScalar^*| \inputVector^*, \paramVector) = \frac{\prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)}{\sum_{\dataScalar^*=0}^1 \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)}
  $$
* This formula is also fairly straightforward to implement for different class conditional distributions.
}
\notes{
\subsection{Making Predictions}

Naive Bayes has given us the class conditional densities: $p(\inputVector_i | \dataScalar_i, \paramVector)$. To make predictions with these densities we need to form the distribution given by
$$
P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector)
$$
This can be computed by using the product rule. We know that
$$
P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector)p(\dataVector, \inputMatrix, \inputVector^*|\paramVector) = p(\dataScalar*, \dataVector, \inputMatrix, \inputVector^*| \paramVector)
$$
implying that 
$$
P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector) = \frac{p(\dataScalar*, \dataVector, \inputMatrix, \inputVector^*| \paramVector)}{p(\dataVector, \inputMatrix, \inputVector^*|\paramVector)}
$$
and we've already defined $p(\dataScalar^*, \dataVector, \inputMatrix, \inputVector^*| \paramVector)$ using our conditional independence assumptions above 
$$
p(\dataScalar^*, \dataVector, \inputMatrix, \inputVector^*| \paramVector) = \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi)
$$
The other required density is
$$
p(\dataVector, \inputMatrix, \inputVector^*|\paramVector)
$$ which can be found from $$p(\dataScalar^*, \dataVector, \inputMatrix, \inputVector^*| \paramVector)$$ using the *sum rule* of probability,
$$
p(\dataVector, \inputMatrix, \inputVector^*|\paramVector) = \sum_{\dataScalar^*=0}^1 p(\dataScalar^*, \dataVector, \inputMatrix, \inputVector^*| \paramVector).
$$
Because of our independence assumptions that is simply equal to
$$
p(\dataVector, \inputMatrix, \inputVector^*| \paramVector) = \sum_{\dataScalar^*=0}^1 \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi).
$$
Substituting both forms in to recover our distribution over the test label conditioned on the training data we have,
$$
P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector) = \frac{\prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi)}{\sum_{\dataScalar^*=0}^1 \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)\prod_{i=1}^{\numData} \prod_{j=1}^{\dataDim} p(\inputScalar_{i,j}|\dataScalar_i, \paramVector)p(\dataScalar_i|\pi)}
$$
and we notice that all the terms associated with the training data actually cancel, the test prediction is *conditionally independent* of the training data *given* the parameters. This is a result of our conditional independence assumptions over the data points.
$$
p(\dataScalar^*| \inputVector^*, \paramVector) = \frac{\prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i,
\paramVector)p(\dataScalar^*|\pi)}{\sum_{\dataScalar^*=0}^1 \prod_{j=1}^{\dataDim} p(\inputScalar^*_{j}|\dataScalar^*_i, \paramVector)p(\dataScalar^*|\pi)}
$$
This formula is also fairly straightforward to implement. First we implement the log probabilities for the Gaussian density.

\code{def log_gaussian(x, mu, sigma2):
    return -0.5* np.log(2*np.pi*sigma2)-((x-mu)**2)/(2*sigma2)}

Now for any test point we compute the joint distribution of the Gaussian features by *summing* their log probabilities. Working in log space can be a considerable advantage over computing the probabilities directly: as the number of features we include goes up, because all the probabilities are less than 1, the joint probability will become smaller and smaller, and may be difficult to represent accurately (or even underflow). Working in log space can ameliorate this problem. We can also compute the log probability for the Bernoulli distribution.

\code{def log_bernoulli(x, theta):
    return x*np.log(theta) + (1-x)*np.log(1-theta)}


\subsection{Laplace Smoothing}

Before we proceed, let's just pause and think for a moment what will happen if `theta` here is either zero or one. This will result in $\log 0 = -\infty$ and cause numerical problems.  This definitely can happen in practice. If some of the features are rare or very common across the data set then the maximum likelihood solution could find values of zero or one respectively. Such values are problematic because they cause posterior probabilities of class membership of either one or zero. In practice we deal with this using *Laplace smoothing* (which actually has an interpretation as a Bayesian fit of the Bernoulli distribution. Laplace used an example of the sun rising each day, and a wish to predict the sun rise the following day to describe his idea of smoothing, which can be found at the bottom of following page from Laplace's 'Essai Philosophique ...'}

\newslide{Laplace Smoothing}

\includegooglebook{1YQPAAAAQAAJ}{PA16}

\notes{
Laplace suggests that when computing the probability of an event where a success or failure is rare (he uses an example of the sun rising across the last 5,000 years or 1,826,213 days) that even though only successes have been observed (in the sun rising case) that the odds for tomorrow shouldn't be given as
$$
\frac{1,826,213}{1,826,213} = 1
$$
but rather by adding one to the numerator and two to the denominator,
$$
\frac{1,826,213 + 1}{1,826,213 + 2} = 0.99999945.
$$
This technique is sometimes called a 'pseudocount technique' because it has an intepretation of assuming some observations before you start, it's as if instead of observing $\sum_{i}\dataScalar_i$ successes you have an additional success, $\sum_{i}\dataScalar_i + 1$ and instead of having observed $n$ events you've observed $\numData + 2$. So we can think of Laplace's idea saying (before we start) that we have 'two observations worth of belief, that the odds are 50/50', because before we start (i.e. when $\numData=0$) our estimate is 0.5, yet because the effective $n$ is only 2, this estimate is quickly overwhelmed by data. Laplace used ideas like this a lot, and it is known as his 'principle of insufficient reason'. His idea was that in the absence of knowledge (i.e. before we start) we should assume that all possible outcomes are equally likely. This idea has a modern counterpart, known as the [principle of maximum entropy](http://en.wikipedia.org/wiki/Principle_of_maximum_entropy). A lot of the theory of this approach was developed by [Ed Jaynes](http://en.wikipedia.org/wiki/Edwin_Thompson_Jaynes), who according to his erstwhile collaborator and friend, John Skilling, learnt French as an undergraduate by reading the works of Laplace. Although John also related that Jaynes's spoken French was not up to the standard of his scientific French. For me Ed Jaynes's work very much carries on the tradition of Laplace into the modern era, in particular his focus on Bayesian approaches. I'm very proud to have met those that knew and worked with him. It turns out that Laplace's idea also has a Bayesian interpretation (as Laplace understood), it comes from assuming a particular prior density for the parameter $\pi$, but we won't explore that interpretation for the moment, and merely choose to estimate the probability as,}\newslide{Pseudo Counts}
$$
\pi = \frac{\sum_{i=1}^{\numData} \dataScalar_i + 1}{\numData + 2}
$$
\notes{to prevent problems with certainty causing numerical issues and misclassifications. Let's refit the Bernoulli features now.}

\code{# fit the Bernoulli with Laplace smoothing.
for column in X_train:
    if column in Bernoulli:
        Bernoulli[column]['theta_0'] = (X_train[column][~y_train].sum() + 1)/((~y_train).sum() + 2)
        Bernoulli[column]['theta_1'] = (X_train[column][y_train].sum() + 1)/((y_train).sum() + 2)}

\notes{That places us in a position to write the prediction function.}

\setupcode{import numpy as np
import pandas as pd}
\code{def predict(X_test, Gaussian, Bernoulli, prior):
    log_positive = pd.Series(data = np.zeros(X_test.shape[0]), index=X_test.index)
    log_negative = pd.Series(data = np.zeros(X_test.shape[0]), index=X_test.index)
    for column in X_test.columns:
        if column in Gaussian:
            log_positive += log_gaussian(X_test[column], Gaussian[column]['mu_1'], Gaussian[column]['sigma2_1'])
            log_negative += log_gaussian(X_test[column], Gaussian[column]['mu_0'], Gaussian[column]['sigma2_0'])
        elif column in Bernoulli:
            log_positive += log_bernoulli(X_test[column], Bernoulli[column]['theta_1'])
            log_negative += log_bernoulli(X_test[column], Bernoulli[column]['theta_0'])
            
    v = np.zeros_like(log_positive.values)
    for i in range(X_test.shape[0]):
        v[i] = np.exp(log_positive.values[i] + np.log(prior))/(np.exp(log_positive.values[i] + np.log(prior)) 
                                                               + np.exp(log_negative.values[i] + np.log(1-prior)))
    return v
    #return np.exp(log_positive + np.log(prior))/(np.exp(log_positive + np.log(prior)) + np.exp(log_negative + np.log(1-prior)))}

\notes{Now we are in a position to make the predictions for the test data.}

\code{p_y = predict(X_test, Gaussian, Bernoulli, prior)}

\notes{We can test the quality of the predictions in the following way. Firstly, we can threshold our probabilities at 0.5, allocating points with greater than 50% probability of membership of the positive class to the positive class. We can then compare to the true values, and see how many of these values we got correct. This is our total number correct.}

\code{correct = y_test.eq(p_y>0.5)
total_correct = sum(correct)
print("Total correct", total_correct, " out of ", len(y_test), "which is", float(total_correct)/len(y_test), "%")}

\notes{We can also now plot the [confusion matrix](http://en.wikipedia.org/wiki/Confusion_matrix). A confusion matrix tells us where we are making mistakes. Along the diagonal it stores the *true positives*, the points that were positive class that we classified correctly, and the *true negatives*, the points that were negative class and that we classified correctly. The off diagonal terms contain the false positives and the false negatives. Along the rows of the matrix we place the actual class, and along the columns we place our predicted class.}

\code{confusion_matrix = pd.DataFrame(data=np.zeros((2,2)), 
                                columns=['predicted no maternity', 'predicted maternity'],
                                index =['actual no maternity','actual maternity'])
confusion_matrix['predicted maternity']['actual maternity'] = (y_test & (p_y>0.5)).sum()
confusion_matrix['predicted maternity']['actual no maternity'] = (~y_test & (p_y>0.5)).sum()
confusion_matrix['predicted no maternity']['actual maternity'] = (y_test & ~(p_y>0.5)).sum()
confusion_matrix['predicted no maternity']['actual no maternity'] = (~y_test & ~(p_y>0.5)).sum()
confusion_matrix}

\exercise{How can you improve your classification, are all the features equally valid? Are some features more helpful than others? What happens if you remove features that appear to be less helpful. How might you select such features?}

\exercise{We have decided to classify positive if probability of maternity is greater than 0.5. This has led us to accidentally classify some facilities as havien't facilities for maternity when in fact they don't. Imagine you wish to ensure that a facility handles maternity. With your test set how low do you have to set the threshold to avoid all the false negatives (i.e. facilities where you predicted there was no maternity, but in actuality there were?}

\notes{
\subsection{Making Predictions}

Naive Bayes has given us the class conditional densities: $p(\inputVector_i | \dataScalar_i, \paramVector)$. To make predictions with these densities we need to form the distribution given by
$$
P(\dataScalar^*| \dataVector, \inputMatrix, \inputVector^*, \paramVector)
$$

\exercise{Write down the negative log likelihood of the Gaussian density over a vector of variables $\inputVector$. Assume independence between each variable. Minimize this objective to obtain the maximum likelihood solution of the form.
$$
\mu = \frac{\sum_{i=1}^{\numData} \inputScalar_i}{\numData}
$$
$$
\dataStd^2 = \frac{\sum_{i=1}^{\numData} (\inputScalar_i - \mu)^2}{\numData}
$$}

If the input data was *binary* then we could also make use of the Bernoulli distribution for the features. For that case we would have the form, 
$$
p(\inputScalar_{i, j} | \dataScalar_i,\paramVector) = \theta_{\dataScalar_i, j}^{\inputScalar_{i, j}}(1-\theta_{\dataScalar_i, j})^{(1-\inputScalar_{i,j})},
$$
where $\theta_{1, j}$ is the probability that the $j$th feature is on if $\dataScalar_i$ is 1.

In either case, maximum likelihood fitting would proceed in the same way. The objective has the form,
$$
\errorFunction(\paramVector) = -\sum_{j=1}^{\dataDim} \sum_{i=1}^{\numData} \log p(\inputScalar_{i,j} |\dataScalar_i, \paramVector),
$$
and if, as above, the parameters of the distributions are specific to each feature vector (we had means and variances for each continuous feature, and a probability for each binary feature) then we can use the fact that these parameters separate into disjoint subsets across the features to write,
$$
\begin{align*}
\errorFunction(\paramVector) &= -\sum_{j=1}^{\dataDim} \sum_{i=1}^{\numData} \log
p(\inputScalar_{i,j} |\dataScalar_i, \paramVector_j)\\
& \sum_{j=1}^{\dataDim}
\errorFunction(\paramVector_j),
\end{align*}
$$
which means we can minimize our objective on each feature independently. 

These characteristics mean that naive Bayes scales very well with big data. To fit the model we consider each feature in turn, we select the positive class and fit parameters for that class, then we select each negative class and fit features for that class. We have code below.}


\newslide{Naive Bayes Summary}

\slides{
* Model *full* joint distribution of data, $p(\dataVector, \inputMatrix | \paramVector, \pi)$
* Make conditional independence assumptions about the data.
  * feature conditional independence
  * data conditional independence
* Fast to implement, works on very large data.
* Despite simple assumptions can perform better than expected.
}

\notes{
\subsection{Naive Bayes Summary}

Naive Bayes is making very simple assumptions about the data, in particular it is modeling the full *joint* probability of the data set, $p(\dataVector, \inputMatrix | \paramVector, \pi)$ by very strong assumptions about factorizations that are unlikely to be true in practice. The data conditional independence assumption is common, and relies on a rich parameter vector to absorb all the information in the training data. The additional assumption of naive Bayes is that features are conditional independent given the class label $\dataScalar_i$ (and the parameter vector, $\paramVector$. This is quite a strong assumption. However, it causes the objective function to decompose into parts which can be independently fitted to the different feature vectors, meaning it is very easy to fit the model to large data. It is also clear how we should handle *streaming* data and *missing* data. This means that the model can be run 'live', adapting parameters and information as it arrives. Indeed, the model is even capable of dealing with new *features* that might arrive at run time. Such is the strength of the modeling the joint probability density. However, the factorization assumption that allows us to do this efficiently is very strong and may lead to poor decision boundaries in practice.
}
