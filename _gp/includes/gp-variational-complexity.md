\subsection{Variational Compression}

\slides{
* Inducing variables are a compression of the real observations.
* They are like pseudo-data. They can be in space of $\mappingFunctionVector$ or a space that is related through a linear operator [@Alvarez:efficient10] — e.g. a gradient or convolution.
}
\notes{Inducing variables are a compression of the real observations. The basic idea is can I create a new data set that summarizes all the information in the original data set. If this data set is smaller, I've compressed the information in the original data set. 

Inducing variables can be thought of as pseudo-data, indeed in @Snelson:pseudo05 they were referred to as *pseudo-points*. 

The only requirement for inducing variables is that they are jointly distributed as a Gaussian process with the original data. This means that they can be from the space $\mappingFunctionVector$ or a space that is related through a linear operator (see e.g. @Alvarez:efficient10). For example we could choose to store the gradient of the function at particular points or a value from the frequency spectrum of the function [@Lazaro:spectrum10].}

\subsection{Variational Compression II}

\slides{
* Introduce *inducing* variables.
* Compress information into the inducing variables and avoid the need to store all the data.
* Allow for scaling e.g. stochastic variational @Hensman:bigdata13 or parallelization @Gal:Distributed14,@Dai:gpu14, @Seeger:auto17
}
\notes{Inducing variables don't only allow for the compression of the non-parameteric information into a reduced data aset but they also allow for computational scaling of the algorithms through, for example stochastic variational approaches @Hensman:bigdata13 or parallelization @Gal:Distributed14,@Dai:gpu14, @Seeger:auto17.}
