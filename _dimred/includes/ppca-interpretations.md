\ifndef{ppcaInterpretations}
\define{ppcaInterpretations}

\editme

\section{Interpretations of Principal Component Analysis}

\subsection{Relationship to Matrix Factorization}

\slides{* PCA is closely related to matrix factorisation.
* Instead of $\latentMatrix$, $\mappingMatrix$
* Define Users $\mathbf{U}$ and items $\mathbf{V}$
}
\notes{We can use the robot naviation example to realise that PCA (and
factor analysis) are very reminiscient of the \refnotes{*matrix
factorization* example}{matrix-factorization} that we used for
introducing objective functions. In that system we used slightly
different notation, $\mathbf{u}_{i, :}$ for *user* location in our
metaphorical library and $\mathbf{v}_{j, :}$ for *item* location in
our metaphorical library. To see how these systems are somewhat
analagous, now let us think about the user as the robot and the items
as the wifi access points. We can plot the relative location of
both. This process is known as "SLAM": simultaneous *localisation* and
*mapping*. A latent variable model of the type we have developed is
one way of performing SLAM. We have an estimate of the *landmarks* in
the system (in this case WIFI access points) and we have an estimate
of the robot position. These are analagous to the estimate of the
user's position and the estimate of the items positions in the
library. In the matrix factorisation example users are informing us
what items they are 'close' to by expressing their preferences, in the
robot localization example the robot is informing us what access point
it is close to by measuring signal strength.}

\notes{From a personal perspective, I find this analogy
quite comforting. I think it is very arguable that one of the mechanisms through
which we (as humans) may have developed higher reasoning is through the need to
navigate around our environment, identifying landmarks and associating them with
our search for food. If such a system were to exist, the idea that it could be
readily adapted to other domains such as categorising the nature of the
different foodstuffs we were able to forage is intriguing.}

\notes{From an algorithmic
perspective, we also can now realise that matrix factorization and latent
variable modelling are effectively the same thing. The only difference is the
objective function and our probabilistic (or lack of probabilistic) treatment of
the variables. But the prediction function for both systems,}\slides{* Matrix factorisation:}
$$
f_{i, j} =
\mathbf{u}_{i, :}^\top \mathbf{v}_{j, :} 
$$
\notes{for matrix factorization or}\slides{PCA:}
$$
f_{i, j} = \latentVector_{i, :}^\top \weightVector_{j, :} 
$$
\notes{for probabilistic PCA and factor analysis are the same.}

\subsection{Other Interpretations of PCA: Separating Model and Algorithm}

\slides{* PCA introduced as latent variable model (a model).
* Solution is through an eigenvalue problem (an algorithm).
* This causes some confusion about what PCA is.}

