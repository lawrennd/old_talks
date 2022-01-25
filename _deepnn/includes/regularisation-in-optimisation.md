\ifndef{regularisationInOptimisation}
\define{regularisationInOptimisation}

\editme

\subsection{Regularization in Optimization}

\slides{* Gradient flow methods allow us to study nature of optima.
* In particular systems, with given initialisations, we can show L1 and L2 norms are minimised.
* In other cases the rank of $\mappingMatrix$ is minimised.
* Questions remain over the nature of this regularisation in neural networks.}

\notes{Another interesting theoretical direction is to study the path that neural network algorithms take when finding the optima. For certain simple linear systems, you can analytically study the 'gradient flow'.}

\notes{Neural networks are normally trained by (stochastic) gradient descent. This is a discrete optimization algorithm where at each point, a step in the direction of the (approximate) gradient is taken.}

\notes{Gradient flow replaces this discrete update with a differential equation, where the step at any point is an exact gradient update. As a result, the path of the optimization can be studied as a *differential equation*.}

\notes{By making assumptions about the initialization, the optima that gradient flow will find can be characterised. For a highly overparameterized linear model, @Gunasekar-implicit2017 show in matrix factorization, that for particular initializations, the optima will be a *global* optimum of the objective that minimizes the L2-norm.}

\notes{By reparameterizing the linear model so that each $\mappingScalar_i = u_i^2 - v_i^2$ and optimising in the space defined by $\mathbf{u}$ and $\mathbf{v}$ @Woodworth-kernel20 show that the L1 norm is found.}

\newslide{Deep Linear Models}
\notes{Other papers have looked at *deep linear models* [@Arora-convergence19] where}
$$
\mappingFunction(\inputVector; \mappingMatrix) = \mappingMatrix_4 \mappingMatrix_3 \mappingMatrix_2 \mappingMatrix_1 \inputVector.
$$
\notes{In these models, a gradient flow analysis shows that the model finds solutions where the linear mapping,}
$$
\mappingMatrix = \mappingMatrix_4 \mappingMatrix_3 \mappingMatrix_2 \mappingMatrix_1 
$$
\notes{is very low rank. This is highly suggestive of another type of regularization that could be occurring in deep neural networks. Low rank parameter matrices mean that the effective capacity of the neural network is reduced. Indeed, empirical observations of the rank of deep nets trained on data suggest that they may be finding such solutions.}

\endif
