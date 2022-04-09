\ifndef{dataInattentionBias}
\define{dataInattentionBias}

\editme

\subsection{Data Selective Attention Bias}

\notes{We are going to see how inattention biases can play out in data analysis by going through a simple example. The analysis involves body mass index and activity information.}

\include{_data-science/includes/bmi-steps-analysis.md}

\subsection{A Hypothesis as a Liability}

\notes{This analysis is from an article titled "A Hypothesis as a Liability" [@Yanai-hypothesis20], they start their article with the following quite from Herman Hesse.}

>“ ‘When someone seeks,’ said Siddhartha, ‘then it easily happens that his eyes see only the thing that he seeks, and he is able to find nothing, to take in nothing. [...] Seeking means: having a goal. But finding means: being free, being open, having no goal.’ ”
>
> Hermann Hesse

\notes{Their idea is that having a hypothesis can constrain our thinking. However, in answer to their paper @Felin-data20 argue that some form of hypothesis is always necessary, suggesting that a hypothesis *can* be a liability}


\newslide{The Scientific Process}

\notes{My view is captured in the introductory chapter to an edited volume on computational systems biology that I worked on with Mark Girolami, Magnus Rattray and Guido Sanguinetti.}

\figure{\includepng{\diagramsDir/data-science/licsb-popper-quote}{80%}}{Quote from @Lawrence:licsbintro10 highlighting the importance of interaction between data and hypothesis.}{licsb-popper-quote}

\notes{Popper nicely captures the interaction between hypothesis and data by relating it to the chicken and the egg. The important thing is that these two co-evolve.}

\subsection{Number Theatre}

\notes{Unfortunately, we don't always have time to wait for this process to converge to an answer we can all rely on before a decision is required.}

\notes{Not only can we be misled by data before a decision is made, but sometimes we can be misled by data to justify the making of a decision. David Spiegelhalter refers to the phenomenon of "Number Theatre" in a conversation with Andrew Marr from May 2020 on the presentation of data.}

\figure{\includeyoutube{9388XmWIHXg}{600}{450}}{Professor Sir David Spiegelhalter on Andrew Marr on 10th May 2020 speaking about some of the challengers around data, data presentation, and decision making in a pandemic. David mentions number theatre at 9 minutes 10 seconds.}{david-andrew-marr}

<!--includebbcvideo{p08csg28}-->

\subsection{Data Theatre}

\notes{Data Theatre exploits data inattention bias to present a particular view on events that may misrepresents through selective presentation. Statisticians are one of the few groups that are trained with a sufficient degree of data skepticism. But it can also be combatted through ensuring there are domain experts present, and that they can speak freely.}

\slides{\figure{\includediagram{\diagramsDir/business/data-theatre000}{60%}}{The phenomenon of number theatre or *data theatre* was described by David Spiegelhalter and is nicely summarized by Martin Robbins in this sub-stack article <https://martinrobbins.substack.com/p/data-theatre-why-the-digital-dashboards>.}{data-theatre-000}}


\newslide{}

\figure{\includediagram{\diagramsDir/business/data-theatre001}{60%}}{The pheonomenon of number theatre or *data theatre* was described by David Spiegelhalter and is nicely sumamrized by Martin Robbins in this sub-stack article <https://martinrobbins.substack.com/p/data-theatre-why-the-digital-dashboards>.}{data-theatre-001}

\notes{The best book I have found for teaching the skeptical sense of data that underlies the statisticians craft is David Spiegelhalter's *Art of Statistics*.}

\include{_books/includes/the-art-of-statistics.md}


\endif
