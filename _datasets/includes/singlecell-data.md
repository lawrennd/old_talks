\ifndef{singlecellData}
\define{singlecellData}


\subsection{Data for Blastocyst Development in Mice: Single Cell TaqMan Arrays}

\notes{Now we analyze some single cell data from @Guo:fate10. Tey performed qPCR TaqMan array on single cells from the developing blastocyst in mouse. The data is taken from the early stages of development when the Blastocyst is forming. At the 32 cell stage the data is already separated into the trophectoderm (TE) which goes onto form the placenta and the inner cellular mass (ICM). The ICM further differentiates into the epiblast (EPI)---which gives rise to the endoderm, mesoderm and ectoderm---and the primitive endoderm (PE) which develops into the amniotic sack. @Guo:fate10 selected 48 genes for expression measurement. They labelled the resulting cells and their labels are included as an aide to visualization.}

\notes{They first visualized their data using principal component analysis. In the first two principal components this fails to separate the domains. This is perhaps because the principal components are dominated by the variation in the 64 cell systems. This in turn may be because there are more cells from the data set in that regime, and may be because the natural variation is greater. We first recreate their visualization using principal component analysis.}


\notes{In this notebook we will perform PCA on the original data, showing that the different regimes do not separate. }


\notes{Next we load in the data. We've provided a convenience function for loading in the data with `pods`. It is loaded in as a `pandas` DataFrame. This allows us to summarize it with the `describe` attribute.}

\setupcode{import pods}

\code{data = pods.datasets.singlecell()
Y = data['Y']
Y.describe}


\subsection{Principal Component Analysis}

\notes{Now we follow @Guo:fate10 in performing PCA on the data. Rather than calling a 'PCA routine', here we break the algorithm down into its steps: compute the data covariance, compute the eigenvalues and eigenvectors and sort according to magnitude of eigenvalue. Because we want to visualize the data, we've chose to compute the eigenvectors of the *inner product matrix* rather than the covariance matrix. This allows us to plot the eigenvalues directly. However, this is less efficient (in this case because the number of genes is smaller than the number of data) than computing the eigendecomposition of the covariance matrix.}


\setupcode{import numpy as np}

\code{# obtain a centred version of data.
centredY = Y - Y.mean()
# compute inner product matrix
C = np.dot(centredY,centredY.T)
# perform eigendecomposition
V, U = np.linalg.eig(C)
# sort eigenvalues and vectors according to size
ind = V.argsort()
ev = V[ind[::-1]]
U = U[:, ind[::-1]]}

\notes{To visualize the result, we now construct a simple helper
function. This will ensure that the plots have the same legends as the
GP-LVM plots we use below.}


\setuphelpercode{import GPy
import matplotlib.pyplot as plt}

\helpercode{def plot_labels(ax, x, y, labels, symbols):
    """A small helper function for plotting with labels"""
    # make sure labels are in order of input:
    ulabels = []
    for lab in labels:
        if not lab in ulabels:
            ulabels.append(lab)
    for i, label in enumerate(ulabels):
        symbol = symbols[i % len(symbols)]
        ind = labels == label
        ax.plot(x[ind], y[ind], symbol)
    ax.legend(ulabels)}

\subsection{PCA Result}

\notes{Now, using the helper function we can plot the results with appropriate labels.}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
plot_labels(ax, U[:, 0], U[:, 1], data['labels'], '<>^vsd')

mlai.write_figure('singlecell-data-pca.svg', directory='\writeDiagramsDir/datasets')}

\figure{\includediagram{\diagramsDir/datasets/singlecell-data-pca}{60%}}{First two principal compoents of the @Guo:fate10 blastocyst development data.}{singlecell-data-pca}

\endif

