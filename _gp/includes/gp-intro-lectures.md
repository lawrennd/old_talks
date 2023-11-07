\ifndef{gpIntroLectures}
\define{gpIntroLectures}

\editme

\subsection{Gaussian Processes}
\slides{
* Basis function models give non-linear predictions.
* Need to choose number and location of basis functions. 
* Gaussian processes is a general framework (basis functions special case)
* Within the framework you can consider models with infinite basis functions.
}
\notes{Models where we model the entire joint distribution of our training data, $p(\dataVector, \inputMatrix)$ are sometimes described as *generative models*. Because we can use sampling to generate data sets that represent all our assumptions. However, as we discussed in the sessions on \refnotes{logistic regression}{logistic-regression} and \refnotes{naive Bayes}{naive-bayes}, this can be a bad idea, because if our assumptions are wrong then we can make poor predictions. We can try to make more complex assumptions about data to alleviate the problem, but then this typically leads to challenges for tractable application of the sum and rules of probability that are needed to compute the relevant marginal and conditional densities. If we know the form of the question we wish to answer then we typically try and represent that directly, through $p(\dataVector|\inputMatrix)$.  In practice, we also have been making assumptions of conditional independence given the model parameters,}
$$
p(\dataVector|\inputMatrix, \mappingVector) =
\prod_{i=1}^{\numData} p(\dataScalar_i | \inputVector_i, \mappingVector)
$$
\notes{Gaussian processes are *not* normally considered to be *generative models*, but we will be much more interested in the principles of conditioning in Gaussian processes because we will use conditioning to make predictions between our test and training data. We will avoid the data conditional indpendence assumption in favour of a richer assumption about the data, in a Gaussian process we assume data is *jointly Gaussian* with a particular mean and covariance,}
$$
\dataVector|\inputMatrix \sim \gaussianSamp{\mathbf{m}(\inputMatrix)}{\kernelMatrix(\inputMatrix)},
$$
\notes{where the conditioning is on the inputs $\inputMatrix$ which are used for computing the mean and covariance. For this reason they are known as mean and covariance functions.}

\endif
