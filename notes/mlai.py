# Python code for MLAI lectures.

# import the time model to allow python to pause.
import time
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from IPython.display import display, clear_output, HTML

def write_figure(filename, figure=None, **kwargs):
    """Write figure in correct formating"""
    if 'transparent' not in kwargs:
        kwargs['transparent'] = True
    if figure is None:
        plt.savefig(filename, **kwargs)
    else:
        figure.savefig(filename, **kwargs)
    
##########          Week 2          ##########
def init_perceptron(x_plus, x_minus, seed=1000001):
    np.random.seed(seed=seed)
    # flip a coin (i.e. generate a random number and check if it is greater than 0.5)
    choose_plus = np.random.rand(1)>0.5
    if choose_plus:
        # generate a random point from the positives
        index = np.random.randint(0, x_plus.shape[1])
        x_select = x_plus[index, :]
        w = x_plus[index, :] # set the normal vector to that point.
        b = 1
    else:
        # generate a random point from the negatives
        index = np.random.randint(0, x_minus.shape[1])
        x_select = x_minus[index, :]
        w = -x_minus[index, :] # set the normal vector to minus that point.
        b = -1
    return w, b, x_select


def update_perceptron(w, b, x_plus, x_minus, learn_rate):
    "Update the perceptron."
    # select a point at random from the data
    choose_plus = np.random.uniform(size=1)>0.5
    updated=False
    if choose_plus:
        # choose a point from the positive data
        index = np.random.randint(x_plus.shape[0])
        x_select = x_plus[index, :]
        if np.dot(w, x_select)+b <= 0.:
            # point is currently incorrectly classified
            w += learn_rate*x_select
            b += learn_rate
            updated=True
    else:
        # choose a point from the negative data
        index = np.random.randint(x_minus.shape[0])
        x_select = x_minus[index, :]
        if np.dot(w, x_select)+b > 0.:
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
        return np.sqrt(self.sum_squares/self.num_data)

    def predict(self, X):
        raise NotImplementedError

    
class ProbMapModel(ProbModel, MapModel):
    """Probabilistic model that provides a mapping from X to y."""
    def __init__(self, X, y):
        ProbModel.__init__(self)
        MapModel.__init__(self, X, y)

    
class LM(ProbMapModel):
    """Linear model
    :param X: input values
    :type X: numpy.ndarray
    :param y: target values
    :type y: numpy.ndarray
    :param basis: basis function 
    :param type: function"""

    def __init__(self, X, y, basis):
        "Initialise"
        ProbModel.__init__(self)
        self.y = y
        self.num_data = y.shape[0]
        self.X = X
        self.sigma2 = 1.
        self.basis = basis
        self.Phi = self.basis.Phi(X)
        self.name = 'LM_'+self.basis.function.__name__
        self.objective_name = 'Sum of Square Training Error'

    def update_QR(self):
        "Perform the QR decomposition on the basis matrix."
        self.Q, self.R = np.linalg.qr(self.Phi)

    def fit(self):
        """Minimize the objective function with respect to the parameters"""
        self.update_QR()
        self.w_star = sp.linalg.solve_triangular(self.R, np.dot(self.Q.T, self.y))
        self.update_sum_squares()
        self.sigma2=self.sum_squares/self.num_data

    def predict(self, X):
        """Return the result of the prediction function."""
        return np.dot(self.basis.Phi(X), self.w_star), None
        
    def update_f(self):
        """Update values at the prediction points."""
        self.f = np.dot(self.Phi, self.w_star)
        
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
        return -self.num_data/2.*np.log(np.pi*2.)-self.num_data/2.*np.log(self.sigma2)-self.sum_squares/(2.*self.sigma2)
    

class basis():
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
    
def polynomial(x, num_basis=4, data_limits=[-1., 1.]):
    "Polynomial basis"
    centre = data_limits[0]/2. + data_limits[1]/2.
    span = data_limits[1] - data_limits[0]
    z = x - centre
    z = 2*z/span
    Phi = np.zeros((x.shape[0], num_basis))
    for i in range(num_basis):
        Phi[:, i:i+1] = z**i
    return Phi

