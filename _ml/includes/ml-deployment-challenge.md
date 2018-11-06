\subsection{Deployment}

\newslide{Premise}
\slides{
Our *machine learning* is based on a *software systems* view that is 20 years out of date.
}

\subsection{Continuous Deployment}
\slides{
* Deployment of modeling code.
* Data dependent models in production need *continuous monitoring*.
}

\notes{Once the decomposition is understood, the data is sourced and the models
are created, the model code needs to be deployed.}

\notes{To extend the USB stick analogy further, how would we deploy that code
if we thought it was likely to evolve in production? This is what
datadoes. We cannot assume that the conditions under which we trained
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

\newslide{Continuous Monitoring}
\slides{
* Continuous deployment:
    * We've changed the code, we should test the effect.
* Continuous Monitoring:
    * The world around us is changing, we should monitor the effect.
* Update our notions of testing: *progression testing*
}

\notes{If the world has changed around our decision making ecosystem, how are we alerted to those changes?}

\recommendation{We establish best practice around model deployment.
We need to shift our culture from standing up a software service, to
standing up a *data as a service*. Data as a Service would involve
continual monitoring of our deployed models in production. This would be
regulated by 'hypervisor' systems[^emulation] that understand the context in
which models are deployed and recognize when circumstance has changed
and models need retraining or restructuring.

[^emulation]: Emulation, or surrogate modelling, is one very promising approach to forming such a hypervisor. Emulators are models we fit to other models, often simulations, but the could also be other machine learning modles. These models operate at the meta-level, not on the systems directly. This means they can be used to model how the sub-systems interact. As well as emulators we shoulc consider real time dash boards, anomaly detection, mutlivariate analysis, data visualization and classical statistical approaches for hypervision of our deployed systems.
}

\newslide{Data Orientated Architectures}

\slides{
* Historically we've been *software first*
    * A necessary but not sufficient condition for *data first*
* Move from
    1. software orientated architectures
	2. *data orientated architectures*
}

\newslide{Streaming Architectures}
\slides{
* AWS Kinesis, Apache Kafka
* Not just about streaming
    * Nodes in the architecture are *stateless* 
	* They persist through storing state on *streams*
* This brings the data *inside out*
}

\recommendation{We should consider a major re-architecting of systems around our services. In particular we should scope the use of a *streaming architecture* (such as Apache Kafka) that ensures data persistence and enables asynchronous operation of our systems.[^data-orientated-architecture] This would enable the provision of QC streams, and real time dash boards as well as hypervisors..

[^data-orientated-architecture]: These approaches are one area of focus for my own team's reasearch. A data first architecture is a prerequisite for efficient deployment of machine learning systems.

Importantly a streaming architecture implies the services we build are
*stateless*, internal state is deployed on streams alongside external
state. This allows for rapid assessment of other services' data.
}

