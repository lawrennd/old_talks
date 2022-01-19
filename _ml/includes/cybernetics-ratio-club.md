\ifndef{cyberneticsRatioClub}
\define{cyberneticsRatioClub}

\editme

\subsection{Cybernetics, Neural Networks and the Ratio Club}


\notes{This is certainly not the first wave of excitement in neural networks. This history of neural networks predates the history of the computer, and papers on neural networks predate papers on the digital computer.}

\newslide{Logic, McCulloch and Pitts}

\figure{\threeColumns{\includejpg{\diagramsDir/philosophy/Bertrand_Russell_1957}{100%}{}{left}}{\includejpg{\diagramsDir/ml/Lettvin_Pitts}{100%}{}{center}}{\includejpg{\diagramsDir/ml/warren_mcculloch}{100%}{}{right}}{30%}{30%}{30%}}{Bertrand Russell (1872-1970), Walter Pitts, *right* (1923-1969), Warren McCulloch (1898-1969)}{russell-pitts-mcculloch}

\notes{Specifically, one of the first papers on neural networks was written by two collaborators from logic and psychology in 1943. [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts) was a child prodigy who read Russell and Whitehead's *Principia Mathematica*. He felt he'd spotted some errors in the text and wrote to Russell in Cambridge, who replied inviting him for a visit. Pitts did not take up the offer because he was only 12 years old. But, three years later, when Russell took a sabbatical at the University of Chicago, Pitts left his home in Detroit and headed to Chicago to hear Russell speak. When Russell left Pitts stayed on studying logic. He never formally took a degree but just worked with whoever was available.}

