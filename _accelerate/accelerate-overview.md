---
title: Accelerate-Spark Information Session
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
- family: Montgomery
  given: Jessica K.
  url: http://mlatcl.github.io/people/jessica-montgomery.html
  institute: University of Cambridge
- family: Urma
  given: Raoul-Gabriel 
  institute: Cambridge Spark
  url: https://urma.com/
date: 2020-12-04
venue: Virtual
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---



\include{../talk-macros.gpp}


\subsection{Accelerate-Spark information session}

\speakernotes{Running order:

Neil to welcome and introduce the Programme, then hand over to
    Raoul;

Raoul to brief on the content of the Spark Residency;

Neil to manage Q&A from attendees.}


\subsection{Welcome}

* Zoom housekeeping
    * Microphone on mute when not speaking.
	* "Raise Hand" or post in chat for questions.


\speakernotes{Thanks, everyone, for coming to today’s session.

Before we get started, a few points of Zoom housekeeping:

Please keep your microphone on mute if you’re not speaking.

To open, Raoul and I will say a few words about the Accelerate
        Programme and our data science for science residency with
        Cambridge Spark. There will then be an opportunity to ask
        questions. To ask a question, you can post in the chat or use
        the ‘raise hand’ function.}

\subsection{A University Computing Laboratory}

> In 1932 John Lennard-Jones, Professor of Theoretical Physics at
> Bristol University, was appointed to the John Humphrey Plummer Chair
> of Theoretical Chemistry at Cambridge University, which had become
> available thanks to a munificent bequest to the University of
> £200,000. In his new position Lennard-Jones continued the research
> he had started at Bristol University on the application of quantum
> mechanics to problems associated with chemistry. He and his students
> identified a number of problems that gave rise to complex equations
> which could only be solved by numerical methods.
> 
> Cambridge Computing (@Ahmed-cambridge13, pg 21)


\notes{The Department of Computer Science and Technology was set up in the
    1930s, when it was known as the Mathematical Laboratory. At that
    time ‘computer’ had a different meaning – a computer was a person
    employed to do numerical calculations by hand. But advances in
    mechanical systems looked promising.}

\notes{The case for creating the Lab, which was made in a report to the
    University in 1936, argued that:

-   Mechanical devices for performing calculations were developing
        (and human ‘computers’ were becoming harder to find).

-   A range of scientists from across disciplines were looking to
        make use of machines for numerical work.

-   But, despite their promise, the machines available at the time
        were unsuitable for some complex problems – tackling these would
        require better machines to be developed.

-   In response to these needs, the Lab was set up with the aim of
    enabling researchers to make use of new mechanical computers and
    developing more sophisticated machines to tackle complex problems.}
	
\newslide{}

