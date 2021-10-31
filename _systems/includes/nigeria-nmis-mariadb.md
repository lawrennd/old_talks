\ifndef{nigeriaNmisMariadb}
\define{nigeriaNmisMariadb}

\editme


\subsection{Create the MariaDB Instance}

\code{hosp_state_joined.to_csv('hospitals_zones_joined.csv')}

\notes{We will now set up a `MariaDB` database instance for storing our data.}



\include{_cloud/includes/aws-mariadb-server.md}

\installcode{ipython-sql}
\installcode{PyMySQL}

\setupcode{%load_ext sql}

\code{with open("credentials.yaml") as file:
  credentials = yaml.safe_load(file)
username = credentials["username"]
password = credentials["password"]
url = database_details["url"]}

\notes{Connect to the database, enabling the uploading of local files as part of the connection.}

\code{%sql mariadb+pymysql://$username:$password@$url?local_infile=1}

\notes{Now that we have the database connection, we're going to create a new database called `nigeria_nmis` for doing our work in.}

\code{%%sql
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `nigeria_nmis` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;}

\code{%%sql
USE `nigeria_nmis`;}

\notes{For the data to be loaded in to the table, we need to describe the *schema*. The schema tells the database server what to expect in the columns of the table.}

\code{%%sql
--
-- Table structure for table `hospitals_zones_joined`
--

CREATE TABLE IF NOT EXISTS `hospitals_zones_joined` (
  `transaction_unique_identifier` tinytext COLLATE utf8_bin NOT NULL,
  `price` int(10) unsigned NOT NULL,
  `date_of_transfer` date NOT NULL,
  `postcode` varchar(8) COLLATE utf8_bin NOT NULL,
  `property_type` varchar(1) COLLATE utf8_bin NOT NULL,
  `new_build_flag` varchar(1) COLLATE utf8_bin NOT NULL,
  `tenure_type` varchar(1) COLLATE utf8_bin NOT NULL,
  `primary_addressable_object_name` tinytext COLLATE utf8_bin NOT NULL,
  `secondary_addressable_object_name` tinytext COLLATE utf8_bin NOT NULL,
  `street` tinytext COLLATE utf8_bin NOT NULL,
  `locality` tinytext COLLATE utf8_bin NOT NULL,
  `town_city` tinytext COLLATE utf8_bin NOT NULL,
  `district` tinytext COLLATE utf8_bin NOT NULL,
  `county` tinytext COLLATE utf8_bin NOT NULL,
  `ppd_category_type` varchar(2) COLLATE utf8_bin NOT NULL,
  `record_status` varchar(2) COLLATE utf8_bin NOT NULL,
  `db_id` bigint(20) unsigned NOT NULL
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;}

\notes{We also need to tell the server what the index of the data base is. Here we're adding `db_id` as the primary key in the index.}

\code{%%sql
--
-- Indexes for table `hospitals_zones_joined`
--
ALTER TABLE `hospitals_zones_joined`
 ADD PRIMARY KEY (`db_id`);}
 
 \code{%%sql
--
-- AUTO_INCREMENT for table `hospitals_zones_joined`
--
ALTER TABLE `hospitals_zones_joined`
MODIFY `db_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;}

\notes{Now we're ready to load the data into the table. This can be done with [the SQL command `LOAD DATA`](https://mariadb.com/kb/en/load-data-infile/). When connecting to the database we used the flag `local_infile=1` to ensure we could load local files into the database.}

\code{%%sql
LOAD DATA LOCAL INFILE 'hospitals_zones_joined.csv' INTO TABLE hospitals_zones_joined
FIELDS TERMINATED BY ','
LINES STARTING BY '' TERMINATED BY '\n';}


\notes{In the database there can be several 'tables'. Each table can be thought of as like a separate dataframe. The table name we've just saved is `hospitals_zones_joined`.}

\endif
