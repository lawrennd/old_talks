\subsection{Overdetermined System}

\notes{The challenge with a linear model is that it has two unknowns, $m$, and $c$. Observing data allows us to write down a system of simultaneous linear equations. So, for example if we observe two data points, the first with the input value, $\inputScalar_1 = 1$ and the output value, $\dataScalar_1 =3$ and a second data point, $\inputScalar = 3$, $\dataScalar=1$, then we can write two simultaneous linear equations of the form. 

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$3 = m + c$$
point 2: $\inputScalar = 3$, $\dataScalar=1$
$$1 = 3m + c$$

The solution to these two simultaneous equations can be represented graphically as}

\notes{\includesvg{../slides/diagrams/ml/over_determined_system003.svg}}
\notes{\caption{The solution of two linear equations represented as the fit of a straight line through two data}}

\notes{
The challenge comes when a third data point is observed and it doesn't naturally fit on the straight line. 

point 3: $\inputScalar = 2$, $\dataScalar=2.5$
$$2.5 = 2m + c$$
}

\notes{\includesvg{../slides/diagrams/ml/over_determined_system004.svg}}
\notes{\caption{A third observation of data is inconsistent with the solution dictated by the first two observations}}

\notes{Now there are three candidate lines, each consistent with our data.}

\notes{\includesvg{../slides/diagrams/ml/over_determined_system007.svg}}
\notes{\caption{Three solutions to the problem, each consistent with two points of the three observations}}

\notes{This is known as an *overdetermined* system because there are more data than we need to determine our parameters. The problem arises because the model is a simplification of the real world, and the data we observe is therefore inconsistent with our model.}


\newslide{}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.over_determined_system(diagrams='../slides/diagrams/ml')}

\setupplotcode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('over_determined_system{samp:0>3}.svg',
                            directory='../slides/diagrams/ml', 
                            samp=IntSlider(1,1,7,1))}

\slides{
\startslides{over_determined_system}{1}{8}
\includesvg{../slides/diagrams/ml/over_determined_system001.svg}{}{over_determined_system}
\includesvg{../slides/diagrams/ml/over_determined_system002.svg}{}{over_determined_system}
\includesvg{../slides/diagrams/ml/over_determined_system003.svg}{}{over_determined_system}
\includesvg{../slides/diagrams/ml/over_determined_system004.svg}{}{over_determined_system}
\includesvg{../slides/diagrams/ml/over_determined_system005.svg}{}{over_determined_system}
\includesvg{../slides/diagrams/ml/over_determined_system006.svg}{}{over_determined_system}
\includesvg{../slides/diagrams/ml/over_determined_system007.svg}{}{over_determined_system}
}


\newslide{$\dataScalar = m\inputScalar + c$}
\slides{

. . . 

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$
3 = m + c
$$

. . .

point 2: $\inputScalar = 3$, $\dataScalar=1$
$$
1 = 3m + c
$$

. . . 

point 3: $\inputScalar = 2$, $\dataScalar=2.5$

$$2.5 = 2m + c$$}

\newslide{}

\notes{The solution was proposed by Pierre-Simon Laplace. His idea was to accept that the model was an incomplete representation of the real world, and the manner in which it was incomplete is *unknown*. His idea was that such unknowns could be dealt with through probability.}

\includeimg{../slides/diagrams/ml/Pierre-Simon_Laplace.png}{30%}{}{center}
\notes{\caption{Pierre Simon Laplace}

\include{_ai/includes/laplaces-determinism.md}

\notes{Laplace's concept was that the reason that the data doesn't match up to the model is because of unconsidered factors, and that these might be well represented through probability densities. He tackles the challenge of the unknown factors by adding a variable, $\noiseScalar$, that represents the unknown. In modern parlance we would call this a *latent* variable. But in the context Laplace uses it, the variable is so common that it has other names such as a "slack" variable or the *noise* in the system.

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$
3 = m + c + \noiseScalar_1
$$
point 2: $\inputScalar = 3$, $\dataScalar=1$
$$
1 = 3m + c + \noiseScalar_2
$$
point 3: $\inputScalar = 2$, $\dataScalar=2.5$
$$
2.5 = 2m + c + \noiseScalar_3
$$

Laplace's trick has converted the *overdetermined* system into an *underdetermined* system. He has now added three variables, $\{\noiseScalar_i\}_{i=1}^3$, which represent the unknown corruptions of the real world. Laplace's idea is that we should represent that unknown corruption with a *probability distribution*.}

\newslide{$\dataScalar = m\inputScalar + c + \noiseScalar$}
\slides{
. . . 

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$
3 = m + c + \noiseScalar_1
$$

. . .

point 2: $\inputScalar = 3$, $\dataScalar=1$
$$
1 = 3m + c + \noiseScalar_2
$$

. . . 

point 3: $\inputScalar = 2$, $\dataScalar=2.5$
$$
2.5 = 2m + c + \noiseScalar_3
$$
}

\subsection{A Probabilistic Process}
\slides{
. . .

Set the mean of Gaussian to be a function.
$$p
\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp \left(-\frac{\left(\dataScalar_i-\mappingFunction\left(\inputScalar_i\right)\right)^{2}}{2\dataStd^2}\right).
$$

. . .

This gives us a 'noisy function'.

. . .

This is known as a stochastic process.
}\notes{However, it was left to an admirer of Gauss to develop a practical probability density for that purpose. It was Carl Friederich Gauss who suggested that the *Gaussian* density (which at the time was unnamed!) should be used to represent this error.}

\notes{The result is a *noisy* function, a function which has a deterministic part, and a stochastic part. This type of function is sometimes known as a probabilistic or stochastic process, to distinguish it from a deterministic process.}

