\ifndef{leeYeastData}
\define{leeYeastData}

\editme

\subsection{Yeast Connectivity Data}

\notes{This data set collection is from an early publication on [Chromatin immunoprecipitation](http://en.wikipedia.org/wiki/Chromatin_immunoprecipitation) experiments to determine which transcription factors bind to which genes in yeast @Lee:trascriptional02.}

\setupcode{import pods}

\code{data = pods.datasets.lee_yeast_ChIP()}

\notes{The data consists of $p$-values for the hypothesized relationships between the transcription factors and the genes. There are 113 transcription factors represented in `data['transcription_factors']`.}


\code{print(data['transcription_factors'])}

\notes{And the 6270 gene names and their annotations are given in `data['annotations']`.}

\notes{A `pandas` data frame containing all the $p$-values for the binding between genes and transcription factors data is available in `data['Y']`.}


\code{data['Y'].describe()}

\endif
