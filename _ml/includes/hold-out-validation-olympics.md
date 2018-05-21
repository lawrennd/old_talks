### Hold Out Validation

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
