\ifndef{bigDataHealthMotivation}
\define{bigDataHealthMotivation}

\editme

\subsubsection{A Motivating Big Data Example}

\notes{To motivate the movement from matrix to vector, we'll consider the type of challenge that might arise in today's era of happenstance data. Mathematical statisticians worked with tables of data that they'd carefully collected, often with
the specific purpose of answering a particular question. The decided
at experiment *design* time what was to be measured $\numData$. We continue to do this today; we even use statistical power calculations to decide how many subjects we need in our data sample.}

\notes{Our motivation will be personalized health: what we can learn
about patients' state of health and when should we suggest
interventions?}

\notes{In the big data era, we are not only interested in what
data we might collect for answering a specific question (although this data remains important) but we are also interested in
existing data that might be assimilated to improve our understanding
of an individual's health. When we imagine systems that can monitor our individual health status, we should not be restricted to the type of data
that might be stored in a doctor's office or a hospital data
base. We can even argue that that hospital data focusses on sickness
rather than health, giving us an incomplete picture.}

\notes{In the modern world of happenstance data, we might like to build models
that incorporate, for example, an individual's exercise regime (for example through
websites such as Strava). We could also include information
about an individual's dietary habits extracted from loyalty card
information like the Nectar card. If we were monitoring potential
degradation in health then we may also be interested in an
individual's social network activity (Twitter, Facebook,
SnapChat). Even musical tastes may feed into our overall picture of
the patient's well-being through music services like Spotify.}

\notes{For a full perspective on a patient's health, this data needs to be
combined with more traditional sources like phenotype and genotype
information. For example, high resolution scans of the genome
provide a detailed characterization of genotype. Large-scale gene-expression measurements, give high resolution understanding of phenotype at
the cellular level. Imaging domains can contain X-rays scans, MRIs or pathologists' samples. Doctor's
notes, both free-form notes and those that encode diagnosis through emerging EHR/EMR coding standards such as the WHO's International Classification of Diseases (ICD-11, see @WHO-icd20). And also, the results of clinical tests, such as cholesterol levels. To
provide a full picture of health status all this information needs to
be assimilated. 

In a traditional model, we might encode each piece of information as
another element on a feature vector: in other words, each data snippet mentioned contributes to increasing $\dataDim$.  However, for most patients,
most of the information above will be missing. We obtain only snippets of information about music tastes and social media habits alongside the occasional clincal measurement. Missing data is often discussed, but not at the scale we are considering here. In a classical analysis we might consider 30% missingness to be a big number. In this new scenario of data snippets almost all the data is missing almost all the time. A typical amount of missingness might be 99.9%. The data snippet domain is one which we might refer to as *massively missing data*. A situation
where a missing value becomes the norm and a data observation is the exception.}

\notes{Alongside the patchy nature of these data snippets, another challenge would be how they arrive. This happenstance data is constantly evolving. In computer systems terminology it is referred to as streaming data. The table form of the design matrix is a consequence of active surveillance of the population. When acquiring data passively it updates haphazardly. 

Our model may need to update because patient 2,342 has just had the results of a
blood test logged, or because patient 28,344,219 has just been for a
run or because patient 12,012,345 just listened to a Leonard Cohen
track or because patient 12,182 just gave birth.}

\notes{For applications like the personalized health monitoring system
described above, we need a model that will give well calibrated
predictions from the first day of it being brought online, and
throughout its operational life. If the model is complex enough to
represent the full spectrum of possible human ailments, then when the
model is first brought on stream, it is unlikely to have sufficient
data to determine the parameters. In the standard modeling framework,
we are faced with the bias-variance dillema [@Geman:bias92]. If the model is complex enough to represent the
underlying data structure, the parameters will be badly determined for
small, or badly designed data sets, and the model will exhibit a large
error due to variance. We are still learning how the deep learning frameworks provide a route out of this dillemma. A part of the story is their overparameterization. But what is the formalism by which we can incorporate more information about each individual patient within these highly parameterized models?}

\notes{A major challenge in the domain we've described is to build a model
that is complex enough to represent the diversity of human health
outcomes. For streaming data this necessarily means that some (or most) of those
parameters will be badly determined. This is reminiscient of the overparameterized deep learning models.}

\endif
