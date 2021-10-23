\ifndef{nigerianPopulationData}
\define{nigerianPopulationData}

\editme

\subsection{Population Data}

\notes{Now we have information about COVID cases, and we have information about how many health centers and how many doctors and nurses there are in each health center. But unless we understand how many people there are in each state, then we cannot make decisions about where they may be problems with the disease.}

\notes{If we were running our ride hailing service, we would also need information about how many people there were in different areas, so we could understand what the demand for the boda boda rides might be.

To access the number of people we can get population statistics from the [Humanitarian Data Exchange](https://data.humdata.org/).

We also want to have population data for each state in Nigeria, so that we can see attributes like whether there are zones of high health facility density but low population density.}


```python
import urllib

pop_url = "https://data.humdata.org/dataset/a7c3de5e-ff27-4746-99cd-05f2ad9b1066/resource/d9fc551a-b5e4-4bed-9d0d-b047b6961817/download/nga_admpop_adm1_2020.csv"
_, msg = urllib.request.urlretrieve(pop_url,"nga_admpop_adm1_2020.csv")
data = pd.read_csv("nga_admpop_adm1_2020.csv")
```

\notes{To do joins with this data, we must first make sure that the columns have the right names. The name should match the same name of the column in our existing data. So we reset the column names, and the name of the index, as follows.}

```python
data.dropna(axis=0, how="all", inplace=True)
data.dropna(axis=1, how="all", inplace=True)
data.rename(columns = {"ADM0_NAME" : "admin0Name_en", 
                       "ADM0_PCODE" : "admin0Pcode", 
                       "ADM1_NAME" : "admin1Name_en", 
                       "ADM1_PCODE" : "admin1Pcode", 
                       "T_TL" : "population"},
            inplace=True)
data["admin0Name_en"] = data["admin0Name_en"].str.title()
data["admin1Name_en"] = data["admin1Name_en"].str.title()
    
data = data.set_index("admin1Name_en")
```

\note{Or you can download directly with pods.}

\code{data = pods.datasets.nigerian_population()["Y"]}

\code{data.head()}


\endif
