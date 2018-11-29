\newslide{Bias Variance Decomposition}

Expected test error for different variations of
the *training data* sampled from, $\Pr(\dataVector, \dataScalar)$
$$\mathbb{E}\left[ \left(\dataScalar - \mappingFunction^*(\dataVector)\right)^2 \right]$$
Decompose as
$$\mathbb{E}\left[ \left(\dataScalar - \mappingFunction(\dataVector)\right)^2 \right] = \text{bias}\left[\mappingFunction^*(\dataVector)\right]^2 + \text{variance}\left[\mappingFunction^*(\dataVector)\right] +\sigma^2$$

\newslide{Bias}

* Given by
  $$\text{bias}\left[\mappingFunction^*(\dataVector)\right] =
\mathbb{E}\left[\mappingFunction^*(\dataVector)\right] * \mappingFunction(\dataVector)$$
* Error due to bias comes from a model that's too simple.

\newslide{Variance}

* Given by
  $$\text{variance}\left[\mappingFunction^*(\dataVector)\right] = \mathbb{E}\left[\left(\mappingFunction^*(\dataVector) - \mathbb{E}\left[\mappingFunction^*(\dataVector)\right]\right)^2\right]$$
* Slight variations in the training set cause changes in the prediction. Error due to variance is error in the model due to an overly complex model.

\include{_ml/includes/bias-variance-plots.md}