def radial(x, num_basis=4, data_limits=[-1., 1.], width=None):
    """Radial basis constructed using exponentiated quadratic form."""
    if num_basis>1:
        centres=np.linspace(data_limits[0], data_limits[1], num_basis)
        if width is None:
            width = (centres[1]-centres[0])/2.
    else:
        centres = np.asarray([data_limits[0]/2. + data_limits[1]/2.])
        if width is None:
            width = (data_limits[1]-data_limits[0])/2.
    
    Phi = np.zeros((x.shape[0], num_basis))
    for i in range(num_basis):
        Phi[:, i:i+1] = np.exp(-0.5*((x-centres[i])/width)**2)
    return Phi


def fourier(x, num_basis=4, data_limits=[-1., 1.], frequency_range=None):
    """Fourier basis"""
    tau = 2*np.pi
    span = float(data_limits[1]-data_limits[0])
    Phi = np.ones((x.shape[0], num_basis))
    for i in range(1, num_basis):
        count = float((i+1)//2)
        if frequency_range is None:
            frequency = count/span
        else:
            frequency = frequency_range[i]
        if i % 2:
            Phi[:, i:i+1] = np.sin(tau*frequency*x)
        else:
            Phi[:, i:i+1] = np.cos(tau*frequency*x)
    return Phi

def relu(x, num_basis=4, data_limits=[-1., 1.], gain=None):
    """Rectified linear units basis"""
    if num_basis>2:
        centres=np.linspace(data_limits[0], data_limits[1], num_basis)
    else:
        centres = np.asarray([data_limits[0]/2. + data_limits[1]/2.])
    if gain is None:
        gain = np.ones(num_basis-1)
    Phi = np.zeros((x.shape[0], num_basis))
    # Create the bias
    Phi[:, 0] = 1.0
    for i in range(1, num_basis):
        Phi[:, i:i+1] = (gain[i-1]*x>centres[i-1])*(x-centres[i-1])
    return Phi

def tanh(x, num_basis=4, data_limits=[-1., 1.], gain=None):
    """Hyperbolic tangents"""
    if num_basis>2:
        centres=np.linspace(data_limits[0], data_limits[1], num_basis)
        width = (centres[1]-centres[0])/2.
    else:
        centres = np.asarray([data_limits[0]/2. + data_limits[1]/2.])
        width = (data_limits[1]-data_limits[0])/2.
    if gain is None:
        gain = np.ones(num_basis-1)/width
    Phi = np.zeros((x.shape[0], num_basis))
    # Create the bias
    Phi[:, 0] = 1.0
    for i in range(1, num_basis):
        Phi[:, i:i+1] = np.tanh(gain[i-1]*(x-centres[i-1]))
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

        return - 0.5*(np.log(varsigma).sum() + arg.sum() + n*d*np.log(2*np.pi))


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
        dlnZ_dmu = np.zeros(nu.shape)
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
        self.w2 = np.random.normal(size=self.nodes)/self.nodes
        self.b2 = np.random.normal(size=1)
        self.w1 = np.random.normal(size=self.nodes)
        self.b1 = np.random.normal(size=self.nodes)
        

    def predict(self, x):
        "Compute output given current basis functions."
        vxmb = self.w1*x + self.b1
        phi = vxmb*(vxmb>0)
        return np.sum(self.w2*phi) + self.b2

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
        gen = np.random.rand(self.nodes)
        self.use = gen > self.drop_p
        
    def predict(self, x):
        "Compute output given current basis functions used."
        vxmb = self.w1[self.use]*x + self.b1[self.use]
        phi = vxmb*(vxmb>0)
        return np.sum(self.w2[self.use]*phi) + self.b2

class NonparametricDropoutNeuralNetwork(SimpleDropoutNeuralNetwork):
    """A non parametric dropout neural network
    :param alpha: alpha parameter of the IBP controlling dropout.
    :param beta: beta parameter of the two parameter IBP controlling dropout."""
    def __init__(self, alpha=10, beta=1, n=1000):
        self.update_num = 0
        self.alpha = alpha
        self.beta = beta
        self.gamma = 0.5772156649
        tot = np.log(n) + self.gamma + 0.5/n * (1./12.)/(n*n)
        self.exp_features = alpha*beta*tot
        self.maxk = np.max((10000,int(self.exp_features + np.ceil(4*np.sqrt(self.exp_features)))))
        donn.__init__(self, nodes=self.maxk, drop_p=self.alpha/self.maxk)
        self.maxval = 0
        self.w2 *= self.maxk/self.alpha
        self.count = np.zeros(self.maxk)
    
    
        
    def do_samp(self):
        "Sample the next set of basis functions to be used"
        
        new=np.random.poisson(self.alpha*self.beta/(self.beta + self.update_num))
        use_prob = self.count[:self.maxval]/(self.update_num+self.beta)
        gen = np.random.rand(1, self.maxval)
        self.use = np.zeros(self.maxk, dtype=bool)
        self.use[:self.maxval] = gen < use_prob
        self.use[self.maxval:self.maxval+new] = True
        self.maxval+=new
        self.update_num+=1
        self.count[:self.maxval] += self.use[:self.maxval]
        

    
class BLM(ProbMapModel):
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
        
    def update_QR(self):
        "Perform the QR decomposition on the basis matrix."
        self.Q, self.R = np.linalg.qr(np.vstack([self.Phi, np.sqrt(self.sigma2/self.alpha)*np.eye(self.basis.number)]))

    def fit(self):
        """Minimize the objective function with respect to the parameters"""
        self.update_QR()
        self.QTy = np.dot(self.Q[:self.y.shape[0], :].T, self.y)
        self.mu_w = sp.linalg.solve_triangular(self.R, self.QTy)
        self.RTinv = sp.linalg.solve_triangular(self.R, np.eye(self.R.shape[0]), trans='T')
        self.C_w = np.dot(self.RTinv, self.RTinv.T)
        self.update_sum_squares()

    def predict(self, X, full_cov=False):
        """Return the result of the prediction function."""
        Phi = self.basis.Phi(X)
        # A= R^-T Phi.T
        A = sp.linalg.solve_triangular(self.R, Phi.T, trans='T')
        mu = np.dot(A.T, self.QTy)
        if full_cov:
            return mu, self.sigma2*np.dot(A.T, A)
        else:
            return mu, self.sigma2*(A*A).sum(0)[:, None]
        
    def update_f(self):
        """Update values at the prediction points."""
        self.f_bar = np.dot(self.Phi, self.mu_w)
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
        self.log_det = self.num_data*np.log(self.sigma2*np.pi*2.)-2*np.log(np.abs(np.linalg.det(self.Q[self.y.shape[0]:, :])))
        self.quadratic = (self.y*self.y).sum()/self.sigma2 - (self.QTy*self.QTy).sum()/self.sigma2
        
    def nll_split(self):
        "Compute the determinant and quadratic term of the negative log likelihood"
        self.update_nll()
        return self.log_det, self.quadratic
    
    def log_likelihood(self):
        """Compute the log likelihood."""
        self.update_ll()
        return -self.log_det - self.quadratic

##########          Week 8            ##########

    

# Code for loading pgm from http://stackoverflow.com/questions/7368739/numpy-and-16-bit-pgm
def load_pgm(filename, directory=None, byteorder='>'):
    """Return image data from a raw PGM file as numpy array.

    Format specification: http://netpbm.sourceforge.net/doc/pgm.html

    """
    import re
    import numpy
    if directory is not None:
        import os.path
        filename=os.path.join(directory, filename)
    with open(filename, 'rb') as f:
        buffer = f.read()
    try:
        header, width, height, maxval = re.search(
            b"(^P5\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    except AttributeError:
        raise ValueError("Not a raw PGM file: '%s'" % filename)
    return numpy.frombuffer(buffer,
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
        self.w_star = np.zeros(self.basis.number)
        
    def predict(self, X):
        "Generates the prediction function and the basis matrix."
        Phi = self.basis.Phi(X)
        f = np.dot(Phi, self.w_star)
        return 1./(1+np.exp(-f)), Phi

    def gradient(self):
        "Generates the gradient of the parameter vector."
        self.update_g()
        dw = -(self.Phi[self.y.values, :]*(1-self.g[self.y.values, :])).sum(0)
        dw += (Phi[~self.y.values, :]*self.g[~self.y.values, :]).sum(0)
        return dw[:, None]

    def compute_g(self, f):
        "Compute the transformation and its logarithms."
        eps = 1e-16
        g = 1./(1+np.exp(f))
        log_g = np.zeros((f.shape))
        log_gminus = np.zeros((f.shape))
        
        # compute log_g for values out of bound
        bound = np.log(eps)
        ind = f<-bound
        
        log_g[ind] = -f[ind]
        log_gminus[ind] = eps
        ind = f>bound
        log_g[ind] = eps
        log_gminus[ind] = f[ind]
        ind = (f>=-bound & f<=bound)
        log_g[ind] = np.log(self.g[ind])
        log_gminus[ind] = np.log(1-self.g[ind])
        return g, log_g, log_gminus
        
    def update_g(self):
        "Computes the prediction function on training data."
        self.f = np.dot(self.Phi, self.w_star)
        self.g, self.log_g, self.log_gminus = self.compute_g(self.f)
        
    def objective(self):
        "Computes the objective function."
        self.update_g()
        return self.log_g[self.y.values, :].sum() + np.log_gminus[~self.y.values, :].sum()
    
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
        self.Kinv = np.linalg.inv(self.K+self.sigma2*np.eye(self.K.shape[0]))
        # the log determinant of the covariance matrix.
        self.logdetK = np.linalg.det(self.K+self.sigma2*np.eye(self.K.shape[0]))
        # The matrix inner product of the inverse covariance
        self.Kinvy = np.dot(self.Kinv, self.y)
        self.yKinvy = (self.y*self.Kinvy).sum()

    def fit(self):
        pass

    def update_nll(self):
        "Precompute the log determinant and quadratic term from the negative log likelihod"
        self.log_det = 0.5*(self.K.shape[0]*np.log(2*np.pi) + self.logdetK)
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
        A = np.dot(self.Kinv, K_star)
        mu_f = np.dot(A.T, self.y)
        k_starstar = self.kernel.diag(X_test)
        c_f = k_starstar - (A*K_star).sum(0)[:, None]
        return mu_f, c_f
        
def posterior_f(self, X_test):
    """Compute the posterior distribution for f in the GP"""
    K_star = self.kernel.K(self.X, X_test)
    A = np.dot(self.Kinv, K_star)
    mu_f = np.dot(A.T, self.y)
    K_starstar = self.kernel.K(X_test, X_test)
    C_f = K_starstar - np.dot(A.T, K_star)
    return mu_f, C_f

def update_inverse(self):
    """Update the inverse covariance in a numerically more stable manner"""
    # Perform Cholesky decomposition on matrix
    self.R = sp.linalg.cholesky(self.K + self.sigma2*self.K.shape[0])
    # compute the log determinant from Cholesky decomposition
    self.logdetK = 2*np.log(np.diag(self.R)).sum()
    # compute y^\top K^{-1}y from Cholesky factor
    self.Rinvy = sp.linalg.solve_triangular(self.R, self.y)
    self.yKinvy = (self.Rinvy**2).sum()
    
    # compute the inverse of the upper triangular Cholesky factor
    self.Rinv = sp.linalg.solve_triangular(self.R, np.eye(self.K.shape[0]))
    self.Kinv = np.dot(self.Rinv, self.Rinv.T)


class kernel():
    """Covariance function
    :param function: covariance function
    :type function: function
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * """

    def __init__(self, function, **kwargs):        
        self.function=function
        self.parameters=kwargs
        
    def K(self, X, X2=None):
        """Compute the full covariance function given a kernel function for two data points."""
        if X2 is None:
            X2 = X
        K = np.zeros((X.shape[0], X2.shape[0]))
        for i in np.arange(X.shape[0]):
            for j in np.arange(X2.shape[0]):
                K[i, j] = self.function(X[i, :], X2[j, :], **self.parameters)

        return K

    def diag(self, X):
        """Compute the diagonal of the covariance function"""
        diagK = np.zeros((X.shape[0], 1))
        for i in range(X.shape[0]):            
            diagK[i] = self.function(X[i, :], X[i, :], **self.parameters)
        return diagK

def exponentiated_quadratic(x, x_prime, variance=1., lengthscale=1.):
    """Exponentiated quadratic covariance function."""
    r = np.linalg.norm(x-x_prime, 2)
    return variance*np.exp((-0.5*r*r)/lengthscale**2)        

def eq_cov(x, x_prime, variance=1., lengthscale=1.):
    """Exponentiated quadratic covariance function."""
    diffx = x - x_prime
    return variance*np.exp(-0.5*np.dot(diffx, diffx)/lengthscale**2)


def mlp_cov(x, x_prime, variance=1., w=1., b=5., alpha=1.):
    """Covariance function for a MLP based neural network."""
    inner = np.dot(x, x_prime)*w + b
    norm = np.sqrt(np.dot(x, x)*w + b + alpha)*np.sqrt(np.dot(x_prime, x_prime)*w + b+alpha)
    arg = np.clip(inner/norm, -1, 1) # clip as numerically can be > 1
    theta = np.arccos(arg)
    return variance*0.5*(1. - theta/np.pi)      

def icm_cov(x, x_prime, B, subkernel, **kwargs):
    """Intrinsic coregionalization model. First index is outputs considered for covariance function."""
    i = x[0]
    i_prime = x_prime[0]
    return B[i, i_prime]*subkernel(x[1:], x_prime[1:], **kwargs)

def slfm_cov(x, x_prime, W, subkernel, **kwargs):
    """Semi-parametric latent factor model covariance function. First index is the output of the covariance function."""
    W = np.asarray(W)
    B = np.dot(W, W.T)
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
        return (1-(2*s*s-1)*cos2th)/np.sqrt(a/inner + 1 - s*s*cos2th)*s

    inner = np.dot(x, x_prime)*w + b
    inner_1 = np.dot(x, x)*w + b
    inner_2 = np.dot(x_prime, x_prime)*w + b
    norm_1 = np.sqrt(inner_1 + alpha)
    norm_2 = np.sqrt(inner_2 + alpha)
    norm = norm_1*norm_2
    s = np.sqrt(inner_1)/norm_1
    s_prime = np.sqrt(inner_2)/norm_2
    arg = np.clip(inner/norm, -1, 1) # clip as numerically can be > 1
    arg2 = np.clip(inner/np.sqrt(inner_1*inner_2), -1, 1) # clip as numerically can be > 1
    theta = np.arccos(arg)
    return variance*0.5*((1. - theta/np.pi)*inner + h(arg2, inner_2, s, alpha)/np.pi + h(arg2, inner_1, s_prime, alpha)/np.pi) 


def polynomial_cov(x, x_prime, variance=1., degree=2., w=1., b=1.):
    """Polynomial covariance function."""
    return variance*(np.dot(x, x_prime)*w + b)**degree

def linear_cov(x, x_prime, variance=1.):
    """Linear covariance function."""
    return variance*np.dot(x, x_prime)

def bias_cov(x, x_prime, variance=1.):
    """Bias covariance function."""
    return variance

def mlp_cov(x, x_prime, variance=1., w=1., b=1.):
    """MLP covariance function."""
    return variance*np.arcsin((w*np.dot(x, x_prime) + b)/np.sqrt((np.dot(x, x)*w +b + 1)*(np.dot(x_prime, x_prime)*w + b + 1)))

def sinc_cov(x, x_prime, variance=1., w=1.):
    """Sinc covariance function."""
    r = np.linalg.norm(x-x_prime, 2)
    return variance*np.sinc(np.pi*w*r)

def ou_cov(x, x_prime, variance=1., lengthscale=1.):
    """Ornstein Uhlenbeck covariance function."""
    r = np.linalg.norm(x-x_prime, 2)
    return variance*np.exp(-r/lengthscale)        

def brownian_cov(t, t_prime, variance=1.):
    """Brownian motion covariance function."""
    if t>=0 and t_prime>=0:
        return variance*np.min([t, t_prime])
    else:
        raise ValueError("For Brownian motion covariance only positive times are valid.")

def periodic_cov(x, x_prime, variance=1., lengthscale=1., w=1.):
    """Periodic covariance function"""
    r = np.linalg.norm(x-x_prime, 2)
    return variance*np.exp(-2./(lengthscale*lengthscale)*np.sin(np.pi*r*w)**2)

def ratquad_cov(x, x_prime, variance=1., lengthscale=1., alpha=1.):
    """Rational quadratic covariance function"""
    r = np.linalg.norm(x-x_prime, 2)
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
