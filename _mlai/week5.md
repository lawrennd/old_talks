---
layout: lectures
title: "Generalization: Model Validation"
author: Neil D. Lawrence
date: 2015/10/27
transition: None
---

\include{talk-macros.tex}

### Review

* Last time: introduced basis functions.
* Showed how to maximize the likelihood of a non-linear model that's linear in parameters.
* Explored the different characteristics of different basis function models


### Alan Turing
\notes{* He was a formidable Marathon runner. 
* In 1946 he ran a time 2 hours 46 minutes.
* What is the probability he would have won an Olympics if one had been held in 1946?}

\notes{If we had to summarise the objectives of machine learning in one word, a very good candidate for that word would be *generalization*. What is generalization? From a human perspective it might be summarised as the ability to take lessons learned in one domain and apply them to another domain. If we accept the definition given in the first session for machine learning, 
$$
\text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}
$$
then we see that without a model we can't generalise: we only have data. Data is fine for answering very specific questions, like "Who won the Olympic Marathon in 2012?", because we have that answer stored, however, we are not given the answer to many other questions. For example, Alan Turing was a formidable marathon runner, in 1946 he ran a time 2 hours 46 minutes (just under four minutes per kilometer, faster than I and most of the other [Endcliffe Park Run](http://www.parkrun.org.uk/sheffieldhallam/) runners can do 5 km). What is the probability he would have won an Olympics if one had been held in 1946?}
\columns{\includeimg{../slides/diagrams/turing-times.gif}{90%}{}{center}}{\includeimg{../slides/diagrams/turing-run.jpg}{90%}{}{center}}{50%}{50%}
\aligncenter{*Alan Turing, in 1946 he was only 11 minutes slower than the winner of the 1948 games. Would he have won a hypothetical games held in 1946? Source: [Alan Turing Internet Scrapbook](http://www.turing.org.uk/scrapbook/run.html).*}
\notes{To answer this question we need to generalize, but before we formalize the concept of generalization let's introduce some formal representation of what it means to generalize in machine learning.}

### Expected Loss

\notes{Our objective function so far has been the negative log likelihood, which we have minimized (via the sum of squares error) to obtain our model. However, there is an alternative perspective on an objective function, that of a *loss function*. A loss function is a cost function associated with the penalty you might need to pay for a particular incorrect decision. One approach to machine learning involves specifying a loss function and considering how much a particular model is likely to cost us across its lifetime. We can represent this with an expectation. If our loss function is given as $L(\dataScalar, \inputScalar, \mappingVector)$ for a particular model that predicts $\dataScalar$ given $\inputScalar$ and $\mappingVector$ then we are interested in minimizing the expected loss under the likely distribution of $\dataScalar$ and $\inputScalar$. To understand this formally we define the *true* distribution of the data samples, $\dataScalar$, $\inputScalar$. This is a particularl distribution that we don't have access to very often, and to represent that we define it with a variant of the letter 'P', $\mathbb{P}(\dataScalar, \inputScalar)$. If we genuinely pay $L(\dataScalar, \inputScalar, \mappingVector)$ for every mistake we make, and the future test data is genuinely drawn from $\mathbb{P}(\dataScalar, \inputScalar)$ then we can define our expected loss, or risk, to be,}
$$
R(\mappingVector) = \int L(\dataScalar, \inputScalar, \mappingVector) \mathbb{P}(\dataScalar, \inputScalar) \text{d}\dataScalar
\text{d}\inputScalar.
$$
\notes{Of course, in practice, this value can't be computed *but* it serves as a reminder of what it is we are aiming to minimize and under certain circumstances it can be approximated.
}

### Sample Based Approximations
\notes{A sample based approximation to an expectation involves replacing the true expectation with a sum over samples from the distribution.}\slides{* Sample based approximation: replace true expectation with sum over samples.}
  $$
  \int \mappingFunction(z) p(z) \text{d}\dataScalar
  \text{d}z\approx \frac{1}{s}\sum_{i=1}^s \mappingFunction(z_i).
  $$
\notes{if $\{z_i\}_{i=1}^s$ are a set of $s$ independent and identically distributed samples from the distribution $p(z)$. This approximation becomes better for larger $s$, although the *rate of convergence* to the true integral will be very dependent on the distribution $p(z)$ *and* the function $\mappingFunction(z)$.

That said, this means we can approximate our true integral with the sum,}\slides{* Allows us to approximate true integral with sum}
  $$
  R(\mappingVector) \approx \frac{1}{\numData}\sum_{i=1}^{\numData} L(\dataScalar_i, \inputScalar_i, \mappingVector),
  $$
\slides{
### Empirical Risk Minimization
* If the loss is the *squared loss*}\notes{if $\dataScalar_i$ and $\inputScalar_i$ are independent samples from the true distribution $\mathbb{P}(\dataScalar, \inputScalar)$. Minimizing this sum directly is known as *empirical risk minimization*. The sum of squares error we have been using can be recovered for this case by considering a *squared loss*,}
$$
L(\dataScalar, \inputScalar, \mappingVector) = (\dataScalar-\mappingVector^\top\boldsymbol{\phi}(\inputScalar))^2,
$$
\notes{which gives an empirical risk of the form}\slides{* This recovers the *empirical risk*}
$$
R(\mappingVector) \approx \frac{1}{\numData} \sum_{i=1}^{\numData}
(\dataScalar_i - \mappingVector^\top \boldsymbol{\phi}(\inputScalar_i))^2
$$
\notes{which up to the constant $\frac{1}{\numData}$ is identical to the objective function we have been using so far.}

### Estimating Risk through Validation

\notes{Unfortuantely, minimising the empirial risk only guarantees something about our performance on the training data. If we don't have enough data for the approximation to the risk to be valid, then we can end up performing significantly worse on test data. Fortunately, we can also estimate the risk for test data through estimating the risk for unseen data. The main trick here is to 'hold out' a portion of our data from training and use the models performance on that sub-set of the data as a proxy for the true risk. This data is known as 'validation' data. It contrasts with test data, because its values are known at the model design time. However, in contrast to test date we don't use it to fit our model. This means that it doesn't exhibit the same bias that the empirical risk does when estimating the true risk.

In this lab we will explore techniques for model selection that make use of validation data. Data that isn't seen by the model in the learning (or fitting) phase, but is used to *validate* our choice of model from amoungst the different designs we have selected.

In machine learning, we are looking to minimise the value of our objective function $E$ with respect to its parameters $\mappingVector$. We do this by considering our training data. We minimize the value of the objective function as it's observed at each training point. However we are really interested in how the model will perform on future data. For evaluating that we choose to *hold out* a portion of the data for evaluating the quality of the model.

We will review the different methods of model selection on the Olympics marathon data. Firstly we import the Olympics data.}

\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']}

We can plot them to check that they've loaded in correctly.

\setupcode{%matplotlib inline
import matplotlib.pyplot as plt}

\plotcode{plt.plot(x, y, 'rx')}

### Hold Out Validation

\notes{The first thing we'll do is fit a standard linear model to the data. We recall from previous lectures and lab classes that to do this we need to solve the system
$$
\basisMatrix^\top \basisMatrix \mappingVector = \basisMatrix^\top \dataVector
$$
for $\mappingVector$  and use the resulting vector to make predictions at the training points and test points,
$$
\mappingFunctionVector = \basisMatrix \mappingVector.
$$
The prediction function can be used to compute the objective function,
$$
E(\mappingVector) = \sum_{i}^{\numData} (\dataScalar_i - \mappingVector^\top\phi(\dataVector_i))^2
$$
by substituting in the prediction in vector form we have
$$
E(\mappingVector) =  (\dataVector - \mappingFunctionVector)^\top(\dataVector - \mappingFunctionVector)
$$}

\codeassignment{In this question you will construct some flexible general code for fitting linear models.

Create a python function that computes $\basisMatrix$ for the linear basis,
$$\basisMatrix = \begin{bmatrix} \dataVector & \mathbf{1}\end{bmatrix}$$
Name your function `linear`. `Phi` should be in the form of a *design matrix* and `x` should be in the form of a `numpy` two dimensional array with $\numData$ rows and 1 column Calls to your function should be in the following form:

```Phi = linear(x)```

Create a python function that accepts, as arguments, a python function that defines a basis (like the one you've just created called `linear`) as well as a set of inputs and a vector of parameters. Your new python function should return a prediction. Name your function `prediction`. The return value `f` should be a two dimensional `numpy` array with $\numData$ rows and $1$ column, where $\numData$ is the number of data points. Calls to your function should be in the following form:

```f = prediction(w, x, linear)```

Create a python function that computes the sum of squares objective function (or error function). It should accept your input data (or covariates) and target data (or response variables) and your parameter vector `w` as arguments. It should also accept a python function that represents the basis. Calls to your function should be in the following form:

```e = objective(w, x, y, linear)```

Create a function that solves the linear system for the set of parameters that minimizes the sum of squares objective. It should accept input data, target data and a python function for the basis as the inputs. Calls to your function should be in the following form:

```w = fit(x, y, linear)```

Fit a linear model to the olympic data using these functions and plot the resulting prediction between 1890 and 2020. Set the title of the plot to be the error of the fit on the *training data*.}{1}{15}

### Polynomial Fit: Training Error

\slides{The next thing we'll do is consider a quadratic fit. We will compute the training error for the two fits.}

\codeassignment{In this question we extend the code above to a non-
linear basis (a quadratic function).

Start by creating a python-function called `quadratic`. It should compute the quadratic basis.
$$
\basisMatrix = \begin{bmatrix} \mathbf{1} & \dataVector & \dataVector^2\end{bmatrix}
$$
It should be called in the following form:

```Phi = quadratic(x)```

Use this to compute the quadratic fit for the model, again plotting the result titled by the error.}{2}{10}

### Polynomial Fits to Olympics Data

\setupcode{import pods
import mlai}

\code{max_basis = 8
basis = mlai.polynomial

data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']

data_limits = [1892, 2020]
num_data = x.shape[0]}

\setupcode{import teaching_plots as plot
%matplotlib inline}

\plotcode{plot.rmse_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1), 
              model=mlai.LM, basis=basis, data_limits=data_limits, 
              xlim=data_limits, objective_ylim=[0, 0.8],
			  diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_LM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1, 1, max_basis, 1))}

### Overfitting
\slides{* Increase number of basis functions we obtain a better 'fit' to the data.
* How will the model perform on previously unseen data?
* Let's consider predicting the future.}

\plotcode{plot.holdout_fit(x, y, param_name='num_basis', 
                 param_range=(1, max_basis+1), 
                 model=mlai.LM, basis=basis, data_limits=data_limits,
                 permute=False, objective_ylim=[0, 0.8], 
				 xlim=data_limits, prefix='olympic_val_extra', 
    		     diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_val_extra_LM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1, 1, max_basis, 1))}

### Extrapolation
\slides{* Here we are training beyond where the model has learnt.
* This is known as *extrapolation*.
* Extrapolation is predicting into the future here, but could be:
    * Predicting back to the unseen past (pre 1892)
    * Spatial prediction (e.g. Cholera rates outside Manchester given rates inside Manchester).}

### Interpolation
\slides{* Predicting the wining time for 1946 Olympics is *interpolation*.
* This is because we have times from 1936 and 1948.
* If we want a model for *interpolation* how can we test it?
* One trick is to sample the validation set from throughout the data set.}

\plotcode{plot.holdout_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1), 
                 model=mlai.LM, basis=basis, data_limits=data_limits, 
                 xlim=data_limits, prefix='olympic_val_inter', 
				 objective_ylim=[0.1, 0.6], permute=True,
   			     diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_val_inter_LM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1, 1, max_basis, 1))}

