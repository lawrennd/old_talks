\ifndef{sigmoidFunction}
\define{sigmoidFunction}

\editme

\subsubsection{Sigmoid Function}

\setupplotcode{import teaching_plots as plot}

\plotcode{plot.logistic('\diagramsDir/ml/logistic.svg')}

\figure{\includediagram{\diagramsDir/ml/logistic}{80%}}{The logistic function.}{the-logistic-function}

\notes{The function has this characeristic 's'-shape (from where the term sigmoid, as in sigma, comes from). It also takes the input from the entire real line and 'squashes' it into an output that is between zero and one. For this reason it is sometimes also called a 'squashing function'.}

\endif
