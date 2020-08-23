\ifndef{probabilisticPca}
\define{probabilisticPca}

\editme

\section{Probabilistic PCA}

\notes{In 1997 [Tipping and
Bishop](http://research.microsoft.com/pubs/67218/bishop-ppca-jrss.pdf) [@Tipping:pca97] and
[Roweis](https://www.cs.nyu.edu/~roweis/papers/empca.pdf) [@Roweis:SPCA97] independently
revisited Hotelling's model and considered the case where the noise variance was
finite, but *shared* across all output dimensons. Their model can be thought of
as a factor analysis where}
$$
\boldsymbol{\Sigma} = \noiseStd^2 \eye.
$$
\notes{This leads to a marginal likelihood of the form}
$$
p(\dataMatrix|\mappingMatrix, \noiseStd^2)
= \prod_{i=1}^\numData\gaussianDist{\dataVector_{i, :}}{\zerosVector}{\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye}
$$
\notes{where the limit of
$\noiseStd^2\rightarrow 0$ is *not* taken. This defines a proper probabilistic
model. Tippping and Bishop then went on to prove that the *maximum likelihood*
solution of this model with respect to $\mappingMatrix$ is given by an eigenvalue
problem. In the probabilistic PCA case the eigenvalues and eigenvectors are
given as follows.}
$$
\mappingMatrix = \mathbf{U}\mathbf{L} \mathbf{R}^\top
$$
\notes{where $\mathbf{U}$ is the eigenvectors of the empirical covariance matrix }
$$
\mathbf{S} = \sum_{i=1}^\numData (\dataVector_{i, :} - \meanVector)(\dataVector_{i,
:} - \meanVector)^\top,
$$ 
\notes{which can be written $\mathbf{S} = \frac{1}{\numData}
\dataMatrix^\top\dataMatrix$ if the data is zero mean. The matrix $\mathbf{L}$ is
diagonal and is dependent on the *eigenvalues* of $\mathbf{S}$,
$\boldsymbol{\Lambda}$. If the $i$th diagonal element of this matrix is given by
$\lambda_i$ then the corresponding element of $\mathbf{L}$ is }
$$
\ell_i = \sqrt{\lambda_i - \noiseStd^2}
$$
\notes{where $\noiseStd^2$ is the noise variance. Note that
if $\noiseStd^2$ is larger than any particular eigenvalue, then that eigenvalue
(along with its corresponding eigenvector) is *discarded* from the solution.}

\subsection{Python Implementation of Probabilistic PCA}

We will now implement this algorithm in python.

\setupcode{import numpy as np}
\code{# probabilistic PCA algorithm
def ppca(Y, q):
    # remove mean
    Y_cent = Y - Y.mean(0)

    # Comute covariance
    S = np.dot(Y_cent.T, Y_cent)/Y.shape[0]
    lambd, U = np.linalg.eig(S)

    # Choose number of eigenvectors
    sigma2 = np.sum(lambd[q:])/(Y.shape[1]-q)
    l = np.sqrt(lambd[:q]-sigma2)
    W = U[:, :q]*l[None, :]
    return W, sigma2}

\notes{In practice we may not wish to compute the eigenvectors of the covariance matrix
directly. This is because it requires us to estimate the covariance, which
involves a sum of squares term, before estimating the eigenvectors. We can
estimate the eigenvectors directly either through [QR
decomposition](http://en.wikipedia.org/wiki/QR_decomposition) or [singular value
decomposition](http://en.wikipedia.org/wiki/Singular_value_decomposition). We
saw a similar issue arise when \refnotes{computing the weights in a regression
problem}{linear-regression}, where we also wished to avoid computation of
$\latentMatrix^\top\latentMatrix$ (or in the case of \refnotes{nonlinear regression with basis functions}{basis-functions} $\boldsymbol{\Phi}^\top\boldsymbol{\Phi}$).}

\section{Posterior for Principal Component Analysis}

\notes{Under the latent variable model
justification for principal component analysis, we are normally interested in
inferring something about the latent variables given the data. This is the
distribution,}
$$
p(\latentVector_{i, :} | \dataVector_{i, :})
$$
\notes{for any given data
point. Determining this density turns out to be very similar to the approach for
determining the Bayesian posterior of $\weightVector$ in Bayesian linear
regression, only this time we place the prior density over $\latentVector_{i, :}$
instead of $\weightVector$. The posterior is proportional to the joint density as
follows,}
$$
p(\latentVector_{i, :} | \dataVector_{i, :}) \propto p(\dataVector_{i,
:}|\mappingMatrix, \latentVector_{i, :}, \noiseStd^2) p(\latentVector_{i, :})
$$
\notes{And as in the Bayesian linear regression case we first consider the log posterior,}
$$
\log p(\latentVector_{i, :} | \dataVector_{i, :}) = \log p(\dataVector_{i, :}|\mappingMatrix,
\latentVector_{i, :}, \noiseStd^2) + \log p(\latentVector_{i, :}) + \text{const}
$$
\notes{where
the constant is not dependent on $\latentVector$. As before we collect the
quadratic terms in $\latentVector_{i, :}$ and we assemble them into a Gaussian
density over $\latentVector$.}
$$
\log p(\latentVector_{i, :} | \dataVector_{i, :}) =
-\frac{1}{2\noiseStd^2} (\dataVector_{i, :} - \mappingMatrix\latentVector_{i,
:})^\top(\dataVector_{i, :} - \mappingMatrix\latentVector_{i, :}) - \frac{1}{2}
\latentVector_{i, :}^\top \latentVector_{i, :} + \text{const}
$$

\writeassignment{Multiply out the terms in the brackets. Then collect
the quadratic term and the linear terms together. Show that the posterior has
the form
$$
\latentVector_{i, :} | \mappingMatrix \sim \gaussianSamp{\meanVector_x}{\covarianceMatrix_x}
$$
where 
$$
\covarianceMatrix_x = \left(\noiseStd^{-2}
\mappingMatrix^\top\mappingMatrix + \eye\right)^{-1}
$$
and 
$$
\meanVector_x
= \covarianceMatrix_x \noiseStd^{-2}\mappingMatrix^\top \dataVector_{i, :} 
$$
Compare this to
the posterior for the Bayesian linear regression from last week, do they have
similar forms? What matches and what differs?}{30}

\subsection{Python Implementation of the Posterior}

Now let's implement the system in
code.


\codeassignment{Use the values for $\mappingMatrix$ and $\noiseStd^2$ you
have computed, along with the data set $\dataMatrix$ to compute the posterior
density over $\latentMatrix$. Write a function of the form}python
mu_x, C_x =
posterior(Y, W, sigma2)}
where `mu_x` and `C_x` are the posterior mean and
posterior covariance for the given $\dataMatrix$. 

Don't forget to subtract the
mean of the data `Y` inside your function before computing the posterior:
remember we assumed at the beginning of our analysis that the data had been
centred (i.e. the mean was removed).}{20}

\code{# Question 4 Answer Code
# Write code for you answer to this question in this box
# Do not delete these comments, otherwise you will get zero for this answer.
# Make sure your code has run and the answer is correct *before* submitting your notebook for marking.
import numpy as np
import scipy as sp
def posterior(Y, W, sigma2):
    Y_cent = Y - Y.mean(0)
    # Compute posterior over X
    C_x = 
    mu_x = 
    return mu_x, C_x}

# Numerically Stable and Efficient Version

Just as we saw for \refnotes{linear
regression}{linear-regression} and \refnotes{regression with basis functions}{basis-functions}
computation of a matrix such as $\dataMatrix^\top\dataMatrix$ (or its centred
version) can be a bad idea in terms of loss of numerical accuracy. Fortunately,
we can find the eigenvalues and eigenvectors of the matrix
$\dataMatrix^\top\dataMatrix$ without direct computation of the matrix. This can
be done with the [*singular value
decomposition*](http://en.wikipedia.org/wiki/Singular_value_decomposition). The
singular value decompsition takes a matrix, $\mathbf{Z}$ and represents it in
the form,
$$
\mathbf{Z} = \mathbf{U}\boldsymbol{\Lambda}\mathbf{V}^\top
$$
where
$\mathbf{U}$ is a matrix of orthogonal vectors in the columns, meaning
$\mathbf{U}^\top\mathbf{U} = \eye$. It has the same number of rows and
columns as $\mathbf{Z}$. The matrices $\mathbf{\Lambda}$ and $\mathbf{V}$ are
both square with dimensionality given by the number of columns of $\mathbf{Z}$.
The matrix $\mathbf{\Lambda}$ is *diagonal* and $\mathbf{V}$ is an orthogonal
matrix so $\mathbf{V}^\top\mathbf{V} = \mathbf{V}\mathbf{V}^\top = \eye$.
The eigenvalues of the matrix $\dataMatrix^\top\dataMatrix$ are then given by the
singular values of the matrix $\dataMatrix^\top$ squared and the eigenvectors are
given by $\mathbf{U}$.

\subsection{Solution for $\mappingMatrix$}

Given the singular value
decomposition of $\dataMatrix$ then we have
$$
\mappingMatrix =
\mathbf{U}\mathbf{L}\mathbf{R}^\top
$$
where $\mathbf{R}$ is an arbitrary
rotation matrix. This implies that the posterior is given by
$$
\covarianceMatrix_x =
\left[\noiseStd^{-2}\mathbf{R}\mathbf{L}^2\mathbf{R}^\top + \eye\right]^{-1}
$$
because $\mathbf{U}^\top \mathbf{U} = \eye$. Since, by convention, we
normally take $\mathbf{R} = \eye$ to ensure that the principal components
are orthonormal we can write
$$
\covarianceMatrix_x = \left[\noiseStd^{-2}\mathbf{L}^2 +
\eye\right]^{-1}
$$
which implies that $\covarianceMatrix_x$ is actually diagonal
with elements given by
$$
c_i = \frac{\noiseStd^2}{\noiseStd^2 + \ell^2_i}
$$
and
allows us to write
$$
\meanVector_x = [\mathbf{L}^2 + \noiseStd^2
\eye]^{-1} \mathbf{L} \mathbf{U}^\top \dataVector_{i, :}
$$
$$
\meanVector_x = \mathbf{D}\mathbf{U}^\top \dataVector_{i, :}
$$
where
$\mathbf{D}$ is a diagonal matrix with diagonal elements given by $d_{i} =
\frac{\ell_i}{\noiseStd^2 + \ell_i^2}$.

\setupcode{import scipy as sp
import numpy as np}
\code{# probabilistic PCA algorithm using SVD
def ppca(Y, q, center=True):
    """Probabilistic PCA through singular value decomposition"""
    # remove mean
    if center:
        Y_cent = Y - Y.mean(0)
    else:
        Y_cent = Y
        
    # Comute singluar values, discard 'R' as we will assume orthogonal
    U, sqlambd, _ = sp.linalg.svd(Y_cent.T,full_matrices=False)
    lambd = (sqlambd**2)/Y.shape[0]
    # Compute residual and extract eigenvectors
    sigma2 = np.sum(lambd[q:])/(Y.shape[1]-q)
    ell = np.sqrt(lambd[:q]-sigma2)
    return U[:, :q], ell, sigma2

def posterior(Y, U, ell, sigma2, center=True):
    """Posterior computation for the latent variables given the eigendecomposition."""
    if center:
        Y_cent = Y - Y.mean(0)
    else:
        Y_cent = Y
    C_x = np.diag(sigma2/(sigma2+ell**2))
    d = ell/(sigma2+ell**2)
    mu_x = np.dot(Y_cent, U)*d[None, :]
    return mu_x, C_x}


\endif