### Choice of Validation Set

\slides{* The choice of validation set should reflect how you will use the model in practice.
* For extrapolation into the future we tried validating with data from the future.
* For interpolation we chose validation set from data.
* For different validation sets we could get different results.}

### Hold Out Data

You have a conclusion as to which model fits best under the training error, but how do the two models perform in terms of validation? In this section we consider *hold out* validation. In hold out validation we remove a portion of the training data for *validating* the model on. The remaining data is used for fitting the model (training). Because this is a time series prediction, it makes sense for us to hold out data at the end of the time series. This means that we are validating on future predictions. We will hold out data from after 1980 and fit the model to the data before 1980.

\code{# select indices of data to 'hold out'
indices_hold_out = np.flatnonzero(x>1980)

# Create a training set
x_train = np.delete(x, indices_hold_out, axis=0)
y_train = np.delete(y, indices_hold_out, axis=0)

# Create a hold out set
x_valid = np.take(x, indices_hold_out, axis=0)
y_valid = np.take(y, indices_hold_out, axis=0)}

\codeassignment{For both the linear and quadratic models, fit the model to the data up until 1980 and then compute the error on the held out data (from 1980 onwards). Which model performs better on the validation data?}{3}{10}

### Richer Basis Set

Now we have an approach for deciding which model to
retain, we can consider the entire family of polynomial bases, with arbitrary
degrees.

