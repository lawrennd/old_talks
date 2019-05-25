\ifndef{clustering}
\define{clustering}

\editme

\subsection{Clustering}

* *Task*:  associate each data point with a different label.
* Label is *not* provided.
* Quite intuitive for humans, we do it naturally.

\newslide{Platonic Ideals}

* Names for animals originally invented by humans through 'clustering'
* Can we have the computer to recreate that process of inventing the label?
* Greek philosopher, Plato, thought about ideas, he considered the concept of the Platonic ideal.
* Platonic ideal bird is the bird that is most bird-like or the chair that is most chair-like.

\newslide{Cluster Center}

* Can define different clusters, by finding their Platonic ideal (known as the cluster center)
* Allocate each data point to the relevant nearest cluster center.
* Allocate each animal to the class defined by its nearest cluster center.

\newslide{Similarity and Distance Measures}

* Define a notion of either similarity or distance between the objects and their Platonic ideal.
* If objects are vectors of data, $\inputVector_i$.
* Represent cluster center for category $j$ by a vector $\meanVector_j$.
* This vector contains the ideal features of a bird, a chair, or whatever category $j$ is.

\newslide{Similarity or Distance}

* Can either think in terms of similarity of the objects, or distances.
* We want objects that are similar to each other to cluster together. We want objects that are distant from each other to cluster apart.
* Use mathematical function to formalize this notion, e.g. for distance
$$
\distanceScalar_{ij} = \mappingFunction(\inputVector_i, \meanVector_j).
$$

\newslide{Squared Distance}


* Find cluster centers that are close to as many data points as possible.
* A commonly used distance is the squared distance,
$$
\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2.
$$
* Already seen for regression.

\newslide{Objective Function}

* Given similarity measure, need number of  cluster centers, $\numComps$.
* Find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,
$$
\errorFunction(\meanMatrix) = \sum_{i \in \mathbf{i}_j} (\inputVector_i - \meanVector_j)^2
$$
here $\mathbf{i}_j$ is all indices of  data points allocated to the $j$th center. 

\newslide{$k$-Means Clustering}

* *$k$-means clustering* is simple and quick to implement.
* Very *initialisation* sensitive.

\newslide{Initialisation}

* Initialisation is the process of selecting a starting set of parameters.
* Optimisation result can depend on the starting point.
* For $k$-means clustering you need to choose an initial set of centers.
* Optimisation surface has many local optima, algorithm gets stuck in ones near initialisation.

\newslide{$k$-Means Clustering}

\slides{
\define{\width}{80%}
\startanimation{kmeans_clustering}{1}{26}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_001}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_002}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_003}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_004}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_005}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_006}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_007}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_008}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_009}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_010}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_011}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_012}{\width}}{kmeans_clustering}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_013}{\width}}{kmeans_clustering}
\endanimation

*Clustering with the $k$-means clustering algorithm.*
}

\notes{\figure{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_013}{\width}}{Clustering with the $k$-means clustering algorithm.}{kmeans-clustering-13}}

\newslide{$k$-Means Clustering}

\figure{\includeyoutube{mfqmoUN-Cuw}{800}{600}}{$k$-means clustering by Alex Ihler.}{k-means-clustering}
\slides{*$k$-means clustering by Alex Ihler*}

\newslide{Hierarchical Clustering}

* Form taxonomies of the cluster centers
* Like humans apply to animals, to form *phylogenies*

\figure{\includeyoutube{OcoE7JlbXvY){800}{600}}{Hierarchical Clustering by Alex Ihler.}{alex-ihler-hierarchical-clustering}

\newslide{Phylogenetic Trees}

* Perform a hierarchical clustering based on genetic data, i.e. the actual contents of the genome.
* Perform across a number of species and produce a *phylogenetic tree*.
* Represents a guess at actual evolution of the species.
* Used to estimate the origin of viruses like AIDS or Bird flu

\newslide{Product Clustering}

* Could apply hierarchical clustering to Amazon's products.
* Would give us a phylogeny of products.
* Each cluster of products would be split into sub-clusters of products until we got down to individual products.
    * E.g. at high level Electronics/Clothing

\newslide{Hierarchical Clustering Challenge}

* Many products belong in more than one cluster: e.g. running shoes are 'sporting goods' and they are 'clothing'.
* Tree structure doesn't allow this allocation.
* Our own psychological grouping capabilities are in cognitive science.
    * E.g. Josh Tenenbaum and collaborators cluster data in more complex ways.

\endif
