\ifndef{emukitSoftware}
\define{emukitSoftware}
\editme

\subsection{Emukit}

\figure{\includepng{../slides/diagrams/uq/emukit-software-page}{80%}}{The Emukit software is a set of software tools for emulation and surrogate modeling. <https://amzn.github.io/emukit/>}{emukit-software-page}

\newslide{Emukit}
\slides{
\includepng{../slides/diagrams/uq/emukit-software-page2}{80%}
\center{<https://amzn.github.io/emukit/>}
}

\newslide{Emukit}

\slides{
* Work by Javier Gonzalez, Andrei Paleyes, Mark Pullin, Maren Mahsereci, Alex Gessner, Aaron Klein.
* Available on [Github](https://github.com/amzn/emukit)
* Example [sensitivity notebook](https://github.com/amzn/emukit/blob/develop/notebooks/Emukit-sensitivity-montecarlo.ipynb).

}

\newslide{Emukit Software}
\slides{
* *Multi-fidelity emulation*: build surrogate models for multiple sources of information;
* *Bayesian optimisation*: optimise physical experiments and tune parameters ML algorithms;
* *Experimental design/Active learning*: design experiments and perform active learning with ML models;
* *Sensitivity analysis*: analyse the influence of inputs on the outputs 
* *Bayesian quadrature*: compute integrals of functions that are expensive to evaluate.
}
\notes{
The aim is to provide a suite where different approaches to emulation are assimilated under one roof. The current version of Emukit includes *multi-fidelity emulation* for build surrogate models when data is obtained from multiple information sources that have different fidelity and/or cost; *Bayesian optimisation* for optimising physical experiments and tune parameters of machine learning algorithms or other computational simulations; *experimental design and active learning*: design the most informative experiments and perform active learning with machine learning models; *sensitivity analysis*: analyse the influence of inputs on the outputs of a given system; and
*Bayesian quadrature*: efficiently compute the integrals of functions that are expensive to evaluate.
}

\endif
