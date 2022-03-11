\ifndef{nigeriaNmisMariadb}
\define{nigeriaNmisMariadb}

\editme


\subsection{Create the MariaDB Instance}


\code{hosp_state_joined.to_csv('hospitals_zones_joined.csv', header=None)}

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
DROP TABLE IF EXISTS `hospitals_zones_joined`;
CREATE TABLE IF NOT EXISTS `hospitals_zones_joined` (
  `db_id` bigint(20) unsigned NOT NULL,
  `facility_name` tinytext COLLATE utf8_bin NOT NULL,
  `facility_type_display` tinytext COLLATE utf8_bin NOT NULL,
  `maternal_health_delivery_services` BOOLEAN COLLATE utf8_bin NOT NULL,
  `emergency_transport` BOOLEAN COLLATE utf8_bin NOT NULL,
  `skilled_birth_attendant` BOOLEAN COLLATE utf8_bin NOT NULL,
  `num_chews_fulltime` bigint(20) unsigned NOT NULL,
  `phcn_electricity` BOOLEAN COLLATE utf8_bin NOT NULL,
  `c_section_yn` BOOLEAN COLLATE utf8_bin NOT NULL,
  `child_health_measles_immun_calc` BOOLEAN COLLATE utf8_bin NOT NULL,
  `num_nurses_fulltime` bigint(20) unsigned NOT NULL,
  `num_nursemidwives_fulltime` bigint(20) unsigned NOT NULL,
  `num_doctors_fulltime` bigint(20) unsigned NOT NULL,
  `date_of_survey` date NOT NULL,
  `facility_id` tinytext COLLATE utf8_bin NOT NULL,
  `community` tinytext COLLATE utf8_bin NOT NULL,
  `ward` tinytext COLLATE utf8_bin NOT NULL,
  `management` tinytext COLLATE utf8_bin NOT NULL,
  `improved_water_supply` BOOLEAN COLLATE utf8_bin NOT NULL,
  `improved_sanitation` BOOLEAN COLLATE utf8_bin NOT NULL,
  `vaccines_fridge_freezer` BOOLEAN COLLATE utf8_bin NOT NULL,
  `antenatal_care_yn` BOOLEAN COLLATE utf8_bin NOT NULL,
  `family_planning_yn` BOOLEAN COLLATE utf8_bin NOT NULL,
  `malaria_treatment_artemisinin` BOOLEAN COLLATE utf8_bin NOT NULL,
  `sector` tinytext COLLATE utf8_bin NOT NULL,
  `formhub_photo_id` tinytext COLLATE utf8_bin NOT NULL,
  `gps` tinytext COLLATE utf8_bin NOT NULL,
  `survey_id` tinytext COLLATE utf8_bin NOT NULL,
  `unique_lga` tinytext COLLATE utf8_bin NOT NULL,
  `latitude` decimal(11,8) NOT NULL,
  `longitude` decimal(10,8) NOT NULL,
  `geometry` tinytext COLLATE utf8_bin NOT NULL,
  `index_right` bigint(20) unsigned NOT NULL,
  `admin1Name_en` tinytext COLLATE utf8_bin NOT NULL,
  `admin1Pcode` tinytext COLLATE utf8_bin NOT NULL,
  `admin1RefName` tinytext COLLATE utf8_bin NOT NULL,
  `admin1AltName1_en` tinytext COLLATE utf8_bin NOT NULL,
  `admin1AltName2_en` tinytext COLLATE utf8_bin NOT NULL,
  `admin0Name_en` tinytext COLLATE utf8_bin NOT NULL,
  `admin0Pcode` tinytext COLLATE utf8_bin NOT NULL,
  `date` date NOT NULL,
  `validOn` date NOT NULL,
  `validTo` date NOT NULL,
  `Shape_Length` decimal(10,10) NOT NULL,
  `Shape_Area` decimal(10,10) NOT NULL  
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

\code{%sql SELECT * FROM hospitals_zones_joined LIMIT 10}

\notes{In the database there can be several 'tables'. Each table can be thought of as like a separate dataframe. The table name we've just saved is `hospitals_zones_joined`.}

\endif
