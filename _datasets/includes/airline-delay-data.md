\ifndef{airlineDelayData}
\define{airlineDelayData}

\editme

\subsection{Data on Airline Delays}

\notes{Flight arrival and departure times for every commercial flight in the USA from January 2008 to April 2008. This dataset contains extensive information about almost 2 million flights, including the delay (in minutes) in reaching the desitnation.}

\setupcode{import pods}

\code{data = pods.datasets.airline_delay()}

\notes{The data dictionary contains the standard keys 'X' and 'Y', which contain 700,000 randomly sub-sampled training points.}


\code{data['X'].shape
data['Y'].shape}
\notes{Additionally there are keys `Xtest` and `Ytest` which provide test data. The number of points considered to be *training data* is controlled by the argument `num_train` argument, which defaults to 700,000. This number is chosen as it matches that used in the Gaussian Processes for Big Data paper.}


\code{data['Xtest'].shape
data['Ytest'].shape}

\notes{The data was compiled by Nicolò Fusi for the paper @Hensman:bigdata13.}

\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys `info` and `details`.}


\code{print(data['info'])
print()
print(data['details'])}

\endif
