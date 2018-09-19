### What does Machine Learning do?
\slides{
* Automation scales by codifying processes and automating them.
* Need:
    * Interconnected components
	* Compatible components
* Early examples:
    * cf Colt 45, Ford Model T
}

\notes{Any process of automation allows us to scale what we do by codifying a process in some way that makes it efficient and repeatable. Machine learning automates by emulating human (or other actions) found in data. Machine learning codifies in the form of a mathematical function that is learnt by a computer. If we can create these mathematical functions in ways in which they can interconnect, then we can also build systems.}

\notes{Machine learning works through codifing a prediction of interest into a mathematical function. For example, we can try and predict the probability that a customer wants to by a jersey given knowledge of their age, and the latitude where they live. The technique known as logistic regression estimates the odds that someone will by a jumper as a linear weighted sum of the features of interest.}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ \text{odds} = \frac{p(\text{bought})}{p(\text{not bought})} $$
$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}$$

\notes{Here $\beta_0$, $\beta_1$ and $\beta_2$ are the parameters of the model. If $\beta_1$ and $\beta_2$  are both positive, then the log-odds that someone will buy a jumper increase with increasing latitude and age, so the further north you are and the older you are the more likely you are to buy a jumper. The parameter $\beta_0$ is an offset parameter, and gives the log-odds of buying a jumper at zero age and on the equator. It is likely to be negative[^logarithms] indicating that the purchase is odds-against. This is actually a classical statistical model, and models like logistic regression are widely used to estimate probabilities from ad-click prediction to risk of disease.

[^logarithm]: The logarithm of a number less than one is negative, for a number greater than one the logarithm is positive. So if odds are greater than evens (odds-on) the log-odds are positive, if the odds are less than evens (odds-against) the log-odds will be negative.

This is called a generalized linear model, we can also think of it as estimating the *probability* of a purchase as a nonlinear function of the features (age, lattitude) and the parameters (the $\beta$ values). The function is known as the *sigmoid* or [logistic function](https://en.wikipedia.org/wiki/Logistic_regression), thus the name *logistic* regression.}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ p(\text{bought}) =  \sigmoid{\beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}}$$

\notes{In the case where we have *features* to help us predict, we sometimes denote such features as a vector, $\inputVector$, and we then use an inner product between the features and the parameters, $\boldsymbol{\beta}^\top \inputVector = \beta_1 \inputScalar_1 + \beta_2 \inputScalar_2 + \beta_3 \inputScalar_3 ...$, to represent the argument of the sigmoid.}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ p(\text{bought}) =  \sigmoid{\boldsymbol{\beta}^\top \inputVector}$$

\notes{More generally, we aim to predict some aspect of our data, $\dataScalar$, by relating it through a mathematical function, $\mappingFunction(\cdot)$, to the parameters, $\boldsymbol{\beta}$ and the data, $\inputVector$.}

\newslide{Codify Through Mathematical Functions}
\slides{
* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
}
$$ \dataScalar =  \mappingFunction\left(\inputVector, \boldsymbol{\beta}\right)$$
\slides{
. . .

}
We call $\mappingFunction(\cdot)$ the *prediction function*

\notes{To obtain the fit to data, we use a separate function called the *objective function* that gives us a mathematical representation of the difference between our predictions and the real data. }

\newslide{Fit to Data}
\slides{
* Use an objective function
}
$$\errorFunction(\boldsymbol{\beta}, \dataMatrix, \inputMatrix)$$
\slides{
. . .

* E.g. least squares}\notes{A commonly used examples (for example in a regression problem) is least squares,}
$$\errorFunction(\boldsymbol{\beta}, \dataMatrix, \inputMatrix) = \sum_{i=1}^\numData \left(\dataScalar_i - \mappingFunction(\inputVector_i, \boldsymbol{\beta})\right)^2.$$

\newslide{Two Components}
\slides{
* Prediction function, $\mappingFunction(\cdot)$
* Objective function, $\errorFunction(\cdot)$
}
\notes{If a linear prediction function is combined with the least squares objective function then that gives us a classical *linear regression*, another classical statistical model. Statistics often focusses on linear models because it makes interpretation of the model easier. Interpretation is key in statistics because the aim is normally to validate questions by analysis of data. Machine learning has typically focussed more on the prediction function itself and worried less about the interpretation of parameters, which are normally denoted by $\mathbf{w}$ instead of $\boldsymbol{\beta}$. As a result *non-linear* functions are explored more often as they tend to improve quality of predictions but at the expense of interpretability.}
