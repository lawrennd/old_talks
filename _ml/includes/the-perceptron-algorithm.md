### The Perceptron

-   Developed in 1957 by Rosenblatt.

-   Take a data point at, $\inputVector_i$.

-   Predict it belongs to a class, $\dataScalar_i=1$ if
    $\sum_j\weightScalar_{j} \inputVector_{i, j} + b  > 0$ i.e.
    $\weightVector^\top \inputVector_i + b > 0$. Otherwise assume
    $\dataScalar_i=-1$.

### Perceptron-like Algorithm

1.  Select a random data point $i$.

2.  Ensure $i$ is correctly classified by setting
    $\weightVector = \dataScalar_i \inputVector_i$.

    -   i.e.
        $\sign{\weightVector^\top\inputVector_{i, :}} = \sign{\dataScalar_i\inputVector_{i, :}^\top\inputVector_{i, :}} = \sign{\dataScalar_i} = \dataScalar_i$

### Perceptron Iteration

1.  Select a misclassified point, $i$.

2.  Set
    $\weightVector \leftarrow \weightVector + \learnRate\dataScalar_i\inputVector_{i, :}$.

    -   If $\learnRate$ is large enough this will guarantee this point
        becomes correctly classified.

3.  Repeat until there are no misclassified points.

\include{../../_ml/includes/the-perceptron.md}
