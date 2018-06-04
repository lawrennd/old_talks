### Alan Turing

\columns{\includeimg{../slides/diagrams/turing-times.gif}{}{}{center}}{\includeimg{../slides/diagrams/turing-run.jpg}{}{}{center}}{50%}{50%}
\aligncenter{*Alan Turing, in 1946 he was only 11 minutes slower than the winner of the 1948 games. Would he have won a hypothetical games held in 1946? Source: [Alan Turing Internet Scrapbook](http://www.turing.org.uk/scrapbook/run.html).*}

\slides{
### Probability Winning Olympics?
}

\slides{* He was a formidable Marathon runner. 
* In 1946 he ran a time 2 hours 46 minutes.
    * That's a pace of 3.95 min/km.
* What is the probability he would have won an Olympics if one had been held in 1946?}

\notes{If we had to summarise the objectives of machine learning in one word, a very good candidate for that word would be *generalization*. What is generalization? From a human perspective it might be summarised as the ability to take lessons learned in one domain and apply them to another domain. If we accept the definition given in the first session for machine learning, 
$$
\text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}
$$
then we see that without a model we can't generalise: we only have data. Data is fine for answering very specific questions, like "Who won the Olympic Marathon in 2012?", because we have that answer stored, however, we are not given the answer to many other questions. For example, Alan Turing was a formidable marathon runner, in 1946 he ran a time 2 hours 46 minutes (just under four minutes per kilometer, faster than I and most of the other [Endcliffe Park Run](http://www.parkrun.org.uk/sheffieldhallam/) runners can do 5 km). What is the probability he would have won an Olympics if one had been held in 1946?}

\notes{To answer this question we need to generalize, but before we formalize the concept of generalization let's introduce some formal representation of what it means to generalize in machine learning.}
