\include{_ml/includes/movie-body-count-data.md}

\notes{Let's use the sum rule to compute the approximate
probability that a film from the movie body count website has over 40 deaths.}

\code{deaths = (data.Body_Count>40).sum()  # number of positive outcomes (in sum True counts as 1, False counts as 0)
total_films = data.Body_Count.count()

prob_death = float(deaths)/float(total_films)
print("Probability of deaths being greather than 40 is:", prob_death)}

\writeassignment{We now have an estimate of the probability a film has
greater than 40 deaths. The estimate seems quite high. What could be wrong with
the estimate? Do you think any film you go to in the cinema has this probability
of having greater than 40 deaths?
}{4}{10}

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
    deaths = (data.Body_Count[data.Year==year]>40).sum()
    total_films = (data.Year==year).sum()

    prob_death = float(deaths)/float(total_films)
    print("Probability of deaths being greather than 40 in year", year, "is:", prob_death)}

\codeassignment{Compute the probability for the number of deaths
being over 40 for each year we have in our `data` data frame. Store the
result in a `numpy` array and plot the probabilities against the years using the
`plot` command from `matplotlib`. Do you think the estimate we have created of
$P(y|t)$ is a good estimate? Write your code and your written answers in the box
below.}{5}{20}


\notes{#### Notes for Question }

\notes{Make sure the plot is included in *this* notebook
file (the `IPython` magic command `%matplotlib inline` we ran above will do that
for you, it only needs to be run once per file).}
