::: {.cell .markdown}
# Datasets: Downloading Data from Google Trends

### 28th May 2014 {#28th-may-2014}

### Neil Lawrence

This data set collection was inspired by a [ipython
notebook](https://github.com/sahuguet/notebooks/blob/master/GoogleTrends%20meet%20Notebook.ipynb)
from [sahuguet](https://github.com/sahuguet) which made queries to
google trends and downloaded the results. We\'ve modified the download
to cache the results of a query: making multiple calls to the google API
results in a block due to terms of service violations, cacheing the data
locally prevents this happening.
:::

::: {.cell .code execution_count="27"}
``` {.python}
import pods
import matplotlib.pyplot as plt
%matplotlib inline
```
:::

::: {.cell .code execution_count="28"}
``` {.python}
# calling without arguments uses the default query terms
data = pods.datasets.google_trends(['big data', 'internet of things']) 
```

::: {.output .stream .stdout}
    Accessing Google trends to acquire the data. Note that repeated accesses will result in a block due to a google terms of service violation. Failure at this point may be due to such blocks.
    Query terms:  big data, internet of things
    Fetching query:
    Done.
:::
:::

::: {.cell .markdown}
The default query terms are \'big data\', \'data science\' and \'machine
learning\'. The dictionary returned from the call contains the standard
\'X\' and \'y\' keys that are ready to be used in the GPy toolkit as
inputs to the Gaussian process. In this case the \'X\' variables are the
time (first column) and an index representing the query.
:::

::: {.cell .code execution_count="29"}
``` {.python}
print(data['X'][284, :])
```

::: {.output .stream .stdout}
    [1.47e+04 1.00e+00]
:::
:::

::: {.cell .markdown}
So the 284th element of X contains is the 34th time point of the query
term 2, which in this case is the 34th time point of the \'machine
learning\' time series. The value of the time series at that point is
given by the corresponding row of `Y`
:::

::: {.cell .code execution_count="30"}
``` {.python}
print(data['Y'][284, :])
```

::: {.output .stream .stdout}
    [5]
:::
:::

::: {.cell .markdown}
The dictionary also contains a pandas data frame of the trend data,
which is in line with what [sahuguet](https://github.com/sahuguet)
originally returned.
:::

::: {.cell .code execution_count="31"}
``` {.python}
data['data frame'].describe()
```

::: {.output .execute_result execution_count="31"}
```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>big data</th>
      <th>internet of things</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>209.000000</td>
      <td>209.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>41.708134</td>
      <td>9.822967</td>
    </tr>
    <tr>
      <th>std</th>
      <td>36.801651</td>
      <td>9.042222</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>31.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>79.000000</td>
      <td>18.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>100.000000</td>
      <td>31.000000</td>
    </tr>
  </tbody>
</table>
</div>
```
:::
:::

::: {.cell .markdown}
And we can plot the trends data to see what the effect is.
:::

::: {.cell .code execution_count="32"}
``` {.python}
data['data frame'].set_index('Date', inplace=True)
```
:::

::: {.cell .code execution_count="33"}
``` {.python}
fig, ax = plt.subplots(figsize=(10,5))
data['data frame'].plot(ax=ax, rot=45)
#fig.savefig('/Users/neil/lawrennd/talks/slides/diagrams/bd-iot-google-trends.svg')
```

::: {.output .execute_result execution_count="33"}
    <AxesSubplot:xlabel='Date'>
:::

::: {.output .display_data}
![](1731f88b5e0daebf04424a98218cd82eb294f21e.png)
:::
:::

::: {.cell .markdown}
### Dogs, Cats and Rabbits

Another data set we might consider downloading from google trends is
different pets. Below we consider cats, dogs and rabbits.
:::

::: {.cell .code execution_count="8"}
``` {.python}
data = pods.datasets.google_trends(['cat', 'dog', 'rabbit'], refresh_data=True)
data['data frame'].set_index('Date', inplace=True)
fig, ax = plt.subplots(figsize=(10,5))
data['data frame'].plot(ax=ax, rot=45)
```

::: {.output .stream .stdout}
    Accessing Google trends to acquire the data. Note that repeated accesses will result in a block due to a google terms of service violation. Failure at this point may be due to such blocks.
    Query terms:  cat, dog, rabbit
    Fetching query:
    Done.
:::

::: {.output .stream .stderr}
    <ipython-input-8-eda81229cc92>:5: UserWarning: FixedFormatter should only be used together with FixedLocator
      _ = ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)
:::

::: {.output .display_data}
![](73c0b51c87d3b10f25478db8b0f345b1edd09760.png)
:::
:::

::: {.cell .markdown}
Here we\'ve plotted the data in the same manner as
[sahuguet](https://github.com/sahuguet) suggested in his original
notebook, using the plotting facility of `pandas`.
:::

::: {.cell .markdown}
### Games Consoles

Finally we can try and compare different games console popularity.
:::

::: {.cell .code execution_count="23"}
``` {.python}
data = pods.datasets.google_trends(['xbox one', 'wii u', 'ps4'])
```

::: {.output .stream .stdout}
    Reading cached data for google trends. To refresh the cache set 'refresh_data=True' when calling this function.
    Query terms:  ps4, wii u, xbox one
:::
:::

::: {.cell .code execution_count="24"}
``` {.python}
data['data frame'].set_index('Date', inplace=True)
fig, ax = plt.subplots(figsize=(10,5))
data['data frame'].plot(ax=ax, rot=45)
```

::: {.output .execute_result execution_count="24"}
    <AxesSubplot:xlabel='Date'>
:::

::: {.output .display_data}
![](4a00954b31d0d693ed95f609bb553f8087f68161.png)
:::
:::

::: {.cell .code}
``` {.python}
```
:::

::: {.cell .code}
``` {.python}
```
:::
