\ifndef{conversationComputer}
\define{conversationComputer}
\editme
\newslide{}

\notes{\subsection{Computer Conversations}}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}


\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('\stubname{sample:0>3}.svg', 
                            '\diagramsDir',  sample=IntSlider(0, 0, 7, 1))}

\define{\stubname}{anne-computer-conversation}

\define{\divoptions}{maxwidth:100vw; max-height:100vh}
\define{\widthVal}{80%}
\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{000}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{001}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{002}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{003}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{004}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{005}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{006}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{007}}{\widthVal}}

\notes{\figure{\includediagram{\diagramsDir/\concat{\stubname}{006}}{80%}}{Conversation relies on internal models of other individuals.}{anne-computer-conversation-6}}

\notes{\figure{\includediagram{\diagramsDir/\concat{\stubname}{007}}{80%}}{Misunderstanding of context and who we are talking to leads to arguments.}{anne-computer-conversation-8}}

\speakernotes{This can be disturbing to humans because we are used to a low bandwidth communication rate. }


\notes{Similarly, we find it difficult to comprehend how computers are making decisions. Because they do so with more data than we can possibly imagine.

In many respects, this is not a problem, it's a good thing. Computers and us are good at different things. But when we interact with a computer, when it acts in a different way to us, we need to remember why.

Just as the first step to getting along with other humans is understanding other humans, so it needs to be with getting along with our computers. 

Embodiment factors explain why, at the same time, computers are so impressive in simulating our weather, but so poor at predicting our moods. Our complexity is greater than that of our weather, and each of us is tuned to read and respond to one another.

Their intelligence is different. It is based on very large quantities of data that we cannot absorb. Our computers don’t have a complex internal model of who we are. They don’t understand the human condition. They are not tuned to respond to us as we are to each other.

Embodiment factors encapsulate a profound thing about the nature of humans. Our locked in intelligence means that we are striving to communicate, so we put a lot of thought into what we’re communicating with. And if we’re communicating with something complex, we naturally anthropomorphize them. 

We give our dogs, our cats, and our cars human motivations. We do the same with our computers. We anthropomorphize them. We assume that they have the same objectives as us and the same constraints. They don’t. 

This means, that when we worry about artificial intelligence, we worry about the wrong things. We fear computers that behave like more powerful versions of ourselves that will struggle to outcompete us. 

In reality, the challenge is that our computers cannot be human enough. They cannot understand us with the depth we understand one another. They drop below our cognitive radar and operate outside our mental models. 

The real danger is that computers don’t anthropomorphize. They’ll make decisions in isolation from us without our supervision because they can’t communicate truly and deeply with us.}

\endif
