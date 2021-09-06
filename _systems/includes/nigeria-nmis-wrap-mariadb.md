\ifndef{nigeriaNmisWrapMariadb}
\define{nigeriaNmisWrapMariadb}

\editme

\setuphelpercode{import mariadb}

\helpercode{def create_connection(user, password, host, port=3306, database):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = mariadb.connect(user=user,
	                           password=password,
	                           host=host,
							   port=port,
							   database=database
	    )
    except Error as e:
        print(f"Error connecting to the MariaDB Server: {e}")
	    sys.exit(1)
    return conn}

\notes{TK: Need to load in connection details here.}

\code{conn = create_connection("")}

\notes{Now that we have a connection, we can write a command and pass it to the database.

The python library, `mariadb`, allows us to access the SQL database directly from python.}


\endif
