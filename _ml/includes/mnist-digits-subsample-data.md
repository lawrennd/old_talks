\ifndef{mnistDigitsSubsampleData}
\define{mnistDigitsSubsampleData}

\editme

\subsection{Subsample of the MNIST Data}

\notes{We will look at a sub-sample of the MNIST digit data set.

First load in the MNIST data set from scikit learn. This can take a little while because it's large to download.}

\setupcode{from sklearn.datasets import fetch_openml}
\code{mnist = fetch_openml('mnist_784')}

\notes{Sub-sample the dataset to make the training faster.}

\setupcode{import numpy as np}
\code{np.random.seed(0)
digits = [0,1,2,3,4]
N_per_digit = 100
Y = []
labels = []
for d in digits:
    imgs = mnist['data'][mnist['target']==d]
    Y.append(imgs[np.random.permutation(imgs.shape[0])][:N_per_digit])
    labels.append(np.ones(N_per_digit)*d)
Y = np.vstack(Y).astype(np.float64)
labels = np.hstack(labels)
Y /= 255.}

\endif
