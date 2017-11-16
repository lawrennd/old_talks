### Multi-fidelity Modelling

* Deep nets are powerful approach to images, speech, language.

* Proposal: Deep GPs may also be a great approach, but better to deploy according to natural strengths.

### Uncertainty Quantification

* Probabilistic numerics, surrogate modelelling, emulation, and UQ.

* Not a fan of AI as a term.

* But we are faced with increasing amounts of *algorithmic decision making*.

### ML and Decision Making

* When trading off decisions: compute or acquire data?

* There is a critical need for uncertainty.

### Uncertainty Quantification

> Uncertainty quantification (UQ) is the science of quantitative characterization and reduction of uncertainties in both computational and real world applications. It tries to determine how likely certain outcomes are if some aspects of the system are not exactly known.

* Interaction between physical and virtual worlds of major interest for Amazon.

### Example: Formula One Racing

* Designing an F1 Car requires CFD, Wind Tunnel, Track Testing etc.

* How to combine them?

### Multi-Fidelity Emulation

* Normally assume that [@Kandasamy:multifidelity16,Alonso:virtual17]:

$$\mappingFunction_i\left(\inputVector\right) = \rho\mappingFunction_{i-1}\left(\inputVector\right) + \delta_i\left(\inputVector \right)$$

### Deep GP Emulation 

But with Deep Gaussian processes [@Perdikaris:multifidelity17] we can consider the form 

$$\mappingFunction_i\left(\inputVector\right) = \mappingFunctionTwo_{i}\left(\mappingFunction_{i-1}\left(\inputVector\right)\right) + \delta_i\left(\inputVector \right),$$

### Surrogate Modelling Bayesian Optimization

### Multi-fidelity

* Formula 1 example
