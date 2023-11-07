\ifndef{nigerianPopulationDataSqlite}
\define{nigerianPopulationDataSqlite}

\editme

\subsection{Loading the Population Data into the SQLite Database}

\notes{We can load the data into the SQLite database using the script as before.}

\notes{\code{pop_data.to_csv('pop_data.csv')}}

\notes{\code{!csv-to-sqlite -f pop_data.csv -t full -o db.sqlite}}


\endif
