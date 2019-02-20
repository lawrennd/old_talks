\ifndef{deepLearningAsPinball}
\define{deepLearningAsPinball}
\editme

\newslide{Deep Learning as Pinball}

\figure{
\includejpg{../slides/diagrams/576px-Early_Pinball}{40%}
\notes{\caption{Deep learning models are composition of simple functions. We can think of a pinball machine as an analogy. Each layer of pins corresponds to one of the layers of functions in the model. Input data is represented by the location of the ball from left to right when it is dropped in from the top. Output class comes from the position of the ball as it leaves the pins at the bottom.}}
}

\notes{\subsubsection{Deep Learning as Pinball}}

\notes{Sometimes deep learning models are described as being like the brain, or too complex to understand, but one analogy I find useful to help the gist of these models is to think of them as being similar to early pin ball machines. 

In a deep neural network, we input a number (or numbers), whereas in pinball, we input a ball. 

Think of the location of the ball on the left-right axis as a single number. Our simple pinball machine can only take one number at a time. As the ball falls through the machine, each layer of pins can be thought of as a different layer of 'neurons'. Each layer acts to move the ball from left to right. 

In a pinball machine, when the ball gets to the bottom it might fall into a hole defining a score, in a neural network, that is equivalent to the decision: a classification of the input object. 

An image has more than one number associated with it, so it's like playing pinball in a *hyper-space*.}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('pinball{sample:0>3}.svg', 
                            '../slides/diagrams',
							sample=IntSlider(1, 1, 2, 1))}

\newslide{}

\figure{\div{\includediagram{../slides/diagrams/pinball001}}{}{text-align:center}
\notes{\caption{At initialization, the pins, which represent the parameters of the function, aren't in the right place to bring the balls to the correct decisions.}}}

\newslide{}

\figure{\div{\includediagram{../slides/diagrams/pinball002}}{}{text-align:center}
\notes{\caption{After learning the pins are now in the right place to bring the balls to the correct decisions.}}
}

\notes{Learning involves moving all the pins to be in the correct position, so that the ball ends up in the right place when it's fallen through the machine. But moving all these pins in hyperspace can be difficult. 

In a hyper-space you have to put a lot of data through the machine for to explore the positions of all the pins. *Adversarial examples* exploit this idea. 

If you have access to the pinball machine, you can use gradient methods to find a position for the ball in the hyper space where the image looks like one thing, but will be classified as another.}

\notes{Probabilistic methods explore more of the space by considering a range of possible paths for the ball through the machine. This helps to make them more data efficient and gives some robustness to adversarial examples.}

\endif
