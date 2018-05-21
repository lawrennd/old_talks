
\notes{In this lab we will explore techniques for model selection that make use of validation data. Data that isn't seen by the model in the learning (or fitting) phase, but is used to *validate* our choice of model from amoungst the different designs we have selected.

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

\include{_ml/includes/validation-olympic-fit.md}
\include{_ml/includes/hold-out-validation-olympics.md}
\include{_ml/includes/loo-validation-olympics.md}
\include{_ml/includes/k-fold-validation-olympics.md}
