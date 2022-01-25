\ifndef{linearRegressionDirectSolution}
\define{linearRegressionDirectSolution}

\editme


\ifndef{designMatrix}
\define{designMatrix}{\inputMatrix}
\endif
\ifndef{designVariable}
\define{designVariable}{X}
\endif

\subsection{Quadratic Loss}

\notes{Now we've identified the empirical risk with the loss, we'll use $\errorFunction(\mappingVector)$ to represent our objective function.}
$$
\errorFunction(\mappingVector) = \sum_{i=1}^\numData \left(\dataScalar_i - \mappingFunction(\inputVector_i, \mappingVector)\right)^2
$$
\notes{gives us our objective.}

\newslide{Linear Model}

\notes{In the case of the linear prediction function, we can substitute $\mappingFunction(\inputVector_i, \mappingVector) = \mappingVector^\top \inputVector_i$.}
$$
\errorFunction(\mappingVector) = \sum_{i=1}^\numData \left(\dataScalar_i - \mappingVector^\top \inputVector_i\right)^2
$$
\notes{To compute the gradient of the objective, we first expand the brackets.}

\subsection{Bracket Expansion}

\ifndef{noNoiseTerm}
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
\else
$$
\begin{align*}
  \errorFunction(\mappingVector,\dataStd^2)  = & \sum
_{i=1}^{\numData}\dataScalar_i^{2}- 2\sum
_{i=1}^{\numData}\dataScalar_i\mappingVector^{\top}\inputVector_i\\&+\sum
_{i=1}^{\numData}\mappingVector^{\top}\inputVector_i\inputVector_i^{\top}\mappingVector\\
    = & \sum_{i=1}^{\numData}\dataScalar_i^{2}-
2 \mappingVector^\top\sum_{i=1}^{\numData}\inputVector_i\dataScalar_i\\&+
\mappingVector^{\top}\left[\sum
_{i=1}^{\numData}\inputVector_i\inputVector_i^{\top}\right]\mappingVector.
\end{align*}
$$
\endif
\notes{
\section{Solution with Linear Algebra}}

\notes{In this section we're going compute the minimum of the quadratic loss with respect to the parameters. When we do this, we'll also review *linear algebra*.
We will represent all our errors and functions in the form of matrices and vectors.}

\notes{Linear algebra is just a shorthand for performing lots of
multiplications and additions simultaneously. What does it have to do with our
system then? Well, the first thing to note is that the classic linear function we fit for a one dimensional regression
has the  form:
$$
\mappingFunction(x) = mx + c
$$
the classical form for a straight line. From a linear algebraic perspective, we are looking for multiplications and additions. We are also looking to separate our parameters from our data. The data is the *givens*. In French the word is données literally translated means *givens* that's great, because we don't need to change the data, what we need to change are the parameters (or variables) of the model. In this function the data comes in through $x$, and the parameters are $m$ and $c$.}

