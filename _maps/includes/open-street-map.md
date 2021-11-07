\ifndef{openStreetMap}
\define{openStreetMap}

\editme


\subsection{Accessing Open Street Map}

\installcode{osmnx}

\setupcode{import osmnx as ox
import matplotlib.pyplot as plt}

\notes{We will center out download on the city of Lagos, which has the following latitude and longitude.}


\code{place_name = "Lagos, Nigeria"

latitude = 6.5244 # Lagos latitude
longitude = 3.3792 # Lagos longitude}

\code{place_name = "Kampala, Uganda"

latitude = 0.347596 # Kampala latitude
longitude = 32.582520 # Kampala langitude}

\code{placestub = place_name.lower().replace(' ', '-').replace(',','')}

\notes{We'll create a bounding box which is 0.2 degrees wide, 1 degree is around 111km ([circumference of the Earth is around 40,000 km](https://en.wikipedia.org/wiki/Metre) and 40,000/360=111km).}

\code{box_width = 0.2 # About 22 km
box_height = 0.2
north = latitude + box_height/2
south = latitude - box_width/2
west = longitude - box_width/2
east = longitude + box_width/2}

\notes{Now we'll download a set of points of interest from OpenStreetMap. We can specify the points of interest we're interested in by building a small dictionary containing their labels as follows.}

\code{# Retrieve POIs
tags = {"amenity": True, 
        "buildings": True, 
		"historic": True, 
		"leisure": True, 
		"shop": True, 
		"tourism": True}}

\notes{Now we can use `osmx` to download all such points of interest within a given bounding baox.}

\code{pois = ox.geometries_from_bbox(north, south, east, west, tags)}

\notes{That operation can take some time, particularly as the bounding box grows larger. Once it is complete we can check how many points of interest we have found.}

\code{print("There are {number} points of interest surrounding {placename} latitude: {latitude}, longitude: {longitude}".format(number=len(pois), placename=place_name, latitude=latitude, longitude=longitude))

\notes{And then we can examine their contents in more detail.}

\code{pois.info}

\notes{We notice a few things.

1. Points of interest do not have a consistent OpenStreetMap `element_type`, some are `node`, others are `relation` and we also have `way`. You can find out more about elements in OpenStreetMap on [this wiki page](https://wiki.openstreetmap.org/wiki/Elements). This will become important when tidying up the data for next stage processing.

2. Many of the values are missing. In SQL we would express a missing value as `NULL`. But in `pandas` a missing value is expressed as not-a-number, `NaN`. This is quite a common standard, but it is not the only standard. Sometimes data is collected and coded with an "unreasonable" value for a missing value. For example, someone might set missing values for heights to -999. The concept is that this is an obviously void "height" and would trigger a human user to check whether it's a missing value. Of course, this is obvious to humans, but not necessarily to a computer!

3. }

\notes{Nodes, ways and relations in OpenStreetMap all have different *keys* associated with them. The data is not structured in standard database columns. Different points of interest might have different keys present or absent. The `gdf` we recover places these keys in its columns, but if }

\notes{So we might be interested in the following keys.}

\code{keys = ["name",
        "addr:city",
        "addr:postcode",
        "amenity",
        "building",
        "building:name",
        "building:colour",
        "building:material",
        "historic",
		"memorial",
        "religion",
        "tourism",
        "emergency",
        "leisure",
        "shop"]}

\notes{But our downloaded `gdf` may have fewer keys.}

\code{pois.columns.values}

\notes{We can write a short piece of code to discover which keys are missing drom the data frame's columns.}

\code{for key in keys:
    if key not in pois.columns:
        print(key)
        
present_keys = [key for key in keys if key in pois.columns]
pois[present_keys]}

\notes{This gives us the relevant points of interest (part of the map). If we'd like to see the entire street network, we can download the entire graph from the location.}

\code{graph = ox.graph_from_bbox(north, south, east, west)

# Retrieve nodes and edges
nodes, edges = ox.graph_to_gdfs(graph)

# Get place boundary related to the place name as a geodataframe
area = ox.geocode_to_gdf(place_name)}

\notes{Which we can then render as follows.}

\notes{<https://towardsdatascience.com/4-must-have-jupyterlab-extensions-for-geospatial-data-science-f3cf7822de4b>}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)

# Plot the footprint
area.plot(ax=ax, facecolor="white")

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor="dimgray")

# Plot buildings
#buildings.plot(ax=ax, facecolor="silver", alpha=0.7)

# Plot all POIs in Lagos
pois.plot(ax=ax, color="blue", alpha=0.7, markersize=10)
plt.tight_layout()
mlai.write_figure(directory="\writeDiagramsDir/maps", filename=placestub+"-pois.png")}

\figure{\includepng{\diagramsDir/maps/kampala-uganda-pois}{40%}}{Points of Interest as identified in Open Street Map.}{kampala-uganda-pois}


\code{tourist_places = pois[pois.tourism.notnull()]}

\plotcode{# Plot a subset of the POIs (e.g., tourist places)
# Create figure
fig, ax = plt.subplots(figsize=plot.big_figsize)

# Plot the footprint
area.plot(ax=ax, facecolor="white")

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor="dimgray")

# Plot tourist places 
tourist_places.plot(ax=ax, color="blue", alpha=1, markersize=50)
plt.tight_layout()
mlai.write_figure(directory="\writeDiagramsDir/maps", filename=placestub + "-tourist-sites.png")}

\figure{\includepng{\diagramsDir/maps/lagos-tourist-sites}{40%}}{Tourist sites identified as Points of Interest in Open Street Map.}{lagos-tourist-sites}


\notes{We have the POIs that are associated with tourist places in a geodataframe. To work with them in a machine learning algorithm, it will be easier to conveert them to a `pandas` DataFrame. This means dealing with the geometry. If we examine the POIs.}


\notes{TK: Plot health centers from the NMIS data}

\code{tourist_places.loc["node"]}

\code{for i in tourist_places["geometry"]["way"]:
    print("latitude: {latitude}, longitude: {longitude}".format(latitude=i.centroid.y, longitude=i.centroid.x))}



\endif
