\ifndef{sumOfSquaresLogLikelihood}
\define{sumOfSquaresLogLikelihood}

\editme

\section{Sum of Squares Error}
\slides{
* Ignoring terms which don’t depend on $m$ and $c$ gives
  $$\errorFunction(m, c) \propto \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputScalar_i))^2$$
  where $\mappingFunction(\inputScalar_i) = m\inputScalar_i + c$.
* This is known as the *sum of squares* error function.
* Commonly used and is closely associated with the Gaussian likelihood.
}
\newslide{Reminder}
\slides{
* Two functions involved:
    * *Prediction function*: $\mappingFunction(\inputScalar_i)$
    * Error, or *Objective function*: $\errorFunction(m, c)$
* Error function depends on parameters through prediction function.
}
\newslide{Mathematical Interpretation}
\slides{
* What is the mathematical interpretation?
* There is a cost function.
    * It expresses mismatch between your prediction and reality.
      $$
      \errorFunction(m, c)=\sum_{i=1}^\numData \left(\dataScalar_i - m\inputScalar_i-c\right)^2
	  $$
    * This is known as the sum of squares error.
}
\subsection{Legendre}

\notes{Minimizing the sum of squares error was first proposed by [Legendre](http://en.wikipedia.org/wiki/Adrien-Marie_Legendre) in 1805 [@Legendre:nouvelles05]. His book, which was on the orbit of comets, is available on google books, we can take a look at the relevant page by calling the code below.

\figure{\includegooglebook{spcAAAAAMAAJ}{PA72}}{Legendre's book was on the determination of orbits of comets. This page describes the formulation of least squares}{legendre-least-squares}

Of course, the main text is in French, but the key part we are interested in can be roughly translated as

>In most matters where we take measures data through observation, the most accurate results they can offer, it is almost always leads to a system of equations of the form 
>$$E = a + bx + cy + fz + etc .$$
>where $a$, $b$, $c$, $f$ etc are the known coefficients and $x$, $y$, $z$ etc are unknown and must be determined by the condition that the value of E is reduced, for each equation, to an amount or zero or very small.

He continues

>Of all the principles that we can offer for this item, I think it is not broader, more accurate, nor easier than the one we have used in previous research application, and that is to make the minimum sum of the squares of the errors. By this means, it is between the errors a kind of balance that prevents extreme to prevail, is very specific to make known the state of the closest to the truth system. The sum of the squares of the errors $E^2 + \left.E^\prime\right.^2 + \left.E^{\prime\prime}\right.^2 + etc$ being
>\begin{align*}   &(a + bx + cy + fz + etc)^2 \\
>+ &(a^\prime +
>b^\prime x + c^\prime y + f^\prime z + etc ) ^2\\
>+ &(a^{\prime\prime} +
>b^{\prime\prime}x  + c^{\prime\prime}y +  f^{\prime\prime}z + etc )^2 \\
>+ & etc
>\end{align*}
>if we wanted a minimum, by varying x alone, we will have the equation ...}

\notes{This is the earliest know printed version of the problem of least squares. The notation, however, is a little awkward for mordern eyes. In particular Legendre doesn't make use of the sum sign,
$$
\sum_{i=1}^3 z_i = z_1 + z_2 + z_3
$$
nor does he make use of the inner product.}

\notes{In our notation, if we were to do linear regression, we would need to subsititue:
$$\begin{align*}
a &\leftarrow \dataScalar_1-c, \\ a^\prime &\leftarrow \dataScalar_2-c,\\ a^{\prime\prime} &\leftarrow
\dataScalar_3 -c,\\ 
\text{etc.} 
\end{align*}$$
to introduce the data observations $\{\dataScalar_i\}_{i=1}^{\numData}$ alongside $c$, the offset. We would then introduce the input locations
$$\begin{align*}
b & \leftarrow \inputScalar_1,\\
b^\prime & \leftarrow \inputScalar_2,\\
b^{\prime\prime} & \leftarrow \inputScalar_3\\
\text{etc.}
\end{align*}$$
and finally the gradient of the function
$$x \leftarrow -m.$$
The remaining coefficients ($c$ and $f$) would then be zero. That would give us 
$$\begin{align*}   &(\dataScalar_1 -
(m\inputScalar_1+c))^2 \\ + &(\dataScalar_2 -(m\inputScalar_2 + c))^2\\ + &(\dataScalar_3 -(m\inputScalar_3 + c))^2 \\ + & \text{etc.}
\end{align*}$$
which we would write in the modern notation for sums as
$$
\sum_{i=1}^\numData (\dataScalar_i-(m\inputScalar_i + c))^2
$$
which is recognised as the sum of squares error for a linear regression.}

\notes{This shows the advantage of modern [summation operator](http://en.wikipedia.org/wiki/Summation), $\sum$,  in keeping our mathematical notation compact. Whilst it may look more complicated the first time you see it, understanding the mathematical rules that go around it, allows us to go much further with the notation.}

\notes{Inner products (or [dot products](http://en.wikipedia.org/wiki/Dot_product)) are similar. They allow us to write
$$
\sum_{i=1}^q u_i v_i
$$
in a more compact notation, $\mathbf{u}\cdot\mathbf{v}.$}

\notes{Here we are using bold face to represent vectors, and we assume that the individual elements of a vector $\mathbf{z}$ are given as a series of scalars
$$
\mathbf{z} = \begin{bmatrix} z_1\\ z_2\\ \vdots\\ z_\numData
\end{bmatrix}
$$
which are each indexed by their position in the vector.}

\endif
