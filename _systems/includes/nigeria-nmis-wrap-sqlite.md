\ifndef{nigeriaNmisCreateSqlite}
\define{nigeriaNmisCreateSqlite}

\editme

\notes{
\setuphelpercode{import sqlite3}

\helpercode{def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn}

\code{conn = create_connection("db.sqlite")}
}

\notes{Now that we have a connection, we can write a command and pass it to the database.

To access a data base, the first thing that is made is a connection. Then SQL is used to extract the information required. A typical SQL command is `SELECT`. It allows us to extract rows from a given table. It operates a bit like the `.head()` method in `pandas`, it will return the first `N` rows (by default the `.head()` command returns the first 5 rows, but you can set `N` to whatever you like. Here we've included a default value of 5 to make it match the `pandas` command.

The python library, `sqlite3`, allows us to access the SQL database directly from python.}

\endif
