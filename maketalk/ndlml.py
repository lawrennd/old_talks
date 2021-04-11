# Python code for ML lectures.

# import the time model to allow python to pause.
import time
import os
import numpy as np

import matplotlib.pyplot as plt
from IPython.display import display, clear_output, HTML

from numpy import sqrt, sin, cos, tanh, arcsin, arccos, sinc, log, exp
from numpy import sum, max, min, abs, ceil, dot
from numpy import eye, diag, zeros, ones, linspace
from numpy import pi, var, asarray, hstack, arange, clip, frombuffer
from numpy.random import randint, rand, seed, uniform, poisson, normal

from numpy.linalg import qr, norm, det, inv
from scipy.linalg import solve_triangular, cholesky


def filename_join(filename, directory=None):
    "Join a filename to a directory and create directory if it's not there"
    if directory is not None:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        return os.path.join(directory, filename)
    return filename

def write_animation(anim, filename, directory=None, **kwargs):
    "Write an animation to a file."
    savename = filename_join(filename, directory)
    anim.save(savename, **kwargs)

def write_animation_html(anim, filename, directory=None):
    """Save an animation to file."""
    savename = filename_join(filename, directory)
    f = open(savename, 'w')
    f.write(anim.to_jshtml())
    f.close()

def write_figure(filename, figure=None, directory=None, **kwargs):
    """Write figure in correct formating"""
    savename = filename_join(filename, directory)
    if 'transparent' not in kwargs:
        kwargs['transparent'] = True
    if figure is None:
        plt.savefig(savename, **kwargs)
    else:
        figure.savefig(savename, **kwargs)
    
##########          Week 2          ##########
def init_perceptron(x_plus, x_minus, seed=1000001):
    seed(seed=seed)
    # flip a coin (i.e. generate a random number and check if it is greater than 0.5)
    choose_plus = rand(1)>0.5
    if choose_plus:
        # generate a random point from the positives
        index = randint(0, x_plus.shape[0])
        x_select = x_plus[index, :]
        w = x_plus[index, :] # set the normal vector to that point.
        b = 1
    else:
        # generate a random point from the negatives
        index = randint(0, x_minus.shape[0])
        x_select = x_minus[index, :]
        w = -x_minus[index, :] # set the normal vector to minus that point.
        b = -1
    return w, b, x_select


def update_perceptron(w, b, x_plus, x_minus, learn_rate):
    "Update the perceptron."
    # select a point at random from the data
    choose_plus = rand(1)>0.5
    updated=False
    if choose_plus:
        # choose a point from the positive data
        index = randint(x_plus.shape[0])
        x_select = x_plus[index, :]
        if dot(w, x_select)+b <= 0.:
            # point is currently incorrectly classified
            w += learn_rate*x_select
            b += learn_rate
            updated=True
    else:
        # choose a point from the negative data
        index = randint(x_minus.shape[0])
        x_select = x_minus[index, :]
        if dot(w, x_select)+b > 0.:
            # point is currently incorrectly classified
            w -= learn_rate*x_select
            b -= learn_rate
            updated=True
    return w, b, x_select, updated

##########           Weeks 4 and 5           ##########
class Model(object):
    def __init__(self):
        pass
    
    def objective(self):
        raise NotImplementedError

    def fit(self):
        raise NotImplementedError

class ProbModel(Model):
    def __init__(self):
        Model.__init__(self)

    def objective(self):
        return -self.log_likelihood()

    def log_likelihood(self):
        raise NotImplementedError

class MapModel(Model):
    "Model that provides a mapping from X to y."
    def __init__(self, X, y):
        Model.__init__(self)
        self.X = X
        self.y = y
        self.num_data = y.shape[0]

    def update_sum_squares(self):
        raise NotImplementedError
    
    def rmse(self):
        self.update_sum_squares()
        return sqrt(self.sum_squares/self.num_data)

    def predict(self, X):
        raise NotImplementedError

    
class ProbMapModel(ProbModel, MapModel):
    """Probabilistic model that provides a mapping from X to y."""
    def __init__(self, X, y):
        ProbModel.__init__(self)
        MapModel.__init__(self, X, y)

    
