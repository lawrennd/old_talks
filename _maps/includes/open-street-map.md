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

\notes{We'll create a bounding box which is 0.2 degrees wide, 1 degree is around 111km ([circumference of the Earth is around 40,000 km](https://en.wikipedia.org/wiki/Metre) and 40,000/360=111km).}

\code{box_width = 0.2 # About 22 km
box_height = 0.2
north = latitude + box_height/2
south = latitude - box_width/2
west = longitude - box_width/2
east = longitude + box_width/2}

\code{# Retrieve POIs
tags = {"amenity": True, 
        "buildings": True, 
		"historic": True, 
		"leisure": True, 
		"shop": True, 
		"tourism": True}
pois = ox.geometries_from_bbox(north, south, east, west, tags)}


\code{# How many POIs do we have?
print("There are {number} points of interest surrounding latitude: {latitude}, longitude: {longitude}".format(number=len(pois), latitude=latitude, longitude=longitude))
pois.info}

\code{pois.columns.values}

\code{cols = ["name","addr:city","addr:postcode","amenity","building","building:name","building:colour","building:material","historic","memorial","religion","tourism","emergency","leisure","shop"]
# Print only selected cols
pois[cols]}

\code{# Get map data.
# Fetch OSM street network from the location
graph = ox.graph_from_bbox(north, south, east, west)

# Retrieve nodes and edges
nodes, edges = ox.graph_to_gdfs(graph)

# Get place boundary related to the place name as a geodataframe
area = ox.geocode_to_gdf(place_name)}

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
mlai.write_figure(directory="\writeDiagramsDir/maps", filename="lagos-pois.svg"}

\figure{\includediagram{\diagramsDir/maps/lagos-pois}{40%}}{Points of Interest in Lagos as identified in Open Street Map.}{lagos-pois}


\plotcode{# Plot a subset of the POIs (e.g., tourist places)
# Create figure
fig, ax = plt.subplots(figsize=plot.big_figsize)

# Plot the footprint
area.plot(ax=ax, facecolor="white")

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor="dimgray")

# Plot tourist places in Lagos
tourist_places = pois[pois.tourism.notnull()]
tourist_places.plot(ax=ax, color="blue", alpha=1, markersize=50)
plt.tight_layout()
mlai.write_figure(directory="\writeDiagramsDir/maps", filename="lagos-tourist-sites.svg"}

\figure{\includediagram{\diagramsDir/maps/lagos-tourist-sites}{40%}}{Tourist sites identified as Points of Interest in Open Street Map from Lagos.}{lagos-tourist-sites}

\endif
