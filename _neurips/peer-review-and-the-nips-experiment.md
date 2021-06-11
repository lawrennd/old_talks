---
title: Peer Review and The NIPS Experiment
abstract: The peer review process can be difficult to navigate for newcomers. In this
  informal talk we will review the results of the NIPS experiment, an experiment on
  the repeatability of peer review conducted for the 2014 conference. We will try
  to keep the presentation information to ensure questions can be asked. With luck
  it will give more insight into the processes that a program committee goes through
  when selecting papers.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
blog: 2014-12-16-the-nips-experiment.md
categories:
- Lawrence-peer15
day: '21'
errata: []
extras:
- label: Software
  link: https://github.com/sods/conference/
ipynb: True
key: Lawrence-peer15
layout: talk
month: 9
published: 2015-09-21
venue: MLPM Summer School, Museum of Science and Industry, Manchester, UK
year: '2015'
---
\notes{The NIPS experiment was an experiment to determine the consistency of the review process. After receiving papers we selected 10% that would be independently rereviewed. The idea was to determine how consistent the decisions between the two sets of independent papers would be. In 2014 NIPS received 1678 submissions and we selected 170 for the experiment. These papers are referred to below as 'duplicated papers'.}

\notes{To run the experiment we created two separate committees within the NIPS program committee. The idea was that the two separate committees would review each duplicated paper independently and results compared.}

\include{_neurips/includes/neurips-in-numbers.md}

\subsection{Speculation}

* To check public opinion before experiment: [scicast question](https://scicast.org/#!/questions/1083/comments/power)

\include{_neurips/includes/neurips-experiment-results.md}
\include{_neurips/includes/neurips-experiment-reaction.md}
\include{_neurips/includes/neurips-experiment-random-committee.md}

\subsection{Conclusion}

\notes{Under the simple model we have outlined, we can be confident that there is inconsistency between two independent committees, but the level of inconsistency is much less than we would find for a random committee. If we accept that the bias introduced by the Area Chairs knowing when they were dealing with duplicates was minimal, then if we were to revisit the NIPS 2014 conference with an independent committee then we would expect between **38% and 64% of the presented papers to be the same**. If the conference was run at random, then we would only expect 25% of the papers to be the same.

It's apparent from comments and speculation about what these results mean, that some people might be surprised by the size of this figure. However, it only requires a little thought to see that this figure is likely to be large for any highly selective conference if there is even a small amount of inconsistency in the decision making process. This is because once the conference has chosen to be 'highly selective' then because by definition only a small percentage of papers are to be accepted. Now if we think of a type I error as accepting a paper which should be rejected, such errors are easier to make because by definition many more papers should be rejected. Type II errors (rejecting a paper that should be accepted) are less likely becaue (by setting the accept rate low) there are fewer papers that should be accepted in the first place. When there is a difference of opinion between reviewers, it does seem that many of the arugments can be distilled down to (a subjective opinion) about whether controlling for type I or type II errors is more important. Further, normally when discussing type I and type II errors we believe that the underlying system of study is genuinely binary: e.g. diseased or not diseased. However, for conferences the accept/reject boundary is not a clear separation point, there is a continuum (or spectrum) of paper quality (as there also is for some diseases). And the decision boundary often falls in a region of very high density. To better quantify these ideas we can explore our duplication experiment in more detail, by introducing the paper scores, that's a task we will perform in a fresh notebook.}

\slides{* For parallel-universe NIPS we expect between 38% and 64% of the presented papers to be the same. 
* For random-parallel-universe NIPS we only expect 25% of the papers to be the same.}

\subsection{Discussion}

* Error types:
  * type I error as accepting a paper which should be rejected.
  * type II error rejecting a paper should be accepted.
* Controlling for error:
  * many reviewer discussions can be summarised as *subjective* opinions about whether controlling for type I or type II is more important.
  * with low accept rates, type I errors are *much* more common.
* Normally in such discussions we believe there is a clear underlying boundary.
* For conferences there is no clear separation points, there is a spectrum of paper quality.
* Should be explored alongside *paper scores*.

\thanks

\references
