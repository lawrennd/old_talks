\ifndef{mlSystemsDesignLong}
\define{mlSystemsDesignLong}
\editme

talk-macros.gpp}i/includes/ml-systems-design-short.md}

talk-macros.gpp}i/includes/pigeonholing.md}

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

talk-macros.gpp}i/includes/centrifugal-governor.md}

\newslide{Adversaries}
\slides{
* Stuxnet
* Mischevious-Adversarial
}

\notes{The centrifugal governor was a key component in the Boulton-Watt steam engine. It senses increases in speed in the engine and closed the steam valve to prevent the engine overspeeding and destroying itself. Until the invention of this device, it was a human job to do this.}

\notes{The formal study of governors and other feedback control devices was then began by [James Clerk Maxwell](https://en.wikipedia.org/wiki/James_Clerk_Maxwell), the Scottish physicist. This field became the foundation of our modern techniques of artificial intelligence through Norbert Wiener's book *Cybernetics* [@Wiener:cybernetics48]. Cybernetics is Greek for governor, a word that in itself simply means helmsman in English.}

\notes{The recent WannaCry virus that had a wide impact on our health services ecosystem was exploiting a security flaw in Windows systems that was first exploited by a virus called Stuxnet.}

\notes{Stuxnet was a virus designed to infect the Iranian nuclear program's Uranium enrichment centrifuges. A centrifuge is prevented from overspeed by a controller, just like the centrifugal governor. Only now it is implemented in control logic, in this case on a Siemens PLC controller. }

\notes{Stuxnet infected these controllers and took over the response signal in the centrifuge, fooling the system into thinking that no overspeed was occuring. As a result, the centrifuges destroyed themselves through spinning too fast. }

\notes{This is equivalent to detaching the governor from the steam engine. Such sabotage would be easily recognized by a steam engine operator. The challenge for the operators of the Iranian Uranium centrifuges was that the sabotage was occurring inside the electronics.}

\notes{That is the effect of an adversary on an intelligent system, but even without adveraries, the mischief of a 10 year old can confuse our AIs.}


talk-macros.gpp}i/includes/intelligent-system-paolo.md}
talk-macros.gpp}i/includes/peppercorn.md}


\newslide{Turnaround And Update}
\slides{
* There is a massive need for turn around and update
* A redeploy of the entire system.
    * This involves changing the way we design and deploy.
* Interface between security engineering and machine learning.
}


\ifdef{blogPosts}
\defeval{\blogPosts}{
\blogPosts
* [Mike Jordan's Medium Post](https://medium.com/@mijordan3/artificial-intelligence-the-revolution-hasnt-happened-yet-5e1d5812e1e7)
}
\else
\define{\blogPosts}{
* [Mike Jordan's Medium Post](https://medium.com/@mijordan3/artificial-intelligence-the-revolution-hasnt-happened-yet-5e1d5812e1e7)
}
\endif


\endif
