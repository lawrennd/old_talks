\ifndef{movieBodyCountData}
\define{movieBodyCountData}

\editme

\subsection{Movie Body Count Data}

Let's consider the movie body count data.}

\setupcode{import pods}
\code{data = pods.datasets.movie_body_count()
movies = data['Y']}

\notes{Let's remind ourselves of the features we've been provided with.}

\code{print(', '.join(movies.columns))}


\endif
