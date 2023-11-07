\ifndef{modelVsAlgorithm}
\define{modelVsAlgorithm}

\editme

\subsection{Traditional Model-Algorithm Separation}

\notes{Across both statistics and machine learning, the traditional view was that the modeling assumptions are the key to making good predictions. Those assumptions might include smoothness assumptions, or linearity assumptions. In some domains we might also wish to incorporate some of our mechanistic understanding of the data (see e.g. @Alvarez:llfm13). The paradigm of model-based machine learning (@Winn:mbml19), builds on the idea that the aim of machine learning is to describe one's views about the world as accurately as possible within a model. The domain expert becomes the model-designer. The process of algorithm design is then automated to as great an extent as possible. This idea originates in the ground-breaking work of the MRC Biostatistics Unit on BUGS that dates to 1997 (see e.g. Lunn-bugs09). It is no surprise that this notion has gained most traction in the Bayesian community, because the probabilistic philosophy promises the separation of modeling and inference. As long as the probabilistic model we build is complex enough to capture the true generating process, we can separate the process of model building and probabilistic inference. Inference becomes turning the handle on the machine. Unfortunately, the handle turning in Bayesian inference involves high dimensional integrals and much of the work in this domain has focused on developing new methods of inference based around either sampling (see e.g. @Carpenter-stan17) or deterministic approximations (see e.g. @Tran-edward16).}

\notes{There are two principle challenges for model-based machine learning. The first is the model design challenge, and the second is the algorithm design challenge. The basic philosophy of the model-based approach is to make it as easy as possible for experts to express their ideas in a modeling language (typically probabilistic) and then automate as much as possible the algorithmic process of fitting that model to data (typically probabilistic inference).}

\notes{The challenge of combining that model with the data, the algorithm design challenge, is then the process of probabilistic inference.}

\notes{The model is a mathematical abstraction of
the regularities of the universe that we believe underly the data as
collected. If the model is well-chosen, we will be able to interpolate
the data and predict likely values of future data points. If it is chosen
badly our predictions will be overconfident and wrong.}

\notes{Deep learning methods conflate two aspects that we used to try to keep distinct. The mathematical model encodes our assumptions about the data. The algorithm is a set of computational instructions that combine our modeling assumptions with data to make predictions.}

\notes{Much of the technical focus in machine learning is on algorithms. In
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
