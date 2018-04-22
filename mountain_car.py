import os
import numpy as np

import matplotlib.pyplot as plt

import GPyOpt
from GPyOpt.acquisitions import AcquisitionBase
import GPy

from matplotlib import animation
from IPython.display import display, HTML
from pylab import cm

import teaching_plots as plot
import mlai

N_STEPS_MAX = 500


    
def make_multi_output_multi_fidelity_kernel(input_dim):
    k_simulator = GPy.kern.Matern52(input_dim = input_dim, active_dims = list(range(input_dim)), ARD=True)
    k_error = GPy.kern.Matern52(input_dim = input_dim, active_dims = list(range(input_dim)), ARD=True)
    k_indicator = GPy.kern.Linear(input_dim = 1, active_dims = [input_dim]) 
    # Some constraints on hyperparameters
    k_indicator.variances.constrain_fixed(1)
    k_indicator.variances.fix(1)
    k_simulator.variance.constrain_bounded(1e-4, 10)
    k_error.variance.constrain_bounded(1e-4, 10)
    k_simulator.lengthscale.constrain_bounded(1e-4, 10)
    k_error.lengthscale.constrain_bounded(1e-4, 10)
    return k_simulator + k_indicator*k_error

def simulation(state):
    """Define a low fidelity simulation that returns the approximate car dynamics"""
    power = 0.0015
    max_speed = 0.07
    min_position = -1.2
    max_position = 0.6
    position = state[0]
    velocity = state[1]
    action = state[2]
    new_velocity = velocity + power*action - 0.0025*np.cos(3*position)
    new_velocity = np.clip(new_velocity, -max_speed, max_speed)
    d_velocity = new_velocity - velocity
    new_position = position + new_velocity
    new_position = np.clip(new_position, min_position, max_position)
    d_position = new_position-position
    return d_position, d_velocity

def low_cost_simulation(state):
    """Define a low fidelity simulation that returns the approximate car dynamics"""
    # A corrupted version of the function above
    power = 0.002
    max_speed = 0.07
    min_position = -1.2
    max_position = 0.6
    position = state[0]
    velocity = state[1]
    action = state[2]
    d_velocity = power*action - 0.004*(np.cos(3.3*position - 0.3))**2 - 0.001
    d_position = d_velocity
    return d_position, d_velocity

class AcquisitionPE(AcquisitionBase):
    """
    Pure Exploration acquisition function

    :param model: GPyOpt class of model
    :param space: GPyOpt class of domain
    :param optimizer: optimizer of the acquisition. Should be a GPyOpt optimizer
    :param cost_withGradients: function
    :param jitter: positive value to make the acquisition more explorative

    .. Note:: does not allow to be used with cost

    """
    analytical_gradient_prediction = True

    def __init__(self, model, space, optimizer=None, cost_withGradients=None):
        self.optimizer = optimizer
        super(AcquisitionPE, self).__init__(model, space, optimizer, cost_withGradients=cost_withGradients)

    def _compute_acq(self, x):
        """
        Computes the GP-Lower Confidence Bound 
        """
        _, s = self.model.predict(x)   
        return s

    def _compute_acq_withGradients(self, x):
        """
        Computes the GP-Lower Confidence Bound and its derivative
        """
        _, s, _, dsdx = self.model.predict_withGradients(x) 
        f_acqu = s       
        df_acqu = dsdx
        return f_acqu, df_acqu


def run_simulation(env, controller_gains, render=False):
    # Reset environment to starting point
    env.seed(0)
    observation = env.reset()
    
    # Initalise matrices to store state + control inputs
    state_trajectory = np.ndarray((0, observation.shape[0]))
    control_inputs = np.ndarray((0, env.action_space.shape[0]))
    frames = []
    cost = 0
    for i in range(0, N_STEPS_MAX):
        # Calculate control input
        control_input = calculate_linear_control(observation, controller_gains)
        if render:
            frames.append(env.render(mode='rgb_array'))
        # Save current state + control
        state_trajectory = np.concatenate([state_trajectory, observation[np.newaxis, :]], axis=0)
        control_inputs = np.concatenate([control_inputs, control_input[np.newaxis, :]])

        observation, reward, done, info = env.step(control_input)
        cost -= (reward - 1)
        if done:
            state_trajectory = np.concatenate([state_trajectory, observation[np.newaxis, :]], axis=0)
            return cost, state_trajectory, control_inputs, frames
    return cost, state_trajectory, control_inputs, frames


