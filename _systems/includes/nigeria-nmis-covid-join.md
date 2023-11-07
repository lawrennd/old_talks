\ifndef{nigerianNmisCovidJoin}
\define{nigerianNmisCovidJoin}


\editme

\notes{\subsection{Covid Data}

Now we have the health data, we're going to combine it with [data about COVID-19 cases in Nigeria over time](https://github.com/dsfsi/covid19africa). This data is kindly provided by Africa open COVID-19 data working group, which [Elaine Nsoesie](https://www.bu.edu/sph/profile/elaine-nsoesie/) has been working with. The data is taken from Twitter, and only goes up until May 2020. 

They provide their data in GitHub. We can access the cases we're interested in from the following URL.

<https://raw.githubusercontent.com/dsfsi/covid19africa/master/data/line_lists/line-list-nigeria.csv>

For convenience, we'll load the data into pandas first, but our next step will be to create a new SQLite table containing the data. Then we'll join that table to our existing tables.}

\include{_datasets/includes/nigerian-covid-data.md}

\ifeq{\databaseType}{sqlite}
\code{covid_data=data
covid_data.to_csv('cases.csv')}
\else
 \ifeq{\databaseType}{mariadb}
\code{covid_data=data
covid_data.to_csv('cases.csv', header=None)}
  \endif
\endif

