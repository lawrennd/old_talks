\ifndef{paperAcceptanceMonteCarlo}
\define{paperAcceptanceMonteCarlo}

\editme

\subsubsection{Monte Carlo Simulations for Probability of Acceptance}

\notes{We can now sample from this posterior distribution of bias-adjusted
scores jointly, to get a set of scores for all papers. For this set of
scores we can perform a ranking and accept the top 400 papers. This
gives us a sampled conference. If we do that 1,000 times then we can see
how many times each paper was accepted to get a probability of
acceptance.}

\code{number_accepts = 420 # 440 because of the 10% replication}

\code{# place this in a separate box, because sampling can take a while.
samples = 1000
score = np.random.multivariate_normal(mean=s, cov=covs, size=samples).T
# Use X1 which maps papers to paper/reviewer pairings to get the average score for each paper.
paper_score = pd.DataFrame(np.dot(np.diag(1./X1.sum(0)), np.dot(X1.T, score)), index=X1.columns)}

\notes{Now we can compute the probability of acceptance for each of the sampled
rankings.}

\code{prob_accept = ((paper_score>paper_score.quantile(1-(float(number_accepts)/paper_score.shape[0]))).sum(1)/1000)
prob_accept.name = 'AcceptProbability'}

\notes{Now we have the probability of accepts, we can decide on the boundaries
of the grey area. These are set in `lower` and `upper`. The grey area is
those papers that will be debated most heavily during the
teleconferences between program chairs and area chairs.}

\code{lower=0.1
upper=0.9
grey_area = ((prob_accept>lower) & (prob_accept<upper))
print('Number of papers in grey area:', grey_area.sum())}


\code{import matplotlib.pyplot as plt
import cmtutils.plot as plot}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
print('Expected Papers Accepted:', prob_accept.sum())
_ = prob_accept.hist(bins=40, ax=ax)
ma.write_figure(directory="\writeDiagramsDir/neurips", filename="probability-of-accept.svg")}


\figure{\includediagram{\diagramsDir/neurips/probability-of-accept}{70%}}{}{probability-of-accept}


\endif
