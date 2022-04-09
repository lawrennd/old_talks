\ifndef{singlecellLle}
\define{singlecellLle}

\include{_datasets/includes/singlecell-data.md}

\editme

\subsection{Blastocyst Data: Locally Linear Embedding}

\notes{Next we try locally linear embedding. In locally linear embedding a neighborhood is also computed. Each point is then reconstructed by it's neighbors using a linear weighting. This implies a locally linear patch is being fitted to the data in that region. These patches are assimilated into a large $\numData \times \numData$ matrix and a lower dimensional data set which reflects the same relationships is then sought. Quite a large number of neighbours needs to be selected for the data to not collapse in on itself. When a large number of neighbours is selected the embedding is more linear and begins to look like PCA. However, the algorithm does *not* converge to PCA in the limit as the number of neighbors approaches $\numData$.}

\setupcode{import sklearn.manifold}

\code{n_neighbors = 50
model = sklearn.manifold.LocallyLinearEmbedding(n_neighbors=n_neighbors, n_components=2)
X = model.fit_transform(Y)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
model.plot_latent(ax=ax, X[:, 0], X[:, 1], data['labels'], '<>^vsd')

mlai.write_figure('singlecell-lle.svg', directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/singlecell-lle}{60%}}{Visualisation of the @Guo:fate10 blastocyst development data with a locally linear embedding.}{singlecell-lle}

\endif

