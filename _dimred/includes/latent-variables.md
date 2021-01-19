\ifndef{latentVariables}
\define{latentVariables}

\editme

\section{Latent Variables}

\notes{Latent means hidden, and hidden variables are simply *unobservable*
variables. The idea of a latent variable is crucial to the concept of artificial
intelligence, machine learning and experimental design. A latent variable could
take many forms. We might observe a man walking along a road with a large bag of
clothes and we might *infer* that the man is walking to the laundrette. Our
observations are a highly complex data space, the response in our eyes is
processed through our visual cortex, the combination of the indidivuals limb
movememnts and the direction they are walking in all conflate in our heads to
cause us to infer that (perhaps) the individual is going to the laundrette. We
don't *know* that the man is walking to the laundrette, but we have a model of
the world that suggests that it's a likely outcome for the very complex data. In
some ways the latent variable can be seen as a *compression* of this very
complex scene. If I were writing a book, I might write that "A man tripped over
whilst walking to the laundrette". In the reader's mind an image of a man,
perhaps laden with dirty clothes, may occur. All these ideas come from our
expectations of the world around us. We can make further inference about the
man, some of it perhaps plausible others less so. The man may be going to the
laundrette because his washing machine is broken, or because he doesn't have a
large enough flat to have a washing machine, or because he's carrying a duvet,
or because he doesn't like ironing. All of these may *increase* in probability
given our observation, but they are still *latent* variables. Unless we follow
the man back to his appartment, or start making other enquirires about the man,
we don't know the true answer.}

\notes{It's clear that to do inference about any
complex system we *must* include latent variables. Latent variables are
extremely powerful. In robotics, they are used to represent the *state* of the
robot. The state of the robot may include its position (in x, y coordinates) its
speed, its direction of facing. How are *these* variables unknown to the robot?
Well the robot only posesses *sensors*, it can make observations of the nearest
object in a certain direction, and it may have a map of its environment. If we
represent the state of the robot as its position on a map, it may be uncertain
of that position. If you go walking or running in the hills around Sheffield,
you can take a very high quality ordnance survey map with you. However, unless
you are a really excellent orienteer, when you are far from any given landmark,
you will probably be *uncertain* about your true position on the map. These
states are also latent variables.}

\notes{In statistical analysis of experiments you
try to control for each aspect of the experiment, in particular by
*randomization*. So if I'm interested in the ability of a particular fertilizer
to improve the yield of a particular plant I may design an experiment where I
apply the fertilizer to some plants (the treatment group) and withold the
fertilizer from others (the control group). I then test to see whether the yield
from the treatment group is better (or worse) than the control group. I may find
that I have an excellent yield for the treatment group. However, what if I'd
(unknowlingly) planted all my treatment plants in a sunny part of the field, and
all the control plants in a shady part of the field. That would also be a latent
variable, in this case known as a *confounder*. In statistical experimental
design *randomization* is used to attempt to eliminate the correlated effects of
these confounders: you aim to ensure that if these confounders *do* exist their
effects are not correlated with treatment and contorl. This is known as a
[randomized control
trial](http://en.wikipedia.org/wiki/Randomized_controlled_trial).}

\notes{Greek philosophers worried a great deal about what was knowable and what was
unknowable. Adherents of [philosophical
Skeptisism](http://en.wikipedia.org/wiki/Skepticism) were inspired by the idea
that since your senses sometimes give you contradictory information, they cannot
be trusted, and in extreme cases they chose to *ignore* their senses. This is an
acknowledgement that very often the true state of the world cannot be known with
precision. Unfortunately, these philosophers didn't have a good understanding of
probability, so they were unable to encapsulate their ideas through a *degree*
of belief.}

\notes{We often use language to express the compression of a complex
behavior or patterns in a simpler way, for example we talk about motives as a
useful distallation for a perhaps very complex patter of behavior. In physics we
use principles of causation and simple laws to describe the world around us.
Such motives or underlying principles are difficult to observe directly, our
conclusions about them emerge over a period of time by observing indirect
consequences of the latent variables.}

\notes{Epistemic uncertainty allows us to deal
with these worries by associating our degree of belief about the state of the
world with a probaiblity distribution. This core idea underpins state space
modelling, probabilistic graphical models and the wider field of latent variable
modelling. In this session we are going to explore the idea in a simple linear
system and see how it relates to *factor analysis* and *principal component
analysis*.}

\section{Your Personality}

\notes{At the beginning of the 20th century there was
a great deal of interest amoungst psychologists in formalizing patterns of
thought. The approach they used became known as factor analysis. The principle
is that we observe a potentially high dimensional vector of characteristics
about an individual. To formalize this, social scientists designed
questionaires. We can envisage many questions that we may ask, but the
assumption is that underlying these questions there are only a few traits that
dictate the behavior. These models are known as latent trait models and the
analysis is sometimes known as factor analysis. The idea is that there are a few
characteristic traits that we are looking to discern. These traits or factors
can be extracted by assimilating the high dimensional characteristics of the
individual into a few latent factors. }

\subsection{Factor Analysis Model}

\notes{This causes
us to consider a model as follows, if we are given a high dimensional vector of
features (perhaps questionaire answers) associated with an individual,
$\dataVector$, we assume that these factors are actually generated from a low
dimensional vector latent traits, or latent variables, which determine the
personality.}
$$
\dataVector = \mathbf{f}(\latentVector) + \noiseVector,
$$
\notes{where $\mathbf{f}(\latentVector)$ is a *vector valued* function that is dependent
on the latent traits and $\noiseVector$ is some corrupting noise. For
simplicity, we assume that the function is given by a *linear* relationship,}
$$
\mathbf{f}(\latentVector) = \mappingMatrix\latentVector
$$
\notes{where we have introduced a
matrix $\mappingMatrix$ that is sometimes referred to as the *factor loadings* but
we also immediately see is related to our *multivariate linear regression*
models from the \refnotes{previous session on linear regression}{linear-regression}. That is
because our vector valued function is of the form}
$$
\mathbf{f}(\latentVector) =
\begin{bmatrix} f_1(\latentVector) \\ f_2(\latentVector) \\ \vdots \\
f_p(\latentVector)\end{bmatrix}
$$
\notes{where there are $\dataDim$ features associated with the
individual. If we consider any of these functions individually we have a
prediction function that looks like a regression model,}
$$
f_j(\latentVector) =
\weightVector_{j, :}^\top \latentVector,
$$
\notes{for each element of the vector valued
function, where $\weightVector_{:, j}$ is the $j$th column of the matrix
$\mappingMatrix$. In that context each column of $\mappingMatrix$ is a vector of
*regression weights*. This is a multiple input and multiple output regression.
Our inputs (or covariates) have dimensionality greater than 1 and our outputs
(or response variables) also have dimensionality greater than one. Just as in a
standard regression, we are assuming that we don't observe the function directly
(note that this *also* makes the function a *type* of latent variable), but we
observe some corrupted variant of the function, where the corruption is given by
$\noiseVector$. Just as in linear regression we can assume that this
corruption is given by Gaussian noise, where the noise for the $j$th element of
$\dataVector$ is by,}
$$
\epsilon_j \sim \gaussianSamp{0}{\noiseStd^2_j}.
$$
\notes{Of course,
just as in a regression problem we also need to make an assumption across the
individual data points to form our full likelihood. Our data set now consists of
many observations of $\dataVector$ for diffetent individuals. We store these
observations in a *design matrix*, $\dataMatrix$, where each *row* of
$\dataMatrix$ contains the observation for one individual. To emphasize that
$\dataVector$ is a vector derived from a row of $\dataMatrix$ we represent the
observation of the features associated with the $i$th individual by
$\dataVector_{i, :}$, and place each individual in our data matrix,}
$$
\dataMatrix
= \begin{bmatrix} \dataVector_{1, :}^\top \\ \dataVector_{2, :}^\top \\ \vdots \\
\dataVector_{n, :}^\top\end{bmatrix},
$$
\notes{where we have $n$ data points. Our data
matrix therefore has $n$ rows and $p$ columns. The point to notice here is that
each data obsesrvation appears as a row vector in the design matrix (thus the
transpose operation inside the brackets). Our prediction functions are now
actually a *matrix value* function,}
$$
\mathbf{F} = \latentMatrix\mappingMatrix^\top,
$$
\notes{where for each matrix the data points are in the rows and the data features
are in the columns. This implies that if we have $q$ inputs to the function we
have $\mathbf{F}\in \Re^{n\times p}$, $\mappingMatrix \in \Re^{p \times q}$ and
$\latentMatrix \in \Re^{n\times q}$.}

\writeassignment{Show that, given all the definitions above, if,
$$
\mathbf{F} = \latentMatrix\mappingMatrix^\top
$$
and the elements of the vector valued
function $\mathbf{F}$ are given by 
$$
f_{i, j} = f_j(\latentVector_{i, :}),
$$
where $\latentVector_{i, :}$ is the $i$th row of the latent variables,
$\latentMatrix$, then show that
$$
f_j(\latentVector_{i, :}) = \weightVector_{j, :}^\top
\latentVector_{i, :}
$$}{10}

\subsection{Latent Variables}

The difference between this model and a multiple output
regression is that in the regression case we are provided with the covariates
$\latentMatrix$, here they are *latent variables*. These variables are unknown.
Just as we have done in the past for unknowns, we now treat them with a
probability distribution. In *factor analysis* we assume that the latent
variables have a Gaussian density which is independent across both across the
latent variables associated with the different data points, and across those
associated with different data features, so we have,
$$
x_{i,j} \sim
\gaussianSamp{0}{1},
$$
and we can write the density governing the latent variable
associated with a single point as,
$$
\latentVector_{i, :} \sim \gaussianSamp{\zerosVector}{\eye}.
$$
If we consider the values of the
function for the $i$th data point as
$$
\mathbf{f}_{i, :} =
\mathbf{f}(\latentVector_{i, :}) = \mappingMatrix\latentVector_{i, :} 
$$
then we can use
the rules for multivariate Gaussian relationships to write that
$$
\mathbf{f}_{i, :} \sim \gaussianSamp{\zerosVector}{\mappingMatrix\mappingMatrix^\top}
$$
which implies that the distribution for $\dataVector_{i, :}$ is given by
$$
\dataVector_{i, :} = \sim \gaussianSamp{\zerosVector}{\mappingMatrix\mappingMatrix^\top + \boldsymbol{\Sigma}}
$$
where $\boldsymbol{\Sigma}$ the covariance of the noise
variable, $\epsilon_{i, :}$ which for factor analysis is a diagonal matrix
(because we have assumed that the noise was *independent* across the features),
$$
\boldsymbol{\Sigma} = \begin{bmatrix}\noiseStd^2_{1} & 0 & 0 & 0\\
0 & \noiseStd^2_{2} & 0 & 0\\
                                     0 & 0 & \ddots &
0\\
                                     0 & 0 & 0 & \noiseStd^2_p\end{bmatrix}.
$$
For completeness, we could also add in a *mean* for the data vector
$\meanVector$, 
$$
\dataVector_{i, :} = \mappingMatrix \latentVector_{i, :} +
\meanVector + \noiseVector_{i, :}
$$
which would give our marginal
distribution for $\dataVector_{i, :}$ a mean $\meanVector$. However, the
maximum likelihood solution for $\meanVector$ turns out to equal the
empirical mean of the data,
$$
\meanVector = \frac{1}{\numData} \sum_{i=1}^\numData
\dataVector_{i, :},
$$
*regardless* of the form of the covariance, $\covarianceMatrix =
\mappingMatrix\mappingMatrix^\top + \boldsymbol{\Sigma}$. As a result it is very common
to simply preprocess the data and ensure it is zero mean. We will follow that
convention for this session.

The prior density over latent variables is
independent, and the likelihood is independent, that means that the marginal
likelihood here is also independent over the data points.
Factor analysis was developed mainly in psychology and the social sciences for
understanding personality and intelligence. [Charles
Spearman](http://en.wikipedia.org/wiki/Charles_Spearman) was concerned with the
measurements of "the abilities of man" and is credited with the earliest version
of factor analysis.

\section{Principal Component Analysis}

In 1933 [Harold
Hotelling](http://en.wikipedia.org/wiki/Harold_Hotelling) published on
*principal component analysis* the first mention of this approach [@Hotelling:analysis33]. Hotelling's
inspiration was to provide mathematical foundation for factor analysis methods
that were by then widely used within psychology and the social sciences. His
model was a factor analysis model, but he considered the noiseless 'limit' of
the model. In other words he took $\noiseStd^2_i \rightarrow 0$ so that he had
$$
\dataVector_{i, :} \sim \lim_{\noiseStd^2 \rightarrow 0} \gaussianSamp{\zerosVector}{\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye}.
$$
The paper had two
unfortunate effects. Firstly, the resulting model is no longer valid
probablistically, because the covariance of this Gaussian is 'degenerate'.
Because $\mappingMatrix\mappingMatrix^\top$ has rank of at most $q$ where $q<p$ (due to
the dimensionality reduction) the determinant of the covariance is zero, meaning
the inverse doesn't exist so the density,
$$
p(\dataVector_{i, :}|\mappingMatrix) =
\lim_{\noiseStd^2 \rightarrow 0} \frac{1}{(2\pi)^\frac{p}{2}
|\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye|^{-1}}
\exp\left(-\frac{1}{2}\dataVector_{i, :}\left[\mappingMatrix\mappingMatrix^\top+ \noiseStd^2
\eye\right]^{-1}\dataVector_{i, :}\right),
$$
is *not* valid for $q<p$
(where $\mappingMatrix\in \Re^{p\times q}$). This mathematical consequence is a
probability density which has no 'support' in large regions of the space for
$\dataVector_{i, :}$. There are regions for which the probability of
$\dataVector_{i, :}$ is zero. These are any regions that lie off the hyperplane
defined by mapping from $\latentVector$ to $\dataVector$ with the matrix
$\mappingMatrix$. In factor analysis the noise corruption, $\noiseVector$,
allows for points to be found away from the hyperplane. In Hotelling's PCA the
noise variance is zero, so there is only support for points that fall precisely
on the hyperplane. Secondly, Hotelling explicity chose to rename factor analysis
as principal component analysis, arguing that the factors social scientist
sought were different in nature to the concept of a mathematical factor. This
was unfortunate because the factor loadings, $\mappingMatrix$ can also be seen as
factors in the mathematical sense because the model Hotelling defined is a
Gaussian model with covariance given by $\covarianceMatrix = \mappingMatrix\mappingMatrix^\top$
so $\mappingMatrix$ is a *factor* of the covariance in the mathematical sense, as
well as a factor loading. 

However, the paper had one great advantage over
standard approaches to factor analysis. Despite the fact that the model was a
special case that is subsumed by the more general approach of factor analysis it
is this special case that leads to a particular algorithm, namely that the
factor loadings (or principal components as Hotelling referred to them) are
given by an *eigenvalue decomposition* of the empirical covariance matrix.

\newslide{Computation of the Marginal Likelihood}

$$
\dataVector_{i,:}=\mappingMatrix\latentVector_{i,:}+\noiseVector_{i,:},\quad \latentVector_{i,:} \sim \gaussianSamp{\zerosVector}{\eye}, \quad \noiseVector_{i,:} \sim \gaussianSamp{\zerosVector}{\noiseStd^{2}\eye}
$$

$$
\mappingMatrix\latentVector_{i,:} \sim \gaussianSamp{\zerosVector}{\mappingMatrix\mappingMatrix^\top}
$$

$$
\mappingMatrix\latentVector_{i, :} + \noiseVector_{i, :} \sim \gaussianSamp{\zerosVector}{\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye}
$$

\newslide{Linear Latent Variable Model II}
  **Probabilistic PCA Max. Likelihood Soln**
(@Tipping:probpca99)

%\includegraphics<1>[width=0.25\textwidth]{../../../gplvm/tex/diagrams/ppcaGraph}
\begin{tikzpicture}
        
      % Define nodes
      \node[obs]
(Y) {$\dataMatrix$};
      \node[const, above=of Y] (W) {$\mappingMatrix$};
\node[const, right=1cm of Y]            (sigma) {$\dataStd^2$};
      
      %
Connect the nodes
      \edge {W,sigma} {Y} ; %
    \end{tikzpicture}

$$p\left(\dataMatrix|\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i, :}}{\zerosVector}{\mappingMatrix\mappingMatrix^{\top}+\noiseStd^{2}\eye}$$

\newslide{Linear Latent Variable Model II}
  
\slides{**Probabilistic PCA Max. Likelihood Soln** (@Tipping:probpca99)
  $$
  p\left(\dataMatrix|\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\zerosVector}{\covarianceMatrix},\quad \covarianceMatrix=\mappingMatrix\mappingMatrix^{\top}+\noiseStd^{2}\eye
  $$
  $$
  \log p\left(\dataMatrix|\mappingMatrix\right)=-\frac{\numData}{2}\log\left|\covarianceMatrix\right|-\frac{1}{2}\text{tr}\left(\covarianceMatrix^{-1}\dataMatrix^{\top}\dataMatrix\right)+\text{const.}
  $$
  If $\mathbf{U}_{q}$ are first $q$ principal eigenvectors of $n^{-1}\dataMatrix^{\top}\dataMatrix$ and the corresponding eigenvalues are $\boldsymbol{\Lambda}_{q}$,
  $$
  \mappingMatrix=\mathbf{U}_{q}\mathbf{L}\mathbf{R}^{\top},\quad\mathbf{L}=\left(\boldsymbol{\Lambda}_{q}-\noiseStd^{2}\eye\right)^{\frac{1}{2}}
  $$
  where $\mathbf{R}$ is an arbitrary rotation matrix.}


\addreading{@Rogers:book11}{Chapter 7 up to pg 249}



\subsection{Eigenvalue Decomposition}

Eigenvalue problems are widespreads in physics and
mathematics, they are often written as a matrix/vector equation but we prefer to
write them as a full matrix equation. In an eigenvalue problem you are looking
to find a matrix of eigenvectors, $\mathbf{U}$ and a *diagonal* matrix of
eigenvalues, $\boldsymbol{\Lambda}$ that satisfy the *matrix* equation
$$
\mathbf{A}\mathbf{U} = \mathbf{U}\boldsymbol{\Lambda}.
$$
where $\mathbf{A}$ is
your matrix of interest. This equation is not trivially solvable through matrix
inverse because matrix multiplication is not
[commutative](http://en.wikipedia.org/wiki/Commutative_property), so
premultiplying by $\mathbf{U}^{-1}$ gives
$$
\mathbf{U}^{-1}\mathbf{A}\mathbf{U}
= \boldsymbol{\Lambda}, 
$$
where we remember that $\boldsymbol{\Lambda}$ is a
*diagonal* matrix, so the eigenvectors can be used to *diagonalise* the matrix.
When performing the eigendecomposition on a Gaussian covariances,
diagonalisation is very important because it returns the covariance to a form
where there is no correlation between points. 

\subsection{Positive Definite}

We are
interested in the case where $\mathbf{A}$ is a covariance matrix, which implies
it is *positive definite*. A positive definite matrix is one for which the inner
product,
$$
\weightVector^\top \covarianceMatrix\weightVector
$$
is positive for *all* values
of the vector $\weightVector$ other than the zero vector. One way of creating a
positive definite matrix is to assume that the symmetric and positive definite
matrix $\covarianceMatrix\in \Re^{p\times p}$ is factorised into, $\mathbf{A}in
\Re^{p\times p}$, a *full rank* matrix, so that
$$
\covarianceMatrix = \mathbf{A}^\top
\mathbf{A}.
$$
This ensures that $\covarianceMatrix$ must be positive definite because
$$
\weightVector^\top \covarianceMatrix\weightVector=\weightVector^\top
\mathbf{A}^\top\mathbf{A}\weightVector 
$$
and if we now define a new *vector*
$\mathbf{b}$ as
$$
\mathbf{b} = \mathbf{A}\weightVector
$$
we can now rewrite as
$$
\weightVector^\top \covarianceMatrix\weightVector = \mathbf{b}^\top\mathbf{b} = \sum_{i}
b_i^2
$$
which, since it is a sum of squares, is positive or zero. The
constraint that $\mathbf{A}$ must be *full rank* ensures that there is no vector
$\weightVector$, other than the zero vector, which causes the vector $\mathbf{b}$
to be all zeros.

\writeassignment{If $\covarianceMatrix=\mathbf{A}^\top \mathbf{A}$ then
express $c_{i,j}$, the value of the element at the $i$th row and the $j$th
column of $\covarianceMatrix$, in terms of the columns of $\mathbf{A}$. Use this to
show that (i) the matrix is symmetric and (ii) the matrix has positive elements
along its diagonal.}{15}


\subsection{Eigenvectors of a Symmetric Matric}

Symmetric matrices have *orthonormal* eigenvectors. This means that
$\mathbf{U}$ is an
[orthogonal matrix](http://en.wikipedia.org/wiki/Orthogonal_matrix),
$\mathbf{U}^\top\mathbf{U} = \eye$. This implies that $\mathbf{u}_{:,
i} ^\top \mathbf{u}_{:, j}$ is equal to 0 if $i\neq j$ and 1 if $i=j$.

\endif
