\ifndef{mxfusionPilco}
\define{mxfusionPilco}

\editme

\subsection{PILCO: A Model-based Policy Search}

\notes{Common reinforcement learning methods suffer from data inefficiency, which can be a issue in real world applications where gathering sufficiently large amounts of data pose economic issues and may be impossible.  propose a model-based policy search method known as PILCO in part to address this issue. PILCO uses a Gaussian process (GP) for learning the dynamics of the environment and optimizes a parametric policy function using the learned dynamics model.}

\slides{PILCO [@Deisenroth:pilco11] is a model-based data-efficient
algorithm that solves the RL problem by the following two step iterative
process:

1. Fit a Gaussian Process that models the state dynamics, using calls to a simulator 
2. Optimize a parametric policy using our GP instead of calling the simulator.}

\newslide{Enhancements MXFusion Brings}

\notes{We construct an implementation of PILCO using MXFusion. This implementation follows the main idea of PILCO and has a few enhancements in addition to the published implementation. The enhancements are as follows:
* **Use Monte Carlo integration instead of moment estimation.** We approximate the expected reward using Monte Carlo integration instead of the proposed moment estimation approach. This removes the bias in the expected reward computation and enables a wide range of choices of kernels and policy functions. In the original work, only RBF and linear kernel and only linear and RBF network policy can be used.
* **Use automatic differentiation.** Thanks to automatic differentiation, no gradient derivation is needed.
* **A unified interface of Gaussian process.** MXFusion provides an unified inferface of GP modules. We allows us to easily switch among plan GP, variational sparse GP and stocastic variational GP implementations.}

\slides{* Use Monte Carlo integration instead of moment estimation
* Use automatic differentiation
* A flexible interface for Gaussian processes, trivial to switch to sparse or stochastic variational}

\newslide{Preparation}

\notes{This notebook depends on MXNet, MXFusion and Open AI Gym. These packages can be installed into your Python environment by running the following commands.}

```bash
pip install mxnet mxfusion gym
```

Set the global configuration.

\setupcode{import os
os.environ['MXNET_ENGINE_TYPE'] = 'NaiveEngine'
from mxfusion.common import config
config.DEFAULT_DTYPE = 'float64'
%matplotlib inline}

\newslide{Example: Pendulum}

\notes{We use the inverted pendulum swingup problem as an example. We use the [Pendulum-v0](https://gym.openai.com/envs/Pendulum-v0/) environment in Open AI Gym. The task is to swing the pendulum up and balance it at the inverted position. This is a classical control problem and is known to be unsolvable with a linear controller.

To solve this problem with PILCO, we need three components:

* Execute a policy in an real environment (an Open AI Gym simulator in this example) and collect data.
* Fit a GP model as the model for the dynamics of the environment.
* Optimize the policy given the dynamics model learned from all the data that have been collected so far.

The overall PILCO algorithm is to iterate the above three steps until a policy that can solve the problem is found.}

\notes{
\subsection{Execute the Environment}

\setupcode{import gym
env = gym.make('Pendulum-v0')}

The state of the pendulum environment is a 3D vector. The first two dimensions
are the 2D location of the end point of the pendulum. The third dimension
encodes the angular speed of the pendulum. The action space is a 1D vector in
[-2, 2].

We write a helper function for executing the environment with a given policy.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation}

\code{def run_one_episode(env, policy, initial_state=None, max_steps=200, verbose=False, render=False):
    """
    Drives an episode of the OpenAI gym environment using the policy to decide next actions.
    """
    observation = env.reset()
    if initial_state is not None:
        env.env.state = initial_state
        observation = env.env._get_obs()
    env._max_episode_steps = max_steps
    step_idx = 0
    done = False
    total_reward = 0
    frames = []
    all_actions = []
    all_observations = [observation]
    while not done:
        if render:
            frames.append(env.render(mode = 'rgb_array'))
        if verbose:
            print(observation)
        action = policy(observation)
        observation, reward, done, info = env.step(action)
        all_observations.append(observation)
        all_actions.append(action)
        total_reward += reward
        step_idx += 1
        if done or step_idx>=max_steps-1:
            print("Episode finished after {} timesteps because {}".format(step_idx+1, "'done' reached" if done else "Max timesteps reached"))
            break
    if render:
        fig = plt.figure()
        ax = fig.gca()
        fig.tight_layout()
        patch = ax.imshow(frames[0])
        ax.axis('off')
        def animate(i):
            patch.set_data(frames[i])
        anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=20)
        return total_reward, np.array(all_observations, dtype=np.float64,), np.array(all_actions, dtype=np.float64), anim
    else:
        return total_reward, np.array(all_observations, dtype=np.float64,), np.array(all_actions, dtype=np.float64)}

