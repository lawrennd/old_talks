
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

\notes{Once the design is complete, the model code needs to be deployed.}

\notes{To extend our USB stick analogy further, how would we deploy that code if we thought it was likely to evolve in production? This is what data does. We cannot assume that the conditions under which we trained our model will be retained as we move forward, indeed the only constant we have is change.}

\notes{This means that when any data dependent model is deployed into production, it requires *continuous monitoring* to ensure the assumptions of design have not been invalidated. Software changes are qualified through testing, in particular a regression test ensures that existing functionality is not broken by change. Since data is continually evolving, machine learning systems require continual regression testing: oversight by systems that ensure their existing functionality has not been broken as the world evolves around them.  Unfortunately, standards around ML model deployment yet been developed.  The modern world of continuous deployment does rely on testing, but it does not recognize the continuous evolution of the world around us.}

\newslide{Continuous Monitoring}
\slides{
* Continuous deployment:
    * We've changed the code, we should test the effect.
* Continuous Monitoring:
    * The world around us is changing, we should monitor the effect.
}

\notes{If the world has changed around our decision making ecosystem, how are we alerted to those changes?}

\recommendation{We establish best practice around model deployment.  We need to shift our culture from standing up a software service, to standing up a *data service*. Data as a Service would involve continual monitoring of our deployed models in production. This would be regulated by 'hypervisor' systems[^3] that understand the context in which models are deployed and recognize when circumstance has changed and models need retraining or restructuring.

[^3]: Emulation is one approach to forming such a hypervisor, because we
    can build emulators that operate at the meta level, not on the
    systems directly, but how they interact. Or emulators that monitor a
    simulation to ensure performance does not change dramatically.
    However, they are not the only approach. Using real time dashboards,
    anomaly detection and classical statistics are also applicable in
    this domain.
}

\newslide{Streaming Architectures}
\slides{
* AWS Kinesis, Apache Kafka
* Not just about streaming
    * Nodes in the architecture are *stateless* 
	* They persist through storing state on *streams*
* This brings the data *inside out*
}

\recommendation{We should consider a major re-architecting of systems around our services. In particular we should scope the use of a *streaming architecture* (such as Apache Kafka) that ensures data persistence and enables asynchronous operation of our systems.[^4] This would enable the provision of QC streams, and real time dash boards as well as hypervisors.

[^4]: The Cambridge team has been exploring this area.  We have a reference architecture, and are also considering how such a system could/should be extended for incorporation of simulation models.

Importantly a streaming architecture implies the services we build are *stateless*, internal state is deployed on streams alongside external state. This allows for rapid assessment of other services' data.}

