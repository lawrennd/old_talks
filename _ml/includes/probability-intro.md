\section{Probabilities}

\notes{We are now going to do some simple review of probabilities and
use this review to explore some aspects of our data.}

\notes{A probability distribution
expresses uncertainty about the outcome of an event. We often encode this
uncertainty in a variable. So if we are considering the outcome of an event,
$Y$, to be a coin toss, then we might consider $Y=1$ to be heads and $Y=0$ to be
tails. We represent the probability of a given outcome with the notation:
$$
P(Y=1) = 0.5
$$
The first rule of probability is that the probability must
normalize. The sum of the probability of all events must equal 1. So if the
probability of heads ($Y=1$) is 0.5, then the probability of tails (the only
other possible outcome) is given by
$$
P(Y=0) = 1-P(Y=1) = 0.5
$$}

\notes{Probabilities
are often defined as the limit of the ratio between the number of positive
outcomes (e.g. *heads*) given the number of trials. If the number of positive
outcomes for event $y$ is denoted by $n$ and the number of trials is denoted by
$N$ then this gives the ratio 
$$
P(Y=y) = \lim_{N\rightarrow
\infty}\frac{n_y}{N}.
$$
In practice we never get to observe an event infinite
times, so rather than considering this we often use the following estimate
$$
P(Y=y) \approx \frac{n_y}{N}.
$$
Let's use this rule to compute the approximate
probability that a film from the movie body count website has over 40 deaths.}

\code{deaths = (film_deaths.Body_Count>40).sum()  # number of positive outcomes (in sum True counts as 1, False counts as 0)
total_films = film_deaths.Body_Count.count()

prob_death = float(deaths)/float(total_films)
print("Probability of deaths being greather than 40 is:", prob_death)}

\writeassignment{We now have an estimate of the probability a film has
greater than 40 deaths. The estimate seems quite high. What could be wrong with
the estimate? Do you think any film you go to in the cinema has this probability
of having greater than 40 deaths?

Why did we have to use `float` around our
counts of deaths and total films? What would the answer have been if we hadn't
used the `float` command? If we were using Python 3 would we have this problem?}{4}{20}

\section{Conditioning}

\notes{When predicting whether a coin turns up head or tails, we might
think that this event is *independent* of the year or time of day. If we include
an observation such as time, then in a probability this is known as
*condtioning*. We use this notation, $P(Y=y|T=t)$, to condition the outcome on a
second variable (in this case time). Or, often, for a shorthand we use $P(y|t)$
to represent this distribution (the $Y=$ and $T=$ being implicit). Because we
don't believe a coin toss depends on time then we might write that 
$$
P(y|t) =
p(y).
$$
However, we might believe that the number of deaths is dependent on the
year. For this we can try estimating $P(Y>40 | T=2000)$ and compare the result,
for example to $P(Y>40|2002)$ using our empirical estimate of the probability.}

\code{for year in [2000, 2002]:
    deaths = (film_deaths.Body_Count[film_deaths.Year==year]>40).sum()
    total_films = (film_deaths.Year==year).sum()

    prob_death = float(deaths)/float(total_films)
    print("Probability of deaths being greather than 40 in year", year, "is:", prob_death)}

\codeassignment{Compute the probability for the number of deaths
being over 40 for each year we have in our `film_deaths` data frame. Store the
result in a `numpy` array and plot the probabilities against the years using the
`plot` command from `matplotlib`. Do you think the estimate we have created of
$P(y|t)$ is a good estimate? Write your code and your written answers in the box
below.}{5}{20}

#### Question 5 Answer Text

\notes{Write your answer to the question in this box.}

#### Notes for Question 5

\notes{Make sure the plot is included in *this* notebook
file (the `IPython` magic command `%matplotlib inline` we ran above will do that
for you, it only needs to be run once per file).}

\newslide{Probability Review}

\slides{
* We are interested in trials which result in two random variables,
  $X$ and $Y$, each of which has an ‘outcome’
  denoted by $x$ or $y$.
* We summarise the notation and terminology for these distributions in
  the following table.}

\newslide{ }

Terminology | Mathematical notation | Description
------|-------------|-------------
joint | $P(X=x, Y=y)$ | prob. that X=x *and* Y=y
marginal | $P(X=x)$ | prob. that X=x *regardless of* Y
conditional | $P(X=x\vert Y=y)$ | prob. that X=x *given that* Y=y

\aligncenter{The different basic probability distributions.}
  

