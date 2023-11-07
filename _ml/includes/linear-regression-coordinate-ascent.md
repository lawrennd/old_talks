\ifndef{linearRegressionCoordinateAscent}
\define{linearRegressionCoordinateAscent}

\editme

\subsection{Coordinate Descent}

\notes{In the movie recommender system example, we minimised the objective function by steepest descent based gradient methods. Our updates required us to compute the gradient at the position we were located, then to update the gradient according to the direction of steepest descent. This time, we will take another approach. It is known as *coordinate descent*. In coordinate descent, we choose to move one parameter at a time. Ideally, we design an algorithm that at each step moves the parameter to its minimum value. At each step we choose to move the individual parameter to its minimum.}

\notes{To find the minimum, we look for the point in the curve where the gradient is zero. This can be found by taking the gradient of $\errorFunction(m,c)$ with respect to the parameter.}

\newslide{Learning is Optimization}
\slides{

* Learning is minimization of the cost function.
* At the minima the gradient is zero.
* Coordinate ascent, find gradient in each coordinate and set to zero.
  $$\frac{\text{d}\errorFunction(c)}{\text{d}c} = -2\sum_{i=1}^\numData \left(\dataScalar_i- m \inputScalar_i - c \right)$$
  $$0 = -2\sum_{i=1}^\numData\left(\dataScalar_i- m\inputScalar_i - c \right)$$}

\newslide{Learning is Optimization}
\slides{

* Fixed point equations
  $$0 = -2\sum_{i=1}^\numData \dataScalar_i +2\sum_{i=1}^\numData m \inputScalar_i +2n c$$
  $$c = \frac{\sum_{i=1}^\numData \left(\dataScalar_i - m\inputScalar_i\right)}{\numData}$$}

