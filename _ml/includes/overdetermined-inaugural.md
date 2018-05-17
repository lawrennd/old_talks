\section{Overdetermined System}

\notes{The challenge with a linear model is that it has two unknowns, $m$, and $c$. Observing data allows us to write down a system of simultaneous linear equations. So, for example if we observe two data points, the first with the input value, $\inputScalar_1 = 1$ and the output value, $\dataScalar_1 =3$ and a second data point, $\inputScalar = 3$, $\dataScalar=1$, then we can write two simultaneous linear equations of the form. 

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$3 = m + c$$
point 2: $\inputScalar = 3$, $\dataScalar=1$
$$1 = 3m + c$$

The solution to these two simultaneous equations can be represented graphically as

\includesvg{../slides/diagrams/ml/over_determined_system003.svg}
\aligncenter{*The solution of two linear equations represented as the fit of a straight line through two data*}

The challenge comes when a third data point is observed and it doesn't naturally fit on the straight line. 

point 3: $\inputScalar = 2$, $\dataScalar=2.5$
$$2.5 = 2m + c$$


\includesvg{../slides/diagrams/ml/over_determined_system004.svg}
\aligncenter{*A third observation of data is inconsistent with the solution dictated by the first two observations*}

Now there are three candidate lines, each consistent with our data.

\includesvg{../slides/diagrams/ml/over_determined_system007.svg}
\aligncenter{*Three solutions to the problem, each consistent with two points of the three observations*}

This is known as an *overdetermined* system because there are more data than we need to determine our parameters. The problem arises because the model is a simplification of the real world, and the data we observe is therefore inconsistent with our model.}

\setupcode{import teaching_plots as plot}
\plotcode{plot.over_determined_system(diagrams='../slides/diagrams/ml')}

### 

\largetext{$$\dataScalar = m\inputScalar + c$$}

\displaycode{pods.notebook.display_plots('over_determined_system{samp:0>3}.svg', directory='../slides/diagrams/ml', samp=(1, 7))}

\slides{
### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system001.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system002.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system003.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system004.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system005.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system006.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system007.svg}
}

\slides{### $\dataScalar = m\inputScalar + c$ 
. . . 
\alignleft{point 1: $\inputScalar = 1$, $\dataScalar=3$}
$$3 = m + c$$
. . .
\alignleft{point 2: $\inputScalar = 3$, $\dataScalar=1$}
$$1 = 3m + c$$
. . . 
\alignleft{point 3: $\inputScalar = 2$, $\dataScalar=2.5$}

$$2.5 = 2m + c$$}

\slides{### }

\notes{The solution was proposed by Pierre-Simon Laplace. His idea was to accept that the model was an incomplete representation of the real world, and the manner in which it was incomplete is *unknown*. His idea was that such unknowns could be dealt with through probability.}

\includeimg{../slides/diagrams/ml/Pierre-Simon_Laplace.png}{30%}

\slides{### 

\includeimg{../slides/diagrams/laplacesDeterminismFrench.png}{80%}}

\notes{Famously, Laplace considered the idea of a deterministic Universe, one in which all the "". He speculates on an "intelligence" that can submit this vast data to analysis and propsoses that such an entity would be able to predict the future.

>Given for one instant an intelligence which could comprehend all the forces by which nature is animated and the respective situation of the beings who compose it---an intelligence sufficiently vast to submit these data to analysis---it woudl embrace in the same formulat the movements of the greatest bodies of the universe and those of the lightest atom; for it, nothing would be uncertain and the future, as the past, would be present in its eyes.}


\slides{### 

\includeimg{../slides/diagrams/laplacesDeterminismEnglish.png}{80%}}


\notes{Unfortunately, most analyses of his ideas stop at that point, whereas his real point is that such a notion is somewhat ridiculous. Just 3 pages later in the "Philosophical Essay on Probabilities", Laplace goes on to observe:

> The curve described by a simple molecule of air or vapor is regulated in a manner just as certain as the planetary orbits; the only difference between them is that which comes from our ignorance.
>
> Probability is relative, in part to this ignorance, in part to our knowledge.}

\slides{### 

\includeimg{../slides/diagrams/philosophicaless00lapliala.png}{80%}}

\notes{In other words, we can never utilize the idealistic deterministc Universe due to our ignorance about the world. }

\notes{Laplace's concept was that the reason that the data doesn't match up to the model is because of unconsidered factors, and that these might be well represented through probability densities. He tackles the challenge of the unknown factors by adding a variable, $\noiseScalar$, that represents the unknown. In modern parlance we would call this a *latent* variable. But in the context Laplace uses it, the variable is so common that it has other names such as a "slack" variable or the *noise* in the system.

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$3 = m + c + \noiseScalar_1$$
point 2: $\inputScalar = 3$, $\dataScalar=1$
$$1 = 3m + c + \noiseScalar_2$$
point 3: $\inputScalar = 2$, $\dataScalar=2.5$
$$2.5 = 2m + c + \noiseScalar_3$$

Laplace's trick has converted the *overdetermined* system into an *underdetermined* system. He has now added three variables, $\{\noiseScalar_i\}_{i=1}^3$, which represent the unknown corruptions of the real world. Laplace's idea is that we should represent that unknown corruption with a *probability distribution*.}

\slides{
### $\dataScalar = m\inputScalar + c + \noiseScalar$ 
. . . 
\alignleft{point 1: $\inputScalar = 1$, $\dataScalar=3$}
$$3 = m + c + \noiseScalar_1$$
. . .
\alignleft{point 2: $\inputScalar = 3$, $\dataScalar=1$}
$$1 = 3m + c + \noiseScalar_2$$
. . . 
\alignleft{point 3: $\inputScalar = 2$, $\dataScalar=2.5$}
$$2.5 = 2m + c + \noiseScalar_3$$
}

### A Probabilistic Process

\notes{However, it was left to an admirer of Gauss to develop a practical probability density for that purpose. It was Carl Friederich Gauss who suggested that the *Gaussian* density (which at the time was unnamed!) should be used to represent this error.}

\notes{The result is a *noisy* function, a function which has a deterministic part, and a stochastic part. This type of function is sometimes known as a probabilistic or stochastic process, to distinguish it from a deterministic process.}

\slides{. . .
\alignleft{Set the mean of Gaussian to be a function.}
$$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp \left(-\frac{\left(\dataScalar_i-\mappingFunction\left(\inputScalar_i\right)\right)^{2}}{2\dataStd^2}\right).$$
. . .
\alignleft{This gives us a 'noisy function'.}
. . .
\alignleft{This is known as a stochastic process.}
}
