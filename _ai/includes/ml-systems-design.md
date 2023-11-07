\ifndef{mlSystemsDesign}
\define{mlSystemsDesign}
\editme

\include{_ai/includes/ml-systems-design-short.md}

\newslide{Rapid Reimplementation}

\slides{
* Whole systems are being deployed.
* But they change their environment.
* The experience evolved adversarial behaviour.
}

\notes{However, the systems we are deploying into the real world actually effect their environment. They change users responses and experience evolved adversarial behaviour.}

\include{_ai/includes/centrifugal-governor.md}

\newslide{Turnaround And Update}
\slides{
* There is a massive need for turn around and update
* A redeploy of the entire system.
     * This involves changing the way we design and deploy.
* Early Example: Stuxnet.
}

\notes{If we contrast this with an adversarial attack in the digital era, we can consider the [Stuxnet virus](https://en.wikipedia.org/wiki/Stuxnet). Stuxnet was a sophisticated virus, presumed to have been developed as a cyberweapon by a combination of state security services. It used four 'zero day' exploits[^zeroday] to infect a specific centrifuge that was used for Uranium enrichment in the Iranian nuclear program. It was a sophisticated sabotage, the virus took over the PLC controllers in the centrifuge and fooled the controllers into overspeeding the centrifuge, destroying it. A PLC controller is a sophisticated electronic governor. Just as a steam engine would be destroyed if it was run without a Watt's governor, the centrifuges could be destroyed by taking over the software signals which should have prevented an overspeed. The main difference lies in the observability of the the sabotage. The cause of the exploding centrifuges was not immediately understood and up to 1000 centrifuges are thought to have been destroyed.

[^zeroday]: A 'zero day' exploit is one that is not know to the manufacturers of a system. Two of the Stuxnet exploits were in the PLC controllers, and two were in the Windows machines used to manage the centrifuges. Zero day exploits are typically only known to highly sophisticated attackers, such as state security services. 

A PLC controller is a relatively simple form of sense and act that implements technology that has been well understood for 70 years. A challenge for machine learning systems is that they present an additional level of complexity. An adversarial attach such as Stuxnet may be much harder to detect. Adversaries also need not be state funded security services. The more common adversary will be of the "mischievous kind". Children delight in finding flaws in "intelligent" computer services. And once these flaws are found, the delight in sharing them. Any vulnerability in deployed machine learning systems would be mercilessly exploited by the worldwide population of 11 year olds. 

The way security flaws in software are rectified is by patching the software. Complex machine learning systems will need close monitoring to determine when a breach has occured, whether is mischevious or nefarious. However, due to the erosion of the component based model for software engineering, patching these systems may prove harder than a traditional system. Rather like the challenges of laying a carpet, pushing down the carpet in one region may cause it to pop up in another region. Even with rigorous simulation testing, the challenge with an uncontrolled environment is the numbe of corner cases is so huge that foreseeing each one in the testing suite is impossible. 

Stuxnet exploited bugs in the software to enter the system and take control, but machine learning systems will face challenges not only from bugs, but unconsidered use cases where the designer did not perceive of how even correct performance could be abused.

One example is asking Siri the question "What is 10 trillion to the power of 1000 minus one? Originally, Siri read out the answer which consists of thirteen thousand nines in sequence. It would take Siri over an hour to read out this answer, likely draining the battery of the iPhone. The answer could only be interrupted by forcing Siri to close. The answer is correct, but foolish. Apple has now updated the iPhone to relate the answer in less than an hour.

}

\include{_ai/includes/peppercorn.md}
\endif
