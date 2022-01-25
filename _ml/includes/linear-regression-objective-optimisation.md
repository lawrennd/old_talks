\ifndef{linearRegressionObjectiveOptimisation}
\define{linearRegressionObjectiveOptimisation}

\editme

\section{Objective Optimization}

\notes{Our *model* has now been defined with two equations: the prediction function and the objective function. Now we will use multivariate calculus to define an *algorithm* to fit the model. The separation between model and algorithm is important and is often overlooked. Our model contains a function that shows how it will be used for prediction, and a function that describes the objective function we need to optimize to obtain a good set of parameters.}

\notes{The model linear regression model we have described is still the same as the one we fitted above with a coordinate ascent algorithm. We have only played with the notation to obtain the same model in a matrix and vector notation. However, we will now fit this model with a different algorithm, one that is much faster. It is such a widely used algorithm that from the end user's perspective it doesn't even look like an algorithm, it just appears to be a single operation (or function). However, underneath the computer calls an algorithm to find the solution. Further, the algorithm we obtain is very widely used, and because of this it turns out to be highly optimized.}

\notes{Once again, we are going to try and find the stationary points of our objective by finding the *stationary points*. However, the stationary points of a multivariate function, are a little bit more complex to find. As before we need to find the point at which the gradient is zero, but now we need to use  *multivariate calculus* to find it. This involves learning a few additional rules of differentiation (that allow you to do the derivatives of a function with respect to vector), but in the end it makes things quite a bit easier. We define vectorial derivatives as follows,
$$
\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} =
\begin{bmatrix}\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingScalar_1}\\\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingScalar_2}\end{bmatrix}.
$$
where $\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingScalar_1}$ is the [partial derivative](http://en.wikipedia.org/wiki/Partial_derivative) of the error function with respect to $\mappingScalar_1$.}

\notes{Differentiation through multiplications and additions is relatively straightforward, and since linear algebra is just multiplication and addition, then its rules of differentiation are quite straightforward too, but slightly more complex than regular derivatives.}


\subsection{Multivariate Derivatives}

\slides{* We will need some multivariate calculus.
* For now some simple multivariate differentiation:
  $$\frac{\text{d}{\mathbf{a}^{\top}}{\mappingVector}}{\text{d}\mappingVector}=\mathbf{a}$$
  and
  $$\frac{\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
  or if $\mathbf{A}$ is symmetric (*i.e.*
    $\mathbf{A}=\mathbf{A}^{\top}$)
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$}

\notes{We will need two rules of multivariate or *matrix* differentiation. The first is differentiation of an inner product. By remembering that the inner product is made up of multiplication and addition, we can hope that its derivative is quite straightforward, and so it proves to be. We can start by thinking about the
definition of the inner product,
$$
\mathbf{a}^\top\mathbf{z} = \sum_{i} a_i
z_i,
$$
which if we were to take the derivative with respect to $z_k$ would simply return the gradient of the one term in the sum for which the derivative was non-zero, that of $a_k$, so we know that 
$$
\frac{\text{d}}{\text{d}z_k} \mathbf{a}^\top \mathbf{z} = a_k
$$
and by our definition for multivariate derivatives, we can simply stack all the partial derivatives of this form in a vector to obtain the result that
$$
\frac{\text{d}}{\text{d}\mathbf{z}}
\mathbf{a}^\top \mathbf{z} = \mathbf{a}.
$$
The second rule that's required is differentiation of a 'matrix quadratic'. A scalar quadratic in $z$ with coefficient $c$ has the form $cz^2$. If $\mathbf{z}$ is a $k\times 1$ vector and $\mathbf{C}$ is a $k \times k$ *matrix* of coefficients then the matrix quadratic form is written as $\mathbf{z}^\top \mathbf{C}\mathbf{z}$, which is itself a *scalar* quantity, but it is a function of a *vector*.}

\notes{\subsubsection{Matching Dimensions in Matrix Multiplications}}

\notes{There's a trick for telling a multiplication leads to a scalar result. When you are doing mathematics with matrices, it's always worth pausing to perform a quick sanity check on the dimensions. Matrix multplication only works when the dimensions match. To be precise, the 'inner' dimension of the matrix must match. What is the inner dimension? If we multiply two matrices $\mathbf{A}$ and $\mathbf{B}$, the first of which has $k$ rows and $\ell$ columns and the second of which has $p$ rows and $q$ columns, then we can check whether the multiplication works by writing the dimensionalities next to each other,
$$
\mathbf{A} \mathbf{B} \rightarrow (k \times
\underbrace{\ell)(p}_\text{inner dimensions} \times q) \rightarrow (k\times q).
$$
The inner dimensions are the two inside dimensions, $\ell$ and $p$. The multiplication will only work if $\ell=p$. The result of the multiplication will then be a $k\times q$ matrix: this dimensionality comes from the 'outer dimensions'. Note that matrix multiplication is not [*commutative*](http://en.wikipedia.org/wiki/Commutative_property). And if you change the order of the multiplication, 
$$
\mathbf{B} \mathbf{A} \rightarrow (\ell \times \underbrace{k)(q}_\text{inner dimensions} \times p) \rightarrow (\ell \times p).
$$
Firstly, it may no longer even work, because now the condition is that $k=q$, and secondly the result could be of a different dimensionality. An exception is if the matrices are square matrices (e.g., same number of rows as columns) and they are both *symmetric*. A symmetric matrix is one for which $\mathbf{A}=\mathbf{A}^\top$, or equivalently, $a_{i,j} = a_{j,i}$
for all $i$ and $j$.}

\notes{For applying and developing machine learning algorithms you should get familiar with working with matrices and vectors. You should have come across them before, but you may not have used them as extensively as we are doing now. It's worth getting used to using this trick to check your work and ensure you know what the dimension of an output matrix should be. For our matrix quadratic form, it turns out that we can see it as a special type of inner product.
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
\sum_{i=1}^{\numData}\inputVector_i\inputVector_i^\top = \designMatrix^\top \designMatrix
$$
$$
\sum_{i=1}^{\numData}\inputVector_i\dataScalar_i = \designMatrix^\top \dataVector
$$}

\notes{First, we need to compute the full objective by substituting our prediction function into the objective function to obtain the objective in terms of $\mappingVector$. Doing this we obtain
$$
\errorFunction(\mappingVector)= (\dataVector - \designMatrix\mappingVector)^\top (\dataVector - \designMatrix\mappingVector).
$$
We now need to differentiate this *quadratic form* to find the minimum. We differentiate with respect to the *vector* $\mappingVector$. But before we do that, we'll expand the brackets in the quadratic form to obtain a series of scalar terms. The rules for bracket expansion across the vectors are similar to those for the scalar system giving,
$$
(\mathbf{a} - \mathbf{b})^\top
(\mathbf{c} - \mathbf{d}) = \mathbf{a}^\top \mathbf{c} - \mathbf{a}^\top
\mathbf{d} - \mathbf{b}^\top \mathbf{c} + \mathbf{b}^\top \mathbf{d}
$$
which substituting for $\mathbf{a} = \mathbf{c} = \dataVector$ and $\mathbf{b}=\mathbf{d} = \designMatrix\mappingVector$ gives
$$
\errorFunction(\mappingVector)=
\dataVector^\top\dataVector - 2\dataVector^\top\designMatrix\mappingVector +
\mappingVector^\top\designMatrix^\top\designMatrix\mappingVector
$$
where we used the fact that $\dataVector^\top\designMatrix\mappingVector=\mappingVector^\top\designMatrix^\top\dataVector$. 

Now we can use our rules of differentiation to compute the derivative of this form, which is,
$$
\frac{\text{d}}{\text{d}\mappingVector}\errorFunction(\mappingVector)=- 2\designMatrix^\top \dataVector +
2\designMatrix^\top\designMatrix\mappingVector,
$$
where we have exploited the fact that $\designMatrix^\top\designMatrix$ is symmetric to obtain this result.}

\writeassignment{Use the equivalence between our vector and our matrix
formulations of linear regression, alongside our definition of vector derivates,
to match the gradients we've computed directly for $\frac{\text{d}\errorFunction(c, m)}{\text{d}c}$ and $\frac{\text{d}\errorFunction(c, m)}{\text{d}m}$ to those for $\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector}$.}{20}


\section{Update Equation for Global Optimum}

\newslide{Update Equations}

\slides{
* Solve the matrix equation for $\mappingVector$.
  $$\designMatrix^\top \designMatrix\mappingVector =  \designMatrix^\top \dataVector$$
\ifndef{noNoiseTerm}
* The equation for $\left.\dataStd^2\right.^{*}$ may also be found
  $$\left.\dataStd^2\right.^{{*}}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\inputVector_i\right)^{2}}{\numData}.$$
\endif}

\notes{We need to find the minimum of our objective function. Using our objective function, we can  minimize for our parameter vector $\mappingVector$. Firstly,  we seek stationary points by find parameter vectors that solve for when the gradients are zero,
$$
\mathbf{0}=- 2\designMatrix^\top
\dataVector + 2\designMatrix^\top\designMatrix\mappingVector,
$$
where $\mathbf{0}$ is a *vector* of zeros. Rearranging this equation, we find the solution to be
$$
\designMatrix^\top \designMatrix \mappingVector = \designMatrix^\top
\dataVector
$$ 
which is a matrix equation of the familiar form $\mathbf{A}\mathbf{x} = \mathbf{b}$.}

\notes{\subsection{Solving the Multivariate System}}

\notes{The solution for $\mappingVector$ can be written mathematically in terms of a matrix inverse of $\designMatrix^\top\designMatrix$, but computation of a matrix inverse requires an algorithm to resolve it. You'll know this if you had to invert, by hand, a $3\times 3$ matrix in high school. From a numerical stability perspective, it is also best not to compute the matrix inverse directly, but rather to ask the computer to *solve* the  system of linear equations given by 
$$
\designMatrix^\top\designMatrix \mappingVector = \designMatrix^\top\dataVector
$$ 
for $\mappingVector$.} 

\notes{\subsection{Multivariate Linear Regression}

A major advantage of the new system is that we can build a linear regression on a multivariate system. The matrix calculus didn't specify what the length of the vector $\inputVector$ should be, or equivalently the size of the design matrix. }

\endif
