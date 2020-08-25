\ifndef{mlAndStatisticsInterface}
\define{mlAndStatisticsInterface}

\editme

\section{The Machine Learning and Statistics Interface}

\notes{Machine learning and Statistics are academic cousins, founded
on the same mathematical princples, but often with different
objectives in mind. But the differences can be as informative as the
overlaps.}

\notes{@Efron:prediction20 rightly alludes to the
fundamental differences to the new wave of predictive models that have
arisen in the last decades of machine learning. And these cultures
were also beautifully described by @Breiman:cultures00. }

\notes{In the discussion of Professor Efron's paper @Friedman:discussion20 highlight the continuum between the classical approaches and the emphasis on prediction. Indeed, the prediction culture does not sit entirely in the
machine learning domain, an excellent example of a prediction-focused approach would be Leo Breiman's bagging of models [@Breiman:bagging96], although it's notable that Breiman, a statistician, chose to publish this paper in a machine
learning journal.}

\notes{From a personal perspective, a strand of work that is highly inspirational in prediction also comes from a statistician. The prequential formalism [@Dawid:callibrated82;@Dawid:prequential84] also emerges from statistics. It provides some hope that a predictive approach can be reconciled with attribution in the manner highlighted also by @Friedman:discussion20. The prequential approach is predictive but allows us to falsify
poorly calibrated models [@Lawrence:licsbintro10]. So while it doesn't give us truth, it does give as falsehood in line with Popper's vision of the philosophy of science [@Popper:conjectures63].}

\notes{There is a quote, that is apocryphally credited to Disraeli by Mark Twain.

> There are three kinds of lies: lies, damned lies and statistics

It stems from the late 19th century. From a time after Laplace, Gauss, Legendre and Galton made their forays into regression, but before Fisher,
Pearson and others had begun to formalize the process of estimation. Today, the academic discipline of statistics is so widely
understood to be underpinned by mathematical rigor that we typically drop the fu full title of *mathematical statistics*, but this history can be informative when looking at the new challenges we face.

The new phenomenon that underpins the challenges that Professor Efron outlines has been called "big data". The vast quantities of data that are accumulating in the course of normal human activities. Where people have seen data, they have also seen the potential to draw inferences, but there is a lack of rigor about some of the approaches that means today we can see a new phenomenon.

> There are three kinds of lies: lies, damned lies and big data

The challenge we face is to repeat the work of Fisher, Pearson, Gosset, Neyman etc and give the new wave of approaches a rigorous mathematical foundation.}

\endif
