\notes{
\subsection{Nigerian NMIS Data}

First we will load in the Nigerian NMIS health data. Our aim will be to predict whether a center has maternal health delivery services given the attributes in the data. We will predict of the number of nurses, the number of doctors, location etc.

 Let's first remind ourselves of the data.}

\ifdef{nmisdatadownloaded}
\code{data.head()}
\else{
\setupcode{import urllib.request}
\code{urllib.request.urlretrieve('https://energydata.info/dataset/f85d1796-e7f2-4630-be84-79420174e3bd/resource/6e640a13-cab4-457b-b9e6-0336051bac27/download/healthmopupandbaselinenmisfacility.csv', 'healthmopupandbaselinenmisfacility.csv')}

\setupcode{import pandas as pd}
\code{data = pd.read_csv('healthmopupandbaselinenmisfacility.csv')}
data.head()}

\notes{Now we will convert this data into a form which we can use as inputs `X`, and labels `y`.}

\setupcode{import pandas as pd
import numpy as np}

\code{data = data[~pd.isnull(data['maternal_health_delivery_services'])]
X = data[['emergency_transport',
		  'num_chews_fulltime', 
		  'phcn_electricity',
          'child_health_measles_immun_calc',
          'num_nurses_fulltime',
          'num_doctors_fulltime', 
		  'improved_water_supply', 
		  'improved_sanitation',
          'antenatal_care_yn', 
		  'family_planning_yn',
          'malaria_treatment_artemisinin', 
		  'latitude', 
		  'longitude']].copy()
y = data['maternal_health_delivery_services']  # set label to be whether there's a maternal health delivery service

# Create series of health center types with the relevant index
s = data['facility_type_display'].apply(pd.Series, 1).stack() 
s.index = s.index.droplevel(-1) # to line up with df's index

# Extract from the series the unique list of types.
types = s.unique()

# For each type extract the indices where it is present and add a column to X
for htype in types:
    index = s[s==htype].index.tolist()
    X.loc[:, htype] = 0.0 
    X.loc[index, htype] = 1.0}

\notes{This has given us a new data frame `X` which contains the different facility types  in different columns.}

\code{X.describe()}

\notes{We can now specify the naive Bayes model. For the genres we want to model the data as Bernoulli distributed, and for the year and body count we want to model the data as Gaussian distributed. We set up two data frames to contain the parameters for the rows and the columns below.}

\code{# assume data is binary or real.
# this list encodes whether it is binary or real (1 for binary, 0 for real)
binary_columns = ['emergency_transport',
		  'phcn_electricity',
          'child_health_measles_immun_calc',
		  'improved_water_supply', 
		  'improved_sanitation',
          'antenatal_care_yn', 
		  'family_planning_yn',
          'malaria_treatment_artemisinin'] + types
real_columns = ['num_chews_fulltime', 
                'num_nurses_fulltime', 
                'num_doctors_fulltime', 
		        'latitude', 
		        'longitude']
Bernoulli = pd.DataFrame(data=np.zeros((2,len(binary_columns))), columns=binary_columns, index=['theta_0', 'theta_1'])
Gaussian = pd.DataFrame(data=np.zeros((4,len(real_columns))), columns=real_columns, index=['mu_0', 'sigma2_0', 'mu_1', 'sigma2_1'])}

\notes{Now we have the data in a form ready for analysis, let's construct our data matrix.}

\code{num_train = 20000
indices = np.random.permutation(X.shape[0])
train_indices = indices[:num_train]
test_indices = indices[num_train:]
X_train = X.loc[train_indices]
y_train = y.loc[train_indices]
X_test = X.loc[test_indices]
y_test = y.loc[test_indices]}

\notes{And we can now train the model. For each feature we can make the fit independently. The fit is given by either counting the number of positives (for binary data) which gives us the maximum likelihood solution for the Bernoulli. Or by computing the empirical mean and variance of the data for the Gaussian, which also gives us the maximum likelihood solution.}

\code{for column in X_train:
    if column in Gaussian:
        Gaussian[column]['mu_0'] = X_train[column][~y].mean()
        Gaussian[column]['mu_1'] = X_train[column][y].mean()
        Gaussian[column]['sigma2_0'] = X_train[column][~y].var(ddof=0)
        Gaussian[column]['sigma2_1'] = X_train[column][y].var(ddof=0)
    if column in Bernoulli:
        Bernoulli[column]['theta_0'] = X_train[column][~y].sum()/(~y).sum()
        Bernoulli[column]['theta_1'] = X_train[column][y].sum()/(y).sum()}

\notes{We can examine the nature of the distributions we've fitted to the model by looking at the entries in these data frames.}

\code{Bernoulli}

\code{Gaussian}

\notes{The final model parameter is the prior probability of the positive class, $\pi$, which is computed by maximum likelihood.}

\code{prior = float(y_train.sum())/len(y_train)}
