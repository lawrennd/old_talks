\ifndef{computeOutputExpectations}
\define{computeOutputExpectations}
\editme

\notes{
\subsection{Computing the Mean and Error Bars of the Functions}

These ideas together, now allow us to compute the mean and error bars of the predictions. The mean prediction, before corrupting by noise is given by,
$$
\mappingFunctionVector = \basisMatrix\mappingVector
$$
in matrix form. This gives you enough information to compute the predictive mean.

\codeassignment{Compute the predictive mean for the function at all
the values of the basis function given by `Phi_pred`. Call the vector of
predictions `\mappingFunction_pred_mean`. Plot the predictions alongside the data. We can also
compute what the training error was. Use the output from your model to compute
the predictive mean, and then compute the sum of squares error of that
predictive mean.
$$
E = \sum_{i=1}^\numData (\dataScalar_i - \langle \mappingFunction_i\rangle)^2
$$
where
$\langle \mappingFunction_i\rangle$ is the expected output of the model at point $\inputScalar_i$.}{2}{15}{# compute mean under posterior density
f_pred_mean = 

# plot the predictions

# compute mean at the training data and sum of squares error
f_mean = 
sum_squares = 
print('The error is: ', sum_squares)}

\subsection{Computing Error Bars}

Finally, we can compute error bars for the predictions. The error bars are the standard deviations of the predictions for $\mappingFunctionVector=\basisMatrix\mappingVector$ under the posterior density for $\mappingVector$. The standard deviations of these predictions can be found from the variance of the prediction at each point. Those variances are the diagonal entries of the covariance matrix. We've already computed the form of the covariance under Gaussian expectations, 
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \basisMatrix\covarianceMatrix \basisMatrix^\top
$$
which under the posterior density is given by
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector_w}{\covarianceMatrix_w}} = \basisMatrix\covarianceMatrix_w \basisMatrix^\top
$$

\codeassignment{The error bars are given by computing the standard
deviation of the predictions, $\mappingFunction$. For a given prediction $\mappingFunction_i$ the variance is
$\text{var}(\mappingFunction_i) = \langle \mappingFunction_i^2\rangle - \langle \mappingFunction_i \rangle^2$. This is given
by the diagonal element of the covariance of $\mappingFunctionVector$,
$$
\text{var}(\mappingFunction_i) =
\basisVector_{i, :}^\top \covarianceMatrix_w \basisVector_{i, :}
$$
where
$\basisVector_{i, :}$ is the basis vector associated with the input
location, $\inputVector_i$.

Plot the mean function and the error bars for your
basis.}{3}{20}{# Compute variance at function values
f_pred_var = 
f_pred_std = 

# plot the mean and error bars at 2 standard deviations above and below the mean}

\subsection{Validation}

Now we will test the generalisation ability of these models.  Firstly we are going to use hold out validation to attempt to see which model is best for extrapolating.

\codeassignment{Now split the data into training and *hold out* validation sets. Hold out the data for years after 1980. Compute the predictions for different model orders between 0 and 8. Find the model order which fits best according to *hold out* validation. Is it the same as the maximum likelihood result fom last week?}{4}{25}

\codeassignment{Now we will use leave one out cross validation to attempt to see which model is best at interpolating. Do you get the same result as for hold out validation? Compare plots of the hold out validation area for different degrees and the cross validation error for different degrees. Why are they so different? Select a suitable polynomial for characterising the differences in the predictions. Plot the mean function and the error bars for the full data set (to represent the leave one out solution) and the training data from the hold out experiment. Discuss your answer.}{5}{30}
}


\newslide{Computing the Expected Output}

\slides{
* Given the posterior for the parameters, how can we compute the expected output at a given location?
* Output of model at location $\inputVector_i$ is given by
  $$
  \mappingFunction(\inputVector_i; \mappingVector) = \basisVector_i^\top \mappingVector
  $$
* We want the expected output under the posterior density, $p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)$.
* Mean of mapping function will be given by 
  $$
  \begin{aligned} \left\langle f(\inputVector_i; \mappingVector)\right\rangle_{p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)} &= \basisVector_i^\top \left\langle\mappingVector\right\rangle_{p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)} \\  & = \basisVector_i^\top \meanVector_w \end{aligned}
  $$

\newslide{Variance of Expected Output}

* Variance of model at location $\inputVector_i$ is given by
  $$
  \begin{aligned}\text{var}(\mappingFunction(\inputVector_i; \mappingVector)) &= \left\langle(\mappingFunction(\inputVector_i; \mappingVector))^2\right\rangle - \left\langle \mappingFunction(\inputVector_i; \mappingVector)\right\rangle^2 \\&= \basisVector_i^\top\left\langle\mappingVector\mappingVector^\top\right\rangle \basisVector_i - \basisVector_i^\top \left\langle\mappingVector\right\rangle\left\langle\mappingVector\right\rangle^\top \basisVector_i \\&= \basisVector_i^\top \covarianceMatrix_i\basisVector_i
  \end{aligned}
  $$ 
  where all these expectations are taken under the posterior density, $p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)$.
}
\endif
