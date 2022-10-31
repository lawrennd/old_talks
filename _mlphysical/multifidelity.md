---
week: 5
session: 2
layout: lecture
title: "Multifidelity Modelling"
featured_image: slides/diagrams/uq/statistical-emulation004.svg
abstract: >
  This week we introduce multifidelity modelling. We use surrogate models to capture different qualities of information from different simulations.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
layout: lecture
time: "10:00"
date: 2022-11-08
youtube: 0aBhHkBaBdE
oldyoutube: 
- code: 29rw9OnYGx0
  year: 2020
ipynb: True
reveal: True
transition: None
---

\include{_mlphysical/includes/mlphysical-notebook-setup.md}

\section{An Introduction to Multi-fidelity Modeling in Emukit}

\notes{A reminder from our lecture on Emulation. This diagram implies
that we might expect our statistical emulator to be able to
'adjudicate' between simulations with different fidelity.}

\figure{\includediagram{\diagramsDir/uq/statistical-emulation004}{80%}}{A statistical emulator is a system that reconstructs the simulation with a statistical model. As well as reconstructing the simulation, a statistical emulator can be used to correlate with the real world.}{statistical-emulation-6}

\subsection{Overview}

\notes{This section is based on the [Emukit multifidelity tutorial found here](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-multi-fidelity-bayesian-optimization.ipynb) and written by Javier Gonzalez, Mark Pullin, Oleg Ponomarev and David-Elias Künstle.}

\notes{A common issue encountered when applying machine learning to
environmental sciences and engineering problems is the difficulty or
cost required to obtain sufficient data for building robust models.
Possible examples include aerospace and nautical engineering, where it
is both infeasible and prohibitively expensive to run a vast number of
experiments using the actual vehicle.  Even when there is no physical
artifact involved, such as in climate modeling, data may still be hard
to obtain when these can only be collected by running an expensive
computer experiment, where the time required to acquire an individual
data sample restricts the volume of data that can later be used for
modeling.}

\notes{Constructing a reliable model when only few observations are
available is challenging, which is why it is common practice to
develop *simulators* of the actual system, from which data points can
be more easily obtained.  In engineering applications, such simulators
often take the form of Computational Fluid Dynamics (CFD) tools which
approximate the behaviour of the true artifact for a given design or
configuration.  However, although it is now possible to obtain more
data samples, it is highly unlikely that these simulators model the
true system exactly; instead, these are expected to contain some
degree of bias and/or noise.}

\notes{From the above, one can deduce that naively combining
observations from multiple information sources could result in the
model giving biased predictions which do not accurately reflect the
true problem.  To this end, *multi-fidelity models* are designed to
augment the limited true observations available with cheaply-obtained
approximations in a principled manner.  In such models, observations
obtained from the true source are referred to as *high-fidelity*
observations, whereas approximations are denoted as being
*low-fidelity*.  These low-fidelity observations are then systemically
combined with the more accurate (but limited) observations in order to
predict the high-fidelity output more effectively.  Note than we can
generally combine information from multiple lower fidelity sources,
which can all be seen as auxiliary tasks in support of a single
primary task.}

\notes{In this notebook, we shall investigate a selection of
multi-fidelity models based on Gaussian processes which are readily
available in `EmuKit`.  We start by investigating the traditional
linear multi-fidelity model as proposed in [@Kennedy-predicting00].
Subsequently, we shall illustrate why this model can be unsuitable
when the mapping from low to high-fidelity observations is nonlinear,
and demonstrate how an alternate model proposed in
@Pedikaris:nonlinear17 can alleviate this issue.  The examples
presented in this notebook can then be easily adapted to a variety of
problem settings.}

\include{_uq/includes/emukit-multifidelity.md}
\include{_deepgp/includes/stochastic-process-composition.md}
\include{_deepgp/includes/process-composition.md}
\include{_deepgp/includes/deep-gp-setup-code.md}
\include{_deepgp/includes/olympic-marathon-deep-gp.md}
\include{_uq/includes/deep-emulation.md}

\subsection{Brief Reflection}
\slides{* Given you a toolkit of Surrogate Modelling.
* Project work is opportunity to use your imagination.
* Can combine different parts together.}

\newslide{}

\notes{In this module, we have been introducing various aspects of surrogate modelling. We've already seen in the sensitivity analysis section, how we used experimental design to make our acquisition of data for the Catapult simulator more efficient. To round of the taught session of the course, we'll also combine ideas from Bayesian optimization, with an emulator built through experimental design.}

\notes{The task is a classic example from reinforcement learning, known as the 'Mountain Car'. The idea is to drive an underpowered car up a hill. The car doesn't have the ability to accelerate hard enough, but it can build momentum by oscillating up and down a hill to get to the target.}

\notes{We provide some wrappers of the OpenAI Gym version of the mountain car simulation in a python file. We will use this example to combine various ideas from surrogate modelling to solve the problem.}

\figure{\includediagram{\diagramsDir/uq/mountain-car-emulation}{80%}}{The mountain car example contains a simulation of a car's dynamics within the wider simulation of the mountain. The simulation of the car is called as a subroutine many times by the wider simulation of the mountain. We can choose to build a surrogate model of the car, and work with a modified mountain simulation where the emulator is called instead of the car's simulation directly.}{mountain-car-emulation}

\include{_uq/includes/mountain-car-simulation.md}
\include{_uq/includes/mountain-car-data-efficient.md}
\include{_uq/includes/mountain-car-multi-fidelity-introduction.md}

\codeAssignment{Can you build a multifidelity emulator for the mountain car problem similar to that we build for the Forrester function above?}{}{40}


\include{_ai/includes/prime-air-system.md}

\thanks

\reading

\references