\notes{We first apply a random policy and see how the environment reacts. The random policy uniformly samples in the space of action.}

\code{def random_policy(state):
    return env.action_space.sample()}

\notes{
The animation is generated with the following commands:
```python
anim = run_one_episode(env, random_policy, max_steps=500, render=True, verbose=False)[-1]

with open('animation_random_policy.html', 'w') as f:
    f.write(anim.to_jshtml())
```
}

\subsection{Pendulum}

\figure{\includehtml{../slides/diagrams/ml/animation_random_policy.html}{100%}{auto}}{Random policy for the control of the pendulum.}{pendulum-random-policy}

\newslide{Fit the Dynamics Model}

\slides{* Dynamics:}
\notes{The dynamics model of pendulum can be written as}
$$
p(\dataScalar_{t+1}|\dataScalar_t, a_t)
$$ 
\notes{where $\dataScalar_t$ is the state vector at the time $t$ and $a_t$ is the action taken at the time $t$.

PILCO uses a Gaussian process to model the above dynamics.}

\code{def prepare_data(state_list, action_list, win_in):
    """
    Prepares a list of states and a list of actions as inputs to the Gaussian Process for training.
    """
    
    X_list = []
    Y_list = []
    
    for state_array, action_array in zip(state_list, action_list):
        # the state and action array shape should be aligned.
        assert state_array.shape[0]-1 == action_array.shape[0]
        
        for i in range(state_array.shape[0]-win_in):
            Y_list.append(state_array[i+win_in:i+win_in+1])
            X_list.append(np.hstack([state_array[i:i+win_in].flatten(), action_array[i:i+win_in].flatten()]))
    X = np.vstack(X_list)
    Y = np.vstack(Y_list)
    return X, Y}

\notes{In this example, we do a maximum likelihood estimate for the model hyper-
parameters. In `MXFusion`, Gaussian process regression model is available as a
module, which includes a dediated inference algorithm.}

\code{import mxnet as mx
from mxfusion import Model, Variable
from mxfusion.components.variables import PositiveTransformation
from mxfusion.components.distributions.gp.kernels import RBF
from mxfusion.modules.gp_modules import GPRegression
from mxfusion.inference import GradBasedInference, MAP}

\subsection{Define and fit the model}

\code{def fit_model(state_list, action_list, win_in, verbose=True):
    """
    Fits a Gaussian Process model to the state / action pairs passed in. 
    This creates a model of the environment which is used during
    policy optimization instead of querying the environment directly.
    
    See mxfusion.gp_modules for additional types of GP models to fit,
    including Sparse GP and Stochastic Varitional Inference Sparse GP.
    """
    X, Y = prepare_data(state_list, action_list, win_in)

    m = Model()
    m.N = Variable()
    m.X = Variable(shape=(m.N, X.shape[-1]))
    m.noise_var = Variable(shape=(1,), transformation=PositiveTransformation(),
                           initial_value=0.01)
    m.kernel = RBF(input_dim=X.shape[-1], variance=1, lengthscale=1, ARD=True)
    m.Y = GPRegression.define_variable(
        X=m.X, kernel=m.kernel, noise_var=m.noise_var,
        shape=(m.N, Y.shape[-1]))
    m.Y.factor.gp_log_pdf.jitter = 1e-6

    infr = GradBasedInference(
        inference_algorithm=MAP(model=m, observed=[m.X, m.Y]))
    infr.run(X=mx.nd.array(X, dtype='float64'),
             Y=mx.nd.array(Y, dtype='float64'),
             max_iter=1000, learning_rate=0.1, verbose=verbose)
    return m, infr, X, Y}

