\ifndef{linearRegressionMultivariateLogLikelihood}
\define{linearRegressionMultivariateLogLikelihood}

\editme

\subsection{Log Likelihood for Multivariate Regression}

\slides{
The likelihood of a single data point is

. . .

$$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}\right).$$

. . .

Leading to a log likelihood for the data set of

. . . 

$$L(\mappingVector,\dataStd^2)= -\frac{\numData}{2}\log \dataStd^2-\frac{\numData}{2}\log 2\pi -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}.$$
}

\newslide{Error Function}
\slides{
And a corresponding error function of
$$\errorFunction(\mappingVector,\dataStd^2)=\frac{\numData}{2}\log\dataStd^2 + \frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}.$$
}

\endif
