
\ifndef{massivelyMissingData}
\define{massivelyMissingData}


\editme

\subsection{Massively Missing Data}

Classical statistical methods act as our principal guardian against misrepresentation of data, particularly in domains such as clinical trials.}

\notes{However, classical statistics does seem to give us a peculiar
bias to tables of data: data where someone has carefully collected all
the relevant features about the particular entities we are focused
on. That is a very different challenge to that of machine learning. In
talks about this I like to tell the audience that my mum drives a
Humvee. I then ask them what the audience thinks about that, what it
makes them think about my mother.  Probably they think she's
unusual. Maybe it also affects what they think about me. Of course,
she actually drives a VW Golf, which makes her much more of a normal
mother. Importantly, the audience didn't know I was going to say that
before I started, but they were able to assimilate new information
about the entity (my mum) through a feature they may have known
existed, but they were unlikely to have predicted I was going to use
before the talk. If we think about clinical data, the situation is
even more extreme. If we are going to track someone's health state
throughout their life, then we need to build models that might need to
take into account clinical tests that don't even exist yet. This is
not an unusual situation; in fact it is the normal situation. The
table of carefully collected statistical values is the unusual (and
valuable) situation. That's why so much attention is normally given to
experimental design in statistics. But if we don't have those controls
what should we do? First, we should recognize that missing data is the
norm, not the exception: even when the table of data we collected is
full there are probably many more things we *could have* collected but
didn't. Second, we should recognize that the missing data normally
dominates. It would be impossible to enumerate all the different types
of data we would be missing for any complex system. The technique of
imputation is suitable when missing data is only up to around half of
our data set. The real world presents the challenge of massively
missing data. Whenever you are doing analysis you are looking only a
very tiny fraction of the things you could know. Interestingly, the
visual and auditory systems present interesting counter examples to
this analysis. Ignoring context (and concepts like sensor fusion) we
can certainly think of the auditory and visual systems as presenting
fixed dimensional signals about the entities they observe. This may
explain why such success has been possible in these domains. But, from
another perspective, both visual and auditory systems are *just* a
very complex sensor. And in the type of intelligence we envisage we
could have an arbritary number of sensors, and new sensors could be
developed at all times. To understand the entire scene, we must be able
to incorporate such sensors as they are produced. Computational
researchers who have worked in the biological sciences will know that
over recent years sensorics has developed at such a rate that the most
success can be garnered by being the first to apply any method
(typically PCA) to the new sensors, and that we all barely have
time to catch our breath before the next generation of sensors (cDNA microarrays, Affymetrix, RNA-seq, single cell RNA-seq) renders our work on the previous generation obsolete. What doesn't
change though, is the validity of the underlying modelling techniques
that attempt to assimilate these data into a coherent whole.}

\notes{Consider the challenges of a highly multimodal domain like health data.
Whilst we have ensured through clever engineering that speech and \tk{FIXME}}

\notes{The wave of Developing the hypothesis that the main reason that these
models became neglected was because there was not enough data to justify
their implementation, we advocate a return to 

tmotivate a return It is
arguable that the main reason that \tk{FIXME}}

\endif
