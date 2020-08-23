---
title: "Introduction to Machine Learning Systems"
abstract: "This notebook introduces some of the challenges of building machine learning data systems. It will introduce you to concepts around joining of databases together. The storage and manipulation of data is at the core of machine learning systems and data science. The goal of this notebook is to introduce the reader to these concepts, not to authoritatively answer any questions about the state of Nigerian health facilities or Covid19, but it may give you ideas about how to try and do that in your own country."
layout: talk
author:
- given: Eric
  family: Meissner
  url: https://www.linkedin.com/in/meissnereric/
  twitter: meissner_eric_7 
- given: Andrei
  family: Paleyes
  url: https://www.linkedin.com/in/andreipaleyes/
- given: Neil D.
  family: Lawrence
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-07-24
ipynb: true
venue: Virtual DSA
transition: None
---

\include{talk-macros.tex}

\slides{\section{AI via ML Systems}

\include{_ai/includes/supply-chain-system.md}
\include{_ai/includes/aws-soa.md}
\include{_ai/includes/dsa-systems.md}
}


\notes{\subsection{Question}

In this notebook, we explore the question of health facility distribution in Nigeria, spatially, and in relation to population density.

We answer and visualize the question "How does the number of health facilities per capita vary across Nigeria?"

Rather than focussing purely on using tools like ```pandas``` to manipulate the data, our focus will be on introducing some concepts from databases.

Machine learning can be summarized as
$$
\text{model} + \text{data} \xrightarrow{\text{compute}} \text{prediction}
$$
and many machine learning courses focus a lot on the model part. But to build a machine learning system in practice, a lot of work has to be put into the data part. This notebook gives some pointers on that work and how to think about your machine learning systems design.}

