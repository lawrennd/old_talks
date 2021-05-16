\ifndef{bmiStepsData}
\define{bmiStepsData}
\editme

\subsection{BMI Steps Data}

\setupcode{import pods}

\code{data = pods.datasets.bmi_steps()
X = data['X'] 
y = data['Y']}

\setupcode{from scipy.stats import pearsonr}

\code{corr, _ = pearsonr(X[:, 0], X[:, 1])
print("Pearson's overall correlation: {corr}".format(corr=corr))}


\code{male_ind = np.where(y.flatten()==0)
male_corr, _ = pearsonr(X[male_ind, 0].flatten(), X[male_ind, 1].flatten())
print("Pearson's correlation for males: {corr}".format(corr=male_corr))}

\code{female_ind = np.where(y.flatten()==1)
female_corr, _ = pearsonr(X[female_ind, 0].flatten(), X[female_ind, 1].flatten())
print("Pearson's correlation for females: {corr}".format(corr=female_corr))}

\newslide{}

\setupdisplaycode{import mlai.teaching_plots as plot
import matplotlib.pyplot as plt}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(X[np.where(y==0), 0], X[np.where(y==0), 1], 'r.',markersize=10)
_ = ax.plot(X[np.where(y==1), 0], X[np.where(y==1), 1], 'r.',markersize=10)
_ = ax.set_xlabel('time', fontsize=20)
_ = ax.set_ylabel('acceleration', fontsize=20)
xlim = (0, 15000)
ylim = (15, 32.5)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(filename='\writeDiagramsDir/datasets/bmi-steps.svg', 
            transparent=True, frameon=True)}


\figure{\includediagram{\diagramsDir/datasets/bmi-steps}{80%}}{BMI/ steps data. The data consists of step readings for different subjects plotted against their BMI}{bmi-step-data}

\endif
