\ifndef{principalComponentAnalysis}
\define{principalComponentAnalysis}

\editme

\subsection{Principal Component Analysis}

* PCA (@Hotelling:analysis33) is a linear embedding.
* Today its presented as:
  * Rotate to find 'directions' in data with maximal variance.
  * How do we find these directions?
* Algorithmically we do this by diagonalizing the sample covariance matrix 
  $$
  \mathbf{S}=\frac{1}{\numData}\sum_{i=1}^\numData \left(\dataVector_{i, :}-\meanVector\right)\left(\dataVector_{i, :} - \meanVector\right)^\top
  $$

\newslide{Principal Component Analysis}

* Find directions in the data, $\latentVector = \mathbf{U}\dataVector$, for which variance is maximized.

\newslide{Lagrangian}

* Solution is found via constrained optimisation (which uses [Lagrange multipliers](https://en.wikipedia.org/wiki/Lagrange_multiplier)):
  $$
  L\left(\mathbf{u}_{1},\lambda_{1}\right)=\mathbf{u}_{1}^{\top}\mathbf{S}\mathbf{u}_{1}+\lambda_{1}\left(1-\mathbf{u}_{1}^{\top}\mathbf{u}_{1}\right)
  $$

* Gradient with respect to $\mathbf{u}_{1}$
  $$\frac{\text{d}L\left(\mathbf{u}_{1},\lambda_{1}\right)}{\text{d}\mathbf{u}_{1}}=2\mathbf{S}\mathbf{u}_{1}-2\lambda_{1}\mathbf{u}_{1}$$
  rearrange to form
  $$\mathbf{S}\mathbf{u}_{1}=\lambda_{1}\mathbf{u}_{1}.$$
  Which is known as an [*eigenvalue problem*](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors).
* Further directions that are *orthogonal* to the first can also be shown to be eigenvectors of the covariance.

\newslide{Linear Dimensionality Reduction}

* Represent data, $\dataMatrix$, with a lower dimensional set of latent variables $\latentMatrix$.
* Assume a linear relationship of the form
  $$
  \dataVector_{i,:}=\mappingMatrix\latentVector_{i,:}+\noiseVector_{i,:},
  $$
  where
  $$
  \noiseVector_{i,:} \sim \gaussianSamp{\zerosVector}{\noiseStd^2\eye}
  $$

\newslide{Linear Latent Variable Model}

**Probabilistic PCA**

\columns{* Define *linear-Gaussian relationship* between latent variables and data.
* **Standard** Latent variable approach:
  * Define Gaussian prior over *latent space*, $\latentMatrix$.
* Integrate out *latent variables*.}{
\figure{\includepng{\diagramsDir/dimred/ppca_graph}{40%}}{Graphical model representing probabilistic PCA.}{ppca-graph}
\slidesmall{
$$
p\left(\dataMatrix|\latentMatrix,\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\mappingMatrix\latentVector_{i,:}}{\noiseStd^2\eye}
$$

$$
p\left(\latentMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\latentVector_{i,:}}{\zerosVector}{\eye}
$$

$$
p\left(\dataMatrix|\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\zerosVector}{\mappingMatrix\mappingMatrix^{\top}+\noiseStd^{2}\eye}
$$}}

\endif
