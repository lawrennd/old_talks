### Linear Gaussian Models {data-transition="None"}

1. linear Gaussian models are easier to deal with 
2. Even the parameters *within* the process can be handled, by considering a particular limit.

### Multivariate Gaussian Properties {data-transition="None"}

* If
$$
\dataVector = \mappingMatrix \inputVector + \noiseVector,
$$
* Assume 
$$\begin{align}
\inputVector & \sim \gaussianSamp{\meanVector}{\covarianceMatrix}\\
\noiseVector & \sim \gaussianSamp{\zerosVector}{\covarianceMatrixTwo}
\end{align}$$
* Then
$$
\dataVector \sim \gaussianSamp{\mappingMatrix\meanVector}{\mappingMatrix\covarianceMatrix\mappingMatrix^\top + \covarianceMatrixTwo}.
$$
If $\covarianceMatrixTwo=\dataStd^2\eye$, this is Probabilistic Principal Component Analysis [@Tipping:probpca99], because we integrated out the inputs (or *latent* variables they would be called in that case). 

### Non linear on Inputs {data-transition="None"}

* Set each activation function computed at each data point to be
$$
\activationScalar_{i,j} = \activationScalar(\mappingVector^{(1)}_{j}, \inputVector_{i})
$$
Define  *design matrix* 
$$
\activationMatrix = 
\begin{bmatrix}
\activationScalar_{1, 1} & \activationScalar_{1, 2} & \dots & \activationScalar_{1, \numHidden} \\
\activationScalar_{1, 2} & \activationScalar_{1, 2} & \dots & \activationScalar_{1, \numData} \\
\vdots & \vdots & \ddots & \vdots \\
\activationScalar_{\numData, 1} & \activationScalar_{\numData, 2} & \dots & \activationScalar_{\numData, \numHidden}
\end{bmatrix}.
$$

### Matrix Representation of a Neural Network {data-transition="None"}

$$\mappingFunction\left(\inputVector\right) = \activationVector\left(\inputVector\right)^\top \mappingVector + \noiseScalar$$

. . .

$$\dataVector = \activationMatrix\mappingVector + \noiseVector$$

. . .

$$\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$$


### Prior Density {data-transition="None"}

* Define
$$
\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha\eye},
$$

* Rules of multivariate Gaussians to see that,
$$
\dataVector \sim \gaussianSamp{\zerosVector}{\alpha \activationMatrix \activationMatrix^\top + \dataStd^2 \eye}.
$$

$$
\kernelMatrix = \alpha \activationMatrix \activationMatrix^\top + \dataStd^2 \eye.
$$

### Joint Gaussian Density {data-transition="None"}

* Elements are a function $\kernel_{i,j} = \kernel\left(\inputVector_i, \inputVector_j\right)$

$$
\kernelMatrix = \alpha \activationMatrix \activationMatrix^\top + \dataStd^2 \eye.
$$

### Covariance Function {data-transition="None"}

$$
\kernel_\mappingFunction\left(\inputVector_i, \inputVector_j\right) = \alpha \activationVector\left(\mappingMatrix_1, \inputVector_i\right)^\top \activationVector\left(\mappingMatrix_1, \inputVector_j\right)
$$

* formed by inner products of the rows of the *design matrix*.  

### Gaussian Process {data-transition="None"}

* Instead of making assumptions about our density over each data point, $\dataScalar_i$ as i.i.d.

*  make a joint Gaussian assumption over our data.

* covariance matrix is now a function of both the parameters of the activation function, $\mappingMatrix_1$, and the input variables, $\inputMatrix$.

* Arises from integrating out $\mappingVector^{(2)}$. 

### Basis Functions {data-transition="None"}

* Can be very complex, such as deep kernels, [@Cho:deep09] or could even put a convolutional neural network inside.

* Viewing a neural network in this way is also what allows us to beform sensible *batch* normalizations [@Ioffe:batch15].

