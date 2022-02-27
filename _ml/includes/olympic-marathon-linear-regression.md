\ifndef{olympicMarathonLinearRegression}
\define{olympicMarathonLinearRegression}

\editme

talk-macros.gpp}atasets/includes/olympic-marathon-data.md}

\subsection{Running Example: Olympic Marathons}

\notes{Note that `x` and `y` are not `pandas` data frames for this example, they are just arrays of dimensionality $\numData\times 1$, where $\numData$ is the number of data.}

\notes{The aim of this lab is to have you coding linear regression in python. We will do it in two ways, once using iterative updates (coordinate ascent) and then using linear algebra. The linear algebra approach will not only work much better, it is also easy to extend to multiple input linear regression and *non-linear* regression using basis functions.}

\subsection{Maximum Likelihood: Iterative Solution}

\notes{Now we will take the maximum likelihood approach we derived in the lecture to fit a line, $\dataScalar_i=m\inputScalar_i + c$, to the data you've plotted. We are trying to minimize the error function:}
$$
\errorFunction(m, c) =  \sum_{i=1}^\numData(\dataScalar_i-m\inputScalar_i-c)^2
$$
\notes{with respect to $m$, $c$ and $\sigma^2$. We can start with an initial guess for $m$,}

\code{m = -0.4
c = 80}

\notes{Then we use the maximum likelihood update to find an estimate for the offset, $c$.}

\endif
