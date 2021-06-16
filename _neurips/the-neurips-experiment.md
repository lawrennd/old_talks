---
title: A Retrospective on the 2014 NeurIPS Experiment
venue: Computer Lab Seminar Series
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: University of Cambridge
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
abstract: >
  In 2014, along with Corinna Cortes, I was Program Chair of the Neural Information Processing Systems conference. At the time, when wondering about innovations for the coference, Corinna and I decided it would be interesting to test the consistency of reviewing. With this in mind, we randomly selected 10% of submissions and had them reviewed by two independent committees. 
  
  In this talk I will review the construction of the experiment, explain how the NeurIPS review process worked and talk about what I felt the implications for reviewing were, vs what the community reaction was.
date: 2021-06-16
ipynb: True
categories:
- notes
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

\ifdef{SLIDES}
\define{DARKBACKGROUND}
\endif

\section{Introduction}

\notes{The NIPS experiment was an experiment to determine the consistency of the review process. After receiving papers we selected 10% that would be independently rereviewed. The idea was to determine how consistent the decisions between the two sets of independent papers would be. In 2014 NIPS received 1678 submissions and we selected 170 for the experiment. These papers are referred to below as 'duplicated papers'.}

\notes{To run the experiment we created two separate committees within the NIPS program committee. The idea was that the two separate committees would review each duplicated paper independently and results compared.}

\include{_neurips/includes/neurips-in-numbers.md}
\include{_neurips/includes/paper-scoring.md}
\include{_neurips/includes/neurips-experiment-speculation.md}
\include{_neurips/includes/neurips-experiment-results.md}
\include{_neurips/includes/neurips-experiment-reaction.md}
\include{_neurips/includes/neurips-experiment-random-committee.md}

<!--include{_neurips/includes/neurips-experiment.md}-->
\include{_neurips/includes/neurips-reviewer-calibration.md}
\include{_neurips/includes/neurips-simulation.md}
\include{_neurips/includes/where-do-the-rejected-papers-go.md}

\notes{\include{_neurips/includes/effect-of-late-reviewers.md}}

\newslide{Late Reviewers}

\slides{\figure{\includediagram{\diagramsDir/neurips/correlation-duplicate-reviews-bootstrap}{70%}}{}{correlation-duplicate-reviews-bootstrap}}

\include{_neurips/includes/impact-of-papers-seven-years-on.md}

\subsection{Conclusion}

\slides{* Inconsistent errors are better than consistent errors
* NeurIPS and Impractical Knives}

\notes{\include{_neurips/includes/neurips-experiment-conclusion.md}}

\notes{I would prefer a world were a conference is no longer viewed as a proxy for research quality. The true test of quality is time. In the current world, papers from conferences such as NeurIPS are being used to judge whether a researcher is worthy of a position at a leading company, or whether a researcher gets tenure. This is problematic and damaging for the community. Reviewing is an inconsistent process, but that is not a bad thing. It is far worse to have a reviewing system that is consistently wrong than one which is inconsistently wrong.}

\notes{My own view of a NeurIPS paper is inspired by the Millenium Galleries in Sheffield. There, amoung the exhibitions they sometimes have work done by apprentices in their 'qualification'. Sheffield is known for knives, and the work of the apprentices in making knives is sometimes very intricate indeed. But it does lead to some very impractical knives. NeurIPS seems to be good at judging technical skill, but not impact. And I suspect the same is true of many other meetings. So, a publication a NeurIPS does seem to indicate that the author has some of the skills required, but it does not necessarily imply that the paper will be impactful.}


