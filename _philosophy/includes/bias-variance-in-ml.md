\ifndef{biasVarianceInML}
\define{biasVarianceInML}

\editme

\subsection{Bias vs Variance}

\notes{One way of looking at this technically in machine learning is to decompose our generalization error into two parts. The bias-variance dilemma emerges from looking at these two parts and observing that part of our error comes from oversimplification in our model (the bias error) and part of our error comes from the fact that there's insufficient data to pin down the parameters of a more complex model (the variance error).}

\slides{* 'bias variance dilemma' @Geman-biasvariance92
* Decompose errors as 
    1. due to oversimplification (the bias error) and 
    2. those due to insufficient data to underpin a complex model (variance error).}

\subsection{In Machine Learning}

\notes{In the past (before the neural network revolution!) there were two principle approaches to resolving the bias-variance dilemma. Either you use over simple models, which lead to better consistency in their generalization and well determined parameters. Or you use more complex models and make use of some form of averaging to deal with the variance.} 

\notes{
* Two approaches
   * Use simpler models (better consistency and good generalization)
   * Use more complex models and average to remove variance.}

\include{_ml/includes/bias-variance-plots.md}

\subsection{Decision Making and Bias-Variance}

\notes{However in a population, where there are many decision makers, I would argue we should always err towards variance error rather than bias. This is because the averaging effects occur naturally, and we don't have large sections of the population making consistent errors.}

\slides{
* In a population we should prefer variance-errors. 
    * Bias errors lead to consistent, decsion making.
	* Consistently wrong!
	
* Variance errors can also be averaged e.g. [bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating)  [@Breiman-bagging96] }

\notes{In practice averaging of variance errors is also prosed by Breiman and is called [bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating)  [@Breiman-bagging96]. (Another ensemble method that works with biased models is called [boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning)).}

\endif
