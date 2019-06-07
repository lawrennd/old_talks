### Covariance Functions

#### Where did this covariance matrix come from?

**Markov Process**

**Visualization of inverse covariance (precision).**


-   Precision matrix is sparse: only neighbours in matrix are non-zero.

-   This reflects *conditional* independencies in data.

-   In this case *Markov* structure.

### Covariance Functions

#### Where did this covariance matrix come from? {data-transition="none"}

**Exponentiated Quadratic**

**Visualization of inverse covariance (precision).**

\columns{
- Precision matrix is not sparse.
- Each point is dependent on all the others.
- In this case non-Markovian.
}{
rbfprecisionSample
}{50%}{50%}

### Covariance Functions {data-transition="none"}

**Markov Process**

**Visualization of inverse covariance (precision).**

\columns{
- Precision matrix is sparse: only neighbours in matrix are non-zero.
- This reflects *conditional* independencies in data.
- In this case *Markov* structure.
}{
markovprecisionPlot
}{50%}{50%}
