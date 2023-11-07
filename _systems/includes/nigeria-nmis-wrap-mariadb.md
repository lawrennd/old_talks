\ifndef{nigeriaNmisWrapMariadb}
\define{nigeriaNmisWrapMariadb}

\editme

\setuphelpercode{import pymysql}

\helpercode{def create_connection(user, password, host, database, port=3306):
    """ Create a database connection to the MariaDB database
        specified by the host url and database name.
    :param user: username
    :param password: password
    :param host: host url
    :param database: database
    :param port: port number
    :return: Connection object or None
    """
    conn = None
    try:
        conn = pymysql.connect(user=user,
                               passwd=password,
                               host=host,
                               port=port,
                               local_infile=1,
                               db=database
                               )
    except Exception as e:
        print(f"Error connecting to the MariaDB Server: {e}")
    return conn}

\notes{Now we make the connection using the details stored in `credentials` and `database_details`.}

\code{conn = create_connection(user=credentials["username"], 
                         password=credentials["password"], 
                         host=database_details["url"],
                         database="nigeria_nmis")}

\notes{Now that we have a connection, we can write a command and pass it to the database.

The python library, `pymysql`, allows us to access the SQL database directly from python.}


\endif
