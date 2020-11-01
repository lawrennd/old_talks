\ifndef{gpCovarianceFunctionImportance}
\define{gpCovarianceFunctionImportance}

\editme



\subsection{The Importance of the Covariance Function}

\notes{The covariance function encapsulates our assumptions about the data. The equations for the distribution of the prediction function, given the training observations, are highly sensitive to the covariation between the test locations and the training locations as expressed by the matrix $\kernelMatrix_*$. We defined a matrix $\mathbf{A}$ which allowed us to express our conditional mean in the form,}
$$
\meanVector_\mappingFunction = \mathbf{A}^\top \dataVector,
$$
\notes{where $\dataVector$ were our *training observations*. In other words our mean predictions are always a linear weighted combination of our *training data*. The weights are given by computing the covariation between the training and the test data ($\kernelMatrix_*$) and scaling it by the inverse covariance of the training data observations, $\left[\kernelMatrix + \dataStd^2 \eye\right]^{-1}$. This inverse is the main computational object that needs to be resolved for a Gaussian process. It has a computational burden which is $O(\numData^3)$ and a storage burden which is $O(\numData^2)$.  This makes working with Gaussian processes computationally intensive for the situation where $\numData>10,000$.}

\includeyoutube{ewJ3AxKclOg}

\endif
