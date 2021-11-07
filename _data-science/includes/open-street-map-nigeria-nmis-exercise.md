\ifndef{openStreetMapNigeriaNmisExercise}
\define{openStreetMapNigeriaNmisExercise}

\editme

\subsection{Matching OpenStreetMap and NMIS Data}

\notes{In this exercise you will download the location of health centres from OpenStreetMap in Lagos and map them to the health centres you've already viewed in the NMIS data. This is a data validation exercise.}

\codeassignment{The latitude and longitude of Lagos in Nigeria are as follows:

```
place_name = "Lagos, Nigeria"

latitude = 6.5244
longitude = 3.3792
```

In OpenStreetMap the key for a health center is `key:healthcare`. Download the POIs on OpenStreetMap that are listed as health centres and match them to POIs in the OpenStreetMap data to the health centres we find in the Nigerian NMIS data (`pods.datasets.nigeria_nmis`).

You may use the distance between the centroid for the match, but you should also consider any additional checks you might wish to perform. 

Ensure your code is reusable, making it easy to integrate any necessary human feedback as required. Demonstrate the reuse by performing the same analysis for Abuja.

```
place_name = "Abuja, Nigeria"

latitude = 9.05785 
longitude = 7.49508
```
}{}{30}



\endif
