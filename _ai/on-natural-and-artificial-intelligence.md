---
layout: slides
title: Natural and Artificial Intelligence
author: Neil D. Lawrence
institute: Amazon Research Cambridge and University of Sheffield
---
<!--notes:
- a plastic plant. is poor. It is poorly define
- it may with us for the did not join us It’s intelligence is based The worth of an idea  A negotiated compromise betwagreed upon , because it is predicated on a shared condition. The constraints on . A shared limitations.  is this condition. This locked in intelligence, because however we create an artificial intelligence it will 
- The challenge for an artificial intelligence is to emulat
-, an ingrained world view.or is predisposed to certain
- to seek out teleological explanations. 
- Each of To have a shared understanding on intent, we need a shared understanding of each other, of how we’ll likely react to different circumstances. We do this through empathy, through our artificial systems are able to communicate any of their thoughts far While communication does not have to be part of an individuals intelligence, if we consider the populations intelligence, we see that the architecture for sharing information wilI if we assume that sharing of information between individual computers or humans is a key 
- The average word in English contains 12 
- The challenges of this new form of systems design have already been explored in systems biology, a field dedicated to the reverse engineering of biological systems. As many researchers have found, classical approaches to reverse engineering, which typically involve subjecting the system to a perturbation. In other words actively changing the system, to obtain a deeper understanding of behaviour normally fail because a natural system will often compensate. Survival dictates that there should be back up systems that kick in. 
- Robust approaches to systems design for the “don’t fail” predicate are beyond the scope of current engineering practice. They require uncertainty, best default behaviours, worst case analyses. They require you to consider how your artificial intelligence should respond to a mischievous 10 year old. 
-  (in the simplest case, hitting it with a hammer
- Firstly, imagine all the different pin configurations there could be in our hyperspace pinball machine. There are many pin configurations that may work well, but in such a complex machine, even if we have a lot of data to test it with, there may be areas of the machine we don’t explore until we test it in the real world, unforeseen circumstances. How do we guarantee that the machine doesn’t mess up?
- Or what if we get the objective function wrong? How do we distil our desired behaviour into a simple mathematical function. 
- *Pigeonholed activity*
- *Natural vs artificial systems*
- *natural vs human intelligence*
- The prediction function is the object that is used to make new pr
- that we are a long way off. Or at least, there are technological breakthroughs that need to happen 
So what will be the last bastion 
- In the timeliSuper human performance on specific tasks are hailed as breaDebates around artificial intelligence are confused because the fail to properly define tBroadly My own position is Human intelligence is quite diffrArtificial intelligence is a loaded term, one that is challenging because it means different things to different people. Historically, artificial intelligence practitioners focussed on planning and logic. Recreating the reasoning abilities of humans in our artificial devices, but the new wave of breakthroughs come from something else. From artificial neural network models. 
- However, just as the origins of Although the origins of - One challenge is that most practitioners of artificial intelligence do not give 
- Or at least in emulating a set of actions that we regard as intelligent. Whether it’s 
-->

\include{talk-macros.tex}

###

<center>Are we close to creating intelligence?</center>

### What is Intelligence?

* Poorly defined.

    * My definition: use of information to achieve goals more efficiently.
	
	* Efficiency is defined through use of less resource.

* Automated decision making: we are continuing to progress well.

### The Silicon Factor

* BBC 1, London, 14th September 1980

* [Series of three programmes](http://genome.ch.bbc.co.uk/8bb0b5a05c38403280483e2f96aff1b9) investigating the so-called microelectronics revolution.

* The promise (and perils) of silicon was broadly similar to that for AI today.

### Public Definition

* Doing things that humans do.

    * There is a narcissistic element to our understanding of *artificial intelligence*

* It's a shifting definition.

    * Intelligence is the stuff I can do computers can't.
		 
### Cybernetics and the Ratio Club

* Cybernetics: Control and Communication in the Animal and the Machine by [Norbert Wiener](https://en.wikipedia.org/wiki/Norbert_Wiener) (1948)

* [Ratio Club](https://en.wikipedia.org/wiki/Ratio_Club) members include [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing), [Jack Good](https://en.wikipedia.org/wiki/I._J._Good), [Horace Barlow](https://en.wikipedia.org/wiki/Horace_Barlow), [Donald MacKay](https://en.wikipedia.org/wiki/Donald_MacCrimmon_MacKay)

###

* Ideas came out of the Second World War.

    * Researchers explored the use of radar (automated sensing) e.g. Donald MacKay
	* Automatic computation for decryption of military codes (automated decision making) e.g. Jack Good and Alan Turing
	
	* Post-war potential for electronic emulation of what had up until then been the preserve of an animallian nervous system. 


### Watt's Governor

\includeimg{../slides/diagrams/science-holborn-viaduct.jpg}{30%}

<center><i>Science on Holborn Viaduct, cradling Watt's Governor</i></center>

[On Governors](http://www.maths.ed.ac.uk/~v1ranick/papers/maxwell1.pdf), James Clerk Maxwell 1868


### Current Situation

* How are we making computers do the things we used to associated only with humans? 

* Have we made a breakthrough in understanding human intelligence?

* Or is it more "chess playing machines"

### Answer 

* Recent achievements might give the sense that the answer is yes. 

. . . 

* My answer is that we are nowhere near. 

. . . 

* All we’ve achieved for the moment is a breakthrough in *emulating intelligence*. 

### Story

* A man and his dog

### Jeff and His Dog

\includeimg{../slides/diagrams/bezos_taking_my_dog.png}{50%}

###

\includeimg{../slides/diagrams/musk_chollet_control_reinforcement_learning.png}{50%}


###

\includeimg{../slides/diagrams/spot_nick_jeff.jpg}{50%}

###

\includeimg{../slides/diagrams/taleb_skin_in_the_game.png}{50%}

###

* Successful deployments of intelligent systems are common.

* But they are redefined to be non-intelligent. 

* My favourite example is [Watt’s governor](https://en.wikipedia.org/wiki/Centrifugal_governor). 

### Computers

* A hundred years ago *computers* were human beings.

* Digital computers originally called *automatic computers* 

* Do we think of such a computer as intelligent?


###

<center>Are we close to creating intelligence?</center>


### Two Answers

1. Current technology is a long way from emulating all aspects of human intelligence: there are a number of technological breakthroughs that remain before we crack the fundamental nature of human intelligence.

. . .

2. More controversially, I believe that there are aspects of human intelligence that we will never be able to emulate, a preserve that remains uniquely ours. 

### Review of Current Technology
 
* Recent breakthroughs  driven by machine learning. 

    * More precisely: deep learning
	
* So what are deep learning and machine leaning? 


\include{../_ml/includes/what-is-ml.md}

\include{../_ml/includes/what-does-machine-learning-do.md}

### Deep Learning

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition

\include{../_ml/includes/deep-learning-overview.md}

\include{../_ai/includes/deploying-ai.md}
\include{../_ai/includes/ml-systems-design-long.md}
\include{../_ai/includes/artificial-vs-natural-systems.md}
\include{../_ai/includes/engineering-systems-design.md}
\include{../_ai/includes/pigeonholing.md}
\include{../_ai/includes/intelligent-system-paolo.md}

### 

* Need to deal with uncertainty and increase robustness.

* Today, it is easy to make a fool of an artificial intelligent agent.

* Technology needs to address the challenge of the uncertain environment to achieve robust intelligences.

\include{../_ai/includes/the-diving-bell-butterfly.md}
\include{../_ai/includes/jean-dominique-bauby.md}
\include{../_ai/includes/embodiment-factors-tedx.md}
#\include{../_ai/includes/sahelanthropus-tchadensis.md}
\include{../_ai/includes/marcel-renault.md}
\include{../_ai/includes/caleb-mcduff.md}
\include{../_ai/includes/conversation.md}
\include{../_ai/includes/baby-shoes.md}
\include{../_ai/includes/computer-conversation.md}


### Conclusion I

* We are a *long* way from emulating human intelligence, animal intelligence, animal motion. 

* The objectives of *cybernetics* still have not been reached. 

* The *robustness* of natural systems is outside the scope of our current design methodologies.

### Conclusion II

* There is something quintisential about the *human* experience.

* We are co-evolved to view the world in a certain way to enable collaboration.

* Our consciousness is a consequence of our limitations. Our *locked-in* intelligence.