\subsection{Policy}

\slides{* Make use of neural network with one hidden layer}
\notes{PILCO computes the expected reward of a policy given
the dynamics model. First, we need to define the parametric form of the policy.
In this example, we use a neural network with one hidden layer. As the action
space is [-2, 2], we apply a `tanh` transformation and multiply the come with two.
This enforces the returned actions stay within the range.}

\notes{We define a neural network with one hidden layer and and output constrained between [-2,2] for the policy.}

\code{from mxnet.gluon import HybridBlock
from mxnet.gluon.nn import Dense

class NNController(HybridBlock):
	"""Define a neural network policy network."""
    def __init__(self, prefix=None, params=None):
        super(NNController, self).__init__(prefix=prefix, params=params)
        self.dense1 = Dense(100, in_units=len(env.observation_space.high), dtype='float64', activation='relu')
        self.dense2 = Dense(1, in_units=100, dtype='float64', activation='tanh')

    def hybrid_forward(self, F, x):
        out = self.dense2(self.dense1(x))*2 # Scale up the output
        return out 
    
policy = NNController()
policy.collect_params().initialize(mx.initializer.Xavier(magnitude=1))}

\notes{To compute the expected reward, we also need to define a reward function. This reward function is defined by us according to the task. The main component is the height of the pendulum. We also penalize the force and the angular momentum.}

\code{class CostFunction(mx.gluon.HybridBlock):
    """
    The goal is to get the pendulum upright and stable as quickly as possible.

	Taken from the code for Pendulum.
    """
    def hybrid_forward(self, F, state, action):
        """
        :param state: [np.cos(theta), np.sin(theta), ~ momentum(theta)]
        a -> 0 when pendulum is upright, largest when pendulum is hanging down completely.
        b -> penalty for taking action
        c -> penalty for pendulum momentum
        """
        a_scale = 2.
        b_scale = .001
        c_scale = .1
        a = F.sum(a_scale * (state[:,:,0:1] -1) ** 2, axis=-1)
        b = F.sum(b_scale * action ** 2, axis=-1)
        c = F.sum(c_scale * state[:,:,2:3] ** 2, axis=-1)
        return (a + c + b)
    
cost = CostFunction()}

\notes{The expected reward function can be written as 
$$
R = \mathbb{E}_{p(\dataScalar_T, \ldots,
\dataScalar_0)}\left(\sum_{t=0}^\top r(\dataScalar_t)\right)
$$
where $r(\cdot)$ is the reward function, $p(\dataScalar_T, \ldots, \dataScalar_0)$ is the joint distribution when applying the policy to the
dynamics model:
$$
p(\dataScalar_T, \ldots, \dataScalar_0) = p(\dataScalar_0) \prod_{t=1}^\top p(\dataScalar_t|\dataScalar_{t-1}, a_{t-1}),
$$
where $a_{t-1} = \pi(\dataScalar_{t-1})$ is the action taken at the time $t-1$, which is the outcome of the policy $\pi(\cdot)$.

The expected reward function is implemented as follows.}

\subsection{Obtaining the policy gradients}

\setupcode{from mxfusion.inference.inference_alg import SamplingAlgorithm}

\code{class PolicyUpdateGPParametricApprox(SamplingAlgorithm):
	"""Class for the policy update for PILCO."""
    def compute(self, F, variables):
        
        s_0 = self.initial_state_generator(self.num_samples)
        a_0 = self.policy(s_0)
        a_t_plus_1 = a_0
        x_t = F.expand_dims(F.concat(s_0, a_0, dim=1), axis=1)

        gp = self.model.Y.factor
        sample_func = gp.draw_parametric_samples(F, variables, self.num_samples, self.approx_samples)
        cost = 0
        for t in range(self.n_time_steps):
            s_t_plus_1 = sample_func(F, x_t)
            cost = cost + self.cost_function(s_t_plus_1, a_t_plus_1)
            a_t_plus_1 = mx.nd.expand_dims(self.policy(s_t_plus_1), axis=2)
            x_t = mx.nd.concat(s_t_plus_1, a_t_plus_1, dim=2)
        total_cost = F.mean(cost)
        return total_cost, total_cost}

