\ifndef{mlDeploymentChallenge}
\define{mlDeploymentChallenge}
\editme

\subsection{Deployment}

\newslide{Premise}
\slides{
Our *machine learning* is based on a *software systems* view that is 20 years out of date.
}
\notes{Much of the academic machine learning systems point of view is based on a software systems point of view that is around 20 years out of date. In particular we build machine learning models on fixed training data sets, and we test them on stationary test data sets. 

In practice modern software systems involve continuous deployment of models into an ever-evolving world of data. These changes are indicated in the software world by greater availability of technologies like *streaming* technologies.}

\subsubsection{Continuous Deployment}
\slides{
* Deployment of modeling code.
* Data dependent models in production need *continuous monitoring*.
* Continous monitoring implies *statistical tests* rather than classic software tests.
}

\notes{Once the decomposition is understood, the data is sourced and the models
are created, the model code needs to be deployed.}

\ifndef{dataScienceAsDebugging}
\notes{I normally use an analogy to describe data science to software engineers. Imagine, as a software engineer you are given a USB stick of unknown provenance with a software library on it. You are told to integrate that code into your system. All good software engineers would refuse to do this. But if they were forced to do it, they would do so very carefully.

This is the role of the data scientist, incorporating data into the system is equivalent to incorporating software of some unknown provenance.}

You can also check my \addblog{Data Science as Debugging}{2017/03/14/data-science-as-debugging}
\endif

\notes{To extend the USB stick analogy further, how would as software engineer deploy the code if they thought that the code might evolve in production? This is what
data does. We cannot assume that the conditions under which we trained
our model will be retained as we move forward, indeed the only constant
we have is change.}

\notes{This means that when any data dependent model is deployed into
production, it requires *continuous monitoring* to ensure the
assumptions of design have not been invalidated. Software changes are
qualified through testing, in particular a regression test ensures that
existing functionality is not broken by change. Since data is
continually evolving, machine learning systems require 'continual
regression testing': oversight by systems that ensure their existing
functionality has not been broken as the world evolves around them. An
approach we refer to as *progression testing*. Unfortunately, standards
around ML model deployment yet been developed. The modern world of
continuous deployment does rely on testing, but it does not recognize
the continuous evolution of the world around us.}

\notes{Progression tests are likely to be *statistical* tests in contrast to classical software tests. The tests should be monitoring model performance and quality measures. They could also monitor conformance to standardized *fairness* measures.}

\newslide{Continuous Monitoring}
\slides{
* Continuous deployment:
    * We've changed the code, we should test the effect.
* Continuous Monitoring:
    * The world around us is changing, we should monitor the effect.
* Update our notions of testing: *progression testing*
}

\notes{If the world has changed around our decision-making ecosystem, how are we alerted to those changes?}

\recommendation{We establish best practice around model deployment.
We need to shift our culture from standing up a software service, to
standing up a *data as a service*. Data as a Service would involve
continual monitoring of our deployed models in production. This would be
regulated by 'hypervisor' systems[^emulation] that understand the context in
which models are deployed and recognize when circumstances have changed,
and models need retraining or restructuring.

[^emulation]: Emulation, or surrogate modelling, is one very promising approach to forming such a hypervisor. Emulators are models we fit to other models, often simulations, but the could also be other machine learning models. These models operate at the meta-level, not on the systems directly. This means they can be used to model how the sub-systems interact. As well as emulators we should consider real time dash boards, anomaly detection, mutlivariate analysis, data visualization and classical statistical approaches for hypervision of our deployed systems.
}

\include{_data-science/includes/data-oriented-architectures.md}
\include{_data-science/includes/data-oriented-programming.md}

\endif
