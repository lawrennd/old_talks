\ifndef{movieBodyCountData}
\define{movieBodyCountData}

\editme

\subsection{Movie Body Count Data}
\slides{* Data containing movie information (year, length, rating, genre, IMDB Rating).}
\notes{This is a data set created by Simon Garnier and Rany Olson for exploring the differences between R and Python for data science. The data contains information about different movies augmented by estimates about how many on-screen deaths are contained in the movie. The data is craped from <http://www.moviebodycounts.com>. The data contains the following featuers for each movie: `Year`, `Body_Count`, `MPAA_Rating`, `Genre`, `Director`, `Actors`, `Length_Minutes`, `IMDB_Rating`.}

\setupcode{import pods}
\code{data = pods.datasets.movie_body_count()
movies = data['Y']}

\notes{The data is provided to us in the form of a pandas data frame, we can see the features we're provided with by inspecting the columns of the data frame.}

\code{print(', '.join(movies.columns))}

\endif
