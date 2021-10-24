\ifndef{openStreetMap}
\define{openStreetMap}

\editme


\subsection{Accessing Open Street Map}

\installcode{osmnx}

\setupcode{import osmnx as ox
import matplotlib.pyplot as plt}

\code{place_name = "Cambridge, England, United Kingdom"}

\code{# Retrieve POIs
tags = {'amenity': True, 'buildings': True, 'historic': True, 'leisure': True, 'shop': True, 'tourism': True}
pois = ox.geometries_from_place(place_name, tags)}


\code{# How many POIs do we have?
print('There are ' + str(len(pois)) + ' points of interest in ' + place_name)
pois.info}

\code{pois.columns.values}

\code{cols = ['name','addr:city','addr:postcode','amenity','building','building:name','building:colour','building:material','historic','memorial','religion','tourism','emergency','leisure','shop']
# Print only selected cols
pois[cols]}

\code{# Get map data.
# Fetch OSM street network from the location
graph = ox.graph_from_place(place_name)

# Retrieve nodes and edges
nodes, edges = ox.graph_to_gdfs(graph)

# Get place boundary related to the place name as a geodataframe
area = ox.geocode_to_gdf(place_name)}

\plotcode{# Create figure
fig, ax = plt.subplots(figsize=(12,8))

# Plot the footprint
area.plot(ax=ax, facecolor='white')

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor='dimgray')

# Plot buildings
#buildings.plot(ax=ax, facecolor='silver', alpha=0.7)

# Plot all POIs in Cambridge
pois.plot(ax=ax, color='blue', alpha=0.7, markersize=10)
plt.tight_layout()}

\plotcode{import numpy as np
# Plot a subset of the POIs (e.g., touristic places)
# Create figure
fig, ax = plt.subplots(figsize=(12,8))

# Plot the footprint
area.plot(ax=ax, facecolor='white')

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor='dimgray')

# Plot touristic places in Cambridge
touristic_places = pois[pois.tourism.notnull()]
print(str(len(touristic_places)))
touristic_places.plot(ax=ax, color='blue', alpha=1, markersize=50)
plt.tight_layout()}

\endif
