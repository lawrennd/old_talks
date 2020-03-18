\ifndef{theBayesianApproach}
\define{theBayesianApproach}
\editme

\notes{
\subsection{The Bayesian Approach}

Now we will study Bayesian approaches to regression. In the Bayesian approach we define a *prior* density over our parameters, $m$ and $c$ or more generally $\mappingVector$. This prior distribution gives us a range of expected values for our parameter *before* we have seen the data. The object in Bayesian inference is to then compute the*posterior* density which is the effect on the density of having observed the data. In standard probability notation we write the prior distribution as, 
$$
p(\mappingVector),
$$
so it is the *marginal* distribution for the parameters, i.e. the distribution we have for the parameters without any knowledge about the data. The posterior distribution is written as, 
$$
p(\mappingVector|\dataVector, \inputMatrix).
$$
So the posterior distribution is the *conditional* distribution for the parameters given the data (which in this case consists of pairs of observations including response variables (or targets), $\dataScalar_i$, and covariates (or inputs) $\inputVector_i$. Where here we are allowing the inputs to be multivariate. 

The posterior is recovered from the prior using *Bayes' rule*. Which is simply a rewriting of the product rule. We can recover Bayes' rule as follows. The product rule of probability tells us that the joint distribution is given as the product of the conditional and the marginal. Dropping the inputs from our conditioning for the moment we have,
$$
p(\mappingVector, \dataVector)=p(\dataVector|\mappingVector)p(\mappingVector),
$$
where we see we have related the joint density to the prior density and the *likelihood* from our previous investigation of regression,
$$
p(\dataVector|\mappingVector) = \prod_{i=1}^\numData\gaussianDist{\dataScalar_i}{\mappingVector^\top \inputVector_i}{ \dataStd^2}
$$
which arises from the assumption that our observation is given by
$$
\dataScalar_i = \mappingVector^\top \inputVector_i + \noiseScalar_i.
$$
In other words this is the Gaussian likelihood we have been fitting by minimizing the sum of squares. Have a look at [the session on multivariate regression](./03-linear-regression.html) as a reminder.

We've introduce the likelihood, but we don't have  relationship with the posterior, however, the product rule can also be written in the following way 
$$
p(\mappingVector, \dataVector) = p(\mappingVector|\dataVector)p(\dataVector),
$$
where here we have simply used the opposite conditioning. We've already introduced the *posterior* density above. This is the density that represents our belief about the parameters *after* observing the data. This is combined with the *marginal likelihood*, sometimes also known as the evidence. It is the marginal likelihood, because it is the original likelihood of the data with the parameters marginalised, $p(\dataVector)$. Here it's conditioned on nothing, but in practice you should always remember that everything here is conditioned on things like model choice: which set of basis functions. Because it's a regression problem, its also conditioned on the inputs. Using the equalitybetween the two different forms of the joint density  we recover
$$
p(\mappingVector|\dataVector) = \frac{p(\dataVector|\mappingVector)p(\mappingVector)}{p(\dataVector)}
$$
where we divided both sides by $p(\dataVector)$ to recover this result. Let's re-introduce the conditioning on the input locations (or covariates), $\inputMatrix$ to write the full form of Bayes' rule for the regression problem. 
$$
p(\mappingVector|\dataVector, \inputMatrix) = \frac{p(\dataVector|\mappingVector, \inputMatrix)p(\mappingVector)}{p(\dataVector|\inputMatrix)}
$$
where the posterior density for the parameters given the data is $p(\mappingVector|\dataVector, \inputMatrix)$, the marginal likelihood is $p(\dataVector|\inputMatrix)$, the prior density is $p(\mappingVector)$ and our original regression likelihood is given by $p(\dataVector|\mappingVector, \inputMatrix)$. It turns out that to compute the posterior the only things we need to do are define the prior and the likelihood. The other term on the right hand side can be computed by *the sum rule*. It is one of the key equations of Bayesian inference, the expectation of the likelihood under the prior, this process is known as marginalisation,
$$
p(\dataVector|\inputMatrix) = \int p(\dataVector|\mappingVector,\inputMatrix)p(\mappingVector) \text{d}\mappingVector
$$
I like the term marginalisation, and the description of the probability as the *marginal likelihood*, because (for me) it somewhat has the implication that the variable name has been removed, and (perhaps) written in the margin. Marginalisation of a variable goes from a likelihood where the variable is in place, to a new likelihood where all possible values of that variable (under the prior) have been considered and weighted in the integral. This implies that all we need for specifying our model is to define the likelihood and the prior. We already have our likelihood from our earlier discussion, so our focus now turns to the prior density.
}

\endif
