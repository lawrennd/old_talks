\include{_ml/includes/nigerian-nmis-data.md}

\notes{Let's use the sum rule to compute the estimate the 
probability that a facility has more than two nurses.}

\code{large = (data.num_nurses_fulltime>2).sum()  # number of positive outcomes (in sum True counts as 1, False counts as 0)
total_facilities = data.num_nurses_fulltime.count()

prob_large = float(large)/float(total_facilities)
print("Probability of number of nurses being greather than 2 is:", prob_large)}


\section{Conditioning}

\notes{When predicting whether a coin turns up head or tails, we might
think that this event is *independent* of the year or time of day. If we include
an observation such as time, then in a probability this is known as
*condtioning*. We use this notation, $P(Y=y|X=x)$, to condition the outcome on a
second variable (in this case the number of doctors). Or, often, for a shorthand we use $P(y|x)$ to represent this distribution (the $Y=$ and $X=$ being implicit). If two variables are independent then we find that
$$
P(y|x) = p(y).
$$
However, we might believe that the number of nurses is dependent on the
number of doctors. For this we can try estimating $P(Y>2 | X>1)$ and compare the result,
for example to $P(Y>2|X\leq 1)$ using our empirical estimate of the probability.}

\code{large = ((data.num_nurses_fulltime>2) & (data.num_doctors_fulltime>1)).sum()
total_large_doctors = (data.num_doctors_fulltime>1).sum()
prob_both_large = large/total_large_doctors
print("Probability of number of nurses being greater than 2 given number of doctors is greater than 1 is:", prob_both_large)
}

\codeassignment{Write code that prints out the probability of nurses being greater than 2 for different numbers of doctors.}{2}{15}


\notes{#### Notes for Question }

\notes{Make sure the plot is included in *this* notebook
file (the `IPython` magic command `%matplotlib inline` we ran above will do that
for you, it only needs to be run once per file).}
