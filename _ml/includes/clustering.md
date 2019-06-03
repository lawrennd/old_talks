\ifndef{clustering}
\define{clustering}

\editme

\subsection{Clustering}
\slides{
* *Task*:  associate each data point with a different label.
* Label is *not* provided.
* Quite intuitive for humans, we do it naturally.}
\notes{Clustering methods associate each data point with a different label. Unlike in classification the label is not provided by a human annotator. It is allocated by the computer. Clustering is quite intuitive for humans, we do it naturally with our observations of the real world. For example, we cluster animals into different groups. If we encounter a new animal, we can immediately assign it to a group: bird, mammal, insect. These are certainly labels that can be provided by humans, but they were also originally invented by humans. With clustering we want the computer to recreate that process of inventing the label.}

\newslide{Platonic Ideals}
\slides{
* Names for animals originally invented by humans through 'clustering'
* Can we have the computer to recreate that process of inventing the label?
* Greek philosopher, Plato, thought about ideas, he considered the concept of the Platonic ideal.
* Platonic ideal bird is the bird that is most bird-like or the chair that is most chair-like.}
\notes{Unsupervised learning enables computers to form similar categorizations on data that is too large scale for us to process. When the Greek philosopher, Plato, was thinking about ideas, he considered the concept of the Platonic ideal. The Platonic ideal bird is the bird that is most bird-like or the chair that is most chair-like. In some sense, the task in clustering is to define different clusters, by finding their Platonic ideal (known as the cluster center) and allocate each data point to the relevant cluster center. So, allocate each animal to the class defined by its nearest cluster center.}

\newslide{Cluster Center}
\slides{
* Can define different clusters, by finding their Platonic ideal (known as the cluster center)
* Allocate each data point to the relevant nearest cluster center.
* Allocate each animal to the class defined by its nearest cluster center.}
\notes{To perform clustering on a computer we need to define a notion of either similarity or distance between the objects and their Platonic ideal, the cluster center. We normally assume that our objects are represented by vectors of data, $\inputVector_i$. Similarly, we represent our cluster center for category $j$ by a vector $\meanVector_j$. This vector contains the ideal features of a bird, a chair, or whatever category $j$ is. In clustering we can either think in terms of similarity of the objects, or distances. We want objects that are similar to each other to cluster together. We want objects that are distant from each other to cluster apart.}

\newslide{Similarity and Distance Measures}
\slides{
* Define a notion of either similarity or distance between the objects and their Platonic ideal.
* If objects are vectors of data, $\inputVector_i$.
* Represent cluster center for category $j$ by a vector $\meanVector_j$.
* This vector contains the ideal features of a bird, a chair, or whatever category $j$ is.}
\notes{This requires us to formalize our notion of similarity or distance. Let's focus on distances. A definition of distance between an object, $i$, and the cluster center of class $j$ is a function of two vectors, the data point, $\inputVector_i$ and the cluster center, $\meanVector_j$,
$$
d_{ij} = f(\inputVector_i, \meanVector_j).
$$
Our objective is then to find cluster centers that are close to as many data points as possible.  For example, we might want to cluster customers into their different tastes. We could represent each customer by the products they've purchased in the past. This could be a binary vector $\inputVector_i$. We can then define a distance between the cluster center and the customer.}


\newslide{Similarity or Distance}
\slides{
* Can either think in terms of similarity of the objects, or distances.
* We want objects that are similar to each other to cluster together. We want objects that are distant from each other to cluster apart.
* Use mathematical function to formalize this notion, e.g. for distance
$$
\distanceScalar_{ij} = \mappingFunction(\inputVector_i, \meanVector_j).
$$}

\subsubsection{Squared Distance}
\slides{
* Find cluster centers that are close to as many data points as possible.
* A commonly used distance is the squared distance,
$$
\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2.
$$
* Already seen for regression.}
\notes{A commonly used distance is the squared distance,
$$
\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2.
$$
The squared distance comes up a lot in machine learning. In unsupervised learning it was used to measure dissimilarity between predictions and observed data. Here its being used to measure the dissimilarity between a cluster center and the data.}


\newslide{Objective Function}
\slides{
* Given similarity measure, need number of  cluster centers, $\numComps$.
* Find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,}\notes{Once we have decided on the distance or similarity function, we can decide a number of cluster centers, $K$. We find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,}
$$
\errorFunction(\meanMatrix) = \sum_{i \in \mathbf{i}_j} (\inputVector_i - \meanVector_j)^2
$$
\slides{here $\mathbf{i}_j$ is all indices of  data points allocated to the $j$th center.}\notes{where the notation $\mathbf{i}_j$ represents all the indices of each data point which has been allocated to the $j$th cluster represented by the center $\meanVector_j$.}

\subsubsection{$k$-Means Clustering}
\slides{
* *$k$-means clustering* is simple and quick to implement.
* Very *initialisation* sensitive.
}

\newslide{Initialisation}
\slides{
* Initialisation is the process of selecting a starting set of parameters.
* Optimisation result can depend on the starting point.
* For $k$-means clustering you need to choose an initial set of centers.
* Optimisation surface has many local optima, algorithm gets stuck in ones near initialisation.}
\notes{One approach to minimizing this objective function is known as *$k$-means clustering*. It is simple and relatively quick to implement, but it is an initialization sensitive algorithm. Initialization is the process of choosing an initial set of parameters before optimization. For $k$-means clustering you need to choose an initial set of centers. In $k$-means clustering your final set of clusters is very sensitive to the initial choice of centers. For more technical details on $k$-means clustering you can watch a video of Alex Ihler introducing the algorithm here.}

\subsubsection{$k$-Means Clustering}

\slides{
\define{\width}{40%}
\define{animationName}{kmeans-clustering}
\startanimation{\animationName}{1}{26}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_001}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_002}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_003}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_004}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_005}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_006}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_007}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_008}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_009}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_010}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_011}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_012}{\width}}{\animationName}
\newframe{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_013}{\width}}{\animationName}
\endanimation