def run_emulation(dynamics_models, controller_gains, X_0, fidelity='single'):
    observation = X_0.copy()
    state_trajectory = np.ndarray((0, observation.shape[0]))*np.nan
    control_inputs = np.ndarray((0, 1))*np.nan
    cost = 0

    for _ in range(0, N_STEPS_MAX):
        # Evalute controller
        control_input = calculate_linear_control(observation, controller_gains)
        cost += (np.power(control_input[0], 2)*0.1 + 1)
        # Store state + control
        state_trajectory = np.concatenate([state_trajectory, observation[np.newaxis, :]], axis=0)
        control_inputs = np.concatenate([control_inputs, control_input[np.newaxis, :]])
        
        # Evalute emulator
        gp_input = np.hstack([observation, control_input])[np.newaxis, :]
        next_state_mean = evalute_model(dynamics_models[0], gp_input, fidelity)
        observation[0] += next_state_mean
        next_state_mean = evalute_model(dynamics_models[1], gp_input, fidelity)
        observation[1] += next_state_mean

        if observation[0] > 0.45:
            state_trajectory = np.concatenate([state_trajectory, observation[np.newaxis, :]], axis=0)
            return cost-100, state_trajectory, control_inputs
    return cost, state_trajectory, control_inputs


def calculate_linear_control(state, gains):
    control_input = (np.dot(gains[0, 0:2], state) + gains[0, 2])[np.newaxis]
    return np.clip(control_input, -1, 1)


def add_data_to_gp(gp_model, new_x, new_y):
    all_X = np.concatenate([gp_model.X, new_x])
    all_y = np.concatenate([gp_model.Y, new_y])
    gp_model.set_XY(all_X, all_y)
    return gp_model

def make_gp_inputs(control_inputs, state_trajectory):
    X = np.concatenate([state_trajectory[:-1, :], control_inputs], axis=1)
    y = np.diff(state_trajectory, axis=0)
    return X, y


def v_simulation(state):
    state = state.copy().flatten()
    power = 0.0015
    max_speed = 0.07
    min_position = -1.2
    max_position = 0.6
    position = state[0]
    velocity = state[1]
    action = state[2]
    new_velocity = velocity + power*action - 0.0025*np.cos(3*position)
    new_velocity = np.clip(new_velocity, -max_speed, max_speed)
    d_velocity = new_velocity - velocity
    new_position = position + new_velocity
    new_position = np.clip(new_position, min_position, max_position)
    d_position = new_position-position
    return np.asarray([d_velocity])[np.newaxis, :]

class plot_control(object):
    def __init__(self, velocity_emulator, fidelity='single'):
        self.velocity_emulator = velocity_emulator
        self.fidelity = fidelity

    def plot_slices(self, control):
        n_points_contour = 50
        position_contour = np.linspace(-1.2, 0.6, n_points_contour)
        velocity_contour = np.linspace(-0.07, 0.07, n_points_contour)
        x_contour_grid = np.meshgrid(position_contour, velocity_contour)
        x_contour = np.ones((n_points_contour**2, 3))*control
        for i in range(0, len(x_contour_grid)):
            x_contour[:, i] = x_contour_grid[i].flatten()
        
        # Evalute emulator
        y_emulator = evalute_model(self.velocity_emulator, x_contour, self.fidelity)
        
        # Evalute simulator
        y_simulator = np.zeros(x_contour.shape[0])
        for i in range(0, x_contour.shape[0]):
            y_simulator[i] = v_simulation(x_contour[i, :])
        
        # Do plots
        fig, ax = plt.subplots(1, 2, figsize=(12, 4))
        ax[0].set_title('Acceleration from Emulator')
        ax[0].contourf(position_contour, velocity_contour, np.reshape(y_emulator, (n_points_contour, n_points_contour)),cmap=cm.RdBu)
        ax[1].set_title('Acceleration from Simulator')
        ax[1].contourf(position_contour, velocity_contour, np.reshape(y_simulator, (n_points_contour, n_points_contour)),cmap=cm.RdBu)
        plt.tight_layout()
        ax[1].set_xlabel('Car Position')
        #ax[1].set_ylabel('Car Velocity')
        ax[0].set_xlabel('Car Position')
        ax[0].set_ylabel('Car Velocity')


