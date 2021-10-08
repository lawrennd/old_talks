\ifndef{awsMariadbServer}
\define{awsMariadbServer}

\editme

\ifndef{sqlDatabaseName}
  \define{sqlDatabaseName}{testdatabase-mariadb}
\endif

\subsection{Creating a MariaDB Server on AWS}


\notes{In this section we'll go through the set up required to create a MariaDB server on AWS.}

\notes{1. Log in to your AWS account and go to the AWS RDS console [here](https://console.aws.amazon.com/rds/home).

2. Set the region to Europe (London) which is denoted as eu-west-2. 

3. Scroll down to "Create Database". Do *not* create an Aurora data base instance.

4. `Standard Create` should be selected. In the box below, which is titled `Engine Options` you should select `MariaDB`. You can leave the `Version` as it's set,

\includepng{\diagramsDir/cloud/aws-select-mariadb-rds}{60%}

5. In the box below that, make sure you select `Free tier`.

\includepng{\diagramsDir/cloud/aws-select-free-tier}{60%}

6. Name your database. For this setup we suggest you use `\sqlDatabaseName` for the name.

7. Set a master password for accessing the data base as admin. 

\includepng{\diagramsDir/cloud/aws-mariadb-setttings}{60%}

8. Leave the `DB instance size` at the default setting. Leave the storage type and allocated storage at the default settings of `General Purpose` (SSD) and `20`.

9. *Disable* autoscaling.

10. In the connectivity leave VPC selection as `Default VPC` and *enable* `Publicly accessible` so that you'll have an IP address for your database.}

\notes{Your database will take a few minutes to launch.}

\endif
