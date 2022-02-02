\ifndef{qrDecompositionRegression}
\define{qrDecompositionRegression}

\editme

\subsection{Solution with QR Decomposition}

\notes{Performing a solve instead of a matrix inverse is the more numerically stable approach, but we can do even better. A [QR-decomposition](http://en.wikipedia.org/wiki/QR_decomposition) of a matrix factorizes it into a matrix which is an orthogonal matrix $\mathbf{Q}$, so that $\mathbf{Q}^\top \mathbf{Q} = \eye$. And a matrix which is upper triangular, $\mathbf{R}$.}
$$
\designMatrix^\top \designMatrix \boldsymbol{\beta} =
\designMatrix^\top \dataVector
$$
\notes{and we }substitute $\designMatrix = \mathbf{Q}{\mathbf{R}$ \notes{so we have}
$$
(\mathbf{Q}\mathbf{R})^\top
(\mathbf{Q}\mathbf{R})\boldsymbol{\beta} = (\mathbf{Q}\mathbf{R})^\top
\dataVector
$$
$$
\mathbf{R}^\top (\mathbf{Q}^\top \mathbf{Q}) \mathbf{R}
\boldsymbol{\beta} = \mathbf{R}^\top \mathbf{Q}^\top \dataVector
$$
\newslide{}
$$
\mathbf{R}^\top \mathbf{R} \boldsymbol{\beta} = \mathbf{R}^\top \mathbf{Q}^\top
\dataVector
$$
$$
\mathbf{R} \boldsymbol{\beta} = \mathbf{Q}^\top \dataVector
$$
\notes{which leaves us with a lower triangular system to solve.}
\newslide{}

\notes{This is a more numerically stable solution because it removes the need to compute $\designMatrix^\top\designMatrix$ as an intermediate. Computing $\designMatrix^\top\designMatrix$ is a bad idea because it involves squaring all the elements of $\designMatrix$ and thereby potentially reducing the numerical precision with which we can represent the solution. Operating on $\designMatrix$ directly preserves the numerical precision of the model.}\slides{* More nummerically stable.
* Avoids the intermediate computation of $\designMatrix^\top\designMatrix$.}


\notes{This can be more particularly seen when we begin to work with *basis functions* in the next session. Some systems that can be resolved with the QR decomposition cannot be resolved by using solve directly.}

\setupcode{import scipy as sp}
\code{Q, R = np.linalg.qr(\designVariable)
w = sp.linalg.solve_triangular(R, Q.T@y) 
w = pd.DataFrame(w, index=\designVariable.columns)
w}

\endif
