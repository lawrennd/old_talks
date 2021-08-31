\ifndef{nigeriaNmisSqlite}
\define{nigeriaNmisSqlite}

\editme

Today though, we'll just stick to SQLite which gives you a sense of the database without the time and expense of setting it up on the cloud. As well as showing you the SQL commands (which is often what's used in a production ML system) we'll also give the equivalent `pandas` commands, which would often be what you would use when you're doing data analysis in `python` and `Jupyter`.}

\notes{\subsection{Create the SQLite Database}

The beautiful thing about SQLite is that it allows us to play with SQL without going to the work of setting up a proper SQL server. Creating a data base in SQLite is as simple as writing a new file. To create the database, we'll first write our joined data to a CSV file, then we'll use a little utility to convert our hospital database into a SQLite database.
}

\notes{\code{hosp_state_joined.to_csv('facilities.csv')}}

\installcode{csv-to-sqlite}

\notes{\code{!csv-to-sqlite -f facilities.csv -t full -o db.sqlite}}

\notes{Rather than being installed on a separate server, SQLite simply stores the database locally in a file called `db.sqlite`.

In the database there can be several 'tables'. Each table can be thought of as like a separate dataframe. The table name we've just saved is 'hospitals_zones_joined'. 
}

\endif
