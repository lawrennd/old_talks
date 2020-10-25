---
week: 7
title: "Dimensionality Reduction: Latent Variable Modelling"
abstract: "In this lecture we turn to *unsupervised learning*. Specifically, we introduce the idea of a latent variable model. Latent variable models are a probabilistic perspective on unsupervised learning which lead to dimensionality reduction algorithms. "
youtube: 0mtK2_rc0IY
---

\include{talk-macros.tex}

\include{_mlai/includes/mlai-notebook-setup.md}

\subsection{Review}

* Last time: Looked at Bayesian Regression.
* Introduced priors and marginal likelihoods.
* This time: Unsupervised Learning

\newslide{Unsupervised Learning}

* Supervised learning is learning where each data has a label (e.g. regression output)
* In unsupervised learning we have no labels for the data.
* Often thought of as structure discovery.
  * Finding features in the data
  * Exploratory data analysis

\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=(5,5))

num_centres = 20
num_data = 200
centres = np.random.normal(size=(num_centres, 2))
w = np.random.normal(size=(num_centres, 2))*0.1
alloc = np.random.randint(0, num_centres, size=(num_data))
sigma = np.random.normal(size=(num_centres, 1))*0.05
epsilon = np.random.normal(size=(num_data,2))*sigma[alloc, :]

Y = w[alloc, :]*np.random.normal(size=(num_data, 1)) + centres[alloc, :] + epsilon

ax.plot(Y[:, 0], Y[:, 1], 'rx')
ax.set_xlabel('$y_1$', fontsize=20)
ax.set_ylabel('$y_2$', fontsize=20)

