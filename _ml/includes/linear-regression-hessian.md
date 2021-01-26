\ifndef{linearRegressionHessian}
\define{linearRegressionHessian}

\editme

\subsection{Hessian Matrix}

\notes{We can also compute the *Hessian* matrix, the curvature of the loss function. We simply take the second derivative of the loss function with respect to the parameter vector,}
$$
\frac{\text{d}^2}{\text{d}\mappingVector \text{d}\mappingVector^\top} \errorFunction(\mappingVector) = 2\designMatrix^\top\designMatrix.
$$
\notes{So we see that the curvature is given by the design matrix.}

\notes{Note that for this linear model the curvature is *not* dependent on the values of the parameter vector, $\mappingVector$, or indeed on the *response* variables, $\dataVector$. This is unusual, in general the curvature will depend on the parameters and the response variables. The linear model with quadratic loss is a special case because the overall loss function has a *quadratic form* which is the unique form with constant curvature across the whole space.}

\notes{This is one reason why linear models are so easy to work with.}

\notes{Because the curvature is constant everywhere, we know that the curvature at the minimum is given by $2\designMatrix^\top\designMatrix$.}

\notes{From univariate calculus you might recall that the optimum is a maximum if the curvature is negative, and a minimum if the curvature is positive. A similar theorem holds for multivariate calculus, but now the curvature must be *positive definite* for the point to be a minimum. The constant curvature also shows us also that the minimum is *unique*.}


\notes{Positive definite means that for any two vectors, $\mathbf{u}$ of unit length $\mathbf{u}^\top\mathbf{u}$ we have that,}
$$
\mathbf{u}^\top\mathbf{A} \mathbf{u} > 0 \quad \forall \quad \mathbf{u} \quad \text{with}\quad \mathbf{u}^\top\mathbf{u}=1
$$
\notes{The matrix $\designMatrix^\top\designMatrix$ (where we've dropped the 2) will satisfy this condition as long as the columns of $\designMatrix$ are *linearly independent* and the number of basis functions is less or equal to the number of data.}

\subsection{Eigendecomposition of Hessian}

\notes{Applying a vector $\mathbf{u}$ to the Hessian matrix gives us the curvature in a particular direction. So we can use this to look at the shape of the minimum by projecting onto the different directions, $\mathbf{u}$.}

\notes{Recall the eigendecomposition of a matrix,}
$$
\mathbf{A}\mathbf{u} = \lambda\mathbf{u}
$$
\notes{If we allow $\mathbf{u}_i$ to be an *eigenvector* of $\designMatrix^\top\designMatrix\mappingVector$ then the curvature in that direction is given by the corresponding eigenvalue, $\lambda_i$.}
$$
\designMatrix^\top\designMatrix\mathbf{u}_i = \lambda_i \mathbf{u}_i
$$

\notes{So the eigendecomposition of the Hessian is a convenient representation of the nature of these minima. The principal eigenvector (the one associated with the largest eigenvalue), $\mathbf{u}_1$ is associated with the direction of *highest curvature*. While the minor eigenvector shows us the flattest direction, where the  curvature is smallest.}

\endif
