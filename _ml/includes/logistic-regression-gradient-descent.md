\ifndef{logisticRegressionGradientDescent}
\define{logisticRegressionGradientDescent}

\editme

\subsection{Batch Gradient Descent}

\notes{We will need to define some initial random values for our vector and then minimize the objective by descending the gradient.}


\code{# Separate train and test
indices = np.random.permutation(X.shape[0])
num_train = np.ceil(X.shape[0]/2)r
train_indices = indices[:num_train]
test_indices = indices[num_train:]
X_train = X.iloc[train_indices]
y_train = y.iloc[train_indices]==True
X_test = X.iloc[test_indices]
y_test = y.iloc[test_indices]==True}


\setupcode{import numpy as np}
\code{# gradient descent algorithm
w = np.random.normal(size=(X.shape[1]+1, 1), scale = 0.001)
eta = 1e-9
iters = 10000
for i in range(iters):
    g, Phi = predict(w, X_train, linear)
    w -= eta*gradient(g, Phi, y_train) + 0.001*w
    if not i % 100:
        print("Iter", i, "Objective", objective(g, y_train))}

\notes{Let's look at the weights and how they relate to the inputs.}

\setupcode{import matplotlib.pyplot as plt}
\code{print(w)}

\notes{What does the magnitude of the weight vectors tell you about the different parameters and their influence on outcome? Are the weights of roughly the same size, if not, how might you fix this?}

\code{g_test, Phi_test = predict(w, X_test, linear)
np.sum(g_test[y_test]>0.5)}

\subsection{Stochastic Gradient Descent}

\exercise{Now construct a stochastic gradient descent algorithm and run it on the data. Is it faster or slower than batch gradient descent? What can you do to improve convergence speed?}

\endif
