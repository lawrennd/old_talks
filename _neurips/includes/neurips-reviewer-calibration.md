\ifndef{neuripsReviewerCalibration}
\define{neuripsReviewerCalibration}

\editme

\subsection{Reviewer Calibration}

\include{_neurips/includes/reviewer-calibration-model.md}
\include{_neurips/includes/reviewer-calibration-fit-model.md}
\include{_neurips/includes/review-quality-prediction.md}
\include{_neurips/includes/paper-acceptance-monte-carlo.md}

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
\include{_neurips/includes/calibration-correlation-of-duplicate-papers.md}

\endif