\notes{Since Hotelling first introduced his perspective on factor
analysis as PCA there has been somewhat of a conflation of the idea of the model
underlying PCA (for which it was very clear that Hotelling was inspired by
Factor Analysis) and the algorithm that is used to fit that model: the
eigenvalues and eigenvectors of the covariance matrix. The eigenvectors of an
ellipsoid have been known since the middle of the 19th century as the principal
axes of the elipsoid, and they arise through the following additional ideas:
seeking the orthogonal directions of *maximum variance* in a dataset. Pearson in
1901 arrived at the same algorithm driven by a desire to seek a *symmetric
regression* between two covariate/response variables $x$ and $y$ [@Pearson:01]. He is,
therefore, often credited with the invention of principal component analysis,
but to me this seems disengenous. His aim was very different from Hotellings, it
was just happened that the optimal solution for his model was coincident with
that of Hotelling. The approach is also known as the [Karhunen Loeve
Transform](http://en.wikipedia.org/wiki/Karhunen%E2%80%93Lo%C3%A8ve_theorem)  in
stochastic process theory and in classical multidimensional scaling the same
operation can be shown to be minimising a particular objective function based on
interpoint distances in the data and the latent space (see the section on
Classical Multidimensional Scaling in [Mardia, Kent and
Bibby](http://store.elsevier.com/Multivariate-Analysis/Kanti-
Mardia/isbn-9780124712522/)) [@Mardia:multivariate79]. One of my own contributions to machine learning
was deriving yet another model whose linear variant was solved by finding the
principal subspace of the covariance matrix (an approach I termed dual
probabilistic PCA or probabilistic principal coordinate analysis). Finally, the
approach is sometimes referred to simply as singular value decomposition (SVD).
The singular value decomposition of a data set has the following form,}
$$
\dataMatrix = \mathbf{V} \boldsymbol{\Lambda} \mathbf{U}^\top
$$
\notes{where $\mathbf{V}\in\Re^{n\times n}$ and $\mathbf{U}^\in \Re^{p\times p}$ are square
orthogonal matrices and $\mathbf{\Lambda}^{n \times p}$ is zero apart from its
first $p$ diagonal entries. Singularvalue decomposition gives a diagonalisation
of the covariance matrix, because under the SVD we have}
$$
\dataMatrix^\top\dataMatrix =
\mathbf{U}\boldsymbol{\Lambda}\mathbf{V}^\top\mathbf{V} \boldsymbol{\Lambda}
\mathbf{U}^\top = \mathbf{U}\boldsymbol{\Lambda}^2 \mathbf{U}^\top
$$
\notes{where $\boldsymbol{\Lambda}^2$ is now the eigenvalues of the covariane matrix and
$\mathbf{U}$ are the eigenvectors. So performing the SVD can simply be seen as
another approach to determining the principal components.}

\subsection{Separating Model and Algorithm}

\slides{* Separation between *model* and *algorithm* is helpful conceptually.
* Even if in practice they conflate (e.g. deep neural networks).
* Sometimes difficult to pull apart.
* Helpful to revisit algorithms with modelling perspective in mind.
  * Probabilistic numerics}

\notes{I've given a fair amount of personal thought to this situation and my
own opinion that this confusion about method arises because of a
conflation of model and algorithm. The model of Hotelling, that which
he termed principal component analysis, was really a variant of factor
analysis, and it was unfortunate that he chose to rename it. However,
the algorithm he derived was a very convenient way of optimising a
(simplified) factor analysis, and it's therefore become very
popular. The algorithm is also the optimal solution for many other
models of the data, even some which might seem initally to be
unrelated (e.g. seeking directions of maximum variance). It is only
through the mathematics of this linear system (which also contains
some intersting symmetries) that all these ides become
related. However, as soon as we choose to non-linearise the system
(e.g. through basis functions) we find that each of the non-linear
intepretations we can derive for the different models each leads to a
very different algorithm (if such an algorithm is possible). For
example
[principal curves](http://web.stanford.edu/~hastie/Papers/Principal_Curves.pdf)
of @Hastie:pcurves89 attempt to non-linearise the maximum variance
interpretation,
[kernel PCA](http://en.wikipedia.org/wiki/Kernel_principal_component_analysis)
of @Scholkopf:nonlinear98 uses basis functions to form the eigenvalue
problem in a nonlinear space, and my own work in this area
[non-linearises the dual probabilistic PCA](http://jmlr.org/papers/volume6/lawrence05a/lawrence05a.pdf) [@Lawrence:pnpca05].}

\notes{My conclusion is that when you are doing machine learning you should
always have it clear in your mind what your *model* is and what your
*algorithm* is. You can recognise your model because it normally
contains a prediction function and an objective function. The
algorithm on the other hand is the sequence of steps you implement on
the computer to solve for the parameters of this model. For efficient
implementation, we often modify our model to allow for faster
algorithms, and this is a perfectly valid pragmatist's approach, so
conflation of model and algorithm is not always a bad thing. But for
clarity of thinking and understanding it is necessary to maintain the
separation and to maintain a handle on when and why we perform the
conflation.}

\endif
