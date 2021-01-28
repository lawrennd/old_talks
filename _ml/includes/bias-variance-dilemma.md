\ifndef{biasVarianceDilemma}
\define{biasVarianceDilemma}
\editme

\subsection{Bias Variance Decomposition}



\notes{One of Breiman's ideas for improving predictive performance is known
as bagging [@Breiman:bagging96]. The idea is to train a number of
models on the data such that they overfit (high variance). Then
average the predictions of these models. The models are trained on
different bootstrap samples [@Efron:bootstrap79] and their predictions
are aggregated giving us the acronym, Bagging. By combining decision
trees with bagging, we recover random forests [@Breiman-forests01].}

\notes{Bias and variance can also be estimated through Efron's
bootstrap [@Efron:bootstrap79], and the traditional view has been that
there's a form of Goldilocks effect, where the best predictions are
given by the model that is 'just right' for the amount of data
available. Not to simple, not too complex. The idea is that bias
decreases with increasing model complexity and variance increases with
increasing model complexity. Typically plots begin with the Mummy bear
on the left (too much bias) end with the Daddy bear on the right (too
much variance) and show a dip in the middle where the Baby bear (just)
right finds themselves.}

\notes{The Daddy bear is typically positioned at the point where the
model is able to exactly interpolate the data. For a generalized
linear model [@McCullagh:gen_linear89], this is the point at which the
number of parameters is equal to the number of data[^assuming].

[^assuming]: Assuming we are ignoring parameters in the link function and the distribution function.}

\notes{The bias-variance decomposition [@Geman:biasvariance92] considers the expected test error for different variations of the *training data* sampled from, $\mathbb{P}(\inputVector, \dataScalar)$}\slides{Generalisation error}
$$\begin{align*}
R(\mappingVector) = & \int \left(\dataScalar - \mappingFunction^*(\inputVector)\right)^2 \mathbb{P}(\dataScalar, \inputVector) \text{d}\dataScalar \text{d}\inputVector \\
& \triangleq & \mathbb{E}\left[ \left(\dataScalar - \mappingFunction^*(\inputVector)\right)^2 \right].
\end{align*}$$
\newslide{Decompose}

\notes{This can be decomposed into two parts,}\slides{Decompose as}
$$
\begin{align*}
\mathbb{E}\left[ \left(\dataScalar - \mappingFunction(\inputVector)\right)^2 \right] = & \text{bias}\left[\mappingFunction^*(\inputVector)\right]^2 \slides{\\
&} + \text{variance}\left[\mappingFunction^*(\inputVector)\right] \slides{\\} \slides{\\ &}+\sigma^2,
\end{align*}
$$
\notes{where the bias is given by}\slides{

\newslide{Bias}

* Given by}
  $$
  \text{bias}\left[\mappingFunction^*(\inputVector)\right] =
\mathbb{E}\left[\mappingFunction^*(\inputVector)\right] * \mappingFunction(\inputVector)
$$
\notes{and it summarizes error that arises from the model's inability to represent the underlying complexity of the data. For example, if we were to model the marathon pace of the winning runner from the Olympics by computing the average pace across time, then that model would exhibit *bias* error because the reality of Olympic marathon pace is it is changing (typically getting faster).}

\slides{* Error due to bias comes from a model that's too simple.

\newslide{Variance}

* Given by}\notes{The variance term is given by}
  $$
  \text{variance}\left[\mappingFunction^*(\inputVector)\right] = \mathbb{E}\left[\left(\mappingFunction^*(\inputVector) - \mathbb{E}\left[\mappingFunction^*(\inputVector)\right]\right)^2\right].
  $$
\notes{The variance term is often described as arising from a model that is too complex, but we have to be careful with this idea. Is the model really too complex relative to the real world that generates the data? The real world is a complex place, and it is rare that we are constructing mathematical models that are more complex than the world around us. Rather, the 'too complex' refers to ability to estimate the parameters of the model given the data we have. Slight variations in the training set cause changes in prediction.}\slides{
* Slight variations in the training set cause changes in the prediction. Error due to variance is error in the model due to an overly complex model.}

\notes{Models that exhibit high variance are sometimes said to 'overfit' the data whereas models that exhibit high bias are sometimes described as 'underfitting' the data.}

\include{_ml/includes/bias-variance-plots.md}

\endif
