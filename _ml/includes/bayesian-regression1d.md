\include{_ml/includes/bayesian-regression1d-short.md}

\newslide{Main Trick}

$$p(c) = \frac{1}{\sqrt{2\pi\alpha_1}} \exp\left(-\frac{1}{2\alpha_1}c^2\right)$$
$$p(\dataVector|\inputVector, c, m, \dataStd^2) = \frac{1}{\left(2\pi\dataStd^2\right)^{\frac{\numData}{2}}} \exp\left(-\frac{1}{2\dataStd^2}\sum_{i=1}^\numData(\dataScalar_i - m\inputScalar_i - c)^2\right)$$

\newslide{}

$$p(c| \dataVector, \inputVector, m, \dataStd^2) = \frac{p(\dataVector|\inputVector, c, m, \dataStd^2)p(c)}{p(\dataVector|\inputVector, m, \dataStd^2)}$$

$$p(c| \dataVector, \inputVector, m, \dataStd^2) =  \frac{p(\dataVector|\inputVector, c, m, \dataStd^2)p(c)}{\int p(\dataVector|\inputVector, c, m, \dataStd^2)p(c) \text{d} c}$$

\newslide{}

$$p(c| \dataVector, \inputVector, m, \dataStd^2) \propto  p(\dataVector|\inputVector, c, m, \dataStd^2)p(c)$$

$$\begin{aligned}
    \log p(c | \dataVector, \inputVector, m, \dataStd^2) =&-\frac{1}{2\dataStd^2} \sum_{i=1}^\numData(\dataScalar_i-c - m\inputScalar_i)^2-\frac{1}{2\alpha_1} c^2 + \text{const}\\
     = &-\frac{1}{2\dataStd^2}\sum_{i=1}^\numData(\dataScalar_i-m\inputScalar_i)^2 -\left(\frac{\numData}{2\dataStd^2} + \frac{1}{2\alpha_1}\right)c^2\\
    & + c\frac{\sum_{i=1}^\numData(\dataScalar_i-m\inputScalar_i)}{\dataStd^2},
  \end{aligned}$$
  
\newslide{}

complete the square of the quadratic form to obtain
$$\log p(c | \dataVector, \inputVector, m, \dataStd^2) = -\frac{1}{2\tau^2}(c - \mu)^2 +\text{const},$$
where $\tau^2 = \left(\numData\dataStd^{-2} +\alpha_1^{-1}\right)^{-1}$
and
$\mu = \frac{\tau^2}{\dataStd^2} \sum_{i=1}^\numData(\dataScalar_i-m\inputScalar_i)$.
