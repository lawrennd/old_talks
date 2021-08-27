\ifndef{nigeriaNmisSqlite}
\define{nigeriaNmisSqlite}

\editme

\notes{\subsection{SQL Database}

Our first join was a special one, because it involved spatial data. That meant using the special `gdb` format and the `GeoPandas` tool for manipulating that data. But we've now saved our updated data in a new file. 

To do this, we use the command line utility that comes standard for SQLite database creation. SQLite is a simple database that's useful for playing with database commands on your local machine. For a real system, you would need to set up a server to run the database. The server is a separate machine with the job of answering database queries. SQLite pretends to be a proper database but doesn't require us to go to the extra work of setting up a server. Popular SQL server software includes [`MySQL`](https://www.mysql.com/) which is free or [Microsoft's SQL Server](https://www.microsoft.com/en-gb/sql-server/sql-server-2019).

A typical machine learning installation might have you running a database from a cloud service (such as AWS, Azure or Google Cloud Platform). That cloud service would host the database for you, and you would pay according to the number of queries made. 

Many start-up companies were formed on the back of a `MySQL` server hosted on top of AWS. You can [read how to do that here](https://aws.amazon.com/getting-started/hands-on/create-mysql-db/).

If you were designing your own ride hailing app, or any other major commercial software you would want to investigate whether you would need to set up a central SQL server in one of these frameworks.

Today though, we'll just stick to SQLite which gives you a sense of the database without the time and expense of setting it up on the cloud. As well as showing you the SQL commands (which is often what's used in a production ML system) we'll also give the equivalent ```pandas``` commands, which would often be what you would use when you're doing data analysis in `python` and `Jupyter`.}

\notes{\subsection{Create the SQLite Database}

The beautiful thing about SQLite is that it allows us to play with SQL without going to the work of setting up a proper SQL server. Creating a data base in SQLite is as simple as writing a new file. To create the database, we'll first write our joined data to a CSV file, then we'll use a little utility to convert our hospital database into a SQLite database.
}

\notes{\code{hosp_state_joined.to_csv('facilities.csv')}}

\installcode{csv-to-sqlite}

\notes{\code{!csv-to-sqlite -f facilities.csv -t full -o db.sqlite}}

\notes{Rather than being installed on a separate server, SQLite simply stores the database locally in a file called `db.sqlite`.

In the database there can be several 'tables'. Each table can be thought of as like a separate dataframe. The table name we've just saved is 'hospitals_zones_joined'. 
}

\notes{\subsection{Accessing the SQL Database}

Now that we have a SQL database, we can create a connection to it and query it using SQL commands. Let's try to simply select the data we wrote to it, to make sure its the same.

Start by making a connection to the database. This will often be done via remote connections, but for this example we'll connect locally to the database using the filepath directly.}

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

The python library, `sqlite3`, allows us to access the SQL database directly from python. We do this using an `execute` command on the connection. 

Typically, its good software engineering practice to 'wrap' the database command in some python code. This allows the commands to be maintained. Below we wrap the SQL command

```
SELECT * FROM [table_name] LIMIT : N
```
in python code. This SQL command selects the first ```N``` entries from a given database called ```table_name```.

We can pass the ```table_name``` and number of rows, ```N``` to the python command.}

\notes{
\helpercode{def select_top(conn, table,  n):
    """
    Query n first rows of the table
    :param conn: the Connection object
    :param table: The table to query
    :param n: Number of rows to query
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM [{table}] LIMIT :limitNum", {"limitNum": n})

    rows = cur.fetchall()
    return rows}
}

\notes{Let's have a go at calling the command to extract the first three facilities from our health center database. Let's try creating a function that does the same thing the pandas `.head()` method does so we can inspect our database.}

\notes{
\setupcode{def head(conn, table, n=5):
  rows = select_top(conn, table, n)
  for r in rows:
      print(r)}
	  
\code{head(conn, 'facilities')}
}

\notes{Great! We now have the data base in SQLite, and some python functions that operate on the data base by wrapping SQL commands.

We will return to the SQL command style after download and add the other datasets to the database using a combination of `pandas` and the `csv-to-sqlite` utility.

Our next task will be to introduce data on COVID19 so that we can join that to our other data sets.}

\endif
