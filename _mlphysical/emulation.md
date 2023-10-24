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
date: 2023-10-24
youtube: Zw2es1Khu_c
oldyoutube:
- code: Zw2es1Khu_c
  year: 2022
- code: 2-kB5J_pfno
  year: 2021
- code: 7Ct_16JicLw
  year: 2020
ipynb: true
reveal: true
featured_image: slides/diagrams/uq/emukit-playground-bayes-opt.png
transition: None
---


\include{_notebooks/includes/plot-setup.md}
\include{_software/includes/notutils-software.md}
\include{_software/includes/mlai-software.md}

\section{Emulation}


\notes{There are a number of ways we can use machine learning to accelerate scientific discovery. But one way is to have the machine learning model learn the effect of the rules. Rather than worrying about the detail of the rules through computing each step, we can have the machine learning model look to abstract the rules and capture emergent phenomena, just as the Maxwell-Boltzmann distribution captures the essence of the behavior of the ideal gas.}

\notes{In the papers listed above, neural networks are being used to speed up computations. In this course we've introduced Gaussian processes that will be used to speed up these computations. In both cases the ideas are similar. Rather than rerunning the simulation, we use data from the simulation to *fit* the neural network or the Gaussian process to the data.}

\notes{We'll see an example of how this is done in a moment, taken from a simple ride hailing simulator, but before we look at that, we'll first consider why this might be a useful approach.}

\section{Surrogate Modelling in Practice}

\slides{* Emergent phenomena require computational power.
* In surrogate modelling we use statistical/ML models to learn regularities in those emergent phenomena.}
\notes{As we've seen from the very simple rules in the Game of Life, emergent phenomena we might be interested in take computation power to discover, just as Laplace's and Dirac's quotes suggest. The objective in surrogate modelling is to harness machine learning models to learn those physical characteristics.}

\subsection{Types of Simulations}

\slides{* Simulation can be differential equation models
  * Either abstracted (like epidemilogical models).
  * Or fine-grained (like climate/weather).
* Discrete event simulations
  * Either turn based (e.g. Game of Life or F1 Strategy Simulations)
  * Or Event based (e.g. Gillespie algorithm for chemical models}

\notes{We've introduced simulations from the perspective of laws of physics. In practice, many simulations may not directly encode for the laws of physics, but they might encode expert intuitions about a problem. 

For example, in Formula 1 races, the cars have tyres that wear at different rates. Softer tyres allow the cars to drive faster but wear quicker. Harder tyres man the car drives slower but they last longer. Changing between tyres is part of the race, and it has a time penalty. Before each race the teams decide what their strategy will be with tyre changes. It's not only how many tyre changes that are important, but when they happen. If you change your tyre early, you might get a speed advantage and be able to pass your rival when they change their tyre later. This is a trick known as 'undercutting', but if your early change puts you back onto the track behind other slower cars, you will lose this advantage. }

\notes{Formula 1 teams determine their strategy through simulating the race. Each team knows how fast other teams are around the track, and what their top speeds are. So, the teams simulate many thousands or millions of races with different strategies for their rivals, and they choose the strategy for which they maximize their number of expected points.}

\notes{When many simulations are done, the results take time to come. During the actual race, the simulations are too slow to provide the real time information teams would need. In this case F1 teams can use emulators, models that have learnt the effect of the simulations, to give real time updates.}

\notes{Formula 1 race simulations contain assumptions that derive from physics but don't directly encode the physical laws. For example, if one car is stuck behind another, in any given lap, it might overtake. A typical race simulation will look at the lap speed of each car and the top speed of each car (as measured in 'speed traps' that are placed on the straight). It will assume a probability of overtake for each lap that is a function of these values. Of course, underlying that function is the physics of how cars overtake each other, but that can be abstracted away into a simpler function that the Race Strategy Engineer defines from their knowledge and previous experience.}

\notes{Many simulations have this characteristic: major parts of the simulation are the result of encoding expert knowledge in the code. But this can lead to challenges. I once asked a strategy engineer, who had completed a new simulation, how it was going. He replied that things had started out well, but over time its performance was degrading. We discussed this for a while and over time a challenge of mis-specified granularity emerged.}

\subsection{Fidelity of the Simulation}

\slides{* Simulations work at different fidelities.
     * e.g. difference between strategy simulation in F1 and aerodynamics simulation}

\notes{The engineer explained how there'd been a race where the simulation had suggested that their main driver *shouldn't* pit because he would have emerged behind a car with a slower lap speed, but a high top-speed. This would have made that car difficult to overtake. However, the driver of that slower car was also in the team's 'development program', so everyone in the team knew that the slower car would have moved aside to let their driver through. Unfortunately, the simulation didn't know this. So, the team felt the wrong stategy decision was made. After the race, the simulation was updated to include a special case for this situation. The new code checked whether the slower car was a development driver, making it 'more realistic'.

Over time there were a number of similar changes, each of which should have improved the simulation, but the reality was the code was now 'mixing granularities'. The formula for computing the probability of overtake as a function of speeds is one that is relatively easy to verify. It ignores the relationships between drivers, whether a given driver is a development driver, whether one bears a grudge or not, whether one is fighting for their place in the team. That's all assimilated into the equation. The original equation is easy to calibrate, but as soon as you move to a finer granularity and consider more details about individual drivers, the model seems more realistic, but it becomes difficult to specify, and therefore performance degrades.}

\notes{Simulations work at different fidelities, but as the Formula 1 example shows you must be very careful about mixing fidelities within the same simulation. The appropriate fidelity of a simulation is strongly dependent on the question being asked of it. On the context. For example, in Formula 1 races you can also simulate the performance of the car in the wind tunnel and using computational fluid dynamics representations of the Navier-Stokes equations. That level of fidelity *is* appropriate when designing the aerodynamic components of the car, but inappropriate when building a strategy simulation.}

\section{Epidemiology}

\notes{The same concept of modelling at a particular fidelity comes up in epidemiology. Disease is transmitted by direct person to person interactions between individuals and objects. But in theoretical epidemiology, this is approximated by differential equations. The resulting models look very similar to reaction rate models used in Chemistry for well mixed beakers. Let's have a look at a simple example used for modelling the policy of 'herd immunity' for Covid19.}

\include{_simulation/includes/herd-immunity.md}

\notes{Thinking about our Formula 1 example, and the differing levels of fidelity that might be included in a model, you can now imagine the challenges of doing large scale theoretical epidemiology. The compartment model is operating at a particular level of fidelity. Imagine trying to modify this model for a specific circumstance, like the way that the University of Cambridge chooses to do lectures. It's not appropriate for this level of fidelity. You need to use different types of models for that decision making. [One of our case studies](https://mlatcl.github.io/mlphysical/casestudies/tti-explorer.html) looks at a simulation that was used to advise the government on the Test Trace Isolate program that took a different approach [@Delve-tti20].}

\section{Strategies for Simulation}

\slides{* Split variables into *state variables*, *parameters* and *results*.
* In herd immunity
  * State variables: susceptible, exposed, infectious, recovered.
  * Parameters: reproduction number, expected lengths of infection, lockdown timings.
  * Results: e.g. total number of deaths}

\newslide{Strategies for Simulation}

\slides{* Use emulator to map from e.g. parameters to total number of deaths.
* Treat parameters and results of simulator as inputs and outputs for emulator.}

\notes{Within any simulation, we can roughly split the variables of interest into the state variables and the parameters. In the Herd immunity example, the state variables were the different susceptible, exposed, infectious and recovered groups. The parameters were the reproduction number and the expected lengths of infection and the timing of lockdown. Often parameters are viewed as the inputs to the simulation, the things we can control. We might want to know how to time lock down to minimize the number of deaths. This behavior of the simulator is what we may want to emulate with our Gaussian process model.}

\notes{So far, we've introduced simulation motivated by the physical laws of the universe. Those laws are sometimes encoded in differential equations, in which case we can try to solve those systems (like with Herd Immunity or Navier Stokes). An alternative approach is taken in the Game of Life. There a turn-based simulation is used, at each turn, we iterate through the simulation updating the state of the simulation. This is known as a *discrete event simulation*. In race simulation for Formula 1 a discrete event simulation is also used. There is another form of discrete event simulation, often used in chemical models, where the events don't take place at regular intervals. Instead, the timing to the next event is computed, and the simulator advances that amount of time. For an example of this see [the Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm)}.

\notes{There is a third type of simulation that we'd also like to introduce. That is simulation within computer software. In particular, the need to backtest software with 'what if' ideas, or to trace errors that may have occurred in production. This can involve loading up entire code bases and rerunning them with simulated inputs. This is a third form of simulation where emulation can also come in useful.}

\subsection{Backtesting Production Code}

\slides{* Third type of simulation.
* Counterfactual running of system code.}

\notes{In Amazon the team I led looked at examples of simulations and emulation as varied as Prime Air drones across to the Amazon Supply Chain. In a purchasing system, the idea is to store stock to balance supply and demand. The aim is to keep product in stock for quick dispatch while keeping prices (and therefore costs) low. This idea is at the heart of Amazon's focus on customer experience.}

\include{_ai/includes/alexa-system.md}
\include{_ai/includes/prime-air-system.md}
\include{_ai/includes/supply-chain-system.md}
\include{_ai/includes/buying-system.md}

\notes{Clearly Conway's Game of Life exhibits an enormous amount of intellectual debt, indeed that was the idea. Build something simple that exhibits great complexity. That's what makes it so popular. But in deployed system software, intellectual debt is a major headache and emulation presents one way of dealing with it.}


\notes{Unfortunately, it also makes sophisticated software systems a breeding ground for intellectual debt. Particularly when they contain components which are themselves ML components. Dealing with this challenge is a major objective of my Senior AI Fellowship at the Alan Turing Institute. You can see me talking about the problems [at this recent seminar given virtually in Manchester](http://inverseprobability.com/talks/notes/deploying-machine-learning-systems-intellectual-debt-and-auto-ai.html).}

\subsection{Examples in Python}


\notes{There are a number of different simulations available in python, and tools specifically design for simulation. For example `simpy` has a [list of example simulations](https://simpy.readthedocs.io/en/latest/examples/) around machine shops, gas stations, car washes.}
\slides{
* [Simpy](https://simpy.readthedocs.io/en/latest/examples/gas_station_refuel.html)}

\notes{Operations research ideas like the newsvendor problem, can also be solved, Andrea Fabry provides an example of the newsvendor problem in python for order of [NFL replica jerseys here](https://github.com/fabryandrea/newsvendor).}
\slides{
* [News Vendor Problem](https://github.com/fabryandrea/newsvendor) in python (for ordering NFL Replica Jerseys.}

\notes{The news vendor problem is also a component in the Amazon supply chain. The Amazon supply chain makes predictions about supply and demand, combines them with a cost basis and computes optimal stock. Inventory orders are based on the difference between this optimal stock and current stock. The [MiniSCOT simulation](https://github.com/amzn/supply-chain-simulation-environment) provides code that illustrates this.}
\slides{
* [Amazon Supply Chain](https://github.com/amzn/supply-chain-simulation-environment)}

\notes{Control problems are also systems that aim to achieve objectives given a set of parameters. A classic control problem is the inverted pendulum. This [python code](https://www.moorepants.info/blog/npendulum.html) generalises the standard inverted pendulum using one with $n$-links using symbolic python code.}
\slides{
* [Trolley & Pendulum](https://www.moorepants.info/blog/npendulum.html) using sympy (symbolic python)}

\newslide{Examples in Python}

\notes{In reinforcement learning similar control problems are studied, a classic reinforcement learning problem is known as the [Mountain Car](https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py). You can work with this problem using an environment known as [OpenAI gym](https://github.com/openai/gym) that includes many different reinforcement learning scenarios.}
\slides{
* [Mountain Car](https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py) in the OpenAI Gym.
}

\notes{In neuroscience Hodgkin and Huxley studied the giant axon in squid to work out a set of differential equations that are still used today to model spiking neurons. Mark Kramer explains how to [simulate them in python here](https://mark-kramer.github.io/Case-Studies-Python/HH.html).}
\slides{
* [Hodgkin Huxley](https://mark-kramer.github.io/Case-Studies-Python/HH.html) by Mark Kramer.}

\notes{All Formula One race teams simulate the race to determine their strategy (tyres, pit stops etc). While those simulations are proprietary, there is sufficient interest in the wider community that race simulations have been developed in python. Here is [one that Nick Roth has made available](https://github.com/rothnic/formulapy).}
\slides{
* [Formula One Race Simulation in Python](https://github.com/rothnic/formulapy) by Nick Roth.}

\notes{Formula one teams also make use of simulation to design car parts. There are at least two components to this, simulations that allow the modelling of fluid flow across the car, and simulations that analyze the capabilities of materials under stress. You can find computational [fluild dynamics simulations in python here](https://github.com/barbagroup/CFDPython) and [finite element analysis methods for computing stress in materials here](https://solidspy.readthedocs.io/en/latest/readme.html).}
\slides{* [Fluid Dynamics](https://github.com/barbagroup/CFDPython) Discretisation of PDEs
* [Stress in a connecting rod](https://solidspy.readthedocs.io/en/latest/readme.html) Discretisation of PDEs
}

\notes{Alongside continuous system simulation through partial differential equations, another form of simulation that arises is known as *discrete event simulation*. This comes up in c[omputer networks](https://github.com/mkalewski/sim2net) and also in chemical systems where the approach to simulating is kown as the [Gillespie algorithm](https://github.com/karinsasaki/gillespie-algorithm-python/).}

\slides{
* [Network simulation](https://github.com/mkalewski/sim2net) Discrete Event simulation.
* [Gillespie Algorithm](https://github.com/karinsasaki/gillespie-algorithm-python/) notebook (in Python 2.7).}




\include{_simulation/includes/simulation-system.md}
\include{_data-science/includes/experiment-analyze-design.md}
\include{_simulation/includes/packing-problems.md}
\subsection{Modelling with a Function}

\notes{What if the question of interest was quite simple, for example in the packing problem, we just wanted to know the minimum side length. Sometimes, regardless of the complexity of the problem, there can be a pattern to the answer that is emergent due to regularities in the underlying problem.}

\slides{* What if question of interest is simple?
* For example in packing problem: what is minimum side length?}

\include{_gp/includes/erich-friedman-packing-gp.md}

\include{_uq/includes/emulation.md}

\include{_software/includes/gpy-software.md}
\include{_gp/includes/gpy-tutorial.md}
\include{_gp/includes/gpy-emulation.md}


\include{_uq/includes/emukit-playground.md}

\notes{\codeassignment{You now know enough to build a simple emulation. To test your knowledge have a go at cobmining GPy with Thomas House's herd immunity simulation. Can you build a Gaussian process emulator of the simulation? Don't spent do long on this exercise. The idea is just to consolidate things like what the inputs and outputs should be.}}

\subsection{Conclusions}

\notes{We summarized the different types of simulation into roughly three groups. Firstly, those based on physical laws in the form of differential equations. Examples include certain compartmental epidemiological models, climate models and weather models. Secondly, discrete event simulations. These simulations often run to a 'clock', where updates to the state are taken in turns. The Game of Life is an example of this type of simulation, and Formula 1 models of race strategy also use this approach. There is another type of discrete event simulation that doesn't use a turn-based approach but waits for the next event. The [Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm) is an example of such an approach but we didn't cover it here. Finally, we realized that general computer code bases are also simulations. If a company has a large body of code, and particularly if it's hosted within a streaming environment (such as Apache Kafka), it's possible to back test the code with different inputs. Such backtests can be viewed as simulations, and in the case of large bodies of code (such as the code that manages Amazon's automated buying systems) the back tests can be slow and could also benefit from emulation.}

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

