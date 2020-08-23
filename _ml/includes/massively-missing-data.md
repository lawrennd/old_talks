
\ifndef{massivelyMissingData}
\define{massivelyMissingData}


\editme

\subsection{Massively Missing Data}

Our
understanding of data still seems heavily influenced by the goals of
early statistics. In particular, early mathematical statistics was
heavily influenced by the need to overcome inductive biases in the
human. To do this they encouraged statisticians to collect tables of
data, with a focus on randomised control trials, to remove such
inductive biases and ensure any conclusions drawn were valid. These
developments were absolutely vital in ensuring rigorous evaluation of
statistical claims. Whether it is concious or unconcious we see myriad
examples from marketing and advertising which are designed to appeal
to the, apparently, irrational aspects[^irrational] of humans and
trick them to doing something which is not to their individual
benefit, but is profitable for the (normally corporate) entity that is
doing the marketing. This may not matter a great deal when we are
buying pet insurance or a new jacket, but is extremely dangerous when
we are making claims for a particular drug to patients.  Classical
statistics acts as our final guardian against these claims, and even
then it is subject to manipulation through failure to report on
negative results.[^results]

[^irrational]: Whether they are
irrational or not depends on how we view them. They are the consequence
of millions of years of evolution and it is only within the last 250
years that we understood the rational basis of probability and companies
were able to exploit areas where people appear irrational to their own
benefit. A particularly depressing read is a section of Laplace's
*Philosophical Essay on Probabilities* [@Laplace-essai14] where he advocates a new
utopia based on rational thinking espousing that

> even the common man under the guidance of great minds will begin to
> understand ... [@] TODO check quote.}

It is an inspiring quote, until you realise that the reality was more of
a dystopia where large (normally commercial) organisations have become
expert in exploiting those irrational aspects that Laplace began to
identify and individual people have little to no understanding of the
rational basis of uncertainty that Laplace was so convinced would become
endemic. 

[^results]: I was once railing against the limitations of classical
statistics to Darren Wilkinson and Joe Whittaker at a very pleasant
meeting in the Lorenz institute, organized by Ernst Wit. It was Joe
Whittaker that drove home this important point to me, although the
connection to the Laplace quote is my own. That came from reading his
Philosophical Essay on Probabilities, and for a moment I became
carried away with him, when he glorified in the new world of
rationality, until I was brought back to the present reality with an
unpleasant jolt, in particular due to the stories about 'Fixed Odds
Betting Machines' that were in the British media at the time. Laplace
singles out games where the odds are stacked against the player a
'particular evil' TODO check. I'm not one for absolutes, but I think
I'd agree with the idea that a larger entity, which has a deep
understanding of rational behavior, exploiting a vulnerable smaller
entity, who has little understanding of it, does come close to such
evils.}

\notes{However, classical statistics does seem to give us a peculiar
bias to tables of data: data where someone has carefully collected all
the relevant features about the particular entites we are focussed
on. That is a very different challenge to that of machine learning. In
talks about this I like to tell the audience that my mum drives an
Humvee. I then ask them what the audience thinks about that, what it
makes them think about my mum.  Certainly they probably think she's
unusual. Maybe it also affects what they think about me. Of course,
she actually drives a VW Golf, which makes her much more of a normal
mum. Importantly, the audience didn't know I was going to say that
before I started, but they were able to assimilate new information
about the entity (my mum) through a feature they may have known
existed, but they were unlikely to have predicted I was going to use
before the talk. If we think about clinical data, the situation is
even more extreme. If we are going to track someone's health state
throughout their life then we need to build models that might need to
take into account clinical tests that don't even exist yet. This is
not an unusual situation, in fact it is the normal situation. The
table of carefully collected statistical values is the unusual (and
valuable) situation. That's why so much attention is normally given to
experimental design in statistics. But if we don't have those controls
what should we do? First we should recognize that missing data is the
norm, not the exception: even when the table of data we collected is
full there are probably many more things we *could have* collected but
didn't. Secondly we should recognise that the missing data normally
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
could have an arbitary number of sensors, and new sensors could be
developed at all times. To understand the entire scene we must be able
to incorporate such sensors as they are produced. Computational
researchers who have worked in the biological sciences will know that
over recent years sensorics has developed at such a rate that the most
success can be garned by being the first to apply any method
(typically PCA) to the sensoring domain, and that we all barely have
time to catch our breath before the next generation of sensorics may
render our work on the previous generation obsolete. What doesn't
change though, is the validity of the underlying modelling techniques
that attempt to assimilate these data into a coherent whole.}

\notes{Consider the challenges of a highly multimodal domain like health data.
Whilst we have ensured through clever engineering that speech and}

\notes{The wave of Developing the hypothesis that the main reason that these
models became neglected was because there was not enough data to justify
their implementation we advocate a return to tmotivate a return It is
arguable that the main reason that}

\endif
