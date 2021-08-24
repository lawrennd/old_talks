\ifndef{moutainCarMultiFidelityIntroduction}
\define{moutainCarMultiFidelityIntroduction}

\editme

\subsection{Mountain Car: Multi-Fidelity Emulation}

\notes{In some scenarios we have simulators of the same environment
that have different fidelities, that is that reflect with different
level of accuracy the dynamics of the real world. Running simulations
of the different fidelities also have a different cost: hight fidelity
simulations are more expensive the cheaper ones. If we have access to
these simulators we can combine high and low fidelity simulations
under the same model.

So let's assume that we have two simulators of the mountain car
dynamics, one of high fidelity (the one we have used) and another one
of low fidelity. The traditional approach to this form of
multi-fidelity emulation is to assume that}
$$
\mappingFunction_i\left(\inputVector\right) = \rho\mappingFunction_{i-1}\left(\inputVector\right) + \delta_i\left(\inputVector \right)
$$
\notes{where $\mappingFunction_{i-1}\left(\inputVector\right)$ is a
low fidelity simulation of the problem of interest and
$\mappingFunction_i\left(\inputVector\right)$ is a higher fidelity
simulation. The function $\delta_i\left(\inputVector \right)$
represents the difference between the lower and higher fidelity
simulation, which is considered additive. The additive form of this
covariance means that if
$\mappingFunction_{0}\left(\inputVector\right)$ and
$\left\{\delta_i\left(\inputVector \right)\right\}_{i=1}^m$ are all
Gaussian processes, then the process over all fidelities of simuation
will be a joint Gaussian process.}

\notes{But with deep Gaussian processes we can consider the form}
$$
\mappingFunction_i\left(\inputVector\right) = \mappingFunctionTwo_{i}\left(\mappingFunction_{i-1}\left(\inputVector\right)\right) + \delta_i\left(\inputVector \right),
$$
\notes{where the low fidelity representation is non linearly transformed by $\mappingFunctionTwo(\cdot)$ before use in the process. This is the approach taken in @Perdikaris:multifidelity17. But once we accept that these models can be composed, a highly flexible framework can emerge. A key point is that the data enters the model at different levels, and represents different aspects. For example these correspond to the two fidelities of the mountain car simulator.}

\notes{We start by sampling both of them at 250 random input locations.}

\setupcode{import gym}
\code{env = gym.make('MountainCarContinuous-v0')}

\setupcode{from emukit.core import ContinuousParameter, ParameterSpace}

\code{position_dynamics_domain = [-1.2, +0.6]
velocity_dynamics_domain = [-0.07, +0.07]
action_dynamics_domain = [-1, +1]

space_dynamics = ParameterSpace(
          [ContinuousParameter('position_dynamics_parameter', *position_dynamics_domain), 
           ContinuousParameter('velocity_dynamics_parameter', *velocity_dynamics_domain),
           ContinuousParameter('action_dynamics_parameter', *action_dynamics_domain)])}

\comment{\setupcode{import GPyOpt}
\code{### --- Collect points from low and high fidelity simulator --- ###

space = GPyOpt.Design_space([
        {'name':'position', 'type':'continuous', 'domain':(-1.2, +1)},
        {'name':'velocity', 'type':'continuous', 'domain':(-0.07, +0.07)},
        {'name':'action', 'type':'continuous', 'domain':(-1, +1)}])

n_points = 250
random_design = GPyOpt.experiment_design.RandomDesign(space)
x_random = random_design.get_samples(n_points)}}

\notes{Next, we evaluate the high and low fidelity simualtors at those locations.}

\setupcode{import numpy as np
import mountain_car as mc}

\code{d_position_hf = np.zeros((n_points, 1))
d_velocity_hf = np.zeros((n_points, 1))
d_position_lf = np.zeros((n_points, 1))
d_velocity_lf = np.zeros((n_points, 1))

# --- Collect high fidelity points
for i in range(0, n_points):
    d_position_hf[i], d_velocity_hf[i] = mc.simulation(x_random[i, :])

# --- Collect low fidelity points  
for i in range(0, n_points):
    d_position_lf[i], d_velocity_lf[i] = mc.low_cost_simulation(x_random[i, :])}

\endif
