\ifndef{nigeriaNmisLinearRegression}
\define{nigeriaNmisLinearRegression}

talk-macros.gpp}atasets/includes/nigeria-nmis-data.md}

\editme

\subsection{Multivariate Regression on Nigeria NMIS Data}

\notes{Now we will build a design matrix based on the numeric features that include the number of nurses, and the number of midwives, the latitude and longitude. These are our *covariates*. The response variable will be the number of doctors.  We build the design matrix as follows:}

\notes{Bias as an additional feature.}
\slides{* Regress from features `num_nurses_fulltime`, `num_nursemidwives_fulltime`, `latitude` and `longitude` to `num_doctors_fulltime`.}

\notes{First we select the covariates and response variables and drop any rows where there are missing values using the `pandas` `dropna` method.}

\code{covariates = ['num_nurses_fulltime', 'num_nursemidwives_fulltime', 'latitude', 'longitude']
response = ['num_doctors_fulltime']
data_without_missing = data[covariates + response].dropna()}

\notes{We can see how many rows we have dropped and have a quick sanity check on our new data frame with `len`.}

\code{print(len(data) - len(data_without_missing))}

\notes{We see that 2,735 of the entries had missing values in one of our variables of interest.}

\notes{You may also want to use `describe` or other functions to explore the new data frame.}

\notes{Now let's perform a linear regression. But this time, we will create a pandas data frame for the result so we can store it in a form that we can visualize easily.}

\code{Phi = data_without_missing[covariates]
Phi['Eins'] = 1 # add a column for the offset
y = data_without_missing[response]}

\setupcode{import pandas as pd}
\code{w = pd.DataFrame(data=np.linalg.solve(\designVariable.T@\designVariable, \designVariable.T@y),  # solve linear regression here
                 index = \designVariable.columns,  # columns of \designVariable become rows of w
                 columns=['regression_coefficient']) # the column of \designVariable is the value of regression coefficient}

\notes{We can check the residuals to see how good our estimates are. First we create a pandas data frame containing the predictions and use it to compute the residuals.}

\code{ypred = pd.DataFrame(data=(\designVariable@w).values, columns=['num_doctors_fulltime'])
resid = y-ypred}

\notes{Let's look at the residuals. We can use `describe` to get a summary.}

\code{resid.describe()}


\notes{We can see that while the standard deviation of our residuals is around 3, (this is equivalent to a root mean square error). The smallest and largest residual sow there are some significant outliers that our regression isn't picking up.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
resid.hist(ax=ax,bins=200)
ax.set_xlim((-10,10))
mlai.write_figure(filename='nigeria-nmis-num-doctors-residuals.svg', 
				  directory='\writeDiagramsDir/ml')}

\newslide{Residuals}

\figure{\includediagram{\diagramsDir/ml/nigeria-nmis-num-doctors-residuals}{80%}}{Residual values for the ratings from the prediction of the movie rating given the data from the film.}{nigeria-nmis-num-doctors-residuals}

\notes{Which shows our model *hasn't* yet done a great job of representation, because the spread of values is large. We can check what the rating is dominated by in terms of regression coefficients.}

\code{w}

\notes{Checking our regression coefficients, we see that the number of doctors is positively influenced by the number of nurses and the number of midwives. The latitude and longitude have a smaller effect. The bias term ('eins') is a small positive offset.}

                            
\endif
