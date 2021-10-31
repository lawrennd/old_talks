\ifndef{covidVaccinationAndSimpsonsParadox}
\define{covidVaccinationAndSimpsonsParadox}

\editme 

\subsection{Covid Vaccination and Simpson's Paradox}

\notes{In this exercise we're going to consider an analysis example that involves computing probabilities. The scenario is associated with covid vaccination and disease.}

\include{_datasets/includes/hospitalized-covid-data.md}

\notes{`pods` has taken care of loading the data into a `pandas.DataFrame` for us.}

\notes{The data frame contains, indexed by age group, the raw counts of disease for the fully vaccinated (`vax`), the partially vaccinated (`partial vax`) and the unvaccinated (`unvax`). Additionally it provides *rates* of disease per 100,000 population (`per 100k`) for each category.}

\notes{Severe disease is also listed for raw counts and disease rates (`severe`), where severe disease is disease that *requires hospitalisation*. Overall this gives us twelve columns total (six for raw counts, six for rates). Data is from 15th August 2021.}

\codeassignment{Estimate the probability of being fully vaccinated given that you have severe disease, $p(\text{vax}|\text{severe})$. Compare this with $p(\text{unvax}|\text{severe})$. What does this number tell you about the efficacy of the vaccine?}{}{10}

\codeassignment{We are given raw counts of disease and we are also given disease rates per 100,000. Use these columns to estimate the total population of vaccinated, unvaccinated and partially vaccinated individuals. Add these columns to the data frame using consistent naming.

Now estimate the probability of an individual in the Israeli population being vaccinated, $p(\text{vax})$?

Note: You may wish to sanity check your population estimates by comparing the total population they imply against the population of Israel (which is about 9 million). Your total population should be slightly less as we have no data for under 12s.}{}{10}

\codeassignment{Now compute the probability of severe disease given that you have the vaccine $p(\text{severe}|\text{vax})$ against $p(\text{severe}|\text{unvax})$. 

Why is this a more informative comparison for estimating disease efficacy than the estimates we looked at of $p(\text{vax}|\text{severe})$ and $p(\text{unvax}|\text{severe})$?}{}{10}

\notes{The [relative risk](https://en.wikipedia.org/wiki/Relative_risk) of severe disease associated with vaccination is defined as
$$
RR =\frac{p(\text{unvax}|\text{severe})}{p(\text{vax}|\text{severe})}.
$$
If this is less than 1 then vaccination is protective, if it is greater than 1 then vaccination is a "risk factor".}

\codeassignment{Compute the relative risk of vaccination in the whole Israeli population, decide whether vaccination is protective against severe disease.}{}{5}

\codeassignment{Now compute the relative risk of vaccination for *each age group* in the data set. Compare these relative risks to the relative risk in the whole population.}{}{10}

\notes{The unusual phenomenon you see is known as *Simpson's paradox*. It is arising because this data is [*observational data*](https://en.wikipedia.org/wiki/Observational_study). It is not surveillance data. When computing relative risk for the whole population age is operating as a *confounder*. We have not controlled for this confounder, so we end up with a misleading representation of the risk. When looking in each individual age group we find that the vaccine is more protective for each individual age group than it appears to be for the population as a whole. This highlights the risks of observational data vs randomization (known as surveillance data). A major challenge of data science is that we are habitually dealing with observational data, not surveillance data.}

\endif
