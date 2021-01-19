\ifndef{ppcaMarginalLikelihood}
\define{ppcaMarginalLikelihood}

\editme

\section{PPCA Marginal Likelihood}

We have developed the posterior density over the latent variables
given the data and the parameters, and due to symmetries in the underlying
prediction function, it has a very similar form to its sister density, the
posterior of the weights given the data from Bayesian regression. Two key
differences are as follows. If we were to do a Bayesian multiple output
regression we would find that the marginal likelihood of the data is independent
across the features and correlated across the data,
$$
p(\dataMatrix|\latentMatrix)
= \prod_{j=1}^p \gaussianDist{\dataVector_{:, j}}{\zerosVector}{
\alpha\latentMatrix\latentMatrix^\top + \noiseStd^2 \eye}
$$
where $\dataVector_{:,
j}$ is a column of the data matrix and the independence is across the
*features*, in probabilistic PCA the marginal likelihood has the form,
$$
p(\dataMatrix|\mappingMatrix) = \prod_{i=1}^\numData \gaussianDist{\dataVector_{i,
:}}{\zerosVector}{\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye}
$$
where
$\dataVector_{i, :}$ is a row of the data matrix $\dataMatrix$ and the
independence is across the data points.

\section{Computation of the Log Likelihood}

The quality of the model can be assessed using the log likelihood of this
Gaussian form.
$$
\log p(\dataMatrix|\mappingMatrix) = -\frac{\numData}{2} \log \left|
\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye \right| -\frac{1}{2}
\sum_{i=1}^\numData \dataVector_{i, :}^\top \left(\mappingMatrix\mappingMatrix^\top + \noiseStd^2
\eye\right)^{-1} \dataVector_{i, :} +\text{const}
$$
but this can be computed more rapidly by exploiting the low rank form
of the covariance covariance, $\covarianceMatrix =
\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye$ and the fact
that $\mappingMatrix = \mathbf{U}\mathbf{L}\mathbf{R}^\top$.
Specifically, we first use the decomposition of $\mappingMatrix$ to
write:
$$
-\frac{\numData}{2} \log \left| \mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye \right|
= -\frac{\numData}{2} \sum_{i=1}^q \log (\ell_i^2 + \noiseStd^2) - \frac{n(p-q)}{2}\log
\noiseStd^2,
$$
where $\ell_i$ is the $i$th diagonal element of $\mathbf{L}$.
Next, we use the [Woodbury matrix
identity](http://en.wikipedia.org/wiki/Woodbury_matrix_identity) which allows us
to write the inverse as a quantity which contains another inverse in a smaller
matrix:
$$
(\noiseStd^2 \eye + \mappingMatrix\mappingMatrix^\top)^{-1} =
\noiseStd^{-2}\eye-\noiseStd^{-4}\mappingMatrix{\underbrace{(\eye+\noiseStd^{-2}\mappingMatrix^\top\mappingMatrix)}_{\covarianceMatrix_x}}^{-1}\mappingMatrix^\top
$$
So, it turns out that the original inversion of the $p \times p$ matrix can
be done by forming a quantity which contains the inversion of a $q \times q$
matrix which, moreover, turns out to be the quantity $\covarianceMatrix_x$ of the
posterior.

Now, we put everything together to obtain:
$$
\log p(\dataMatrix|\mappingMatrix) = -\frac{\numData}{2} \sum_{i=1}^q
\log (\ell_i^2 + \noiseStd^2)
- \frac{n(p-q)}{2}\log \noiseStd^2 - \frac{1}{2} \trace{\dataMatrix^\top \left(
\noiseStd^{-2}\eye-\noiseStd^{-4}\mappingMatrix \covarianceMatrix_x
\mappingMatrix^\top \right) \dataMatrix} + \text{const},
$$
where we used the fact that a scalar sum can be written as
$\sum_{i=1}^\numData \dataVector_{i,:}^\top \kernelMatrix
\dataVector_{i,:} = \trace{\dataMatrix^\top \kernelMatrix
\dataMatrix}$, for any matrix $\kernelMatrix$ of appropriate
dimensions. We now use the properties of the trace
$\trace{\mathbf{A}+\mathbf{B}}=\trace{\mathbf{A}}+\trace{\mathbf{B}}$
and $\trace{c \mathbf{A}} = c \trace{\mathbf{A}}$, where $c$ is
a scalar and $\mathbf{A},\mathbf{B}$ matrices of compatible
sizes. Therefore, the final log likelihood takes the form:
$$
\log p(\dataMatrix|\mappingMatrix) = -\frac{\numData}{2}
\sum_{i=1}^q \log (\ell_i^2 + \noiseStd^2) - \frac{\numData(p-q)}{2}\log \noiseStd^2 -
\frac{\noiseStd^{-2}}{2} \trace{\dataMatrix^\top \dataMatrix}
+\frac{\noiseStd^{-4}}{2} \trace{\mathbf{B}\covarianceMatrix_x\mathbf{B}^\top} +
\text{const}
$$
where we also defined $\mathbf{B}=\dataMatrix^\top\mappingMatrix$.
Finally, notice that
$\trace{\dataMatrix\dataMatrix^\top}=\trace{\dataMatrix^\top\dataMatrix}$ can
be computed faster as the sum of all the elements of
$\dataMatrix\circ\dataMatrix$, where $\circ$ denotes the element-wise (or
[Hadamard](http://en.wikipedia.org/wiki/Hadamard_product_(matrices)) product.

\endif