\notes{[Warren McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch) was a psychologist who moved to the University of Chicago in 1941. Overlapping interests meant that he met Pitts, who was still living an itinerant lifestyle around the campus of the University. McCulloch invited Pitts to live with his family and they began collaborating on a simple model of the neuron and how neurons might interact. The dominant 'theory of knowledge' at the time was *logic* and their paper attempted to show how networks of neurons. Their paper, *A Logical Calculus of the Ideas Immanent in Nervous Activity* [@McCulloch:neuron43], was published in the middle of the Second World War. It modelled the neuron as a linear threshold and described how networks of such neurons could create logical functions. The inspiration in the paper is clear, they make use of Rudolf Carnap's Language II [@Carnap-logical37] to represent their theorem and cite the second edition of Russell and Whitehead [@Russell-principia25]. }

\subsection{Cybernetics}

\figure{\threeColumns{\includepng{\diagramsDir/physics/james-clerk-maxwell}{100%}{}{left}}{\includejpg{\diagramsDir/physics/j-w-gibbs}{100%}{}{center}}{\includejpg{\diagramsDir/physics/Norbert_wiener}{100%}{}{right}}{30%}{30%}{30%}}{James Clerk Maxwell (1831-1879), Josiah Willard Gibbs (1839-1903), Norbert Wiener (1894-1964)}{maxwell-gibbs-wiener}

\notes{After the war, this work, along with McCulloch and Pitts, was at the heart of a movement known as *Cybernetics*. A term coined by [Norbert Wiener](https://en.wikipedia.org/wiki/Norbert_Wiener) [@Wiener:cybernetics48] to reflect the wealth of work on sensing and computing. Wiener chose the term as an alternative rendering of the word *governor*. Governor comes to us from Latin but is a corruption of the Greek κυβερνήτης meaning helmsman. Wiener's choice of the term was a nod to the importance of James Clerk Maxwell's work on understanding surging in James Watt's steam engine governor [@Maxwell:governors1867]. It reflected the importance that Wiener placed on *feedback* in these systems. From this strand of work came the field of *control theory*.}

\notes{Many of the constituent ideas of Cybernetics came from  the war itself. Norbert Wiener was a Professor of Applied Mathematics at MIT. He was another child prodigy who visited Russell in Cambridge having completed his PhD at Harvard by the age of 19. But Wiener was less keen on logic than McCulloch and Pitts, he looked to stochastic processes and probability theory as the key to intelligent decision making. He rejected the need for a 'theory of knowledge' and preferred to think of a 'theory of ignorance' which was inspired by statistical mechanics, Maxwell was also an originator of the field, but Wiener wrote of Josiah Willard Gibbs as being his inspiration.}

\notes{This nascent community was mainly based on those who were involved in war work. Wiener worked on radar systems for tracking aircraft (leading to the Wiener filter [@Wiener:yellow49]). In the UK researchers such as Jack Good, Alan Turing, Donald MacKay, Ross Ashby formed the *Ratio Club*. A group of scientists interested in how the brain works and how it might be modelled. Many of these scientists also worked on radar systems or code breaking. }

\subsection{Analogue and Digital}

\figure{\includejpg{\diagramsDir/physics/dmaccrimmonmackay}{30%}}{Donald M. MacKay (1922-1987), an early member of the Cybernetics community and member of the Ratio Club.}{donald-maccrimmon-mackay}

\notes{Donald MacKay wrote of the influence that his own work on radar had on
his interest in the brain.

> ... during the war I had worked on the theory of automated and
> electronic computing and on the theory of information, all of which
> are highly relevant to such things as automatic pilots and automatic
> gun direction. I found myself grappling with problems in the design of
> artificial sense organs for naval gun-directors and with the
> principles on which electronic circuits could be used to simulate
> situations in the external world so as to provide goal-directed
> guidance for ships, aircraft, missiles and the like.
>
> Later in the 1940's, when I was doing my Ph.D. work, there was much
> talk of the brain as a computer and of the early digital computers
> that were just making the headlines as "electronic brains." As an
> analogue computer man I felt strongly convinced that the brain,
> whatever it was, was not a digital computer. I didn't think it was an
> analogue computer either in the conventional sense.
>
> But this naturally rubbed under my skin the question: well, if it is
> not either of these, what kind of system is it? Is there any way of
> following through the kind of analysis that is appropriate to their
> artificial automata so as to understand better the kind of system the
> human brain is? That was the beginning of my slippery slope into brain
> research.
>
> *Behind the Eye* pg 40. Edited version of the 1986 Gifford Lectures given by Donald M. MacKay and edited by Valerie MacKay
}

\notes{Importantly, MacKay distinguishes between the *analogue*
computer and the *digital* computer. As he mentions, his experience
was with analogue machines. An analogue machine is *literally* an
analogue. The radar systems that Wiener and MacKay both worked on were
made up of electronic components such as resistors, capacitors, and
inductors, that together represented a physical system, such as an
anti-aircraft gun and a plane. The design of the analogue computer
required the engineer to simulate the real world in analogue
electronics, using dualities that exist between e.g. mechanical
circuits (mass, spring, damper) and electronic circuits (inductor,
resistor, capacitor). The analogy between mass and a damper, between
spring and a resistor and between capacitor and a damper works because
the underlying mathematics is approximated with the same linear
system: a second order differential equation. This mathematical
analogy allowed the designer to map from the real world, through
mathematics, to a virtual world where the components reflected the
real world through analogy.}

\notes{This is a quite different from the approach that McCulloch and
Pitts were taking with their paper on the logical calculus of the
nervous system. They were attempting to map their model of the neuron
onto logic. Logical reasoning was the mainstay of the contemporary
understanding of intelligence. But the components they were
considering were neurons, they could only map onto the logical world
because their analogy for the neuron was so simple. An 'on' or 'off'
linear threshold unit. Where the synapses of the neuron were compared
to a threshold in the neuron. Firing occurs when the sum of input
neurons crosses a threshold in the receiving neuron. These networks can
then be built together in cascades.}

\notes{In the late 1940s and early 1950s, Cyberneticists were also
working on *digital computers*. The type of machines (such as
Colossus, built by Tommy Flowers, and known to Turing) and the
ENIAC. Indeed, by 1949 Cambridge had built its own machine, the EDSAC
in the Mathematical Laboratory, inspired by "draft of a report on the
EDVAC" by von Neumann.}

\notes{Digital computers are themselves (at their heart) a series of
analogue devices, but in the digital computer, the analogue is between
collections of transistors and logic gates. Logic gates allow the
computer to reconstruct *logical truth tables*, which Wittgenstein had
popularised in his *Tractatus Logico-Philosophicus*
[@Wittgenstein-logico21]. The mathematical operations we need can be
reconstructed through logic, so this 'analogue machine' which we call
a *digital computer* becomes capable of directly computing the
mathematics we're interested in, rather than going via the analogue
machine.}

\subsection{The Perceptron}

\figure{\threeColumns{\includejpg{\diagramsDir/ml/w-ross-ashby}{100%}{}{left}}{\includegif{\diagramsDir/physics/JohnvonNeumann-LosAlamos}{100%}{}{center}}{\includejpg{\diagramsDir/Frank_Rosenblatt}{100%}{}{right}}{30%}{30%}{30%}}{W. Ross
Ashby (1903-1972), John von Neumann (1903-1957), Frank Rosenblatt
(1928-1971). *Photograph of W. Ross Ashby is Copyright W. Ross
Ashby*.}{ashby-neumann-rosenblatt}

\notes{The early story of Cybernetics starts with the success of analogue control, and in the domain of neural networks, analogues machines were built. Inspired by F. Ross Ashby's [@Ashby-design52] ideas that suggested *random connections* and von Neumann [@Neumann-probabilistic56], who wrote about *probabilistic logics*, Frank Rosenblatt constructed the Perceptron [@Rosenblatt-perceptron58]. This was a deep neural network that recognised images from TV cameras.}

\notes{The perceptron created a great deal of interest, but it was rapidly eclipsed by the emerging *digital computer*. Perhaps as a marker as the increasing importance of the digital computer, the Apollo program (1961-1972) had a guidance computer that was a 16-bit digital machine for navigating to the moon. It implemented Kalman filters for guidance. In signal processing there's a shift from the 1950s to the 1960s of researchers moving from analogue designs to designs that are suitable for implementation of digital machines.}

\notes{That same shift was imposed on the Cybernetics community. Artificial Intelligence is often traced to the 'summer research project' proposed by John McCarthy at Dartmouth. But the proposal is not just notable for the introduction of the term, it is notable for the extent to which it marks a break with the Cybernetics community. Wiener's name isn't even mentioned in the proposal. And Cyberneticists either weren't invited to, or couldn't make, the event (with the notable exception of Warren McCulloch). Turing had died, and von Neumann was seriously ill with cancer. W. Ross Ashby was even in the US, but from his diaries there's no trace of him attending. Donald MacKay was on the initial proposal, but didn't make the event (perhaps because that summer his son, [Robert](https://warwick.ac.uk/fac/sci/maths/people/staff/robert_mackay/),  was born).}

\notes{One of the great ironies of modern artificial intelligence is that it is almost wholly reliant on deep neural network methodologies for the recent breakthroughs. But the dawn of the term artificial intelligence is associated with a period of around three decades when those methods (and the community that originated them) was actively marginalised.}

\notes{There were many reasons for this, including personal enmities between Wiener and McCulloch, the untimely death of Frank Rosenblatt in a sailing accident. But regardless of these personal tragedies and tales of academic politics, the principal reason that neural networks were eclipsed was the dominance of the digital computer. From 1956 to 1986 we saw the rise of the computer from a tool for science and big business to a personal machine, available to individual researchers.}


\endif
