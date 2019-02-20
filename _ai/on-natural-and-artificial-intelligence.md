---
transition: None
title: Natural and Artificial Intelligence
abstract: "What is the nature of machine intelligence and how does it differ from humans? In this talk we explore some of the differences between natural and machine intelligence."
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
extras:
- link: https://arxiv.org/abs/1705.07996
  label: Paper on Mind and Machine Intelligence
layout: talk
venue: Amazon Thursday Thoughts
date: 2018-03-29
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
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

\newslide{}
\slides{
\aligncenter{Are we close to creating intelligence?</center>}
}
\notes{*How are we making computers do the things we used to associated only with humans? Have we made a breakthrough in understanding human intelligence?*

While recent achievements might give the sense that the answer is yes, the short answer is that we are nowhere near. All we’ve achieved for the moment is a breakthrough in *emulating intelligence*. }

\newslide{What is Intelligence?}
\slides{
* Poorly defined.
    * My definition: use of information to achieve goals more efficiently.
	* Efficiency is defined through use of less resource.
* Automated decision making: we are continuing to progress well.
}

\newslide{The Silicon Factor}
\slides{
* BBC 1, London, 14th September 1980
* [Series of three programmes](http://genome.ch.bbc.co.uk/8bb0b5a05c38403280483e2f96aff1b9) investigating the so-called microelectronics revolution.
* The promise (and perils) of silicon was broadly similar to that for AI today.
}


\newslide{Public Definition}
\slides{
* Doing things that humans do.
    * There is a narcissistic element to our understanding of *artificial intelligence*
* It's a shifting definition.
    * Intelligence is the stuff I can do computers can't.
}

\notes{A more recent example comes from the middle of the last century. A hundred years ago *computers* were human beings, often female, who conducted repetitive mathematical tasks for the creation of mathematical tables such as logarithms. Our modern digital computers were originally called *automatic computers* to reflect the fact that the intelligence of these human operators had been automated. But despite the efficiency with which they perform these tasks, very few think of their mobile phones or computers as intelligent.}



\newslide{Cybernetics and the Ratio Club}
\slides{
* Cybernetics: Control and Communication in the Animal and the Machine by [Norbert Wiener](https://en.wikipedia.org/wiki/Norbert_Wiener) (1948)
* [Ratio Club](https://en.wikipedia.org/wiki/Ratio_Club) members include [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing), [Jack Good](https://en.wikipedia.org/wiki/I._J._Good), [Horace Barlow](https://en.wikipedia.org/wiki/Horace_Barlow), [Donald MacKay](https://en.wikipedia.org/wiki/Donald_MacCrimmon_MacKay)
}
\notes{Norbert Wiener launched last century’s first wave of interest in emulation of intelligence with his book “Cybernetics”. The great modern success that stemmed from that work is the modern engineering discipline of Automatic Control. The technology that allows fighter jets to fly. These ideas came out of the Second World War, when researchers explored the use of radar (automated sensing) and automatic computation for decryption of military codes (automated decision making). Post war a body of researchers, including Alan Turing, were seeing the potential for electronic emulation of what had up until then been the preserve of an animallian nervous system.}



\newslide{ }
\slides{
* Ideas came out of the Second World War.
    * Researchers explored the use of radar (automated sensing) e.g. Donald MacKay
	* Automatic computation for decryption of military codes (automated decision making) e.g. Jack Good and Alan Turing
	* Post-war potential for electronic emulation of what had up until then been the preserve of an animallian nervous system. 


\newslide{The Centrifugal Governor}
\figure{
\includejpg{../slides/diagrams/science-holborn-viaduct}{30%}
\caption{Science on Holborn Viaduct, cradling the Centrifugal Governor.}
}
\slides{
[On Governors](http://www.maths.ed.ac.uk/~v1ranick/papers/maxwell1.pdf), James Clerk Maxwell 1868
}
\notes{Artificial intelligence is a badly defined term. Successful deployments of intelligent systems are common, but normally they are redefined to be non-intelligent. My favourite example is [the Centrifugal governor](https://en.wikipedia.org/wiki/Centrifugal_governor). Applied to the Steam Engine by Boulton and Watt and immortalised in the arms of the statue of “Science” on the Holborn viaduct in London, the centrifugal governor automatically regulated the speed of a steam engine, closing the inlet valve progressively as the engine ran faster. It did the job that an intelligent operator used to have to do, but few today would describe it as “artificial intelligence”.}

\newslide{Current Situation}
\slides{
* How are we making computers do the things we used to associated only with humans? 
* Have we made a breakthrough in understanding human intelligence?
* Or is it more "chess playing machines"
}
\notes{So what of the modern revolution? Is this any different? Are we finally encroaching on the quintessential nature of human intelligence? Or is there a last bastion of our minds that remains out of reach from this latest technical wave?} 

\newslide{Answer}
\slides{ 
* Recent achievements might give the sense that the answer is yes. 

. . . 

* My answer is that we are nowhere near. 

. . . 

* All we’ve achieved for the moment is a breakthrough in *emulating intelligence*. 
}
\notes{
My answer has two parts. Firstly, current technology is a long way from emulating all aspects of human intelligence: there are a number of technological breakthroughs that remain before we crack the fundamental nature of human intelligence. Secondly, and perhaps more controversially, I believe that there are aspects of human intelligence that we will never be able to emulate, a preserve that remains uniquely ours. 

Before we explore these ideas though, we first need to give some sense of current technology.
 
Recent breakthroughs in artificial intelligence are being driven by advances in machine learning. Or more precisely, a sub domain of that field known as deep learning. So what is deep learning? Well, machine learning algorithms proceed in the following way. They observe data, often from humans, and they attempt to emulate that data creation process with a mathematical function. Let’s explain that in a different way. Whichever activities we are interested in emulating, we acquire data about them. Data is simply a set of numbers representing the activity. It might include location, or number representing past behaviour. Once we have the behaviour represented in a set of numbers, then we can emulate it mathematically.}

\notes{Different mathematical functions have different characteristics, in trigonometry we learnt about sine and cosine functions. Those are functions that have a period. They repeat over time. They are useful for emulating behaviour that repeats itself, perhaps behaviour that reflects day/night cycles. But these functions on their own are too simple to emulate human behaviour in all its richness. So how do we make things more complex? In practice we can add functions together, scale them up and scale them down. All these things are done. Deep learning refers to the practice of creating a new function by feeding one function in to another. So we create the output of a function, feed it in to a new function, and take the output of that as our answer. In maths this is known as *composition* of functions. The advantage is that we can generate much more complex functions from simpler functions. The resulting functions allow us to take an *image* as an input and produce an output that includes numbers representing what the objects or people are in that image. Doing this accurately is achieved through composition of mathematical functions, otherwise known as deep learning. 

To describe this process, I sometimes use the following analogy. Think of a pinball machine with rows of pins. A plunger is used to fire a ball into the top of the machine. Think of each row of pins as a function. The input to the function is the position of the ball along the left to right axis of the machine at the top. The output of the function is the position of the ball as it leaves each row of pins. Composition of functions is simply feeding the output of one row of pins into the next. If we do this multiple times, then although the machine has multiple functions in it, by feeding one function into another, then the entire machine is in itself representing a single function. Just a more complex function than that that any individual row of pins can represent. Our modern machine learning systems are just like this machine. Except they take very high dimensional inputs. The pinball is only represented by its left to right position, a one dimensional function. A real learning machine will often represent multiple dimensions, like playing pinball in a hyperspace.

So the intelligence we’ve created is just a (complex) mathematical function. But how do we make this function match what humans do?  We use more maths. In fact we use another mathematical function. To avoid confusion let’s call the function represented by our pinball machine the *prediction function*. In the pinball machine, we can move the pins around, and any configuration of pins leads to a different answer for our functions. So how do we find the correct configuration? For that we use a separate function known as the *objective function*. 

The objective function measures the dissimilarity between the output of our prediction function, and data we have from the humans. The process of learning in these machines is the process of moving the pins around in the pinball machine to make the prediction more similar to the data. The quality of any given pin configuration is assessed by quantifying the differences between what the humans have done, and what the machine is predicting using the objective function. Different objective functions are used for different tasks, but objective functions are typically much simpler than prediction functions.

So, we have some background. And some understanding of the challenges for the designer of machine learning algorithms. You need data, you need a prediction function, and you need an objective function. Choice of prediction function and objective function are in the hands of the algorithm designer. Deep learning is a way of making very complex, and flexible, classes of prediction functions that deal well with the type of data we get from speech, written language and images. 

But what if the designer gets the choice of prediction function wrong? Or the choice of the objective function wrong? Or what if they choose the right class of prediction function (such as a convolutional neural network, used for classifying images) but get the location of all those pins in the machine wrong?

This is a major challenge for our current generation of AI solutions. They are fragile. They are sensitive to incorrect choices and when they fail, they fail catastrophically.}

\newslide{Story}
\slides{
* A man and his dog
}
\newslide{Jeff and His Dog}
\slides{
\includepng{../slides/diagrams/bezos_taking_my_dog}{50%}
}
\newslide{}
\slides{
\includepng{../slides/diagrams/musk_chollet_control_reinforcement_learning}{50%}
}
\newslide{}
\slides{
\includejpg{../slides/diagrams/spot_nick_jeff}{50%}
}
\newslide{}
\slides{
\includejpg{../slides/diagrams/taleb_skin_in_the_game}{50%}
}
\newslide{}
\slides{
* Successful deployments of intelligent systems are common.
* But they are redefined to be non-intelligent. 
* My favourite example is [Watt’s governor](https://en.wikipedia.org/wiki/Centrifugal_governor). 
}
\newslide{Computers}
\slides{
* A hundred years ago *computers* were human beings.
* Digital computers originally called *automatic computers* 
* Do we think of such a computer as intelligent?
}

\newslide{}
\slides{
\aligncenter{Are we close to creating intelligence?}
}

\newslide{Two Answers}
\slides{
1. Current technology is a long way from emulating all aspects of human intelligence: there are a number of technological breakthroughs that remain before we crack the fundamental nature of human intelligence.

. . .

2. More controversially, I believe that there are aspects of human intelligence that we will never be able to emulate, a preserve that remains uniquely ours. 
}

\newslide{Review of Current Technology
\slides{ 
* Recent breakthroughs  driven by machine learning. 
    * More precisely: deep learning
* So what are deep learning and machine leaning? 
}

\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/what-does-machine-learning-do.md}

\newslide{Deep Learning}
\slides{
* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition
}

\include{_ml/includes/deep-learning-overview.md}
\include{_ai/includes/deploying-ai.md}
\include{_ai/includes/ml-systems-design-long.md}
\include{_ai/includes/artificial-vs-natural-systems.md}
\include{_ai/includes/engineering-systems-design.md}
\include{_ai/includes/pigeonholing.md}
\include{_ai/includes/intelligent-system-paolo.md}

\newslide{}
\slides{
* Need to deal with uncertainty and increase robustness.
* Today, it is easy to make a fool of an artificial intelligent agent.
* Technology needs to address the challenge of the uncertain environment to achieve robust intelligences.
}
\include{_ai/includes/the-diving-bell-butterfly.md}
\include{_ai/includes/jean-dominique-bauby.md}
\include{_ai/includes/embodiment-factors-tedx.md}
#\include{_ai/includes/sahelanthropus-tchadensis.md}
\include{_ai/includes/marcel-renault.md}
\include{_ai/includes/caleb-mcduff.md}
\include{_ai/includes/conversation.md}
\include{_ai/includes/baby-shoes.md}
\include{_ai/includes/computer-conversation.md}

\section{Conclusions}
\newslide{Conclusion I}

* We are a *long* way from emulating human intelligence, animal intelligence, animal motion. 
* The objectives of *cybernetics* still have not been reached. 
* The *robustness* of natural systems is outside the scope of our current design methodologies.


\newslide{Conclusion II}

* There is something quintisential about the *human* experience.
* We are co-evolved to view the world in a certain way to enable collaboration.
* Our consciousness is a consequence of our limitations. Our *locked-in* intelligence.


\thanks

\references
