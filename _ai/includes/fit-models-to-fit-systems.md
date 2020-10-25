\ifndef{fitModelsToFitSystems}
\define{fitModelsToFitSystems}


\editme

\subsection{AutoAI: FIT Models to FIT Systems}

\slides{* Streaming algebra provides a tube map for data.
* Can now deploy classical statistical and software verification techniques.
   * e.g. outlier detection, verification that prohibited characteristics are not used
* Also explore ML techniques for fairness, interpretability, transparency for *system* instead of *model*.
}

\notes{The idea of AutoAI is to combine the streaming algebra we obtain from the data oriented architecture (we can think of it as a 'tube map for data flows') with monitoring techniques both from machine learning, classical statistics and softare verification for ensuring that the system is performing as designed and/or alerting us to when our assumptions about the system are invalidated. 

We can already deploy classical statistical approaches for e.g. outlier detection, or use proofs from category theory to demonstrate that a particular decision is not based on a protected characteristic. 

The additional aim would be to use techniques from uncertainty quantification and statistical emulation to provide more interpretability to those decisions.

This domain has been called FAT modelling in machine learning, but I prefer the acronym FIT for fairness, interpretability and transparency. 

AutoAI makes us realise that AutoML isn't sufficient for improving the performance of the system, because it works on a componentwise basis. Similarly, FIT machine learning models are not sufficient. We need to move from FIT models to FIT systems.
}

\endif
