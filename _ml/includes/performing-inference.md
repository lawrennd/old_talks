### Performing Inference

\slides{
* Easy to write in probabilities

* But underlying this is a wealth of computational challenges.

* High dimensional integrals typically require approximation.
}

\notes{As far as combining our data and our model to form our prediction, the devil is in the detail. While everything is easy to write in terms of probability densities, as we move from $\text{data}$ and $\text{model}$ to $\text{prediction}$ there is that simple $\xrightarrow{\text{compute}}$ sign, which is now burying a wealth of difficulties. Each integral sign above is a high dimensional integral which will typically need approximation. Approximations also come with computational demands. As we consider more complex classes of functions, the challenges around the integrals become harder and prediction of future test data given our model and the data becomes so involved as to be impractical or impossible. 
}

\slidenotes{
### Linear Models

* In statistics, focussed more on *linear* model implied by}{Statisticians realized these challenges early on, indeed, so early that they were actually physicists, both Laplace and Gauss worked on models such as this, in Gauss's case he made his career on prediction of the location of the lost planet (later reclassified as a asteroid, then dwarf planet), Ceres. Gauss and Laplace made use of maximum a posteriori estimates for simplifying their computations and Laplace developed Laplace's method (and invented the Gaussian density) to expand around that mode. But classical statistics needs better guarantees around model performance and interpretation, and as a result has focussed more on the *linear* model implied by} 
  $$
  \mappingFunction(\inputVector) = \left.\mappingVector^{(2)}\right.^\top \activationVector(\mappingMatrix_1, \inputVector)
  $$

\slides{
* Hold $\mappingMatrix_1$ fixed for given analysis.

* Gaussian prior for $\mappingMatrix$,}{by holding $\mappingMatrixTwo$ fixed for any given analysis. In this case, a Gaussian prior is formulated over the parameters $\mappingMatrix$,}
  $$
  \mappingVector^{(2)} \sim \gaussianSamp{\zerosVector}{\covarianceMatrix}.
  $$\notes{
	
The Gaussian likelihood given above implies that the data observation is related to the function by noise corruption so we have,}
  $$
  \dataScalar_i = \mappingFunction(\inputVector_i) + \noiseScalar_i,
  $$
  where 
  $$
  \noiseScalar_i \sim \gaussianSamp{0}{\dataStd^2}
  $$
\slides{

### Linear Gaussian Models

* Normally integrals are complex but for this Gaussian linear case they are trivial.
}\notes{and while normally integrating over high dimensional parameter vectors is highly complex, here it is *trivial*. That is because of a property of the multivariate Gaussian.}