\comment{Post from Balazs Kegl: <https://balazskegl.medium.com/embrace-the-random-2957d078bfb3>}


\comment{Conversation with Ani Nenkova via twitter}

\comment{Hi Ani, I think I can get that notebook running again if there's specific analysis you need. Drop me a line on ndl21@cam.ac.uk and we can probably sort something out.
Oct 27, 2020, 6:55 PM
Hi Neil, I will send an email shortly, with a little bit of background on my questions! Thanks for taking the time
Oct 27, 2020, 7:31 PM
Quote Tweet
Mark Neumann
@MarkNeumannnn
 · Aug 31
Replying to @ani_nenkova
I just checked - 9.8% and 9.4% of rejections from 2017/18 respectively were accepted at one of these top conferences:

ICML
NeurIPS
AAAI
JMLR
COLT
FATML
EMNLP
ACL
NAACL-HLT
CVPR
ECCV
https://twitter.com/markneumannnn/status/1300504708553949184?s=21
I will include this in the email but sending this as preview
Oct 27, 2020, 7:35 PM
AISTATS and UAI are two big missing meetings from that list ...
Oct 27, 2020, 8:03 PM
I don't know how easy it will be to do the matches ... but I also publish PMLR and I make all the title/author names available in yaml files for that.
PMLR covers ICML, AISTATS, more recently UAI, COLT, ACML and a bunch of others.}


\comment{Email Conversation with Ani Nenkova}

\comment{Yes, please do a retrospective! Even better if you are inclined to write it as a Science or PNAS paper, with focus on the questions you addressed and what the findings teach us about this question. All the modelling part can go in a supplementary material if you ask me 🙂

I do appreciate that you used the statistical model prediction to guide area chair attention. I did not realize this was happening before our exchange. In the popular blog posts there are some abstract models of the review process and I find these useless, but this may be a matter of taste.  

Thanks for your support for women and minorities. I don't think we can win that one at the "top" schools, because a refusal to make shortcuts by judgments of prestige would require reading and making your own judgements and who has time for that. 

I am still puzzling over why in your experiment 20% of papers had a chance of being accepted (in a comparable venue)  in rereview but in the empirical data from three different venues we see only 10%. Who knows what the explanation is, but I have one more idea for an explanation that I didn't think you'd be interested in hearing. Maybe some authors took the rejection to heart and didn't submit to a top venue, either gave up or went for a lower prestige, easier to accept venue. I can imagine who these authors would be, the ones that have the most to lose by doing so, from underrepresented groups.



On Wed, Oct 28, 2020 at 1:14 PM Neil David Lawrence <ndl21@cam.ac.uk> wrote:
Your digression is super important. And how we attack that (it’s not just female academics, but underrepresented groups, e.g. our African colleagues) is key to whatever solutions we look at.

There’s a particular problem for multidisciplinary research, which is the most useful research (often) but the hardest to get into narrow-minded ‘prestige’ conferences. When I speak to early career female CS researchers (e.g. at WiML mentoring sessions), I find they are typically more inclined towards interdisciplinary research. So that may be compounding the problem.

My main takeaway is “stop taking conferences so seriously”. I thought that beforehand and after. But I guess people are too attached to them.

In an ideal world, conferences would be about sharing and evolving ideas. But I guess that’s not the world we live in any more.

That blog post, which is a pretty shallow analysis, was widely shared because it has a catchy headline. And it’s the main thing that comes up when people search. Perhaps it’s time for a retrospective …

 

From: Ani Nenkova <nenkova@seas.upenn.edu>
Date: Wednesday, 28 October 2020 at 15:30
To: Neil David Lawrence <ndl21@cam.ac.uk>
Subject: Re: conference reviewing

Thanks for sharing your thoughts, Neil. This is very useful, I like your notes more than the blog post that I have seen shared most, by someone not directly involved in the experiment.

In a nutshell, what is the main takeaway of what you did? I do agree that what you shared is not inline with the conclusion that I have heard repeatedly, that the review process is random.

To me, what stands out is that it is unreasonable to consider venue only when talking about prestige. Half of the accepted papers could have been rejected, accept precision is 50%.

The reject precision is 83%, which is high. To me, in terms of practical conclusions this means that authors need to revise their paper before resubmitting. Maybe the work was good but they did not explain well. Hoping for a different outcome is not that reasonable, given the high chance of being rejected again but I have seen people repeatedly cite your experiment as a justification why they are simply resubmitting a manuscript that just got rejected.

About prestige, I agree with you in general. But people do make arguments around that and I can tell you from my personal experience as a woman that I'd and my female students would be torn apart by promotion and hiring committees if we didn't have these high prestige papers. For my students (mostly women), I also know that getting the first couple of papers in a conference considered prestigious completely transforms their attitude to work and gives them the self-confidence to pursue their own ideas. This is a digression but I couldn't resist.

 

On Tue, Oct 27, 2020 at 5:46 PM Neil David Lawrence <ndl21@cam.ac.uk> wrote:

HI Ani,

I think that year at NeurIPS we did quite a lot … the blog posts document a lot of it.

I guess these rankings of conferences mean very little to me. In ML we’re now swamped by a lot of new entrants to the field (when you realise that the recent NeurIPS had 7,000 submissions .. and the one Corinna and I did 6 years ago had 1600).

I would prefer to publish at AISTATS than ICLR … but that’s mainly because of subject matter. AISTATS (to me) has a lot more interesting papers.

Prestige is very subjective.

You can see our process in some of the other notebooks. For example, this one:

https://github.com/sods/conference/blob/master/Reviewer%20Calibration.ipynb

Details reviewer calibration. This was done across area chairs and run daily during discussion periods.

If you scan down you can see the “Monte Carlo Simulations for Probability of Acceptance”.


That information was updated daily as well, so that each area chair could see papers in the ‘grey area’. Grey area was defined as between 10% and 90% probability of acceptance.

I ran regular scripts to check these papers were being discussed. See the attention report here:

https://github.com/sods/conference/blob/master/Attention%20Report.ipynb

This triggered discussions for grey area papers (and papers with other conditions like too few reviews, or high variance scores).

By the time we got together for the Video Conferences to discuss papers, a lot of discussion had taken place between reviewers and area chairs.

So Area Chairs did have this probability of accept score in front of them when representing the paper. But there was a lot of movement in these scores as we converged on decision time as they ‘worked the discussions’.

By the way … a ‘dependable’ decision process is *not* necessarily a good thing. Indeed, I think it’s likely very bad.

Three reviewers are entitled to have a different opinion about a paper. Indeed, the calibration score shows that about 50% of the variance of the score is subjective (once reviewer ‘bias’ is removed, see the variances in output 20 in the notebook … the “noise variance” is subjectivity in the scores, the “K_f.variances” is the variance associated with the objective score … reviewer bias is small relatively speaking). Here subjective means something quite specific because it’s coming from the decomposition of the reviewer scores into a term that is consistent within a paper, a term that is consistent within a reviewer (that’s the reviewer bias) and a term that is specific to that paper/reviewer combination. The first is the ‘objective opinion’ and the last is the ‘subjective opinion’.

So you’re looking at scores which across the conference are around 50% subjective and 50% objective.

And indeed, often reviewer instructions ask for subjective opinion (e.g. what is the ‘novelty’ and ‘impact’ of the paper … these are totally subjective questions).

I guess we should have tested for the consistency of a process where the underlying scores are 50% subjective and 50% objective …

Makes sense to do that now.

Below I’m pasting code for the simulation, but the headline result is:

Percentage consistently accepted: 0.43499

That’s with a million papers.

So looks like we did a bit better than might be expected given the subjective nature of (the) reviewing. That can be put down to sample error.

You can remove this inconsistency if you remove subjectivity, but that can also be indicative of a biased reviewing community who’s not judging the paper on its merits. E.g. for a silly example, we could only accept papers whose abstracts start with vowels.

So in the end my conclusion was that the reviewing process is subjective, we ask for it to be subjective … and then we’re surprised when it doesn’t lead to consistent results.

By the way, we also *could* have removed subjectivity from our scores (like we removed reviewer bias). But this actually felt like the wrong thing to do … why?

Well some of that subjectivity is down to different experience … we made special efforts to ensure every paper had at least one highly experienced reviewer. The ‘subjective’ opinion here is now coming from their different experiences …

Sorry, that was long and rambling … but you get the idea. In my opinion the community missed the message of the experiment (almost) completely.

Neil}

\setupcode{import numpy as np}

\code{samples = 1000000
accept_rate = 0.2
score_1 = []
score_2 = []

for i in range(samples):
    objective = np.random.randn()
    score_1.append(objective + np.random.randn())
    score_2.append(objective + np.random.randn())

 
score_1 = np.asarray(score_1)
score_2 = np.asarray(score_2)

accept_1 = score_1.argsort()[:int(samples*accept_rate)]
accept_2 = score_2.argsort()[:int(samples*accept_rate)]

consistent_accept = len(set(accept_1).intersection(set(accept_2)))

print('Percentage consistently accepted: {prop}'.format(prop=consistent_accept/(samples*accept_rate)))}

\comment{From: Ani Nenkova <nenkova@seas.upenn.edu>
Date: Tuesday, 27 October 2020 at 20:47
To: Neil David Lawrence <ndl21@cam.ac.uk>
Subject: conference reviewing

Hi, Neil, nice to meet you!

I work in natural language processing and am interested in figuring out how to set up an efficient and fair system to evaluate scholarly work. I have recently started to despair that this is not possible in a large field but occasionally forget that, as I did this morning 🙂

In large conferences program chairs often resort to shortcuts, like sorting papers by score but I wonder how stable these scores are across different runs of the review process. So I'd be curious what is the 95% confidence interval for the difference between scores for the same paper over the entire sample you had and for the subset of papers for which there was a disagreement. For the papers for which there was a disagreement, what percentage were borderline in both runs of the review process, with similar middling scores, and what percentage had a big difference, so it is really the subjective evaluation of the reviewers that flipped.

At the most recent EMNLP the program chairs decided to accept the top 25% of papers to the main conference, and then accept the next 10% by score in a supplementary proceedings for papers that are published but do not get a presentation slot at the conference. To me that sort of sorting by score would be meaningful only if the scores are stable enough to be confident in the ranking. This background may give you a better idea about why I am fixating on the scores.

The analysis of ICLR data that I sent you shows that only 9% of rejected papers are accepted at another top tier venue. This is very similar to what I have observed unofficially for one edition of NAACL and historically for TACL. Only 5% of the rejected papers are accepted at the conference with a deadline right after the current conference decision. The others probably get rejected at least once more and I assume are considerably edited. 

You mentioned that you publish at other venues as well, but these would not be considered as prestigious, right? I roughly go by csrankings.org, whose creators explain they picked the three venues identified as the most prestigious by people working in that area. I am wondering what are the chances that a paper will be published at an equally prestigious venue. In Mark's and mine independent analysis of venues, about 30% of rejected papers will eventually be published somewhere, at a workshop, other reasonable conferences etc. Understandably the percentage is larger than when considering only venues that are perceived to be the most prestigious. Still, the fact that only 30% of papers are published with the same titles somewhere make the decision process look much more dependable than your study might suggest.

In your experiment the chance of a rejected paper to be accepted in a rerun of the review was ~18% but in the smaller venues without predefined acceptance rate it is 9%. I wonder if this is in any way related to the instructions given to area chairs. Did you give them a target acceptance rate or did you tell them to accept any paper worth accepting?

This email has gotten long enough, I'd better stop here!

Best,

Ani}

\section{Introduction}

Experimental setup

Model calibration

Results

Model of Results

Community Reaction

What happened to rejected papers?


\thanks

\references



