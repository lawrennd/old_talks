\ifndef{nigerianNmisDataClassification}
\define{nigerianNmisDataClassification}

\editme

\notes{
\subsection{Nigerian NMIS Data}

First we will load in the Nigerian NMIS health data. Our aim will be to predict whether a center has maternal health delivery services given the attributes in the data. We will predict of the number of nurses, the number of doctors, location etc.

 Let's first remind ourselves of the data.}

\include{_ml/includes/nigerian-nmis-data.md}

\notes{Now we will convert this data into a form which we can use as inputs `X`, and labels `y`.}

\setupcode{import pandas as pd
import numpy as np}

\code{data = data[~pd.isnull(data['maternal_health_delivery_services'])]
data = data.dropna() # Remove entries with missing values
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
y = data['maternal_health_delivery_services']==True  # set label to be whether there's a maternal health delivery service

# Create series of health center types with the relevant index
s = data['facility_type_display'].apply(pd.Series, 1).stack() 
s.index = s.index.droplevel(-1) # to line up with df's index

# Extract from the series the unique list of types.
types = s.unique()

# For each type extract the indices where it is present and add a column to X
type_names = []
for htype in types:
    index = s[s==htype].index.tolist()
    type_col=htype.replace(' ', '_').replace('/','-').lower()
    type_names.append(type_col)
    X.loc[:, type_col] = 0.0 
    X.loc[index, type_col] = 1.0}

\notes{This has given us a new data frame `X` which contains the different facility types  in different columns.}

\code{X.describe()}

\endif
