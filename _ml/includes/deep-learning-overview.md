###

\fragment{<small>Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected.</small>}{fade-in}

\includeimg{../slides/diagrams/deepface_neg.png}{100%}

<p align="right">
<small>Source: DeepFace</small></p>

### 

\includeimg{../slides/diagrams/576px-Early_Pinball.jpg}{50%}

\notes{We can think of what these models are doing as being similar to early pin ball machines. In a neural network, we input a number (or numbers), whereas in pinball, we input a ball. The location of the ball on the left-right axis can be thought of as the number. As the ball falls through the machine, each layer of pins can be thought of as a different layer of neurons. Each layer acts to move the ball from left to right. 

In a pinball machine, when the ball gets to the bottom it might fall into a hole defining a score, in a neural network, that is equivalent to the decision: a classification of the input object. 

An image has more than one number associated with it, so it's like playing pinball in a *hyper-space*.}

\displaycode{import pods
pods.notebook.display_plots('pinball{sample:0>3}.svg', 
                            '../slides/diagrams', sample=(1,2))}

\slides{
###

\includesvg{../slides/diagrams/pinball001.svg}
}
\notes{At initialization, the pins aren't in the right place to bring the ball to the correct decision.}

\slides{
### {.slide: data-transition="none" }

\includesvg{../slides/diagrams/pinball002.svg}
}
\notes{Learning involves moving all the pins to be in the right position, so that the ball falls in the right place. But moving all these pins in hyperspace can be difficult. In a hyper space you have to put a lot of data through the machine for to explore the positions of all the pins. Adversarial learning reflects the fact that a ball can be moved a small distance and lead to a very different result.

Probabilistic methods explore more of the space by considering a range of possible paths for the ball through the machine.}
