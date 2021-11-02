\ifndef{deepLearningAsPinball}
\define{deepLearningAsPinball}
\editme

\subsubsection{Deep Learning as Pinball}

\figure{\includejpg{\diagramsDir/576px-Early_Pinball}{50%}}{Deep learning models are composition of simple functions. We can think of a pinball machine as an analogy. Each layer of pins corresponds to one of the layers of functions in the model. Input data is represented by the location of the ball from left to right when it is dropped in from the top. Output class comes from the position of the ball as it leaves the pins at the bottom.}{early-pinball}

\notes{Sometimes deep learning models are described as being like the brain, or too complex to understand, but one analogy I find useful to help the gist of these models is to think of them as being similar to early pin ball machines. 

In a deep neural network, we input a number (or numbers), whereas in pinball, we input a ball. 

Think of the location of the ball on the left-right axis as a single number. Our simple pinball machine can only take one number at a time. As the ball falls through the machine, each layer of pins can be thought of as a different layer of 'neurons'. Each layer acts to move the ball from left to right. 

In a pinball machine, when the ball gets to the bottom it might fall into a hole defining a score, in a neural network, that is equivalent to the decision: a classification of the input object. 

An image has more than one number associated with it, so it is like playing pinball in a *hyper-space*.}

\include{_software/includes/notutils-install.md}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('pinball{sample:0>3}.svg', 
                            directory='\writeDiagramsDir',
							sample=IntSlider(1, 1, 2, 1))}

\newslide{}

\figure{\includediagram{\diagramsDir/pinball001}{80%}}{At initialization, the pins, which represent the parameters of the function, aren't in the right place to bring the balls to the correct decisions.}{pinball-initialization}

\newslide{}

\figure{\includediagram{\diagramsDir/pinball002}{80%}}{After learning the pins are now in the right place to bring the balls to the correct decisions.}{pinball-trained}

\notes{Learning involves moving all the pins to be in the correct position, so that the ball ends up in the right place when it's fallen through the machine. But moving all these pins in hyperspace can be difficult. 

In a hyper-space you have to put a lot of data through the machine for to explore the positions of all the pins. Even when you feed many millions of data points through the machine, there are likely to be regions in the hyper-space where no ball has passed. When future test data passes through the machine in a new route unusual things can happen.

*Adversarial examples* exploit this high dimensional space. If you have access to the pinball machine, you can use gradient methods to find a position for the ball in the hyper space where the image looks like one thing, but will be classified as another.}

\notes{Probabilistic methods explore more of the space by considering a range of possible paths for the ball through the machine. This helps to make them more data efficient and gives some robustness to adversarial examples.}

\endif
