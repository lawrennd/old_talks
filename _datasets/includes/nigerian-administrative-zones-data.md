\ifndef{nigerianAdministrativeZones}
\define{nigerianAdministrativeZones}

\editme

\subsection{Nigerian Administrative Zones Data}

\notes{For ease of use we've packaged this data set in the `pods` library}

\include{_software/includes/pods-software.md}

\code{data = pods.datasets.nigerian_administrative_zones()['Y']
data.set_index("admin1Name_en", inplace=True)
data.head()}

\notes{Alternatively you can access the data directly with the following commands.

```{.python}
import zipfile

admin_zones_url = 'https://data.humdata.org/dataset/81ac1d38-f603-4a98-804d-325c658599a3/resource/0bc2f7bb-9ff6-40db-a569-1989b8ffd3bc/download/nga_admbnda_osgof_eha_itos.gdb.zip'
_, msg = urllib.request.urlretrieve(admin_zones_url, 'nga_admbnda_osgof_eha_itos.gdb.zip')
with zipfile.ZipFile('/content/nga_admbnda_osgof_eha_itos.gdb.zip', 'r') as zip_ref:
    zip_ref.extractall('/content/nga_admbnda_osgof_eha_itos.gdb')

import geopandas as gpd
import fiona

states_file = "./nga_admbnda_osgof_eha_itos.gdb/nga_admbnda_osgof_eha_itos.gdb/nga_admbnda_osgof_eha_itos.gdb/nga_admbnda_osgof_eha_itos.gdb/"

layers = fiona.listlayers(states_file)
data = gpd.read_file(states_file, layer=1)
data.crs = "EPSG:4326"
data = data.set_index('admin1Name_en')
	
```}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
data.plot(ax=ax, color='white', edgecolor='black')
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')

mlai.write_figure('nigerian-state-borders.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/nigerian-state-borders}{60%}}{Border locations for the thirty-six different states of Nigeria.}{nigerian-state-borders}

\endif
