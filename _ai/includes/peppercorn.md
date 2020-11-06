\ifndef{peppercorn}
\define{peppercorn}

\editme

\subsection{Peppercorns}
\slides{
* A new name for system failures which aren't bugs.
* Difference between finding a fly in your soup vs a peppercorn in your soup. 
}

\newslide{Peppercorns}

\figure{\includeyoutube{1y2UKz47gew}{600}{450}}{A peppercorn is a system design failure which is not a bug, but a conformance to design specification that causes problems when the system is deployed in the real world with mischevious and adversarial actors.}{peppercorn-siri}

\notes{Asking Siri "What is a trillion to the power of a thousand minus one?" leads to a 30 minute response[^fixed] consisting of only 9s. I found this out because my nine year old grabbed my phone and did it. The only way to stop Siri was to force closure. This is an interesting example of a system feature that's *not* a bug, in fact it requires clever processing from Wolfram Alpha. But it's an unexpected result from the system performing correctly.

[^fixed]: Apple has fixed this issue so that Siri no longer does this.}

\notes{This challenge of facing a circumstance that was unenvisaged in design but has consequences in deployment becomes far larger when the environment is uncontrolled. Or in the extreme case, where actions of the intelligent system effect the wider environment and change it.}

\notes{These unforseen circumstances are likely to lead to need for much more efficient turn-around and update for our intelligent systems. Whether we are correcting for security flaws (which *are* bugs) or unenvisaged circumstantial challenges: an issue I'm referring to as *peppercorns*. Rapid deployment of system updates is required. For example, Apple have "fixed" the problem of Siri returning long numbers.}

\notes{The challenge is particularly acute because of the *scale* at which we can deploy AI solutions. This means when something does go wrong, it may be going wrong in billions of households simultaneously.}


\notes{You can also check this }\addblog{Decision Making and Diversity}{2017/11/15/decision-making}\notes{ and this }
\addblog{Natural vs Artifical Intelligence}{2018/02/06/natural-and-artificial-intelligence}\notes{.}

\endif