\setupcode{import teaching_plots as plot}
\plotcode{plot.prob_diagram(diagrams='../slides/diagrams/mlai')}

### A Pictorial Definition of Probability

\includesvg{../slides/diagrams/mlai/prob_diagram.svg}

\alignright{Inspired by lectures from Christopher Bishop}

### Definition of probability distributions.

      Terminology        |              Definition                                |      Probability Notation
-------------------------|--------------------------------------------------------|------------------------------
  Joint Probability      | $\lim_{N\rightarrow\infty}\frac{n_{X=3,Y=4}}{N}$       | $P\left(X=3,Y=4\right)$
  Marginal Probability   | $\lim_{N\rightarrow\infty}\frac{n_{X=5}}{N}$           | $P\left(X=5\right)$
 Conditional Probability | $\lim_{N\rightarrow\infty}\frac{n_{X=3,Y=4}}{n_{Y=4}}$ | $P\left(X=3\vert Y=4\right)$
 

### Notational Details

\slides{
* Typically we should write out
  $P\left(X=x,Y=y\right)$.

* In practice, we often use $P\left(x,y\right)$.
* This looks very much like we might write a multivariate function,
  *e.g.*
  $f\left(x,y\right)=\frac{x}{y}$.
  * For a multivariate function though,
    $f\left(x,y\right)\neq f\left(y,x\right)$.
  * However
    $P\left(x,y\right)=P\left(y,x\right)$
    because
    $P\left(X=x,Y=y\right)=P\left(Y=y,X=x\right)$.
* We now quickly review the ‘rules of probability’.}

