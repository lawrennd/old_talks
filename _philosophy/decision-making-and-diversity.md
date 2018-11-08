---
title: "Decision Making and Diversity: The Folly of Value Alignment"
abstract: 
published: 2018-04-30
venue: CFI Lunchtime Seminar
reveal: 2018-04-30-decision-making-and-diversity.slides.html
blog: 2018-02-06-natural-and-artificial-intelligence.md
blog1: 2017-11-15-decision-making.md
blog2: 2015-12-04-what-kind-of-ai.md
layout: talk
bibliography: decision-making-and-diversidty.bib
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
published: 2018-04-30
transition: None
---

\include{../talk-macros.tex}

\newslide{}


\includejpg{../slides/diagrams/philosophy/justice-whats-the-right-thing-to-do}{50%}

\newslide{}

\includejpg{../slides/diagrams/ai/Trolley_1}{80%}

\newslide{Utility Theory and Utilitarianism}

* Utilitarianism maps to *utility theory*
* Assume that result of a decision can be evaluated mathematically.

\newslide{Utility Theory}

* An approach to balancing sensitivity vs specificity in a decision.
* Decision theory

\newslide{Basics}

* define a *utility function*

\newslide{The Push and the Trolley}

\includejpg{../slides/diagrams/ai/trolley2}{80%}


\newslide{Evolution and Utilitarianism}

* Bentham was not aware of Darwin's principle of natural selection
* Bentham believed that we should take an action if it maximised the happiness of the population (thereby minimising pain). 
* His utility function was the sum of the happiness of the population. 


\newslide{John Stuart Mill}

* Struggled with the idea that a night of debauchery was the same form of happiness.
* See also Epicurius

\newslide{Natural Selection}

* Species evolve through natural selection
* Bentham's idea was that we should maximize happiness. 
* In reality happiness is some form of *intermediate* reward.

\newslide{Mathematics of Change}

* Driven by Newton and [Leibniz](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz)'s work differential calculus. 
* Actually happiness is some (monotonic) function of the gradient of whatever personal utility function we have. 
* John Stuart Mill's variation on utilitarianism considered 'higher pleasures', such as the pleasure gained from literature and learning. (See also Eleni Vasilaki on Epicurus @Vasilaki:epicurius17)
* our happiness must be integrated to form our utility. 

\newslide{Prospect Theory}


* Daniel Kahneman's Nobel Memorial Prize in Economics was awarded for the idea of *prospect theory*. 
* Kahneman describes the theory and its background in his book, "Thinking Fast and Slow" [@Kahneman-fastslow11]. 
* Empirical theory about how people are responsive to change in circumstance, not absolute circumstance. 

\newslide{Subjective Utility}

* Bentham's ideas focussed around the idea of a global utility.
* Natural selection insists there must be *variation* in the population
* Without variation, there is no separation between effective and ineffective strategies.

\newslide{A Cognitive Bias towards Variance}

* Kahneman explores our tendency to produce overcomplicated explanations
* Prediction is
    $$ \text{model} + \text{data} \rightarrow \text{prediction}$$
* Models fail as overly simple or overly complex


\newslide{Bias vs Variance}

* 'bias variance dilemma' @Geman-biasvariance92
* Decompose errors as 
    1. due to oversimplification (the bias error) and 
	2. those due to insufficient data to underpin a complex model (variance error).

\newslide{In Machine Learning}

* Two approaches
   * Use simpler models (better consistency and generalization)
   * Use more complex models and average.



\newslide{Decision Making and Bias-Variance}

* In a population we should prefer variance-errors. 
    * Bias errors lead to consistent, decsion making.
	* Consistently wrong!
	
* Variance errors can also be averaged e.g. [bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating) and [boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning)) [@Breiman-bagging96] 



\newslide{Rational Behaviour}

* Sustain a variety of approaches to life.
* Complex explanations such as half-time football punditry.
* Also clinical experts [@Meehl-clinicalstatistical54]. Meehl suggested they 'try to be clever and think outside the box'. 

\newslide{One Correct Solution}

* Artificial Selection and Eugenics.
* OK for race horses, greyhounds, crops, sheep and cows 
* Not OK for the human race.

\newslide{One Correct Solution}

* Flawed understanding of science
* Animals in a species become too specialised then they may not be able to respond to changing circumstances. 
    * Think of cheetahs and eagles vs rats and pigeons.

\newslide{Similar Ideas Socially}

> I may not agree with many people's subjective approach to life, I may even believe it to be severely sub-optimal. But I should not presume to know better, even if prior experience shows that my own 'way of being' is effective. 
>
> Variation is vitally important for robustness. There may be future circumstances where my approaches fail utterly, and other ways of being are better.

\newslide{A Universal Utility}

* Quality of our individual subjective utilities measured by effectiveness.
* But it is surival of entire species that dominates long term.
* A universal utility by which we are judged is difficult to define.

\newslide{The Real Ethical Dilemma}

* Trolley Problem is an oversimplification.
* Driverless cars: 
    * introduce driverless cars and bring about a 90% reduction in deaths 
	* What if remaining deaths are all cyclists?
	
\newslide{Uncertainty: The Tyger that Burns Bright}

* Non-survival of the non-fit 
* The marvel of evolution is its responsiveness.
* Utility function evolves socially and in our environment.

(["survival of the fittest"](https://en.wikipedia.org/wiki/Survival_of_the_fittest) is due to [Herbert Spencer](https://en.wikipedia.org/wiki/Herbert_Spencer))

\newslide{Absolute Policies}

* There is only one absolute policy we should follow. 

> There will be single absolute policy that should be followed slavishly in all circumstances


\newslide{George Box}


> Since all models are wrong the scientist must be alert to what is importantly wrong. It is inappropriate to be concerned about mice when there are tigers abroad.
>
> George E. P. Box [@Box-science76]



\newslide{Tigers and Trolleys}

* A simple switch in the points, is deterministic/mechanistic

\includejpg{../slides/diagrams/ai/Trolley_1}{60%}

\newslide{Tigers and Trolleys}

* The second example is largely contrived, and riddled with uncertainty.

\includejpg{../slides/diagrams/ai/trolley2}{60%}


\newslide{Conclusion}

* Uncertainty of the correct utility implies  'correct' decision is difficult produce or verify. 
* Tendency to seek proxies such as *consistency* in decision making. 
* Consistent algorithms oversimplifies.
* Society would be more robust if diversity of solutions and opinions are sustained and respected. 

\newslide{Links}

* Articles in the Guardian are available from my [Guardian Profile Page](http://www.theguardian.com/profile/neil-lawrence)
* [My blog](http://inverseprobability.com/blog.html) has articles relating to this area.
* [This post on System Zero](http://inverseprobability.com/2015/12/04/what-kind-of-ai/) and [This post on the Mechanistic Fallacy](http://inverseprobability.com/2015/11/09/artificial-stupidity/) relate to the ideas in this talk.
* [This post on natural vs artificial systems](http://inverseprobability.com/2018/02/06/natural-and-artificial-intelligence)
* [This paper on decision making and diversity](http://inverseprobability.com/2017/11/15/decision-making)

\newslide{Thanks!}

* twitter: ```@lawrennd```
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)


\newslide{Bibliography}

