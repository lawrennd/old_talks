\newslide{Maximum Likelihood in the Bernoulli}

\notes{### Maximum Likelihood in the Bernoulli Distribution

Maximum likelihood in the Bernoulli distribution is straightforward. Let's assume we have data, $\dataVector$ which consists of a vector of binary values of length $n$. If we assume each value was sampled independently from the Bernoulli distribution, conditioned on the parameter $\pi$ then our joint probability density has the form}\slides{
* Assume data, $\dataVector$ is binary vector length $\numData$. 
* Assume each value was sampled independently from the  Bernoulli distribution, given probability $\pi$}
$$
p(\dataVector|\pi) = \prod_{i=1}^{\numData} \pi^{\dataScalar_i} (1-\pi)^{1-\dataScalar_i}.
$$
\notes{As normal in maximum likelihood we consider the negative log likelihood as our objective,}\slides{

\newslide{Negative Log Likelihood}

* Minimize the negative log likelihood}
  $$\begin{align*}
  \errorFunction(\pi)& = -\log p(\dataVector|\pi)\\ 
                     & = -\sum_{i=1}^{\numData} \dataScalar_i \log \pi - \sum_{i=1}^{\numData} (1-\dataScalar_i) \log(1-\pi),
  \end{align*}$$
\slides{* Take gradient with respect to the parameter $\pi$.}\notes{
and we can derive the gradient with respect to the parameter $\pi$.}
  $$\frac{\text{d}\errorFunction(\pi)}{\text{d}\pi} = -\frac{\sum_{i=1}^{\numData} \dataScalar_i}{\pi}  + \frac{\sum_{i=1}^{\numData} (1-\dataScalar_i)}{1-\pi},$$

\newslide{Fixed Point}

\notes{and as normal we look for a stationary point for the log likelihood by setting this derivative to zero,}\slides{
* Stationary point: set derivative to zero}
  $$0 = -\frac{\sum_{i=1}^{\numData} \dataScalar_i}{\pi}  + \frac{\sum_{i=1}^{\numData} (1-\dataScalar_i)}{1-\pi},$$
\notes{rearranging we form}\slides{
* Rearrange to form}
  $$(1-\pi)\sum_{i=1}^{\numData} \dataScalar_i =   \pi\sum_{i=1}^{\numData} (1-\dataScalar_i),$$
\notes{which implies}\slides{
* Giving}
  $$\sum_{i=1}^{\numData} \dataScalar_i =   \pi\left(\sum_{i=1}^{\numData} (1-\dataScalar_i) + \sum_{i=1}^{\numData} \dataScalar_i\right),$$

\newslide{Solution}

\notes{and now we recognise that $\sum_{i=1}^{\numData} (1-\dataScalar_i) + \sum_{i=1}^{\numData} \dataScalar_i = \numData$ so we have}\slides{
* Recognise that $\sum_{i=1}^{\numData} (1-\dataScalar_i) + \sum_{i=1}^{\numData} \dataScalar_i = n$ so we have}
  $$\pi = \frac{\sum_{i=1}^{\numData} \dataScalar_i}{\numData}$$
\slides{
* Estimate the probability associated with the Bernoulli by setting it to the number of observed positives, divided by the total length of $\dataScalar$. 
* Makes intiutive sense. 
* What's your best guess of probability for coin toss is heads when you get 47 heads from 100 tosses?}

\notes{so in other words we estimate the probability associated with the Bernoulli by setting it to the number of observed positives, divided by the total length of $\dataScalar$. This makes intiutive sense. If I asked you to estimate the probability of a coin being heads, and you tossed the coin 100 times, and recovered 47 heads, then the estimate of the probability of heads should be $\frac{47}{100}$.}

\exercise{Show that the maximum likelihood solution we have found is a *minimum* for our objective.}

