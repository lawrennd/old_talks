\ifndef{awsMariadbServer}
\define{awsMariadbServer}

\editme

\ifndef{sqlDatabaseName}
  \define{sqlDatabaseName}{testdatabase-mariadb}
\endif

\subsection{Creating a MariaDB Server on AWS}


\notes{In this section we'll go through the set up required to create a MariaDB server on AWS.}

\notes{Before you start, you're going to need a username and password for accessing the database. You will need to tell the MariaDB server what that username and password is, and you'll also need to make use of it when your client connects to the database. It's good practice to never expose passwords in your code directly. So to protect your passowrd, we're going to create a `credentials.yaml` file locally that will store your username and password so that the client can access the server without ever showing your password in the notebook.}

\notes{We suggest you set the `username` as `admin` and make secure choice of password for your password.} 

\notes{We'll use the following code for recording the username and password for the SQL client.}

\include{_software/includes/save-credentials-file.md}
\include{_cloud/includes/aws-sign-up.md}

\notes{1. Log in to your AWS account and go to the AWS RDS console [here](https://console.aws.amazon.com/rds/home).

2. Set the region to Europe (London) which is denoted as eu-west-2. 

3. Scroll down to "Create Database". Do *not* create an Aurora database instance.

4. `Standard Create` should be selected. In the box below, which is titled `Engine Options` you should select `MariaDB`. You can leave the `Version` as it's set,

\figure{\includepng{\diagramsDir/cloud/aws-select-mariadb-rds}{60%}}{The AWS console box for selecting the `MariaDB` database.}{aws-select-mariadb-rds}

5. In the box below that, make sure you select `Free tier`.

\figure{\includepng{\diagramsDir/cloud/aws-select-free-tier}{60%}}{Make sure you select the free tier option for your database.}{aws-select-free-tier}

6. Name your database. For this setup we suggest you use `\sqlDatabaseName` for the name.

7. Set a master password for accessing the data base as admin.

\figure{\includepng{\diagramsDir/cloud/aws-mariadb-settings}{60%}}{Set the password and username for the database access.}{aws-mariadb-settings}

8. Leave the `DB instance class` as it is.

8. Leave the `DB instance size` at the default setting. Leave the storage type and allocated storage at the default settings of `General Purpose` (SSD) and `20`.

9. *Disable* autoscaling.

10. In the connectivity leave VPC selection as `Default VPC` and *enable* `Publicly accessible` so that you'll have an IP address for your database.}

\notes{Your database will take a few minutes to launch.}

\endif