\notes{Typically we should write out
$P\left(X=x,Y=y\right)$, but in practice we often shorten this to $P\left(x,y\right)$. This looks very much like we might write a multivariate function, *e.g.*
 
 $$f\left(x,y\right)=\frac{x}{y},$$ 
 
but for a multivariate funciton

$$f\left(x,y\right)\neq f\left(y,x\right)$$.

However,

$$P\left(x,y\right)=P\left(y,x\right)$$

because

$$P\left(X=x,Y=y\right)=P\left(Y=y,X=x\right).$$

Sometimes I think of this as akin to the way in Python we can write 'keyword arguments' in functions. If we use keyword arguments, the ordering of arguments doesn't matter.}

\notes{We've now introduced conditioning and independence to
the notion of probability and computed some conditional probabilities on a
practical example The scatter plot of deaths vs year that we created above can
be seen as a *joint* probability distribution. We represent a joint probability
using the notation $P(Y=y, T=t)$ or $P(y, t)$ for short. Computing a joint
probability is equivalent to answering the simultaneous questions, what's the
probability that the number of deaths was over 40 and the year was 2002? Or any
other question that may occur to us. Again we can easily use pandas to ask such
questions.}

\code{year = 2000
deaths = (film_deaths.Body_Count[film_deaths.Year==year]>40).sum()
total_films = film_deaths.Body_Count.count() # this is total number of films
prob_death = float(deaths)/float(total_films)
print("Probability of deaths being greather than 40 and year being", year, "is:", prob_death)}

\newslide{Normalization}

\slides{
*All* distributions are normalized. This is clear from the fact that
$\sum_{x}n_{x}=N$, which gives
$$\sum_{x}P\left(x\right)={\lim_{N\rightarrow\infty}}\frac{\sum_{x}n_{x}}{N}={\lim_{N\rightarrow\infty}}\frac{N}{N}=1.$$
A similar result can be derived for the marginal and conditional
distributions.}

### The Product Rule
\slides{
-   $P\left(x|y\right)$ is
    $${\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{n_{y}}.$$

-   $P\left(x,y\right)$ is
    $${\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{N}={\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{n_{y}}\frac{n_{y}}{N}$$
    or in other
    words$$P\left(x,y\right)=P\left(x|y\right)P\left(y\right).$$
    This is known as the product rule of probability.}
	
\notes{This number is the joint probability, $P(Y, T)$ which is
much *smaller* than the conditional probability. The number can never be bigger
than the conditional probabililty because it is computed using the *product
rule*.
$$
p(Y=y, T=t) = p(Y=y|T=t)p(T=t)
$$
and $$p(T=t)$$ is a probability
distribution, which is equal or less than 1, ensuring the joint distribution is
typically smaller than the conditional distribution.}

\notes{The product rule is a
*fundamental* rule of probability, and you must remember it! It gives the
relationship between the two questions: 1) What's the probability that a film
was made in 2002 and has over 40 deaths? and 2) What's the probability that a
film has over 40 deaths given that it was made in 2002?}

\notes{In our shorter notation
we can write the product rule as
$$
p(y, t) = p(y|t)p(t)
$$
We can see the
relation working in practice for our data above by computing the different
values for $t=2000$.}

\code{p_t = float((film_deaths.Year==2002).sum())/float(film_deaths.Body_Count.count())
p_y_given_t = float((film_deaths.Body_Count[film_deaths.Year==2002]>40).sum())/float((film_deaths.Year==2002).sum())
p_y_and_t = float((film_deaths.Body_Count[film_deaths.Year==2002]>40).sum())/float(film_deaths.Body_Count.count())

print("P(t) is", p_t)
print("P(y|t) is", p_y_given_t)
print("P(y,t) is", p_y_and_t)}

### The Sum Rule

\slides{Ignoring the limit in our definitions:

-   The marginal probability $P\left(y\right)$ is
    ${\lim_{N\rightarrow\infty}}\frac{n_{y}}{N}$ .

-   The joint distribution $P\left(x,y\right)$ is
    ${\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{N}$.

-   $n_{y}=\sum_{x}n_{x,y}$
    so$${\lim_{N\rightarrow\infty}}\frac{n_{y}}{N}={\lim_{N\rightarrow\infty}}\sum_{x}\frac{n_{x,y}}{N},$$
    in other words
    $$P\left(y\right)=\sum_{x}P\left(x,y\right).$$
    This is known as the sum rule of probability.}

\notes{The other *fundamental rule* of probability is the *sum rule*
this tells us how to get a *marginal* distribution from the joint distribution.
Simply put it says that we need to sum across the value we'd like to remove.
$$
P(Y=y) = \sum_{t} P(Y=y, T=t)
$$
Or in our shortened notation
$$
P(y) = \sum_{t}
P(y, t)
$$}

\codeassignment{Write code that computes $P(y)$ by adding $P(y, t)$
for all values of $t$.}{6}{10}

### Bayes’ Rule

\slides{
* From the product rule,
  $$
  P\left(y,x\right)=P\left(x,y\right)=P\left(x|y\right)P\left(y\right),$$
  so
  $$
  P\left(y|x\right)P\left(x\right)=P\left(x|y\right)P\left(y\right)
  $$
  which leads to Bayes’ rule,
  $$
  P\left(y|x\right)=\frac{P\left(x|y\right)P\left(y\right)}{P\left(x\right)}.
  $$
}

\notes{Bayes rule is a very simple rule, it's hardly worth the name of
a rule at all. It follows directly from the product rule of probability. Because
$P(y, t) = P(y|t)P(t)$ and by symmetry $P(y,t)=P(t,y)=P(t|y)P(y)$ then by
equating these two equations and dividing through by $P(y)$ we have
$$
P(t|y) =
\frac{P(y|t)P(t)}{P(y)}
$$
which is known as Bayes' rule (or Bayes's rule, it
depends how you choose to pronounce it). It's not difficult to derive, and its
importance is more to do with the semantic operation that it enables. Each of
these probability distributions represents the answer to a question we have
about the world. Bayes rule (via the product rule) tells us how to *invert* the
probability.}

\newslide{Bayes’ Theorem Example}

\slides{
* There are two barrels in front of you. Barrel One contains 20 apples
  and 4 oranges. Barrel Two other contains 4 apples and 8 oranges. You
  choose a barrel randomly and select a fruit. It is an apple. What is
  the probability that the barrel was Barrel One?}

\newslide{Bayes’ Theorem Example: Answer I}

\slides{
* We are given that: 
  $$\begin{aligned}
    P(\text{F}=\text{A}|\text{B}=1) = & 20/24 \\
    P(\text{F}=\text{A}|\text{B}=2) = & 4/12 \\
    P(\text{B}=1) = & 0.5 \\
    P(\text{B}=2) = & 0.5
  \end{aligned}$$
}

\newslide{Bayes’ Theorem Example: Answer II}

\slides{
* We use the sum rule to compute: 
  $$\begin{aligned}
    P(\text{F}=\text{A}) = & P(\text{F}=\text{A}|\text{B}=1)P(\text{B}=1) \\& + P(\text{F}=\text{A}|\text{B}=2)P(\text{B}=2) \\
          = & 20/24\times 0.5 + 4/12 \times 0.5 = 7/12
   \end{aligned}$$
* And Bayes’ theorem tells us that: 
  $$\begin{aligned}
    P(\text{B}=1|\text{F}=\text{A}) = & \frac{P(\text{F} = \text{A}|\text{B}=1)P(\text{B}=1)}{P(\text{F}=\text{A})}\\ 
         = & \frac{20/24 \times 0.5}{7/12} = 5/7
  \end{aligned}$$}


\newslide{Reading & Exercises}

\slides{* Bishop on probability distributions: page
    12–17 (Section 1.2).

* Complete Exercise 1.3 in Bishop.}


\newslide{Expectation Computation Example

\slides{
* Consider the following distribution.

$y$        |  1  |  2  |  3  |  4
-----------|-----|-----|-----|-----
$P\left(y\right)$ |  0.3|  0.2|  0.1|  0.4

* What is the mean of the distribution?
* What is the standard deviation of the distribution?
* Are the mean and standard deviation representative of the distribution form?
* What is the expected value of $-\log P(y)$?}

\slides{### Expectations Example: Answer

-   We are given that:

$y$        |   1   |   2   |   3   |   4
---------------------|-------|-------|-------|-------
$P\left(y\right)$ |  0.3  |  0.2  |  0.1  |  0.4
$y^2$       |   1   |   4   |   9   |  16
  $-\log(P(y))$   | 1.204 | 1.609 | 2.302 | 0.916

-   Mean:
    $1\times 0.3 + 2\times 0.2 + 3 \times 0.1 + 4 \times 0.4 = 2.6$

-   Second moment:
    $1 \times 0.3 + 4 \times 0.2 + 9 \times 0.1 + 16 \times 0.4 = 8.4$

-   Variance: $8.4 - 2.6\times 2.6 = 1.64$

-   Standard deviation: $\sqrt{1.64} = 1.2806$

-   Expectation $-\log(P(y))$:
    $0.3\times 1.204 + 0.2\times 1.609 + 0.1\times 2.302 +0.4\times 0.916 = 1.280$}

\slides{### Sample Based Approximation Example

-   You are given the following values samples of heights of students,

    $i$   |   1  |    2 |  3   |   4  |   5  |    6
----------|------|------|------|------|------|------
    $y_i$ |  1.76|  1.73| 1.79 | 1.81 | 1.85 |  1.80

-   What is the sample mean?

-   What is the sample variance?

-   Can you compute sample approximation expected value of
    $-\log P(y)$?

-   Actually these “data” were sampled from a Gaussian with mean 1.7 and
    standard deviation 0.15. Are your estimates close to the real
    values? If not why not?}

\slides{### Sample Based Approximation Example: Answer

-   We can compute:

$i$        |    1    |    2    |    3    |    4    |    5    |    6
-------------------|--------|--------|--------|--------|--------|--------
$y_i$  |   1.76  |   1.73  |   1.79  |   1.81  |   1.85  |   1.80
$y^2_i$ |  3.0976 |  2.9929 |  3.2041 |  3.2761 |  3.4225 |  3.2400

-   Mean: $\frac{1.76 + 1.73 + 1.79 + 1.81 + 1.85 + 1.80}{6} = 1.79$

-   Second moment:
    $ \frac{3.0976 + 2.9929 + 3.2041 + 3.2761 + 3.4225 + 3.2400}{6} = 3.2055$

-   Variance: $3.2055 - 1.79\times1.79 = 1.43\times 10^{-3}$

-   Standard deviation: $0.0379$

-   No, you can’t compute it. You don’t have access to
    $P(y)$ directly.}

\notes{### Probabilities for Extracting Information from Data}

\notes{What use is all this
probability in data science? Let's think about how we might use the
probabilities to do some decision making. Let's load up a little more
information about the movies.}

\code{movies = pd.read_csv('./R-vs-Python-master/Deadliest movies scrape/code/film-death-counts-Python.csv')
movies.columns}

\writeassignment{Now we see we have several additional features
including the quality rating (`IMDB_Rating`). Let's assume we want to predict
the rating given the other information in the data base. How would we go about
doing it? 

Using what you've learnt about joint, conditional and marginal
probabilities, as well as the sum and product rule, how would you formulate the
question you want to answer in terms of probabilities? Should you be using a
joint or a conditional distribution? If it's conditional, what should the
distribution be over, and what should it be conditioned on?}{7}{20}

