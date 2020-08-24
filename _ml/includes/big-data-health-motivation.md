\ifndef{bigDataHealthMotivation}
\define{bigDataHealthMotivation}

\editme

\subsubsection{A Motivating Big Data Example}

\notes{Mathematical statisticians like Pearson, Fisher and Gosset
worked with tables of data that they'd carefully collected, often with
the specific purpose of answering a particular question. The decided
at experiment *design* time what was to be measured $\numData$. The
number of samples was determined by statistical power calculations
*CHECK THIS*, this was something that could be varied.}

\notes{One of my own interests is personalized health: what we can
learn about patients' state of health and when we should make an
intervention. In the big data era, we aren't only interested in what
data we might collect for answering a specific question (although data
of this type remains very important) but we are also interested in
existing data that might be assimilated to improve our understanding
of an individual's health. When imagining future systems that monitor
our health status, we should not be restricted to the type of data
that might be stored in a doctor's office or a hospital data
base. Indeed, it might be argued that such data focusses on sickness
rather than health, giving us an incomplete picture.}

\notes{ Modern data availability means that we could build models
that incorporate an individual's exercise regime (for example through
websites such as Strava). We could include information
about an individual's dietary habits (e.g. through loyalty card
information like the Nectar card). If we were monitoring potential
degradation in health then we may also be interested in an
individual's social network activity (Twitter, Facebook,
Google+). Even musical tastes may feed into our overall picture of
the patient's well-being through music services like Spotify. For a
full perspective on a patient's health, this data would need to be
combined with more traditional sources like phenotype and genotype
information. For example, high resolution scans of the genome
providing a detailed characterization of genotype. Large scale gene
expression measurements, giving detailed insights into phenotype at
the cellular level. Images containing x-rays or biopsies. Doctor's
notes, both free-form notes and those that encode a diagnosis. Clinical
tests, for example in cardiovascular disease, cholesterol level. To
provide a full picture of health status all this information needs to
be assimilated. In a traditional model, we might encode each piece of
information as another element on a feature vector: in other words,
all the above contributes to increasing $\dataDim$.  However, for most
patients, most of the information above is likely to be missing. The
paradigm of missing data is often discussed, but in this domain, we
have a situation we might refer to as *massivelv missing data*. A
situation where a missing value becomes the norm rather than an
exception.}

\notes{Another facet of the personalized health problem will be the
streaming nature of data. When acquiring data passively data doesn't
arrive in blocks, it arrives in a haphazard fashion. Our model may
need to update because patient 2,342 has just had the results of a
blood test logged, or because patient 28,344,219 has just been for a
run or because patient 12,012,345 just listened to a Leonard Cohen
track or because patient 12,182 just gave birth.}

\notes{ One possible motivation for making independence assumptions
across data points is the ease with which predictions can be made for
a previously unseen vector $\dataVector^*$. Given an estimate of a
vector of parameters, $\hat{\paramVector}$, perhaps obtained by
optimizing the likelihood on the training data, then due to our
assumption of independence across data then we can easily predict for
the new point using the conditional distribution: $$
p(\dataVector_*|\hat{\paramVector}).  $$ Perhaps, though, we should
find this ease of prediction suspicious.  Let's momentarily examine
what we are really saying here. We are assuming that all the
information we wish to store about the world, and communicate to a
test data set is storable in a parameter vector, $\paramVector$, the
nature of which (for example its length) is set at design time, before
we've seen the data. That is precisely the meaning of statistical
*independence given the parameters*.}

\notes{For applications like the personalized health monitoring system
described above, we need a model that will give well calibrated
predictions from the first day of it being brought online, and
throughout its operational life. If the model is complex enough to
represent the full spectrum of possible human ailments, then when the
model is first brought on stream, it is unlikely to have sufficient
data to determine the parameters. In the standard modeling framework,
we are faced with the bias variance dilema [@Geman:bias92]. If the model is complex enough to represent the
underlying data structure, the parameters will be badly determined for
small, or badly designed data sets, and the model will exhibit a large
error due to variance. A traditional solution is to err towards bias,
by constructing a simpler model, but one where the parameters can be
well determined by the data, we reduce variance at the expense of some
bias.  In the context of our medical application, there are three
major problems with this approach. Firstly, the size and scope of the
data is continually evolving, we do not have a fixed design. This
means that even if we were to find a good initial compromise between
bias and variance, this compromise may be rapidly
invalidated. Secondly, the compromise we find would have to apply
equally to all patients despite the diversity of data we have
associated with those patients. Finally, we should fear the confidence
of predictions from a model with well determined parameters unless we
truly believe we have sufficient data to capture some underlying
deterministic truth. Medical outcome is laced with uncertainty, and
this uncertainty needs to be modeled correctly because its structure
has a significant effect on treatment.}

\notes{A major challenge in the domain we've described is to build a model
that is complex enough to represent the diversity of human health
outcomes. For streaming data this necessarily means that some of those
parameters will be badly determined. I'd also argue further that if the
parameters are well determined this is actually a warning. If all
parameters are well determined, then our assumption of statistical
independence becomes a strong one: the residual uncertainty is only in
the noise, which by its independent nature, is impossible to model.
However, any uncertainty in the parameters gives a much more structured
uncertainty distribution for the data.}

\endif
