\ifndef{linearRegressionDirectSolution}
\define{linearRegressionDirectSolution}

\editme


\subsection{Log Likelihood for Multivariate Regression}

\slides{
The likelihood of a single data point is

. . .

$$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}\right).$$

. . .

Leading to a log likelihood for the data set of

. . . 

$$L(\mappingVector,\dataStd^2)= -\frac{\numData}{2}\log \dataStd^2-\frac{\numData}{2}\log 2\pi -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}.$$
}
\newslide{Error Function}
\slides{
And a corresponding error function of
$$\errorFunction(\mappingVector,\dataStd^2)=\frac{\numData}{2}\log\dataStd^2 + \frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\dataStd^2}.$$
}

\newslide{Expand the Brackets}
\slides{

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

\notes{We look to turn the multiplications and additions into a linear algebraic form, we have one multiplication ($m\times c$) and one addition ($mx + c$). But we can turn this into a inner product by writing it in the following way,
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

\setupcode{import numpy as np}
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

\setupcode{import numpy as np}
\code{X = np.hstack((np.ones_like(x), x))
print(X)}

\notes{
\subsection{Writing the Objective with Linear Algebra}

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

\setupcode{import numpy as np}
\code{f = X@w # The @ sign performs matrix multiplication}

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
Try writing this down in matrix and vector form. How many of the terms can you do? For each variable and parameter carefully think about whether it should be represented as a matrix or vector. Do as many of the terms as you can. Use $\LaTeX$ to give your answers and give the *dimensions* of any matrices you create.}{20}


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


\subsection{Multivariate Derivatives}

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

\notes{\subsubsection{Matching Dimensions in Matrix Multiplications}}

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
$$}

\subsection{Differentiate the Objective}

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

\subsection{Differentiate the Objective}

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
to match the gradients we've computed directly for $\frac{\text{d}\errorFunction(c, m)}{\text{d}c}$ and $\frac{\text{d}\errorFunction(c, m)}{\text{d}m}$ to those for $\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector}$.}{20}


\section{Update Equation for Global Optimum}

\newslide{Update Equations}

\slides{
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

\subsection{Solving the Multivariate System}

\notes{The solution for $\mappingVector$ is given in terms of a matrix inverse, but computation of a matrix inverse requires, in itself, an algorithm to resolve it. You'll know this if you had to invert, by hand, a $3\times 3$ matrix in high school. From a numerical stability perspective, it is also best not to compute the matrix inverse directly, but rather to ask the computer to *solve* the  system of linear equations given by $$\inputMatrix^\top\inputMatrix \mappingVector = \inputMatrix^\top\dataVector$$ for $\mappingVector$. This can be done in `numpy` using the command}

\setupcode{import numpy as np}
\code{np.linalg.solve?}

\notes{so we can obtain the solution using}

\code{w = np.linalg.solve(X.T@X, X.T@y)
print(w)}

\notes{We can map it back to the liner regression and plot the fit as follows}

\setupplotcode{import matplotlib.pyplot as plt}
\plotcode{m = w[1]; c=w[0]
f_test = m*x_test + c
print(m)
print(c)
plt.plot(x_test, f_test, 'b-')
plt.plot(x, y, 'rx')}

\notes{\subsection{Multivariate Linear Regression}

A major advantage of the new system is that we can build a linear regression on a multivariate system. The matrix calculus didn't specify what the length of the vector $\inputVector$ should be, or equivalently the size of the design matrix. }

\notes{\include{_ml/include/movie-body-count-linear-regression.md}}

\endif
