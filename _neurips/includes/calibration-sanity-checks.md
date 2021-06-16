\ifndef{calibrationSanityChecks}
\define{calibrationSanityChecks}

\editme

\subsection{Some Sanity Histograms}

\notes{Here is the histogram of the reviewer scores after calibration.}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
s.hist(bins=100, ax=ax)
_ = ax.set_title('Calibrated Reviewer Scores')
ma.write_figure(directory="\writeDiagramsDir/neurips", filename="calibrated-reviewer-scores.svg")}

\figure{\includediagram{\diagramsDir/neurips/calibrated-reviewer-scores}{70%}}{}{calibrated-reviewer-scores}

\notes{\subsubsection{Adjustments to Reviewer Scores}

We can also compute the posterior distribution for the adjustments to
the reviewer scores.}

\code{# Compute mean and covariance of review biases
b = pd.Series(np.dot(K_b, alpha), index=X2.index)
covb = alpha_f*(K_b - np.dot(K_b, np.dot(Kinv, K_b)))}

\code{reviewer_bias = pd.Series(np.dot(np.diag(1./X2.sum(0)), np.dot(X2.T, b)), index=X2.columns, name='ReviewerBiasMean')
reviewer_bias_std = pd.Series(np.dot(np.diag(1./X2.sum(0)), np.dot(X2.T, np.sqrt(np.diag(covb)))), index=X2.columns, name='ReviewerBiasStd')}

\notes{Here is a histogram of the mean adjustment for the reviewers.}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
reviewer_bias.hist(bins=100, ax=ax)
_ = ax.set_title('Reviewer Calibration Adjustments Histogram')
ma.write_figure(directory="\writeDiagramsDir/neurips", filename="reviewer-calibration-adjustments.svg")}

\figure{\includediagram{\diagramsDir/neurips/reviewer-calibration-adjustments}{70%}}{}{reviewer-calibration-adjustments}

\notes{Export a version of the bias scores for use in CMT.}

\code{bias_export = pd.DataFrame(data={'Quality Score - Does the paper deserves to be published?':reviewer_bias, 
                   'Impact Score - Independently of the Quality Score above, this is your opportunity to identify papers that are very different, original, or otherwise potentially impactful for the NIPS community.':pd.Series(np.zeros(len(reviewer_bias)), index=reviewer_bias.index),
                    'Confidence':pd.Series(np.zeros(len(reviewer_bias)), index=reviewer_bias.index)})
cols = bias_export.columns.tolist()
cols = [cols[2], cols[1], cols[0]]
bias_export = bias_export[cols]
#bias_export.to_csv(os.path.join(cu.cmt_data_directory, 'reviewer_bias.csv'), sep='\t', header=True, index_label='Reviewer Email')}

\subsection{Sanity Check}

\notes{As a sanity check Corinna suggested it makes sense to plot the average
raw score for the papers vs the probability of accept, just to ensure
nothing weird is going on. To clarify the plot, I've actually plotted
raw score vs log odds of accept.}

\code{raw_score = pd.Series(np.dot(np.diag(1./X1.sum(0)), np.dot(X1.T, r.Quality)), index=X1.columns)
prob_accept[prob_accept==0] = 1/(10*samples)
prob_accept[prob_accept==1] = 1-1/(10*samples)}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(raw_score, np.log(prob_accept)- np.log(1-prob_accept), 'rx')
ax.set_title('Raw Score vs Log odds of accept')
ax.set_xlabel('raw score')
_ = ax.set_ylabel('log odds of accept')
ma.write_figure(directory="\writeDiagramsDir/neurips", filename="raw-score-vs-log-odds.svg")}

\figure{\includediagram{\diagramsDir/neurips/raw-score-vs-log-odds}{70%}}{}{raw-score-vs-log-odds}

\subsection{Calibraton Quality Sanity Checks}

\code{s.name = 'CalibratedQuality'
r = r.join(s)}

\notes{We can also look at a scatter plot of the review quality vs the
calibrated quality.}

\setupplotcode{import matplotlib.plt as plt
import cmtutils.plot as plot}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(r.Quality, r.CalibratedQuality, 'r.', markersize=10)
ax.set_xlim([0, 11])
ax.set_xlabel('original review score')
_ = ax.set_ylabel('calibrated review score')
ma.write_figure(directory="\writeDiagramsDir/neurips", filename="calibrated-review-score-vs-original-score.svg")}

\figure{\includediagram{\diagramsDir/neurips/calibrated-review-score-vs-original-score}{70%}}{}{}

\endif
