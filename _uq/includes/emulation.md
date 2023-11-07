\ifndef{emulation}
\define{emulation}

\editme

\subsection{Statistical Emulation}

\figure{\includediagram{\diagramsDir/simulation/unified-model-systems}{80%}}{The UK Met office runs a shared code base for its simulations of climate and the weather. This plot shows the different spatial and temporal scales used.}{met-office-unified-model}

\notes{In many real-world systems, decisions are made through simulating the environment. Simulations may operate at different granularities. For example, simulations are used in weather forecasts and climate forecasts. Interestingly, the UK Met office uses the same code for both, it has a ["Unified Model" approach](https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model/index), but they operate climate simulations at greater spatial and temporal resolutions.}

\newslide{}

\figure{\includediagram{\diagramsDir/uq/statistical-emulation000}{80%}}{Real world systems consist of simulators that capture our domain knowledge about how our systems operate. Different simulators run at different speeds and granularities.}{statistical-emulation-1}


\newslide{Emulation}

\figure{\includediagram{\diagramsDir/uq/statistical-emulation001}{80%}}{A statistical emulator is a system that reconstructs the simulation with a statistical model.}{statistical-emulation-2}

\notes{A statistical emulator is a data-driven model that learns about the underlying simulation. Importantly, learns with uncertainty, so it 'knows what it doesn't know'. In practice, we can call the emulator in place of the simulator. If the emulator 'doesn't know', it can call the simulator for the answer.}


\newslide{Emulation}

\slides{\figure{\includediagram{\diagramsDir/uq/statistical-emulation002}{80%}}{A statistical emulator is a system that reconstructs the simulation with a statistical model.}{statistical-emulation-3}}

\newslide{Emulation}

\slides{\figure{\includediagram{\diagramsDir/uq/statistical-emulation003}{80%}}{As well as reconstructing the simulation, a statistical emulator can be used to correlate with the real world.}{statistical-emulation-4}}

\newslide{Emulation}

\figure{\includediagram{\diagramsDir/uq/statistical-emulation004}{80%}}{A statistical emulator is a system that reconstructs the simulation with a statistical model. As well as reconstructing the simulation, a statistical emulator can be used to correlate with the real world.}{statistical-emulation-5}

\newslide{Emulation}

\slides{\figure{\includediagram{\diagramsDir/uq/statistical-emulation005}{80%}}{In modern machine learning system design, the emulator may also consider the output of ML models (for monitoring bias or accuracy) and Operations Research models.}{statistical-emulation-6}}

\notes{As well as reconstructing an individual simulator, the emulator can calibrate the simulation to the real world, by monitoring differences between the simulator and real data. This allows the emulator to characterize where the simulation can be relied on, i.e., we can validate the simulator.}

\notes{Similarly, the emulator can adjudicate between simulations. This is known as *multi-fidelity emulation*. The emulator characterizes which emulations perform well where.

If all this modelling is done with judicious handling of the uncertainty, the *computational doubt*, then the emulator can assist in deciding what experiment should be run next to aid a decision: should we run a simulator, in which case which one, or should we attempt to acquire data from a real-world intervention.}

\endif
