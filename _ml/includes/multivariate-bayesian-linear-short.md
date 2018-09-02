\subsection{Multivariate Regression Likelihood}

* Noise corrupted data point
  $$\dataScalar_i = \weightVector^\top \inputVector_{i, :} + {\noiseScalar}_i$$

. . .

* Multivariate regression likelihood:
  $$p(\dataVector| \inputMatrix, \weightVector) = \frac{1}{\left(2\pi {\dataStd}^2\right)^{\numData/2}} \exp\left(-\frac{1}{2{\dataStd}^2}\sum_{i=1}^{\numData}\left(\dataScalar_i - \weightVector^\top \inputVector_{i, :}\right)^2\right)$$

. . .

* Now use a *multivariate* Gaussian prior:
  $$p(\weightVector) = \frac{1}{\left(2\pi \alpha\right)^\frac{\dataDim}{2}} \exp \left(-\frac{1}{2\alpha} \weightVector^\top \weightVector\right)$$

