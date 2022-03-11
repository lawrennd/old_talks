\ifndef{nigeriaNmisDataNaiveBayes}
\define{nigeriaNmisDataNaiveBayes}

\include{_datasets/includes/nigeria-nmis-data-classification.md}

\editme

\notes{\subsection{Naive Bayes NMIS}}

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
          'malaria_treatment_artemisinin'] + type_names
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
X_train = X.iloc[train_indices]
y_train = y.iloc[train_indices]==True
X_test = X.iloc[test_indices]
y_test = y.iloc[test_indices]==True}

\notes{And we can now train the model. For each feature we can make the fit independently. The fit is given by either counting the number of positives (for binary data) which gives us the maximum likelihood solution for the Bernoulli. Or by computing the empirical mean and variance of the data for the Gaussian, which also gives us the maximum likelihood solution.}

\code{for column in X_train:
    if column in Gaussian:
        Gaussian[column]['mu_0'] = X_train[column][~y_train].mean()
        Gaussian[column]['mu_1'] = X_train[column][y_train].mean()
        Gaussian[column]['sigma2_0'] = X_train[column][~y_train].var(ddof=0)
        Gaussian[column]['sigma2_1'] = X_train[column][y_train].var(ddof=0)
    if column in Bernoulli:
        Bernoulli[column]['theta_0'] = X_train[column][~y_train].sum()/(~y_train).sum()
        Bernoulli[column]['theta_1'] = X_train[column][y_train].sum()/(y_train).sum()}

\notes{We can examine the nature of the distributions we've fitted to the model by looking at the entries in these data frames.}

\code{Bernoulli}

The distributions show the parameters of the *independent* class conditional probabilities for no maternity services. It is a Bernoulli distribution with the parameter, $\pi$, given by (`theta_0`) for the facilities without maternity services and `theta_1` for the facilities with maternity services. The parameters whow that, facilities with maternity services also are more likely to have other services such as grid electricity, emergency transport, immunization programs etc. 

The naive Bayes assumption says that the joint probability for these services is given by the product of each of these Bernoulli distributions.

\code{Gaussian}

We have modelled the numbers in our table with a Gaussian density. Since several of these numbers are counts, a more appropriate distribution might be the Poisson distribution. But here we can see that the average number of nurses, healthworkers and doctors is *higher* in the facilities with maternal services (`mu_1`) than those without maternal services (`mu_0`). There is also a small difference between the mean latitude and longitudes. However, the *standard deviation* which would be given by the square root of the variance parameters (`sigma_0` and `sigma_1`) is large, implying that a difference in latitude and longitude may be due to sampling error. To be sure more analysis would be required.

\notes{The final model parameter is the prior probability of the positive class, $\pi$, which is computed by maximum likelihood.}

\code{prior = float(y_train.sum())/len(y_train)}

\notes{The prior probability tells us that slightly more facilities have maternity services than those that don't.}

\endif
