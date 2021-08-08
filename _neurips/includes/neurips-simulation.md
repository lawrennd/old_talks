\ifndef{neuripsSimulation}
\define{neuripsSimulation}

\editme

\subsection{Conference Simulation}

\notes{Given the realization that roughly 50% of the score seems to be 'subjective' and 50% of the score seems to be 'objective', then we can simulate the conference and see what it does for the consistency of accepts for different probability of accept.}

\slides{* Calibration model suggests score is roughly 50% subjective, 50% objective.
* Duplicate experiment backs this up with roughly 50% correlation.}

\newslide{Experiment}

\slides{* Simulate conference scores which are 50% subjective/objective.
* Study statistics of conference.}

\setupcode{import numpy as np}

\code{samples = 100000
subjectivity_portion = 0.5}

\code{accept_rates = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
consistent_accepts = []
for accept_rate in accept_rates:
	score_1 = []
	score_2 = []
	for i in range(samples):
		objective = (1-subjectivity_portion)*np.random.randn()
		score_1.append(objective + subjectivity_portion*np.random.randn())
		score_2.append(objective + subjectivity_portion*np.random.randn())

	score_1 = np.asarray(score_1)
	score_2 = np.asarray(score_2)

	accept_1 = score_1.argsort()[:int(samples*accept_rate)]
	accept_2 = score_2.argsort()[:int(samples*accept_rate)]

	consistent_accept = len(set(accept_1).intersection(set(accept_2)))
	consistent_accepts.append(consistent_accept/(samples*accept_rate))
	print('Percentage consistently accepted: {prop}'.format(prop=consistent_accept/(samples*accept_rate)))

consistent_accepts = np.array(consistent_accepts)
accept_rate = np.array(accept_rate)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(accept_rates, consistent_accepts, "r.", markersize=10)
ax.plot(accept_rates, accept_rates, "k-", linewidth=2)
ax.set_xlabel("accept rate")
ax.set_ylabel("accept precision")
mlai.write_figure(filename="accept-precision-vs-accept-rate.svg",
                  directory="\writeDiagramsDir/neurips/")}

\newslide{Consistency vs Accept Rate}

\figure{\includediagram{\diagramsDir/neurips/consistency-vs-accept-rate}{50%}}{Plot of the accept rate vs the consistency of the conference for 50% subjectivity.}{consistency-vs-accept-rate}

\newslide{Gain in Consistency}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(accept_rates, consistent_accepts-accept_rates, "k-", linewidth=2)
ax.set_xlabel("accept rate")
ax.set_ylabel("(accept precision)-(accept rate)")
mlai.write_figure(filename="gain-in-consistency.svg",
                  directory="\writeDiagramsDir/neurips/")}

\figure{\includediagram{\diagramsDir/neurips/gain-in-consistency}{50%}}{Plot of the accept rate vs gain in consistency over a random conference for 50% subjectivity.}{gain-in-consistency}

\endif