\notes{What we'd like to create is a vector of parameters and a vector of data. Then we could represent the system with vectors that represent the data, and vectors that represent the parameters.}

\notes{We look to turn the multiplications and additions into a linear algebraic form, we have one multiplication ($m\times c$) and one addition ($mx + c$). But we can turn this into an inner product by writing it in the following way,
$$
\mappingFunction(x) = m \times x +
c \times 1,
$$
in other words, we've extracted the unit value from the offset, $c$. We can think of this unit value like an extra item of data, because it is always given to us, and it is always set to 1 (unlike regular data, which is likely to vary!). We can therefore write each input data location, $\inputVector$, as a vector
$$
\inputVector = \begin{bmatrix} 1\\ x\end{bmatrix}.
$$}

\notes{Now we choose to also turn our parameters into a vector. The parameter vector will be defined to contain 
$$
\mappingVector = \begin{bmatrix} c \\ m\end{bmatrix}
$$
because if we now take the inner product between these two vectors we recover
$$
\inputVector\cdot\mappingVector = 1 \times c + x \times m = mx + c
$$
In `numpy` we can define this vector as follows}

\setupcode{import numpy as np}
\code{# define the vector w
w = np.zeros(shape=(2, 1))
w[0] = m
w[1] = c}

\notes{This gives us the equivalence between original operation and an operation in vector space. Whilst the notation here isn't a lot shorter, the beauty is that we will be able to add as many features as we like and keep the same
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
matrix*](http://en.wikipedia.org/wiki/Design_matrix) $\designMatrix$,}
$$
\designMatrix
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
\end{bmatrix}\notes{,}
$$
\notes{which in `numpy` can be done with the following commands:}

\setupcode{import numpy as np}
\code{\designVariable = np.hstack((np.ones_like(x), x))
print(\designVariable)}

\subsection{Writing the Objective with Linear Algebra}

\notes{When we think of the objective function, we can think of it as the errors where the error is defined in a similar way to what it was in Legendre's day $\dataScalar_i - \mappingFunction(\inputVector_i)$, in statistics these errors are also sometimes called [*residuals*](http://en.wikipedia.org/wiki/Errors_and_residuals_in_statistics). So, we can think as the objective and the prediction function as two separate parts, first we have,}
$$
\errorFunction(\mappingVector) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputVector_i; \mappingVector))^2,
$$
\notes{where we've made the function $\mappingFunction(\cdot)$'s dependence on the parameters $\mappingVector$ explicit in this equation. Then we have the definition of the function itself,}
$$
\mappingFunction(\inputVector_i; \mappingVector) = \inputVector_i^\top \mappingVector.
$$
\notes{Let's look again at these two equations and see if we can identify any inner products. The first equation is a sum of squares, which is promising. Any sum of squares can be represented by an inner product,
$$
a = \sum_{i=1}^{k} b^2_i = \mathbf{b}^\top\mathbf{b}.
$$
If we wish to represent $\errorFunction(\mappingVector)$ in this way, all we need to do is convert the sum operator to an inner product. We can get a vector from that sum operator by placing both $\dataScalar_i$ and $\mappingFunction(\inputVector_i; \mappingVector)$ into vectors, which we do by defining
$$
\dataVector = \begin{bmatrix}\dataScalar_1\\ \dataScalar_2\\ \vdots \\ \dataScalar_\numData\end{bmatrix}
$$
and defining
$$
\mappingFunctionVector(\inputVector_1; \mappingVector) = \begin{bmatrix}\mappingFunction(\inputVector_1; \mappingVector)\\ \mappingFunction(\inputVector_2; \mappingVector)\\ \vdots \\ \mappingFunction(\inputVector_\numData; \mappingVector)\end{bmatrix}.
$$
The second of these is a vector-valued function. This term may appear intimidating, but the idea is straightforward. A vector valued function is simply a vector whose elements are themselves defined as *functions*, i.e., it is a vector of functions, rather than a vector of scalars. The idea is so straightforward, that we are going to ignore it for the moment, and barely use it in the derivation. But it will reappear later when we introduce *basis functions*. So, we will for the moment ignore the dependence of $\mappingFunctionVector$ on $\mappingVector$ and $\designMatrix$ and simply summarise it by a vector of numbers}\newslide{Stacking Vectors}
$$
\mappingFunctionVector = \begin{bmatrix}\mappingFunction_1\\\mappingFunction_2\\
\vdots \\ \mappingFunction_\numData\end{bmatrix}.
$$
\notes{This allows us to write our objective in the folowing, linear algebraic form,}
$$
\errorFunction(\mappingVector) = (\dataVector - \mappingFunctionVector)^\top(\dataVector - \mappingFunctionVector)
$$
\notes{from the rules of inner products. But what of our matrix $\designMatrix$ of input data? At this point, we need to dust off [*matrix-vector multiplication*](http://en.wikipedia.org/wiki/Matrix_multiplication). Matrix multiplication is simply a convenient way of performing many inner products together, and it's exactly what we need to summarize the operation
$$
f_i = \inputVector_i^\top\mappingVector.
$$
This operation tells us that each element of the vector $\mappingFunctionVector$ (our vector valued function) is given by an inner product between $\inputVector_i$ and $\mappingVector$. In other words, it is a series of inner products. Let's look at the definition of matrix multiplication, it takes the form
$$
\mathbf{c} = \mathbf{B}\mathbf{a},
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
b_{k, 1}a_1 + b_{k, 2}a_2 + \dots + b_{k, k}a_k\end{bmatrix}.
$$
We see that each element of the result, $\mathbf{a}$ is simply the inner product between each *row* of $\mathbf{B}$ and the vector $\mathbf{c}$. Because we have defined each element of $\mappingFunctionVector$ to be given by the inner product between each *row* of the design matrix and the vector $\mappingVector$ we now can write the full operation in one matrix multiplication,}
\newslide{}
$$
\mappingFunctionVector = \designMatrix\mappingVector.
$$

\setupcode{import numpy as np}
\code{f = \designVariable@w # The @ sign performs matrix multiplication}

\notes{Combining this result with our objective function,}
$$
\errorFunction(\mappingVector) = (\dataVector - \mappingFunctionVector)^\top(\dataVector - \mappingFunctionVector)
$$
\notes{we find we have defined the *model* with two equations. One equation tells us the form of our predictive function and how it depends on its parameters, the other tells us the form of our objective function.}

\code{resid = (y-f)
E = np.dot(resid.T, resid) # matrix multiplication on a single vector is equivalent to a dot product.
print("Error function is:", E)}

\endif