def evalute_deep_multi_fidelity(models, x):
    y_lf = models[0].predict(x)[0]
    x_hf = np.hstack((x.copy(), y_lf))
    return models[1].predict(x_hf)[0]

def evalute_model(model, x, fidelity):
    # Evalute emulator
    if fidelity == 'single':
        y = model.predict(x)[0]
    elif fidelity == 'multi-linear':
        x_extended = np.hstack([x, np.ones([x.shape[0], 1])])
        y = model.predict(x_extended)[0]
    elif fidelity == 'multi-deep':
        y = evalute_deep_multi_fidelity(model, x)
    return y


def create_deep_multi_fidelity_models(x, y1, y2):
    """
    Function to create deep multi-fidelity models
    """
    m1 = GPy.models.GPRegression(x.copy(), y1, kernel=GPy.kern.RBF(3))
    m1.optimize_restarts(10, verbose=False);
    mu1, _ = m1.predict(x)
    XX = np.hstack((x.copy(), mu1))
    
    ## Make second model
    n_dim = x.shape[1]
    k2 = GPy.kern.RBF(1, active_dims = [n_dim])*GPy.kern.RBF(n_dim, active_dims=np.arange(0, n_dim)) \
        + GPy.kern.RBF(n_dim, active_dims=np.arange(0, n_dim))
    m2 = GPy.models.GPRegression(XX, y2, kernel=k2)
    m2.optimize_restarts(10, verbose=False)
    return m1, m2

def animate_frames(frames, title=None):
    """
    Converts a list of frames to an animation.
    """
    fig, ax = plt.subplots(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi = 72)
    fig.set_alpha(0.0)
    if title is None:
        ax.set_position([0, 0, 1, 1])
    else:
        ax.set_title(title)
    ax.set_alpha(0.0)
    patch = ax.imshow(frames[0])
    
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])
        
    return animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=30)
    #HTML(anim.to_jshtml())##display(display_animation(anim, default_mode='loop'))
    #HTML(anim.to_html5_video())##display(display_animation(anim, default_mode='loop'))


def emu_sim_comparison(env, control_params, emulator, fidelity='single', max_steps=500, diagrams='../diagrams'):
    """Plot a comparison between the emulator and the simulator"""
    reward, state_trajectory, control_inputs, _ = run_simulation(env, control_params)
    
    reward_emu, state_trajectory_emu_mean, control_inputs_emu_mean = run_emulation(
        emulator, control_params, state_trajectory[0, :].copy(), fidelity=fidelity)

    fig, ax = plt.subplots(1, 3, figsize=plot.three_figsize)
    x_axis = np.arange(0, max_steps)
    x_axis_emu = np.arange(0, max_steps)
    h1, = ax[0].plot(state_trajectory_emu_mean[:, 0])

    h2, = ax[0].plot(state_trajectory[:, 0])
    ax[0].set_title('Position')
    ax[1].plot(state_trajectory_emu_mean[:,1])
    ax[1].plot(state_trajectory[:,1])
    ax[1].set_title('Velocity')

    ax[2].plot(control_inputs_emu_mean)
    ax[2].plot(control_inputs)
    ax[2].set_title('Control Input')
    fig.legend([h1,h2], ['Emulation', 'Simulation'], loc=4)
    plt.tight_layout()
    plt.show()
    file_name = 'emu_sim_comparison.svg'
    mlai.write_figure(os.path.join(diagrams, file_name),
                      figure=fig,
                      transparent=True)

def invert_frames(frames):
    inverted = []
    for fr in frames:
        fr = fr/255.
        shp = fr[:, :, 0].shape
        a=np.ones(shp)
        #a[np.logical_and(np.logical_and(fr[:, :, 0]==1.0,fr[:, :, 1]==1.0), fr[:, :, 2]==1.0)]=0.0
        fr = (1.0-fr)
        frn = np.zeros(shp + (4,))
        frn[:, :, :3] = fr
        frn[:, :, 3] = a
        inverted.append(frn)
    return inverted


def save_frames(frames, filename, diagrams='../diagrams', inverted=True):
    if inverted:
        frames = invert_frames(frames)
    anim=animate_frames(frames)
    plot.save_animation(anim, filename, diagrams)
