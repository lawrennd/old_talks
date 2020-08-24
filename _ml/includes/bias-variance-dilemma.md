\ifndef{biasVarianceDilemma}
\define{biasVarianceDilemma}
\editme

\subsection{Bias Variance Decomposition}

\notes{The bias-variance decomposition considers the expected test error for different variations of the *training data* sampled from, $\Pr(\dataVector, \dataScalar)$}\slides{Generalisation error}
$$
\mathbb{E}\left[ \left(\dataScalar - \mappingFunction^*(\dataVector)\right)^2 \right].
$$
\notes{This can be decomposed into two parts,}\slides{Decompose as}
$$
\mathbb{E}\left[ \left(\dataScalar - \mappingFunction(\dataVector)\right)^2 \right] = \text{bias}\left[\mappingFunction^*(\dataVector)\right]^2 + \text{variance}\left[\mappingFunction^*(\dataVector)\right] +\sigma^2,
$$
\notes{where the bias is given by}\slides{

\newslide{Bias}

* Given by}
  $$
  \text{bias}\left[\mappingFunction^*(\dataVector)\right] =
\mathbb{E}\left[\mappingFunction^*(\dataVector)\right] * \mappingFunction(\dataVector)
$$
\notes{and it summarizes error that arises from the model's inability to represent the underlying complexity of the data. For example, if we were to model the marathon pace of the winning runner from the Olympics by computing the average pace across time, then that model would exhibit *bias* error because the reality of Olympic marathon pace is it is changing (typically getting faster).}

\slides{* Error due to bias comes from a model that's too simple.

\newslide{Variance}

* Given by}\notes{The variance term is given by}
  $$
  \text{variance}\left[\mappingFunction^*(\dataVector)\right] = \mathbb{E}\left[\left(\mappingFunction^*(\dataVector) - \mathbb{E}\left[\mappingFunction^*(\dataVector)\right]\right)^2\right].
  $$
\notes{The variance term is often described as arising from a model that is too complex, but we have to be careful with this idea. Is the model really too complex relative to the real world that generates the data? The real world is a complex place, and it is rare that we are constructing mathematical models that are more complex than the world around us. Rather, the 'too complex' refers to ability to estimate the parameters of the model given the data we have. Slight variations in the training set cause changes in prediction.}\slides{
* Slight variations in the training set cause changes in the prediction. Error due to variance is error in the model due to an overly complex model.}

\notes{Models that exhibit high variance are sometimes said to 'overfit' the data whereas models that exhibit high bias are sometimes described as 'underfitting' the data}.

\include{_ml/includes/bias-variance-plots.md}

\endif
