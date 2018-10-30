\section{Machine Learning System Design}

\newslide{Fragility of AI Systems}
\slides{
> * They are componentwise built from ML capabilities.
  * Each capability is independently constructed and verified.
      * Pedestrian detection
      * Road line detection
  * Componentwise deconstruciton is Important for verification purposes.
}

\newslide{Pigeonholing}
\slides{
\includeimg{../slides/diagrams/TooManyPigeons.jpg}{60%}{}{center}
}

\notes{The way we are deploying artificial intelligence systems in practice is to build up systems of machine learning components. To build a machine learning system, we decompose the task into parts, each of which we can emulate with ML methods. These parts are typically independently constructed and verified. For example, in a driverless car we can decompose the tasks into components such as "pedestrian detection" and "road line detection". Each of these components can be constructed with, for example, an independent classifier. We can then superimpose a logic on top. For example, "Follow the road line unless you detect a pedestrian in the road". 

This allows for verification of car performance, as long as we can verify the individual components. However, it also implies that the AI systems we deploy are *fragile*.

Our intelligent systems are composed by "pigeonholing" each indvidual task, then substituting with a machine learning model.}

\subsection{Rapid Reimplementation}

\slides{
* Whole systems are being deployed.
* But they change their environment.
* The experience evolved adversarial behaviour.
}

\notes{This is also the classical approach to automation, but in traditional automation we also ensure the *environment* in which the system operates becomes controlled. For example, trains run on railway lines, fast cars run on motorways, goods are manufactured in a controlled factory environment. 

The difference with modern automated decision making systems is our intention is to deploy them in the *uncontrolled* environment that makes up our own world.}

\notes{This exposes us to either unforseen circumstances or adversarial action. And yet it is unclear our our intelligent systems are capable of adapting to this.

We become exposed to mischief and adversaries. Adversaries intentially may wish to take over the artificial intelligence system, and mischief is the constant practice of many in our society. Simply watching a 10 year old interact with a voice agent such as Alexa or Siri shows that they are delighted when the can make the the "intelligent" agent seem foolish. }

\newslide{Machine Learning Systems Design}

\include{_ai/includes/centrifugal_governor.md}

\newslide{Adversaries}
\slides{
* Stuxnet
* Mischevious-Adversarial
}

\notes{One of the first automated decision making systems was Watt's governor, as held by "Science" on Holborns viaduct. Watt's governor was a key component in his steam engine. It senses increases in speed in the engine and closed the steam valve to prevent the engine overspeeding and destroying itself. Until the invention of this device, it was a human job to do this. 

The formal study of governors and other feedback control devices was then began by [James Clerk Maxwell](https://en.wikipedia.org/wiki/James_Clerk_Maxwell), the Scottish physicist. This field became the foundation of our modern techniques of artificial intelligence through Norbert Wiener's book *Cybernetics* [@Wiener:cybernetics48]. Cybernetics is Greek for governor, a word that in itself simply means helmsman in English. 

The recent WannaCry virus that had a wide impact on our health services ecosystem was exploiting a security flaw in Windows systems that was first exploited by a virus called Stuxnet.

Stuxnet was a virus designed to infect the Iranian nuclear program's Uranium enrichment centrifuges. A centrifuge is prevented from overspeed by a controller, just like Watt's governor. Only now it is implemented in control logic, in this case on a Siemens PLC controller. 

Stuxnet infected these controllers and took over the response signal in the centrifuge, fooling the system into thinking that no overspeed was occuring. As a result, the centrifuges destroyed themselves through spinning too fast. 

This is equivalent to detaching Watt's governor from the steam engine. Such sabotage would be easily recognized by a steam engine operator. The challenge for the operators of the Iranian Uranium centrifuges was that the sabotage was occurring inside the electronics.

That is the effect of an adversary on an intelligent system, but even without adveraries, the mischief of a 10 year old can confuse our AIs.

\includeyoutube{1y2UKz47gew}

Asking Siri "What is a trillion to the power of a thousand minus one?" leads to a 30 minute response consisting of only 9s. I found this out because my nine year old grabbed my phone and did it. The only way to stop Siri was to force closure. This is an interesting example of a system feature that's *not* a bug, in fact it requires clever processing from Wolfram Alpha. But it's an unexpected result from the system performing correctly. 

This challenge of facing a circumstance that was unenvisaged in design but has consequences in deployment becomes far larger when the environment is uncontrolled. Or in the extreme case, where actions of the intelligent system effect the wider environment and change it.

These unforseen circumstances are likely to lead to need for much more efficient turn-around and update for our intelligent systems. Whether we are correcting for security flaws (which *are* bugs) or unenvisaged circumstantial challenges: an issue I'm referring to as *peppercorns*. Rapid deployment of system updates is required. For example, Apple have "fixed" the problem of Siri returning long numbers.

The challenge is particularly acute because of the *scale* at which we can deploy AI solutions. This means when something does go wrong, it may be going wrong in billions of households simultaneously.

See also [this blog on the differences between natural and artificial intelligence](http://inverseprobability.com/2018/02/06/natural-and-artificial-intelligence) and this paper [on the need for diversity in decision making](http://inverseprobability.com/2017/11/15/decision-making).}

\newslide{Turnaround And Update}
\slides{
* There is a massive need for turn around and update
* A redeploy of the entire system.
    * This involves changing the way we design and deploy.
* Interface between security engineering and machine learning.
}

\newslide{Peppercorns}
\slides{
* A new name for system failures which aren't bugs.
* Difference between finding a fly in your soup vs a peppercorn in your soup. 
}

