\ifndef{googleTrendsData}
\define{googleTrendsData}

\editme

\subsection{Data from Google Trends}

\notes{This data set collection was inspired by a [ipython
notebook](https://github.com/sahuguet/notebooks/blob/master/GoogleTrends%20meet%20Notebook.ipynb) from [sahuguet](https://github.com/sahuguet) which made queries to
google trends and downloaded the results. We\'ve modified the download
to cache the results of a query: making multiple calls to the google API
results in a block due to terms of service violations, cacheing the data
locally prevents this happening.

sahuguet's original code stopped working so the notebook was updated to use the `pytrends` package instead on 6th May 2021.}

\setupcode{import pods}


\setupplotcode{import matplotlib.pyplot as plt}

\code{# calling without arguments uses the default query terms
data = pods.datasets.google_trends(['big data', 'internet of things'])}

\notes{The default query terms are 'big data', 'data science' and 'machine
learning'. The dictionary returned from the call contains the standard
`X` and `y` keys that are ready to be used in the GPy toolkit as
inputs to the Gaussian process. In this case the `X` variables are the
time (first column) and an index representing the query.}

\code{print(data['X'][284, :])}


\notes{So the 284th element of X contains is the 34th time point of the query
term 2, which in this case is the 34th time point of the 'machine
learning' time series. The value of the time series at that point is
given by the corresponding row of `Y`}

\code{print(data['Y'][284, :])}

\notes{The dictionary also contains a pandas data frame of the trend data,
which is in line with what [sahuguet](https://github.com/sahuguet)
originally returned.}

\code{data['data frame'].describe()}


\notes{And we can plot the trends data to see what the effect is.}

\code{data['data frame'].set_index('Date', inplace=True)}

\plotcode{fig, ax = plt.subplots(figsize=(10,5))
data['data frame'].plot(ax=ax, rot=45)}


\subsubsection{Dogs, Cats and Rabbits}

\notes{Another data set we might consider downloading from google trends is
different pets. Below we consider cats, dogs and rabbits.}

\code{data = pods.datasets.google_trends(['cat', 'dog', 'rabbit'], refresh_data=True)
data['data frame'].set_index('Date', inplace=True)}

\plotcode{fig, ax = plt.subplots(figsize=(10,5))
data['data frame'].plot(ax=ax, rot=45)}




\notes{Here we've plotted the data in the same manner as
[sahuguet](https://github.com/sahuguet) suggested in his original
notebook, using the plotting facility of `pandas`.}

\subsubsection{Games Consoles}

\notes{Finally we can try and compare different games console popularity.}

\code{data = pods.datasets.google_trends(['xbox one', 'wii u', 'ps4'])}

\plotcode{data['data frame'].set_index('Date', inplace=True)
fig, ax = plt.subplots(figsize=(10,5))
data['data frame'].plot(ax=ax, rot=45)}


\endif
