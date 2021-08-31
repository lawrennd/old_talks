\ifndef{awsMysqlServer}
\define{awsMysqlServer}

\editme

\ifndef{mysqlDatabaseName}
\define{mysqlDatabaseName}{example-mysql-database}
\subsection{Creating a MySQL Server on AWS}


\notes{In this section we'll go through the set up required to create a MySQL server on AWS.}

\notes{1. Log in to your AWS account and go to the AWS RDS console [here](https://console.aws.amazon.com/rds/home).

2. Set the region to Europe (London) which is denoted as eu-west-2. 

3. Scroll down to "Create Database". Do *not* create an Aurora data base instance.

4. `Standard Create` should be selected. In the box below, which is titled `Engine Options` you should select `MySQL`. You can leave the `Version` as it's set, but in the box below that, make sure you select `Free tier`.

5. Name your database. For this assessment we suggest you use `\mysqlDatabaseName` for the name.

6. Set a master password for accessing the data base as admin.

7. Leave the `DB instance size` at the default setting. Leave the storage type and allocated storage at the default settings of `General Purpose` (SSD) and `20`.

8. *Disable* autoscaling.

9. In the connectivity leave VPC selection as `Default VPC` and *enable* `Publicly accessible` so that you'll have an IP address for your database.}

\notes{Your database will take a few minutes to launch.}

\endif
