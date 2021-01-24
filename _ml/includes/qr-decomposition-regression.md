\ifndef{qrDecompositionRegression}
\define{qrDecompositionRegression}

\editme

\subsection{Solution with QR Decomposition}

\notes{Performing a solve instead of a matrix inverse is the more numerically stable approach, but we can do even better. A [QR-decomposition](http://en.wikipedia.org/wiki/QR_decomposition) of a matrix factorises it into a matrix which is an orthogonal matrix $\mathbf{Q}$, so that $\mathbf{Q}^\top \mathbf{Q} = \eye$. And a matrix which is upper triangular, $\mathbf{R}$.}
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
\newslide{}
$$
\mathbf{R}^\top \mathbf{R} \boldsymbol{\beta} = \mathbf{R}^\top \mathbf{Q}^\top
\dataVector
$$
$$
\mathbf{R} \boldsymbol{\beta} = \mathbf{Q}^\top \dataVector
$$
\newslide{}

\notes{This is a more numerically stable solution because it removes the need to compute $\inputMatrix^\top\inputMatrix$ as an intermediate. Computing $\inputMatrix^\top\inputMatrix$ is a bad idea because it involves squaring all the elements of $\inputMatrix$ and thereby potentially reducing the numerical precision with which we can represent the solution. Operating on $\inputMatrix$ directly preserves the numerical precision of the model.}\slides{* More nummerically stable.
* Avoids the intermediate computation of $\inputMatrix^\top\inputMatrix$.}


\notes{This can be more particularly seen when we begin to work with *basis functions* in the next session. Some systems that can be resolved with the QR decomposition can not be resolved by using solve directly.}

\setupcode{import scipy as sp}
\code{Q, R = np.linalg.qr(X)
w = sp.linalg.solve_triangular(R, Q.T@y) 
w = pd.DataFrame(w, index=X.columns)
w}

\endif
