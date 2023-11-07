\ifndef{whatDoesMachineLearningDo}
\define{whatDoesMachineLearningDo}

\editme

\subsection{What does Machine Learning do?}
\slides{
* Automation scales by codifying processes and automating them.
* Need:
    * Interconnected components
	* Compatible components
* Early examples:
    * cf Colt 45, Ford Model T
}

\notes{Any process of automation allows us to scale what we do by
codifying a process in some way that makes it efficient and
repeatable. Machine learning automates by emulating human (or other
actions) found in data. Machine learning codifies in the form of a
mathematical function that is learnt by a computer. If we can create
these mathematical functions in ways in which they can interconnect,
then we can also build systems.}

\notes{Machine learning works through codifying a prediction of
interest into a mathematical function. For example, we can try and
predict the probability that a customer wants to by a jersey given
knowledge of their age, and the latitude where they live. The
technique known as logistic regression estimates the odds that someone
will by a jumper as a linear weighted sum of the features of
interest.}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ \text{odds} = \frac{p(\text{bought})}{p(\text{not bought})} $$

$$ \log \text{odds}  = \weightScalar_0 + \weightScalar_1 \text{age} + \weightScalar_2 \text{latitude}.$$
\notes{Here $\weightScalar_0$, $\weightScalar_1$ and $\weightScalar_2$
are the parameters of the model. If $\weightScalar_1$ and
$\weightScalar_2$ are both positive, then the log-odds that someone
will buy a jumper increase with increasing latitude and age, so the
further north you are and the older you are the more likely you are to
buy a jumper. The parameter $\weightScalar_0$ is an offset parameter
and gives the log-odds of buying a jumper at zero age and on the
equator. It is likely to be negative[^logarithm] indicating that the
purchase is odds-against. This is also a classical statistical model,
and models like logistic regression are widely used to estimate
probabilities from ad-click prediction to disease risk.

[^logarithm]: The logarithm of a number less than one is negative, for
    a number greater than one the logarithm is positive. So if odds
    are greater than evens (odds-on) the log-odds are positive, if the
    odds are less than evens (odds-against) the log-odds will be
    negative.}

\notes{This is called a generalized linear model, we can also think of
it as estimating the *probability* of a purchase as a nonlinear
function of the features (age, latitude) and the parameters (the
$\weightScalar$ values). The function is known as the *sigmoid* or
[logistic function](https://en.wikipedia.org/wiki/Logistic_regression),
thus the name *logistic* regression.}

\include{_ml/includes/sigmoid-function.md}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ p(\text{bought}) =  \sigmoid{\weightScalar_0 + \weightScalar_1 \text{age} + \weightScalar_2 \text{latitude}}.$$

\notes{In the case where we have *features* to help us predict, we
sometimes denote such features as a vector, $\inputVector$, and we
then use an inner product between the features and the parameters,
$\weightVector^\top \inputVector = \weightScalar_1 \inputScalar_1 +
\weightScalar_2 \inputScalar_2 + \weightScalar_3 \inputScalar_3 ...$,
to represent the argument of the sigmoid.}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ p(\text{bought}) =  \sigmoid{\weightVector^\top \inputVector}.$$
\notes{More generally, we aim to predict some aspect of our data, $\dataScalar$, by relating it through a mathematical function, $\mappingFunction(\cdot)$, to the parameters, $\weightVector$ and the data, $\inputVector$.}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ \dataScalar =  \mappingFunction\left(\inputVector, \weightVector\right).$$
\slides{
. . .

}We call $\mappingFunction(\cdot)$ the *prediction function*.

\notes{To obtain the fit to data, we use a separate function called the *objective function* that gives us a mathematical representation of the difference between our predictions and the real data. }

\newslide{Fit to Data}
\slides{
* Use an objective function
}
$$\errorFunction(\weightVector, \dataMatrix, \inputMatrix)$$
\slides{
. . .

* E.g. least squares}\notes{A commonly used examples (for example in a regression problem) is least squares,}
$$\errorFunction(\weightVector, \dataMatrix, \inputMatrix) = \sum_{i=1}^\numData \left(\dataScalar_i - \mappingFunction(\inputVector_i, \weightVector)\right)^2.$$

\newslide{Two Components}
\slides{
* Prediction function, $\mappingFunction(\cdot)$
* Objective function, $\errorFunction(\cdot)$
}
\notes{If a linear prediction function is combined with the least squares objective function, then that gives us a classical *linear regression*, another classical statistical model. Statistics often focusses on linear models because it makes interpretation of the model easier. Interpretation is key in statistics because the aim is normally to validate questions by analysis of data. Machine learning has typically focused more on the prediction function itself and worried less about the interpretation of parameters. In statistics, where interpretation is typically more important than prediction, parameters are normally denoted by $\boldsymbol{\beta}$ instead of $\weightVector$.}

\newslide{Prediction vs Interpretation}

\notes{A key difference between statistics and machine learning, is that (traditionally) machine learning has focussed on predictive capability and statistics has focussed on interpretability. That means that in a statistics class far more emphasis will be placed on interpretation of the parameters. In machine learning, the parameters, $\mathbf{w}, are just a means to an end. But in statistics, when we denote the parameters by $\boldsymbol{\beta}$, we often use the parameters to tell us something about the disease.} 

\notes{So we move between}
$$ p(\text{bought}) =  \sigmoid{w_0 + w_1 \text{age} + w_2 \text{latitude}}.$$

\notes{to denote the emphasis is on predictive power to}

$$ p(\text{bought}) =  \sigmoid{\beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}}.$$

\notes{to denote the emphasis is on interpretation of the parameters.}

\notes{Another effect of the focus on prediction in machine learning is that *non-linear* approaches, which can be harder to interpret, are more widely deployedin machine learning -- they tend to improve quality of predictions at the expense of interpretability.}
\endif
