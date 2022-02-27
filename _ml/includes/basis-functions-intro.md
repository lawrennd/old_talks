\ifndef{basisFunctionsIntro}
\define{basisFunctionsIntro}
\editme

\subsection{Basis Functions}

\notes{Here's the idea, instead of working directly on the original input space, $\inputVector$, we build models in a new space, $\basisVector(\inputVector)$ where $\basisVector(\cdot)$ is a *vector-valued* function that is defined on the space $\inputVector$.}

\subsection{Quadratic Basis}
\slides{
* Basis functions can be global. E.g. quadratic basis:
  $$
  \basisVector = [1, \inputScalar, \inputScalar^2]
  $$
}

\notes{Remember, that a *vector-valued function* is just a vector that contains functions instead of values. Here's an example for a one dimensional input space, $x$, being projected to a *quadratic* basis. First we consider each basis function in turn, we can think of the elements of our vector as being indexed so that we have}
$$
\begin{align*}
\basisFunc_1(\inputScalar) & = 1, \\
\basisFunc_2(\inputScalar) & = \inputScalar, \\
\basisFunc_3(\inputScalar) & = \inputScalar^2.
\end{align*}
$$
\notes{Now we can consider them together by placing them in a vector,}
$$
\basisVector(\inputScalar) = \begin{bmatrix} 1\\ \inputScalar \\ \inputScalar^2\end{bmatrix}.
$$
\notes{For the vector-valued function, we have simply collected the different functions together in the same vector making them notationally easier to deal with in our mathematics.}

\newslide{Matrix Valued Function}

\notes{When we consider the vector-valued function for each data point, then we place all the data into a matrix. The result is a matrix valued function,}
$$
\basisMatrix(\inputVector) = 
\begin{bmatrix} 1 & \inputScalar_1 &
\inputScalar_1^2 \\
1 & \inputScalar_2 & \inputScalar_2^2\\
\vdots & \vdots & \vdots \\
1 & \inputScalar_\numData & \inputScalar_\numData^2
\end{bmatrix}
$$
\notes{where we are still in the one dimensional input setting so $\inputVector$ here represents a vector of our inputs with $\numData$ elements.}

talk-macros.gpp}l/includes/quadratic-basis.md}

\endif
