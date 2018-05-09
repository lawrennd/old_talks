\section{Quantifying the Value of Data}

\notes{The situation is reminiscent of a thirsty castaway, set adrift. There is a sea of data, but it is not fit to drink. We need some form of data desalination before it can be consumed. But like real desalination, this is a non trivial process, particularly if we want to achieve it at scale. 

\slides{
### Quantifying the Value of Data

There's a sea of data, but most of it is undrinkable

\includeimg{../slides/diagrams/sea-water-ocean-waves.jpg}{50%}

We require data-desalination before it can be consumed!
}

\notes{I spoke about the challenges in data science at the NIPS 2016 Workshop on Machine Learning for Health. NIPS mainly focuses on machine learning methodologies, and many of the speakers were doing so. But before my talk, I listened to some of the other speakers talk about the challenges they had with data preparation. 

\slides{### Data}

* 90% of our time is spent on validation and integration (Leo Anthony Celi)
* "The Dirty Work We Don't Want to Think About" (Eric Xing)
* "Voodoo to get it decompressed" (Francisco Giminez?)
\slides{* In health care clinicians collect the data and often control the direction of research through guardianship of data.}

A further challenge in healthcare is that the data is collected by clinicians, often at great inconvenience to both themselves and the patient, but the control of the data is sometimes used to steer the direction of research.

The fact that we put so much effort into processing the data, but so little into allocating credit for this work is a major challenge for realizing the benefit in the data we have.

This type of work is somewhat thankless, with the exception of the clinicians' control of the data, which probably takes things too far, those that collate and correct data sets gain little credit. In the domain of *reinforcement learning* the aim is to take a series of actions to achieve a stated goal and gain a reward. The *credit assignment problem* is the challenge in the learning algorithm of distributing credit to each of the actions which brought about the reward. We also experience this problem in society, we use proxies such as monetary reward to incentivise intermediate steps in our economy. Modern society functions because we agree to make basic expenditure on infrastructure, such as roads, which we all make use of. Our data-society is not sufficiently mature to be correctly crediting and rewarding those that undertake this work.


\slides{### Value

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management
  * Incentivization for sharing and production.
  * Quantifying the value in the contribution of *each actor*.
}

\notes{We need to properly incetivize the sharing and production of clean data sets, we need to correctly quantify the value in the contribution of each actor, otherwise there won't be enough clean data to satiate the thirst of our decision making processes.}

\notesfigure{\includesvg{../slides/diagrams/pomdp004.svg}
\center{*Partially observable Markov decision process observing reward as actions are taken in different states*}}

\setupcode{import pods}
\displaycode{pods.notebook.display_plots('pomdp{samp:0>3}.svg', 
                            directory='../slides/diagrams/', samp=(1, 4))}

\slides{
## {.slide: data-transition="none"}

\includesvg{../slides/diagrams/pomdp001.svg}

## {.slide: data-transition="none"}

\includesvg{../slides/diagrams/pomdp002.svg}

## {.slide: data-transition="none"}

\includesvg{../slides/diagrams/pomdp003.svg}

## {.slide: data-transition="none"}

\includesvg{../slides/diagrams/pomdp004.svg}
}

\slides{
## Credit Allocation

* Direct work on data generates an enormous amount of 'value' in the data economy but this is unaccounted in the economy

* Hard because data is difficult to 'embody'

* Value of shared data: [Wellcome Trust 2010 Joint Statement](https://wellcome.ac.uk/what-we-do/our-work/sharing-research-data-improve-public-health-full-joint-statement-funders-health) (from the "Foggy Bottom" meeting)
}

\notes{The value of shared data infrastructures in computational biology was recognized by the 2010 joint statement from the Wellcome Trust and other funders of research at the "Foggy Bottom" meeting. They recognised three key benefits to sharing of health data: 

* faster progress in improving health
* better value for money
* higher quality science

But incentivising sharing requires incentivising collection and collation of data, and the associated credit allocation models.}

\include{_data-science/includes/data-readiness-levels.md}
\include{_data-science/includes/data-joel-tests.md}

\slides{
## Solutions

* Encourage greater interaction between application domains and data scientists

* Encourage visualization of data

* Adoption of 'data readiness levels'

* Implications for incentivization schemes
}
