\ifndef{entropyIntro}
\define{entropyIntro}



\include{_physics/includes/daniel-bernoulli-hydrodynamica.md}
\include{_physics/includes/entropy-billiards.md}

\editme

\newslide{}

\setupcode{import numpy as np}

\code{p = np.random.randn(10000, 1)
xlim = [-4, 4]
x = np.linspace(xlim[0], xlim[1], 200)
y = 1/np.sqrt(2*np.pi)*np.exp(-0.5*x*x)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x, y, 'r', linewidth=3)
ax.hist(p, 100, density=True)
ax.set_xlim(xlim)

mlai.write_figure('gaussian-histogram.svg', directory='\writeDiagramsDir/ml')}

\notes{Another important figure for Cambridge was the first to derive the probability distribution that results from small balls banging together in this manner. In doing so, James Clerk Maxwell founded the field of statistical physics.}

\figure{\includediagram{\diagramsDir/ml/gaussian-histogram}{80%}}{James Clerk Maxwell 1831-1879 Derived distribution of velocities of particles in an ideal gas (elastic fluid).}{gaussian-histogram}

\newslide{}

\figure{\threeColumns{\includepng{\diagramsDir/physics/james-clerk-maxwell}{100%}{}{left}}{\includejpg{\diagramsDir/physics/boltzmann2}{100%}{}{center}}{\includejpg{\diagramsDir/physics/j-w-gibbs}{100%}{}{right}}{30%}{30%}{30%}}{James Clerk Maxwell (1831-1879), Ludwig Boltzmann (1844-1906) Josiah Willard Gibbs (1839-1903)}{maxwell-boltzmann-gibbs}

\notes{Many of the ideas of early statistical physicists were rejected by a cadre of physicists who didn't believe in the notion of a molecule. The stress of trying to have his ideas established caused Boltzmann to commit suicide in 1906, only two years before the same ideas became widely accepted.}

\newslide{}

\figure{\includegooglebook{Vuk5AQAAMAAJ}{PA373}}{Boltzmann's paper @Boltzmann-warmetheorie77 which introduced the relationship between entropy and probability. A translation with notes is available in @Kim-translation15.}{boltzmann-warmetheorie}


\notes{The important point about the uncertainty being represented here is that it is not genuine stochasticity, it is a lack of knowledge about the system. The techniques proposed by Maxwell, Boltzmann and Gibbs allow us to exactly represent the state of the system through a set of parameters that represent the sufficient statistics of the physical system. We know these values as the volume, temperature, and pressure. The challenge for us, when approximating the physical world with the techniques we will use is that we will have to sit somewhere between the deterministic and purely stochastic worlds that these different scientists described.}

\newslide{}

\notes{One ongoing characteristic of people who study probability and uncertainty is the confidence with which they hold opinions about it. Another leader of the Cavendish laboratory expressed his support of the second law of thermodynamics (which can be proven through the work of Gibbs/Boltzmann) with an emphatic statement at the beginning of his book.}

\figure{\columns{\includejpg{\diagramsDir/physics/arthur-stanley-eddington}{100%}{}{left}}{\includepng{\diagramsDir/physics/natureofphysical00eddi_7}{80%}{}{right}}{49%}{49%}}{Eddington's book on the Nature of the Physical World [@Eddington:nature29]}{eddington-book}

\newslide{}

\notes{The same Eddington is also famous for dismissing the ideas of a young Chandrasekhar who had come to Cambridge to study in the Cavendish lab. Chandrasekhar demonstrated the limit at which a star would collapse under its own weight to a singularity, but when he presented the work to Eddington, he was dismissive suggesting that there "must be some natural law that prevents this abomination from happening".}

\figure{\columns{\includepng{\diagramsDir/physics/natureofphysical00eddi_100}{80%}{}{left}}{\includepng{\diagramsDir/physics/ChandraNobel}{100%}{}{right}}{49%}{49%}}{Chandrasekhar (1910-1995) derived the limit at which a star collapses in on itself. Eddington's confidence in the 2nd law may have been what drove him to dismiss Chandrasekhar's ideas, humiliating a young scientist who would later receive a Nobel prize for the work.}{physical-world-chandra}

\newslide{}

\figure{\includepng{\diagramsDir/physics/natureofphysical00eddi_100_cropped}{60%}}{Eddington makes his feelings about the primacy of the second law clear. This primacy is perhaps because the second law can be demonstrated mathematically, building on the work of Maxwell, Gibbs and Boltzmann. @Eddington:nature29}{deepest-humiliation-eddington-cropped}

\notes{Presumably he meant that the creation of a black hole seemed to transgress the second law of thermodynamics, although later Hawking was able to show that blackholes do evaporate, but the time scales at which this evaporation occurs is many orders of magnitude slower than other processes in the universe.}


\endif

