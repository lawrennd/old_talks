\ifndef{logisticRegressionGradientDescent}
\define{logisticRegressionGradientDescent}

\editme

\subsection{Batch Gradient Descent}

\notes{We will need to define some initial random values for our vector and then minimize the objective by descending the gradient.}

\setupcode{import numpy as np}
\code{# gradient descent algorithm
w = np.random.normal(size=(X.shape[1]+1, 1), scale = 0.001)
eta = 1e-9
iters = 10000
for i in range(iters):
    g, Phi = predict(w, X, linear)
    w -= eta*gradient(g, Phi, y) + 0.001*w
    if not i % 100:
        print("Iter", i, "Objective", objective(g, y))}

\notes{Let's look at the weights and how they relate to the inputs.}

\setupcode{import matplotlib.pyplot as plt}
\code{print(w)}

\notes{What does the magnitude of the weight vectors tell you about the different parameters and their influence on outcome? Are the weights of roughly the same size, if not, how might you fix this?}


\subsection{Stochastic Gradient Descent}

\exercise{Now construct a stochastic gradient descent algorithm and run it on the data. Is it faster or slower than batch gradient descent? What can you do to improve convergence speed?}

\endif