*Clustering with the $k$-means clustering algorithm.*
}

\notes{\figure{\includediagram{../slides/diagrams/ml/kmeans-clustering/kmeans_clustering_013}{\width}}{Clustering with the $k$-means clustering algorithm.}{kmeans-clustering-13}}

\newslide{$k$-Means Clustering}

\figure{\includeyoutube{mfqmoUN-Cuw}{800}{600}}{$k$-means clustering by Alex Ihler.}{k-means-clustering}

\slides{*$k$-means clustering by Alex Ihler*}

\subsubsection{Hierarchical Clustering}
\slides{
* Form taxonomies of the cluster centers
* Like humans apply to animals, to form *phylogenies*
}
\notes{Other approaches to clustering involve forming taxonomies of the cluster centers, like humans apply to animals, to form trees. You can learn more about agglomerative clustering in this video from Alex Ihler.}

\figure{\includeyoutube{OcoE7JlbXvY}{800}{600}}{Hierarchical Clustering by Alex Ihler.}{alex-ihler-hierarchical-clustering}

\subsubsection{Phylogenetic Trees}
\slides{
* Perform a hierarchical clustering based on genetic data, i.e. the actual contents of the genome.
* Perform across a number of species and produce a *phylogenetic tree*.
* Represents a guess at actual evolution of the species.
* Used to estimate the origin of viruses like AIDS or Bird flu
}
\notes{Indeed, one application of machine learning techniques is performing a hierarchical clustering based on genetic data, i.e. the actual contents of the genome. If we do this across a number of species then we can produce a *phylogeny*. The phylogeny aims to represent the actual evolution of the species and some phylogenies even estimate the timing of the common ancestor between two species[^commonancestor]. Similar methods are used to estimate the origin of viruses like AIDS or Bird flu which mutate very quickly. Determining the origin of viruses can be important in containing or treating outbreaks.

[^commonancestor]: These models are quite a lot more complex than the simple clustering we describe here. They represent a common ancestor through a cluster center that is then allowed to evolve over time through a mutation rate. The time of separation between different species is estimated via these mutation rates. 
}

\subsubsection{Product Clustering}
\slides{
* Could apply hierarchical clustering to an e-commerce company's products.
* Would give us a phylogeny of products.
* Each cluster of products would be split into sub-clusters of products until we got down to individual products.
    * E.g. at high level Electronics/Clothing
}
\notes{An e-commerce company could apply hierarchical clustering to all its products. That would  give a phylogeny of products. Each cluster of products would be split into sub-clusters of products until we got down to individual products. For example, we might expect a high level split to be Electronics/Clothing. Of course, a challenge with these tree-like structures is that many products belong in more than one parent cluster: for example running shoes should be in more than one group, they are 'sporting goods' and they are 'apparel'. A tree structure doesn't allow this allocation.}

\subsubsection{Hierarchical Clustering Challenge}
\slides{
* Many products belong in more than one cluster: e.g. running shoes are 'sporting goods' and they are 'clothing'.
* Tree structure doesn't allow this allocation.
* Our own psychological grouping capabilities are in cognitive science.
    * E.g. Josh Tenenbaum and collaborators cluster data in more complex ways.}
\notes{Our own psychological grouping capabilities are studied as a domain of cognitive science. Researchers like Josh Tenenbaum have developed algorithms that decompose data in more complex ways, but they can normally only be applied to smaller data sets.}

\endif