\notes{
\subsection{Datasets}

In this notebook , we download 3 datasets: 
* Nigeria NMIS health facility data
* Population data for Administrative Zone 1 (states) areas in Nigeria
* Map boundaries for Nigerian states (for plotting and binning)
* Covid cases across Nigeria (as of May 20, 2020)

But joining these data sets together is just an example. As another example, you could think of [SafeBoda](https://safeboda.com/ng/), a ride-hailing app that's available in Lagos and Kampala. As well as looking at the health examples, try to imagine how SafeBoda may have had to design their systems to be scalable and reliable for storing and sharing data.}

\notes{
\subsection{Imports, Installs, and Downloads}

First, we're going to download some particular python libraries for dealing with geospatial data. We're dowloading [```geopandas```](https://geopandas.org) which will help us deal with 'shape files' that give the geographical lay out of Nigeria. We'll also download  [```pygeos```](https://pygeos.readthedocs.io/en/latest/), a library for dealing with points rapidly in python. And finally, to get a small database set up running quickly, we're installing [```csv-to-sqlite```](https://pypi.org/project/csv-to-sqlite/) which allows us to convert CSV data to a simple database.}

\notes{
\code{%pip install geopandas pygeos}
}

\notes{
\subsection{Databases and Joins}

The main idea we will be working with today is called the 'join'.  A join does exactly what it sounds like, it combines two database tables.

You have already started to look at data structures, in particular you have been learning about ```pandas``` which is a great way of storing and structuring your data set to make it easier to plot and manipulate your data.

Pandas is great for the data scientist to analyze data because it makes many operations easier. But it is not so good for building the machine learning system. In a machine learning system, you may have to handle a lot of data. Even if you start with building a system where you only have a few customers, perhaps you build an online taxi  system (like SafeBoda) for Kampala. Maybe you will have 50 customers. Then maybe your system can be handled with some python scripts and pandas.

\subsection{Scaling ML Systems}

But what if you are succesful? What if everyone in Kampala wants to use your system? There are 1.5 million people in Kampala and maybe 100,000 Boda Boda drivers.

What if you are even more succesful? What if everyone in Lagos wants to use your system? There are around 20 million people in Lagos ... and maybe as many Okada drivers as people in Kampala!

We want to build safe and reliable machine learning systems. Building them from pandas and python is about as safe and reliable as [taking six children to school on a boda boda](https://www.monitor.co.ug/News/National/Boda-accidents-kill-10-city-UN-report-Kampala/688334-4324032-15oru2dz/index.html).

To build a reliable system, we need to turn to *databases*. In this notebook [we'll be focussing on SQL databases](https://en.wikipedia.org/wiki/Join_(SQL)) and how you bring together different streams of data in a Machine Learning System.

In a machine learning system, you will need to bring different data sets together. In database terminology this is known as a 'join'. You have two different data sets, and you want to join them together. Just like you can join two pieces of metal using a welder, or two pieces of wood with screws.

But instead of using a welder or screws to join data, we join it using particular columns of the data. We can join data together using people's names. One database may contain where people live, another database may contain where they go to school. If we join these two databases we can have a database which shows where people live and where they got to school.

In the notebook, we will join together some data about where the health centres are in Nigeria and where the have been cases of Covid19. There are other challenges in the ML System Design that are not going to be covered here. They include: how to update the data bases, and how to control access to the data bases from different users (boda boda drivers, riders, administrators etc). }


\notes{
\subsection{Hospital Data}

The first and primary dataset we use is the NMIS health facility dataset, which contains data on the location, type, and staffing of health facilities across Nigeria. }

\notes{
\setupcode{import urllib.request
import pandas as pd}

\code{urllib.request.urlretrieve('https://energydata.info/dataset/f85d1796-e7f2-4630-be84-79420174e3bd/resource/6e640a13-cab4-457b-b9e6-0336051bac27/download/healthmopupandbaselinenmisfacility.csv', 'healthmopupandbaselinenmisfacility.csv')
hospital_data = pd.read_csv('healthmopupandbaselinenmisfacility.csv')}
}

\notes{It's always a good idea to inspect your data once it's downloaded to check it contains what you expect. In ```pandas``` you can do this with the ```.head()``` method. That allows us to see the first few entries of the ```pandas``` data structure.}

\notes{
\code{hospital_data.head()}
}

\notes{We can also check in ```pandas``` what the different columns of the data frame are to see what it contains. }

\notes{
\code{hospital_data.columns}
}

\notes{We can immiediately see that there are facility names, dates, and some characteristics of each health center such as number of doctors etc. As well as all that, we have two fields, ```latitude``` and ```longitude``` that likely give us the hospital locaiton. Let's plot them to have a look. }

\notes{
\setupcode{import matplotlib.pyplot as plt}

\code{plt.plot(hospital_data.longitude, hospital_data.latitude,'ro', alpha=0.01)}
}

\notes{There we have the location of these different hospitals. We set alpha in the plot to 0.01 to make the dots transparent, so we can see the locations of each health center.}


\notes{
\subsection{Administrative Zone Geo Data}

A very common operation is the need to map from locations in a country to the administrative regions. If we were building a ride sharing app, we might also want to map riders to locations in the city, so that we could know how many riders we had in different city areas.

Administrative regions have various names like cities, counties, districts or states. These conversions for the administrative regions are important for getting the right information to the right people.

Of course, if we had a knowlegdeable Nigerian, we could ask her about what the right location for each of these health facilities is, which state is it in? But given that we have the latitude and longitude, we should be able to find out automatically what the different states are. 

This is where "geo" data becomes important. We need to download a dataset that stores the location of the different states in Nigeria. These files are known as 'outline' files. Because the draw the different states of different countries in outline. 

There are special databases for storing this type of information, the database we are using is in the ```gdb``` or GeoDataBase format. It comes in a zip file. Let's download the outline files for the Nigerian states. They have been made available by the [Humanitarian Data Exchange](https://data.humdata.org/), you can also find other states data from the same site.}

\notes{
\setupcode{import zipfile}

\code{admin_zones_url = 'https://data.humdata.org/dataset/81ac1d38-f603-4a98-804d-325c658599a3/resource/0bc2f7bb-9ff6-40db-a569-1989b8ffd3bc/download/nga_admbnda_osgof_eha_itos.gdb.zip'
_, msg = urllib.request.urlretrieve(admin_zones_url, 'nga_admbnda_osgof_eha_itos.gdb.zip')
with zipfile.ZipFile('/content/nga_admbnda_osgof_eha_itos.gdb.zip', 'r') as zip_ref:
    zip_ref.extractall('/content/nga_admbnda_osgof_eha_itos.gdb')}
	}
\notes{Now we have this data of the outlines of the different states in Nigeria. 

The next thing we need to know is how these health facilities map onto different states in Nigeria. Without "binning" facilities somehow, it's difficult to effectively see how they are distributed across the country.

We do this by finding a "geo" dataset that contains the spatial outlay of Nigerian states by latitude/longitude coordinates. The dataset we use is of the "gdb" (GeoDataBase) type and comes as a zip file. We don't need to worry much about this datatype for this notebook, only noting that geopandas knows how to load in the dataset, and that it contains different "layers" for the same map. In this case, each layer is a  different degree of granularity of the political boundaries, with layer 0 being the whole country, 1 is by state, or 2 is by local government. We'll go with a state level view for simplicity, but as an excercise you can change it to layer 2 to view the distribution by local government. 

Once we have these ```MultiPolygon``` objects that define the boundaries of different states, we can perform a spatial join (sjoin) from the coordinates of individual health facilities (which we already converted to the appropriate ```Point``` type when moving the health data to a GeoDataFrame.)}

\notes{\subsection{Joining a GeoDataFrame}

The first database join we're going to do is a special one, it's a 'spatial join'. We're going to join together the locations of the hospitals with their states. 

This join is unusual because it requires some mathematics to get right. The outline files give us the borders of the different states in latitude and longitude, the health facilities have given locations in the country. 

A spatial join involves finding out which state each health facility belongs to. Fortunately, the mathematics you need is already programmed for you in GeoPandas. That means all we need to do is convert our ```pandas``` dataframe of health facilities into a ```GeoDataFrame``` which allows us to do the spatial join. }

\notes{
\setupcode{import geopandas as gpd}
\code{hosp_gdf = gpd.GeoDataFrame(
    hospital_data, geometry=gpd.points_from_xy(hospital_data.longitude, hospital_data.latitude))
hosp_gdf.crs = "EPSG:4326"}
}

\notes{There are some technial details here: the  ```crs``` refers to the coordinate system in use by a particular GeoDataFrame. ```EPSG:4326``` is the standard coordinate system of latitude/longitude.}

\notes{\subsection{Your First Join: Converting GPS Coordinates to States}

Now we have the data in the ```GeoPandas``` format, we can start converting into states. We will use the [```fiona```](https://pypi.org/project/Fiona/) library for reading the right layers from the files. Before we do the join, lets plot the location of health centers and states on the same map.}

\notes{
\setupcode{import fiona}

\code{states_file = "/content/nga_admbnda_osgof_eha_itos.gdb/nga_admbnda_osgof_eha_itos.gdb/nga_admbnda_osgof_eha_itos.gdb/nga_admbnda_osgof_eha_itos.gdb/"

# geopandas included map, filtered to just Nigeria
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.crs = "EPSG:4326"
nigeria = world[(world['name'] == 'Nigeria')]
base = nigeria.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))

layers = fiona.listlayers(states_file)
zones_gdf = gpd.read_file(states_file, layer=1)
zones_gdf.crs = "EPSG:4326"
zones_gdf = zones_gdf.set_index('admin1Name_en')
zones_gdf.plot(ax=base, color='white', edgecolor='black')

# We can now plot our ``GeoDataFrame``.
hosp_gdf.plot(ax=base, color='b', alpha=0.02, )

plt.show()}
}

\notes{\subsection{Performing the Spatial Join}

We've now plotted the different health center locations across the states. You can clearly see that each of the dots falls within a different state. For helping the visualisation, we've made the dots somewhat transparent (we set the ```alpha``` in the plot). This means that we can see the regions where there are more health centers, you should be able to spot where the major cities in Nigeria are given the increased number of health centers in those regions.

Of course, we can now see by eye, which of the states each of the health centers belongs to. But we want the computer to do our join for us. ```GeoPandas``` provides us with the spatial join. Here we're going to do a [```left``` or ```outer``` join](https://en.wikipedia.org/wiki/Join_(SQL)#Left_outer_join). }

\notes{
\setupcode{from geopandas.tools import sjoin}
}

\notes{We have two GeoPandas data frames, ```hosp_gdf``` and ```zones_gdf```. Let's have a look at the columns the contain.}

\notes{
\code{hosp_gdf.columns}
}

\notes{We can see that this is the GeoDataFrame containing the information about the hospital. Now let's have a look at the ```zones_gdf``` data frame.}

\notes{
\code{zones_gdf.columns}
}

\notes{You can see that this data frame has a different set of columns. It has all the different administrative regions. But there is one column name that overlaps. We can find it by looking for the intersection between the two sets.}

\notes{
\code{set(hosp_gdf.columns).intersection(set(zones_gdf.columns))}
}

\notes{Here we've converted the lists of columns into python 'sets', and then looked for the intersection. The *join* will occur on the intersection between these columns. It will try and match the geometry of the hospitals (their location) to the geometry of the states (their outlines). This match is done in one line in GeoPandas.

We're having to use GeoPandas because this join is a special one based on geographical locations, if the join was on customer name or some other discrete variable, we could do the join in pandas or directly in SQL. }

\notes{
\code{hosp_state_joined = sjoin(hosp_gdf, zones_gdf, how='left')}
}

\notes{The intersection of the two data frames indicates how the two data frames will be joined (if there's no intersection, they can't be joined). It's like indicating the two holes that would need to be bolted together on two pieces of metal. If the holes don't match, the join can't be done. There has to be an intersection. 

But what will the result look like? Well the join should be the 'union' of the two data frames. We can have a look at what the union should be by (again) converting the columns to sets.}

\notes{
\code{set(hosp_gdf.columns).union(set(zones_gdf.columns))}
}

\notes{That gives a list of all the columns (notice that 'geometry' only appears once). 

Let's check that's what the join command did, by looking at the columns of our new data frame, ```hosp_state_joined```. Notice also that there's a new column: ```index_right```. The two original data bases had separate indices. The ```index_right``` column represents the index from the ```zones_gdf```, which is the Nigerian state.}

\notes{
\code{set(hosp_state_joined.columns)}
}

\notes{Great! They are all there! We have completed our join. We had two separate data frames with information about states and information about hospitals. But by performing an 'outer' or a 'left' join, we now have a single data frame with all the information in the same place! Let's have a look at the first frew entries in the new data frame.}

\notes{
\code{hosp_state_joined.head()}
}

\notes{\subsection{SQL Database}

Our first join was a special one, because it involved spatial data. That meant using the special ```gdb``` format and the ```GeoPandas``` tool for manipulating that data. But we've now saved our updated data in a new file. 

To do this, we use the command line utility that comes standard for SQLite database creation. SQLite is a simple database that's useful for playing with database commands on your local machine. For a real system, you would need to set up a server to run the database. The server is a separate machine with the job of answering database queries. SQLite pretends to be a proper database, but doesn't require us to go to the extra work of setting up a server. Popular SQL server software includes [```MySQL```](https://www.mysql.com/) which is free or [Microsoft's SQL Server](https://www.microsoft.com/en-gb/sql-server/sql-server-2019).

A typical machine learning installation might have you running a database from a cloud service (such as AWS, Azure or Google Cloud Platform). That cloud service would host the database for you and you would pay according to the number of queries made. 

Many start-up companies were formed on the back of a ```MySQL``` server hosted on top of AWS. You can [read how to do that here](https://aws.amazon.com/getting-started/hands-on/create-mysql-db/).

If you were designing your own ride hailing app, or any other major commercial software you would want to investigate whether you would need to set up a central SQL server in one of these frameworks.

Today though, we'll just stick to SQLite which gives you a sense of the database without the time and expense of setting it up on the cloud. As well as showing you the SQL commands (which is often what's used in a production ML system) we'll also give the equivalent ```pandas``` commands, which would often be what you would use when you're doing data analysis in ```python``` and ```Jupyter```.}

\notes{\subsection{Create the SQLite Database}

The beautiful thing about SQLite is that it allows us to play with SQL without going to the work of setting up a proper SQL server. Creating a data base in SQLite is as simple as writing a new file. To create the database, we'll first write our joined data to a CSV file, then we'll use a little utility to convert our hospital database into a SQLite database.
}

\notes{\code{hosp_state_joined.to_csv('facilities.csv')}}

\notes{\code{%pip install csv-to-sqlite}}

\notes{\code{!csv-to-sqlite -f facilities.csv -t full -o db.sqlite}}

\notes{Rather than being installed on a separate server, SQLite simply stores the database locally in a file called ```db.sqlite```.

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

To access a data base, the first thing that is made is a connection. Then SQL is used to extract the information required. A typical SQL command is ```SELECT```. It allows us to extract rows from a given table. It operates a bit like the ```.head()``` method in ```pandas```, it will return the first ```N``` rows (by default the ```.head()``` command returns the first 5 rows, but you can set ```n``` to whatever you like. Here we've included a default value of 5 to make it match the ```pandas``` command.

The python library, ```sqlite3```, allows us to access the SQL database directly from python. We do this using an ```execute``` command on the connection. 

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

\notes{Let's have a go at calling the command to extract the first three facilities from our health center database. Let's try creating a function that does the same thing the pandas .head() method does so we can inspect our database.}

\notes{
\setupcode{def head(conn, table, n=5):
  rows = select_top(conn, table, n)
  for r in rows:
      print(r)}
	  
\code{head(conn, 'facilities')}
}

\notes{Great! We now have the data base in SQLite, and some python functions that operate on the data base by wrapping SQL commands.

We will return to the SQL command style after download and add the other datasets to the database using a combination of ```pandas``` and the ```csv-to-sqlite``` utility.

Our next task will be to introduce data on COVID19 so that we can join that to our other data sets.}

\notes{\subsection{Covid Data}

Now we have the health data, we're going to combine it with [data about COVID-19 cases in Nigeria over time](https://github.com/dsfsi/covid19africa). This data is kindly provided by Africa open COVID-19 data working group, which Elaine Nsoesie has been working with. The data is taken from Twitter, and only goes up until May 2020. 

They provide their data in github. We can access the cases we're interested in from the following URL.

For convenience, we'll load the data into pandas first, but our next step will be to create a new SQLite table containing the data. Then we'll join that table to our existing tables.}

\notes{
\code{covid_data_url = 'https://raw.githubusercontent.com/dsfsi/covid19africa/master/data/line_lists/line-list-nigeria.csv'
covid_data_csv = 'cases.csv'
urllib.request.urlretrieve(covid_data_url, covid_data_csv)
covid_data = pd.read_csv(covid_data_csv)
}}

\notes{As normal, we should inspect our data to check that it contains what we expect. }

\notes{\code{covid_data.head()}}

\notes{And we can get an idea of all the information in the data from looking at the columns.}

\notes{\code{covid_data.columns}}

\notes{Now we convert this CSV file we've downloaded into a new table in the database file. We can do this, again, with the csv-to-sqlite script.}

\notes{\code{!csv-to-sqlite -f cases.csv -t full -o db.sqlite}}

\notes{\subsection{Population Data}

Now we have information about COVID cases, and we have information about how many health centers and how many doctors and nurses there are in each health center. But unless we understand how many people there are in each state, then we cannot make decisions about where they may be problems with the disease. 

If we were running our ride hailing service, we would also need information about how many people there were in different areas, so we could understand what the *demand* for the boda boda rides might be.

To access the number of people we can get population statistics from the [Humanitarian Data Exchange](https://data.humdata.org/).

We also want to have population data for each state in Nigeria, so that we can see attributes like whether there are zones of high health facility density but low population density.}

\notes{\code{pop_url = 'https://data.humdata.org/dataset/a7c3de5e-ff27-4746-99cd-05f2ad9b1066/resource/d9fc551a-b5e4-4bed-9d0d-b047b6961817/download/nga_pop_adm1_2016.csv'
_, msg = urllib.request.urlretrieve(pop_url,'nga_pop_adm1_2016.csv')
pop_data = pd.read_csv('nga_pop_adm1_2016.csv')}}

\notes{\code{pop_data.head()}}

\notes{To do joins with this data, we must first make sure that the columns have the right names. The name should match the same name of the column in our existing data. So we reset the column names, and the name of the index, as follows.}

\notes{\code{pop_data.columns = ['admin1Name_en', 'admin1Pcode', 'admin0Name_en', 'admin0Pcode', 'population']
pop_data = pop_data.set_index('admin1Name_en')}}

\notes{When doing this for real world data, you should also make sure that the names used in the rows are the same across the different data bases. For example, has someone decided to use an abbreviation for 'Federal Capital Territory' and set it as 'FCT'. The computer won't understand these are the same states, and if you do a join with such data you can get duplicate entries or missing entries. This sort of thing happens a lot in real world data and takes a lot of time to sort out. Fortunately, in this case, the data is well curated and we don't have these problems.}

\notes{\subsection{Save to database file}

The next step is to add this new CSV file as an additional table in our SQLite database. This is done using the script as before.}

\notes{\code{pop_data.to_csv('pop_data.csv')}}

\notes{\code{!csv-to-sqlite -f pop_data.csv -t full -o db.sqlite}}

\notes{\subsection{Computing per capita hospitals and COVID}

The Minister of Health in Abuja may be interested in which states are most vulnerable to COVID19. We now have all the information in our SQL data bases to compute what our health center provision is per capita, and what the COVID19 situation is.

To do this, we will use the ```JOIN``` operation from SQL and introduce a new operation called ```GROUPBY```.}

\notes{#### Joining in Pandas

As before, these operations can be done in pandas or GeoPandas. Before we create the SQL commands, we'll show how you can do that in pandas.

In pandas, the equivalent of a database table is a dataframe. So the JOIN operation takes two dataframes and joins them based on the key. The key is that special shared column between the two tables. The place where the 'holes align' so the two databases can be joined together.

In GeoPandas we used an outer join. In an outer join you keep all rows from both tables, even if there is no match on the key. In an inner join, you only keep the rows if the two tables have a matching key.

This is sometimes where problems can creep in. If in one table Abuja's state is encoded as 'FCT' or 'FCT-Abuja', and in another table it's encoded as 'Federal Capital Territory', they won't match and that data wouldn't appear in the joined table.

In simple terms, a JOIN operation takes two tables (or dataframes) and combines them based on some key, in this case the index of the Pandas data frame which is the state name.}

\notes{\code{pop_joined = zones_gdf.join(pop_data['population'], how='inner')}}

\notes{\subsection{GroupBy in Pandas}

Our COVID19 data is in the form of individual cases. But we are interested in total case counts for each state. There is a special data base operation known as ```GROUP BY``` for collecting information about the individual states. The type of information you might want could be a sum, the maximum value, an average, the minimum value. We can use a GroupBy operation in ```pandas``` and SQL to summarize the counts of covid cases in each state. 

A ```GROUPBY``` operation groups rows with the same key (in this case 'province/state') into separate objects, that we can operate on further such as to count the rows in each group, or to sum or take the mean over the values in some column (imagine each case row had the age of the patient, and you were interested in the mean age of patients.)}

\notes{\code{covid_cases_by_state = covid_data.groupby(['province/state']).count()['case_id']}}

\notes{The ```.groupby()``` method on the dataframe has now given us a new data series that contains the total number of covid cases in each state. We can examine it to check we have something sensible.}

\notes{\code{covid_cases_by_state}}

\notes{Now we have this new data series, it can be added to the pandas data frame as a new column.}

\notes{\code{pop_joined['covid_cases_by_state'] = covid_cases_by_state}}

\notes{The spatial join we did on the original data frame to obtain hosp_state_joined introduced a new column, index_right which contains the state of each of the hospitals. Let's have a quick look at it below.}

\notes{\code{hosp_state_joined['index_right']}

\notes{To count the hospitals in each of the states, we first create a grouped series where we've grouped on these states.}

\notes{\code{grouped = hosp_state_joined.groupby('index_right')}}

\notes{This python operation now goes through each of the groups and counts how many hospitals there are in each state. It stores the result in a dictionary. If you're new to Python, then to understand this code you need to understand what a 'dictionary comprehension' is. In this case the dictionary comprehension is being used to create a python dictionary of states and total hospital counts. That's then being converted into a ```pandas``` Data Series and added to the ```pop_joined``` dataframe.}

\notes{\code{counted_groups = {k: len(v) for k, v in grouped.groups.items()}
pop_joined['hosp_state'] = pd.Series(counted_groups)}}

\notes{For convenience, we can now add a new data series to the data frame that contains the per capita information about hospitals. that makes it easy to retrieve later.}

\notes{\code{pop_joined['hosp_per_capita_10k'] = (pop_joined['hosp_state'] * 10000 )/ pop_joined['population']}}

\notes{\subsection{SQL-style}

That's the ```pandas``` approach to doing it. But ```pandas``` itself is inspired by database language, in particular relational databases such as SQL. To do these types of joins at scale, e.g. for our ride hailing app, we need to see how to do these joins in a database.

As before, we'll wrap the underlying SQL commands with a convenient python command. 

What you see below gives the full SQL command. There is a [```SELECT``` command](https://www.w3schools.com/sql/sql_select.asp), which extracts ```FROM``` a particular table. It then completes an [```INNER JOIN```](https://www.w3schools.com/sql/sql_join_inner.asp) using particular columns (```provice/state``` and ```index_right```)}

\helpercode{def join_counts(conn):
    """
    Calculate counts of cases and facilities per state, join results
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT ct.[province/state] as [state], ct.[case_count], ft.[facility_count]
                FROM
                    (SELECT [province/state], COUNT(*) as [case_count] FROM [cases] GROUP BY [province/state]) ct
                INNER JOIN 
                    (SELECT [index_right], COUNT(*) as [facility_count] FROM [facilities] GROUP BY [index_right]) ft
                ON
                    ct.[province/state] = ft.[index_right]
                """)

    rows = cur.fetchall()
    return rows}}

\notes{Now we've created our python wrapper, we can connect to the data base and run our SQL command on the database using the wrapper.}

\notes{\code{conn = create_connection("db.sqlite")}}

\notes{\code{state_cases_hosps = join_counts(conn)}}

\notes{\code{for row in state_cases_hosps:
    print("State {} \t\t Covid Cases {} \t\t Health Facilities {}".format(row[0], row[1], row[2]))}}
	

\notes{\code{base = nigeria.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='population', edgecolor='black', legend=True)
base.set_title("Population of Nigerian States")}}

\notes{\code{base = nigeria.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='hosp_per_capita_10k', edgecolor='black', legend=True)
base.set_title("Hospitals Per Capita (10k) of Nigerian States")}}

\notes{\subsection{Exercise}

1. Add a new column the dataframe for covid cases per 10,000 population, in the same way we computed health facilities per 10k capita.

2. Add a new column for covid cases per health facility. 

Do this in both the SQL and the Pandas styles to get a feel for how they differ.}

\notes{\code{# pop_joined['cases_per_capita_10k'] = ???
# pop_joined['cases_per_facility'] = ???}

\notes{\code{base = nigeria.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='cases_per_capita_10k', edgecolor='black', legend=True)
base.set_title("Covid Cases Per Capita (10k) of Nigerian States")}}

\notes{\code{base = nigeria.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='covid_cases_by_state', edgecolor='black', legend=True)
base.set_title("Covid Cases by State")}}

\notes{\code{base = nigeria.plot(color='white', edgecolor='black', alpha=0, figsize=(11, 11))
pop_joined.plot(ax=base, column='cases_per_facility', edgecolor='black', legend=True)
base.set_title("Covid Cases per Health Facility")}}

\thanks



\references
