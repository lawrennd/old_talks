### Regression: Linear Releationship

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

\section{Laplace's Idea}

### A Probabilistic Process

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

### Height as a Function of Weight

In the standard Gaussian, parametized by mean and variance.

Make the mean a linear function of an *input*.

This leads to a regression model. 
$$
\begin{align*}
  \dataScalar_i=&\mappingFunction\left(\inputScalar_i\right)+\noiseScalar_i,\\
         \noiseScalar_i \sim & \gaussianSamp{0}{\dataStd^2}.
  \end{align*}
$$

Assume $\dataScalar_i$ is height and $\inputScalar_i$ is weight.

\slides{
### Data Point Likelihood
}
Likelihood of an individual data point
$$
p\left(\dataScalar_i|\inputScalar_i,m,c\right)=\frac{1}{\sqrt{2\pi \dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\dataStd^2}\right).
$$
Parameters are gradient, $m$, offset, $c$ of the function and noise variance $\dataStd^2$.

### Data Set Likelihood

If the noise, $\epsilon_i$ is sampled independently for each data point.
Each data point is independent (given $m$ and $c$).
For *independent* variables:
$$
p(\dataVector) = \prod_{i=1}^\numData p(\dataScalar_i)
$$
$$
p(\dataVector|\inputVector, m, c) = \prod_{i=1}^\numData p(\dataScalar_i|\inputScalar_i, m, c)
$$

### For Gaussian 

i.i.d. assumption
$$
p(\dataVector|\inputVector, m, c) = \prod_{i=1}^\numData \frac{1}{\sqrt{2\pi \dataStd^2}}\exp \left(-\frac{\left(\dataScalar_i- m\inputScalar_i-c\right)^{2}}{2\dataStd^2}\right).
$$
$$
p(\dataVector|\inputVector, m, c) = \frac{1}{\left(2\pi \dataStd^2\right)^{\frac{\numData}{2}}}\exp\left(-\frac{\sum_{i=1}^\numData\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\dataStd^2}\right).
$$

### Log Likelihood Function

* Normally work with the log likelihood:
$$
L(m,c,\dataStd^{2})=-\frac{\numData}{2}\log 2\pi -\frac{\numData}{2}\log \dataStd^2 -\sum_{i=1}^{\numData}\frac{\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\dataStd^2}.
$$

### Consistency of Maximum Likelihood

* If data was really generated according to probability we specified.
* Correct parameters will be recovered in limit as $\numData \rightarrow \infty$.
* This can be proven through sample based approximations (law of large numbers) of "KL divergences".
* Mainstay of classical statistics.

### Probabilistic Interpretation of the Error Function

* Probabilistic Interpretation for Error Function is Negative Log Likelihood.
* *Minimizing* error function is equivalent to *maximizing* log likelihood.
* Maximizing *log likelihood* is equivalent to maximizing the *likelihood* because $\log$ is monotonic.
* Probabilistic interpretation: Minimizing error function is equivalent to maximum likelihood with respect to parameters.

### Error Function

* Negative log likelihood is the error function leading to an error function 
  $$\errorFunction(m,c,\dataStd^{2})=\frac{\numData}{2}\log \dataStd^2+\frac{1}{2\dataStd^2}\sum _{i=1}^{\numData}\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}.$$
* Learning proceeds by minimizing this error function for the data set provided.

### Connection: Sum of Squares Error

* Ignoring terms which don’t depend on $m$ and $c$ gives
  $$\errorFunction(m, c) \propto \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputScalar_i))^2$$
  where $\mappingFunction(\inputScalar_i) = m\inputScalar_i + c$.
* This is known as the *sum of squares* error function.
* Commonly used and is closely associated with the Gaussian likelihood.

### Reminder

* Two functions involved:
    * *Prediction function*: $\mappingFunction(\inputScalar_i)$
    * Error, or *Objective function*: $\errorFunction(m, c)$
* Error function depends on parameters through prediction function.

### Mathematical Interpretation

* What is the mathematical interpretation?
* There is a cost function.
    * It expresses mismatch between your prediction and reality.
      $$
      \errorFunction(m, c)=\sum_{i=1}^\numData \left(\dataScalar_i - m\inputScalar_i-c\right)^2
	  $$
    * This is known as the sum of squares error.

\section{Sum of Squares Error}

