\ifndef{spellmanEigengenes}
\define{spellmanEigengenes}

\editme

\subsection{Gene Expression}

Each of the cells in your body stores your entire genetic code in your DNA, but at any one moment it is only 'expressing' a small portion of that code. Your cells are mainly constructed of protein, and these proteins are manufactured by first transcribing the DNA to RNA and then translating the RNA to protein. If the DNA is the cells hard drive, then one role of the RNA is to act like a cache of data that is being read from the hard drive at any one time. Gene expression arrays allow us to measure the quantity of different types of RNA in the cell, effectively analyzing what's in the cache (although we have to destroy the cell or the tissue to access it). A gene expression experiment often consists of a time course or a series of experiments that characterise the gene expression of cells at any given time.

We will now load in one of the earliest gene expression data sets from a [1998 paper by Spellman et al.](http://www.ncbi.nlm.nih.gov/pubmed/9843569), it consists of gene expression measurements of over six thousand genes in a range of conditions for brewer's yeast. The experiment was designed for understanding the cell cycle of the genes. The expectation is that there should be oscillating signals inside the cell.

First we extract the principale components of the gene expression.

\code{# load in data and replace missing values with zero
data=pods.datasets.spellman_yeast_cdc15()
Y = data['Y'].fillna(0)
q = 5
U, ell, sigma2 = ppca(Y, q)
mu_x, C_x = posterior(Y, U, ell, sigma2)}

Now, looking through, we find that there is indeed a latent variable that appears to oscilate at approximately the right frequency. The 4th latent dimension (`index=3`) can be plotted across the time course as follows.

\setupcode{import matplotlib.pyplot as plt}
\code{plt.plot(mu_x[:, 3])}

To reveal an oscillating shape. We can see which genes correspond to this shape by examining the associated column of $\mathbf{U}$. Let's augment our data matrix with this score.

\code{gene_list = Y.T
gene_list['oscilation'] = np.sqrt(U[:, 3]**2)
gene_list.sort(columns='oscilation', ascending=False).index[:4]}

\notes{We can look up the first three genes in this list which now ranks the genes according to how strongly they respond to the fourth latent dimension. [The NCBI gene database](http://www.ncbi.nlm.nih.gov/gene/) allows us to search for the function of these genes. Looking at the function of the four genes that respond most strongly to the third latent variable they are all genes that encode [histone](http://en.wikipedia.org/wiki/Histone) proteins. The histone is thesupport scaffold for the DNA that ensures it folds correctly within the cell creating the nucleosomes. It seems to make sense that production of histone proteins should be strongly correlated with the cell cycle, as when the cell divides it needs to create a large number of histone proteins for creating the duplicated nucleosomes. The relevant links giving the descriptions of each gene given here: [YDR224C](http://www.ncbi.nlm.nih.gov/gene/851810), [YDR225W](http://www.ncbi.nlm.nih.gov/gene/851811), [YBL003C](http://www.ncbi.nlm.nih.gov/gene/852283) and [YNL030W](http://www.ncbi.nlm.nih.gov/gene/855701).}

\endif
