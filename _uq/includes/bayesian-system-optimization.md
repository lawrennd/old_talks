\ifndef{bayesianSystemOptimization}
\define{bayesianSystemOptimization}

\editme

\subsection{Bayesian *System* Optimization}
\slides{
* Aim: maintain interpretable components.
* Monitor downstream/upstream effects through emulation.
* Optimize individual components considering upstream and downstream.
}
\notes{We introduce the notion of Bayesian *system* optimisation. Standard Bayesian optimisation is about optimising individual components under a given (localised) optimisation criterion. Bayesian system optimisation is about realising that there are upstream and downstream effects, 'no model is an island'. If we can use emulation to estimate those effects, then we can optimise individual components not just according to their own objective functions, but according to their situation in the wider system and their downstream effects.}

\endif
