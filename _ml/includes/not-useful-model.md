\ifndef{notUsefulModel}
\define{notUsefulModel}

\editme

\subsubsection{Uncertainty in Parameters}

\notes{If the parameters are badly determined, then small fluctuations in the
data set lead to larger fluctuations in prediction. One approach to this
problem is to build models in which the parameters are well determined.
For the independence across data points case, this involves having many
observations (large $\numData$) relative to the number of parameters
(which often scales with $\dataDim$). This motivates the issues of the
large $\dataDim$ small $\numData$ domain, where the conditions are
reversed. Of course, from a modelling perspective this issue is
trivially solved by assuming independence across the $\dataDim$ data
dimensions and allowing the parameters to scale with the number of data
$\numData$. This is a characteristic exhibited, for example by the
Gaussian process latent variable model [@Lawrence:pnpca05] which in standard form assumes independence
across $\dataDim$ for high dimensional data and associates each data
point with a latent variable that is treated as a parameter. In
[@Lawrence:unifying12] I argued that the successful class of *spectral*
approaches to dimensionality reduction (e.g.
 LLE @Roweis:lle00 and maximum variance unfolding @Weinberger:learning04, which are widely
applied in the large $\dataDim$ small $\numData$ domain, also have a
probabilistic interpretation where the underlying likelihood factorizes
across data dimensions. Regardless of our choice of factorization
though, we are still making the same claim: a particular vector, or
matrix, of parameters is sufficient for us to consider that the data
independent, either across features or data points.}


\subsubsection{Massively Missing Data}

\notes{I'd like to argue that the separation of the data into features and
data points is rather arbitrary. I believe it stems from the origin of
the field of statistics, where the intention was to make a strong
scientific claim based on numbers take from a *table* of data. A table
naturally lends itself towards a matrix form. In these data a
statistical design normally involved measuring a fixed number of
*features* for a perhaps variable number of *items*. The objective is to
find sufficient number of items so that you can make strong claims about
which features are important. For example, does smoking correlate with
lung cancer? This explains the desire to write down the data as a matrix
$\dataMatrix$. I think this view of data, whilst important at the time,
is outdated when considering modern big data problems.}


\notes{The modern data analysis challenge is very different. We receive
streaming data of varying provenance. If each number we receive is given
by an observation $\dataScalar_i$, where $\dataScalar_i$ could be in the
natural numbers, the real numbers or binary or in any processable form,
then $\dataScalar_{17}$ might be the price of a return rail fair from
Sheffield to Oxford on 6th February 2014, whilst $\dataScalar_{29}$
might be the number of people on the 8:20 train that day, but
$\dataScalar_{72,394}$ could be the temperature of the Atlantic ocean on
23rd August 2056 at a point on the Arctic circle midway between Greenland
and Norway. When we see data in this form, we realize that most of the
time we are missing most of the data. This leads to the idea of *massive
missing data*. Contrast this situation with that traditionally faced in
missing data where a table of values, $\dataMatrix$, might have 10%-50%
of the measurements missing, perhaps due to problems in data collection.
I'd argue that if we are to model complex processes (such as the brain,
or the cell, or human health) then almost all the data is missing.}

\installcode{daft}

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[1, 1],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)

pgm.add_node(daft.Node("y", r"$\mathbf{y}$", 0.5, 0.5, fixed=False, observed=True))

pgm.render().figure.savefig("\diagramsDir/ml/y-only-graph.svg", transparent=True)}


\figure{\includediagram{\diagramsDir/ml/y-only-graph}{30%}}{The most general graphical model. It makes no assumptions about conditional probability relationships between variables in the vector $\dataVector$.}{y-only-graph}

\notes{A model that's not wrong, just not useful. I like graphical
representations of probabilistic models and this is my favourite graph.
It is the simplest graph but also the most general model. It says that all the
data in our vector $\dataVector$ is governed by an unspecified
probability disribution $p(\dataVector)$. 

Graphical models normally
express the conditional independence relationships in the data, with
this graph we are not a priori considering any such relationships. This
is the most general model (it includes all factorized models as special
cases). It is not wrong, but since it doesn't suggest what the next
steps are or give us any handles on the problem it is also not useful.}

\endif
