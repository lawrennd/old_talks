\ifndef{movieBodyCountLinearRegression}
\define{movieBodyCountLinearRegression}

talk-macros.gpp}atasets/includes/movie-body-count-data.md}

\editme

\subsection{Multivariate Regression on Movie Body Count Data}

\notes{Now we will build a design matrix based on the numeric features: year, Body_Count, Length_Minutes in an effort to predict the rating. We build the design matrix as follows:}

\notes{Bias as an additional feature.}
\slides{* Regress from features `Year`, `Body_Count`, `Length_Minutes` to IMDB_Rating.}

\code{select_features = ['Year', 'Body_Count', 'Length_Minutes']
\designVariable = movies[select_features]
\designVariable['Eins'] = 1 # add a column for the offset
y = movies[['IMDB_Rating']]}

\notes{Now let's perform a linear regression. But this time, we will create a pandas data frame for the result so we can store it in a form that we can visualise easily.}

\setupcode{import pandas as pd}
\code{w = pd.DataFrame(data=np.linalg.solve(\designVariable.T@\designVariable, \designVariable.T@y),  # solve linear regression here
                 index = \designVariable.columns,  # columns of \designVariable become rows of w
                 columns=['regression_coefficient']) # the column of \designVariable is the value of regression coefficient}

\notes{We can check the residuals to see how good our estimates are. First we create a pandas data frame containing the predictions and use it to compute the residuals.}

\code{ypred = pd.DataFrame(data=(\designVariable@w).values, columns=['IMDB_Rating'])
resid = y-ypred}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
resid.hist(ax=ax)
mlai.write_figure(filename='movie-body-count-rating-residuals.svg', 
				  directory='\writeDiagramsDir/ml')}

\newslide{Residuals}

\figure{\includediagram{\diagramsDir/ml/movie-body-count-rating-residuals}{80%}}{Residual values for the ratings from the prediction of the movie rating given the data from the film.}{movie-body-count-residuals}

\notes{Which shows our model *hasn't* yet done a great job of representation, because the spread of values is large. We can check what the rating is dominated by in terms of regression coefficients.}

\code{w}

\notes{Although we have to be a little careful about interpretation because our input values live on different scales, however it looks like we are dominated by the bias, with a small negative effect for later films (but bear in mind the years are large, so this effect is probably larger than it looks) and a positive effect for length. So it looks like long earlier films generally do better, but the residuals are so high that we probably haven't modelled the system very well.}

                            
\endif
