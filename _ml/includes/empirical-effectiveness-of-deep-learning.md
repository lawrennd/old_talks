\ifndef{empiricalEffectivenessOfDeepLearning}
\define{empiricalEffectivenessOfDeepLearning}

\editme

\subsection{Empirical Effectiveness of Deep Learning}

\notes{The OpenAI model represents just a recent example from a wave
of *deep* neural network models has proved highly performant across a
range of challenges that were previously seen as being beyond our
statistical modelling capabilities.}

\notes{They stem from the courage of a group of researchers who saw
that methods were improving with increasing data and chose to collect
and label data sets of ever increasing size, in particular the
ImageNet team led by Fei-Fei Li [@Russakovsky-imagenet15] who
collected a large data set of images for object detection (currently
14 million images). To make these neural network methods work on such
large data sets new implementations were required. By deploying neural
network training algorithms on graphics processing units (GPUs)
breakthrough results were achieved on these large data sets
[@Krizhevsky:imagenet12]. Similar capabilities have then been shown in
the domains of face identification [@Taigman:deepface14], and speech
recognition [@Hinton:acoustic12], translation [@Sutskever:sequence14]
and language modelling [@Radford:language19;@Devlin:bert19].}

\notes{Impressive though these performances are, they are reliant on
massive data and enormous costs of training. Yet they can be seen
through the lens of regression, as outlined by Professor Efron in his
paper. They map from inputs to outputs. For language modelling,
extensive use of auto-regression allows for sequences to be
generated.}

\endif
