### Clustering

* *Task*:  associate each data point with a different label.

* Label is *not* provided.

* Quite intuitive for humans, we do it naturally.

### Platonic Ideals

* Names for animals originally invented by humans through 'clustering'

* Can we have the computer to recreate that process of inventing the label?

* Greek philosopher, Plato, thought about ideas, he considered the concept of the Platonic ideal.

* Platonic ideal bird is the bird that is most bird-like or the chair that is most chair-like.

### Cluster Center

* Can define different clusters, by finding their Platonic ideal (known as the cluster center)

* Allocate each data point to the relevant nearest cluster center.

* Allocate each animal to the class defined by its nearest cluster center.

### Similarity and Distance Measures

* Define a notion of either similarity or distance between the objects and their Platonic ideal.

* If objects are vectors of data, $\inputVector_i$.

* Represent cluster center for category $j$ by a vector $\meanVector_j$.

* This vector contains the ideal features of a bird, a chair, or whatever category $j$ is.

### Similarity or Distance

* Can either think in terms of similarity of the objects, or distances.

* We want objects that are similar to each other to cluster together. We want objects that are distant from each other to cluster apart.

* Use mathematical function to formalize this notion, e.g. for distance

$$
\distanceScalar_{ij} = \mappingFunction(\inputVector_i, \meanVector_j).
$$

### Squared Distance


* Find cluster centers that are close to as many data points as possible.

* A commonly used distance is the squared distance,

$$
\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2.
$$

* Already seen for regression.

### Objective Function

* Given similarity measure, need number of  cluster centers, $\numComps$.

* Find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,

$$
\errorFunction(\meanMatrix) = \sum_{i \in \mathbf{i}_j} (\inputVector_i - \meanVector_j)^2
$$

here $\mathbf{i}_j$ is all indices of  data points allocated to the $j$th center. 

### $k$-Means Clustering

* *$k$-means clustering* is simple and quick to implement.

* Very *initialisation* sensitive.

### Initialisation

* Initialisation is the process of selecting a starting set of parameters.

* Optimisation result can depend on the starting point.

* For $k$-means clustering you need to choose an initial set of centers.

* Optimisation surface has many local optima, algorithm gets stuck in ones near initialisation.

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_000.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_001.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_002.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_003.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_004.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_005.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_006.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_007.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_008.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_009.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_010.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_011.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

\includesvg{../slides/diagrams/kmeans-clustering/kmeans_clustering_012.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering {.slide: data-transition="none"}

<object class="svgplot"
data="../slides/diagrams/kmeans-clustering/kmeans_clustering_013.svg}

*Clustering with the $k$-means clustering algorithm.*

### $k$-Means Clustering

\includeyoutube{mfqmoUN-Cuw}

*$k$-means clustering by Alex Ihler*
### Hierarchical Clustering

* Form taxonomies of the cluster centers

* Like humans apply to animals, to form *phylogenies*

[![Hierarchical Clustering by Alex Ihler](https://img.youtube.com/vi/OcoE7JlbXvY/0.jpg)](https://www.youtube.com/watch?v=OcoE7JlbXvY)

### Phylogenetic Trees

* Perform a hierarchical clustering based on genetic data, i.e. the actual contents of the genome.

* Perform across a number of species and produce a *phylogenetic tree*.

* Represents a guess at actual evolution of the species.

* Used to estimate the origin of viruses like AIDS or Bird flu

### Product Clustering

* Could apply hierarchical clustering to Amazon's products.

* Would give us a phylogeny of products.

* Each cluster of products would be split into sub-clusters of products until we got down to individual products.

    * E.g. at high level Electronics/Clothing

### Hierarchical Clustering Challenge

* Many products belong in more than one cluster: e.g. running shoes are 'sporting goods' and they are 'clothing'.

* Tree structure doesn't allow this allocation.

* Our own psychological grouping capabilities are in cognitive science.

    * E.g. Josh Tenenbaum and collaborators cluster data in more complex ways.
