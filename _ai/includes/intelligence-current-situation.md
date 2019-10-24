\ifndef{intelligenceCurrentSituation}
\define{intelligenceCurrentSituation}

\editme


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

\endif