\notes{
\subsubsection{Update for Offset}

Let's consider the parameter $c$ first. The gradient goes nicely through the summation operator, and we obtain
$$
\frac{\text{d}\errorFunction(m,c)}{\text{d}c} = -\sum_{i=1}^\numData 2(\dataScalar_i-m\inputScalar_i-c).
$$
Now we want the point that is a minimum. A minimum is an example of a [*stationary point*](http://en.wikipedia.org/wiki/Stationary_point), the stationary points are those points of the function where the gradient is zero. They are found by solving the equation for $\frac{\text{d}\errorFunction(m,c)}{\text{d}c} = 0$. Substituting in to our gradient, we can obtain the following equation, 
$$
0 = -\sum_{i=1}^\numData 2(\dataScalar_i-m\inputScalar_i-c)
$$
which can be reorganised as follows,
$$
c^* = \frac{\sum_{i=1}^\numData(\dataScalar_i-m^*\inputScalar_i)}{\numData}.
$$
The fact that the stationary point is easily extracted in this manner implies that the solution is *unique*. There is only one stationary point for this system. Traditionally when trying to determine the type of stationary point we have encountered we now compute the *second derivative*,
$$
\frac{\text{d}^2\errorFunction(m,c)}{\text{d}c^2} = 2n.
$$
The second derivative is positive, which in turn implies that we have found a minimum of the function. This means that setting $c$ in this way will take us to the lowest point along that axes.}

\code{# set c to the minimum
c = (y - m*x).mean()
print(c)}


\newslide{Learning is Optimization}

\slides{
* Learning is minimization of the cost function.
* At the minima the gradient is zero.
* Coordinate ascent, find gradient in each coordinate and set to zero.
  $$\frac{\text{d}\errorFunction(m)}{\text{d}m} = -2\sum_{i=1}^\numData \inputScalar_i\left(\dataScalar_i- m \inputScalar_i - c \right)$$
  $$0 = -2\sum_{i=1}^\numData \inputScalar_i \left(\dataScalar_i-m \inputScalar_i - c \right)$$
}

\newslide{Learning is Optimization}
\slides{
* Fixed point equations
  $$0 = -2\sum_{i=1}^\numData \inputScalar_i\dataScalar_i+2\sum_{i=1}^\numData m \inputScalar_i^2+2\sum_{i=1}^\numData c\inputScalar_i$$
  $$m  =    \frac{\sum_{i=1}^\numData \left(\dataScalar_i -c\right)\inputScalar_i}{\sum_{i=1}^\numData\inputScalar_i^2}$$
}
\notes{
\subsection{Update for Slope}

Now we have the offset set to the minimum value, in coordinate descent, the next step is to optimise another parameter. Only one further parameter remains. That is the slope of the system.}

\notes{Now we can turn our attention to the slope. We once again peform the same set of computations to find the minima. We end up with an update equation of the following form.}

$$m^* = \frac{\sum_{i=1}^\numData (\dataScalar_i - c)\inputScalar_i}{\sum_{i=1}^\numData \inputScalar_i^2}$$

\notes{Communication of mathematics in data science is an essential skill, in a moment, you will be asked to rederive the equation above. Before we do that, however, we will briefly review how to write mathematics in the notebook.}

\notes{
\subsection{$\LaTeX$ for Maths}

These cells use [Markdown format](http://en.wikipedia.org/wiki/Markdown). You can include maths in your markdown using [$\LaTeX$ syntax](http://en.wikipedia.org/wiki/LaTeX), all you have to do is write your answer inside dollar signs, as follows:}

\notes{To write a fraction, we write `$\frac{a}{b}$`, and it will display like this $\frac{a}{b}$. To write a subscript we write `$a_b$` which will appear as $a_b$. To write a superscript (for example in a polynomial) we write `$a^b$` which will appear as $a^b$. There are lots of other macros as well, for example we can do greek letters such as `$\alpha, \beta, \gamma$` rendering as $\alpha, \beta, \gamma$. And we can do sum and intergral signs as `$\sum \int \int$`.}

\notes{You can combine many of these operations together for composing expressions.}

\writeassignment{Convert the following python code expressions into $\LaTeX$j, writing your answers below. In each case write your answer as a single equality (i.e. your maths should only contain one expression, not several lines of expressions). For the purposes of your $\LaTeX$ please assume that `x` and `w` are $n$ dimensional vectors.

```(a) f = x.sum()```

```(b) m = x.mean()```

```(c) g = (x*w).sum()```}{15}

\subsection{Fixed Point Updates}

\alignleft{Worked example.}
$$
\begin{aligned}
    c^{*}=&\frac{\sum
_{i=1}^{\numData}\left(\dataScalar_i-m^{*}\inputScalar_i\right)}{\numData},\\
    m^{*}=&\frac{\sum
_{i=1}^{\numData}\inputScalar_i\left(\dataScalar_i-c^{*}\right)}{\sum _{i=1}^{\numData}\inputScalar_i^{2}},\\
\left.\dataStd^2\right.^{*}=&\frac{\sum
_{i=1}^{\numData}\left(\dataScalar_i-m^{*}\inputScalar_i-c^{*}\right)^{2}}{\numData}
\end{aligned}
$$

\notes{
\subsection{Gradient With Respect to the Slope}

Now that you've had a little training in writing maths with $\LaTeX$, we will be able to use it to answer questions. The next thing we are going to do is a little differentiation practice.}

\writeassignment{Derive the the gradient of the objective function
with respect to the slope, $m$. Rearrange it to show that the update equation
written above does find the stationary points of the objective function. By
computing its derivative show that it's a minimum.}{20}

\code{m = ((y - c)*x).sum()/(x**2).sum()
print(m)}

\notes{We can have a look at how good our fit is by computing the prediction across the input space. First create a vector of 'test points',}

\setupcode{import numpy as np}
\code{x_test = np.linspace(1890, 2020, 130)[:, None]}

\notes{Now use this vector to compute some test predictions,}

\code{f_test = m*x_test + c}

\notes{Now plot those test predictions with a blue line on the same plot as the data,}

\setupcode{import matplotlib.pyplot as plt}
\code{plt.plot(x_test, f_test, 'b-')
plt.plot(x, y, 'rx')}

\notes{The fit isn't very good, we need to iterate between these parameter updates in a loop to improve the fit, we have to do this several times,}

\code{for i in np.arange(10):
    m = ((y - c)*x).sum()/(x*x).sum()
    c = (y-m*x).sum()/y.shape[0]
print(m)
print(c)}

\notes{And let's try plotting the result again}

\code{f_test = m*x_test + c
plt.plot(x_test, f_test, 'b-')
plt.plot(x, y, 'rx')}

\notes{Clearly we need more iterations than 10! In the next question you will add more iterations and report on the error as optimisation proceeds.}

\codeassignment{There is a problem here, we seem to need many interations to get to a good solution. Let's explore what's going on. Write code which alternates between updates of `c` and `m`. Include the following features in your code.

1. Initialise with `m=-0.4` and `c=80`.
2. Every 10 iterations
compute the value of the objective function for the training data and print it
to the screen (you'll find hints on this in [the lab from last
week](./week2.ipynb)).
3. Cause the code to stop running when the error change
over less than 10 iterations is smaller than $1\times10^{-4}$. This is known as
a stopping criterion.

Why do we need so many iterations to get to the solution?}{}{25}

\endif
