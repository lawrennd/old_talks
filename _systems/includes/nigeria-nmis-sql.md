\ifndef{nigeriaNmisSql}
\define{nigeriaNmisSql}

\editme

\notes{\subsection{SQL Database}

Our first join was a special one, because it involved spatial data. That meant using the special `gdb` format and the `GeoPandas` tool for manipulating that data. But we've now saved our updated data in a new file. 

To do this, we use the command line utility that comes standard for SQLite database creation. SQLite is a simple database that's useful for playing with database commands on your local machine. For a real system, you would need to set up a server to run the database. The server is a separate machine with the job of answering database queries. SQLite pretends to be a proper database but doesn't require us to go to the extra work of setting up a server. Popular SQL server software includes [`MariaDB`](https://mariadb.org/) which is open source, or [Microsoft's SQL Server](https://www.microsoft.com/en-gb/sql-server/sql-server-2019).

A typical machine learning installation might have you running a database from a cloud service (such as AWS, Azure or Google Cloud Platform). That cloud service would host the database for you, and you would pay according to the number of queries made. 

Many start-up companies were formed on the back of a `MySQL` server hosted on top of AWS. Although since MySQL was sold to Sun, and then passed on to Oracle, the open source community has turned its attention to `MariaDB`, here's the [AWS instructions on how to set up `MariaDB`](https://aws.amazon.com/getting-started/hands-on/create-mariadb-db/).

If you were designing your own ride hailing app, or any other major commercial software you would want to investigate whether you would need to set up a central SQL server in one of these frameworks.}

\ifndef{databaseType}
  \define{databaseType}{sqlite}
\endif
\ifeq{\databaseType}{sqlite}
  \include{_systems/includes/nigeria-nmis-sqlite.md}
\else
  \ifeq{\databaseType}{mariadb}
    \include{_systems/includes/nigeria-nmis-mariadb.md}
  \endif
\endif

\notes{\subsection{Accessing the SQL Database}

Now that we have a SQL database, we can create a connection to it and query it using SQL commands. Let's try to simply select the data we wrote to it, to make sure it's the same.

Start by making a connection to the database. This will often be done via remote connections, but for this example we'll connect locally to the database using the filepath directly.}


\notes{To access a data base, the first thing that is made is a connection. Then SQL is used to extract the information required. A typical SQL command is `SELECT`. It allows us to extract rows from a given table. It operates a bit like the `.head()` method in `pandas`, it will return the first `N` rows (by default the `.head()` command returns the first 5 rows, but you can set `N` to whatever you like. Here we've included a default value of 5 to make it match the `pandas` command.

We do this using an `execute` command on the connection. 

Typically, its good software engineering practice to 'wrap' the database command in some python code. This allows the commands to be maintained. Below we wrap the SQL command

```
SELECT * FROM [table_name] LIMIT\ifeq{\databaseType}{sqlite} :\endif N
```
in python code. This SQL command selects the first `N` entries from a given database called `table_name`.

We can pass the `table_name` and number of rows, `n`, to the python command.}


\ifeq{\databaseType}{sqlite}
  \include{_systems/includes/nigeria-nmis-wrap-sqlite.md}
\else
  \ifeq{\databaseType}{mariadb}
    \include{_systems/includes/nigeria-nmis-wrap-mariadb.md}
  \endif
\endif

\helpercode{def select_top(conn, table,  n):
    """
    Query n first rows of the table
    :param conn: the Connection object
    :param table: The table to query
    :param n: Number of rows to query
    """
    cur = conn.cursor()
    \ifeq{\databaseType}{sqlite}cur.execute(f"SELECT * FROM [{table}] LIMIT : limitNum", {"limitNum": n})\else\ifeq{\databaseType}{mariadb}cur.execute(f"SELECT * FROM {table} LIMIT limitNum", {"limitNum": n})\endif\endif

    rows = cur.fetchall()
    return rows}


\notes{Let's have a go at calling the command to extract the first three facilities from our health center database. Let's try creating a function that does the same thing the pandas `.head()` method does so we can inspect our database.}

\setupcode{def head(conn, table, n=5):
  rows = select_top(conn, table, n)
  for r in rows:
      print(r)}
	  
\code{head(conn, 'facilities')}

\notes{Great! We now have the database in  and some python functions that operate on the data base by wrapping SQL commands.

We will return to the SQL command style after download and add the other datasets to the database using a combination of `pandas` and the database utilities.

Our next task will be to introduce data on COVID19 so that we can join that to our other data sets.}

\endif