class LM(ProbMapModel):
    """Linear model class."""

    def __init__(self, X, y, basis):
        """Initialise a linear model object

        :param X: input values
        :type X: numpy.ndarray
        :param y: target values
        :type y: numpy.ndarray
        :param basis: basis function 
        :param type: function"""

        ProbModel.__init__(self)
        self.y = y
        self.num_data = y.shape[0]
        self.X = X
        self.sigma2 = 1.
        self.basis = basis
        self.Phi = self.basis.Phi(X)
        self.name = 'LM_'+self.basis.function.__name__
        self.objective_name = 'Sum of Square Training Error'

    def set_param(self, name, val, update_fit=True):
        """Set a parameter to a given value"""
        if name in self.__dict__:
            if self.__dict__[name] == val:
                update_fit=False
            else:
                self.__dict__[name] = val
        elif name in self.basis.__dict__:
            if self.basis.__dict__[name] == val:
                update_fit=False
            else:
                self.basis.__dict__[name] = val
                self.Phi = self.basis.Phi(self.X)            
        else:
            raise ValueError("Unknown parameter '{}' being set.".format(name))
        if update_fit:
            self.fit()

    def update_QR(self):
        "Perform the QR decomposition on the basis matrix."
        self.Q, self.R = qr(self.Phi)

    def fit(self):
        """Minimize the objective function with respect to the parameters"""
        self.update_QR()
        self.w_star = solve_triangular(self.R, self.Q.T@self.y)
        self.update_sum_squares()
        self.sigma2=self.sum_squares/self.num_data

    def predict(self, X):
        """Return the result of the prediction function."""
        return self.basis.Phi(X)@self.w_star, None
        
    def update_f(self):
        """Update values at the prediction points."""
        self.f = self.Phi@self.w_star
        
    def update_sum_squares(self):
        """Compute the sum of squares error."""
        self.update_f()
        self.sum_squares = ((self.y-self.f)**2).sum()
        
    def objective(self):
        """Compute the objective function."""
        self.update_sum_squares()
        return self.sum_squares

    def log_likelihood(self):
        """Compute the log likelihood."""
        self.update_sum_squares()
        return -self.num_data/2.*log(pi*2.)-self.num_data/2.*log(self.sigma2)-self.sum_squares/(2.*self.sigma2)
    

class Basis():
    """Basis function
    :param function: basis function
    :type function: function
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * """
    def __init__(self, function, number, **kwargs):
        """"""
        self.arguments=kwargs
        self.number=number
        self.function=function

    def Phi(self, X):
        return self.function(X, num_basis=self.number, **self.arguments)

def linear(x, **kwargs):
    "Defines the linear basis."
    return hstack([ones((x.shape[0], 1)), asarray(x, dtype=float)])

def polynomial(x, num_basis=4, data_limits=[-1., 1.]):
    "Polynomial basis"
    centre = data_limits[0]/2. + data_limits[1]/2.
    span = data_limits[1] - data_limits[0]
    z = asarray(x, dtype=float) - centre
    z = 2*z/span
    Phi = zeros((x.shape[0], num_basis))
    for i in range(num_basis):
        Phi[:, i:i+1] = z**i
    return Phi

def radial(x, num_basis=4, data_limits=[-1., 1.], width=None):
    """Radial basis constructed using exponentiated quadratic form."""
    if num_basis>1:
        centres=linspace(data_limits[0], data_limits[1], num_basis)
        if width is None:
            width = (centres[1]-centres[0])/2.
    else:
        centres = asarray([data_limits[0]/2. + data_limits[1]/2.])
        if width is None:
            width = (data_limits[1]-data_limits[0])/2.
    
    Phi = zeros((x.shape[0], num_basis))
    for i in range(num_basis):
        Phi[:, i:i+1] = exp(-0.5*((asarray(x, dtype=float)-centres[i])/width)**2)
    return Phi


