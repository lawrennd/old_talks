\ifndef{mountainCarSimulator}
\define{mountainCarSimulator}
\editme

\subsection{Mountain Car Simulator}

\notes{To illustrate the above mentioned concepts we use the
[mountain car simulator](https://github.com/openai/gym/wiki/MountainCarContinuous-v0). This
simulator is widely used in machine learning to test reinforcement
learning algorithms. The goal is to define a control policy on a car
whose objective is to climb a mountain. Graphically, the problem looks
as follows:}

\figure{\includepng{\diagramsDir/uq/mountaincar}{60%}{negate}}{The mountain car simulation from the Open AI gym.}{mountain-car}

\notes{The goal is to define a sequence of actions (push the car right
or left with certain intensity) to make the car reach the flag after a
number $T$ of time steps.}

\notes{At each time step $t$, the car is characterized by a vector
$\inputVector_{t} = (p_t,v_t)$ of states which are respectively the
the position and velocity of the car at time $t$. For a sequence of
states (an episode), the dynamics of the car is given by}

\newslide{Car Dynamics}

$$
\inputVector_{t+1} = \mappingFunction(\inputVector_{t},\textbf{u}_{t})
$$
\slides{where $\textbf{u}_t$ is the action force, $\inputVector_t = (p_t, v_t)$ is the vehicle state}
\notes{where $\textbf{u}_{t}$ is the value of an action force, which in this example corresponds to push car to the left (negative value) or to the right (positive value). The actions across a full episode are represented in a policy $\textbf{u}_{t} = \pi(\inputVector_{t},\theta)$ that acts according to the current state of the car and some parameters $\theta$. In the following examples we will assume that the policy is linear which allows us to write $\pi(\inputVector_{t},\theta)$ as}

\include{_uq/includes/mountain-car-setup.py}

\newslide{Policy}

\slides{* Assume policy is linear with parameters $\boldsymbol{\theta}$}
$$
\pi(\inputVector,\theta)= \theta_0 + \theta_p p + \theta_vv.
$$
\notes{For $t=1,\dots,T$ now given some initial state $\inputVector_{0}$ and some some values of each $\textbf{u}_{t}$, we can **simulate** the full dynamics of the car for a full episode using [Gym](https://gym.openai.com/envs/). The values of 
$\textbf{u}_{t}$ are fully determined by the parameters of the linear controller.}

\notes{After each episode of length $T$ is complete, a reward function $R_{T}(\theta)$ is computed. In the mountain car example, the reward is computed as 100 for reaching the target of the hill on the right hand side, minus the squared sum of actions (a real negative to push to the left and a real positive to push to the right) from start to goal.  Note that our reward depends on $\theta$ as we make it dependent on the parameters of the linear controller.}

\subsection{Emulate the Mountain Car}

\installcode{gym}

\setupcode{import gym}
\code{env = gym.make('MountainCarContinuous-v0')}

\notes{Our goal in this section is to find the parameters $\theta$ of the linear controller such that}
\slides{* Goal is find $\theta$ such that}
$$
\theta^* = arg \max_{\theta} R_T(\theta).
$$ 
\slides{* Reward is computed as 100 for target, minus squared sum of actions}

\notes{In this section, we directly use Bayesian optimization to solve this problem. We will use [EmuKit](https://emukit.github.io) so we first define the objective function.}


\setupcode{import mountain_car as mc
import numpy as np}


\helpercode{def target_function(X):
	"""Run the Mountain Car simulaton for each set of controller parameters in the matrix."""
    simulation_function = lambda x: mc.run_simulation(env, x)[0]
    return np.asarray([simulation_function(np.atleast_2d(x)) for x in X])[:, np.newaxis]}

\notes{For each set of parameter values of the linear controller we can run an episode of the simulator (that we fix to have a horizon of $T=500$) to generate the reward. Using as input the parameters of the controller and as outputs the rewards we can build a Gaussian process emulator of the reward. 

We start defining the input space, which is three-dimensional:}

\setupcode{from emukit.core import ContinuousParameter, ParameterSpace}

\code{position_domain = [-1.2, +1]
velocity_domain = [-1/0.07, +1/0.07]
constant_domain = [-1, +1]

space = ParameterSpace(
          [ContinuousParameter('position_parameter', *position_domain), 
           ContinuousParameter('velocity_parameter', *velocity_domain),
           ContinuousParameter('constant', *constant_domain)])}

\notes{To initalize the model we start sampling some initial points for the linear controller randomly.}

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{design = RandomDesign(space)
n_initial_points = 25
initial_design = design.get_samples(n_initial_points)}

\notes{Now run the simulation 25 times across our initial design.}

\code{y = target_function(initial_design)}

\notes{Before we start any optimization, lets have a look to the behaviour of the car with the first of these initial points that we have selected randomly.}

\setupcode{import numpy as np}

\notes{This won't render in Google `colab`, but should work in a regular Jupyter notebook if `pyglet` is installed. Details on rendering in `colab` are given in answer to this stackoverflow question <https://stackoverflow.com/questions/50107530/how-to-render-openai-gym-in-google-colab>.}

\code{random_controller = initial_design[0,:]
_, _, _, frames = mc.run_simulation(env, np.atleast_2d(random_controller), render=True)
anim=mc.animate_frames(frames, 'Random linear controller')}

\setupplotcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
               diagrams='\writeDiagramsDir/uq', 
			   filename='mountain-car-random.html')}

\newslide{Random Linear Controller}

\figure{\includehtml{\diagramsDir/uq/mountain-car-random.html}{600}{450}}{Random linear controller for the Mountain car. It fails to move the car to the top of the mountain.}{mountain-car-random}

\notes{As we can see the random linear controller does not manage to
push the car to the top of the mountain. Now, let's optimize the
regret using Bayesian optimization and the emulator for the reward. We
try 50 new parameters chosen by the expected improvement acquisition function.}

\notes{First, we initizialize a Gaussian process emulator.}

\setupcode{import GPy}

\code{kern = GPy.kern.RBF(3)
model_gpy = GPy.models.GPRegression(initial_design, y, kern, noise_var=1e-10)}

\setupcode{from emukit.model_wrappers.gpy_model_wrappers import GPyModelWrapper}

\code{model_emukit = GPyModelWrapper(model_gpy, n_restarts=5)
model_emukit.optimize()}

\notes{In Bayesian optimization an acquisition function is used to
balance exploration and exploitation to evaluate new locations close
to the optimum of the objective. In this notebook we select the
expected improvement (EI). For further details have a look at the
review paper of @Shahriari-human16.}

\setupcode{from emukit.bayesian_optimization.acquisitions import ExpectedImprovement}

\code{acquisition = ExpectedImprovement(model_emukit)}

\setupcode{from emukit.bayesian_optimization.loops.bayesian_optimization_loop import BayesianOptimizationLoop}

\code{bo = BayesianOptimizationLoop(space, model_emukit, acquisition=acquisition)
bo.run_loop(target_function, 50)
results= bo.get_results()}

\notes{Now we visualize the result for the best controller that we have found with Bayesian optimization.}

\code{_, _, _, frames = mc.run_simulation(env, np.atleast_2d(results.minimum_location), render=True)
anim=mc.animate_frames(frames, 'Best controller after 50 iterations of Bayesian optimization')}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
               diagrams='\writeDiagramsDir/uq', 
			   filename='mountain-car-simulated.html')}

\newslide{Best Controller after 50 Iterations of Bayesian Optimization}

\figure{\includehtml{\diagramsDir/uq/mountain-car-simulated.html}{600}{450}{auto}}{Mountain car simulator trained using Bayesian optimization and the simulator of the dynamics. Fifty iterations of Bayesian optimization are used to optimize the controler.}{mountain-car-similated-bayes-opt}

\notes{The car can now make it to the top of the mountain! Emulating
the reward function and using expected improvement acquisition helped us to find a linear
controller that solves the problem.}

\endif