\notes{We optimize the policy with respect to the expected reward by using a gradient optimizer.}

\setupcode{from mxfusion.inference import GradTransferInference}

\code{def optimize_policy(policy, cost_func, model, infr, model_data_X, model_data_Y,
                    initial_state_generator, num_grad_steps,
                    learning_rate=1e-2, num_time_steps=100, 
                    num_samples=10, verbose=True):
    """
    Takes as primary inputs a policy, cost function, and trained model.
    Optimizes the policy for num_grad_steps number of iterations.
    """
    mb_alg = PolicyUpdateGPParametricApprox(
        model=model, observed=[model.X, model.Y], cost_function=cost_func,
        policy=policy, n_time_steps=num_time_steps,
        initial_state_generator=initial_state_generator,
        num_samples=num_samples)

    infr_pred = GradTransferInference(
        mb_alg, infr_params=infr.params, train_params=policy.collect_params())
    infr_pred.run(
        max_iter=num_grad_steps,
        X=mx.nd.array(model_data_X, dtype='float64'),
        Y=mx.nd.array(model_data_Y, dtype='float64'),
        verbose=verbose, learning_rate=learning_rate)
    return policy}

\subsection{The Loop}


\notes{We need to define a function that provides random initial states.}

\code{def initial_state_generator(num_initial_states):
    """
    Starts from valid states by drawing theta and momentum
    then computing np.cos(theta) and np.sin(theta) for state[0:2].s
    """
    return mx.nd.array(
        [env.observation_space.sample() for i in range(num_initial_states)],
        dtype='float64')}


\code{num_episode = 20 # how many model fit + policy optimization episodes to run
num_samples = 100 # how many sample trajectories the policy optimization loop uses
num_grad_steps = 1000 # how many gradient steps the optimizer takes per episode
num_time_steps = 100 # how far to roll out each sample trajectory
learning_rate = 1e-3 # learning rate for the policy optimization

all_states = []
all_actions = []}

\code{for i_ep in range(num_episode):
    # Run an episode and collect data.
    if i_ep == 0:
        policy_func = lambda x: env.action_space.sample()
    else:
        policy_func = lambda x: policy(mx.nd.expand_dims(mx.nd.array(x, dtype='float64'), axis=0)).asnumpy()[0]
    total_reward, states, actions = run_one_episode(
        env, policy_func, max_steps=num_time_steps)
    all_states.append(states)
    all_actions.append(actions)

    # Fit a model.
    model, infr, model_data_X, model_data_Y = fit_model(
        all_states, all_actions, win_in=1, verbose=True)

    # Optimize the policy.
    policy = optimize_policy(
        policy, cost, model, infr, model_data_X, model_data_Y,
        initial_state_generator, num_grad_steps=num_grad_steps,
        num_samples=num_samples, learning_rate=learning_rate,
        num_time_steps=num_time_steps)}

\newslide{After First Epsiode}

Policy after the first episode (random exploration):

\figure{\includehtml{../slides/diagrams/ml/animation_policy_iter_0.html}{100%}{auto}}{PILCO policy for control of the animation after first episode (using random exploration).}{pilco-pendulum-policy-iter-0}

\newslide{After Fifth Episode}

Policy after the 5th episode:

\figure{\includehtml{../slides/diagrams/ml/animation_policy_iter_4.html}{100%}{auto}}{PILCO policy for control of the animation after the fifth episode.}{pilco-pendulum-policy-iter-0}

\newslide{Contribute!}

[https://github.com/amzn/mxfusion](https://github.com/amzn/mxfusion)

\newslide{Future plans}

\slides{* Deep GPs (implemented, not yet merged)
* MCMC Methods
* Time series models (RGPs)}

\endif
