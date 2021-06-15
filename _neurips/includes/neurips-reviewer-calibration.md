\ifndef{neuripsReviewerCalibration}
\define{neuripsReviewerCalibration}

\editme

\subsection{Reviewer Calibration}

\include{_neurips/includes/reviewer-calibration-model.md}
\include{_neurips/includes/reviewer-calibration-fit-model.md}
\include{_neurips/includes/review-quality-predicton.md}
\include{_neurips/includes/paper-acceptance-monte-carlo.md}

\subsection{Calibraton Quality Sanity Checks}

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
