\newslide{}
\slides{

\fragment{\smalltext{Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected.}}{fade-in}}

\div{\includeimg{../slides/diagrams/deepface_neg.png}}{}{width:100%;text-align:center}
\notes{\caption{The DeepFace architecture [@Taigman:deepface14], visualized through colors to represent the functional mappings at each layer. There are 120 million parameters in the model.}}\slides{\alignright{\smalltext{Source: DeepFace [@Taigman:deepface14]}}}

\notes{The DeepFace architecture [@Taigman:deepface14] consists of layers that deal  with *translation* and *rotational* invariances. These layers are followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected layers.}

\newslide{}

\div{\includeimg{../slides/diagrams/576px-Early_Pinball.jpg}}{}{height:600px;text-align:center}
\notes{\caption{Deep learning models are composition of simple functions. We can think of a pinball machine as an analogy. Each layer of pins corresponds to one of the layers of functions in the model. Input data is represented by the location of the ball from left to right when it is dropped in from the top. Output class comes from the position of the ball as it leaves the pins at the bottom.}}

\notes{We can think of what these models are doing as being similar to early pin ball machines. In a neural network, we input a number (or numbers), whereas in pinball, we input a ball. The location of the ball on the left-right axis can be thought of as the number. As the ball falls through the machine, each layer of pins can be thought of as a different layer of neurons. Each layer acts to move the ball from left to right. 

In a pinball machine, when the ball gets to the bottom it might fall into a hole defining a score, in a neural network, that is equivalent to the decision: a classification of the input object. 

An image has more than one number associated with it, so it's like playing pinball in a *hyper-space*.}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}


\displaycode{pods.notebook.display_plots('pinball{sample:0>3}.svg', 
                            '../slides/diagrams',  
							sample=IntSlider(1, 1, 2, 1))}

\newslide{}

\div{\includesvg{../slides/diagrams/pinball001.svg}}{}{text-align:center}
\notes{\caption{At initialization, the pins, which represent the parameters of the function,  aren't in the right place to bring the balls to the correct decisions.}}

\newslide{}

\div{\includesvg{../slides/diagrams/pinball002.svg}}{}{text-align:center}
\notes{\caption{After learning the pins are now in the right place to bring the balls to the correct decisions.}}

\notes{Learning involves moving all the pins to be in the right position, so that the ball falls in the right place. But moving all these pins in hyperspace can be difficult. In a hyper space you have to put a lot of data through the machine for to explore the positions of all the pins. Adversarial learning reflects the fact that a ball can be moved a small distance and lead to a very different result.

Probabilistic methods explore more of the space by considering a range of possible paths for the ball through the machine.}
