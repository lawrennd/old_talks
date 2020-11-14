\ifndef{precisionMatrices}
\define{precisionMatrices}

\include{_kern/includes/brownian-covariance.md}

\editme

\subsection{Where did this covariance matrix come from?}

**Markov Process**

**Visualization of inverse covariance (precision).**


-   Precision matrix is sparse: only neighbours in matrix are non-zero.

-   This reflects *conditional* independencies in data.

-   In this case *Markov* structure.


\subsection{Where did this covariance matrix come from?}

**Exponentiated Quadratic**

**Visualization of inverse covariance (precision).**

\columns{
- Precision matrix is not sparse.
- Each point is dependent on all the others.
- In this case non-Markovian.
}{
rbfprecisionSample
}{50%}{50%}

\subsection{Covariance Functions}

**Markov Process**

**Visualization of inverse covariance (precision).**

\columns{
- Precision matrix is sparse: only neighbours in matrix are non-zero.
- This reflects *conditional* independencies in data.
- In this case *Markov* structure.
}{
markovprecisionPlot
}{50%}{50%}


\endif
