\ifndef{highFiveDeepGp}
\define{highFiveDeepGp}

talk-macros.gpp}atasets/includes/high-five-data.md}

\editme

\subsection{Shared LVM}

\figure{\includediagram{\diagramsDir/shared}{60%}}{Shared latent variable model structure. Here two related data sets are brought together with a set of latent variables that are partially shared and partially specific to one of the data sets.}{shared-latent-variable-model-graph}

\newslide

\figure{\includeimg{\diagramsDir/deep-gp-high-five2.png}{80%}}{Latent spaces of the 'high five' data. The structure of the model is automatically learnt. One of the latent spaces is coordinating how the two figures walk together, the other latent spaces contain latent variables that are specific to each of the figures separately.}{deep-gp-high-five}

\endif
