\ifndef{pmlrData}
\define{pmlrData}

\editme

\subsection{Paper Data from the Proceedings of Machine Learning Research}

\notes{This data set collection comes from the rebranding of JMLR W&CP as PMLR. As part of the move of the web we've set it up to be convenient to download the current set of proceedings.}


\setupcode{import pods}

\code{# calling without arguments downloads all volumes
data = pods.datasets.pmlr()}

\code{data['Y'].describe()}

\endif
