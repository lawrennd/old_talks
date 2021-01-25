\ifndef{linearAlgebraRegression}
\define{linearAlgebraRegression}

\editme

\subsection{Regression: Linear Releationship}

\notes{For many their first encounter with what might be termed a machine learning method is fitting a straight line. A straight line is characterized by two parameters, the scale, $m$, and the offset $c$.}

$$\dataScalar_i = m \inputScalar_i + c$$

\slides{* $\dataScalar_i$ : winning
pace.

* $\inputScalar_i$ : year of Olympics.

* $m$ : rate of improvement over time.

* $c$ : winning time at year 0.}

\notes{For the olympic marathon example $\dataScalar_i$ is the winning pace and it is given as a function of the year which is represented by $\inputScalar_i$. There are two further parameters of the prediction function. For the olympics example we can interpret these parameters, the scale $m$ is the rate of improvement of the olympic marathon pace on a yearly basis. And $c$ is the winning pace as estimated at year 0.}

\include{_ml/includes/overdetermined-inaugural.md}
\include{_ml/includes/univariate-gaussian.md}
\include{_ml/includes/univariate-gaussian-properties.md}
\include{_ml/includes/linear-regression-log-likelihood.md}
\include{_ml/includes/sum-of-squares-log-likelihood.md}
\include{_ml/includes/olympic-marathon-linear-regression.md}
\include{_ml/includes/linear-regression-coordinate-ascent.md}

\subsection{Important Concepts Not Covered}

* Other optimization methods:
    * Second order methods, conjugate gradient, quasi-Newton and Newton.
* Effective heuristics such as momentum.
* Local vs global solutions.

\addreading{@Rogers:book11}{For fitting linear models: Section 1.1-1.2}
\addreading{@Bishop:book06}{Section 1.2.5 up to equation 1.65}

\newslide{Multi-dimensional Inputs}
\slides{
* Multivariate functions involve more than one input.
* Height might be a function of weight and gender.
* There could be other contributory factors.
* Place these factors in a feature vector $\inputVector_i$.
* Linear function is now defined as
  $$\mappingFunction(\inputVector_i) = \sum_{j=1}^p w_j \inputScalar_{i, j} + c$$
}

\newslide{Vector Notation}
\slides{

* Write in vector notation,
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \inputVector_i + c$$
* Can absorb $c$ into $\mappingVector$ by assuming extra input $\inputScalar_0$ which is always 1.
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \inputVector_i$$
}

\include{_ml/includes/linear-regression-iterative.md}
\include{_ml/includes/linear-regression-multivariate-log-likelihood.md}
\include{_ml/includes/linear-regression-direct-solution.md}
\writeassignment{The prediction for our movie recommender system had the form
$$
f_{i,j} = \mathbf{u}_i^\top \mathbf{v}_j
$$
and the objective
function was then
$$
E = \sum_{i,j} s_{i,j}(\dataScalar_{i,j} - f_{i, j})^2
$$
Try writing this down in matrix and vector form. How many of the terms can you do? For each variable and parameter carefully think about whether it should be represented as a matrix or vector. Do as many of the terms as you can. Use $\LaTeX$ to give your answers and give the *dimensions* of any matrices you create.}{20}

\include{_ml/includes/linear-regression-objective-optimisation.md}
\include{_ml/includes/movie-body-count-linear-regression.md}

\notes{
\figure{\includeyoutube{ui-uNlFHoms}{600}{450}}{MLAI Lecture 15 from 2014 on Multivariate Regression.}{mlai-15-multivariate-regression}

\figure{\includeyoutube{78YNphT90-k}{600}{450}}{MLAI Lecture 3 from 2012 on Maximum Likelihood}{mlai-3-maximum-likelihood}
}

\include{_ml/includes/qr-decomposition-regression.md}

\addreading{@Rogers:book11}{Section 1.3 for Matrix & Vector Review}

\endif
