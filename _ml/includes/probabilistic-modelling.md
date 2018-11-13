\subsection{Probabilistic Modelling}

\slides{
* Probabilistically we want,}\notes{
This Bayesian approach is designed to deal with uncertainty arising from fitting our prediction function to the data we have, a reduced data set.

The Bayesian approach can be derived from a broader understanding of what our objective is. If we accept that we can jointly represent all things that happen in the world with a probability distribution, then we can interogate that probability to make predictions. So, if we are interested in predictions, $\dataScalar_*$ at future points input locations of interest, $\inputVector_*$ given previously training data, $\dataVector$ and corresponding inputs, $\inputMatrix$, then we are really interogating the following probability density,}
$$
p(\dataScalar_*|\dataVector, \inputMatrix, \inputVector_*),
$$\slides{
 $\dataScalar_*$ is a test output
 $\inputVector_*$ is a test input
 $\inputMatrix$ is a training input matrix
$\dataVector$ is training outputs
}\notes{
there is nothing controversial here, as long as you accept that you have a good joint model of the world around you that relates test data to training data, $p(\dataScalar_*, \dataVector, \inputMatrix, \inputVector_*)$ then this conditional distribution can be recovered through standard rules of probability ($\text{data} + \text{model} \rightarrow \text{prediction}$). 
}
\slides{
\newslide{Joint Model of World}

}\notes{We can construct this joint density through the use of the following decomposition:}
$$
p(\dataScalar_*|\dataVector, \inputMatrix, \inputVector_*) = \int p(\dataScalar_*|\inputVector_*, \mappingMatrix) p(\mappingMatrix | \dataVector, \inputMatrix) \text{d} \mappingMatrix
$$
\slides{
. . .

$\mappingMatrix$  contains $\mappingMatrix_1$ and $\mappingMatrix_2$

$p(\mappingMatrix | \dataVector, \inputMatrix)$ is posterior density
}\notes{
where, for convenience, we are assuming *all* the parameters of the model are now represented by $\parameterVector$ (which contains $\mappingMatrix$ and $\mappingMatrixTwo$) and $p(\parameterVector | \dataVector, \inputMatrix)$ is recognised as the posterior density of the parameters given data and $p(\dataScalar_*|\inputVector_*, \parameterVector)$ is the *likelihood* of an individual test data point given the parameters.}

\slides{
\newslide{Likelihood}

$p(\dataScalar|\inputVector, \mappingMatrix)$ is the *likelihood* of data point

. . .

Normally assume independence:
}\notes{
The likelihood of the data is normally assumed to be independent across the parameters,
}$$
p(\dataVector|\inputMatrix, \mappingMatrix) \prod_{i=1}^\numData p(\dataScalar_i|\inputVector_i, \mappingMatrix),$$
\notes{
and if that is so, it is easy to extend our predictions across all future, potential, locations,
$$
p(\dataVector_*|\dataVector, \inputMatrix, \inputMatrix_*) = \int p(\dataVector_*|\inputMatrix_*, \parameterVector) p(\parameterVector | \dataVector, \inputMatrix) \text{d} \parameterVector.
$$
}

\slides{
\newslide{Likelihood and Prediction Function}

$$
p(\dataScalar_i | \mappingFunction(\inputVector_i)) = \frac{1}{\sqrt{2\pi \dataStd^2}} \exp\left(-\frac{\left(\dataScalar_i - \mappingFunction(\inputVector_i)\right)^2}{2\dataStd^2}\right)
$$
}\notes{
The likelihood is also where the *prediction function* is incorporated. For example in the regression case, we consider an objective based around the Gaussian density,
$$
p(\dataScalar_i | \mappingFunction(\inputVector_i)) = \frac{1}{\sqrt{2\pi \dataStd^2}} \exp\left(-\frac{\left(\dataScalar_i - \mappingFunction(\inputVector_i)\right)^2}{2\dataStd^2}\right)
$$
}

\slides{
\newslide{Unsupervised Learning}

* Can also consider priors over latents
$$
p(\dataVector_*|\dataVector) = \int p(\dataVector_*|\inputMatrix_*, \mappingMatrix) p(\mappingMatrix | \dataVector, \inputMatrix) p(\inputMatrix) p(\inputMatrix_*) \text{d} \mappingMatrix \text{d} \inputMatrix \text{d}\inputMatrix_*
$$

* This gives *unsupervised learning*.

}\notes{
In short, that is the classical approach to probabilistic inference, and all approaches to Bayesian neural networks fall within this path. For a deep probabilistic model, we can simply take this one stage further and place a probability distribution over the input locations,
$$
p(\dataVector_*|\dataVector) = \int p(\dataVector_*|\inputMatrix_*, \parameterVector) p(\parameterVector | \dataVector, \inputMatrix) p(\inputMatrix) p(\inputMatrix_*) \text{d} \parameterVector \text{d} \inputMatrix \text{d}\inputMatrix_*
$$
and we have *unsupervised learning*  (from where we can get deep generative models). 
}
\slides{
\newslide{Probabilistic Inference}

* Data: $\dataVector$

* Model: $p(\dataVector, \dataVector^*)$

* Prediction: $p(\dataVector^*| \dataVector)$
}
