---
title: Description of Datasets Available in `pods`
date: 2020-11-19
---

\notes{The pods toolbox provides easy access to various data sets. The data sets are accessed through calls to the `pods.datasets` module. This module contains functions which download and preprocess the data for you, presenting it in a dictionary with a standard format for use in `pods`. On download you will also be informed of any licensing restrictions and relevant citations for the data. The data is then cached on your local drive.}

\notes{Here are some descriptions of the data sets in different notebooks.}

\subsection{Count Data}

* [`pods.datasets.google_trends()`](./google-trends.ipynb) download data from Google trends. Based on an original [notebook](https://github.com/sahuguet/notebooks/blob/master/GoogleTrends%20meet%20Notebook.ipynb) by [sahuguet](https://github.com/sahuguet).

\subsection{Regression Data}

* [`pods.datasets.airline_delay()`](./airline-delay.ipynb) airline delay data set used for in @Hensman:bigdata13.
* [`pods.datasets.mauna_loa()`](./mauna-loa.ipynb) download the latest version of the Mauna Loa data set. This is data giving carbon dioxide concentrations from the Mauna Loa observatory in Hawaii.

\subsection{Other Data}

* [`pods.datasets.spellman_yeast()`](./spellman-yeast.ipynb) download the yeast cell cycle gene expression data set from @Spellman:yeastcellcy98.
* [`pods.datasets.lee_yeast()`](./lee-yeast.ipynb) download the yeast connectivity data from @Lee:trascriptional02.
* [`pods.datasets.ceres()`](./ceres.ipynb) celestial observations of the dwarf planet Ceres by Giuseppe Piazzi.
* [`pods.datasets.della_gatta_gene()`](./della-gatta-gene.ipynb) gene expression data from papyer by @DellaGatta:direct08.

\subsection{Adding a Data Set}

* [Adding a Data Set](./adding-data-set.ipynb) Overview of how to add a new data set to pods.


\references
