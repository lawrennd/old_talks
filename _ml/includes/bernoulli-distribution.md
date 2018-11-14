\newslide{Bernoulli Distribution}

\slides{* Binary classification: need a probability distribution for discrete variables. 
* Discrete probability is in some ways easier:  $P(\dataScalar=1) = \pi$ & specify distribution as a table.
* Instead of $\dataScalar=-1$ for negative class we take $\dataScalar=0$.}
\notes{Our focus has been on models where the objective function is inspired by a probabilistic analysis of the problem. In particular we've argued that we answer questions about the data set by placing probability distributions over the various quantities of interest. For the case of binary classification this will normally involve introducing probability distributions for discrete variables. Such probability distributions, are in some senses easier than those for continuous variables, in particular we can represent a probability distribution over $\dataScalar$, where $\dataScalar$ is binary, with one value. If we specify the probability that $\dataScalar=1$ with a number that is between 0 and 1, i.e. let's say that $P(\dataScalar=1) = \pi$ (here we don't mean $\pi$ the number, we are setting $\pi$ to be a variable) then we can specify the probability distribution through a table.}

| $\dataScalar$      | 0  | 1     |
|:------:|:---------:|:-----:|
| $P(\dataScalar)$ | $(1-\pi)$ | $\pi$ |

\slides{
  This is the [Bernoulli distribution](http://en.wikipedia.org/wiki/Bernoulli_distribution).}

\newslide{Mathematical Switch}

\slides{* The Bernoulli distribution}\notes{Mathematically we can use a trick to implement this same table. We can use the value $\dataScalar$ as a mathematical switch and write that}
  $$
  P(\dataScalar) = \pi^\dataScalar (1-\pi)^{(1-\dataScalar)}
  $$
\notes{where our probability distribution is now written as a function of $\dataScalar$. This probability distribution is known as the [Bernoulli distribution](http://en.wikipedia.org/wiki/Bernoulli_distribution). The Bernoulli distribution is a clever trick for mathematically switching between two probabilities if we were to write it as code it would be better described as}\slides{
* Is a clever trick for switching probabilities, as code it would be}

```python
def bernoulli(y_i, pi):
    if y_i == 1:
        return pi
	else:
        return 1-pi
```

\notes{If we insert $\dataScalar=1$ then the function is equal to $\pi$, and if we insert $\dataScalar=0$ then the function is equal to $1-\pi$. So the function recreates the table for the distribution given above.}

\newslide{Jacob Bernoulli's Bernoulli}

\slides{* Bernoulli described the Bernoulli distribution in terms of an 'urn' filled with balls.
* There are red and black balls. There is a fixed number of balls in the urn.
* The portion of red balls is given by $\pi$.
* For this reason in Bernoulli's distribution there is *epistemic* uncertainty about the distribution parameter.}
\notes{The probability distribution is named for [Jacob Bernoulli](http://en.wikipedia.org/wiki/Jacob_Bernoulli), the swiss mathematician. In his book Ars Conjectandi he considered the distribution and the result of a number of 'trials' under the Bernoulli distribution to form the *binomial* distribution. Below is the page where he considers Pascal's triangle in forming combinations of the Bernoulli distribution to realise the binomial distribution for the outcome of positive trials.}

\newslide{}

\includegooglebook{CF4UAAAAQAAJ}{PA87}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.one_figsize)
plot.bernoulli_urn(ax, diagrams='../slides/diagrams/ml/')}

\newslide{Jacob Bernoulli's Bernoulli}

\includesvg{../slides/diagrams/ml/bernoulli-urn.svg}

\newslide{Thomas Bayes's Bernoulli}

\slides{* Bayes described the Bernoulli distribution (he didn't call it that!) in terms of a table and two balls.
* Each ball is rolled so it comes to rest at a uniform distribution across the table.
* The first ball comes to rest at a position that is a $\pi$ times the width of table.
* After placing the first ball you consider whether a second would land to the left or the right.
* For this reason in Bayes's distribution there is considered to be *aleatoric* uncertainty about the distribution parameter.}
\notes{Thomas Bayes also described the Bernoulli distribution, only he didn't refer to Jacob Bernoulli's work, so he didn't call it by that name. He described the distribution in terms of a table (think of a *billiard table*) and two balls. 
Bayes suggests that each ball can be rolled across the table such that it comes to rest at a position that is *uniformly distributed* between the sides of the table. 

Let's assume that the first ball is rolled, and that it comes to reset at a position that is $\pi$ times the width of the table from the left hand side. 

Now, we roll the second ball. We are interested if the second ball ends up on the left side (+ve result) or the right side (-ve result) of the first ball. We use the Bernoulli distribution to determine this.

For this reason in Bayes's distribution there is considered to be *aleatoric* uncertainty about the distribution parameter.}

\newslide{Thomas Bayes' Bernoulli}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.one_figsize)
plot.bayes_billiard(ax, diagrams='../slides/diagrams/ml/')}

\slides{
\startslides{bayes_billiard}{1}{10}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard000.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard001.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard002.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard003.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard004.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard005.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard006.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard007.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard008.svg}}{bayes_billiard}{text-align:center}
\div{\includesvg{../slides/diagrams/ml/bayes-billiard009.svg}}{bayes_billiard}{text-align:center}
}
\notesfigure{\div{\includesvg{../slides/diagrams/ml/bayes-billiard009.svg}}{}{text-align:center}}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('bayes-billiard{counter:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							counter=IntSlider(0,0,9,1))}
