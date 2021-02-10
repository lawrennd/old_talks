---
title: "Laplace's Gremlin: Uncertainty and Artificial Intelligence"
abstract: >
  With breakthroughs in understanding images, translating language,
  transcribing speech artificial intelligence promises to
  revolutionise the technological landscape. Machine learning
  algorithms are able to convert unstructured data into actionable
  knowledge. With the increasing impact of these technologies,
  society’s interest is also growing.

  The word *intelligence* conjures notions of human-like
  capabilities. But are we really on the cusp of creating machines
  that match us? We associate intelligence with knowledge, but in this
  talk I will argue that the true marvel of our intelligence is the
  way it deals with ignorance.

  Despite the large strides forward we have made, I will argue that we
  have a long way to go to deliver on the promise of artificial
  intelligence. And it is a journey that our societies need to take
  together, not just as computer scientists, but together by
  rediscovering the interdisciplinary spirit that Celsius, Linnaeus
  and their contemporaries did so much to demonstrate.
reveal: True
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2021-02-11
ipynb: True
venue: Celsius Lecture, Uppsala University, Sweden
transition: None
---



\include{talk-macros.gpp}

\notes{GREAT AI FALLACY

UNPRECEDENTED COMBINATION OF SCIENCE, SOCIAL SCIENCE, ETC REQUIRED TO DELIVER}

\section{SUPERINTELLIGENCE}

\newslide{}

>Given for one instant an intelligence which could comprehend all the forces by which nature is animated and the respective situation of the beings who compose it---an intelligence sufficiently vast to submit these data to analysis---it would embrace in the same formulate the movements of the greatest bodies of the universe and those of the lightest atom; for it, nothing would be uncertain and the future, as the past, would be present in its eyes.
>
> *Philosophical Essay on Probabilities* @Laplace-essai14 pg 3

\speakernotes{This notion is known as *Laplace's demon* or *Laplace's superman*.}

<!--include{_physics/includes/laplaces-determinism.md}-->


\aligncenter{
$$
\text{data} + \text{model} \stackrel{\text{compute}}{\rightarrow} \text{prediction}$$}


\include{_simulation/includes/life-rules.md}


\include{_simulation/includes/life-glider-loafer-conway.md}



