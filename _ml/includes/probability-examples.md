\newslide{Computing Expectations Example}

\slides{
* Consider the following distribution.

$y$        |  1  |  2  |  3  |  4
-----------|-----|-----|-----|-----
$P\left(y\right)$ |  0.3|  0.2|  0.1|  0.4

* What is the mean of the distribution?
* What is the standard deviation of the distribution?
* Are the mean and standard deviation representative of the distribution form?
* What is the expected value of $-\log P(y)$?}

\newslide{Expectations Example: Answer}

\slides{
* We are given that:

$y$               |   1   |   2   |   3   |   4
------------------|-------|-------|-------|-------
$P\left(y\right)$ |  0.3  |  0.2  |  0.1  |  0.4
$y^2$             |   1   |   4   |   9   |  16
$-\log(P(y))$     | 1.204 | 1.609 | 2.302 | 0.916

* Mean: $1\times 0.3 + 2\times 0.2 + 3 \times 0.1 + 4 \times 0.4 = 2.6$
* Second moment: $1 \times 0.3 + 4 \times 0.2 + 9 \times 0.1 + 16 \times 0.4 = 8.4$
* Variance: $8.4 - 2.6\times 2.6 = 1.64$
* Standard deviation: $\sqrt{1.64} = 1.2806$
}

\newslide{Expectations Example: Answer II}

\slides{
* We are given that:

$y$               |   1   |   2   |   3   |   4
------------------|-------|-------|-------|-------
$P\left(y\right)$ |  0.3  |  0.2  |  0.1  |  0.4
$y^2$             |   1   |   4   |   9   |  16
$-\log(P(y))$     | 1.204 | 1.609 | 2.302 | 0.916

* Expectation $-\log(P(y))$: $0.3\times 1.204 + 0.2\times 1.609 + 0.1\times 2.302 +0.4\times 0.916 = 1.280$}

\newslide{Sample Based Approximation Example}

\slides{
* You are given the following values samples of heights of students,

    $i$   |   1  |    2 |  3   |   4  |   5  |    6
----------|------|------|------|------|------|------
    $y_i$ |  1.76|  1.73| 1.79 | 1.81 | 1.85 |  1.80

* What is the sample mean?
* What is the sample variance?
* Can you compute sample approximation expected value of $-\log P(y)$?
}

\newslide{Sample Based Approximation Example: Answer}

\slides{
* We can compute:

$i$        |    1    |    2    |    3    |    4    |    5    |    6
-----------|---------|---------|---------|---------|---------|--------
$y_i$      |   1.76  |   1.73  |   1.79  |   1.81  |   1.85  |   1.80
$y^2_i$    |  3.0976 |  2.9929 |  3.2041 |  3.2761 |  3.4225 |  3.2400

* Mean: $\frac{1.76 + 1.73 + 1.79 + 1.81 + 1.85 + 1.80}{6} = 1.79$
* Second moment: $ \frac{3.0976 + 2.9929 + 3.2041 + 3.2761 + 3.4225 + 3.2400}{6} = 3.2055$
* Variance: $3.2055 - 1.79\times1.79 = 1.43\times 10^{-3}$
* Standard deviation: $0.0379$
* No, you can’t compute it. You don’t have access to $P(y)$ directly.}


\newslide{Sample Based Approximation Example}

\slides{
* You are given the following values samples of heights of students,

    $i$   |   1  |    2 |  3   |   4  |   5  |    6
----------|------|------|------|------|------|------
    $y_i$ |  1.76|  1.73| 1.79 | 1.81 | 1.85 |  1.80

* Actually these "data" were sampled from a Gaussian with mean 1.7 and standard deviation 0.15. Are your estimates close to the real values? If not why not?}