\codeassignment{Now we are going to build a more sophisticated form of basis function, one that can accept arguments to its inputs (similar to those we used in [this lab](./week4.ipynb)). Here we will start with a polynomial basis.

```
def polynomial(x, degree, loc, scale):
    degrees =np.arange(degree+1)
    return ((x-loc)/scale)**degrees
```

The basis as we've defined it has three arguments as well as the input. The degree of the polynomial, the scale of the polynomial and the offset. These arguments need to be passed to the basis functions whenever they are called. Modify your code to pass these additional arguments to the python function for creating the basis. Do this for each of your functions `predict`, `fit` and `objective`. You will find `*args` (or `**kwargs`) useful.

Write code that tries to fit different models to the data with polynomial basis. Use a maximum degree for your basis from 0 to 17. For each polynomial store the *hold out validation error* and the *training error*. When you have finished the computation plot the hold out error for your models and the training error for your p. When computing your polynomial basis use `offset=1956.` and `scale=120.` to ensure that the data is mapped (roughly) to the -1, 1 range.

Which polynomial has the minimum training error? Which polynomial has the minimum validation error?}{4}{25}

### Leave One Out Validation

\slides{### Leave One Out Error
* Take training set and remove one point.
* Train on the remaining data.
* Compute the error on the point you removed (which wasn't in the training data).
* Do this for each point in the training set in turn.
* Average the resulting error. 
* This is the leave one out error.}

\plotcode{plot.loo_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1),  
             model=mlai.LM, basis=basis, data_limits=data_limits, 
             xlim=data_limits, objective_ylim=[0, 0.8], prefix='olympic_loo',
			  diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_loo{part:0>3}_LM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1, 1, max_basis, 1), 
							part=IntSlider(0, 0, x.shape[0], 1))}

