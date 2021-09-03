\ifndef{nigeriaNmisMariadb}
\define{nigeriaNmisMariadb}

\editme


\subsection{Create the MariaDB Instance}

\code{hosp_state_joined.to_csv('facilities.csv')}

\notes{We will now set up a `MariaDB` database instance for storing our data.}


\installcode{mariadb}

\include{_cloud/includes/aws-mariadb-server.md}


\installCode{ipython-sql}
\installCode{mysqlclient}

\setupcode{%load_ext sql}

\code{%sql mysql+mysqldb://admin:even+vac@ads-assessment-database.cgrre17yxw11.eu-west-2.rds.amazonaws.com:3306/adsdatabase}

\code{%%sql
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `nigeria_nmis` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;}

\code{%%sql
USE `nigeria_nmis`;}


\code{%%sql
--
-- Table structure for table `facilities`
--

CREATE TABLE IF NOT EXISTS `facilities` (
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


\code{%%sql
--
-- Indexes for table `facilities`
--
ALTER TABLE `facilities`
 ADD PRIMARY KEY (`db_id`);}
 
 \code{%%sql
--
-- AUTO_INCREMENT for table `facilities`
--
ALTER TABLE `facilities`
MODIFY `db_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;}


\code{%%sql
LOAD DATA LOCAL INFILE 'facilities.csv' INTO TABLE facilities}


In the database there can be several 'tables'. Each table can be thought of as like a separate dataframe. The table name we've just saved is 'hospitals_zones_joined'. 
}

\endif
