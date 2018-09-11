\section{Natural and Artificial Intelligence: Embodiment Factors}

\newslide{"Embodiment Factors"}

<table>
 <tr>
  <td></td>
  <td align="center">\includeimg{../slides/diagrams/IBM_Blue_Gene_P_supercomputer.jpg}{40%}{}{center}</td>
  <td align="center">\includeimg{../slides/diagrams/ClaudeShannon_MFO3807.jpg}{25%}{}{center}</td>
 </tr>
 <tr>
  <td>compute</td>
  <td align="center">$$\approx 100 \text{ gigaflops}$$</td><td align="center">$$\approx 16 \text{ petaflops}$$</td>
 </tr>
 <tr>
  <td>communicate</td>
  <td align="center">$$1 \text{ gigbit/s}$$</td>
  <td align="center">$$100 \text{ bit/s}$$</td>
 </tr>
 <tr>
  <td>(compute/communicate)</td>
  <td align="center">$$10^{4}$$</td>
  <td align="center">$$10^{14}$$</td>
 </tr>
</table>

\slides{See ["Living Together: Mind and Machine Intelligence"](https://arxiv.org/abs/1705.07996)}

\notes{There is a fundamental limit placed on our intelligence based on our ability to communicate. Claude Shannon founded the field of information theory. The clever part of this theory is it allows us to separate our measurement of information from what the information pertains to[^knowledge-representation].

[^knowledge-representation]: the challenge of understanding what information pertains to is known as knowledge representation. 

Shannon measured information in bits. One bit of information is the amount of information I pass to you when I give you the result of a coin toss. Shannon was also interested in the amount of information in the English language. He estimated that on average a word in the English language contains 12 bits of information. 

Given typical speaking rates, that gives us an estimate of our ability to communicate of around 100 bits per second [@Reed-information98]. Computers on the other hand can communicate much more rapidly. Current wired network speeds are around a billion bits per second, ten million times faster. 

When it comes to compute though, our best estimates indicate our computers are slower. A typical modern computer can process make around 100 billion floating point operations per second, each floating point operation involves a 64 bit number. So the computer is processing around 6,400 billion bits per second. 

It's difficult to get similar estimates for humans, but by some estimates the amount of compute we would require to *simulate* a human brain is equivalent to that in the UK's fastest computer [@Ananthanarayanan-cat09], the MET office machine in Exeter, which in 2018 ranks as the 11th fastest computer in the world. That machine simulates the world's weather each morning, and then simulates the world's climate. It is a 16 petaflop machine, processing around 1,000 *trillion* bits per second. 

So when it comes to our ability to compute we are extraordinary, not compute in our conscious mind, but the underlying neuron firings that underpin both our consciousness, our sbuconsciousness as well as our motor control etc. By analogy I sometimes like to think of us as a Formula One engine. But in terms of our ability to deploy that computation in actual use, to share the results of what we have inferred, we are very limited. So when you imagine the F1 car that represents a psyche, think of an F1 car with bicycle wheels.}

\newslide{}

\includeimg{../slides/diagrams/640px-Marcel_Renault_1903.jpg}{70%}{}{center}

\notes{In contrast, our computers have less computational power, but they can communicate far more fluidly. They are more like a go-kart, less well powered, but with tires that allow them to deploy that power.}

\newslide{}

\includeimg{../slides/diagrams/Caleb_McDuff_WIX_Silence_Racing_livery.jpg}{70%}{}{center}

\notes{For humans, that means much of our computation should be dedicated to considering *what* we should compute. To do that efficiently we need to model the world around us. The most complex thing in the world around us is other humans. So it is no surprise that we model them. We second guess what their intentions are, and our communication is only necessary when they are departing from how we model them. Naturally, for this to work well, we need to understand those we work closely with. So it is no surprise that social communication, social bonding, forms so much of a part of our use of our limited bandwidth. 

There is a second effect here, our need to anthropomorphise objects around us. Our tendency to model our fellow humans extends to when we interact with other entities in our environment. To our pets as well as inanimate objects around us, such as computers or even our cars. This tendency to overinterpret could be a consequence of our limited ability to communicate. 

For more details see this paper ["Living Together: Mind and Machine Intelligence"](https://arxiv.org/abs/1705.07996), and this [TEDx talk](http://inverseprobability.com/talks/lawrence-tedx17/living-together.html).}