\notes{Minimizing the sum of squares error was first proposed by [Legendre](http://en.wikipedia.org/wiki/Adrien-Marie_Legendre) in 1805. His book, which was on the orbit of comets, is available on google books, we can take a look at the relevant page by calling the code below.

\includegooglebook{spcAAAAAMAAJ}{PA72}

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
\sum_{i=1}^3 z_i = z_1
+ z_2 + z_3
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
(m\inputScalar_1+c))^2 \\
+ &(\dataScalar_2 -(m\inputScalar_2 + c))^2\\
+ &(\dataScalar_3 -(m\inputScalar_3 + c))^2 \\
+ &
\text{etc.}
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

\section{Linear Algebra}

\notes{Linear algebra provides a very similar role, when we introduce [linear algebra](http://en.wikipedia.org/wiki/Linear_algebra), it is because we are faced with a large number of addition and multiplication operations. These operations need to be done together and would be very tedious to write down as a group. So the first reason we reach for linear algebra is for a more compact representation of our mathematical formulae.}

\notes{
### Running Example: Olympic Marathons

Now we will load in the Olympic marathon data. This is data of the olympic marath times for the men's marathon from the first olympics in 1896 up until the London 2012 olympics.}

\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']}

\notes{You can see what these values are by typing:}

\code{print(x)
print(y)}

\notes{Note that they are not `pandas` data frames for this example, they are just arrays of dimensionality $\numData\times 1$, where $\numData$ is the number of data.}

\notes{The aim of this lab is to have you coding linear regression in python. We will do it in two ways, once using iterative updates (coordinate ascent) and then using linear algebra. The linear algebra approach will not only work much better, it is easy to extend to multiple input linear regression and *non-linear* regression using basis functions.}

\notes{
### Plotting the Data

You can make a plot of $\dataScalar$ vs $\inputScalar$ with the following command:}

\plotcode{%matplotlib inline 
import matplotlib.pyplot as plt}

\plotcode{plt.plot(x, y, 'rx')
plt.xlabel('year')
plt.ylabel('pace in min/km')}

\notes{
### Maximum Likelihood: Iterative Solution

Now we will take the maximum likelihood approach we derived in the lecture to fit a line, $\dataScalar_i=m\inputScalar_i + c$, to the data you've plotted. We are trying to minimize the error function:
$$
\errorFunction(m, c) =  \sum_{i=1}^\numData(\dataScalar_i-m\inputScalar_i-c)^2
$$
with respect to $m$, $c$ and $\sigma^2$. We can start with an initial guess for $m$,}

\code{m = -0.4
c = 80}

\notes{Then we use the maximum likelihood update to find an estimate for the offset, $c$.}

### Coordinate Descent

\notes{In the movie recommender system example, we minimised the objective function by steepest descent based gradient methods. Our updates required us to compute the gradient at the position we were located, then to update the gradient according to the direction of steepest descent. This time, we will take another approach. It is known as *coordinate descent*. In coordinate descent, we choose to move one parameter at a time. Ideally, we design an algorithm that at each step moves the parameter to its minimum value. At each step we choose to move the individual parameter to its minimum.}

\notes{To find the minimum, we look for the point in the curve where the gradient is zero. This can be found by taking the gradient of $\errorFunction(m,c)$ with respect to the parameter.}

\slides{
### Learning is Optimization

* Learning is minimization of the cost function.
* At the minima the gradient is zero.
* Coordinate ascent, find gradient in each coordinate and set to zero.
  $$\frac{\text{d}\errorFunction(c)}{\text{d}c} = -2\sum_{i=1}^\numData \left(\dataScalar_i- m \inputScalar_i - c \right)$$
  $$0 = -2\sum_{i=1}^\numData\left(\dataScalar_i- m\inputScalar_i - c \right)$$}

\slides{
### Learning is Optimization

* Fixed point equations
  $$0 = -2\sum_{i=1}^\numData \dataScalar_i +2\sum_{i=1}^\numData m \inputScalar_i +2n c$$
  $$c = \frac{\sum_{i=1}^\numData \left(\dataScalar_i - m\inputScalar_i\right)}{\numData}$$}

\notes{
#### Update for Offset

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


\slides{
### Learning is Optimization

* Learning is minimization of the cost function.
* At the minima the gradient is zero.
* Coordinate ascent, find gradient in each coordinate and set to zero.
  $$\frac{\text{d}\errorFunction(m)}{\text{d}m} = -2\sum_{i=1}^\numData \inputScalar_i\left(\dataScalar_i- m \inputScalar_i - c \right)$$
  $$0 = -2\sum_{i=1}^\numData \inputScalar_i \left(\dataScalar_i-m \inputScalar_i - c \right)$$
}

\slides{
### Learning is Optimization

* Fixed point equations
  $$0 = -2\sum_{i=1}^\numData \inputScalar_i\dataScalar_i+2\sum_{i=1}^\numData m \inputScalar_i^2+2\sum_{i=1}^\numData c\inputScalar_i$$
  $$m  =    \frac{\sum_{i=1}^\numData \left(\dataScalar_i -c\right)\inputScalar_i}{\sum_{i=1}^\numData\inputScalar_i^2}$$
}
\notes{
### Update for Slope

Now we have the offset set to the minimum value, in coordinate descent, the next step is to optimise another parameter. Only one further parameter remains. That is the slope of the system.}

\notes{Now we can turn our attention to the slope. We once again peform the same set of computations to find the minima. We end up with an update equation of the following form.}

$$m^* = \frac{\sum_{i=1}^\numData (\dataScalar_i - c)\inputScalar_i}{\sum_{i=1}^\numData \inputScalar_i^2}$$

\notes{Communication of mathematics in data science is an essential skill, in a moment, you will be asked to rederive the equation above. Before we do that, however, we will briefly review how to write mathematics in the notebook.}

\notes{
### $\LaTeX$ for Maths

These cells use [Markdown format](http://en.wikipedia.org/wiki/Markdown). You can include maths in your markdown using [$\LaTeX$ syntax](http://en.wikipedia.org/wiki/LaTeX), all you have to do is write your answer inside dollar signs, as follows:}

\notes{To write a fraction, we write `$\frac{a}{b}$`, and it will display like this $\frac{a}{b}$. To write a subscript we write `$a_b$` which will appear as $a_b$. To write a superscript (for example in a polynomial) we write `$a^b$` which will appear as $a^b$. There are lots of other macros as well, for example we can do greek letters such as `$\alpha, \beta, \gamma$` rendering as $\alpha, \beta, \gamma$. And we can do sum and intergral signs as `$\sum \int \int$`.}

\notes{You can combine many of these operations together for composing expressions.}

\writeassignment{Convert the following python code expressions into $\LaTeX$j, writing your answers below. In each case write your answer as a single equality (i.e. your maths should only contain one expression, not several lines of expressions). For the purposes of your $\LaTeX$ please assume that `x` and `w` are $n$ dimensional vectors.

```(a) f = x.sum()```

```(b) m = x.mean()```

```(c) g = (x*w).sum()```}{1}{15}


### Fixed Point Updates

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
### Gradient With Respect to the Slope

Now that you've had a little training in writing maths with $\LaTeX$, we will be able to use it to answer questions. The next thing we are going to do is a little differentiation practice.}

\writeassignment{Derive the the gradient of the objective function
with respect to the slope, $m$. Rearrange it to show that the update equation
written above does find the stationary points of the objective function. By
computing its derivative show that it's a minimum.}{2}{20}

\code{m = ((y - c)*x).sum()/(x**2).sum()
print(m)}

\notes{We can have a look at how good our fit is by computing the prediction across the input space. First create a vector of 'test points',}

\code{import numpy as np
x_test = np.linspace(1890, 2020, 130)[:, None]}

\notes{Now use this vector to compute some test predictions,}

\code{f_test = m*x_test + c}

\notes{Now plot those test predictions with a blue line on the same plot as the data,}

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
week](./week2.ipynb).
3. Cause the code to stop running when the error change
over less than 10 iterations is smaller than $1\times10^{-4}$. This is known as
a stopping criterion.

Why do we need so many iterations to get to the solution?}{3}{25}

### Important Concepts Not Covered

* Other optimization methods:
    * Second order methods, conjugate gradient, quasi-Newton and Newton.
* Effective heuristics such as momentum.
* Local vs global solutions.

### Reading

* Section 1.1-1.2 of @Rogers:book11 for fitting linear models. 
* Section 1.2.5 of @Bishop:book06 up to equation 1.65.

\slides{
### Multi-dimensional Inputs

* Multivariate functions involve more than one input.
* Height might be a function of weight and gender.
* There could be other contributory factors.
* Place these factors in a feature vector $\inputVector_i$.
* Linear function is now defined as
  $$\mappingFunction(\inputVector_i) = \sum_{j=1}^p w_j \inputScalar_{i, j} + c$$
}

\slides{
### Vector Notation

* Write in vector notation,
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \inputVector_i + c$$
* Can absorb $c$ into $\mappingVector$ by assuming extra input $\inputScalar_0$ which is always 1.
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \inputVector_i$$
}

\include{_ml/includes/linear-regression-iterative.md}


\slides{
### Log Likelihood for Multivariate Regression

The likelihood of a single data point is

. . .

$$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}\right).$$

. . .

Leading to a log likelihood for the data set of

. . . 

$$L(\mappingVector,\dataStd^2)= -\frac{\numData}{2}\log \dataStd^2-\frac{\numData}{2}\log 2\pi -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}.$$

### Error Function

And a corresponding error function of
$$\errorFunction(\mappingVector,\dataStd^2)=\frac{\numData}{2}\log\dataStd^2 + \frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}.$$
}

\slides{
### Expand the Brackets

$$
\begin{align*}
  \errorFunction(\mappingVector,\dataStd^2)  = &
\frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum
_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2}\sum
_{i=1}^{\numData}\dataScalar_i\mappingVector^{\top}\inputVector_i\\&+\frac{1}{2\dataStd^2}\sum
_{i=1}^{\numData}\mappingVector^{\top}\inputVector_i\inputVector_i^{\top}\mappingVector
+\text{const}.\\
    = & \frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum
_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\dataStd^2}
\mappingVector^\top\sum_{i=1}^{\numData}\inputVector_i\dataScalar_i\\&+\frac{1}{2\dataStd^2}
\mappingVector^{\top}\left[\sum
_{i=1}^{\numData}\inputVector_i\inputVector_i^{\top}\right]\mappingVector +\text{const}.
\end{align*}
$$
}

