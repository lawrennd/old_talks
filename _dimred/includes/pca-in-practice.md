\ifndef{pcaInPractice}
\define{pcaInPractice}

\editme

\notes{\section{PCA in Practice}

Principal component analysis is so effective in practice that there
has almost developed a mini-industry in renaming the method itself
(which is ironic, given its origin).  In particular
[Latent Semantic Indexing](http://en.wikipedia.org/wiki/Latent_semantic_indexing)
in text processing is simply PCA on a particular representation of the
term frequencies of the document. There is a particular fad to rename
the eigenvectors after the nature of the data you are examining,
perhaps initially triggered by
[Turk and Pentland's](http://www.face-rec.org/algorithms/PCA/jcn.pdf)
paper on eigenfaces, but also with
[eigenvoices](https://wiki.inf.ed.ac.uk/twiki/pub/CSTR/ListenSemester1_2007_8/kuhn-
junqua-eigenvoice-icslp1998.pdf) and
[eigengenes](http://www.biomedcentral.com/1752-0509/1/54). This seems
to be an instantiation of a wider, and hopefully subconcious, tendency
in academia to attempt to differentiate one idea from the same idea in
related fields in order to emphasise the novelty. The unfortunate
result is somewhat of a confusing literature for relatively simple
model. My recommendations would be as follows.  If you have
multivariate data, applying some form of principal component would
seem to be a very good idea as a first step. Even if you intend to
later perform classification or regression on your data, it can give
you understanding of the structure of the underlying data and help you
to develop your intuitions about the nature of your data. Intelligent
plotting and interaction with your data is always a good think, and
for high dimensional data that means that you need some way of
visualisation, PCA is typically a good starting point.}

\endif
