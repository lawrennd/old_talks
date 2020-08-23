\ifndef{modelVsAlgorithm}
\define{modelVsAlgorithm}

\editme

\subsubsection{Models vs Algorithms}

Much of the technical focus in machine learning is on algorithms. In
this document I want to retain a strong separation between the *model*
and the *algorithm*. The model is a mathematical abstraction of the
world that encapsulates our assumptions about the data. Normally it will
depend on one or more parameters which are adaptable. The algorithm
provides a procedure for adapting the model to different contexts, often
through the provision of a set of data that is used for training the
model.}

\notes{ Despite the different role of model and algorithm, the two
concepts are often conflated. This sometimes leads to a confused
discussion. I was recently asked "Is it correct to remove the mean
from the data before you do principal component analysis." This
question is about an algorithmic procedure, but the correct answer
depends on what modelling assumption you are seeking to make when you
are constructing your principal component analysis. Principal
component analysis was originally proposed by a *model* for data by
[@Hotelling:analysis33]. It is a latent variable model that was
directly inspired by work in the social sciences on factor
analysis. However, much of our discussion of PCA today focusses on PCA
as an algorithm. The algorithm for fitting the PCA model is to seek
the eigenvectors of the covariance matrix, and people often refer to
this algorithm as principal component analysis. However, that
algorithm also finds the linear directions of maximum variance in the
data. Seeking directions of maximum variance in the data was not the
objective of Hotelling, but it is related to a challenge posed by
@Pearson:01 who sought a variant of regression that predicted
symmetrically regardless of which variable was considered to be the
covariate and which variable the response. Coincidentally the
algorithm for this model is also the eigenvector decomposition of the
covariance matrix. However, the underlying model is different. The
difference becomes clear when you begin to seek non-linear variants of
principal component analysis.  Depending on your interpretation
(finding directions of maximum variance in the data or a latent
variable model) the corresponding algorithm differs. For the Pearson
model a valid non-linearization is kernel PCA
[@Scholkopf:nonlinear98], but for the Hotelling model this
generalization doesn't make sense. A valid generalization of the
Hotelling model is provided by the Gaussian process latent variable
model [@Lawrence:pnpca05]. This confusion is often unhelpful, so for
the moment we will leave algorithmic considerations to one side and
focus *only* on the model.}

\endif
