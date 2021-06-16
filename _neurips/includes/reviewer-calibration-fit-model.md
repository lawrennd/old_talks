\ifndef{reviewerCalibrationFitModel}
\define{reviewerCalibrationFitModel}

\editme

\subsection{Fitting the Model}

\slides{* Sum of Gaussian random variables is Gaussian.
* Model is a *joint Gaussian* over the data.
* Fit by maximum likelihood three parameters, $\alpha_f$, $\alpha_b$, $\sigma_2$}

\setupcode{import cmtutils as cu
import os
import pandas as pd
import numpy as np
import GPy
from scipy.sparse.csgraph import connected_components
from scipy.linalg import solve_triangular }


\code{date = '2014-09-06'}

\notes{\subsection{Loading in the Data}}

\code{filename = date + '_reviews.xls'
reviews = cu.CMT_Reviews_read(filename=filename)
papers = list(sorted(set(reviews.reviews.index), key=int))
reviews.reviews = reviews.reviews.loc[papers]}

\notes{The maximum likelihood solution for $\mu$ is simply the mean quality of
the papers, this is easily computed.}

\code{mu = reviews.reviews.Quality.mean()
print("Mean value, mu = ", mu)}

\notes{\subsection{Data Preparation}}

\notes{We take the reviews, which are indexed by the paper number, and create a
new data frame, that indexes by paper id and email combined. From these
reviews we tokenize the `PaperID` and the `Email` to extract two
matrices that can be used in creation of covariance matrices. We also
create a target vector which is the mean centred vector of scores.}

\code{r = reviews.reviews.reset_index()
r.rename(columns={'ID':'PaperID'}, inplace=True)
r.index = r.PaperID + '_' + r.Email
X1 = pd.get_dummies(r.PaperID)
X1 = X1[sorted(X1.columns, key=int)]
X2 = pd.get_dummies(r.Email)
X2 = X2[sorted(X2.columns, key=str.lower)]
y = reviews.reviews.Quality - mu}

\notes{\subsubsection{Constructing the Model in GPy}

Having reduced the model to two parameters, I was hopeful I could set
parameters broadly by hand. My initial expectation was that `alpha_b`
and `sigma2` would both be less than 1, but some playing with parameters
showed this wasn't the case. Rather than waste further time, I decided
to use our [`GPy` Software](https://github.com/SheffieldML/GPy) (see
below) to find a maximum likelihood solution for the parameters.

Model construction firstly involves constructing covariance functions
for the model and concatanating `X1` and `X2` to a new input matrix `X`.}

\code{X = X1.join(X2)
kern1 = GPy.kern.Linear(input_dim=len(X1.columns), active_dims=np.arange(len(X1.columns)))
kern1.name = 'K_f'
kern2 = GPy.kern.Linear(input_dim=len(X2.columns), active_dims=np.arange(len(X1.columns), len(X.columns)))
kern2.name = 'K_b'}

\notes{Next, the covariance function is used to create a Gaussian process
regression model with `X` as input and `y` as target. The covariance
function is given by $\mathbf{K}_f + \mathbf{K}_b$.}

\code{model = GPy.models.GPRegression(X, y.to_numpy()[:, np.newaxis], kern1+kern2)
model.optimize()}

\notes{Now we can check the parameters of the result.}

\code{print(model)
print(model.log_likelihood())}

\notes{
```
    Name : GP regression
    Objective : 10071.679092815619
    Number of Parameters : 3
    Number of Optimization Parameters : 3
    Updates : True
    Parameters:
      GP_regression.           |               value  |  constraints  |  priors
      sum.K_f.variances        |  1.2782303448777643  |      +ve      |        
      sum.K_b.variances        |  0.2400098787580176  |      +ve      |        
      Gaussian_noise.variance  |  1.2683656892796749  |      +ve      |        
    -10071.679092815619
```}

\newslide{NeurIPS 2014 Parameters}

\slides{
$$ \alpha_f = 1.28$$
$$ \alpha_b = 0.24$$
$$ \sigma^2 = 1.27$$}

\notes{\subsubsection{Construct the Model Without GPy}

The answer from the GPy solution is introduced here, alongside the code
where the covariance matrices are explicitly created (above they are
created using GPy's high level code for kernel matrices, which may be
less clear on the details).}

\code{# set parameter values to ML solutions given by GPy.
alpha_f = model.sum.K_f.variances
alpha_b = model.sum.K_b.variances/alpha_f
sigma2 = model.Gaussian_noise.variance/alpha_f}

\notes{Now we create the covariance functions based on the tokenized paper IDs
and emails.}

\code{K_f = np.dot(X1, X1.T)
K_b = alpha_b*np.dot(X2, X2.T)
K = K_f + K_b + sigma2*np.eye(X2.shape[0])
Kinv, L, Li, logdet = GPy.util.linalg.pdinv(K) # since we have GPy loaded in use their positive definite inverse.
y = reviews.reviews.Quality - mu
alpha = np.dot(Kinv, y)
yTKinvy = np.dot(y, alpha)
alpha_f = yTKinvy/len(y)}

\notes{Since we have removed the data mean, the log likelihood we are
interested in is the likelihood of a multivariate Gaussian with
covariance $\mathbf{K}$ and mean zero. This is computed below.}

\code{ll = 0.5*len(y)*np.log(2*np.pi*alpha_f) + 0.5*logdet + 0.5*yTKinvy/alpha_f 
print("negative log likelihood: ", ll)}

\endif
