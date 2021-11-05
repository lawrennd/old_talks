\ifndef{nigeriaHealthIntro}
\define{nigeriaHealthIntro}

\edtime

\notes{\subsection{Nigerian Health Facility Distribution}

\notes{In this notebook, we explore the question of health facility distribution in Nigeria, spatially, and in relation to population density.}

\notes{We explore and visualize the question "How does the number of health facilities per capita vary across Nigeria?"}

\notes{Rather than focussing purely on using tools like `pandas` to manipulate the data, our focus will be on introducing some concepts from databases.}

\notes{Machine learning can be summarized as
$$
\text{model} + \text{data} \xrightarrow{\text{compute}} \text{prediction}
$$
and many machine learning courses focus a lot on the model part. But to build a machine learning system in practice, a lot of work must be put into the data part. This notebook gives some pointers on that work and how to think about your machine learning systems design.}

\notes{\subsection{Datasets}}

\notes{In this notebook, we download 4 datasets:}

\notes{* Nigeria NMIS health facility data
* Population data for Administrative Zone 1 (states) areas in Nigeria
* Map boundaries for Nigerian states (for plotting and binning)
* Covid cases across Nigeria (as of May 20, 2020)}

\notes{But joining these data sets together is just an example. As another example, you could think of [SafeBoda](https://safeboda.com/ng/), a ride-hailing app that's available in Lagos and Kampala. As well as looking at the health examples, try to imagine how SafeBoda may have had to design their systems to be scalable and reliable for storing and sharing data.}

\endif
