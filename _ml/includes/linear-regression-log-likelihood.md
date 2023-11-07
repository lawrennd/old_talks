\ifndef{linearRegressionLogLikelihood}
\define{linearRegressionLogLikleihood}

\editme

\subsection{Laplace's Idea}

\newslide{A Probabilistic Process}

\slides{Set the mean of Gaussian to be a function.

. . .

}\notes{Laplace had the idea to augment the observations by noise, that is equivalent to considering a probability density whose mean is given by the *prediction function*}
  $$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-f\left(\inputScalar_i\right)\right)^{2}}{2\dataStd^2}\right).$$
\slides{
. . .

This gives us a 'noisy function'.

. . .

This is known as a stochastic process.}
\notes{This is known as *stochastic process*. It is a function that is corrupted by noise. Laplace didn't suggest the Gaussian density for that purpose, that was an innovation from Carl Friederich Gauss, which is what gives the Gaussian density its name.}

\subsection{Height as a Function of Weight}

In the standard Gaussian, parameterized by mean and variance, make the mean a linear function of an *input*.

This leads to a regression model. 
$$
\begin{align*}
  \dataScalar_i=&\mappingFunction\left(\inputScalar_i\right)+\noiseScalar_i,\\
         \noiseScalar_i \sim & \gaussianSamp{0}{\dataStd^2}.
  \end{align*}
$$

Assume $\dataScalar_i$ is height and $\inputScalar_i$ is weight.

\newslide{Data Point Likelihood}
\slides{
Likelihood of an individual data point
$$
p\left(\dataScalar_i|\inputScalar_i,m,c\right)=\frac{1}{\sqrt{2\pi \dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\dataStd^2}\right).
$$
Parameters are gradient, $m$, offset, $c$ of the function and noise variance $\dataStd^2$.
}

\newslide{Data Set Likelihood}

\slides{
If the noise, $\epsilon_i$ is sampled independently for each data point.
Each data point is independent (given $m$ and $c$).
For *independent* variables:
$$
p(\dataVector) = \prod_{i=1}^\numData p(\dataScalar_i)
$$
$$
p(\dataVector|\inputVector, m, c) = \prod_{i=1}^\numData p(\dataScalar_i|\inputScalar_i, m, c)
$$
}

\newslide{For Gaussian}
\slides{
i.i.d. assumption
$$
p(\dataVector|\inputVector, m, c) = \prod_{i=1}^\numData \frac{1}{\sqrt{2\pi \dataStd^2}}\exp \left(-\frac{\left(\dataScalar_i- m\inputScalar_i-c\right)^{2}}{2\dataStd^2}\right).
$$
$$
p(\dataVector|\inputVector, m, c) = \frac{1}{\left(2\pi \dataStd^2\right)^{\frac{\numData}{2}}}\exp\left(-\frac{\sum_{i=1}^\numData\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\dataStd^2}\right).
$$
}

\newslide{Log Likelihood Function}
\slides{
* Normally work with the log likelihood:
$$
L(m,c,\dataStd^{2})=-\frac{\numData}{2}\log 2\pi -\frac{\numData}{2}\log \dataStd^2 -\sum_{i=1}^{\numData}\frac{\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\dataStd^2}.
$$
}

\newslide{Consistency of Maximum Likelihood}
\slides{
* If data was really generated according to probability we specified.
* Correct parameters will be recovered in limit as $\numData \rightarrow \infty$.
* This can be proven through sample based approximations (law of large numbers) of "KL divergences".
* Mainstay of classical statistics [@Wasserman:all03].
}

\newslide{Probabilistic Interpretation of the Error Function}
\slides{
* Probabilistic Interpretation for Error Function is Negative Log Likelihood.
* *Minimizing* error function is equivalent to *maximizing* log likelihood.
* Maximizing *log likelihood* is equivalent to maximizing the *likelihood* because $\log$ is monotonic.
* Probabilistic interpretation: Minimizing error function is equivalent to maximum likelihood with respect to parameters.
}

\newslide{Error Function}
\slides{
* Negative log likelihood is the error function leading to an error function 
  $$\errorFunction(m,c,\dataStd^{2})=\frac{\numData}{2}\log \dataStd^2+\frac{1}{2\dataStd^2}\sum _{i=1}^{\numData}\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}.$$
* Learning proceeds by minimizing this error function for the data set provided.
}

\endif
