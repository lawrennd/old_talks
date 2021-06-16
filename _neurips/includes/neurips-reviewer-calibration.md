\ifndef{neuripsReviewerCalibration}
\define{neuripsReviewerCalibration}

\editme

\subsection{Reviewer Calibration}

\notes{Calibration of reviewers is the process where different interpretations of the reviewing scale are addressed. The tradition of calibration goes at least as far back as John Platt's Program Chairing, and included a Bayesian model by Ge, Welling and Ghahramani at NeurIPS 2013.}

\include{_neurips/includes/reviewer-calibration-model.md}
\include{_neurips/includes/reviewer-calibration-fit-model.md}
\include{_neurips/includes/review-quality-prediction.md}
\include{_neurips/includes/paper-acceptance-monte-carlo.md}
\notes{\include{_neurips/includes/calibration-sanity-checks.md}}

\newslide{}

\slides{\figure{\includediagram{\diagramsDir/neurips/calibrated-review-score-vs-original-score}{70%}}{}{}}

\include{_neurips/includes/calibration-correlation-of-duplicate-papers.md}

\endif
