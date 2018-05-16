### Uncertainty Quantification

* Deep nets are powerful approach to images, speech, language.

* Proposal: Deep GPs may also be a great approach, but better to deploy according to natural strengths.

### Uncertainty Quantification

* Probabilistic numerics, surrogate modelling, emulation, and UQ.

* Not a fan of AI as a term.

* But we are faced with increasing amounts of *algorithmic decision making*.

### ML and Decision Making

* When trading off decisions: compute or acquire data?

* There is a critical need for uncertainty.


### Uncertainty Quantification

> Uncertainty quantification (UQ) is the science of quantitative characterization and reduction of uncertainties in both computational and real world applications. It tries to determine how likely certain outcomes are if some aspects of the system are not exactly known.

* Interaction between physical and virtual worlds of major interest for Amazon.

\notes{We will to illustrate different concepts of [Uncertainty Quantification](https://en.wikipedia.org/wiki/Uncertainty_quantification) (UQ) and the role that Gaussian processes play in this field. Based on a simple simulator of a car moving between a valley and a mountain, we are going to illustrate the following concepts:

- **Systems emulation**. Many real world decisions are based on simulations that can be computationally very demanding. We will show how simulators can be replaced by *emulators*: Gaussian process models fitted on a few simulations that can be used to replace the *simulator*. Emulators are cheap to compute, fast to run, and always provide ways to quantify the uncertainty of how precise they are compared the original simulator.

- **Emulators in optimization problems**. We will show how emulators can be used to optimize black-box functions that are expensive to evaluate. This field is also called Bayesian Optimization and has gained an increasing relevance in machine learning as emulators can be used to optimize computer simulations (and machine learning algorithms) quite efficiently.

- **Multi-fidelity emulation methods**. In many scenarios we have simulators of different quality about the same measure of interest. In these cases the goal is to merge all sources of information under the same model so the final emulator is cheaper and more accurate than an emulator fitted only using data from the most accurate and expensive simulator.}


### Example: Formula One Racing

* Designing an F1 Car requires CFD, Wind Tunnel, Track Testing etc.

* How to combine them?

\include{./_uq/includes/mountain-car-simulation.md}
\include{./_uq/includes/mountain-car-data-efficient.md}
\include{./_uq/includes/mountain-car-multi-fidelity.md}

