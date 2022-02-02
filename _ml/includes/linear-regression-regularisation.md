\ifndef{linearRegressionRegularisation}
\define{linearRegressionregularisation}

\editme

\subsection{Regularization}

\slides{Linear system, solve:}
\notes{The solution to the linear system is given by solving,}
$$
\designMatrix^\top\designMatrix \mappingVector = \designMatrix^\top\dataVector
$$ 
\notes{for $\mappingVector$.}\slides{But if $\designMatrix^\top\designMatrix$ then this is not well posed.}

\notes{But if $\designMatrix^\top\designMatrix$ is not full rank, this system cannot be solved. This is reflective of an *underdetermined system* of equations. There are *infinite* solutions. This happens when there are more basis functions than data points, in effect the number of data we have is not enough to determine the parameters.}

\notes{Thinking about this in terms of the Hessian, if $\designMatrix^\top\designMatrix$ is not full rank, then we are no longer at a minimum. We are in a trough, because *not full rank* implies that there are fewer eigenvectors than dimensions, in effect for those dimensions where there is no eigenvector, the objective function is 'flat'. It is ambivalent to changes in parameters. This implies there are infinite valid solutions.}

\notes{One solution to this problem is to regularize the system.}

\notes{\subsection{Coefficient Shrinkage}}

\notes{Coefficient shrinkage is a technique where the parameters of the of the model are 'encouraged' to be small. In practice this is normally done by augmenting the objective function with a term that keeps the parameters low, typically by penalizing a norm.}

\subsection{Tikhonov Regularization}

\notes{In neural network models this approach is sometimes called 'weight decay'. At every gradient step we reduce the value of the weight a little. This idea comes from an approach called Tikhonov regularization [@Tikhonov:book77], where the objective function is augmented by the L2 norm of the weights,}\slides{* Updated objective:}
$$
\errorFunction(\mappingVector) = (\dataVector - \mappingFunctionVector)^\top(\dataVector - \mappingFunctionVector) + \alpha\ltwoNorm{\mappingMatrix}^2
$$
\notes{with some weighting $\alpha >0$. This has the effect of changing the Hessian at the minimum to}\slides{* Hessian:}
$$
\designMatrix^\top\designMatrix + \alpha \eye
$$
\notes{Which is always full rank. The minimal eigenvalues are now given by $\alpha$.}

\notes{\subsection{Lasso}}

\notes{Other techniques for regularization based on a norm of the parameters include the Lasso [@Tibshirani-lasso96], which is an L1 norm of the parameters}



\subsection{Splines, Functions, Hilbert Kernels}

\slides{* Can also regularize the function $\mappingFunction(\cdot)$ directly.
* This approach taken in *splines* and  @Wahba:book90 and kernels @Scholkopf:learning01.
* Mathematically more elegant, but algorithmically less flexible and harder to scale.}

\notes{Regularization of the parameters has the desired effect of making the solution viable, but it can sometimes be difficult to interpret, particularly if the parameters don't have any inherent meaning (like in a neural network). An alternative approach is to regularize the function, $\mappingFunctionVector$, directly, (see e.g., @Kimeldorf:correspondence70 and @Wahba:book90). This is the approach taken by *spline models* which use energy-based regularization for $\mappingFunction(\cdot)$ and also *kernel methods* such as the support vector machine [@Scholkopf:learning01].}



\endif