\figure{\includepng{\diagramsDir/accelerate/human-computers-at-work}{40%}}{A typical accounting office in a large commercial organisation showing 'computers' at work using mechanical or electrical machines as calculators. Image from ["Cambridge Computing: The First 75 Years"](https://www.cl.cam.ac.uk/downloads/books/CambridgeComputing_Ahmed.pdf)}{human-computers-at-work}


\subsection{AI for Science}

\notes{Recent years have brought a lot of excitement about artificial intelligence, and its potential to revolutionise research.}

\notes{In some disciplines, machine learning is already supporting impressive
advances. Just this week, for example, we’ve seen headlines about new
work by DeepMind, using machine learning to predict patterns of
protein folding – an advance that could unlock the development of a
range of new drugs to treat different diseases.}

\notes{In other areas, there is clear potential for machine learning to make
a contribution, but current tools and techniques aren’t being used as
widely as they could be.}

\figure{\includepng{\diagramsDir/accelerate/bbc-alpha-fold-2}{40%}}{The announcement on 30th November of Alpha Fold 2 result on CASP14.}{bbc-alpha-fold-2}


\newslide{}

> One of biology’s biggest mysteries is how proteins fold to create
> exquisitely unique three-dimensional structures. Every living thing –
> from the smallest bacteria to plants, animals and humans – is defined
> and powered by the proteins that help it function at the molecular
> level.
>
> So far, this mystery remained unsolved, and determining a single
> protein structure often required years of experimental effort. It’s
> tremendous to see the triumph of human curiosity, endeavour and
> intelligence in solving this problem. A better understanding of
> protein structures and the ability to predict them using a computer
> means a better understanding of life, evolution and, of course,
> human health and disease.
>
> Professor Dame Janet Thornton, Director Emeritus of EMBL

\notes{As quoted in the [CASP14 press release](https://predictioncenter.org/casp14/doc/CASP14_press_release.html).}

\notes{This week we received the wonderful news about the AlphaFold2's
breakthrough in protein folding prediction. I've already sent my
congratulations to Demis and the team directly, but I'd also like to
highlight how we fit into this landscape. Several colleagues have asked
me how we can hope to contribute when we already have such tremendous
strides being made by industrial labs. My perspective is that work like
DeepMind's provides beacons that demonstrate the possible. Those
beacons inspire the community, but the success we're looking for is
achieved when such techniques have moved from the hands of the world's
leading AI company into the hands of the scientists. Our aim is to
develop the portfolio of tools available to these scientists and the
skills base to use those tools, empowering them to drive forward their
discoveries. Cambridge University is in a strong position to lead on
this agenda and I view the Accelerate Programme as being the route to
that vision. With that in mind, I'd like to outline some of the
thinking that Jess, Carl Henrik and I have been doing around strategy
for Accelerate.}


\notes{Core to our thinking is that the Programme should function as a ramp or
a bridge. The bridge analogy addresses the intellectual isolation of
machine learning techniques from the sciences, with disciplinary
boundaries contributing to a situation where those students who are
working on ML techniques within a scientific domain are often isolated
from a wider ML community, lacking access to the expertise they need to
avoid reinventing the wheel or chasing phantoms. If we can support these
students then we can scale our activities across the University --
providing opportunities and connections that build skills, ramp-up
current activities, and deliver the step change we envision.}

\notes{Supporting this community is at the core of what we're doing. You've
already seen the "Data for Science" course that we ran across the
summer, our next edition will be in early February. Alongside this,
we're launching an Accelerate Machine Learning school, to be run also in
February, which will take the first Cohort from the Data for Science
course on the next step of their journey to creating their own machine
learning tools. After initial introduction courses on ML, Challenger
Mishra will deliver a day focusing on how AI techniques are used in
science.}

\newslide{}

\figure{\includepng{\diagramsDir/accelerate/ai-revolution-in-scientific-research}{40%}}{Joint report from the Royal Society and the Alan Turing Institute on the [AI revolution in scientific research](https://royalsociety.org/-/media/policy/projects/ai-and-society/AI-revolution-in-science.pdf?la=en-GB&hash=5240F21B56364A00053538A0BC29FF5F)}{ai-revolution-in-scientific-research}

\newslide{}

\figure{\includepng{\diagramsDir/accelerate/ai-is-changing-how-we-do-science}{40%}}{[Article from July 2017](https://www.sciencemag.org/news/2017/07/ai-changing-how-we-do-science-get-glimpse) in how AI is changing the way we do Science.}{ai-is-changing-how-we-do-science}

\newslide{}

\figure{\includepng{\diagramsDir/accelerate/babbage-difference-engine}{60%}}{Difference Engine No 2, designed by Charles Babbage but completed in June 1991 by [Doron Swade and colleagues](https://collection.sciencemuseumgroup.org.uk/objects/co526657/difference-engine-no-2-designed-by-charles-babbage-built-by-science-museum-difference-engine) at the Science Museum in London.}{babbage-difference-engine}


\subsection{The Accelerate Programme}

\slides{* Research
* Teaching and learning
    * Ramp or Bridge model
* Engagement}

\notes{We’re now in a new phase of the development of computing, with rapid
advances in machine learning. But we see some of the same issues –
researchers across disciplines hope to make use of machine learning,
but need access to skills and tools to do so, while the field
machine learning itself will need to develop new methods to tackle
some complex, ‘real world’ problems.}

\notes{It is with these challenges in mind that the Computer Lab has
started the Accelerate Programme for Scientific Discovery. This new
Programme is seeking to support researchers across the University to
develop the skills they need to be able to use machine learning and
AI in their research.}

\notes{To do this, the Programme is developing three areas of activity:}

\notes{* Research: we’re developing a research agenda that develops
and applies cutting edge machine learning methods to scientific
challenges, with four Accelerate Research fellows working directly on
issues relating to computational biology, psychiatry, string theory
and materials science. While we’re concentrating on STEM subjects for
now, in the longer term our ambition is to build links with the social
sciences and humanities.}

\notes{* Teaching and learning: building on the teaching activities
already delivered through University courses, we’re creating a
pipeline of learning opportunities to help PhD students and
postdocs better understand how to use data science and machine
learning in their work. Our programme with Spark is one element
of this, and we’ll be announcing further activities soon.}

\notes{* Engagement: we hope that Accelerate will help build a community
of researchers working across the University at the interface on
machine learning and the sciences, helping to share best
practice and new methods, and support each other in advancing
their research. Over the coming years, we’ll be running a
variety of events and activities in support of this, and would
welcome your ideas about what might be most useful.}

\newslide{}

\figure{\includepng{\diagramsDir/accelerate/j-j-thomson-avenue}{60%}}{The Computer Lab is located on J. J. Thomson Avenue, right next to the Cavendish laboratory.}{j-j-thomson}

\subsection{Accelerate-Spark data science for science residency}

\slides{* Next activity:
    * Data for science residency.
* Hand over to Raoul.}

\notes{* The next activity from the Accelerate Programme is our data
for science residency with Cambridge Spark. This five-week
programme will equip participants with tools and techniques in data
science that they can apply in their work, with a focus on using the
methods taught on the course to solve your research problems.}

\notes{* To give a bit more detail on the content of this course, I’ll
hand over now to Raoul-Gabriel Urma, Cambridge Spark’s founder.}


\thanks

\references
