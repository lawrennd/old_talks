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
$$}


\include{_ml/includes/probability-nigerian-nmis.md}
\include{_ml/includes/probability-review.md}

