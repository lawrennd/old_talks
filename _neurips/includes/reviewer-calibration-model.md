\ifndef{reviewerCalibrationModel}
\define{reviewerCalibrationModel}

\editme

\subsection{Reviewer Calibration Model}

\notes{In this note book we deal with reviewer calibration. Our assumption is
that the score from the $j$th reviwer for the $i$th paper is given by}
$$
y_{i,j} = f_i + b_j + \epsilon_{i, j}
$$
\notes{where $f_i$ is the 'objective quality' of paper $i$ and $b_j$ is an
offset associated with reviewer $j$. $\epsilon_{i,j}$ is a subjective
quality estimate which reflects how a specific reviewer's opinion
differs from other reviewers (such differences in opinion may be due to
differing expertise or perspective). The underlying 'objective
quality' of the paper is assumed to be the same for all reviewers and
the reviewer offset is assumed to be the same for all papers.}

\notes{If we have $n$ papers and $m$ reviewers then this implies $n$ + $m$ +
$nm$ values need to be estimated. Naturally this is too many, and we can
start by assuming that the subjective quality is drawn from a normal
density with variance $\sigma^2$ $$
\epsilon_{i, j} \sim N(0, \sigma^2 \mathbf{I})
$$ which reduces us to $n$ + $m$ + 1 parameters. Further we can assume
that the objective quality is also normally distributed with mean $\mu$
and variance $\alpha_f$, $$
f_i \sim N(\mu, \alpha_f)
$$ this now reduces us to $m$+3 parameters. However, we only have
approximately $4m$ observations (4 papers per reviewer) so parameters
may still not be that well determined (particularly for those reviewers
that have only one review). We therefore, finally, assume that reviewer
offset is normally distributed with zero mean, $$
b_j \sim N(0, \alpha_b),
$$ leaving us only four parameters: $\mu$, $\sigma^2$, $\alpha_f$ and
$\alpha_b$. Combined together these three assumptions imply that $$
\mathbf{y} \sim N(\mu \mathbf{1}, \mathbf{K})
$$ where $\mathbf{y}$ is a vector of stacked scores $\mathbf{1}$ is the
vector of ones and the elements of the covariance function are given by
$$
k(i,j; k,l) = \delta_{i,k} \alpha_f + \delta_{j,l} \alpha_b + \delta_{i, k}\delta_{j,l} \sigma^2
$$ where $i$ and $j$ are the index of first paper and reviewer and $k$
and $l$ are the index of second paper and reviewer. The mean is easily
estimated by maximum likelihood, and is given as the mean of all scores.}

\notes{It is convenient to reparameterize slightly into an overall scale
$\alpha_f$, and normalized variance parameters, $$
k(i,j; k,l) = \alpha_f(\delta_{i,k}  + \delta_{j,l} \frac{\alpha_b}{\alpha_f} + \delta_{i, k}\delta_{j,l} \frac{\sigma^2}{\alpha_f})
$$ which we rewrite to give two ratios: offset/signal ratio,
$\hat{\alpha}_b$ and noise/signal $\hat{\sigma}^2$ ratio. $$
k(i,j; k,l) = \alpha_f(\delta_{i,k}  + \delta_{j,l} \hat{\alpha}_b + \delta_{i, k}\delta_{j,l} \hat{\sigma}^2)
$$ The advantage of this parameterization is it allows us to optimize
$\alpha_f$ directly (with a fixed point equation) and it will be very
well determined. This leaves us with two free parameters, that we can
explore on the grid. It is in these parameters that we expect the
remaining underdetermindness of the model. We expect $\alpha_f$ to be
well determined because the negative log likelihood is now $$
\frac{|\mathbf{y}|}{2}\log\alpha_f + \frac{1}{2}\log  \left|\hat{\mathbf{K}}\right| + \frac{1}{2\alpha_f}\mathbf{y}^\top \hat{\mathbf{K}}^{-1} \mathbf{y}
$$ where $|\mathbf{y}|$ is the length of $\mathbf{y}$ (i.e. the number
of reviews) and $\hat{\mathbf{K}}=\alpha_f^{-1}\mathbf{K}$ is the scale
normalised covariance. This negative log likelihood is easily minimized
to recover $$
\alpha_f = \frac{1}{|\mathbf{y}|} \mathbf{y}^\top \hat{\mathbf{K}}^{-1} \mathbf{y}
$$ A Bayesian analysis of this parameter is possible with gamma priors,
but it would merely shows that this parameter is extremely well
determined (the degrees of freedom parameter of the associated
Student-$t$ marginal likelihood scales will the number of reviews, which
will be around $|\mathbf{y}| \approx 6,000$ in our case.}

\notes{So, we propose to proceed as follows. Set the mean from the reviews
($\mu$) and then choose a two dimensional grid of parameters for
reviewer offset and diversity. For each parameter choice, optimize to
find $\alpha_f$ and then evaluate the liklihood. Worst case this will
require us inverting $\hat{\mathbf{K}}$, but if the reviewer paper
groups are disconnected, it can be done a lot quicker. Next stage is to
load in the reviews for analysis.}

\endif