\section{Multiple Input Solution with Linear Algebra}

\notes{You've now seen how slow it can
be to perform a coordinate ascent on a system. Another approach to solving the
system (which is not always possible, particularly in *non-linear* systems) is
to go direct to the minimum. To do this we need to introduce *linear algebra*.
We will represent all our errors and functions in the form of linear algebra.
As we mentioned above, linear algebra is just a shorthand for performing lots of
multiplications and additions simultaneously. What does it have to do with our
system then? Well the first thing to note is that the linear function we were
trying to fit has the following form:
$$
\mappingFunction(x) = mx + c
$$
the classical form for a straight line. From a linear algebraic perspective we are looking for multiplications and additions. We are also looking to separate our parameters from our data. The data is the *givens* remember, in French the word is données literally translated means *givens* that's great, because we don't need to change the data, what we need to change are the parameters (or variables) of the model. In this function the data comes in through $x$, and the parameters are $m$ and $c$.}

\notes{What we'd like to create is a vector of parameters and a vector of data. Then we could represent the system with vectors that represent the data, and vectors that represent the parameters.}

\notes{We look to turn the multiplications and additions into a linear algebraic form, we have one multiplication ($m\times c$ and one addition ($mx + c$). But we can turn this into a inner product by writing it in the following way,
$$
\mappingFunction(x) = m \times x +
c \times 1,
$$
in other words we've extracted the unit value, from the offset, $c$. We can think of this unit value like an extra item of data, because it is always given to us, and it is always set to 1 (unlike regular data, which is likely to vary!). We can therefore write each input data location, $\inputVector$, as a vector
$$
\inputVector = \begin{bmatrix} 1\\ x\end{bmatrix}.
$$}

\notes{Now we choose to also turn our parameters into a vector. The parameter vector will be defined to contain 
$$
\mappingVector = \begin{bmatrix} c \\ m\end{bmatrix}
$$
because if we now take the inner product between these to vectors we recover
$$
\inputVector\cdot\mappingVector = 1 \times c + x \times m = mx + c
$$
In `numpy` we can define this vector as follows}

\code{# define the vector w
w = np.zeros(shape=(2, 1))
w[0] = m
w[1] = c}

\notes{This gives us the equivalence between original operation and an operation in vector space. Whilst the notation here isn't a lot shorter, the beauty is that we will be able to add as many features as we like and still keep the seame
representation. In general, we are now moving to a system where each of our predictions is given by an inner product. When we want to represent a linear product in linear algebra, we tend to do it with the transpose operation, so since we have $\mathbf{a}\cdot\mathbf{b} = \mathbf{a}^\top\mathbf{b}$ we can write
$$
\mappingFunction(\inputVector_i) = \inputVector_i^\top\mappingVector.
$$
Where we've assumed that each data point, $\inputVector_i$, is now written by appending a 1 onto the original vector
$$
\inputVector_i = \begin{bmatrix} 
1 \\
\inputScalar_i
\end{bmatrix}
$$}

\section{Design Matrix}

\notes{We can do this for the entire data set to form a [*design
matrix*](http://en.wikipedia.org/wiki/Design_matrix) $\inputMatrix$,

$$\inputMatrix
= \begin{bmatrix} 
\inputVector_1^\top \\\ 
\inputVector_2^\top \\\ 
\vdots \\\
\inputVector_\numData^\top
\end{bmatrix} = \begin{bmatrix}
1 & \inputScalar_1 \\\
1 & \inputScalar_2 \\\
\vdots
& \vdots \\\
1 & \inputScalar_\numData 
\end{bmatrix},$$}

\notes{which in `numpy` can be done with the following commands:}

\code{X = np.hstack((np.ones_like(x), x))
print(X)}

\notes{
### Writing the Objective with Linear Algebra

When we think of the objective function, we can think of it as the errors where the error is defined in a similar way to what it was in Legendre's day $\dataScalar_i - \mappingFunction(\inputVector_i)$, in statistics these errors are also sometimes called [*residuals*](http://en.wikipedia.org/wiki/Errors_and_residuals_in_statistics). So we can think as the objective and the prediction function as two separate parts, first we have,
$$
\errorFunction(\mappingVector) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputVector_i; \mappingVector))^2,
$$
where we've made the function $\mappingFunction(\cdot)$'s dependence on the parameters $\mappingVector$ explicit in this equation. Then we have the definition of the function itself,
$$
\mappingFunction(\inputVector_i; \mappingVector) = \inputVector_i^\top \mappingVector.
$$
Let's look again at these two equations and see if we can identify any inner products. The first equation is a sum of squares, which is promising. Any sum of squares can be represented by an inner product,
$$
a = \sum_{i=1}^{k} b^2_i = \mathbf{b}^\top\mathbf{b},
$$
so if we wish to represent $\errorFunction(\mappingVector)$ in this way, all we need to do is convert the sum operator to an inner product. We can get a vector from that sum operator by placing both $\dataScalar_i$ and $\mappingFunction(\inputVector_i; \mappingVector)$ into vectors, which we do by defining 
$$
\dataVector = \begin{bmatrix}\dataScalar_1\\ \dataScalar_2\\ \vdots \\ \dataScalar_\numData\end{bmatrix}
$$
and defining
$$
\mappingFunctionVector(\inputVector_1; \mappingVector) = \begin{bmatrix}\mappingFunction(\inputVector_1; \mappingVector)\\ \mappingFunction(\inputVector_2; \mappingVector)\\ \vdots \\ \mappingFunction(\inputVector_\numData; \mappingVector)\end{bmatrix}.
$$
The second of these is actually a vector-valued function. This term may appear intimidating, but the idea is straightforward. A vector valued function is simply a vector whose elements are themselves defined as *functions*, i.e. it is a vector of functions, rather than a vector of scalars. The idea is so straightforward, that we are going to ignore it for the moment, and barely use it in the derivation. But it will reappear later when we introduce *basis functions*. So we will, for the moment, ignore the dependence of $\mappingFunctionVector$ on $\mappingVector$ and $\inputMatrix$ and simply summarise it by a vector of numbers
$$
\mappingFunctionVector = \begin{bmatrix}\mappingFunction_1\\\mappingFunction_2\\
\vdots \\ \mappingFunction_\numData\end{bmatrix}.
$$
This allows us to write our objective in the folowing, linear algebraic form,
$$
\errorFunction(\mappingVector) = (\dataVector - \mappingFunctionVector)^\top(\dataVector - \mappingFunctionVector)
$$
from the rules of inner products. But what of our matrix $\inputMatrix$ of input data? At this point, we need to dust off [*matrix-vector multiplication*](http://en.wikipedia.org/wiki/Matrix_multiplication). Matrix multiplication is simply a convenient way of performing many inner products together, and it's exactly what we need to summarise the operation
$$
f_i = \inputVector_i^\top\mappingVector.
$$
This operation tells us that each element of the vector $\mappingFunctionVector$ (our vector valued function) is given by an inner product between $\inputVector_i$ and $\mappingVector$. In other words it is a series of inner products. Let's look at the definition of matrix multiplication, it takes the form
$$
\mathbf{c} = \mathbf{B}\mathbf{a}
$$
where $\mathbf{c}$ might be a $k$ dimensional vector (which we can intepret as a $k\times 1$ dimensional matrix), and $\mathbf{B}$ is a $k\times k$ dimensional matrix and $\mathbf{a}$ is a $k$ dimensional vector ($k\times 1$ dimensional matrix).}

\notes{The result of this multiplication is of the form
$$
\begin{bmatrix}c_1\\c_2 \\ \vdots \\
a_k\end{bmatrix} = 
\begin{bmatrix} b_{1,1} & b_{1, 2} & \dots & b_{1, k} \\
b_{2, 1} & b_{2, 2} & \dots & b_{2, k} \\
\vdots & \vdots & \ddots & \vdots \\
b_{k, 1} & b_{k, 2} & \dots & b_{k, k} \end{bmatrix} \begin{bmatrix}a_1\\a_2 \\
\vdots\\ c_k\end{bmatrix} = \begin{bmatrix} b_{1, 1}a_1 + b_{1, 2}a_2 + \dots +
b_{1, k}a_k\\
b_{2, 1}a_1 + b_{2, 2}a_2 + \dots + b_{2, k}a_k \\ 
\vdots\\
b_{k, 1}a_1 + b_{k, 2}a_2 + \dots + b_{k, k}a_k\end{bmatrix}
$$
so we see that each element of the result, $\mathbf{a}$ is simply the inner product between each *row* of $\mathbf{B}$ and the vector $\mathbf{c}$. Because we have defined each element of $\mappingFunctionVector$ to be given by the inner product between each *row* of the design matrix and the vector $\mappingVector$ we now can write the full operation in one matrix multiplication,
$$
\mappingFunctionVector = \inputMatrix\mappingVector.
$$}

\code{f = np.dot(X, w) # np.dot does matrix multiplication in python}

\notes{Combining this result with our objective function,
$$
\errorFunction(\mappingVector) = (\dataVector - \mappingFunctionVector)^\top(\dataVector - \mappingFunctionVector)
$$
we find we have defined the *model* with two equations. One equation tells us the form of our predictive function and how it depends on its parameters, the other tells us the form of our objective function.}

\code{resid = (y-f)
E = np.dot(resid.T, resid) # matrix multiplication on a single vector is equivalent to a dot product.
print("Error function is:", E)}

\writeassignment{The prediction for our movie recommender system had the form
$$
f_{i,j} = \mathbf{u}_i^\top \mathbf{v}_j
$$
and the objective
function was then
$$
E = \sum_{i,j} s_{i,j}(\dataScalar_{i,j} - f_{i, j})^2
$$
Try writing this down in matrix and vector form. How many of the terms can you do? For each variable and parameter carefully think about whether it should be represented as a matrix or vector. Do as many of the terms as you can. Use $\LaTeX$ to give your answers and give the *dimensions* of any matrices you create.}{4}{20}


\section{Objective Optimisation}

\notes{Our *model* has now been defined with two equations, the prediction function and the objective function. Next we will use multivariate calculus to define an *algorithm* to fit the model. The separation between model and algorithm is important and is often overlooked. Our model contains a function that shows how it will be used for prediction, and a function that describes the objective function we need to optimise to obtain a good set of parameters.}

\notes{The model linear regression model we have described is still the same as the one we fitted above with a coordinate ascent algorithm. We have only played with the notation to obtain the same model in a matrix and vector notation. However, we will now fit this model with a different algorithm, one that is much faster. It is such a widely used algorithm that from the end user's perspective it doesn't even look like an algorithm, it just appears to be a single operation (or function). However, underneath the computer calls an algorithm to find the solution. Further, the algorithm we obtain is very widely used, and because of this it turns out to be highly optimised.}

\notes{Once again we are going to try and find the stationary points of our objective by finding the *stationary points*. However, the stationary points of a multivariate function, are a little bit more complext to find. Once again we need to find the point at which the derivative is zero, but now we need to use  *multivariate calculus* to find it. This involves learning a few additional rules of differentiation (that allow you to do the derivatives of a function with respect to  vector), but in the end it makes things quite a bit easier. We define vectorial derivatives as follows,
$$
\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} =
\begin{bmatrix}\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingScalar_1}\\\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingScalar_2}\end{bmatrix}.
$$
where $\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingScalar_1}$ is the [partial derivative](http://en.wikipedia.org/wiki/Partial_derivative) of the error function with respect to $\mappingScalar_1$.}

\notes{Differentiation through multiplications and additions is relatively straightforward, and since linear algebra is just multiplication and addition, then its rules of diffentiation are quite straightforward too, but slightly more complex than regular derivatives. }


### Multivariate Derivatives

\slides{* We will need some multivariate calculus.
* For now some simple multivariate differentiation:
  $$\frac{\text{d}{\mathbf{a}^{\top}}{\mappingVector}}{\text{d}\mappingVector}=\mathbf{a}$$
  and
  $$\frac{\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
  or if $\mathbf{A}$ is symmetric (*i.e.*
    $\mathbf{A}=\mathbf{A}^{\top}$)
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$}

\notes{We will need two rules of multivariate or *matrix* differentiation. The first is diffentiation of an inner product. By remembering that the inner product is made up of multiplication and addition, we can hope that its derivative is quite straightforward, and so it proves to be. We can start by thinking about the
definition of the inner product,
$$
\mathbf{a}^\top\mathbf{z} = \sum_{i} a_i
z_i,
$$
which if we were to take the derivative with respect to $z_k$ would simply return the gradient of the one term in the sum for which the derivative was non zero, that of $a_k$, so we know that 
$$
\frac{\text{d}}{\text{d}z_k} \mathbf{a}^\top \mathbf{z} = a_k
$$
and by our definition of multivariate derivatives we can simply stack all the partial derivatives of this form in a vector to obtain the result that
$$
\frac{\text{d}}{\text{d}\mathbf{z}}
\mathbf{a}^\top \mathbf{z} = \mathbf{a}.
$$
The second rule that's required is differentiation of a 'matrix quadratic'. A scalar quadratic in $z$ with coefficient $c$ has the form $cz^2$. If $\mathbf{z}$ is a $k\times 1$ vector and $\mathbf{C}$ is a $k \times k$ *matrix* of coefficients then the matrix quadratic form is written as $\mathbf{z}^\top \mathbf{C}\mathbf{z}$, which is itself a *scalar* quantity, but it is a function of a *vector*.}

\notes{#### Matching Dimensions in Matrix Multiplications

\notes{There's a trick for telling that it's a scalar result. When you are doing maths with matrices, it's always worth pausing to perform a quick sanity check on the dimensions. Matrix multplication only works when the dimensions match. To be precise, the 'inner' dimension of the matrix must match. What is the inner dimension. If we multiply two matrices $\mathbf{A}$ and $\mathbf{B}$, the first of which has $k$ rows and $\ell$ columns and the second of which has $p$ rows and $q$ columns, then we can check whether the multiplication works by writing the dimensionalities next to each other,
$$
\mathbf{A} \mathbf{B} \rightarrow (k \times
\underbrace{\ell)(p}_\text{inner dimensions} \times q) \rightarrow (k\times q).
$$
The inner dimensions are the two inside dimensions, $\ell$ and $p$. The multiplication will only work if $\ell=p$. The result of the multiplication will then be a $k\times q$ matrix: this dimensionality comes from the 'outer dimensions'. Note that matrix multiplication is not [*commutative*](http://en.wikipedia.org/wiki/Commutative_property). And if you change the order of the multiplication, 
$$
\mathbf{B} \mathbf{A} \rightarrow (\ell \times \underbrace{k)(q}_\text{inner dimensions} \times p) \rightarrow (\ell \times p).
$$
firstly it may no longer even work, because now the condition is that $k=q$, and secondly the result could be of a different dimensionality. An exception is if the matrices are square matrices (e.g. same number of rows as columns) and they are both *symmetric*. A symmetric matrix is one for which $\mathbf{A}=\mathbf{A}^\top$, or equivalently, $a_{i,j} = a_{j,i}$
for all $i$ and $j$.}

\notes{You will need to get used to working with matrices and vectors applying and developing new machine learning techniques. You should have come across them before, but you may not have used them as extensively as we will now do in this course. You should get used to using this trick to check your work and ensure you know what the dimension of an output matrix should be. For our matrix quadratic form, it turns out that we can see it as a special type of inner product.
$$
\mathbf{z}^\top\mathbf{C}\mathbf{z} \rightarrow (1\times
\underbrace{k) (k}_\text{inner dimensions}\times k) (k\times 1) \rightarrow
\mathbf{b}^\top\mathbf{z}
$$
where $\mathbf{b} = \mathbf{C}\mathbf{z}$ so
therefore the result is a scalar,
$$
\mathbf{b}^\top\mathbf{z} \rightarrow
(1\times \underbrace{k) (k}_\text{inner dimensions}\times 1) \rightarrow
(1\times 1)
$$
where a $(1\times 1)$ matrix is recognised as a scalar.}

\notes{This implies that we should be able to differentiate this form, and indeed the rule for its differentiation is slightly more complex than the inner product, but still quite simple,
$$
\frac{\text{d}}{\text{d}\mathbf{z}}
\mathbf{z}^\top\mathbf{C}\mathbf{z}= \mathbf{C}\mathbf{z} + \mathbf{C}^\top
\mathbf{z}.
$$
Note that in the special case where $\mathbf{C}$ is symmetric then we have $\mathbf{C} = \mathbf{C}^\top$ and the derivative simplifies to 
$$
\frac{\text{d}}{\text{d}\mathbf{z}} \mathbf{z}^\top\mathbf{C}\mathbf{z}=
2\mathbf{C}\mathbf{z}.
$$}}

### Differentiate the Objective

\slides{\alignleft{Differentiating with respect to the vector $\mappingVector$ we obtain}
$$
\frac{\partial L\left(\mappingVector,\dataStd^2 \right)}{\partial
\mappingVector}=\frac{1}{\dataStd^2} \sum _{i=1}^{\numData}\inputVector_i \dataScalar_i-\frac{1}{\dataStd^2}
\left[\sum _{i=1}^{\numData}\inputVector_i\inputVector_i^{\top}\right]\mappingVector
$$
Leading to
$$
\mappingVector^{*}=\left[\sum
_{i=1}^{\numData}\inputVector_i\inputVector_i^{\top}\right]^{-1}\sum
_{i=1}^{\numData}\inputVector_i\dataScalar_i,
$$\slides{

### Differentiate the Objective

}
Rewrite in matrix notation:
$$
\sum_{i=1}^{\numData}\inputVector_i\inputVector_i^\top = \inputMatrix^\top \inputMatrix
$$
$$
\sum_{i=1}^{\numData}\inputVector_i\dataScalar_i = \inputMatrix^\top \dataVector
$$}

\notes{First, we need to compute the full objective by substituting our prediction function into the objective function to obtain the objective in terms of $\mappingVector$. Doing this we obtain
$$
\errorFunction(\mappingVector)= (\dataVector - \inputMatrix\mappingVector)^\top (\dataVector - \inputMatrix\mappingVector).
$$
We now need to differentiate this *quadratic form* to find the minimum. We differentiate with respect to the *vector* $\mappingVector$. But before we do that, we'll expand the brackets in the quadratic form to obtain a series of scalar terms. The rules for bracket expansion across the vectors are similar to those for the scalar system giving,
$$
(\mathbf{a} - \mathbf{b})^\top
(\mathbf{c} - \mathbf{d}) = \mathbf{a}^\top \mathbf{c} - \mathbf{a}^\top
\mathbf{d} - \mathbf{b}^\top \mathbf{c} + \mathbf{b}^\top \mathbf{d}
$$
which substituting for $\mathbf{a} = \mathbf{c} = \dataVector$ and $\mathbf{b}=\mathbf{d} = \inputMatrix\mappingVector$ gives
$$
\errorFunction(\mappingVector)=
\dataVector^\top\dataVector - 2\dataVector^\top\inputMatrix\mappingVector +
\mappingVector^\top\inputMatrix^\top\inputMatrix\mappingVector
$$
where we used the fact that $\dataVector^\top\inputMatrix\mappingVector=\mappingVector^\top\inputMatrix^\top\dataVector$. Now we can use our rules of differentiation to compute the derivative of this form, which is,
$$
\frac{\text{d}}{\text{d}\mappingVector}\errorFunction(\mappingVector)=- 2\inputMatrix^\top \dataVector +
2\inputMatrix^\top\inputMatrix\mappingVector,
$$
where we have exploited the fact that $\inputMatrix^\top\inputMatrix$ is symmetric to obtain this result.}

\writeassignment{Use the equivalence between our vector and our matrix
formulations of linear regression, alongside our definition of vector derivates,
to match the gradients we've computed directly for $\frac{\text{d}\errorFunction(c, m)}{\text{d}c}$ and $\frac{\text{d}\errorFunction(c, m)}{\text{d}m}$ to those for $\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector}$.}{5}{20}


\section{Update Equation for Global Optimum}

\slides{### Update Equations

* Update for $\mappingVector^{*}$.
  $$\mappingVector^{*} = \left(\inputMatrix^\top \inputMatrix\right)^{-1} \inputMatrix^\top \dataVector$$
* The equation for $\left.\dataStd^2\right.^{*}$ may also be found
  $$\left.\dataStd^2\right.^{{*}}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\inputVector_i\right)^{2}}{\numData}.$$}

\notes{Once again, we need to find the minimum of our objective function. Using our likelihood for multiple input regression we can now minimize for our parameter vector $\mappingVector$. Firstly, just as in the single input case, we seek stationary points by find parameter vectors that solve for when the gradients are zero,
$$
\mathbf{0}=- 2\inputMatrix^\top
\dataVector + 2\inputMatrix^\top\inputMatrix\mappingVector,
$$
where $\mathbf{0}$ is a *vector* of zeros. Rearranging this equation we find the solution to be
$$
\mappingVector = \left[\inputMatrix^\top \inputMatrix\right]^{-1} \inputMatrix^\top
\dataVector
$$ 
where $\mathbf{A}^{-1}$ denotes [*matrix inverse*](http://en.wikipedia.org/wiki/Invertible_matrix).}

### Solving the Multivariate System

\notes{The solution for $\mappingVector$ is given in terms of a matrix inverse, but computation of a matrix inverse requires, in itself, an algorithm to resolve it. You'll know this if you had to invert, by hand, a $3\times 3$ matrix in high school. From a numerical stability perspective, it is also best not to compute the matrix inverse directly, but rather to ask the computer to *solve* the  system of linear equations given by $$\inputMatrix^\top\inputMatrix \mappingVector = \inputMatrix^\top\dataVector$$ for $\mappingVector$. This can be done in `numpy` using the command}

\code{np.linalg.solve?}

\notes{so we can obtain the solution using}

\code{w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y))
print(w)}

\notes{We can map it back to the liner regression and plot the fit as follows}

\code{m = w[1]; c=w[0]
f_test = m*x_test + c
print(m)
print(c)
plt.plot(x_test, f_test, 'b-')
plt.plot(x, y, 'rx')}

\notes{### Multivariate Linear Regression

A major advantage of the new system is that we can build a linear regression on a multivariate system. The matrix calculus didn't specify what the length of the vector $\inputVector$ should be, or equivalently the size of the design matrix. }

\notes{### Movie Body Count Data

Let's consider the movie body count data.}

\code{data = pods.datasets.movie_body_count()
movies = data['Y']}

\notes{Let's remind ourselves of the features we've been provided with.}

\code{print(', '.join(movies.columns))}

\notes{Now we will build a design matrix based on the numeric features: year, Body_Count, Length_Minutes in an effort to predict the rating. We build the design matrix as follows:}

\notes{### Relation to Single Input System

Bias as an additional feature.}

\code{select_features = ['Year', 'Body_Count', 'Length_Minutes']
X = movies[select_features]
X['Eins'] = 1 # add a column for the offset
y = movies[['IMDB_Rating']]}

\notes{Now let's perform a linear regression. But this time, we will create a pandas data frame for the result so we can store it in a form that we can visualise easily.}

\code{import pandas as pd
w = pd.DataFrame(data=np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y)),  # solve linear regression here
                 index = X.columns,  # columns of X become rows of w
                 columns=['regression_coefficient']) # the column of X is the value of regression coefficient}

\notes{We can check the residuals to see how good our estimates are}

\code{(y - np.dot(X, w)).hist()}

\notes{Which shows our model *hasn't* yet done a great job of representation, because the spread of values is large. We can check what the rating is dominated by in terms of regression coefficients.}

\code{w}

\notes{Although we have to be a little careful about interpretation because our input values live on different scales, however it looks like we are dominated by the bias, with a small negative effect for later films (but bear in mind the years are large, so this effect is probably larger than it looks) and a positive effect for length. So it looks like long earlier films generally do better, but the residuals are so high that we probably haven't modelled the system very well.}

\notes{
\includeyoutube{ui-uNlFHoms}

\includeyoutube{78YNphT90-k}
}

\notes{### Solution with QR Decomposition

Performing a solve instead of a matrix inverse is the more numerically stable approach, but we can do even better. A [QR-decomposition](http://en.wikipedia.org/wiki/QR_decomposition) of a matrix factorises it into a matrix which is an orthogonal matrix $\mathbf{Q}$, so that $\mathbf{Q}^\top \mathbf{Q} = \eye$. And a matrix which is upper triangular, $\mathbf{R}$. 
$$
\inputMatrix^\top \inputMatrix \boldsymbol{\beta} =
\inputMatrix^\top \dataVector
$$
$$
(\mathbf{Q}\mathbf{R})^\top
(\mathbf{Q}\mathbf{R})\boldsymbol{\beta} = (\mathbf{Q}\mathbf{R})^\top
\dataVector
$$
$$
\mathbf{R}^\top (\mathbf{Q}^\top \mathbf{Q}) \mathbf{R}
\boldsymbol{\beta} = \mathbf{R}^\top \mathbf{Q}^\top \dataVector
$$
$$
\mathbf{R}^\top \mathbf{R} \boldsymbol{\beta} = \mathbf{R}^\top \mathbf{Q}^\top
\dataVector
$$
$$
\mathbf{R} \boldsymbol{\beta} = \mathbf{Q}^\top \dataVector
$$
This is a more numerically stable solution because it removes the need to compute $\inputMatrix^\top\inputMatrix$ as an intermediate. Computing $\inputMatrix^\top\inputMatrix$ is a bad idea because it involves squaring all the elements of $\inputMatrix$ and thereby potentially reducing the numerical precision with which we can represent the solution. Operating on $\inputMatrix$ directly preserves the numerical precision of the model.}

\notes{This can be more particularly seen when we begin to work with *basis functions* in the next session. Some systems that can be resolved with the QR decomposition can not be resolved by using solve directly.}

\code{import scipy as sp
Q, R = np.linalg.qr(X)
w = sp.linalg.solve_triangular(R, np.dot(Q.T, y)) 
w = pd.DataFrame(w, index=X.columns)
w}


### Reading

* Section 1.3 of @Rogers:book11 for Matrix & Vector Review.
