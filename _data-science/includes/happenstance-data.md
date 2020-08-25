\ifndef{happenstanceData}
\define{happenstanceData}

\editme

\subsection{Happenstance Data}

\notes{Following the revolution of mathematical statistics, data
became a carefully curated commodity. It was actively collected in
response to a scientific hypothesis. Popper suggests [Popper:conjectures63] that the answer to which comes first, the hypothesis or the data, is the same as the chicken and the egg. The answer is that they co-evolve. 

Until now, the expense of data collection has meant that a classical approach to statistical testing is normally followed. The question is formulated, typically as a null hypothesis, a power calculation is performed, and the study has launched. 

What Tukey described as confirmatory data analysis [Tukey:exploratory77] is still the mainstay of statistics. While the philosophy of statistical hypothesis testing has been the subject of longstanding debates, there is no controversy around the notion that in order to remove confounders you must have a well-designed experiment, and randomization for statistical data collection is the foundation of confimatory work. Today, randomized trials are deployed today more than ever
before, in particular due to their widespread use in computer interface design. Without our knowledge, we are daily assigned to social experiments that place us in treatment and control groups to determine what dose of different interface ideas will keep us more tightly engaged with our machines. These A/B tests social experiments involve randomization
across many millions of users and dictate our modern user experience (see e.g. @Kohavi-online17). }

\notes{Such experiments are still carefully designed to remain valid,
but the modern data environment is not only about larger experimental
data, but perhaps more so about what I term "happenstance data". Data
that was not collected with a particular purpose in mind, but which is
simply being recorded in the normal course of events due to increasing
interconnection between portable digital devices and decreasing cost
of storage. }

\notes{Happenstance data are the breadcrumbs of our trail through the
forest of life. They may be being written for a particular purpose,
but later we wish to consume them for a different purpose. For
example, within the recent Covid-19 pandemic, the Royal Society DELVE
initiative [@Delve:economics20] was able to draw on transaction data
to give near-real time assessments on the effect of the pandemic and governmental response on GDP[^payments] (see also
@Carvalho:tracking20). The data wasn't recorded with pandemic responses in mind, but it can be used to help inform interventions. Other data sets of use include mobility data from mobile telecoms companies (see e.g. @Oliver-mobile20).

[^payments]: Although challenges with availability of payments data
    within the UK meant that the researchers were able to get good
    assessment of the Spanish and French economies, but struggled to
    assess their main target, the United Kingdom.}

\notes{Historically, data was expensive. It was carefully collected
according to a design. Statistical surveys can still be expensive, but
today there is a strong temptation to do them on the cheap, to use
happenstance data to achieve what had been done in the past only
through rigorous data-fieldwork, but care needs to be taken [@Wang-forecasting15]. A Professor Efron points out, early
attempts to achieve this, such as the Google flu predictor have been
somewhat naive [@Ginsberg:detecting09;@Halevy:unreasonable09].[^elections] As
these methodologies are gaining traction in the social sciences
[@Salganik:bitbybit18] and the field of Computational Social Science
[@Alvarez:computational16] emerges we can expect more innovation and
more ideas that may help us bridge the fundamentally different
characters of qualitative and quantitative research. For the moment,
one particularly promising approach is to use measures derived from
happenstance data (such as searches for flu) as proxy indicators for
statistics that are rigorously surveilled. With the Royal Society's
DELVE initiative, examples of this approach include work of Peter
Diggle to visualize the progression of the Covid-19 disease. Across
the UK the "Zoe App" has been used for self-reporting of Covid
symptoms [@Menni:tracking20], and by interconnecting this data with
Office for National Statistics surveys [@ONS:covid19infection20],
Peter has been able to calibrate the Zoe map of Covid-19 prevalence,
allowing nowcasting of the disease that was validated by the
production of ONS surveys. These enriched surveys can already be done
without innovation to our underlying mathematical 

[^elections]: Although despite conventional wisdom it appears that election polls haven't got worse over recent years, see @Will-election18. 
}

\notes{Classical statistical methodologies remain the gold-standard by
which these new methodologies should be judged. The situation reminds
me somewhat of the challenges Xerox faced with the advent of the
computer revolution. With great prescience, Xerox realized that the
advent of the computer meant that information was going to be shared
more often via electronic screens. As a company whose main revenue stream was
coming from photocopying documents, the notion of the paperless office
represented something of a threat to Xerox. They responded
by funding a research center, known as Xerox PARC. They developed many of the innovations
that underpin the modern information revolution: the Xerox Alto (the
first graphical user interface), the laser printer, ethernet. All of these
inventions were commercial successes, but created a need for *more* paper, not less. The computers produced more information, and much of it was
still shared on paper. Per capita paper consumption continued to rise
in the US until it peaked at around the turn of the millennium
[@Andres:internet14]. A similar story will now apply with the
advent of predictive models and data science. The increasing use of
predictive methodologies does not obviate the need for confirmatory data analysis, it makes them more important than ever
before.}

\notes{Not only is there an ongoing role for the
classical methodologies we have at our disposal, it is likely to be an increasing demand in the near future. But what about new mathematical theories? How
can we come to a formalism for the  new approacches of mathematical data science, just
as early 20th century statisticians were able to reformulate
statistics on a rigorous mathematical footing?}

\endif
