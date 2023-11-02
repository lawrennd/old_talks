\ifndef{emukitSoftware}
\define{emukitSoftware}
\editme

\section{Emukit}

\centerdiv{\javierGonzalezPicture{10%}\andreiPaleyesPicture{10%}\markPullinPicture{10%}\marenMahsereciPicture{10%}}

\notes{The Emukit software we will be using across the next part of this module is a python software library that facilitates emulation of systems. The software's origins go back to work done by [Javier Gonzalez](https://javiergonzalezh.github.io/) as part of his post-doctoral project at the University of Sheffield. Javier led the design and build of a Bayesian optimization software. The package `GPyOpt` worked with the SheffieldML software GPy for performing Bayesian optimization.}

\notes{`GPyOpt` had a modular design that allows the user to provide their own surrogate models, the package was built with `GPy` as a surrogate model in mind, but other surrogate models could also be wrapped and integrated.}

\notes{However, `GPyOpt` didn't allow the full flexibility of surrogate modelling for domains like experimental design, sensitivity analysis etc.}

\notes{Emukit [@Paleyes-emulation19] is designed and built for a more general approach. The software is MIT licensed and its design and implementation was led by Javier Gonzalez and [Andrei Paleyes](https://www.linkedin.com/in/andreipaleyes) at Amazon. Building on the experience of `GPyOpt`, the aim with Emukit was to use the modularisation ideas embedded in `GPyOpt`, but to extend them beyond the modularisation of the surrogate models to modularisation of the acquisition function.}

\figure{\includepng{\diagramsDir/uq/emukit-software-page}{80%}}{The Emukit software is a set of software tools for emulation and surrogate modeling. <https://emukit.github.io/emukit/>}{emukit-software-page}

\newslide{Emukit}
\slides{
\figure{\includepng{\diagramsDir/uq/emukit-software-page2}{80%}}{The lower potion of the emukit sofware page.}{emukit-software-page2}
\centerdiv{<https://emukit.github.io/emukit/>}
}

\notes{To use Emukit you need a set of models to use as the surrogates, we'll use `GPy`.}

\installcode{GPy}

\notes{Emukit does active experimental design, to access stratified sampling and latin hypercube designs it makes use of the `pyDOE` package.}

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

\centerdiv{\javierGonzalezPicture{10%}\andreiPaleyesPicture{10%}\markPullinPicture{10%}\marenMahsereciPicture{10%}}
\notes{The software was initially built by the team in Amazon. As well as Javier Gonzalez (ML side) and Andrei Paleyes (Software Engineering) the team included Mark Pullin, Maren Mahsereci, Alex Gessner, Aaron Klein, Henry Moss, David-Elias Künstle  as well as management input from Cliff McCollum and myself.}

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
