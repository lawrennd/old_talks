---
title: Adding a Data Set to `pods`
date: 2014-05-28
---


talk-macros.gpp}/talk-macros.gpp}

\notes{Adding a data set to GPy should be done in two stages. Firstly, you need to edit the `data_resources.json` file to provide information about where to download the data from and what the license and citation information for the data is. Then you can edit the `datasets.py` file, located in `GPy.util` to load in the data and perform any preprocessing, before returning the data set to the user in the standard dictionary format.}

\subsection{Step 1: Editing `data_resources.json`}

\notes{A `json` file is a simple way of storing a python dictionary in a format that is interchangeable with other languages. This file is loaded in at the beginning of `datasets.py` to provide information on where he data set is located, what its licensing terms are and any other standard details about the data. You can use any `json` editor to edit the file. You can also use a standard text editor, but be careful not to damage the format of the file! If you do damage the format, there are various on line json format checkers you can use to try and recover the file.}

\notes{The file consists of a comma separated list of dictionary entries. Each dictionary entry corresponds to a single data set. Below is the dictionary entry for the Boston Housing data.}

```
"boston_housing": {
	"citation": "Harrison, D. and Rubinfeld, D.L. 'Hedonic prices and the demand for clean air', J. Environ. Economics & Management, vol.5, 81-102, 1978.",
	"details": "The Boston Housing data relates house values in Boston to a range of input variables.",
	"files": [
		[
			"Index",
			"housing.data",
			"housing.names"
		]
	],
	"license": null,
	"size": 51276,
	"urls": [
		"http://archive.ics.uci.edu/ml/machine-learning-databases/housing/"
	]
},
```

\notes{The entry includes firstly, the data set name. Then it includes six fields for describing. 
* `url` The download url location of the data. This is provided as a *list* of urls. Just in case several different locations need to be visited. Here the list contains only one element.
* `files` This is a *list of lists*. Each list contains the files to be downloaded from the corresponding url. Here there are three files required from the first (and only) url.
* `details` Some helpful information for the user about the data.
* `citation` The citation to use when publishing on the data. If you use a data set you should always cite its origin.
* `size` A total size information for the user to know how much disk space the data will take when its all downloaded.
* `license` The license terms for the data. Many data sets have a license associated. Don't include data sets in this collection that don't permit their inclusion. There don't appear to be any license constraints for the use of the Boston housing data, so in this case this vealue is set to `null`.}

\subsection{Step 2: Including the Data in `datasets.py`}

\notes{The `data_resources.json` file includes all the information about how to download the data. Now in `datasets.py` we write a short dataset recovery function to execute the download and return the data to the user. It has the following form:}


\code{def boston_housing(data_set='boston_housing'):
    if not data_available(data_set):
        download_data(data_set)
    all_data = np.genfromtxt(os.path.join(data_path, data_set, 'housing.data'))
    X = all_data[:, 0:13]
    Y = all_data[:, 13:14]
    return data_details_return({'X' : X, 'Y': Y}, data_set)}

\notes{The function name allows users to call `data = pods.datasets.boston_housing()` to acquire the data. You should use a name that makes it clear to readers of the code what is going on. The data set name is passed to the function as a default argument. This name corresponds to the entry in the `json` file.}

\notes{The next two lines call the function `data_available()` to check if the data set is already in the cache. If the data set is not there, then `download_data()`, which handles the interface with the user for downloading the data is called.}

\notes{The location of the cached data can be determined through the configuration file. By default it is set to be in a temporary directory under your home directory: `tmp/GPy-datasets`. But you can change this by creating your own configuration file in your home directiory, `.gpy_user.cfg` or by editing the configuration file for your GPy installation, `installation.cfg`. See [this notebook](../pods/config.ipynb) for details on the config file.}

\notes{The final line, `data_details_return` returns the dictionary of information loaded in from `data_resource.json` alongside the dictionary we've just constructed. The dictionary we return to the user is in a standard format with entries `X` and `Y` for the covariates and response variables.}

\notes{Now things should be ready for you to download the data!}


\code{import pods
data = pods.datasets.boston_housing()}


\subsection{Optional Step 3: Preprocessing}

\notes{In the above we haven't performed any preprocessing of the data. What if we want to preprocess the data before giving it to the user? We can write a different, additional, version of the data set recovery function for providing a different preprocessing. Here we preprocess the `Y` values to be zero mean and unit standard deviation.}


\code{from pods.datasets import *
import numpy as np
def boston_housing_preprocess(data_set='boston_housing'):
    if not data_available(data_set):
        download_data(data_set)
    all_data = np.genfromtxt(os.path.join(data_path, data_set, 'housing.data'))
    X = all_data[:, 0:13]
    Y = all_data[:, 13:14]
    Y = (Y - np.mean(Y))/np.std(Y)
    return data_details_return({'X' : X, 'Y': Y, 
                                'info' : 'The response variables have been preprocessed to have zero mean and unit standard deviation'
                                }, data_set)}

\notes{Now we can access the same data set, but this time, because we have the data in cache no download is performed.}


\code{data = boston_housing_preprocess()}

\notes{For this version of the data set we can check that the response variables have been normalized.}


\code{print('Mean: ', data['Y'].mean())
print('Standard deviation ', data['Y'].std())}

\references
