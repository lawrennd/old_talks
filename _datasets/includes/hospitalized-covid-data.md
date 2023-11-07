\ifndef{hospitalizedCovidData}
\define{hospitalizedCovidData}

\editme

\subsection{Data on Covid Hospitalizations from Israel}

\notes{The data is originally from the Israeli government data dashboard, but we've made it available throught he `pods` library.}

\notes{This version of the data was created for a blog post, @Morris-israeli21, that analyzed that investigated hospitalization of vaccinated and unvaccinated patients with Covid19.}


\setupcode{import pods}

\code{data = pods.datasets.hospitalized_covid()["X"]}



\endif
