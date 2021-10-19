\ifndef{herdImmunity}
\define{herdImmunity}

\editme

\subsection{Modelling Herd Immunity}

\notes{This example is taken from [Thomas House's blog post](https://personalpages.manchester.ac.uk/staff/thomas.house/blog/modelling-herd-immunity.html) on Herd Immunity. This model was shared at the beginning of the Covid19 pandemic when the first UK lockdown hadn't yet occurred.}



\note{The model is a [compartmental differential equation](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) model. It assumes three groups: Susceptible, Infectious or Recovered. These groups are considered to be 'well mixed'. If they are well mixed, and the numbers are large, then the stochastic nature of transmission can be ignored and the disease numbers can be modelled by a set of stochastic differential equations.

} 

\setupcode{import numpy as np
from scipy import integrate}

\notes{The next piece of code sets up the dynamics of the compartmental model. He doesn't give the specific details in the blog post, but my understanding is that the four states are as follows. `x[0]` is the susceptible population, those that haven't had the disease yet. The susceptible population decreases by encounters with infections people. In Thomas's model, both `x[3]` and `x[4]` are infections. So the dynamics of the reduction of the susceptible is given by}
$$
\frac{\text{d}{S}}{\text{d}t} = - \beta S (I_1 + I_2).
$$
\notes{Here, we've used $I_1$ and $I_2$ to represent what appears to be two separate infectious compartments in Thomas's model. We'll speculate about why there are two in a moment.

The model appears to be an SEIR model, so rather than becoming infectious directly you next move to an 'exposed', where you have the disease, but you are not yet infectious. There are again *two* exposed states, we'll return to that in a moment. We denote the first, `x[1]` by $E_1$. We have}
$$
\frac{\text{d}{E_1}}{\text{d}t} = \beta S (I_1 + I_2) - \sigma E_1.
$$
\notes{Note that the first term matches the term from the Susceptible equation. This is because it is the incoming exposed population.

The exposed population move to a second compartment of exposure, $E_2$. I believe the reason for this is that if you use only one exposure compartment, then the statistics of the duration of exposure are incorrect (implicitly they are exponentially distributed in the underlying stochastic version of the model). By using two exposure departments, Thomas is making a slight correction to this which would impose a first order gamma distribution on those statistics. A similar trick is being deployed for the 'infectious group'. So we gain an additional equation to help with these statistics,}\newslide{}
$$
\frac{\text{d}{E_2}}{\text{d}t} = \sigma E_1 - \sigma E_2.
$$
\notes{giving us the exposed group as the sum of the two compartments $E_1$ and $E_2$. The exposed group from the second compartment then become 'infected', which we represent with $I_1$, in the code this is `x[3]`,}
$$
\frac{\text{d}{I_1}}{\text{d}t} = \sigma E_2 - \gamma I_1,
$$
\notes{and similarly, Thomas is using a two-compartment infectious group to fix up the duration model. So we have,}
$$
\frac{\text{d}{I_2}}{\text{d}t} = \gamma I_1 - \gamma I_2.
$$
\notes{And finally, we have those that have recovered emerging from the second infections compartment. In this model there is no separate model for 'deaths', so the recovered compartment, $R$, would also include those that die,}
$$
\frac{\text{d}R}{\text{d}t} = \gamma I_2.
$$
\notes{All of these equations are then represented in code as follows.}

\code{def odefun(t,x,beta0,betat,t0,t1,sigma,gamma):
    dx = np.zeros(6)
    if ((t>=t0) and (t<=t1)):
        beta = betat
    else:
        beta = beta0
    dx[0] = -beta*x[0]*(x[3] + x[4])
    dx[1] = beta*x[0]*(x[3] + x[4]) - sigma*x[1]
    dx[2] = sigma*x[1] - sigma*x[2]
    dx[3] = sigma*x[2] - gamma*x[3]
    dx[4] = gamma*x[3] - gamma*x[4]
    dx[5] = gamma*x[4]
    return dx}

\notes{Where the code takes in the states of the compartments (the values of `x`) and returns the gradients of those states for the provided parameters (`sigma`, `gamma` and `beta`). Those parameters are set according to the known characteristics of the disease.}

\notes{The next block of code sets up the parameters of the SEIR model. A particularly important parameter is the reproduction number ($R_0$), here Thomas has assumed a reproduction number of 2.5, implying that each infected member of the population transmits the infection up to 2.5 other people. The effective $R$ decreases over time though, because some of those people they meet will no longer be in the susceptible group.}

\code{# Parameters of the model
N = 6.7e7 # Total population
i0 = 1e-4 # 0.5*Proportion of the population infected on day 0
tlast = 365.0 # Consider a year
latent_period = 5.0 # Days between being infected and becoming infectious
infectious_period = 7.0 # Days infectious
R0 = 2.5 # Basic reproduction number in the absence of interventions
Rt = 0.75 # Reproduction number in the presence of interventions
tend = 21.0 # Number of days of interventions}

\notes{The parameters are correct for the 'discrete system', where the infectious period is a discrete time, and the numbers are discrete values. To translate into our continuous differential equation system's parameters, we need to do a couple of manipulations. Note the factor of 2 associated with `gamma` and `sigma`. This is a doubling of the rate to account for the fact that there are two compartments for each of these states (to fix-up the statistics of the duration models).}

\code{beta0 = R0 / infectious_period
betat = Rt / infectious_period
sigma = 2.0 / latent_period
gamma = 2.0 / infectious_period}

\notes{Next, we solve the system using `scipy`'s initial value problem solver. The solution method is "Runge-Kutta-Fehlberg method, as indicated by the `'RK45'` solver. This is a numerical method for solving differential equations. The 45 is the order of the method and the error estimator.

We can view the solver itself as somehow a piece of simulation code, but here it's being called as sub routine in the system. It returns a solution for each time step, stored in a list `sol`.}

\notes{This is typical of this type of non-linear differential equation problem. Whether it's partial differential equations, ordinary differential equations, there's a step where a numerical solver needs to be called. These are often expensive to run. For climate and weather models, this would be where we solved the Navier-Stokes equations. For this simple model, the solution is relatively quick.}

\code{
t0ran = np.array([-100, 40, 52.5, 65])
sol=[]
for tt in range(0,len(t0ran)):
    sol.append(integrate.solve_ivp(lambda t,x: odefun(t,x,beta0,betat,t0ran[tt],t0ran[tt]+tend,sigma,gamma),
                              (0.0,tlast),
                              np.array([1.0-2.0*i0, 0.0, 0.0, i0, i0, 0.0]),
                              'RK45',
                              atol=1e-8,
                              rtol=1e-9))}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{def mylab(t):
    if t>0:
        return "Start at " + str(t) + " days"
    else:
        return "Baseline"}


\plotcode{fig, ax = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
for tt in range(0,len(t0ran)):
    ax[0].plot(sol[tt].t,N*(sol[tt].y[3] + sol[tt].y[4]).T, label=mylab(t0ran[tt]))
ax[0].set_xlim([30,70])
ax[0].set_ylim([0,7e6])
ax[0].set_xlabel('Time (days)')
ax[0].set_ylabel('Number of infectious cases')
ax[0].legend()
for tt in range(0,len(t0ran)):
    ax[1].plot(sol[tt].t,N*sol[tt].y[5].T, label=mylab(t0ran[tt]))
ax[1].set_xlim([30,70])
ax[1].set_ylim([0,1e7])
ax[1].set_xlabel('Time (days)')
ax[1].set_ylabel('Cumulative infections')
ax[1].legend()

mlai.write_figure('house-model-zoom.svg', directory='\writeDiagramsDir/simulation')}

\newslide{}

\figure{\includediagram{\diagramsDir/simulation/house-model-zoom}{80%}}{A zoomed in version of Thomas House's variation on the SEIR model for evaluating the effect of early interventions.}{house-model-zoom}

\plotcode{fig, ax = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
for tt in range(0,len(t0ran)):
    ax[0].plot(sol[tt].t,N*(sol[tt].y[3] + sol[tt].y[4]).T, label=mylab(t0ran[tt]))
ax[0].set_xlim([0,tlast])
ax[0].set_ylim([0,1.2e7])
ax[0].set_xlabel('Time (days)')
ax[0].set_ylabel('Number of infectious cases')
ax[0].legend()
for tt in range(0,len(t0ran)):
    ax[1].plot(sol[tt].t,N*sol[tt].y[5].T, label=mylab(t0ran[tt]))
ax[1].set_xlabel('Time (days)')
ax[1].set_ylabel('Cumulative infections')
ax[1].legend()
ax[1].set_xlim([0,tlast])
ax[1].set_ylim([0,6.2e7])

mlai.write_figure('house-model-full.svg', directory='\writeDiagramsDir/simulation/')}

\newslide{}

\figure{\includediagram{\diagramsDir/simulation/house-model-full}{80%}}{The full progress of the disease in Thomas House's variation on the SEIR model for evaluating the effect of early interventions.}{house-model-full}

\notes{In practice, immunity for Covid19 may only last around 6 months. As an exercise, try to extend Thomas's model for the case where immunity is temporary. You'll need to account for deaths as well in your new model.}

\endif