mlai.write_figure(\diagramsDir/ml/cluster_data00.svg')
pi_vals = np.linspace(-np.pi, np.pi, 200)[:, None]
for i in range(num_centres):
    ax.plot(centres[i, 0], centres[i, 1], 'o', markersize=5, color=[0, 0, 0], linewidth=2)
    x = np.hstack([np.sin(pi_vals), np.cos(pi_vals)])
    L = np.linalg.cholesky(np.outer(w[i, :],w[i, :]) + sigma[i]**2*np.eye(2))
    el = np.dot(x, L.T)
    ax.plot(centres[i, 0] + el[:, 0], centres[i, 1] + el[:, 1], linewidth=2, color=[0,0,0])
mlai.write_figure(\diagramsDir/ml/cluster_data01.svg')}

\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_plots('cluster_data{counter:0>2}.svg', directory='\writeDiagramsDir/ml', counter=(0, 1))}

\newslide{Clustering}

* One common approach, not deeply covered in this course. 
* Associate each data point, $\dataVector_{i, :}$ with one of $k$ different discrete groups.
* For example:
  * Clustering animals into discrete groups. Are animals discrete or continuous?
  * Clustering into different different *political* affiliations.
* Humans do seem to like clusters:
  * Very useful when interacting with biologists.
* Subtle difference between clustering and *vector quantisation*

\newslide{Trying to Teach About Infinity}

* Little anecdote.

\newslide{Clustering and Vector Quantisation}

* To my mind difference is in clustering there should be a reduction in data density between samples.
* This definition is not universally applied.
* For today's purposes we merge them:
  * Determine how to allocate each point to a group and *harder* total number of groups.

\newslide{$k$-means Clustering}

* Simple algorithm for allocating points to groups. 
* *Require*: Set of $k$ cluster centres & assignment of each points to a cluster.
1. Initialize cluster centres as randomly selected data points.
    2. Assign each data point to *nearest* cluster centre.
    3. Update each cluster centre by setting it to the mean of assigned data points.
    4. Repeat 2 and 3 until cluster allocations do not change.

\newslide{Objective Function}

* This minimizes the objective
  $$
  E=\sum_{j=1}^K \sum_{i\ \text{allocated to}\ j}  \left(\dataVector_{i, :} - \meanVector_{j, :}\right)^\top\left(\dataVector_{i, :} - \meanVector_{j, :}\right)
  $$
  *i.e.* it minimizes thesum of Euclidean squared distances betwen points and their associated centres.
* The minimum is *not* guaranteed to be *global* or *unique*.
* This objective is a non-convex optimization problem.

\setupplotcode{import mlai
import numpy as np}

\plotcode{def write_plot(counter, caption):
    filebase = '\writeDiagramsDir/ml/kmeans_clustering_{counter:0>3}'.format(counter=counter)
    plt.savefig(filebase + '.svg')
    f = open(filebase + '.tex', 'w')
    f.write(caption)
    f.close()
    
fig, ax = plt.subplots(figsize=(5,5))
fontsize = 20

num_clust_points = 30

Y = np.vstack([np.random.normal(size=(num_clust_points, 2)) + 2.5,
       np.random.normal(size=(num_clust_points, 2)) - 2.5,
       np.random.normal(size=(num_clust_points, 2)) + np.array([2.5, -2.5])])

centre_inds = np.random.permutation(Y.shape[0])[:3]
centres = Y[centre_inds, :]

ax.cla()

ax.plot(Y[:, 0], Y[:, 1], '.', color=[0, 0, 0], markersize=10)
ax.set_xlabel('$y_1$')
ax.set_ylabel('$y_2$')
ax.set_title('Data')
counter=0
write_plot(counter, 'Data set to be analyzed. Initialize cluster centres.')
ax.plot(centres[:, 0], centres[:, 1], 'o', color=[0,0,0], linewidth=3, markersize=12)    
counter+=1
write_plot(counter, 'Allocate each point to the cluster with the nearest centre')
i = 0

for i in range(6):
    dist_mat = ((Y[:, :, None] - centres.T[None, :, :])**2).sum(1)
    ind = dist_mat.argmin(1)
    ax.cla()
    ax.plot(Y[ind==0, 0], Y[ind==0, 1], 'x', color= [1, 0, 0], markersize=10)
    ax.plot(Y[ind==1, 0], Y[ind==1, 1], 'o', color=[0, 1, 0], markersize=10)
    ax.plot(Y[ind==2, 0], Y[ind==2, 1], '+', color=[0, 0, 1], markersize=10)
    c = ax.plot(centres[:, 0], centres[:, 1], 'o', color=[0,0, 0], markersize=12, linewidth=3)
    ax.set_xlabel('$y_1$',fontsize=fontsize)
    ax.set_ylabel('$y_2$',fontsize=fontsize)
    ax.set_title('Iteration ' + str(i))
    counter+=1
    write_plot(counter, 'Update each centre by setting to the mean of the allocated points.')
    for j in range(centres.shape[0]):
          centres[j, :] = np.mean(Y[ind==j, :], 0)
    c[0].set_data(centres[:, 0], centres[:, 1])
    counter+=1
    mlai.write_figure(\diagramsDir/ml/kmeans_clustering_{counter:0>3}.svg'.format(counter=counter))
    write_plot(counter, 'Allocate each data point to the nearest cluster centre.')}

\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_plots('kmeans_clustering_{counter:0>3}.svg', directory='\writeDiagramsDir/ml', 
                            text_top='kmeans_clustering_{counter:0>3}.tex', counter=(0, 13))}

\newslide{Other Clustering Approaches}

* Spectral clustering (@Shi:normalized00,@Ng:spectral02)
  * Allows clusters which aren't convex hulls.
* Dirichlet process
  * A probabilistic formulation for a clustering algorithm that is *non-parametric*. 
  * Loosely speaking it allows infinite
clusters
  * In practice useful for dealing with previously unknown species (e.g. a "Black Swan Event").

\newslide{High Dimensional Data}

* USPS Data Set Handwritten Digit
* 3648 dimensions (64 rows, 57 columns)
* Space contains much more than just this digit.

\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai}
\plotcode{fig, ax = plt.subplots(figsize=(5,5))

six_image = mlai.load_pgm('br1561_6.3.pgm', directory ='\writeDiagramsDir/ml')
rows = six_image.shape[0]
col = six_image.shape[1]
      
ax.imshow(six_image,interpolation='none').set_cmap('gray')
mlai.write_figure(\diagramsDir/ml/dem_six000.png')
for i in range(3):
    rand_image = np.random.rand(rows, col)<((six_image>0).sum()/float(rows*col))
    ax.imshow(rand_image,interpolation='none').set_cmap('gray')
    mlai.write_figure(\diagramsDir/ml/dem_six{i:0>3}.png'.format(i=i+1))}

\setupdisplaycode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('dem_six{counter:0>3}.png', directory='\writeDiagramsDir/ml', counter=IntSlider(0, 0, 3, 1))}

\newslide{USPS Samples}

* Even if we sample every nanonsecond from now until end of universe you won't see original six!

\newslide{Simple Model of Digit}

* Rotate a prototype 

\setupcode{from scipy.misc import imrotate}

\code{six_image = np.hstack([np.zeros((rows, 3)), six_image, np.zeros((rows, 4))])
dim_one = np.asarray(six_image.shape)
angles = range(360)
i = 0
Y = np.zeros((len(angles), np.prod(dim_one)))
for angle in angles:
    rot_image = imrotate(six_image, angle, interp='nearest')
    dim_two = np.asarray(rot_image.shape)
    start = [int(round((dim_two[0] - dim_one[0])/2)), int(round((dim_two[1] - dim_one[1])/2))]
    crop_image = rot_image[start[0]+np.array(range(dim_one[0])), start[1]+np.array(range(dim_one[1]))]
    Y[i, :] = crop_image.flatten()}

\displaycode{pods.notebook.display_plots('dem_six_rotate{counter:0>3}.png', directory='\writeDiagramsDir/ml', counter=(0, 3))}

\newslide{Low Dimensional Manifolds}

* Pure rotation is too simple
  * In practice data may undergo several distortions.
* For high dimensional data with *structure*:
  * We expect fewer distortions than dimensions;
  * Therefore we expect the data to live on a lower dimensional manifold.
  * Conclusion: Deal with high dimensional data by looking for a lower dimensional non-linear embedding.

\newslide{Principal Component Analysis}

* PCA (@Hotelling:analysis33) is a linear embedding.
* Today its presented as:
  * Rotate to find 'directions' in data with maximal variance.
  * How do we find these directions?
* Algorithmically we do this by diagonalizing the sample covariance matrix 
  $$
  \mathbf{S}=\frac{1}{\numData}\sum_{i=1}^\numData \left(\dataVector_{i, :}-\meanVector\right)\left(\dataVector_{i, :} - \meanVector\right)^\top
  $$

\newslide{Principal Component Analysis}

* Find directions in the data, $\latentVector = \mathbf{U}\dataVector$, for which variance is maximized.

\newslide{Lagrangian}

* Solution is found via constrained optimisation (which uses [Lagrange multipliers](https://en.wikipedia.org/wiki/Lagrange_multiplier)):
  $$
  L\left(\mathbf{u}_{1},\lambda_{1}\right)=\mathbf{u}_{1}^{\top}\mathbf{S}\mathbf{u}_{1}+\lambda_{1}\left(1-\mathbf{u}_{1}^{\top}\mathbf{u}_{1}\right)
  $$

* Gradient with respect to $\mathbf{u}_{1}$
  $$\frac{\text{d}L\left(\mathbf{u}_{1},\lambda_{1}\right)}{\text{d}\mathbf{u}_{1}}=2\mathbf{S}\mathbf{u}_{1}-2\lambda_{1}\mathbf{u}_{1}$$
  rearrange to form
  $$\mathbf{S}\mathbf{u}_{1}=\lambda_{1}\mathbf{u}_{1}.$$
  Which is known as an [*eigenvalue problem*](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors).
* Further directions that are *orthogonal* to the first can also be shown to be eigenvectors of the covariance.

\newslide{Linear Dimensionality Reduction}

* Represent data, $\dataMatrix$, with a lower dimensional set of latent variables $\latentMatrix$.
* Assume a linear relationship of the form
  $$
  \dataVector_{i,:}=\mappingMatrix\latentVector_{i,:}+\noiseVector_{i,:},
  $$
  where
  $$
  \noiseVector_{i,:} \sim \gaussianSamp{\zerosVector}{\noiseStd^2\eye}
  $$

\newslide{Linear Latent Variable Model}

**Probabilistic PCA**

* Define *linear-Gaussian relationship* between latent variables and data.
* **Standard** Latent variable approach:
  * Define Gaussian prior over *latent space*, $\latentMatrix$.
* Integrate out *latent variables*.

\begin{tikzpicture}
          
          % Define nodes
          \node[obs]
(Y) {$\dataMatrix$};
          \node[const, above=of Y, xshift=-1.2cm] (W)
{$\mappingMatrix$};
          \node[latent, above=of Y, xshift=1.2cm]  (X)
{$\latentMatrix$};
          \node[const, right=1cm of Y]            (sigma)
{$\dataStd^2$};
          
          % Connect the nodes
          \edge
{X,W,sigma} {Y} ; %
          
\end{tikzpicture}

$$
p\left(\dataMatrix|\latentMatrix,\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\mappingMatrix\latentVector_{i,:}}{\noiseStd^2\eye}
$$

$$
p\left(\latentMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\latentVector_{i,:}}{\zerosVector}{\eye}
$$

$$
p\left(\dataMatrix|\mappingMatrix\right)=\prod_{i=1}^{\numData}\gaussianDist{\dataVector_{i,:}}{\zerosVector}{\mappingMatrix\mappingMatrix^{\top}+\noiseStd^{2}\eye}
$$

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
  
**Probabilistic PCA Max. Likelihood Soln** (@Tipping:probpca99)
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
  where $\mathbf{R}$ is an arbitrary rotation matrix.


\addreading{@Rogers:book11}{Chapter 7 up to pg 249}

\reading

\notes{So far in our classes we have focussed mainly on regression
problems, which are examples of supervised learning. We have considered the
relationship between the likelihood and the objective function and we have shown
how we can find paramters by maximizing the likelihood (equivalent to minimizing
the objective function) and in the last session we saw how we can *marginalize*
the parameters in a process known as Bayesian inference.}

\notes{Now we are going to
turn to a different form of learning, commonly known as *unsupervised* learning.
In unsupervised learning our data isn't necessarily labelled in any form, but we
want models that give us a better understanding of the data. We've actually seen
an example of this already with \refnotes{*matrix factorization* for collaborative
filtering}{matrix-factorization},  which we introduces in the context of *objective
functions*. Now we will introduce a more probabilistic approach to such models,
specifically we are interested in *latent variable* modelling.}

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

\include{_dimred/includes/probabilistic-pca.md}

\include{_dimred/includes/mocap-ppca.md}
\include{_dimred/includes/robot-wireless-ppca.md}


\section{Relationship to Matrix Factorization}

We can use the robot naviation example
to realise that PCA (and factor analysis) are very reminiscient of the \refnotes{*matrix
factorization* example}{matrix-factorization} that we used for introducing objective
functions. In that system we used slightly different notation, $\mathbf{u}_{i,
:}$ for *user* location in our metaphorical library and $\mathbf{v}_{j, :}$ for
*item* location in our metaphorical library. To see how these systems are
somewhat analagous, now let us think about the user as the robot and the items
as the wifi access points. We can plot the relative location of both. This
process is known as "SLAM": simultaneous *localisation* and *mapping*. A latent
variable model of the type we have developed is one way of performing SLAM. We
have an estimate of the *landmarks* in the system (in this case WIFI access
points) and we have an estimate of the robot position. These are analagous to
the estimate of the user's position and the estimate of the items positions in
the library. In the matrix factorisation example users are informing us what
items they are 'close' to by expressing their preferences, in the robot
localization example the robot is informing us what access point it is close to
by measuring signal strength.

From a personal perspective, I find this analogy
quite comforting. I think it is very arguable that one of the mechanisms through
which we (as humans) may have developed higher reasoning is through the need to
navigate around our environment, identifying landmarks and associating them with
our search for food. If such a system were to exist, the idea that it could be
readily adapted to other domains such as categorising the nature of the
different foodstuffs we were able to forage is intriguing. 

From an algorithmic
perspective, we also can now realise that matrix factorization and latent
variable modelling are effectively the same thing. The only difference is the
objective function and our probabilistic (or lack of probabilistic) treatment of
the variables. But the prediction functoin for both systems,
$$
f_{i, j} =
\mathbf{u}_{i, :}^\top \mathbf{v}_{j, :} 
$$
for matrix factorization or
$$
f_{i, j} = \latentVector_{i, :}^\top \weightVector_{j, :} 
$$
for probabilistic PCA
and factor analysis are the same.

\section{Other Interpretations of PCA: Separating Model and Algorithm}

Since Hotelling first introduced his perspective on factor
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
The singular value decomposition of a data set has the following form,
$$
\dataMatrix = \mathbf{V} \boldsymbol{\Lambda} \mathbf{U}^\top
$$
where
$\mathbf{V}\in\Re^{n\times n}$ and $\mathbf{U}^\in \Re^{p\times p}$ are square
orthogonal matrices and $\mathbf{\Lambda}^{n \times p}$ is zero apart from its
first $p$ diagonal entries. Singularvalue decomposition gives a diagonalisation
of the covariance matrix, because under the SVD we have
$$
\dataMatrix^\top\dataMatrix =
\mathbf{U}\boldsymbol{\Lambda}\mathbf{V}^\top\mathbf{V} \boldsymbol{\Lambda}
\mathbf{U}^\top = \mathbf{U}\boldsymbol{\Lambda}^2 \mathbf{U}^\top
$$
where
$\boldsymbol{\Lambda}^2$ is now the eigenvalues of the covariane matrix and
$\mathbf{U}$ are the eigenvectors. So performing the SVD can simply be seen as
another approach to determining the principal components.

\subsection{Separating Model and Algorithm}

I've given a fair amount of personal thought to this situation and my
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
[non-linearises the dual probabilistic PCA](http://jmlr.org/papers/volume6/lawrence05a/lawrence05a.pdf) [@Lawrence:pnpca05].

My conclusion is that when you are doing machine learning you should
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
conflation.

\section{PCA in Practice}

Principal component analysis is so effective in practice that there
has almost developed a mini-industry in renaming the method itself
(which is ironic, given its origin).  In particular
[Latent Semantic Indexing](http://en.wikipedia.org/wiki/Latent_semantic_indexing)
in text processing is simply PCA on a particular representation of the
term frequencies of the document. There is a particular fad to rename
the eigenvectors after the nature of the data you are examining,
perhaps initially triggered by
[Turk and Pentland's](http://www.face-rec.org/algorithms/PCA/jcn.pdf)
paper on eigenfaces, but also with
[eigenvoices](https://wiki.inf.ed.ac.uk/twiki/pub/CSTR/ListenSemester1_2007_8/kuhn-
junqua-eigenvoice-icslp1998.pdf) and
[eigengenes](http://www.biomedcentral.com/1752-0509/1/54). This seems
to be an instantiation of a wider, and hopefully subconcious, tendency
in academia to attempt to differentiate one idea from the same idea in
related fields in order to emphasise the novelty. The unfortunate
result is somewhat of a confusing literature for relatively simple
model. My recommendations would be as follows.  If you have
multivariate data, applying some form of principal component would
seem to be a very good idea as a first step. Even if you intend to
later perform classification or regression on your data, it can give
you understanding of the structure of the underlying data and help you
to develop your intuitions about the nature of your data. Intelligent
plotting and interaction with your data is always a good think, and
for high dimensional data that means that you need some way of
visualisation, PCA is typically a good starting point.

\section{Marginal Likelihood}

We have developed the posterior density over the latent variables
given the data and the parameters, and due to symmetries in the underlying
prediction function, it has a very similar form to its sister density, the
posterior of the weights given the data from Bayesian regression. Two key
differences are as follows. If we were to do a Bayesian multiple output
regression we would find that the marginal likelihood of the data is independent
across the features and correlated across the data,
$$
p(\dataMatrix|\latentMatrix)
= \prod_{j=1}^p \gaussianDist{\dataVector_{:, j}}{\zerosVector}{
\alpha\latentMatrix\latentMatrix^\top + \noiseStd^2 \eye}
$$
where $\dataVector_{:,
j}$ is a column of the data matrix and the independence is across the
*features*, in probabilistic PCA the marginal likelihood has the form,
$$
p(\dataMatrix|\mappingMatrix) = \prod_{i=1}^\numData \gaussianDist{\dataVector_{i,
:}}{\zerosVector}{\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye}
$$
where
$\dataVector_{i, :}$ is a row of the data matrix $\dataMatrix$ and the
independence is across the data points.

\section{Computation of the Log Likelihood}

The quality of the model can be assessed using the log likelihood of this
Gaussian form.
$$
\log p(\dataMatrix|\mappingMatrix) = -\frac{\numData}{2} \log \left|
\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye \right| -\frac{1}{2}
\sum_{i=1}^\numData \dataVector_{i, :}^\top \left(\mappingMatrix\mappingMatrix^\top + \noiseStd^2
\eye\right)^{-1} \dataVector_{i, :} +\text{const}
$$
but this can be computed more rapidly by exploiting the low rank form
of the covariance covariance, $\covarianceMatrix =
\mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye$ and the fact
that $\mappingMatrix = \mathbf{U}\mathbf{L}\mathbf{R}^\top$.
Specifically, we first use the decomposition of $\mappingMatrix$ to
write:
$$
-\frac{\numData}{2} \log \left| \mappingMatrix\mappingMatrix^\top + \noiseStd^2 \eye \right|
= -\frac{\numData}{2} \sum_{i=1}^q \log (\ell_i^2 + \noiseStd^2) - \frac{n(p-q)}{2}\log
\noiseStd^2,
$$
where $\ell_i$ is the $i$th diagonal element of $\mathbf{L}$.
Next, we use the [Woodbury matrix
identity](http://en.wikipedia.org/wiki/Woodbury_matrix_identity) which allows us
to write the inverse as a quantity which contains another inverse in a smaller
matrix:
$$
(\noiseStd^2 \eye + \mappingMatrix\mappingMatrix^\top)^{-1} =
\noiseStd^{-2}\eye-\noiseStd^{-4}\mappingMatrix{\underbrace{(\eye+\noiseStd^{-2}\mappingMatrix^\top\mappingMatrix)}_{\covarianceMatrix_x}}^{-1}\mappingMatrix^\top
$$
So, it turns out that the original inversion of the $p \times p$ matrix can
be done by forming a quantity which contains the inversion of a $q \times q$
matrix which, moreover, turns out to be the quantity $\covarianceMatrix_x$ of the
posterior.

Now, we put everything together to obtain:
$$
\log p(\dataMatrix|\mappingMatrix) = -\frac{\numData}{2} \sum_{i=1}^q
\log (\ell_i^2 + \noiseStd^2)
- \frac{n(p-q)}{2}\log \noiseStd^2 - \frac{1}{2} \trace{\dataMatrix^\top \left(
\noiseStd^{-2}\eye-\noiseStd^{-4}\mappingMatrix \covarianceMatrix_x
\mappingMatrix^\top \right) \dataMatrix} + \text{const},
$$
where we used the fact that a scalar sum can be written as
$\sum_{i=1}^\numData \dataVector_{i,:}^\top \kernelMatrix
\dataVector_{i,:} = \trace{\dataMatrix^\top \kernelMatrix
\dataMatrix}$, for any matrix $\kernelMatrix$ of appropriate
dimensions. We now use the properties of the trace
$\trace{\mathbf{A}+\mathbf{B}}=\trace{\mathbf{A}}+\trace{\mathbf{B}}$
and $\trace{c \mathbf{A}} = c \trace{\mathbf{A}}$, where $c$ is
a scalar and $\mathbf{A},\mathbf{B}$ matrices of compatible
sizes. Therefore, the final log likelihood takes the form:
$$
\log p(\dataMatrix|\mappingMatrix) = -\frac{\numData}{2}
\sum_{i=1}^q \log (\ell_i^2 + \noiseStd^2) - \frac{\numData(p-q)}{2}\log \noiseStd^2 -
\frac{\noiseStd^{-2}}{2} \trace{\dataMatrix^\top \dataMatrix}
+\frac{\noiseStd^{-4}}{2} \trace{\mathbf{B}\covarianceMatrix_x\mathbf{B}^\top} +
\text{const}
$$
where we also defined $\mathbf{B}=\dataMatrix^\top\mappingMatrix$.
Finally, notice that
$\trace{\dataMatrix\dataMatrix^\top}=\trace{\dataMatrix^\top\dataMatrix}$ can
be computed faster as the sum of all the elements of
$\dataMatrix\circ\dataMatrix$, where $\circ$ denotes the element-wise (or
[Hadamard](http://en.wikipedia.org/wiki/Hadamard_product_(matrices)) product.

\subsection{Reconstruction of the Data}

Given any posterior projection of a data point,
we can replot the original data as a function of the input space. 

We will now try to reconstruct the motion capture figure form some different places in the latent plot.

\writeassignment{Project the motion capture data onto its principal components, and then use the *mean posterior estimate* to reconstruct the data from the latent variables at the data points. Use two latent dimensions. What is the sum of squares error for the reconstruction?}{25}

\subsection{Other Data Sets to Explore}

Below there are a few other data sets from `pods` you might want to explore with PCA. Both of them have $p$>$n$ so you need to consider how to do the larger eigenvalue probleme efficiently without large demands on computer memory.

The data is actually quite high dimensional, and solving the eigenvalue problem in the high dimensional space can take some time. At this point we turn to a neat trick, you don't have to solve the full eigenvalue problem in the $\dataDim\times \dataDim$ covariance, you can choose instead to solve the related eigenvalue problem in the $\numData \times \numData$ space, and in this case $\numData=200$ which is much smaller than $\dataDim$.

The original eigenvalue problem has the form
$$
\dataMatrix^\top\dataMatrix \mathbf{U} = \mathbf{U}\boldsymbol{\Lambda}
$$
But if we premultiply by $\dataMatrix$ then we can solve,
$$
\dataMatrix\dataMatrix^\top\dataMatrix \mathbf{U} = \dataMatrix\mathbf{U}\boldsymbol{\Lambda}
$$
but it turns out that we can write
$$
\mathbf{U}^\prime = \dataMatrix \mathbf{U} \Lambda^{\frac{1}{2}}
$$
where $\mathbf{U}^\prime$ is an orthorormal matrix because
$$
\left.\mathbf{U}^\prime\right.^\top\mathbf{U}^\prime = \Lambda^{-\frac{1}{2}}\mathbf{U}\dataMatrix^\top\dataMatrix \mathbf{U} \Lambda^{-\frac{1}{2}}
$$
and since $\mathbf{U}$ diagonalises $\dataMatrix^\top\dataMatrix$, 
$$
\mathbf{U}\dataMatrix^\top\dataMatrix \mathbf{U} = \Lambda
$$
then 
$$
\left.\mathbf{U}^\prime\right.^\top\mathbf{U}^\prime = \eye
$$

\include{_dimred/includes/olivetti-eigenfaces.md}
\include{_dimred/includes/spellman-eigengenes.md}

