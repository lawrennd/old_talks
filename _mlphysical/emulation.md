---
week: 3
session: 1
title: "Emulation"
abstract:  >
  In this lecture we motivate the use of emulation, and introduce the GPy software as a framework for building Gaussian process emulators.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
layout: lecture
time: "12:00"
date: 2021-10-22
youtube: 7Ct_16JicLw
ipynb: true
reveal: true
transition: None
---


\section{Emulation}

\subsection{Surrogate Models and Emulators}

\notes{There are a number of ways we can use machine learning to accelerate scientific discovery. But one way is to have the machine learning model learn the effect of the rules. Rather than worrying about the detail of the rules through computing each step, we can have the machine learning model look to abstract the rules and capture emergent phenomena, just as the Maxwell-Boltzmann distribution captures the essence of the behavior of the ideal gas.}

\notes{In the papers listed above, neural networks are being used to speed up computations. In this course we've introduced Gaussian processes that will be used to speed up these computations. In both cases the ideas are similar. Rather than rerunning the simulation, we use data from the simulation to *fit* the neural network or the Gaussian process to the data.}

\notes{We'll see an example of how this is done in a moment, taken from a simple ride hailing simulator, but before we look at that, we'll first consider why this might be a useful approach.}

\section{Modelling in Practice}

\notes{As we've seen from the very simple rules in the Game of Life, emergent phenomena we might be interested in take computation power to discover, just as Laplace's and Dirac's quotes suggest. The objective in surrogate modelling is to harness machine learning models to learn those physical characteristics.}

\subsection{Types of Simulations}

\notes{We've introduced simulations from the perspective of laws of physics. In practice, many simulations may not directly encode for the laws of physics, but they might encode expert intuitions about a problem. 

For example, in Formula 1 races, the cars have tyres that wear at different rates. Softer tyres allow the cars to drive faster but wear quicker. Harder tyres man the car drives slower but they last longer. Changing between tyres is part of the race, and it has a time penalty. Before each race the teams decide what their strategy will be with tyre changes. It's not only how many tyre changes that are important, but when they happen. If you change your tyre early, you might get a speed advantage and be able to pass your rival when they change their tyre later. This is a trick known as 'undercutting', but if your early change puts you back onto the track behind other slower cars, you will lose this advantage. }

\notes{Formula 1 teams determine their strategy through simulating the race. Each team knows how fast other teams are around the track, and what their top speeds are. So the teams simulate many thousands or millions of races with different strategies for their rivals, and they choose the strategy for which they maximize their number of expected points.}

\notes{When many simulations are done, the results take time to come. During the actual race, the simulations are too slow to provide the real time information teams would need. In this case F1 teams can use emulators, models that have learnt the effect of the simulations, to give real time updates.}

\notes{Formula 1 race simulations contain assumptions that derive from physics but don't directly encode the physical laws. For example, if one car is stuck behind another, in any given lap, it might overtake. A typical race simulation will look at the lap speed of each car and the top speed of each car (as measured in 'speed traps' that are placed on the straight). It will assume a probability of overtake for each lap that is a function of these values. Of course, underlying that function is the physics of how cars overtake each other, but that can be abstracted away into a simpler function that the Race Strategy Engineer defines from their knowledge and previous experience.}

\notes{Many simulations have this characteristic: major parts of the simulation are the result of encoding expert knowledge in the code. But this can lead to challenges. I once asked a strategy engineer, who had completed a new simulation, how it was going. He replied that things had started out well, but over time its performance was degrading. We discussed this for a while and over time a challenge of mispecified granularity emerged.}

\subsection{Fidelity of the Simulation}

\slides{* Simulations work at different fidelities.
     * e.g. difference between strategy simulation in F1 and aerodynamics simulation}

\notes{The engineer explained how there'd been a race where the simulation had suggested that their main driver *shouldn't* pit because he would have emerged behind a car with a slower lap speed, but a high top-speed. This would have made that car difficult to overtake. However, the driver of that slower car was also in the team's 'development program', so everyone in the team knew that the slower car would have moved aside to let their driver through. Unfortunately, the simulation didn't know this. So, the team felt the wrong stategy decision was made. After the race, the simulation was updated to include a special case for this situation. The new code checked whether the slower car was a development driver, making it 'more realistic'.

Over time there were a number of similar changes, each of which should have improved the simulation, but the reality was the code was now 'mixing granularities'. The formula for computing the probability of overtake as a function of speeds is one that is relatively easy to verify. It ignores the relationships between drivers, whether a given driver is a development driver, whether one bears a grudge or not, whether one is fighting for their place in the team. That's all assimilated into the equation. The original equation is easy to calibrate, but as soon as you move to a finer granularity and consider more details about individual drivers, the model seems more realistic, but it becomes difficult to specify, and therefore performance degrades.}

\notes{Simulations work at different fidelities, but as the Formula 1 example shows you must be very careful about mixing fidelities within the same simulation. The appropriate fidelity of a simulation is strongly dependent on the question being asked of it. On the context. For example, in Formula 1 races you can also simulate the performance of the car in the wind tunnel and using computational fluid dynamics represenations of the Navier Stokes equations. That level of fidelity *is* appropriate when designing the aerodynamic components of the car, but inappropriate when building a strategy simulation.}

\section{Epidemiology}

\notes{The same concept of modelling at a particular fidelity comes up in epidemiology. Disease is transmitted by direct person to person interactions between individuals and objects. But in theoretical epidemiology, this is approximated by differential equations. The resulting models look very similar to reaction rate models used in Chemistry for well mixed beakers. Let's have a look at a simple example used for modelling the policy of 'herd immunity' for Covid19.}

\include{_simulation/includes/herd-immunity.md}

\notes{Thinking about our Formula 1 example, and the differing levels of fidelity that might be included in a model, you can now imagine the challenges of doing large scale theoretical epidemiology. The compartment model is operating at a particular level of fidelity. Imagine trying to modify this model for a specific circumstance, like the way that the University of Cambridge chooses to do lectures. It's not appropriate for this level of fidelity. You need to use different types of models for that decision making. Later, we'll look at a simulation that was used to advise the government on the Test Trace Isolate program that took a different approach [@Delve-tti20].}

\section{Strategies for Simulation}

\notes{Within any simulation, we can roughly split the variables of interest into the state variables and the parameters. In the Herd immunity example, the state variables were the different susceptible, exposed, infectious and recovered groups. The parameters were the reproduction number and the expected lengths of infection and the timing of lockdown. Often parameters are viewed as the inputs to the simulation, the things we can control. We might want to know how to time lock down to minimize the number of deaths. This behavior of the simulator is what we may want to emulate with our Gaussian process model.}

\notes{So far, we've introduced simulation motivated by the physical laws of the universe. Those laws are sometimes encoded in differential equations, in which case we can try to solve those systems (like with Herd Immunity or Navier Stokes). An alternative approach is taken in the Game of Life. There a turn-based simulation is used, at each turn, we iterate through the simulation updating the state of the simulation. This is known as a *discrete event simulation*. In race simulation for Formula 1 a discrete event simulation is also used. There is another form of discrete event simulation, often used in Chemical models, where the events don't take place at regular intervals. Instead, the timing to the next event is computed, and the simulator advances that amount of time. For an example of this see [the Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm)}.

\notes{There is a third type of simulation that we'd also like to introduce. That is simulation within computer software. In particular, the need to backtest software with 'what if' ideas, or to trace errors that may have occurred in production. This can involve loading up entire code bases and rerunning them with simulated inputs. This is a third form of simulation where emulation can also come in useful.}

\subsection{Backtesting Production Code}

\notes{In Amazon the team I led looked at examples of simulations and emulation as varied as Prime Air drones across to the Amazon Supply Chain. In a purchasing system, the idea is to store stock to balance supply and demand. The aim is to keep product in stock for quick dispatch while keeping prices (and therefore costs) low. This idea is at the heart of Amazon's focus on customer experience.}

\notes{Modern software development uses an approach known as *service-oriented architecture* to build highly complex systems. Such systems have similar emergent properties to Conway's "Game of Life". Understanding these emergent properties is vitally important when diagnosing problems in the system.}

\notes{In the context of machine learning and complex systems, Jonathan Zittrain has coined the term ["Intellectual Debt"](https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c) to describe the challenge of understanding what you've created.}

\notes{Clearly Conway's Game of Life exhibits an enormous amount of intellectual debt, indeed that was the idea. Build something simple that exhibits great complexity. That's what makes it so popular. But in deployed system software, intellectual debt is a major headache and emulation presents one way of dealing with it.}

\include{_ai/includes/buying-system.md}

\notes{Unfortunately, it also makes sophisticated software systems a breeding ground for intellectual debt. Particularly when they contain components which are themselves ML components. Dealing with this challenge is a major objective of my Senior AI Fellowship at the Alan Turing Institute. You can see me talking about the problems [at this recent seminar given virtually in Manchester](http://inverseprobability.com/talks/notes/deploying-machine-learning-systems-intellectual-debt-and-auto-ai.html).}

<!--[Simpy](https://simpy.readthedocs.io/en/latest/examples/gas_station_refuel.html)

* News Vendor Problem
* Trolley & Pendulum
* Mountain Car
* Hodgkin Huxley 
* Formula One Race
* Plane/F1 Car/Drone
* [Fluid Dynamics](https://github.com/barbagroup/CFDPython) Discretisation of PDEs
* [Stress in a connecting rod](https://solidspy.readthedocs.io/en/latest/readme.html) Discretisation of PDEs
* [Network simulation](https://github.com/mkalewski/sim2net) Discrete Event


* Reaction Rates: 
<>

-->

\section{Related Approaches}

\notes{While this module is mainly focusing on emulation as a route to bringing machine learning closer to the physical world, I don't want to give the impression that's the only approach. It's worth bearing in mind three important domains of machine learning (and statistics) that we also could have explored.}

* Probabilistic Programming
* Approximate Bayesian Computation
* Causal inference

\notes{Each of these domains also brings a lot to the table in terms of understanding the physical world.}

\subsection{Probabilistic Programming}
\slides{* Dates back to BUGS
* Modern descendent (same spirit) is Stan
* Also languages like pyro (based on PyTorch)
}

\notes{Probabilistic programming is an idea that, from our perspective, can be summarized as follows. What if, when constructing your simulator, or your model, you used a programming language that was aware of the state variables and the probability distributions. What if this language could 'compile' the program into code that would automatically compute the Bayesian posterior for you?

This is the objective of probabilistic programming. The idea is that you write your model in a language, and that language is automatically converted into the different modelling codes you need to perform Bayesian inference.

The ideas for probabilistic programming originate in [BUGS](https://www.mrc-bsu.cam.ac.uk/software/bugs/). The software was developed at the MRC Biostatistics Unit here in Cambridge in the early 1990s, by among others, David Spiegelhalter. Carl Henrik covered in last week's lecture some of the approaches for approximate inference. BUGS uses Gibbs sampling. Gibbs sampling, however, can be slow to converge when there are strong correlations in the posterior between variables. 

The descendent of BUGS that is probably most similar in the spirit of its design is [Stan](https://mc-stan.org/). Stan came from researchers at Columbia University and makes use of a variant of Hamiltonian Monte Carlo called the No-U-Turn sampler. It builds on automatic differentiation for the gradients it needs. It's all written in C++ for speed, but has interfaces to Python, R, Julia, MATLAB etc. Stan has been highly successful during the Coronavirus pandemic, with a number of epidemiological simulations written in the language, for example see this [blog post](https://mc-stan.org/users/documentation/case-studies/boarding_school_case_study.html).}

\notes{Other probabilistic programming languages of interest include those that make use of variational approaches (such as [pyro](https://pyro.ai/)) and allow use of neural network components.}

\subsection{Approximate Bayesian Computation}

\notes{We reintroduced Gaussian processes at the start of this lecture by sampling from the Gaussian process and matching the samples to data, discarding those that were distant from our observations. This approach to Bayesian inference is the starting point for *approximate Bayesian computation* or ABC.}

\notes{The idea is straightforward, if we can measure 'closeness' in some relevant fashion, then we can sample from our simulation, compare our samples to real world data through 'closeness measure' and eliminate samples that are distant from our data. Through appropriate choice of closeness measure, our samples can be viewed as coming from an approximate posterior.}

\notes{My Sheffield colleague, Rich Wilkinson, was one of the pioneers of this approach during his PhD in the Statslab here in Cambridge. You can hear Rich talking about ABC at NeurIPS in 2013 here.}

\figure{\includeyoutube{sssbLkn2JjI}{600}{450}}{Rich Wilkinson giving a Tutorial on ABC at NeurIPS in 2013. Unfortunately they've not synchronised the slides with the tutorial. You can find the slides [separately here](http://media.nips.cc/Conferences/2013/Video/Tutorial2B.pdf).}{rich-wilkinson-abc}


\subsection{Causality}

\figure{\includeyoutube{yksduYxEusQ}{600}{450}}{Judea Pearl and Elias Bareinboim giving a Tutorial on Causality at NeurIPS in 2013. Again, the slides aren't synchronised, but you can find them separately [here](http://media.nips.cc/Conferences/2013/nips-dec2013-pearl-bareinboim-tutorial-full.pdf).}{judea-pearl-causality}

\notes{All these approaches offer a lot of promise for developing machine learning at the interface with science but covering each in detail would require four separate modules. We've chosen to focus on the emulation approach, for two principal reasons. Firstly, it's conceptual simplicity. Our aim is to replace all or part of our simulation with a machine learning model. Typically, we're going to want uncertainties as part of that representation. That explains our focus on Gaussian process models. Secondly, the emulator method is flexible. Probabilistic programming requires that the simulator has been built in a particular way, otherwise we can't compile the program. Finally, the emulation approach can be combined with any of the existing simulation approaches. For example, we might want to write our emulators as probabilistic programs. Or we might do causal analysis on our emulators, or we could speed up the simulation in ABC through emulation.} 
\include{_simulation/includes/simulation-system.md}
\include{_data-science/includes/experiment-analyze-design.md}
\include{_uq/includes/emulation.md}

\include{_software/includes/gpy-software.md}
\include{_gp/includes/gpy-tutorial.md}
\include{_gp/includes/gpy-emulation.md}


\include{_uq/includes/emukit-playground.md}

\subsection{Conclusions}

\notes{We summarized the different types of simmulation into roughly three groups. Firstly, those based on physical laws in the form of differential equations. Examples include certain compartmental epidemiological models, climate models and weather models. Secondly, discrete event simulations. These simulations often run to a 'clock', where updates to the state are taken in turns. The Game of Life is an example of this type of simulation, and Formula 1 models of race strategy also use this approach. There is another type of discrete event simulation that doesn't use a turn-based approach but waits for the next event. The [Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm) is an example of such an approach but we didn't cover it here. Finally, we realised that general computer code bases are also simulations. If a company has a large body of code, and particularly if it's hosted within a streaming environment (such as Apache Kafka), it's possible to back test the code with different inputs. Such backtests can be viewed as simulations, and in the case of large bodies of code (such as the code that manages Amazon's automated buying systems) the back tests can be slow and could also benefit from emulation.}

\notes{We've introduced emulation as a way of dealing with different fidelities of simulations and removing the computational demands that come with them. We've highlighted how emulation can be deployed and introduced the `GPy` software for Gaussian process modelling.}

\slides{* Characterised types of simulation.
    * Physical laws
	* Discrete event
	* Production Software Systems
* Introduced notion of emulation to replace simulation.
* Overviewed GPy software.}

\thanks

\reading

\references

