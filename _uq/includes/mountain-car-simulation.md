
\subsection{Mountain Car Simulator}

\notes{To illustrate the above mentioned concepts we we use the [mountain car simulator](https://github.com/openai/gym/wiki/MountainCarContinuous-v0). This simulator is widely used in machine learning to test reinforcement learning algorithms. The goal is to define a control policy on a car whose objective is to climb a mountain. Graphically, the problem looks as follows:}

\includepng{../slides/diagrams/uq/mountaincar}{}{negate}
\notes{\caption{The mountain car simulation from the Open AI gym.}}

\notes{The goal is to define a sequence of actions (push the car right or left with certain intensity) to make the car reach the flag after a number $T$ of time steps.

At each time step $t$, the car is characterized by a vector $\inputVector_{t} = (p_t,v_t)$ of states which are respectively the the position and velocity of the car at time $t$. For a sequence of states (an episode), the dynamics of the car is given by}

\newslide{Car Dynamics}

$$\inputVector_{t+1} = \mappingFunction(\inputVector_{t},\textbf{u}_{t})$$

\slides{where $\textbf{u}_t$ is the action force, $\inputVector_t = (p_t, v_t)$ is the vehicle state}

\notes{where $\textbf{u}_{t}$ is the value of an action force, which in this example corresponds to push car to the left (negative value) or to the right (positive value). The actions across a full episode are represented in a policy $\textbf{u}_{t} = \pi(\inputVector_{t},\theta)$ that acts according to the current state of the car and some parameters $\theta$. In the following examples we will assume that the policy is linear which allows us to write $\pi(\inputVector_{t},\theta)$ as}


\newslide{Policy}

\slides{
* Assume policy is linear with parameters $\boldsymbol{\theta}$}

$$\pi(\inputVector,\theta)= \theta_0 + \theta_p p + \theta_vv.$$

\notes{For $t=1,\dots,T$ now given some initial state $\inputVector_{0}$ and some some values of each $\textbf{u}_{t}$, we can **simulate** the full dynamics of the car for a full episode using [Gym](https://gym.openai.com/envs/). The values of 
$\textbf{u}_{t}$ are fully determined by the parameters of the linear controller.}

\notes{After each episode of length $T$ is complete, a reward function $R_{T}(\theta)$ is computed. In the mountain car example the reward is computed as 100 for reaching the target of the hill on the right hand side, minus the squared sum of actions (a real negative to push to the left and a real positive to push to the right) from start to goal.  Note that our reward depend on $\theta$ as we make it dependent on the parameters of the linear controller.}

\subsection{Emulate the Mountain Car}

\setupcode{import gym}
\code{env = gym.make('MountainCarContinuous-v0')}

\notes{Our goal in this section is to find the parameters $\theta$ of the linear controller such that}

\slides{* Goal is find $\theta$ such that}

$$\theta^* = arg \max_{\theta} R_T(\theta).$$ 

\slides{* Reward is computed as 100 for target, minus squared sum of actions}

\notes{In this section, we directly use Bayesian optimization to solve this problem. We will use [GPyOpt](https://sheffieldml.github.io/GPyOpt/) so we first define the objective function:}

\setupcode{import mountain_car as mc
import GPyOpt}

\code{obj_func = lambda x: mc.run_simulation(env, x)[0]
objective = GPyOpt.core.task.SingleObjective(obj_func)}

\notes{For each set of parameter values of the linear controller we can run an episode of the simulator (that we fix to have a horizon of $T=500$) to generate the reward. Using as input the parameters of the controller and as outputs the rewards we can build a Gaussian process emulator of the reward. 

We start defining the input space, which is three-dimensional:}

\code{## --- We define the input space of the emulator

space= [{'name':'postion_parameter', 'type':'continuous', 'domain':(-1.2, +1)},
        {'name':'velocity_parameter', 'type':'continuous', 'domain':(-1/0.07, +1/0.07)},
        {'name':'constant', 'type':'continuous', 'domain':(-1, +1)}]

design_space = GPyOpt.Design_space(space=space)}

\notes{Now we initizialize a Gaussian process emulator.}

\code{model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)}

\notes{In Bayesian optimization an acquisition function is used to balance exploration and exploitation to evaluate new locations close to the optimum of the objective. In this notebook we select the expected improvement (EI). For further details have a look to the review paper of [Shahriari et al (2015)](http://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf).}

\code{aquisition_optimizer = GPyOpt.optimization.AcquisitionOptimizer(design_space)
acquisition = GPyOpt.acquisitions.AcquisitionEI(model, design_space, optimizer=aquisition_optimizer)
evaluator = GPyOpt.core.evaluators.Sequential(acquisition) # Collect points sequentially, no parallelization.}

\notes{To initalize the model we start sampling some initial points (25) for the linear controler randomly.}


\setupcode{from GPyOpt.experiment_design.random_design import RandomDesign}
\code{n_initial_points = 25
random_design = RandomDesign(design_space)
initial_design = random_design.get_samples(n_initial_points)}

\notes{Before we start any optimization, lets have a look to the behavior of the car with the first of these initial points that we have selected randomly.}

\setupcode{import numpy as np}

\code{random_controller = initial_design[0,:]
_, _, _, frames = mc.run_simulation(env, np.atleast_2d(random_controller), render=True)
anim=mc.animate_frames(frames, 'Random linear controller')}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
                  diagrams='../slides/diagrams/uq', 
				  filename='mountain_car_random.html')}

\newslide{Random Linear Controller}

\includehtml{../slides/diagrams/uq/mountain_car_random.html}{1024}{768}


\notes{As we can see the random linear controller does not manage to push the car to the top of the mountain. Now, let's optimize the regret using Bayesian optimization and the emulator for the reward. We try 50 new parameters chosen by the EI.}

\code{max_iter = 50
bo = GPyOpt.methods.ModularBayesianOptimization(model, design_space, objective, acquisition, evaluator, initial_design)
bo.run_optimization(max_iter = max_iter )}

\notes{Now we visualize the result for the best controller that we have found with Bayesian optimization.}

\code{_, _, _, frames = mc.run_simulation(env, np.atleast_2d(bo.x_opt), render=True)
anim=mc.animate_frames(frames, 'Best controller after 50 iterations of Bayesian optimization')}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{mc.save_frames(frames, 
                  diagrams='../slides/diagrams/uq', 
				  filename='mountain_car_simulated.html')}

\newslide{Best Controller after 50 Iterations of Bayesian Optimization}

\includehtml{../slides/diagrams/uq/mountain_car_simulated.html}{1024}{768}

\notes{he car can now make it to the top of the mountain! Emulating the reward function and using the EI helped as to find a linear controller that solves the problem.}
