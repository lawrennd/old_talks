\ifndef{nigeriaNmisInstalls}
\define{nigeriaNmisInstalls}

\editme

\notes{
\subsection{Imports, Installs, and Downloads}

First, we're going to download some particular python libraries for dealing with geospatial data. We're dowloading [```geopandas```](https://geopandas.org) which will help us deal with 'shape files' that give the geographical lay out of Nigeria. We also need ```pygeos``` for indexing.}

\comment{And  to get a small database set up running quickly, we're installing [```csv-to-sqlite```](https://pypi.org/project/csv-to-sqlite/) which allows us to convert CSV data to a simple database.}

\installcode{geopandas}
\installcode{pygeos}

\include{_mlai/includes/mlai-notebook-setup.md}


\endif