\speakernotes{The phenomenon of emergent behaviour also applies to real world simulations like climate and weather. E.g. Niall Robinson defining a hurricane to search for hurricane's im climate simulations.}

<!--LAPLACE'S GREMLIN-->

\newslide{Laplace's Gremlin}

> The curve described by a simple molecule of air or vapor is regulated in a manner just as certain as the planetary orbits; the only difference between them is that which comes from our ignorance.
>
> Probability is relative, in part to this ignorance, in part to our knowledge.
>
> *Philosophical Essay on Probabilities* @Laplace-essai14 pg 5


INTRODUCE ENTROPY TO MEASURE IGNORANCE

<!--THEORY of IGNORANCE-->

\newslide{A Theory of Ignorance}

\figure{\threeColumns{\aligncenter{\includejpg{\diagramsDir/philosophy/Bertrand_Russell_1957}{100%}}\slides{\aligncenter{*Betrand Russell*}}}{\aligncenter{\includejpg{\diagramsDir/physics/Albert_Einstein_photo_1921}{50%}}\slides{\aligncenter{*Albert Einstein*}}}{\aligncenter{\includejpg{\diagramsDir/physics/Norbert_wiener}{100%}}\slides{\aligncenter{*Norbert Wiener*}}}{30%}{30%}{30%}}{Bertrand Russell (1872-1970), Albert Einstein (1879-1955), Norbert Wiener, (1894-1964)}{russell-wiener-russell}

\speakernotes{Wiener came to Cambridge in 1913. Russell showed him Einstein's 1905 paper on Brownian motion (@Einstein-brownian05)}

\newslide{}

\figure{\includegif{\diagramsDir/physics/brownian-motion}{40%}}{Brownian motion of a large particle in a group of smaller particles. The movement is known as a *Wiener process* after Norbert Wiener.}{brownian-motion}

<!--EINSTEIN-->

\newslide{}


\section{UNCERTAINTY}

\newslide{}

\include{_physics/includes/entropy-billiards.md}

\newslide{}

\figure{\threeColumns{\includepng{\diagramsDir/physics/james-clerk-maxwell}{100%}{}{left}}{\includejpg{\diagramsDir/physics/boltzmann2}{100%}{}{center}}{\includejpg{\diagramsDir/physics/j-w-gibbs}{100%}{}{right}}{30%}{30%}{30%}}{James Clerk Maxwell (1831-1879), Ludwig Boltzmann (1844-1906) Josiah Willard Gibbs (1839-1903)}{maxwell-boltzmann-gibbs}

<!--ENTROPY BILLIARDS-->

<!--include{_physics/includes/maxwells-demon.md}-->

\newslide{}

> But if we conceive a being whose faculties are so sharpened that he can follow every molecule in its course, such a being, whose attributes are still as essentially finite as our own, would be able to do what is at present impossible to us. For we have seen that the molecules in a vessel full of air at uniform temperature are moving with velocities by no means uniform, though the mean velocity of any great number of them, arbitrarily selected, is almost exactly uniform. Now let us suppose that such a vessel is divided into two portions, A and B, by a division in which there is a small hole, and that a being, who can see the individual molecules, opens and closes this hole, so as to allow only the swifter molecules to pass from A to B, and the only the slower ones to pass from B to A. He will thus, without expenditure of work, raise the temperature of B and lower that of A, in contradiction to the second law of thermodynamics.
>
> *Theory of Heat* [@Maxwell-theory71] page 308


\newslide{}

\figure{
<div>
<div style="width:68%;float:left">
  <canvas id="maxwell-canvas" width="700" height="500" style="border:1px solid black;display:inline;text-align:left"></canvas>
</div>
<div style="width:28%;float:right;margin:auto">
  <div style="float:right;width:100%;margin:auto">Entropy: <output id="maxwell-entropy"></output></div>
  <div id="maxwell-histogram-canvas" style="width:300px;height:250px;display:inline-block;text-align:right;margin:auto">
  </div>
</div>
</div>
<div>
<button id="maxwell-newball" style="text-align:right">New Ball</button>
<button id="maxwell-pause" style="text-align:right">Pause</button>
<button id="maxwell-skip" style="text-align:right">Skip 1000s</button>
<button id="maxwell-histogram" style="text-align:right">Histogram</button>
</div>

\include{_scripts/includes/maxwell-js.md}
}{Maxwell's Demon. The demon decides balls are either cold (blue) or hot (red) according to their velocity. Balls are allowed to pass the green membrane from right to left only if they are cold, and from left to right, only if they are hot.}{maxwells-demon}


\newslide{}

\figure{\includejpg{\diagramsDir/ClaudeShannon_MFO3807}{40%}}{Claude Shannon (1916-2001)}{claude-shannon}


\section{MEASUREMENT}

\newslide{Measurement and Intelligence}

> For instance, the temperature at which ice melts is found to be always the same under ordinary circumstances, though, as we shall see, it is slightly altered by change of pressure. The temperature of steam which issues from boiling water is also constant when the pressure is constant.
>
> These two pheomena therefore--the melting of ice and the boiling of water--indicate in a visible manner two temperatures which we may use as points of reference, the position of which depends on the properties of water and not on the conditions of our senses.
>
> *Theory of Heat* @Maxwell-theory71 page 3



\comment{\figure{\includegooglebook{0p8AAAAAMAAJ}{PA3}}{Quote from Maxwell's theory of heat on the melting and boiling point of water.}{maxwell-melting-boiling}}

\newslide{Locked In}

\figure{\include{_ai/includes/embodiment-factors-computer-human-table.html}}{Embodiment factors are the ratio between our ability to compute and our ability to communicate. Relative to the machine we are also locked in. In the table we represent embodiment as the length of time it would take to communicate one second's worth of computation. For computers it is a matter of minutes, but for a human, it is a matter of thousands of millions of years.}{embodiment-factors-table}


\include{_ai/includes/conversation-tedx.md}

\notes{Stories, between humans.}

\speakernotes{I have a great dislike for Russell; I cannot explain it completely, but I feel a detestation for the man. As far as any sympathy with me, or with anyone else, I believe, he is an iceberg. His mind impresses one as a keen, cold, narrow logical machine, that cuts the universe into neat little packets, that measure, as it were, just three inches each way. His type of mathematical analysis he applies as a sort of Procrustean bed to the facts, and those that contain more than his system provides for, he lops short, and those that contain less, he draws out.

Norbert Wiener in a letter to his family, 1913}


\include{_ai/includes/heider-simmel.md}

\include{_ai/includes/conversation-computer.md}


\newslide{}




\section{ARTIFICIAL}

\subsection{Artificial Intelligence}

\notes{One of the struggles of artificial intelligence is that the term means different things to different people. Our intelligence is precious to us, and the notion that it can be easily recreated is disturbing to us. This leads to some dystopian notions of artificial intelligence, such as the singularity.}

\notes{Depending on whether this powerful technology is viewed as beneficent or maleficent, it can be viewed either as a helpful assistant, in the manner of Jeeves, or a tyrannical dictator.}

\include{_ai/includes/ai-as-manservant.md}

\notes{The history of automation and technology is a history of us adapting to technological change. The invention of the railways, and the need for consistent national times to timetable our movements. The development of the factory system in the mills of Derbyshire required workers to operate and maintain the machines that replaced them.}


\notes{Listening to modern to conversations about artificial intelligence, I think the use of the term *intelligence* has given rise to an idea that this technology will be the But amoung these different assessments of artificial intelligence is buried an idea, one that }


\notes{Introduce Linnaeus and the hydra.}

\include{_philosophy/includes/the-hamburg-hydra.md}

\speakernotes{Our natural environment provides a Gibbsian hydra for us to do battle with. Statistical ensemble as hydra.}

\newslide{}

\figure{\includepng{\diagramsDir/ai/lenox-globe}{50%}}{[The Lenox globe](http://www.myoldmaps.com/renaissance-maps-1490-1800/314-the-lenox-globe/314-lenox.pdf), which dates from early 16th century, one of the earliest known globes.}{lenox-globe}

\slidesmall{\credit{New York Public Library Rare Books Collection}{https://digitalcollections.nypl.org/collections/hunt-lenox-globe#/?tab=about}}



\newslide{}

\figure{\includepng{\diagramsDir/ai/lenox-globe-by-b-f-da-costa}{100%}{negate}}{Drawing of the Lenox Globe by the historian for the Magazine of American History in September 1879.}{lenox-globe-by-b-f-da-costa}

\newslide{}

\figure{\includepng{\diagramsDir/ai/lenox-globe-hic-sunt-dracones}{60%}}{Detail from the Lenox globe located in the region of China, "hic sunt dracones"}{lenox-globe-hic-sunt-dracones}


\section{*ARTIFICIAL* INTELLIGENCE}

\include{_ml/includes/deep-face.md}
\include{_ml/includes/deep-learning-as-pinball.md}

\newslide{}

\includeyoutube{WXuK6gekU1Y}{600}{450}

\newslide{}

\speakernotes{Sedolian void: Despite the many millions of matches that AlphaGo had played, Lee Sedol
managed to find a board position that was distinct from anything AlphaGo
had seen before. Within the high dimensional pinball machine that made
up AlphaGo's decision making systems, Lee Sedol found a niche, an
Achillean chink in AlphaGo's armour. He found a path through the neural
network where no data had every been before. He found a location in
feature space where there be dragons.}

\figure{\columns{\includepng{\diagramsDir/ai/lee-se-dol-alpha-go-game-4-move-78}{60%}}{\includejpg{\diagramsDir/ai/lee-se-dol}{60%}}{49%}{49%}}{Move 78 of [Game 4](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol#Game_4) was critical in allowing Lee Se-dol to win the match. Described by [Gu Li](https://en.wikipedia.org/wiki/Gu_Li_(Go_player)) as a 'divine move'.}{lee-se-dol-move-78}

\speakernotes{Sedolian void: Despite the many millions of matches that AlphaGo had played, Lee Se-dol
managed to find a board position that was distinct from anything AlphaGo
had seen before. Within the high dimensional pinball machine that made
up AlphaGo's decision making systems, Lee Sedol found a niche, an
Achillean chink in AlphaGo's armour. He found a path through the neural
network where no data had every been before. He found a location in
feature space where there be dragons.}


<!--include{_physics/includes/kappenball.md}-->

\newslide{}

\figure{\includeyoutube{iWGhXof45zI}{600}{450}}{A vehicle operated by Uber ATG was involved in a fatal crash when it killed pedestrian Elaine Herzberg, 49.}{uber-atg-elaine}


\newslide{Academy of Sweden}

* The academy was founded on 2 June 1739 by naturalist Carl Linnaeus, mercantilist Jonas Alströmer, mechanical engineer Mårten Triewald, civil servants Sten Carl Bielke and Carl Wilhelm Cederhielm, and statesman/author Anders Johan von Höpken.

\newslide{}

\figure{\includediagram{\diagramsDir/simulation/data-driven-and-mechanistic-models}{80%}}{Data driven and mechanistic models have separated since the origin of the field. Accelerate science is about bringing these two modalities back together.}{data-driven-and-mechanistic-models}

https://uu.se/en/research/ai4research/

\newslide{Four Pillar Programme}


\columns{\aligncenter{\circleText{policy}{45%}}}{\aligncenter{\circleText{<tspan x="100" y="90">data</tspan><tspan x="100" y="130">governance</tspan>}{45%}}}{50%}{50%}
\columns{\aligncenter{\circleText{<tspan x="100" y="90">accelerate</tspan><tspan x="100" y="130">science</tspan>}{45%}}}{\aligncenter{\circleText{AutoAI}{45%}}}{50%}{50%}

\newslide{}

* Addressing Technical Debt (with Alan Turing Institute and ELLIS/ELISE Network)
* Accelerate Programme (funded by Schmidt Futures)
* Data Trusts Initiative (http://datatrusts.uk, funded by McGovern)
* Active Policy Engagement

One thing is I can live with doubt, and uncertainty and not knowing. I think it's much more interesting to live with not knowing that to have an answer that might be wrong. 

\thanks

\references

\comment{\notes{Uber ATG Accident}

\notes{HOw simple phenomena become complex}
\notes{Connect the use of ML for physics/biology with the previous use of physics/biology for talking about ML.}

\notes{Challenges for science: Causal, representation, symmetries: understanding complexity}
\notes{Next move towards Turing and Accelerate agenda.}



\notes{Yes, something like that is a good idea. I'm going to start a small document.

22nd sounds sensible.

I think bringing together the Accelerate, Turing and McGovern work could be interesting. Putting together under a theme … maybe that is supply chain of ideas. But need to relate that to passage of information and perhaps the role for ML in society??

From: Jessica Montgomery <jkm40@cam.ac.uk>
Date: Monday, 19 October 2020 at 16:17
To: Neil David Lawrence <ndl21@cam.ac.uk>
Subject: Re: Official invitation letter to the Celsius-Linnaeus lectures, February 11 2021

How about I send out an invite for the afternoon of 22 January? (Give you a week or so of adjusting to term starting, but 3 weeks to make changes before the event?)
 
Also happy to kick around ideas before that, if useful. Feels like you could tie together intellectual debt and supply chain of ideas (what happens when you speed up the pace of coconut production?) and the characteristics you need for AI systems to work well with people.
 
 
 
From: Neil David Lawrence <ndl21@cam.ac.uk>
Date: Monday, 19 October 2020 at 16:06
To: Jessica Montgomery <jkm40@cam.ac.uk>
Subject: Re: Official invitation letter to the Celsius-Linnaeus lectures, February 11 2021
 
Yes, good idea. 
 
Let's get a target date for the test run in (I'm still not 100% sure what to talk about!)
 
From: Jessica Montgomery <jkm40@cam.ac.uk>
Date: Monday, 19 October 2020 at 15:14
To: Neil David Lawrence <ndl21@cam.ac.uk>
Subject: Re: Official invitation letter to the Celsius-Linnaeus lectures, February 11 2021
 
Oooo! I was thinking about this the other day – we could do a test run on this with the group. Sort of a dress rehearsal, if you want to try out different lines or ideas? But also a way of contributing to the process of introducing ML@CL and Accelerate to each other.
 
 
 
From: Neil David Lawrence <ndl21@cam.ac.uk>
Date: Monday, 19 October 2020 at 15:11
To: Jessica Montgomery <jkm40@cam.ac.uk>
Subject: FW: Official invitation letter to the Celsius-Linnaeus lectures, February 11 2021
 a
For info (this is for the Celsius talk in February)
 
From: Thomas Schön <thomas.schon@it.uu.se>
Date: Monday, 19 October 2020 at 13:22
To: Neil David Lawrence <ndl21@cam.ac.uk>
Subject: Re: Official invitation letter to the Celsius-Linnaeus lectures, February 11 2021
 
Hi Neil, 
 
We have a new initiative here at the university AI4Research where the focus is on developing AI/ML and in particular the use of AI/ML at a tool to develop other disciplines (medicine, physics, chemistry, etc.). Some background on the project is available here https://uu.se/en/research/ai4research/  and when I was asked to write about the ideas it resulted in this
https://www.uu.se/en/news-media/news/article/?id=14730&typ=artikel&lang=en
 
If you like these ideas and have a story that somehow aligns with this that would be great. However, I definitely do not want to force you into talking about this topic, I only mentioning it since you asked for some concrete ideas.
 
In any case, it is important that your talk is broadly accessible to a wide audience (Technology and Natural Science) at the same time as it remains scientific, which is of course the challenge with talks of this kind. 
 
Hope this can be of some help?
 
Best,
Thomas
 
 
On 15 Oct 2020, at 16:25, Neil David Lawrence <ndl21@cam.ac.uk> wrote:
 
It would be great to have a sense of what you'd prefer me to talk about. I can imagine a few different things, but if I have a good steer from yourself, I'd be happy to use that!
 
 
From: Thomas Sch0n <thomas.schon@it.uu.se>
Date: Thursday, 15 October 2020 at 15:12
To: Neil David Lawrence <ndl21@cam.ac.uk>
Subject: Re: Official invitation letter to the Celsius-Linnaeus lectures, February 11 2021
 
Hi Neil,
 
Just let me know if you want to discuss title, abstract or anything else related to your talk at this stage.
 
Cheers,
Thomas
 
On 15 Oct 2020, at 14:59, Neil David Lawrence <ndl21@cam.ac.uk> wrote:
 
Hi Karin,
 
I have a few photos and bios of various lengths available here:
 
http://inverseprobability.com/biog.html
 
Neil}
}

