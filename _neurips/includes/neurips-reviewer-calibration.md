\ifndef{neuripsReviewerCalibration}
\define{neuripsReviewerCalibration}

\editme

\subsection{Reviewer Calibration}

\include{_neurips/includes/reviewer-calibration-model.md}
\include{_neurips/includes/reviewer-calibration-fit-model.md}
\include{_neurips/includes/review-quality-predicton.md}
\include{_neurips/includes/paper-acceptance-monte-carlo.md}

\notes{\subsubsection{Monte Carlo Simulations for Probability of Acceptance}

We can now sample from this posterior distribution of bias-adjusted
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
ma.write_figure(directory="\writeDiagramsDir/neurips", "probability-of-accept.svg")}


\figure{\includediagram{\diagramsDir/neurips/probability-of-accept}{70%}}{}{probability-of-accept}

\subsection{Some Sanity Histograms}

\notes{Here is the histogram of the reviewer scores after calibration.}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
s.hist(bins=100, ax=ax)
_ = ax.set_title('Calibrated Reviewer Scores')
ma.write_figure(directory="\writeDiagramsDir/neurips", "calibrated-reviewer-scores.svg")}

\figure{\includediagram{\diagramsDir/neurips/calbirated-reviewer-scores}{70%}}{}{calibrated-reviewer-scores}

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
ma.write_figure(directory="\writeDiagramsDir/neurips", "reviewer-calibration-adjustments.svg")}

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
ma.write_figure(directory="\writeDiagramsDir/neurips", "raw-score-vs-log-odds.svg")}

\figure{\includediagram{\diagramsDir/neurips/raw-score-vs-log-odds}{70%}}{}{raw-score-vs-log-odds}

\code{s.name = 'CalibratedQuality'
r = r.join(s)}

\notes{We can also look at a scatter plot of the review quality vs the
calibrated quality.}

\setupplotcode{import matplotlib.plt as plt
import cmtutils.plot as plot}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(r.Quality, r.CalibratedQuality, 'rx')
ax.set_xlim([0, 11])
ax.set_xlabel('original review score')
_ = ax.set_ylabel('calibrated review score')
ma.write_figure(directory="\writeDiagramsDir/neurips", "calibrated-review-score-vs-original-score.svg")}

\figure{\includediagram{\diagramsDir/neurips/calibrated-review-score-vs-original-score}{70%}}{}{}

\subsection{Duplicate Papers}

\notes{For NIPS 2014 we experimented with duplicate papers: we pushed papers
through the system twice, exposing them to different subsets of the
reviewers. The first thing we'll look at is the duplicate papers.
Firstly we identify them by matching on title.}

\code{filename = date + '_paper_list.xls'
papers = cu.CMT_Papers_read(filename=filename)
duplicate_list = []
for ID, title in papers.papers.Title.iteritems():
    if int(ID)>1779 and int(ID) != 1949:
        pair = list(papers.papers[papers.papers['Title'].str.contains(papers.papers.Title[ID].strip())].index)
        pair.sort(key=int)
        duplicate_list.append(pair)}

\notes{Next we compute the correlation coefficients for the duplicated papers
for the average impact and quality scores.}

\code{quality = []
calibrated_quality = []
accept = []
impact = []
confidence = []
for duplicate_pair in duplicate_list:
    quality.append([np.mean(r[r.PaperID==duplicate_pair[0]].Quality), np.mean(r[r.PaperID==duplicate_pair[1]].Quality)])
    calibrated_quality.append([np.mean(r[r.PaperID==duplicate_pair[0]].CalibratedQuality), np.mean(r[r.PaperID==duplicate_pair[1]].CalibratedQuality)])
    impact.append([np.mean(r[r.PaperID==duplicate_pair[0]].Impact), np.mean(r[r.PaperID==duplicate_pair[1]].Impact)])
    confidence.append([np.mean(r[r.PaperID==duplicate_pair[0]].Conf), np.mean(r[r.PaperID==duplicate_pair[1]].Conf)])
quality = np.array(quality)
calibrated_quality = np.array(calibrated_quality)
impact = np.array(impact)
confidence = np.array(confidence)
quality_cor = np.corrcoef(quality.T)[0, 1]
calibrated_quality_cor = np.corrcoef(calibrated_quality.T)[0, 1]
impact_cor = np.corrcoef(impact.T)[0, 1]
confidence_cor = np.corrcoef(confidence.T)[0, 1]
print("Quality correlation: ", quality_cor)
print("Calibrated Quality correlation: ", calibrated_quality_cor)
print("Impact correlation: ", impact_cor)
print("Confidence correlation: ", confidence_cor)}

```
    Quality correlation:  0.54403674862622
    Calibrated Quality correlation:  0.5455958618174274
    Impact correlation:  0.26945269236041036
    Confidence correlation:  0.3854251559444674
```

\subsection{Correlation Plots}

\notes{To visualize the quality score correlation we plot the group 1 papers
against the group 2 papers. Here we add a small amount of jitter to
ensure points to help visualize points that would otherwise fall on the
same position.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(quality[:, 0]+np.random.randn(quality.shape[0])*0.06125, quality[:, 1]+np.random.randn(quality.shape[0])*0.06125, 'r.', markersize=10)
_ = ax.set_title('Quality Correlation: ' + str(quality_cor))
ma.write_figure(directory="\writeDiagramsDir/neurips",
                filename="quality-correlation.svg")}

\figure{\includediagram{\diagramsDir/neurips/quality-correlation}{70%}}{}{quality-correlation}

\notes{Similarly for the calibrated quality of the papers.}

\newslide{Correlation Plots}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(calibrated_quality[:, 0]+np.random.randn(calibrated_quality.shape[0])*0.06125, calibrated_quality[:, 1]+np.random.randn(calibrated_quality.shape[0])*0.06125, 'rx')
_ = ax.set_title('Calibrated Quality Correlation: ' + str(calibrated_quality_cor))
ma.write_figure(directory="\writeDiagramsDir/neurips",
                filename="calibrated-quality-correlation.svg")}

\figure{\includediagram{\diagramsDir/neurips/calibrated-quality-correlation}{70%}}{}{calibrated-quality-correlation}

\code{# Apply Laplace smoothing to accept probabilities before incorporating them.
revs = r.join((prob_accept+0.0002)/1.001, on='PaperID').join(reviewer_bias, on='Email').join(papers.papers['Number Of Discussions'], on='PaperID').join(reviewer_bias_std, on='Email').sort_values(by=['AcceptProbability','PaperID', 'CalibratedQuality'], ascending=False)
revs.set_index(['PaperID'], inplace=True)
def len_comments(x):
    return len(x.Comments)
revs['comment_length']=revs.apply(len_comments, axis=1)
# Save the computed information to disk
#revs.to_csv(os.path.join(cu.cmt_data_directory, date + '_processed_reviews.csv'), encoding='utf-8')}


\endif
