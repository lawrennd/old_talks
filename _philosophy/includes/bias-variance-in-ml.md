\newslide{Bias vs Variance}
\slides{
* 'bias variance dilemma' @Geman-biasvariance92
* Decompose errors as 
    1. due to oversimplification (the bias error) and 
	2. those due to insufficient data to underpin a complex model (variance error).
}

\newslide{In Machine Learning}
\slides{
* Two approaches
   * Use simpler models (better consistency and generalization)
   * Use more complex models and average.
}

\include{_ml/includes/bias-variance-plots.md}

\newslide{Decision Making and Bias-Variance}
\slides{
* In a population we should prefer variance-errors. 
    * Bias errors lead to consistent, decsion making.
	* Consistently wrong!
	
* Variance errors can also be averaged e.g. [bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating) and [boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning)) [@Breiman-bagging96] 
}

