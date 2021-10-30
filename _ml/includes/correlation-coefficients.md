\ifndef{correlationCoefficients}
\define{correlationCoefficients}

\editme{Correlation Coefficients}

\notes{When considering multivariate data, a very useful notion is the *correlation coefficient*. It gives us the relationship between two variables. The most widely used correlation coefficient is due to Karl Pearson, it's defined in the following way.}

\notes{Let's define our data set to be kept in a matrix, $\dataMatrix$ with $\dataDim$ columns. We assume that $\dataVector_{:, j}$ is the $j$th column of that matrix which corresponds to the $j$th *feature* of the data. Then $\dataScalar_{i,j}$ is the $j$th feature for the $i$th data point. Then the sample mean of that feature/column is given by
$$
\mu_j = \frac{1}{\numData} \sum_{i=1}^\numData\dataScalar_{i,j}
$$
where $\numData$ is the total number of data points (often refered to as the sample size in statistics). Then the variance of that column is given by,[^variance-footnote]
$$
\dataStd_j^2 = \frac{1}{\numData} \sum_{i=1}^\numData (\dataScalar_{i,j} - \mu_j)^2.
$$
The covariance between two variables can also be found as
$$
c_{j,k} = \frac{1}{\numData} \sum_{i=1}^\numData (\dataScalar_{i,j} - \mu_j)(\dataScalar_{i, k} - \mu_k).
$$
If we normalise this covariance by the standard deviaton of the two variables ($\dataStd_j, \dataStd_k$) then we recover Pearson's correlation, often known as Pearson's $\rho$ (the Greek letter rho),
$$
\rho_{j,k} = \frac{c_{j,k}}{\dataStd_{j} \dataStd_{k}}.
$$
Computing the correlation between two values is a way to determine if the values have a relationship with each other.

[^variance-footnote]: sometimes the formula used uses $\frac{1}{\numData-1}$ instead of $\frac{1}{\numData}$. This can be motivated by the observation that this estimate is a *biased* estimate of the true variance. Where bias is a statistical concept relating to how the estimate converges as $\numData \rightarrow \infty$. Personally, I prefer to normalize by $\numData$, which emerges e.g. from performing maximum likelihood with a Gaussian model. }

\notes{One of the problems of statistics, is that when we are working with small data, an apparant correlation might just be a statistical anomally, i.e. a conicidence, that arises just because the quantity of data we have collected is low. In mathematical statistics we make use of hypothesis testing to estimate if a given statistic is "statistically significant".}

\notes{In classical hypothesis testing, we define a *null hypothesis*. This is a hypothesis that contradicts the idea we're interested in. So for correlation analysis, the null hypothesis would be "there is no correlation between the features $i$ and $j$". We then measure the $p$ value. The $p$ value is the probability that we would observe a value as extreme as the one we see if the null hypothesis is true. If this value is low (typically below 0.05 or below 0.01 depending on how stringent we want to be) we *reject the null hypothesis* and the statistic is declared to be significant.}

\notes{Hypothesis testing gives us critical values of the correlation coefficient that we need to believe that there is a relationship between the variables. Those values get smaller as $\numData$ gets larger.}

\subsection{Limitations of Pearson's $\rho$}

\notes{Two major limitations of $\rho$ that you'll normally see mentioned. Firstly, the measure is really focussed on linear relationships between variables. It's possible to construct examples of interesting non-linear relationships between two variables for which the correlation is zero. Secondly, we are often interested in a causal relationship between two variables. Two variables which are not directly related will appear correlated if there is a common factor affecting both variables. For example, we might see a correlation between sales figures for swim gear and ice creams. There is no direct relationship between these to variables, but there is a third variable associated with the passing of the seasons that triggers the sales figures of both swim gear and ice creams to increase.}

\endif
