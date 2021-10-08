\ifndef{overdeterminedMlphysical}
\define{overdeterminedMlphysical}
\editme

\include{_ml/includes/overdetermined-system.md}
\include{_ml/includes/overdetermined-laplace-intro.md}
\include{_physics/includes/laplaces-demon.md}
\include{_physics/includes/laplaces-gremlin.md}

\notes{Laplace's concept was that the reason that the data doesn't match up to the model is because of unconsidered factors, and that these might be well represented through probability densities. He tackles the challenge of the unknown factors by adding a variable, $\noiseScalar$, that represents the unknown. In modern parlance we would call this a *latent* variable. But in the context Laplace uses it, the variable is so common that it has other names such as a "slack" variable or the *noise* in the system.

point 1: $\inputScalar = 1$, $\dataScalar=3$
\[
3 = m + c + \noiseScalar_1
\]
point 2: $\inputScalar = 3$, $\dataScalar=1$
\[
1 = 3m + c + \noiseScalar_2
\]
point 3: $\inputScalar = 2$, $\dataScalar=2.5$
\[
2.5 = 2m + c + \noiseScalar_3
\]

Laplace's trick has converted the *overdetermined* system into an *underdetermined* system. He has now added three variables, $\{\noiseScalar_i\}_{i=1}^3$, which represent the unknown corruptions of the real world. Laplace's idea is that we should represent that unknown corruption with a *probability distribution*.}

\newslide{$\dataScalar = m\inputScalar + c + \noiseScalar$}
\slides{
. . . 

point 1: $\inputScalar = 1$, $\dataScalar=3$
\[
3 = m + c + \noiseScalar_1
\]

. . .

point 2: $\inputScalar = 3$, $\dataScalar=1$
\[
1 = 3m + c + \noiseScalar_2
\]

. . . 

point 3: $\inputScalar = 2$, $\dataScalar=2.5$
\[
2.5 = 2m + c + \noiseScalar_3
\]
}

\subsection{A Probabilistic Process}
\slides{
. . .

Set the mean of Gaussian to be a function.
$$
p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp \left(-\frac{\left(\dataScalar_i-\mappingFunction\left(\inputScalar_i\right)\right)^{2}}{2\dataStd^2}\right).
$$

. . .

This gives us a 'noisy function'.

. . .

This is known as a stochastic process.
}\notes{However, it was left to an admirer of Laplace to develop a practical probability density for that purpose. It was Carl Friedrich Gauss who suggested that the *Gaussian* density (which at the time was unnamed!) should be used to represent this error.}

\notes{The result is a *noisy* function, a function which has a deterministic part, and a stochastic part. This type of function is sometimes known as a probabilistic or stochastic process, to distinguish it from a deterministic process.}

\endif
