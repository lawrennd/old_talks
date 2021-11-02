\ifndef{emukitVision}
\define{emukitVision}

\editme

\newslide{Structure}

\slides{* loop
* model
* candidate point calculator
* acquisition
* acquisition optimizer
* user function
* model updater
* stopping condition}

\section{Emukit Vision}

\notes{\subsection{Emulation in Emukit}}

\notes{We see emulation comprising of three main parts:}

\notes{**Models**. This is a probabilistic data-driven representation of the process/simulator that the user is working with. There is normally a modelling framework that is used to create a model. Examples: neural network, Gaussian process, random forest.}

\notes{**Methods**. Relatively low-level techniques that are aimed that either understanding, quantifying or using uncertainty that the model provides. Examples: Bayesian optimization, experimental design.}

\notes{**Tasks**. High level goals that owners of the process/simulator might be actually interested in. Examples: measure quality of a simulator, explain complex system behavior.}

\notes{Typical workflow that we envision for a user interested in emulation is:

1. Figure out which questions/tasks are important for them in regard to their process/simulation.

2. Understand which emulation techniques are needed to accomplish the chosen task.

3. Build an emulator of the process. That can be a very involved step, that may include a lot of fine tuning and validation.}

\notes{Feed the emulator to the chosen technique and use it to answer the question/complete the task.}

\subsection{Emukit and Emulation}

\figure{\includediagram{\diagramsDir/uq/emukit-vision}{60%}}{The emukit approach to the three parts of emulation.}{emukit-vision}

\subsection{Methods}

\slides{* The different methods: Bayesian optimization, experimental design.}

\notes{This is the main focus of Emukit. Emukit defines a general sctructure of a decision making method, called OuterLoop, and then offers implementations of few such methods: Bayesian optimization, experimental design. In addition to provide a framework for decision making Emukit provide other tools, like sensitivity analysis, that help to debug and interpret emulators. All methods in Emukit are model-agnostic.}

\subsection{Models}

\slides{* The probabilistic model that will be used to emulate. Emukit doesn't define these, the user brings their own.}

\notes{Generally speaking, Emukit does not provide modelling capabilities, instead expecting users to bring their own models. Because of the variety of modelling frameworks out there, Emukit does not mandate or make any assumptions about a particular modelling technique or a library. Instead it suggests to implement a subset of defined model interfaces required to use a particular method. Nevertheless, there are a few model-related functionalities in Emukit: - Example models, which give users something to play with to explore Emukit. - Model wrappers, which are designed to help adapting models in particular modelling frameworks to Emukit interfaces. - Multi-fidelity models, implemented based on GPy.}

\subsection{Tasks}

\slides{* Still in development: High level goals that owners of the process/simulator might be actually interested in. Examples: measure quality of a simulator, explain complex system behavior.}

\notes{Emukit does not contribute much to this part at the moment. However Emukit team are on lookout for typical use cases for Emukit, and if a reoccuring pattern emerges, it may become a part of the library.}

\newslide{Structure}

```
while stopping condition is not met:
    optimize acquisition function
    evaluate user function
    update model with new observation
```

\notes{Emukit is build in a modular way so that each component in this loop can be swapped out. This means that scientists, applied mathematicians, machine learnings, statisticians can swap out the relavant part of their method and build on the undelrying structure. You just need to pick out the part that requires implementation.}

\subsection{Loop}
\slides{* An abstract class where the different components come together.}

\notes{The ```emukit.core.loop.OuterLoop``` class is the abstract loop where the different components come together. There are more specific loops for Bayesian optimization and experimental design that construct some of the component parts for you.}

\subsection{Model}

\slides{* The surrogate model or *emulator*, often a Gaussian process.}
\notes{All `Emukit` loops need a probabilistic model of the underlying system. Emukit does not provide functionality to build models as there are already many good modelling frameworks available in python. Instead, we provide a way of interfacing third part modelling libraries with Emukit. We already provide a wrapper for using a model created with `GPy`. For instructions on how to include your own model please [see this notebook](https://emukit.readthedocs.io/en/latest/notebooks/Emukit-tutorial-custom-model.html).}

\notes{Different models and modelling frameworks will provide different functionality. For instance a Gaussian process will usually have derivatives of the predictions available but random forests will not. These different functionalities are represented by a set of interfaces which a model implements. The basic interface that all models must implement is `IModel`, which implements functionality to make predictions and update the model but a model may implement any number of other interfaces such as `IDifferentiable` which indicates a model has prediction derivatives available.}

\subsection{Candidate Point Calculator}

\slides{* The routine that combines acquisition with optimizer to compute the next candidate point (or points).}

\notes{This class decides which point to evaluate next. The simplest implementation, `SequentialPointCalculator`, collects one point at a time by finding where the acquisition is a maximum by applying the acquisition optimizer to the acquisition function. More complex implementations will enable batches of points to be collected so that the user function can be evaluated in parallel.}

\subsection{Acquisition}

\slides{* Our acquisition function: in Bayesian Optimization, this might be Expected Improvement.}
\notes{The acquisition is a heuristic quantification of how valuable collecting a future point might be. It is used by the candidate point calculator to decide which point(s) to collect next.}

\subsection{Acquisition Optimizer}

\slides{* The optimization routine we use to optimize the acquisition function. (often this is a non-linear optimizer like L-BFGS [@Byrd:lbfgsb95])}

\notes{The `AcquisitionOptimizer` optimizes the acquisition function to find the point at which the acquisition is a maximum. This will use the acquisition function gradients if they are available. If gradients of the acquisition function are not available it will either estimate them numerically or use a gradient free optimizer.}

\subsection{User Function}

\slides{* The function we're trying to reason about.}
\notes{This is the function that we are trying to reason about. It can be either evaluated by the user or it can be passed into the loop and evaluated by Emukit.}

\subsection{Model Updater}

\slides{* How to update our surrogate model when we have new training data.}

\notes{The `ModelUpdater` class updates the model with new training data after a new point is observed and optimizes any hyper-parameters of the model. It can decide whether hyper-parameters need updating based on some internal logic.}

\subsection{Stopping Condition}

\slides{* How to decide when to stop our cycle of data acquisition from the target function.}

\notes{The `StoppingCondition` class chooses when we should stop collecting points. The most commonly used example is to stop when a set number of iterations have been reached.}

\endif
