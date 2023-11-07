\ifndef{singlecellIsomap}
\define{singlecellIsomap}

\include{_datasets/includes/singlecell-data.md}

\editme

\subsection{Blastocyst Data: Isomap}

\notes{Isomap first builds a neighbourhood graph, and then uses distances along this graph to approximate the geodesic distance between points. These distances are then visualized by performing classical multidimensional scaling (which involves computing the eigendecomposition of the centred distance matrix). As the neighborhood size is increased to match the data, principal component analysis is recovered (or strictly speaking, principal coordinate analysis). The fewer the neighbors, the more 'non-linear' the isomap embeddings are.}


\setupcode{import sklearn.manifold}

\code{n_neighbors = 10
model = sklearn.manifold.Isomap(n_neighbors=n_neighbors, n_components=2)
X = model.fit_transform(Y)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
plot_labels(ax, X[:, 0], X[:, 1], data['labels'], '<>^vsd')


mlai.write_figure('singlecell-isomap.svg', directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/singlecell-isomap}{60%}}{Visualisation of the @Guo:fate10 blastocyst development data with Isomap.}{singlecell-isomap}


\endif