\notes{Now we convert this CSV file we've downloaded into a new table in the database file.}
\ifeq{\databaseType}{sqlite}
\notes{We can do this, again, with the csv-to-sqlite script.}

\code{!csv-to-sqlite -f cases.csv -t full -o db.sqlite}
\else
  \ifeq{\databaseType}{mariadb}
\notes{Once again we have to construct a schema for the data.}
\code{%%sql
--
-- Table structure for table `cases`
--
DROP TABLE IF EXISTS `cases`;
CREATE TABLE IF NOT EXISTS `cases` (
  `index` int(10) unsigned NOT NULL,
  `case_id` int(10) unsigned NOT NULL,
  `origin_case_id` int(10) unsigned NOT NULL,
  `date` date NOT NULL,
  `age` int(10),
  `gender` tinytext COLLATE utf8_bin NOT NULL,
  `city` tinytext COLLATE utf8_bin NOT NULL,
  `province/state` tinytext COLLATE utf8_bin NOT NULL,
  `country` tinytext COLLATE utf8_bin NOT NULL,
  `current_status` tinytext COLLATE utf8_bin,
  `source` text COLLATE utf8_bin,
  `symptoms` text COLLATE utf8_bin,
  `date_onset_symptoms` date,
  `date_admission_hospital` date,
  `date_confirmation` date,
  `underlying_conditions` text COLLATE utf8_bin,
  `travel_history_dates` text COLLATE utf8_bin,
  `travel_history_location` text COLLATE utf8_bin,
  `death_date` date,
  `notes_for_discussion` text COLLATE utf8_bin,
  `Unnamed: 19` text COLLATE utf8_bin
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;}

\notes{Once again we need to set the index.}

\code{%%sql
--
-- Indexes for table `cases`
--
ALTER TABLE `cases`
 ADD PRIMARY KEY (`index`);}
 
\notes{And now we can load the data into the table.}

\code{%%sql
LOAD DATA LOCAL INFILE 'cases.csv' INTO TABLE cases
FIELDS TERMINATED BY ','
LINES STARTING BY '' TERMINATED BY '\n';}

  \endif
\endif

\include{_datasets/includes/nigerian-population-data.md}

\code{pop_data=data}

\notes{When doing this for real world data, you should also make sure that the names used in the rows are the same across the different data bases. For example, has someone decided to use an abbreviation for 'Federal Capital Territory' and set it as 'FCT'. The computer won't understand these are the same states, and if you do a join with such data, you can get duplicate entries or missing entries. This sort of thing happens a lot in real world data and takes a lot of time to sort out. Fortunately, in this case, the data is well curated, and we don't have these problems.}

\notes{\subsection{Save to database file}

The next step is to add this new CSV file as an additional table in our database.}

\include{_systems/includes/nigerian-population-data-sql.md}


\notes{\subsection{Computing per capita hospitals and COVID}

The Minister of Health in Abuja may be interested in which states are most vulnerable to COVID19. We now have all the information in our SQL data bases to compute what our health center provision is per capita, and what the COVID19 situation is.

To do this, we will use the `JOIN` operation from SQL and introduce a new operation called `GROUPBY`.}

\notes{\subsubsection{Joining in Pandas}

As before, these operations can be done in pandas or GeoPandas. Before we create the SQL commands, we'll show how you can do that in pandas.

In `pandas`, the equivalent of a database table is a dataframe. So, the JOIN operation takes two dataframes and joins them based on the key. The key is that special shared column between the two tables. The place where the 'holes align' so the two databases can be joined together.

In GeoPandas we used an outer join. In an outer join you keep all rows from both tables, even if there is no match on the key. In an inner join, you only keep the rows if the two tables have a matching key.

This is sometimes where problems can creep in. If in one table Abuja's state is encoded as 'FCT' or 'FCT-Abuja', and in another table it's encoded as 'Federal Capital Territory', they won't match, and that data wouldn't appear in the joined table.

In simple terms, a JOIN operation takes two tables (or dataframes) and combines them based on some key, in this case the index of the Pandas data frame which is the state name.}

\code{zones_gdf.set_index("admin1Name_en", inplace=True)
pop_joined = zones_gdf.join(pop_data['population'], how='inner')}

\notes{\subsection{GroupBy in Pandas}

Our COVID19 data is in the form of individual cases. But we are interested in total case counts for each state. There is a special data base operation known as `GROUP BY` for collecting information about the individual states. The type of information you might want could be a sum, the maximum value, an average, the minimum value. We can use a GroupBy operation in `pandas` and SQL to summarize the counts of covid cases in each state. 

A `GROUPBY` operation groups rows with the same key (in this case 'province/state') into separate objects, that we can operate on further such as to count the rows in each group, or to sum or take the mean over the values in some column (imagine each case row had the age of the patient, and you were interested in the mean age of patients.)}

\code{covid_cases_by_state = covid_data.groupby(['province/state']).count()['case_id']}

\notes{The ```.groupby()``` method on the dataframe has now given us a new data series that contains the total number of covid cases in each state. We can examine it to check we have something sensible.}

\code{covid_cases_by_state}

\notes{Now we have this new data series, it can be added to the pandas dataframe as a new column.}

\code{pop_joined['covid_cases_by_state'] = covid_cases_by_state}

\notes{The spatial join we did on the original data frame to obtain hosp_state_joined introduced a new column, `index_right` that contains the state of each of the hospitals. Let's have a quick look at it below.}

\code{hosp_state_joined['index_right']}

\notes{To count the hospitals in each of the states, we first create a grouped series where we've grouped on these states.}

\code{grouped = hosp_state_joined.groupby('admin1Name_en')}

\notes{This python operation now goes through each of the groups and counts how many hospitals there are in each state. It stores the result in a dictionary. If you're new to python, then to understand this code you need to understand what a 'dictionary comprehension' is. In this case the dictionary comprehension is being used to create a python dictionary of states and total hospital counts. That's then being converted into a `pandas` Data Series and added to the `pop_joined` dataframe.}

\setupcode{import pandas as pd}

\code{counted_groups = {k: len(v) for k, v in grouped.groups.items()}
pop_joined['hosp_state'] = pd.Series(counted_groups)}

\notes{For convenience, we can now add a new data series to the data frame that contains the per capita information about hospitals. that makes it easy to retrieve later.}

\code{pop_joined['hosp_per_capita_10k'] = (pop_joined['hosp_state'] * 10000 )/ pop_joined['population']}

\notes{\subsection{SQL-style}

That's the `pandas` approach to doing it. But `pandas` itself is inspired by database languages, in particular relational databases such as SQL. To do these types of joins at scale, e.g., for a ride hailing app, we need to do these joins in a database.

As before, we'll wrap the underlying SQL commands with a convenient python command. 

What you see below gives the full SQL command. There is a [`SELECT` command](https://www.w3schools.com/sql/sql_select.asp), which extracts `FROM` a particular table. It then completes an [`INNER JOIN`](https://www.w3schools.com/sql/sql_join_inner.asp) using particular columns (`province/state` and `admin1Name_en`)}

\helpercode{def join_counts(conn):
    """
    Calculate counts of cases and facilities per state, join results
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT ct.`province/state` as state, ct.case_count, ft.facility_count
                FROM
                    (SELECT `province/state`, COUNT(*) as case_count FROM cases GROUP BY `province/state`) ct
                INNER JOIN 
                    (SELECT admin1Name_en, COUNT(*) as facility_count FROM hospitals_zones_joined GROUP BY admin1Name_en) ft
                ON
                    ct.`province/state` = ft.admin1Name_en
                """)

    rows = cur.fetchall()
    return rows}

\notes{Now we've created our python wrapper, we can connect to the data base and run our SQL command on the database using the wrapper.}

\ifeq{\databaseType}{sqlite}
\code{conn = create_connection("db.sqlite")}
\else
  \ifeq{\databaseType}{mariadb}
\code{conn = create_connection(user=credentials["username"], 
                         password=credentials["password"],
			 host=database_details["url"],
			 database="nigeria_nmis")}
  \endif
\endif
\code{state_cases_hosps = join_counts(conn)}

\code{for row in state_cases_hosps:
    print("State {} \t\t Covid Cases {} \t\t Health Facilities {}".format(row[0], row[1], row[2]))}
	

\code{base = nigeria_gdf.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='population', edgecolor='black', legend=True)
base.set_title("Population of Nigerian States")}

\code{base = nigeria_gdf.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='hosp_per_capita_10k', edgecolor='black', legend=True)
base.set_title("Hospitals Per Capita (10k) of Nigerian States")}


\codeassignment{Add a new column the dataframe for covid cases per 10,000 population, in the same way we computed health facilities per 10k capita.}{}{10}

\codeassignment{Add a new column for covid cases per health facility.}{}{10}

\codeassignment{Do this in both the SQL and the Pandas styles to get a feel for how they differ.}{}{10}

\codeassignment{Perform an inner join using SQL on your databases and convert the result into a `pandas` DataFrame.}{}{10}


\code{
# pop_joined['cases_per_capita_10k'] = ???
# pop_joined['cases_per_facility'] = ???
}

\notes{\code{base = nigeria_gdf.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='cases_per_capita_10k', edgecolor='black', legend=True)
base.set_title("Covid Cases Per Capita (10k) of Nigerian States")}}

\notes{\code{base = nigeria_gdf.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='covid_cases_by_state', edgecolor='black', legend=True)
base.set_title("Covid Cases by State")}}

\notes{\code{base = nigeria_gdf.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='cases_per_facility', edgecolor='black', legend=True)
base.set_title("Covid Cases per Health Facility")}}

\endif
