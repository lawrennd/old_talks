\ifndef{neuripsSimulation}
\define{neuripsSimulation}

\editme

\subsection{Conference Simulation}

\notes{Given the realization that roughly 50% of the score seems to be 'subjective' and 50% of the score seems to be 'objective', then we can simulate the conference and see what it does for the accept precision for different probability of accept.}

\slides{* Calibration model suggests score is roughly 50% subjective, 50% objective.
* Duplicate experiment backs this up with roughly 50% correlation.}

\newslide{Experiment}

\notes{To explore the effect of the subjective scoring on the accept precision we construct a simple simulation that scores hypothetical papers with random values drawn from a Gaussian density. Each paper has an underlying objective score (shared across the hypothetical reviewers), and then alongside it there are Gaussian variables drawn independently at random to represent the subjectivity of the hypothetical reviewers.}

\notes{Each paper is rated by two independent committees, and the papers are reordered to accept the top $x$% where $x$ is our chosen accept rate. We can then use sample based estimates for the resulting accept precision.}

\notes{In these experiments the scores are taken to be 50% subjective and 50% objective, in line with the results we see from the NeurIPS 2014 calibration model. We vary the number of reviewers in the simulation to see the effect of increasing reviewers on the accept precision.}

\slides{* Simulate conference scores which are 50% subjective/objective.
* Study statistics of conference.}

\setupcode{import numpy as np}

\notes{We repeat the experiment `samples` number of times, here we've set this to be 100000. The subjectivity portion gives how much of the scores for each paper is subjective.}

\code{num_papers = 100000
subjectivity_portion = 0.5}

\code{accept_rates = [0.05, 0.1, 0.15, 0.2, 0.25, 
                      0.3, 0.35, 0.4, 0.45, 0.5, 
                      0.55, 0.6, 0.65, 0.7, 0.75, 
                      0.8, 0.85, 0.9, 0.95, 1.0]
all_accepts = []
for num_reviewers in range(1,7):
    consistent_accepts = []
    for accept_rate in accept_rates:
        objective = (1-subjectivity_portion)*np.random.randn(num_papers) 
        subjective_0 = subjectivity_portion*np.random.randn(num_papers, num_reviewers).mean(1)
        subjective_1 = subjectivity_portion*np.random.randn(num_papers, num_reviewers).mean(1)
        score_0 = objective + subjective_0    
        score_1 = objective + subjective_1

        accept_0 = score_0.argsort()[:int(num_papers*accept_rate)]
        accept_1 = score_1.argsort()[:int(num_papers*accept_rate)]

        consistent_accept = len(set(accept_0).intersection(set(accept_1)))
        consistent_accepts.append(consistent_accept/(samples*accept_rate))
        print('Percentage consistently accepted: {prop}'.format(prop=consistent_accept/(samples*accept_rate)))

    all_accepts.append(consistent_accepts)
all_accepts = np.array(all_accepts)
consistent_accepts = np.array(consistent_accepts)
accept_rate = np.array(accept_rate)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot
from cycler import cycler
monochrome = (cycler('color', ['k']) * cycler('linestyle', ['-', '--', ':', '=.']) * cycler('marker', ['^','o', 's']))}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.set_prop_cycle(monochrome)

ax.plot(accept_rates, accept_rates, "k-", linewidth=2)
ax.plot(accept_rates, all_accepts.T, markersize=7)
ax.legend(['random', '1 reviewer', '2 reviewers', '3 reviewers', '4 reviewers', '5 reviewers', '6 reviewers'])
ax.set_xlabel("accept rate")
ax.set_ylabel("accept precision")
ax.axvline(0.23)
mlai.write_figure(filename="accept-precision-vs-accept-rate.svg",
                  directory="\writeDiagramsDir/neurips/")}

\newslide{Consistency vs Accept Rate}

\figure{\includediagram{\diagramsDir/neurips/accept-precision-vs-accept-rate}{50%}}{Plot of the accept rate vs the accept precision for the conference for 50% subjectivity and different numbers of reviewers. The grey line gives the NeurIPS accept rate for 2014 of 23%.}{accept-precision-vs-accept-rate}

\notes{In Figure \ref{accept-precision-vs-accept-rate} we see the change in accept precision as we vary accept rate and number of reviewers for a conference where reviewers are 50% subjective.}

\newslide{Gain in Consistency}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.set_prop_cycle(monochrome)
ax.plot(accept_rates, (all_accepts-accept_rates).T)
ax.legend(['1 reviewer', '2 reviewers', '3 reviewers', '4 reviewers', '5 reviewers', '6 reviewers'])
ax.set_xlabel("accept rate")
ax.set_ylabel("(accept precision)-(accept rate)")
mlai.write_figure(filename="gain-in-consistency.svg",
                  directory="\writeDiagramsDir/neurips/")}

\figure{\includediagram{\diagramsDir/neurips/gain-in-consistency}{50%}}{Plot of the accept rate vs gain in consistency over a random conference for 50% subjectivity.}{gain-in-consistency}

\notes{Figure \ref{gain-in-consistency} shows the accept rate against the gain in accept precision we have over the random committee.}

\endif
