\ifndef{nigeriaNmisSpatialJoin}
\define{nigeriaNmisSpatialJoin}

\editme

\notes{
\subsection{Administrative Zone Geo Data}

A very common operation is the need to map from locations in a country to the administrative regions. If we were building a ride sharing app, we might also want to map riders to locations in the city, so that we could know how many riders we had in different city areas.

Administrative regions have various names like cities, counties, districts or states. These conversions for the administrative regions are important for getting the right information to the right people.

Of course, if we had a knowlegdeable Nigerian, we could ask her about what the right location for each of these health facilities is, which state is it in? But given that we have the latitude and longitude, we should be able to find out automatically what the different states are. 

This is where "geo" data becomes important. We need to download a dataset that stores the location of the different states in Nigeria. These files are known as 'outline' files. Because they draw the different states of different countries in outline. 

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

\endif
