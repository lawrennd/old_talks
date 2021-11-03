\ifndef{planckCmpMasterGp}
\define{planckCmpMasterGp}
\editme

\notes{\subsection{Universe isn't as Gaussian as it Was}}

\notes{The [Planck space craft](https://en.wikipedia.org/wiki/Planck_(spacecraft)) was a European Space Agency space telescope that mapped the cosmic microwave background (CMB) from 2009 to 2013. The [Cosmic Microwave Background](https://en.wikipedia.org/wiki/Cosmic_microwave_background) is the first observable echo we have of the big bang. It dates to approximately 400,000 years after the big bang, at the time the Universe was approximately $10^8$ times smaller and the temperature of the Universe was high, around $3 \times 10^8$ degrees Kelvin. The Universe was in the form of a hydrogen plasma. The echo we observe is the moment when the Universe was cool enough for Protons and electrons to combine to form hydrogen atoms. At this moment, the Universe became transparent for the first time, and photons could travel through space.

\figure{\includejpg{\diagramsDir/physics/Front_view_of_the_European_Space_Agency_Planck_satellite}{60%}}{Artist's impression of the Planck spacecraft which measured the Cosmic Microwave Background between 2009 and 2013.}{planck-spacecraft}

The objective of the Planck spacecraft was to measure the anisotropy and statistics of the Cosmic Microwave Background. This was important, because if the standard model of the Universe is correct the variations around the very high temperature of the Universe of the CMB should be distributed according to a Gaussian process.[^kyle-cranmer] Currently our best estimates show this to be the case [@Jaffe:cmb98;@Pontzen-cmb10;@Elsner-unbiased15;@Elsner-unbiased16].


[^kyle-cranmer]: Most of my understanding of this is taken from conversations with Kyle Cranmer, a physicist who makes extensive use of machine learning methods in his work. See e.g. @Mishra-Sharma-semi-parametric20 from Kyle and Siddharth Mishra-Sharma. Of course, any errors in the above text are mine and do not stem from Kyle.}

\newslide{}

\notes{To the high degree of precision that we could measure with the Planck space telescope, the CMB appears to be a Gaussian process. The parameters of its covariance function are given by the fundamental parameters of the universe, for example the amount of dark matter and matter in the universe}

\figure{\includepng{\diagramsDir/Planck_CMB}{50%}{vertical-align:middle}}{The cosmic microwave background is, to a very high degree of precision, a Gaussian process. The parameters of its covariance function are given by fundamental parameters of the universe, such as the amount of dark matter and mass.}{cosmic-microwave-background}

\notes{\subsection{Simulating a CMB Map}}

\notes{The simulation was created by [Boris Leistedt](https://ixkael.github.io/), see the [original Jupyter notebook here](https://github.com/ixkael/Prob-tools/blob/master/notebooks/The%20CMB%20as%20a%20Gaussian%20Process.ipynb).}

\notes{Here we use that code to simulate our own universe and sample from what it looks like.}

\notes{First, we install some specialist software as well as `matplotlib`, `scipy`, `numpy` we require

- `camb`: <http://camb.readthedocs.io/en/latest/>
- `healpy`: <https://healpy.readthedocs.io/en/latest/>}

\installcode{camb}
\installcode{healpy}

\setupplotcode{%config IPython.matplotlib.backend = 'retina'
%config InlineBackend.figure_format = 'retina'

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from cycler import cycler

import numpy as np

rc("font", family="serif", size=14)
rc("text", usetex=False)
matplotlib.rcParams['lines.linewidth'] = 2
matplotlib.rcParams['patch.linewidth'] = 2
matplotlib.rcParams['axes.prop_cycle'] =\
    cycler("color", ['k', 'c', 'm', 'y'])
matplotlib.rcParams['axes.labelsize'] = 16}

\setupcode{import healpy as hp

import camb
from camb import model, initialpower}

\notes{Now we use the theoretical power spectrum to design the covariance function.}

\code{nside = 512  # Healpix parameter, giving 12*nside**2 equal-area pixels on the sphere.
lmax = 3*nside # band-limit. Should be 2*nside < lmax < 4*nside to get information content.}

\notes{Now we design our Universe. It is parameterized according to the [$\Lambda$CDM model](https://en.wikipedia.org/wiki/Lambda-CDM_model). The variables are as follows. `H0` is the Hubble parameter (in Km/s/Mpc). The `ombh2` is Physical Baryon density parameter. The `omch2` is the physical dark matter density parameter. `mnu` is the sum of the neutrino masses (in electron Volts). `omk` is the $\Omega_k$ is the curvature parameter, which is here set to 0, giving the minimal six parameter Lambda-CDM model. `tau` is the reionization optical depth.}

\notes{Then we set `ns`, the "scalar spectral index". This was estimated by Planck to be 0.96. Then there's `r`, the ratio of the tensor power spectrum to scalar power spectrum. This has been estimated by Planck to be under 0.11. Here we set it to zero. These parameters are associated [with inflation](https://en.wikipedia.org/wiki/Primordial_fluctuations). }

\code{# Mostly following http://camb.readthedocs.io/en/latest/CAMBdemo.html with parameters from https://en.wikipedia.org/wiki/Lambda-CDM_model

pars = camb.CAMBparams()
pars.set_cosmology(H0=67.74, ombh2=0.0223, omch2=0.1188, mnu=0.06, omk=0, tau=0.066)
pars.InitPower.set_params(ns=0.96, r=0)
}

\notes{Having set the parameters, we now use the python software "Code for Anisotropies in the Microwave Background" to get the results.}

\code{pars.set_for_lmax(lmax, lens_potential_accuracy=0);
results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars)
totCL = powers['total']
unlensedCL = powers['unlensed_scalar']

ells = np.arange(totCL.shape[0])
Dells = totCL[:, 0]
Cells = Dells * 2*np.pi / ells / (ells + 1)  # change of convention to get C_ell
Cells[0:2] = 0}



\code{cmbmap = hp.synfast(Cells, nside, 
                 lmax=lmax, mmax=None, alm=False, pol=False, 
                 pixwin=False, fwhm=0.0, sigma=None, new=False, verbose=True)}
				 
\plotcode{hp.mollview(cmbmap)
fig = plt.gcf()
mlai.write_figure('mollweide-sample-cmb.png',
                  directory='\writeDiagramsDir/physics/')}

\newslide{}

\figure{\includepng{\diagramsDir/physics/mollweide-sample-cmb}{50%}{vertical-align:middle}}{A simulation of the Cosmic Microwave Background obtained through sampling from the relevant Gaussian process covariance (in polar co-ordinates).}{mollweide-sample-cmb}


\newslide{}

\notes{The world we see today, of course, is not a Gaussian process. There are many discontinuities, for example, in the density of matter, and therefore in the temperature of the Universe.}


\figure{\div{<img src="\diagramsDir/earth_PNG37.png" width="20%" style="display:inline-block;background:none;vertical-align:middle;border:none;box-shadow:none;">$=f\Bigg($<img src="\diagramsDir/Planck_CMB.png"  width="50%" style="display:inline-block;background:none;vertical-align:middle;border:none;box-shadow:none;">$\Bigg)$}{}{fontsize:120px;vertical-align:middle}}{What we observe today is some non-linear function of the cosmic microwave background.}{modern-universe-non-linear-function}

\notes{We can think of today's observed Universe, though, as a being a consequence of those temperature fluctuations in the CMB. Those fluctuations are only order $10^{-6}$ of the scale of the overall temperature of the Universe. But minor fluctuations in that density are what triggered the pattern of formation of the Galaxies. They determined how stars formed and created the elements that are the building blocks of our Earth [@Vogelsberger-cosmological20].}


\endif

