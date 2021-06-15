\ifndef{reviewQualityPrediction}
\define{reviewQualityPrediction}

\editme

\subsubsection{Review Quality Prediction}

\notes{Now we wish to predict the bias corrected scores for the papers. That
involves considering a variable $s_{i,j} = f_i + e_{i,j}$ which is the
score with the bias removed. That variable has a covariance matrix,
$\mathbf{K}_s=\mathbf{K}_f + \sigma^2 \mathbf{I}$ and a cross covariance
between $\mathbf{y}$ and $\mathbf{s}$ is also given by $\mathbf{K}_s$.
This means we can compute the posterior distribution of the scores as
follows:}

\code{# Compute mean and covariance of quality scores
K_s = K_f + np.eye(K_f.shape[0])*sigma2
s = pd.Series(np.dot(K_s, alpha) + mu, index=X1.index)
covs = alpha_f*(K_s - np.dot(K_s, np.dot(Kinv, K_s)))}

\endif
