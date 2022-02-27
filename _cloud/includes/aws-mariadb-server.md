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

talk-macros.gpp}oftware/includes/save-credentials-file.md}

talk-macros.gpp}loud/includes/history-of-cloud.md}

talk-macros.gpp}loud/includes/aws-sign-up.md}

\notes{The earliest AWS services of S3 and EC2 gave storage and compute. Together these could be combined to host a database service. Today cloud providers also provide machines that are already set up to provide a database service. We will make use of AWS's Relational Database Service to provide our `MariaDB` server.}

\notes{1. Log in to your AWS account and go to the AWS RDS console [here](https://console.aws.amazon.com/rds/home).

2. Make sure the region is set to Europe (London) which is denoted as eu-west-2. 

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

11. In `VPC security group` select `Create new` to create a new security group for the instance.
12. Write `ADSMariaDB` as the group name for the VPC security group.
 
12. Select `Create database` at the bottom to launch the database.} 

\notes{Your database will take a few minutes to launch.}

\notes{While it's launching you can check the access rules for the database [here](https://eu-west-2.console.aws.amazon.com/ec2/v2/home?region=eu-west-2#SecurityGroups:). 

1. Select the `Default` security group.
2. The source of the active inbound rule must be set to `0.0.0.0/0`. It means you can connect from any source using IPv4.

A wrong inbound rule can cause you fail connecting to the database from this notebook.}

\notes{*Note:* by setting the inbound rule to `0.0.0.0/0` we have opened up access to *any* IP address. If this were production code you wouldn't do this, you would specify a range of addresses or the specific address of the compute server that needed to access the system. Because we're using Google colab or another notebook client to access, and we can't control the IP address of that access, for simplicity we've set it up so that any IP address can access the database, but that is *not good practice* for production systems.}

\notes{Once the database is up and running you should be able to find its url on [this page](https://eu-west-2.console.aws.amazon.com/rds/home?region=eu-west-2#databases:). You can add that to the credentials file using the following code.}

\code{# Insert your database url below
database_details = {"url": INSERT_YOUR_DATABASE_URL_HERE, 
                    "port": 3306}}


\endif
