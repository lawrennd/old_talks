\newslide{Multivariate Gaussian Properties}
\slides{
* If}\notes{
Let's first of all review the properties of the multivariate Gaussian distribution that make linear Gaussian models easier to deal with. We'll return to the, perhaps surprising, result on the parameters within the nonlinearity, $\parameterVector$, shortly.

To work with linear Gaussian models, to find the marginal likelihood all you need to know is the following rules. If}
$$
\dataVector = \mappingMatrix \inputVector + \noiseVector,
$$
\slides{
* Assume}\notes{where $\dataVector$, $\inputVector$ and $\noiseVector$ are vectors and we assume that $\inputVector$ and $\noiseVector$ are drawn from multivariate Gaussians,}
$$\begin{align}
\inputVector & \sim \gaussianSamp{\meanVector}{\covarianceMatrix}\\
\noiseVector & \sim \gaussianSamp{\zerosVector}{\covarianceMatrixTwo}
\end{align}$$
\slides{
* Then}\notes{then we know that $\dataVector$ is also drawn from a multivariate Gaussian with,}
$$
\dataVector \sim \gaussianSamp{\mappingMatrix\meanVector}{\mappingMatrix\covarianceMatrix\mappingMatrix^\top + \covarianceMatrixTwo}.
$$
\slides{If $\covarianceMatrixTwo=\dataStd^2\eye$, this is Probabilistic Principal Component Analysis [@Tipping:probpca99], because we integrated out the inputs (or *latent* variables they would be called in that case).}
\notes{With apprioriately defined covariance, $\covarianceTwoMatrix$, this is actually the marginal likelihood for Factor Analysis, or Probabilistic Principal Component Analysis [@Tipping:probpca99], because we integrated out the inputs (or *latent* variables they would be called in that case).}

\newslide{Non linear on Inputs}

\slides{
* Set each activation function computed at each data point to be
}\notes{However, we are focussing on what happens in models which are non-linear in the inputs, whereas the above would be *linear* in the inputs. To consider these, we introduce a matrix, called the design matrix. We set each activation function computed at each data point to be}
$$
\activationScalar_{i,j} = \activationScalar(\mappingVector^{(1)}_{j}, \inputVector_{i})
$$
\slides{Define  *design matrix*}\notes{and define the matrix of activations (known as the *design matrix* in statistics) to be,}
$$
\activationMatrix = 
\begin{bmatrix}
\activationScalar_{1, 1} & \activationScalar_{1, 2} & \dots & \activationScalar_{1, \numHidden} \\
\activationScalar_{1, 2} & \activationScalar_{1, 2} & \dots & \activationScalar_{1, \numData} \\
\vdots & \vdots & \ddots & \vdots \\
\activationScalar_{\numData, 1} & \activationScalar_{\numData, 2} & \dots & \activationScalar_{\numData, \numHidden}
\end{bmatrix}.
$$
\notes{By convention this matrix always has $\numData$ rows and $\numHidden$ columns, now if we define the vector of all noise corruptions, $\noiseVector = \left[\noiseScalar_1, \dots \noiseScalar_\numData\right]^\top$.}


\newslide{Matrix Representation of a Neural Network}
\slides{
$$\dataScalar\left(\inputVector\right) = \activationVector\left(\inputVector\right)^\top \mappingVector + \noiseScalar$$

. . .

$$\dataVector = \activationMatrix\mappingVector + \noiseVector$$

. . .

$$\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$$
}
\newslide{Prior Density}
\slides{
* Define}
\notes{
If we define the prior distribution over the vector $\mappingVector$ to be Gaussian,}
$$
\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha\eye},
$$

\slides{
* Rules of multivariate Gaussians to see that,}
\notes{
then we can use rules of multivariate Gaussians to see that,}
$$
\dataVector \sim \gaussianSamp{\zerosVector}{\alpha \activationMatrix \activationMatrix^\top + \dataStd^2 \eye}.
$$
\slides{
$$
\kernelMatrix = \alpha \activationMatrix \activationMatrix^\top + \dataStd^2 \eye.
$$}

\newslide{Joint Gaussian Density}
\slides{
* Elements are a function $\kernel_{i,j} = \kernel\left(\inputVector_i, \inputVector_j\right)$
}\notes{In other words, our training data is distributed as a multivariate Gaussian, with zero mean and a covariance given by}
$$
\kernelMatrix = \alpha \activationMatrix \activationMatrix^\top + \dataStd^2 \eye.
$$
\notes{
This is an $\numData \times \numData$ size matrix. Its elements are in the form of a function. The maths shows that any element, index by $i$ and $j$, is a function *only* of inputs associated with data points $i$ and $j$, $\dataVector_i$, $\dataVector_j$. $\kernel_{i,j} = \kernel\left(\inputVector_i, \inputVector_j\right)$}

\newslide{Covariance Function}
\notes{
If we look at the portion of this function associated only with $\mappingFunction(\cdot)$, i.e. we remove the noise, then we can write down the covariance associated with our neural network,}
$$
\kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) = \alpha \activationVector\left(\mappingMatrix_1, \inputVector_i\right)^\top \activationVector\left(\mappingMatrix_1, \inputVector_j\right)
$$
\slides{
* formed by inner products of the rows of the *design matrix*.  
}\notes{so the elements of the covariance or *kernel* matrix are formed by inner products of the rows of the *design matrix*.}


\subsection{Gaussian Process}
\slides{
* Instead of making assumptions about our density over each data point, $\dataScalar_i$ as i.i.d.

*  make a joint Gaussian assumption over our data.

* covariance matrix is now a function of both the parameters of the activation function, $\mappingMatrix_1$, and the input variables, $\inputMatrix$.

* Arises from integrating out $\mappingVector^{(2)}$. 
}\notes{
This is the essence of a Gaussian process. Instead of making assumptions about our density over each data point, $\dataScalar_i$ as i.i.d. we make a joint Gaussian assumption over our data. The covariance matrix is now a function of both the parameters of the activation function, $\mappingMatrixTwo$, and the input variables, $\inputMatrix$. This comes about through integrating out the parameters of the model, $\mappingVector$. 
}

\subsection{Basis Functions}
\slides{
* Can be very complex, such as deep kernels, [@Cho:deep09] or could even put a convolutional neural network inside.
* Viewing a neural network in this way is also what allows us to beform sensible *batch* normalizations [@Ioffe:batch15].
}\notes{
We can basically put anything inside the basis functions, and many people do. These can be deep kernels [@Cho:deep09] or we can learn the parameters of a convolutional neural network inside there.

Viewing a neural network in this way is also what allows us to beform sensible *batch* normalizations [@Ioffe:batch15].
}


