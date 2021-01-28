\ifndef{theBootstrap}
\define{theBootstrap}

\editme


\subsection{The Bootstrap}

\notes{Bootstrap sampling [@Efron:bootstrap79] is an approach to assessing the sensitivity of the model to different variations on a data set. In an ideal world, we'd like to be able to look at different realisations from the original data generating distribution $\mathbb{P}(\dataScalar, \inputVector)$, but this is not available to us.}

\notes{In bootstrap sampling, we take the sample we have,}
$$
\dataVector, \inputMatrix \sim \mathbb{P}(\dataScalar, \inputVector)
$$
\notes{and resample from that data, rather than from the true distribution. So we have a new data set, $\hat{\dataVector}$, $\hat{\inputMatrix}$ which is sampled from the original *with* replacement.}

\newslide{Resample Dataset}

\slides{```python
def bootstrap(X):
    "Return a bootstrap sample from a data set."
    n = X.shape[0]
    ind = np.random.choice(n, n, replace=True) # Sample randomly with replacement.
    return X[ind, :]
```}

\setupcode{import numpy as np}
	
\code{def bootstrap(X):
    "Return a bootstrap sample from a data set."
    n = X.shape[0]
    ind = np.random.choice(n, n, replace=True) # Sample randomly with replacement.
    return X[ind, :]  }
	

\endif
