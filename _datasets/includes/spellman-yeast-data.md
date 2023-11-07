\ifndef{spellmanYeastData}
\define{spellmanYeastData}

\editme

\subsection{Spellman Yeast Cell Cycle Data}

\notes{This data set collection is from an classic early microarray paper on the yeast cell cycle [@Spellman:yeastcellcy98].}


\setupcode{import pods}

\code{data = pods.datasets.spellman_yeast()}

\notes{The data is from two colour spotted cDNA arrays. It has been widely studied in computational biology. There are four different time series in the data as well as induction experiments. The data is returned in the form of a `pandas` data frame which can be described as follows.}


\code{data['Y'].describe()}

\notes{The first five columns are the clb2 and cln3 induction experiments. The columns that follow are the alpha, cdc15, cdc28 and elutriation time course experiments. The index gives the gene names. The columns are named according to the experiment.}

\code{print(data['Y'].columns)}

\notes{And the index is given by the gene name, there are 6178 genes in total.}


\code{print(data['Y'].index)}

\notes{We also provide a variant of the data for just the cdc15 time course.}

\code{data = pods.datasets.spellman_yeast_cdc15()}

\notes{And in this data we also provide the associated time points.}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(data['t'], data['Y']['YAR015W'],'r.',markersize=10)
ax.set_xlabel('time')
ax.set_ylabel('$\log_2$ expression ratio')

mlai.write_figure('spellman-yeast-data.svg', directory='\writeDiagramsDir/datasets')}

\figure{\includediagram{\diagramsDir/datasets/spellman-yeast-data}{80%}}{Gene YAR015W from @Spellman:yeastcellcy98 for the cdc15 Time Course}{spellman-yeast-data}

\notes{As normal we include the citation information for the data.}


\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys `info` and `details`.}


\code{print(data['info'])
print()
print(data['details'])}

\endif