def fourier(x, num_basis=4, data_limits=[-1., 1.], frequency_range=None):
    """Fourier basis"""
    tau = 2*pi
    span = float(data_limits[1]-data_limits[0])
    Phi = ones((x.shape[0], num_basis))
    for i in range(1, num_basis):
        count = float((i+1)//2)
        if frequency_range is None:
            frequency = count/span
        else:
            frequency = frequency_range[i]
        if i % 2:
            Phi[:, i:i+1] = sin(tau*frequency*asarray(x, dtype=float))
        else:
            Phi[:, i:i+1] = cos(tau*frequency*asarray(x, dtype=float))
    return Phi

def relu(x, num_basis=4, data_limits=[-1., 1.], gain=None):
    """Rectified linear units basis"""
    if num_basis>2:
        centres=linspace(data_limits[0], data_limits[1], num_basis-1)
    elif num_basis==2:
        centres = asarray([data_limits[0]/2. + data_limits[1]/2.])
    else:
        centres = []
    if gain is None:
        gain = ones(num_basis-1)
    Phi = zeros((x.shape[0], num_basis))
    # Create the bias
    Phi[:, 0] = 1.0
    for i in range(1, num_basis):
        Phi[:, i:i+1] = (gain[i-1]*asarray(x, dtype=float)>centres[i-1])*(asarray(x, dtype=float)-centres[i-1])
    return Phi

def tanh(x, num_basis=4, data_limits=[-1., 1.], gain=None):
    """Hyperbolic tangents"""
    if num_basis>2:
        centres=linspace(data_limits[0], data_limits[1], num_basis-1)
        width = (centres[1]-centres[0])/2.
    elif num_basis==2:
        centres = asarray([data_limits[0]/2. + data_limits[1]/2.])
        width = (data_limits[1]-data_limits[0])/2.
    else:
        centres = []
        width = None
    if gain is None and width is not None:
        gain = ones(num_basis-1)/width
    Phi = zeros((x.shape[0], num_basis))
    # Create the bias
    Phi[:, 0] = 1.0
    for i in range(1, num_basis):
        Phi[:, i:i+1] = tanh(gain[i-1]*(asarray(x, dtype=float)-centres[i-1]))
    return Phi

class Noise(ProbModel):
    """Noise model"""
    def __init__(self):
        ProbModel.__init__(self)

    def _repr_html_(self):
        raise NotImplementedError

    
class Gaussian(Noise):
    """Gaussian Noise Model."""
    def __init__(self, offset=0., scale=1.):
        Noise.__init__(self)
        self.scale = scale
        self.offset = offset
        self.variance = scale*scale

    def log_likelihood(self, mu, varsigma, y):
        """Log likelihood of the data under a Gaussian noise model.
        :param mu: input mean locations for the log likelihood.
        :type mu: np.array
        :param varsigma: input variance locations for the log likelihood.
        :type varsigma: np.array
        :param y: target locations for the log likelihood.
        :type y: np.array"""

        n = y.shape[0]
        d = y.shape[1]
        varsigma = varsigma + self.scale*self.scale
        for i in range(d):
            mu[:, i] += self.offset[i]
        arg = (y - mu);
        arg = arg*arg/varsigma

        return - 0.5*(log(varsigma).sum() + arg.sum() + n*d*log(2*pi))


    def grad_vals(self, mu, varsigma, y):
        """Gradient of noise log Z with respect to input mean and variance.
        :param mu: mean input locations with respect to which gradients are being computed.
        :type mu: np.array
        :param varsigma : variance input locations with respect to which gradients are being computed.
        :type varsigma: np.array
        :param y: noise model output observed values associated with the given points.
        :type y: np.array
        :rtype: tuple containing the gradient of log Z with respect to the input mean and the gradient of log Z with respect to the input variance."""

        d = y.shape[1]
        nu = 1/(self.scale*self.scale+varsigma)
        dlnZ_dmu = zeros(nu.shape)
        for i in range(d):
            dlnZ_dmu[:, i] = y[:, i] - mu[:, i] - self.offset[i]
        dlnZ_dmu = dlnZ_dmu*nu
        dlnZ_dvs = 0.5*(dlnZ_dmu*dlnZ_dmu - nu)
        return dlnZ_dmu, dlnZ_dvs

class SimpleNeuralNetwork(Model):
    """A simple one layer neural network
    :param nodes: number of hidden nodes
    """
    def __init__(self, nodes):
        self.nodes = nodes
        self.w2 = normal(size=self.nodes)/self.nodes
        self.b2 = normal(size=1)
        self.w1 = normal(size=self.nodes)
        self.b1 = normal(size=self.nodes)
        

    def predict(self, x):
        "Compute output given current basis functions."
        vxmb = self.w1*x + self.b1
        phi = vxmb*(vxmb>0)
        return sum(self.w2*phi) + self.b2

class SimpleDropoutNeuralNetwork(SimpleNeuralNetwork):
    """Simple neural network with dropout
    :param nodes: number of hidden nodes
    :param drop_p: drop out probability
    """
    def __init__(self, nodes, drop_p=0.5):
        self.drop_p = drop_p
        nn.__init__(self, nodes=nodes)
        # renormalize the network weights
        self.w2 /= self.drop_p 
        
    def do_samp(self):
        "Sample the set of basis functions to use" 
        gen = rand(self.nodes)
        self.use = gen > self.drop_p
        
    def predict(self, x):
        "Compute output given current basis functions used."
        vxmb = self.w1[self.use]*x + self.b1[self.use]
        phi = vxmb*(vxmb>0)
        return sum(self.w2[self.use]*phi) + self.b2

class NonparametricDropoutNeuralNetwork(SimpleDropoutNeuralNetwork):
    """A non parametric dropout neural network
    :param alpha: alpha parameter of the IBP controlling dropout.
    :param beta: beta parameter of the two parameter IBP controlling dropout."""
    def __init__(self, alpha=10, beta=1, n=1000):
        self.update_num = 0
        self.alpha = alpha
        self.beta = beta
        self.gamma = 0.5772156649
        tot = log(n) + self.gamma + 0.5/n * (1./12.)/(n*n)
        self.exp_features = alpha*beta*tot
        self.maxk = max((10000,int(self.exp_features + ceil(4*sqrt(self.exp_features)))))
        donn.__init__(self, nodes=self.maxk, drop_p=self.alpha/self.maxk)
        self.maxval = 0
        self.w2 *= self.maxk/self.alpha
        self.count = zeros(self.maxk)
    
    
        
    def do_samp(self):
        "Sample the next set of basis functions to be used"
        
        new=poisson(self.alpha*self.beta/(self.beta + self.update_num))
        use_prob = self.count[:self.maxval]/(self.update_num+self.beta)
        gen = rand(1, self.maxval)
        self.use = zeros(self.maxk, dtype=bool)
        self.use[:self.maxval] = gen < use_prob
        self.use[self.maxval:self.maxval+new] = True
        self.maxval+=new
        self.update_num+=1
        self.count[:self.maxval] += self.use[:self.maxval]
        

    
class BLM(LM):
    """Bayesian Linear model
    :param X: input values
    :type X: numpy.ndarray
    :param y: target values
    :type y: numpy.ndarray
    :param alpha: Scale of prior on parameters
    :type alpha: float
    :param sigma2: Noise variance
    :type sigma2: float
    :param basis: basis function 
    :param type: function"""

    def __init__(self, X, y, alpha, sigma2, basis):
        "Initialise"
        ProbMapModel.__init__(self, X, y)
        self.sigma2 = sigma2
        self.alpha = alpha
        self.basis = basis
        self.Phi = self.basis.Phi(X)
        self.name = 'BLM_'+self.basis.function.__name__
        self.objective_name = 'Negative Marginal Likelihood'

    def set_param(self, name, val, update_fit=True):
        """Set a parameter to a given value"""
        if name in self.__dict__:
            if self.__dict__[name] == val:
                update_fit=False
            else:
                self.__dict__[name] = val
        elif name in self.basis.__dict__:
            if self.basis.__dict__[name] == val:
                update_fit=False
            else:
                self.basis.__dict__[name] = val
                self.Phi = self.basis.Phi(self.X)            
        else:
            raise ValueError("Unknown parameter being set.")
        if update_fit:
            self.fit()
        
    def update_QR(self):
        "Perform the QR decomposition on the basis matrix."
        self.Q, self.R = qr(vstack([self.Phi, sqrt(self.sigma2/self.alpha)*eye(self.basis.number)]))

    def fit(self):
        """Minimize the objective function with respect to the parameters"""
        self.update_QR()
        self.QTy = self.Q[:self.y.shape[0], :].T@self.y
        self.mu_w = solve_triangular(self.R, self.QTy)
        self.RTinv = solve_triangular(self.R, eye(self.R.shape[0]), trans='T')
        self.C_w = self.RTinv@self.RTinv.T
        self.update_sum_squares()

    def predict(self, X, full_cov=False):
        """Return the result of the prediction function."""
        Phi = self.basis.Phi(X)
        # A= R^-T Phi.T
        A = solve_triangular(self.R, Phi.T, trans='T')
        mu = A.T@self.QTy
        if full_cov:
            return mu, self.sigma2*A.T@A
        else:
            return mu, self.sigma2*(A*A).sum(0)[:, None]
        
    def update_f(self):
        """Update values at the prediction points."""
        self.f_bar = self.Phi@self.mu_w
        self.f_cov = (self.Q[:self.y.shape[0], :]*self.Q[:self.y.shape[0], :]).sum(1)

    def update_sum_squares(self):
        """Compute the sum of squares error."""
        self.update_f()
        self.sum_squares = ((self.y-self.f_bar)**2).sum()
    
    def objective(self):
        """Compute the objective function."""
        return - self.log_likelihood()

    def update_nll(self):
        """Precompute terms needed for the log likelihood."""
        self.log_det = self.num_data*log(self.sigma2*pi*2.)-2*log(abs(det(self.Q[self.y.shape[0]:, :])))
        self.quadratic = (self.y*self.y).sum()/self.sigma2 - (self.QTy*self.QTy).sum()/self.sigma2
        
    def nll_split(self):
        "Compute the determinant and quadratic term of the negative log likelihood"
        self.update_nll()
        return self.log_det, self.quadratic
    
    def log_likelihood(self):
        """Compute the log likelihood."""
        self.update_nll()
        return -self.log_det - self.quadratic

##########          Week 8            ##########

    

# Code for loading pgm from http://stackoverflow.com/questions/7368739/numpy-and-16-bit-pgm
def load_pgm(filename, directory=None, byteorder='>'):
    """Return image data from a raw PGM file as numpy array.

    Format specification: http://netpbm.sourceforge.net/doc/pgm.html

    """
    import re
    savename = filename_join(filename, directory)
    with open(savename, 'rb') as f:
        buffer = f.read()
    try:
        header, width, height, maxval = re.search(
            b"(^P5\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    except AttributeError:
        raise ValueError("Not a raw PGM file: '%s'" % filename)
    return frombuffer(buffer,
                            dtype='u1' if int(maxval) < 256 else byteorder+'u2',
                            count=int(width)*int(height),
                            offset=len(header)
                            ).reshape((int(height), int(width)))

##########          Week 10          ##########

class LR(ProbMapModel):
    """Logistic regression
    :param X: input values
    :type X: numpy.ndarray
    :param y: target values
    :type y: numpy.ndarray
    :param alpha: Scale of prior on parameters
    :type alpha: float
    :param sigma2: Noise variance
    :type sigma2: float
    :param basis: basis function 
    :param type: function"""

    def __init__(self, X, y, basis):
        ProbMapModel.__init__(self, X, y)
        self.basis = basis
        self.Phi = self.basis.Phi(X)
        self.w_star = zeros(self.basis.number)
        
    def predict(self, X):
        "Generates the prediction function and the basis matrix."
        Phi = self.basis.Phi(X)
        f = Phi@self.w_star
        return 1./(1+exp(-f)), Phi

    def gradient(self):
        "Generates the gradient of the parameter vector."
        self.update_g()
        dw = -(self.Phi[self.y.values, :]*(1-self.g[self.y.values, :])).sum(0)
        dw += (Phi[~self.y.values, :]*self.g[~self.y.values, :]).sum(0)
        return dw[:, None]

    def compute_g(self, f):
        "Compute the transformation and its logarithms."
        eps = 1e-16
        g = 1./(1+exp(f))
        log_g = zeros((f.shape))
        log_gminus = zeros((f.shape))
        
        # compute log_g for values out of bound
        bound = log(eps)
        ind = f<-bound
        
        log_g[ind] = -f[ind]
        log_gminus[ind] = eps
        ind = f>bound
        log_g[ind] = eps
        log_gminus[ind] = f[ind]
        ind = (f>=-bound & f<=bound)
        log_g[ind] = log(self.g[ind])
        log_gminus[ind] = log(1-self.g[ind])
        return g, log_g, log_gminus
        
    def update_g(self):
        "Computes the prediction function on training data."
        self.f = self.Phi@self.w_star
        self.g, self.log_g, self.log_gminus = self.compute_g(self.f)
        
    def objective(self):
        "Computes the objective function."
        self.update_g()
        return self.log_g[self.y.values, :].sum() + log_gminus[~self.y.values, :].sum()
    
##########          Week 12          ##########
class GP(ProbMapModel):
    """Gaussian Process
    :param X: input values
    :type X: numpy.ndarray
    :param y: target values
    :type y: numpy.ndarray
    :param sigma2: Noise variance
    :type sigma2: float
    :param kernel: covariance function 
    :param type: kernel"""
    def __init__(self, X, y, sigma2, kernel):
        self.sigma2 = sigma2
        self.kernel = kernel
        self.K = kernel.K(X, X)
        self.X = X
        self.y = y
        self.update_inverse()
        self.name = 'GP_'+kernel.function.__name__
        self.objective_name = 'Negative Marginal Likelihood'

    def update_inverse(self):
        # Pre-compute the inverse covariance and some quantities of interest
        ## NOTE: This is *not* the correct *numerical* way to compute this! It is for ease of mapping onto the maths.
        self.Kinv = inv(self.K+self.sigma2*eye(self.K.shape[0]))
        # the log determinant of the covariance matrix.
        self.logdetK = det(self.K+self.sigma2*eye(self.K.shape[0]))
        # The matrix inner product of the inverse covariance
        self.Kinvy = self.Kinv@self.y
        self.yKinvy = (self.y*self.Kinvy).sum()

    def fit(self):
        pass

    def update_nll(self):
        "Precompute the log determinant and quadratic term from the negative log likelihod"
        self.log_det = 0.5*(self.K.shape[0]*log(2*pi) + self.logdetK)
        self.quadratic =  0.5*self.yKinvy
                            
    def nll_split(self):
        "Return the two components of the negative log likelihood"
        return self.log_det, self.quadratic
    
    def log_likelihood(self):
        "Use the pre-computes to return the likelihood"
        self.update_nll()
        return -self.log_det - self.quadratic
    
    def objective(self):
        "Use the pre-computes to return the objective function"
        return -self.log_likelihood()

    def predict(self, X_test, full_cov=False):
        "Give a mean and a variance of the prediction."
        K_star = self.kernel.K(self.X, X_test)
        A = self.Kinv@K_star
        mu_f = A.T@self.y
        k_starstar = self.kernel.diag(X_test)
        c_f = k_starstar - (A*K_star).sum(0)[:, None]
        return mu_f, c_f
        
def posterior_f(self, X_test):
    """Compute the posterior distribution for f in the GP"""
    K_star = self.kernel.K(self.X, X_test)
    A = self.Kinv@K_star
    mu_f = A.T@self.y
    K_starstar = self.kernel.K(X_test, X_test)
    C_f = K_starstar - A.T@K_star
    return mu_f, C_f

def update_inverse(self):
    """Update the inverse covariance in a numerically more stable manner"""
    # Perform Cholesky decomposition on matrix
    self.R = cholesky(self.K + self.sigma2*self.K.shape[0])
    # compute the log determinant from Cholesky decomposition
    self.logdetK = 2*log(diag(self.R)).sum()
    # compute y^\top K^{-1}y from Cholesky factor
    self.Rinvy = solve_triangular(self.R, self.y)
    self.yKinvy = (self.Rinvy**2).sum()
    
    # compute the inverse of the upper triangular Cholesky factor
    self.Rinv = solve_triangular(self.R, eye(self.K.shape[0]))
    self.Kinv = self.Rinv@self.Rinv.T


class Kernel():
    """Covariance function
    :param function: covariance function
    :type function: function
    :param name: name of covariance function
    :type name: string
    :param shortname: abbreviated name of covariance function
    :type shortname: string
    :param formula: latex formula of covariance function
    :type formula: string
    :param function: covariance function
    :type function: function
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * """

    def __init__(self, function, name=None, shortname=None, formula=None, **kwargs):        
        self.function=function
        self.formula = formula
        self.name = name
        self.shortname = shortname
        self.parameters=kwargs
        
    def K(self, X, X2=None):
        """Compute the full covariance function given a kernel function for two data points."""
        if X2 is None:
            X2 = X
        K = zeros((X.shape[0], X2.shape[0]))
        for i in arange(X.shape[0]):
            for j in arange(X2.shape[0]):
                K[i, j] = self.function(X[i, :], X2[j, :], **self.parameters)

        return K

    def diag(self, X):
        """Compute the diagonal of the covariance function"""
        diagK = zeros((X.shape[0], 1))
        for i in range(X.shape[0]):            
            diagK[i] = self.function(X[i, :], X[i, :], **self.parameters)
        return diagK

    def _repr_html_(self):
        raise NotImplementedError

    
def exponentiated_quadratic(x, x_prime, variance=1., lengthscale=1.):
    """Exponentiated quadratic covariance function."""
    r = norm(x-x_prime, 2)
    return variance*exp((-0.5*r*r)/lengthscale**2)        

def eq_cov(x, x_prime, variance=1., lengthscale=1.):
    """Exponentiated quadratic covariance function."""
    diffx = x - x_prime
    return variance*exp(-0.5*dot(diffx, diffx)/lengthscale**2)

def ou_cov(x, x_prime, variance=1., lengthscale=1.):
    """Exponential covariance function."""
    diffx = x - x_prime
    return variance*exp(-sqrt(dot(diffx, diffx))/lengthscale)

def matern32_cov(x, x_prime, variance=1., lengthscale=1.):
    """Matern 3/2 covariance function."""
    diffx = x - x_prime
    r_norm = sqrt(dot(diffx, diffx))/lengthscale
    sqrt3r_norm = r_norm*sqrt(3)
    return variance*(1+sqrt3r_norm)*exp(-sqrt3r_norm)

def matern52_cov(x, x_prime, variance=1., lengthscale=1.):
    """Matern 5/2 covariance function."""
    diffx = x - x_prime
    r_norm = sqrt(dot(diffx, diffx))/lengthscale
    sqrt5r_norm = r_norm*sqrt(5)
    return variance*(1+sqrt5r_norm+sqrt5r_norm*sqrt5r_norm/3)*exp(-sqrt5r_norm)

def mlp_cov(x, x_prime, variance=1., w=1., b=5., alpha=1.):
    """Covariance function for a MLP based neural network."""
    inner = dot(x, x_prime)*w + b
    norm = sqrt(dot(x, x)*w + b + alpha)*sqrt(dot(x_prime, x_prime)*w + b+alpha)
    arg = clip(inner/norm, -1, 1) # clip as numerically can be > 1
    theta = arccos(arg)
    return variance*0.5*(1. - theta/pi)      

def icm_cov(x, x_prime, B, subkernel, **kwargs):
    """Intrinsic coregionalization model. First index is outputs considered for covariance function."""
    i = x[0]
    i_prime = x_prime[0]
    return B[i, i_prime]*subkernel(x[1:], x_prime[1:], **kwargs)

def slfm_cov(x, x_prime, W, subkernel, **kwargs):
    """Semi-parametric latent factor model covariance function. First index is the output of the covariance function."""
    W = asarray(W)
    B = W@W.T
    return icm_cov(x, x_prime, B, subkernel, **kwargs)

def add_cov(x, x_prime, kernargs):
    """Additive covariance function."""
    k = 0.
    for kernel, kwargs in kernargs:
        k+=kernel(x, x_prime, **kwargs)
    return k

def prod_kern(x, x_prime, kernargs):
    """Product covariance function."""
    k = 1.
    for kernel, kwargs in kernargs:
        k*=kernel(x, x_prime, **kwargs)
    return k

def relu_cov(x, x_prime, variance=1., scale=1., w=1., b=5., alpha=0.):
    """Covariance function for a ReLU based neural network.
    :param x: first input
    :param x_prime: second input
    :param scale: overall scale of the covariance
    :param w: the overall scale of the weights on the input.
    :param b: the overall scale of the bias on the input
    :param alpha: the smoothness of the relu activation"""
    def h(costheta, inner, s, a):
        "Helper function"
        cos2th = costheta*costheta
        return (1-(2*s*s-1)*cos2th)/sqrt(a/inner + 1 - s*s*cos2th)*s

    inner = dot(x, x_prime)*w + b
    inner_1 = dot(x, x)*w + b
    inner_2 = dot(x_prime, x_prime)*w + b
    norm_1 = sqrt(inner_1 + alpha)
    norm_2 = sqrt(inner_2 + alpha)
    norm = norm_1*norm_2
    s = sqrt(inner_1)/norm_1
    s_prime = sqrt(inner_2)/norm_2
    arg = clip(inner/norm, -1, 1) # clip as numerically can be > 1
    arg2 = clip(inner/sqrt(inner_1*inner_2), -1, 1) # clip as numerically can be > 1
    theta = arccos(arg)
    return variance*0.5*((1. - theta/pi)*inner + h(arg2, inner_2, s, alpha)/pi + h(arg2, inner_1, s_prime, alpha)/pi) 


def polynomial_cov(x, x_prime, variance=1., degree=2., w=1., b=1.):
    """Polynomial covariance function."""
    return variance*(dot(x, x_prime)*w + b)**degree

def linear_cov(x, x_prime, variance=1.):
    """Linear covariance function."""
    return variance*dot(x, x_prime)

def bias_cov(x, x_prime, variance=1.):
    """Bias covariance function."""
    return variance

def mlp_cov(x, x_prime, variance=1., w=1., b=1.):
    """MLP covariance function."""
    return variance*arcsin((w*dot(x, x_prime) + b)/sqrt((dot(x, x)*w +b + 1)*(dot(x_prime, x_prime)*w + b + 1)))

def sinc_cov(x, x_prime, variance=1., w=1.):
    """Sinc covariance function."""
    r = norm(x-x_prime, 2)
    return variance*sinc(pi*w*r)

def ou_cov(x, x_prime, variance=1., lengthscale=1.):
    """Ornstein Uhlenbeck covariance function."""
    r = norm(x-x_prime, 2)
    return variance*exp(-r/lengthscale)        

def brownian_cov(t, t_prime, variance=1.):
    """Brownian motion covariance function."""
    if t>=0 and t_prime>=0:
        return variance*min([t, t_prime])
    else:
        raise ValueError("For Brownian motion covariance only positive times are valid.")

def periodic_cov(x, x_prime, variance=1., lengthscale=1., w=1.):
    """Periodic covariance function"""
    r = norm(x-x_prime, 2)
    return variance*exp(-2./(lengthscale*lengthscale)*sin(pi*r*w)**2)

def ratquad_cov(x, x_prime, variance=1., lengthscale=1., alpha=1.):
    """Rational quadratic covariance function"""
    r = norm(x-x_prime, 2)
    return variance*(1. + r*r/(2*alpha*lengthscale*lengthscale))**-alpha

def prod_cov(x, x_prime, kerns, kern_args):
    """Product covariance function."""
    k = 1.
    for kern, kern_arg in zip(kerns, kern_args):
        k*=kern(x, x_prime, **kern_arg)
    return k
        
def add_cov(x, x_prime, kerns, kern_args):
    """Additive covariance function."""
    k = 0.
    for kern, kern_arg in zip(kerns, kern_args):
        k+=kern(x, x_prime, **kern_arg)
    return k

def basis_cov(x, x_prime, basis):
    """Basis function covariance."""
    return (basis.Phi(x)*basis.Phi(x_prime)).sum()

def contour_data(model, data, length_scales, log_SNRs):
    """
    Evaluate the GP objective function for a given data set for a range of
    signal to noise ratios and a range of lengthscales.

    :data_set: A data set from the utils.datasets director.
    :length_scales: a list of length scales to explore for the contour plot.
    :log_SNRs: a list of base 10 logarithm signal to noise ratios to explore for the contour plot.
    :kernel: a kernel to use for the 'signal' portion of the data.
    """

    
    lls = []
    total_var = var(data['Y'])
    for log_SNR in log_SNRs:
        SNR = 10.**log_SNR
        noise_var = total_var / (1. + SNR)
        signal_var = total_var - noise_var
        model.kern['.*variance'] = signal_var
        model.likelihood.variance = noise_var
        length_scale_lls = []

        for length_scale in length_scales:
            model['.*lengthscale'] = length_scale
            length_scale_lls.append(model.log_likelihood())

        lls.append(length_scale_lls)

    return asarray(lls)



