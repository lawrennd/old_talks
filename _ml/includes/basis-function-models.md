### Basis Function Models

* The *prediction function* is now defined as 
  $$\mappingFunction(\inputVector_i) = \sum_{j=1}^\numBasisFunc \mappingScalar_j \basisFunc_{i, j}$$

### Vector Notation

* Write in vector notation,
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \basisFuncVector_i$$

### Log Likelihood for Basis Function Model

* The likelihood of a single data point is
  $$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp
\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\basisFuncVector_i\right)^{2}}{2\dataStd^2}\right).$$

### Log Likelihood for Basis Function Model

* Leading to a log likelihood for
the data set of
  $$L(\mappingVector,\dataStd^2)= -\frac{\numData}{2}\log \dataStd^2-\frac{\numData}{2}\log 2\pi -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisFuncVector_i\right)^{2}}{2\dataStd^2}.$$

### Objective Function

* And a corresponding *objective function* of the form
$$E(\mappingVector,\dataStd^2)= \frac{\numData}{2}\log
          \dataStd^2 + \frac{\sum
_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisFuncVector_i\right)^{2}}{2\dataStd^2}.$$

### Expand the Brackets

$$\begin{align}
  E(\mappingVector,\dataStd^2) =
&\frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i\mappingVector^{\top}\basisFuncVector_i\\ &+\frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\mappingVector^{\top}\basisFuncVector_i\basisFuncVector_i^{\top}\mappingVector+\text{const}.\end{align}$$

### Expand the Brackets

$$\begin{align} E(\mappingVector, \dataStd^2) = & \frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2} \mappingVector^\top\sum_{i=1}^{\numData}\basisFuncVector_i \dataScalar_i\\ & +\frac{1}{2\dataStd^2}\mappingVector^{\top}\left[\sum_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^{\top}\right]\mappingVector+\text{const}.\end{align}$$

### Multivariate Derivatives Reminder

* We will need some multivariate calculus.
  $$\frac{\text{d}\mathbf{a}^{\top}\mappingVector}{\text{d}\mappingVector}=\mathbf{a}$$
  and
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
  or if $\mathbf{A}$ is symmetric (*i.e.* $\mathbf{A}=\mathbf{A}^{\top}$)
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$

### Differentiate

Differentiating with respect to the vector $\mappingVector$ we
obtain
$$\frac{\text{d} E\left(\mappingVector,\dataStd^2 \right)}{\text{d}
\mappingVector}=-\frac{1}{\dataStd^2} \sum
_{i=1}^{\numData}\basisFuncVector_i\dataScalar_i+\frac{1}{\dataStd^2} \left[\sum
_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^{\top}\right]\mappingVector$$
Leading to
$$\mappingVector^{*}=\left[\sum
_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^{\top}\right]^{-1}\sum
_{i=1}^{\numData}\basisFuncVector_i\dataScalar_i,$$

### Matrix Notation

Rewrite in matrix notation:
$$\sum
_{i=1}^{\numData}\basisFuncVector_i\basisFuncVector_i^\top = \basisFuncVector^\top
\basisFuncVector$$
$$\sum _{i=1}^{\numData}\basisFuncVector_i\dataScalar_i =
\basisFuncVector^\top \dataVector$$

### Update Equations

* Update for $\mappingVector^{*}$.
  $$\mappingVector^{*} = \left(\basisFuncVector^\top \basisFuncVector\right)^{-1} \basisFuncVector^\top \dataVector$$

* The equation for $\left.\dataStd^2\right.^{*}$ may also be found
  $$\left.\dataStd^2\right.^{{*}}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\basisFuncVector_i\right)^{2}}{\numData}.$$

### Avoid Direct Inverse

* E.g. Solve for $\mappingVector$
  $$\left(\basisFuncVector^\top \basisFuncVector\right)\mappingVector = \basisFuncVector^\top \dataVector$$
  
* See `np.linalg.solve`

* In practice use $\mathbf{Q}\mathbf{R}$ decomposition (see lab class notes).

### Polynomial Fits to Olympic Data

\setupcode{import numpy as np
from matplotlib import pyplot as plt
import teaching_plots as plot
import mlai
import pods}

\code{basis = mlai.polynomial

data = pods.datasets.olympic_marathon_men()

x = data['X']
y = data['Y']

xlim = [1892, 2020]
max_basis = 27

ll = np.array([np.nan]*(max_basis))
sum_squares = np.array([np.nan]*(max_basis))}

\plotcode{plot.rmse_fit(x, y, param_name='num_basis', param_range=(1, 28), 
              model=mlai.LM, basis=mlai.polynomial, data_limits=xlim, 
              xlim=xlim, objective_ylim=[0, 0.8],
              diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_LM_polynomial_num_basis{num_basis:0>3}.svg',
                            directory='../slides/diagrams/ml', 
                            num_basis=IntSlider(1,1,28,1))}