\notes{Hold out validation uses a portion of the data to hold out and a portion of the data to train on. There is always a compromise between how much data to hold out and how much data to train on. The more data you hold out, the better the estimate of your performance at 'run-time' (when the model is used to make predictions in real applications). However, by holding out more data, you leave less data to train on, so you have a better validation, but a poorer quality model fit than you could have had if you'd used all the data for training. Leave one out cross validation leaves as much data in the training phase as possible: you only take *one point* out for your validation set. However, if you do this for hold-out validation, then the quality of your validation error is very poor because you are testing the model quality on one point only. In *cross validation* the approach is to improve this estimate by doing more than one model fit. In *leave one out cross validation* you fit $\numData$ different models, where $\numData$ is the number of your data. For each model fit you take out one data point, and train the model on the remaining $n-1$ data points. You validate the model on the data point you've held out, but you do this $\numData$ times, once for each different model. You then take the *average* of all the $\numData$ badly estimated hold out validation errors. The average of this estimate is a good estimate of performance of those models on the test data.}

\codeassignment{Write code that computes the *leave one out* validation error for the olympic data and the polynomial basis. Use the functions you have created above: `objective`, `fit`, `polynomial`. Compute the *leave-one-out* cross validation error for basis functions containing a maximum degree from 0 to 17.}{5}{20}

