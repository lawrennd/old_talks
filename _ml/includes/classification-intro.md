\ifndef{classificationIntro}
\define{classificationIntro}
\editme

\subsection{Introduction to Classification}

\notes{Machine learning problems normally involve a prediction function and an objective function. So far in the course we've mainly focussed on the case where the prediction function was over the real numbers, so the codomain of the functions, $\mappingFunction(\inputMatrix)$ was the real numbers or sometimes real vectors. The classification problem consists of predicting whether or not a particular example is a member of a particular class. So we may want to know if a particular image represents a digit 6 or if a particular user will click on a given advert. These are classification problems, and they require us to map to *yes* or *no* answers. That makes them naturally discrete mappings.}

\slides{* We are given a  data set containing 'inputs', $\inputMatrix$ and 'targets', $\dataVector$.
* Each data point consists of an input vector $\inputVector_i$ and a class label, $\dataScalar_i$.
* For binary classification assume $\dataScalar_i$ should be either $1$ (yes) or $-1$ (no).
* Input vector can be thought of as features.}


\newslide{Discrete Probability}

\notes{In classification we are given an input vector, $\inputVector$, and an associated label, $\dataScalar$ which either takes the value $-1$ to represent *no* or $1$ to represent *yes*.}
\slides{* Algorithms based on *prediction* function and *objective* function.
* For regression the *codomain* of the functions, $f(\inputMatrix)$ was the real numbers or sometimes real vectors. 
* In classification we are given an input vector, $\inputVector$, and an associated label, $\dataScalar$ which either takes the value $-1$ or $1$.}


\endif
