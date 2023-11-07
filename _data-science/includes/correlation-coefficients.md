\ifndef{correlationCoefficients}
\define{correlationCoefficients}

\editme

\subsection{Correlation Coefficients}

\notes{When considering multivariate data, a very useful notion is the *correlation coefficient*. It gives us the relationship between two variables. The most widely used correlation coefficient is due to Karl Pearson, it's defined in the following way.}

\notes{Let's define our data set to be kept in a matrix, $\dataMatrix$ with $\dataDim$ columns. We assume that $\dataVector_{:, j}$ is the $j$th column of that matrix which corresponds to the $j$th *feature* of the data. Then $\dataScalar_{i,j}$ is the $j$th feature for the $i$th data point. Then the sample mean of that feature/column is given by
$$
\mu_j = \frac{1}{\numData} \sum_{i=1}^\numData\dataScalar_{i,j}
$$
where $\numData$ is the total number of data points (often refered to as the sample size in statistics). Then the variance of that column is given by,[^variance-footnote]
$$
\dataStd_j^2 = \frac{1}{\numData} \sum_{i=1}^\numData (\dataScalar_{i,j} - \mu_j)^2.
$$
The covariance between two variables can also be found as
$$
c_{j,k} = \frac{1}{\numData} \sum_{i=1}^\numData (\dataScalar_{i,j} - \mu_j)(\dataScalar_{i, k} - \mu_k).
$$
If we normalise this covariance by the standard deviaton of the two variables ($\dataStd_j, \dataStd_k$) then we recover Pearson's correlation, often known as Pearson's $\rho$ (the Greek letter rho),
$$
\rho_{j,k} = \frac{c_{j,k}}{\dataStd_{j} \dataStd_{k}}.
$$
Computing the correlation between two values is a way to determine if the values have a relationship with each other.

[^variance-footnote]: sometimes the formula used uses $\frac{1}{\numData-1}$ instead of $\frac{1}{\numData}$. This can be motivated by the observation that this estimate is a *biased* estimate of the true variance. Where bias is a statistical concept relating to how the estimate converges as $\numData \rightarrow \infty$. Personally, I prefer to normalize by $\numData$, which emerges e.g. from performing maximum likelihood with a Gaussian model. }

\notes{One of the problems of statistics, is that when we are working with small data, an apparant correlation might just be a statistical anomally, i.e. a conicidence, that arises just because the quantity of data we have collected is low. In mathematical statistics we make use of hypothesis testing to estimate if a given statistic is "statistically significant".}

\notes{In classical hypothesis testing, we define a *null hypothesis*. This is a hypothesis that contradicts the idea we're interested in. So for correlation analysis, the null hypothesis would be "there is no correlation between the features $i$ and $j$". We then measure the $p$ value. The $p$ value is the probability that we would observe a value as extreme as the one we see if the null hypothesis is true. If this value is low (typically below 0.05 or below 0.01 depending on how stringent we want to be) we *reject the null hypothesis* and the statistic is declared to be significant.}

\notes{Hypothesis testing gives us critical values of the correlation coefficient that we need to believe that there is a relationship between the variables. Those values get smaller as $\numData$ gets larger.}

\subsection{Limitations of Pearson's $\rho$}

\notes{Two major limitations of $\rho$ that you'll normally see mentioned. Firstly, the measure is really focussed on linear relationships between variables. It's possible to construct examples of interesting non-linear relationships between two variables for which the correlation is zero. Secondly, we are often interested in a causal relationship between two variables. Two variables which are not directly related will appear correlated if there is a common factor affecting both variables. For example, we might see a correlation between sales figures for swim gear and ice creams. There is no direct relationship between these to variables, but there is a third variable associated with the passing of the seasons that triggers the sales figures of both swim gear and ice creams to increase.}

\notes{Let's look an example using the Nigerian NMIS data.}

\include{_systems/includes/nigeria-nmis-data-systems.md}

\notes{We'll just look at the numbers of nurses, doctors, midwives and community health extension workers (CHEWs).}

\code{hospital_workers_data = hospital_data[["num_chews_fulltime", "num_nurses_fulltime", "num_nursemidwives_fulltime", "num_doctors_fulltime"]]} 

\notes{We can compute the correlation of the columns using `.corr()` on the `pandas.DataFrame`.}

\setupcode{import numpy as np
import pandas as pd}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
im = ax.matshow(hospital_workers_data.corr())
ax.set_xticks([0.5, 1.5, 2.5, 3.5])
ax.set_xticklabels(hospital_workers_data.columns, fontsize=14, rotation=45)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(hospital_workers_data.columns, fontsize=14)

fig.colorbar(im, ax=ax)

mlai.write_figure(filename="nigeria-nmis-correlation-matrix.svg", directory="\writeDiagramsDir/data-science")}

\figure{\includediagram{\diagramsDir/data-science/nigeria-nmis-correlation-matrix}{80%}}{Correlation matrix for the number of community health workers, nurses, midwives and doctors in the Nigerian NMIS health centre data.}{nigeria-nmis-correlation-matrix}

\notes{From plotting this matrix of correlations, we can immediately see that there are good correlations between the numbers of doctors, nurses and midwives, but less correlation with the number of community health workers.}

\notes{There are also specialised libraries for plotting correlation matrices, see for example `corrplot` from `biokit.viz`.}

\notes{Before we proceed, let's just dive deeper into some of these correlations using scatter plots.}

\subsection{Plotting Variables}

\notes{When exploring a data set it's often useful to create a scatter plot of the different variables. In `pandas` this can be done using `pandas.tools.plotting.scatter_matrix`.}

\plotcode{axs = pd.plotting.scatter_matrix(hospital_workers_data, alpha=0.2, figsize=(15, 15))
mlai.write_figure(filename="nigeria-nmis-scatter-matrix.png", directory="\writeDiagramsDir/data-science")}

\figure{\includepng{\diagramsDir/data-science/nigeria-nmis-scatter-matrix}{70%}}{Scatter matrix of the numbers of commuity health extension workers, nurses, doctors and midwives in the Nigerian health facilities data. Numbers are hard to see because they range from small numbers to larger numbers.}{nigeria-nmis-scatter-matrix}

\notes{Immediately we note that the values are difficult to see in the scatter plot. They are ranging from zero for some health facilities but to hundreds for others. To get a better view, we can look at the logarithm of the data. Some counts are zero, so instead of plotting the logarithm directly, we plot $\log_{10}(\cdot + 1)$ as follows.}

\plotcode{axs = pd.plotting.scatter_matrix(np.log10(hospital_workers_data+1), alpha=0.2, figsize=(15, 15))
mlai.write_figure(filename="nigeria-nmis-log-plus-one-scatter-matrix.png", directory="\writeDiagramsDir/data-science")}

\figure{\includepng{\diagramsDir/data-science/nigeria-nmis-log-plus-one-scatter-matrix}{70%}}{Scatter matrix of the $\log_{10}(\cdot + 1)$ of numbers of commuity health extension workers, nurses, doctors and midwives in the Nigerian health facilities data.}{nigeria-nmis-scatter-matrix}

\notes{There are a few odd things in the plots that might be worth investigating. For example, the nurse numbers seem to drop very abruptly after some point. Let's investigate by zooming in on a region of the relevant plot.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(np.log10(hospital_data["num_chews_fulltime"]+1), np.log10(hospital_data["num_nurses_fulltime"]+1), 'bo', alpha=0.2)
ax.set_ylim([1.0, 1.5])
ax.set_xlabel("Number of Community Health Workers")
ax.set_ylabel("Number of Full Time Nurses")

mlai.write_figure(filename="nigeria-nmis-nurse-zoom-in.svg", directory="\writeDiagramsDir/data-science")}


\figure{\includediagram{\diagramsDir/data-science/nigeria-nmis-nurse-zoom-in}{40%}}{Zoom in on the scatter plot of the number of nurses in the health centres. There's an odd "cliff" in the data density between 1.2 and 1.3.}

\notes{From the zoom in we can see that the cliff is occurring somewhere below 1.3 on the plot, let's find what the value of this cliff is.}

\code{hospital_data["num_nurses_fulltime"][np.log10(hospital_data["num_nurses_fulltime"]+1)<1.3].max()}

\notes{Giving us the value of 16. This is slightly odd, and suggests the values may have been censored in some way. We can see this if we bar chart them.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
hospital_data["num_nurses_fulltime"].value_counts().sort_index().plot.bar(ax=ax)
ax.set_ylim([0, 200])
ax.set_xlabel("full time nurse count")
ax.set_ylabel("number of health centres")

mlai.write_figure(filename="nigerian-nmis-number-nurses-health-centre.svg",
                  directory="\writeDiagramsDir/data-science")}

\figure{\includediagram{\diagramsDir/data-science/nigerian-nmis-number-nurses-health-centre}{50%}}{Number of nurses in each health centre. Note the over-representation of centres with 10 nurses, as well as the underrepresentation of centres with over 16 nurses.}{nigerian-nmis-number-nurses-health-centre}

\notes{Not only do we see the cliff after 16 nurses, but there are a few other interesting effects. The number of health centres with 10 nurses is many more than those with either 9 or 11 nurses. This is likely an example of a rounding effect. When people report numbers by hand, they tend to round them. This may well explain the overepresentation of 10. This should give some cause for concern about the data.}

\notes{*Aside*: likely the problems in the NMIS data are to do with mistakes in reporting, but analysis of data can also be used to unpick serious problems in scientific data. See for example this paper [Evidence of Fraud in an Influential Field Experiment About Dishonesty](https://datacolada.org/98) [@Simonsohn-evidence21], which ironically finds evidence of fraud in a paper about dishonesty. One of the techniques they use is looking for overrepresentation of round numbers in hand-reported data. Another technique that can be used when looking for fraudulent data is known as [Benford's law](https://en.wikipedia.org/wiki/Benford%27s_law), which describes the distribution of first digits.}





\endif
