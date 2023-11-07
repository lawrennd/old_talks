\ifndef{bmiStepsAnalysis}
\define{bmiStepsAnalysis}

\include{_datasets/includes/bmi-steps-data.md}

\editme


\subsection{BMI Steps Data Analysis}

\notes{We can also separate out the means from the male and female populations. In python this can be done by setting male and female indices as follows.}

\code{male_ind = (gender==0)
female_ind = (gender==1)}

\notes{And now we can extract the variables for the two populations.}

\code{male_steps = steps[male_ind]
male_bmi = bmi[male_ind]}

\notes{And as before we compute the mean.}

\code{print('Male steps mean is {mean}.'.format(mean=male_steps.mean()))}
\code{print('Male BMI mean is {mean}.'.format(mean=male_bmi.mean()))}

\notes{Similarly, we can get the same result for the female portion of the populaton.}

\code{female_steps = steps[female_ind]
female_bmi = bmi[female_ind]}

\code{print('Female steps mean is {mean}.'.format(mean=female_steps.mean()))}
\code{print('Female BMI mean is {mean}.'.format(mean=female_bmi.mean()))}

\notes{Interesting, the female BMI average is slightly higher than the male BMI average. The number of steps in the male group is higher than that in the female group. Perhaps the steps and the BMI are anti-correlated. The more steps, the lower the BMI.}

\notes{Python provides a statistics package. We'll import this in `python` so that we can try and understand the correlation between the `steps` and the `BMI`.}

\setupcode{from scipy.stats import pearsonr}

\code{corr, _ = pearsonr(steps, bmi)
print("Pearson's overall correlation: {corr}".format(corr=corr))}


\code{

male_corr, _ = pearsonr(male_steps, male_bmi)
print("Pearson's correlation for males: {corr}".format(corr=male_corr))}

\code{
female_corr, _ = pearsonr(female_steps, female_bmi)
print("Pearson's correlation for females: {corr}".format(corr=female_corr))}

\newslide{}

\setupdisplaycode{import mlai.plot as plot
import mlai
import matplotlib.pyplot as plt}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(X[male_ind, 0], X[male_ind, 1], 'g.',markersize=10)
_ = ax.plot(X[female_ind, 0], X[female_ind, 1], 'r.',markersize=10)
_ = ax.set_xlabel('steps', fontsize=20)
_ = ax.set_ylabel('BMI', fontsize=20)
xlim = (0, 15000)
ylim = (15, 32.5)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(filename='bmi-steps.svg',
                directory='\writeDiagramsDir/datasets',
                transparent=True)}


\slides{\figure{\includediagram{\diagramsDir/datasets/bmi-steps}{80%}}{BMI/ steps data. The data consists of step readings for different subjects plotted against their BMI}{bmi-step-data}}

\endif
