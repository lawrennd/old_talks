\ifndef{emukitSoftware}
\define{emukitSoftware}
\editme

\section{Emukit}

\notes{The Emukit software we will be using across the next part of this module is a python software library that facilitates emulation of systems. The software's origins go back to work done by Javier Gonzalez as part of his post-doctoral project at the University of Sheffield. Javier led the design and build of a Bayesian optimization software. The package `GPyOpt` worked with the SheffieldML software GPy for performing Bayesian optimization. 

GPyOpt has a modular design that allows the user to provide their own surrogate models, the package is build with GPy as a surrogate model in mind, but other surrogate models can also be wrapped and integrated. 

However, GPyOpt doesn't allow the full flexibility of surrogate modelling for domains like experimental design, sensitivity analysis etc.}

\notes{Emukit was designed and built for a more general approach. The software is MIT licensed and its design and implementation was led by Javier Gonzalez and Andrei Paleyes at Amazon. Building on the experience of GPyOpt, the aim with Emukit was to use the modularisation ideas embedded in GPyOpt, but to extend them beyond the modularisation of the surrogate models to modularisation of the acquisition function.}

\figure{\includepng{\diagramsDir/uq/emukit-software-page}{80%}}{The Emukit software is a set of software tools for emulation and surrogate modeling. <https://emukit.github.io/emukit/>}{emukit-software-page}

\newslide{Emukit}
\slides{
\includepng{\diagramsDir/uq/emukit-software-page2}{80%}
\center{<https://emukit.github.io/emukit/>}
}

\installcode{GPy}
\installcode{pyDOE}
\installcode{EmuKit}

\newslide{Emukit}

\slides{
* Led by: Javier Gonzalez and Andrei Paleyes
    * Team: Mark Pullin, Maren Mahsereci, Alex Gessner, Aaron Klein, Henry Moss and David-Elias Künstle.
	* Management: Cliff McCollum & Neil
* Available on [Github](https://github.com/EmuKit/emukit)
    * Example [sensitivity notebook](https://github.com/EmuKit/emukit/blob/develop/notebooks/Emukit-sensitivity-montecarlo.ipynb), documentation <https://emukit.readthedocs.io/en/latest/>
}

\notes{The software was initially built by the team in Amazon. As well as Javier Gonzalez (ML side) and Andrei Paleyes (Software Engineering) included Mark Pullin, Maren Mahsereci, Alex Gessner, Aaron Klein, Henry Moss, David-Elias Künstle  as well as management input from Cliff McCollum and myself.}

\newslide{Modular Design}

\slides{Introduce your own surrogate models.

```{.python}
from emukit.model_wrappers import GPyModelWrapper
```}
\slides{To building your own model [see this notebook](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-custom-model.ipynb).}
\slides{```{.python}
from emukit.model_wrappers import YourModelWrapperHere
```}


\endif