### $k$-fold Cross Validation
\notes{* Leave one out error can be very time consuming.
* Need to train your algorithm $\numData$ times.
* An alternative: $k$ fold cross validation.}

\plotcode{num_parts=5 # set k
plot.cv_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1),
               model=mlai.LM, basis=basis, data_limits=data_limits,
               xlim=data_limits, objective_ylim=[0.2,0.6], num_parts=num_parts,
			   diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_{num_parts}'.format(num_parts=num_parts) + 'cv{part:0>2}_LM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							part=IntSlider(0,0,5,1),
							num_basis=IntSlider(1, 1, max_basis, 1))}

Leave one out cross validation produces a very good estimate of the performance at test time, and is particularly useful if you don't have a lot of data. In these cases you need to make as much use of your data for model fitting as possible, and having a large hold out data set (to validate model performance) can have a significant effect on the size of the data set you have to fit your model, and correspondingly, the complexity of the model you can fit. However, leave one out cross validation involves fitting $\numData$ models, where $\numData$ is your number of training data. For the olympics example, this is only 27 model fits, but in practice many data sets consist thousands or millions of data points, and fitting many millions of models for estimating validation error isn't really practical. One option is to return to *hold out* validation, but another approach is to perform $k$-fold cross validation. In $k$-fold cross validation you split your data into $k$ parts. Then you use $k-1$ of those parts for training, and hold out one part for validation. Just like we did for the hold out validation above. In *cross* validation, however, you repeat this process. You swap the part of the data you just used for validation back in to the training set and select another part for validation. You then fit the model to the new training data and validate on the portion of data you've just extracted. Each split of training/validation data is called a *fold* and since you do this process $k$ times, the procedure is known as $k$-fold cross validation. The term *cross* refers to the fact that you cross over your validation portion back into the training data every time you perform a fold.

\codeassignment{Perform $k$-fold cross validation on the olympic data
with your polynomial basis. Use $k$ set to 5 (e.g. five fold cross validation).
Do the different forms of validation select different models? Does five fold
cross validation always select the same model?

*Note*: The data doesn't divide into 5 equal size partitions for the five fold
cross validation error. Don't worry about this too much. Two of the partitions
will have an extra data point. You might find `np.random.permutation?` useful.
}{6}{20}

### Bias Variance Decomposition

Expected test error for different variations of
the *training data* sampled from, $\Pr(\dataVector, \dataScalar)$
$$\mathbb{E}\left[ \left(\dataScalar - \mappingFunction^*(\dataVector)\right)^2 \right]$$
Decompose as
$$\mathbb{E}\left[ \left(\dataScalar - \mappingFunction(\dataVector)\right)^2 \right] = \text{bias}\left[\mappingFunction^*(\dataVector)\right]^2 + \text{variance}\left[\mappingFunction^*(\dataVector)\right] +\sigma^2$$

### Bias

* Given by
  $$\text{bias}\left[\mappingFunction^*(\dataVector)\right] =
\mathbb{E}\left[\mappingFunction^*(\dataVector)\right] * \mappingFunction(\dataVector)$$
* Error due to bias comes from a model that's too simple.

### Variance

* Given by
  $$\text{variance}\left[\mappingFunction^*(\dataVector)\right] = \mathbb{E}\left[\left(\mappingFunction^*(\dataVector) - \mathbb{E}\left[\mappingFunction^*(\dataVector)\right]\right)^2\right]$$
* Slight variations in the training set cause changes in the prediction. Error due to variance is error in the model due to an overly complex model.

### Reading

* Section 1.5 of @Rogers:book11


