\subsection{Artificial Intelligence and Data Science}
\slides{
* AI aims to equip computers with human capabilities
    * Image understanding
	* Computer vision
	* Speech recognition
	* Natural language understanding
	* Machine translation
}
\notes{Artificial intelligence has the objective of endowing computers with human-like intelligent capabilities. For example, understanding an image (computer vision) or the contents of some speech (speech recognition), the meaning of a sentence (natural language processing) or the translation of a sentence (machine translation).}
\subsection{Supervised Learning for AI}
\slides{
* Dominant approach today:
    * Generate large labelled data set from humans.
	* Use *supervised learning* to emulate that data.
	    * *E.g.* [ImageNet](www.image-net.org) @Russakovsky-imagenet15
* Significant advances due to *deep learning*
	* *E.g.* Alexa, Amazon Go
}
\notes{The machine learning approach to artificial intelligence is to collect and annotate a large data set from humans. The problem is characterized by input data (e.g. a particular image) and a label (e.g. is there a car in the image yes/no). The machine learning algorithm fits a mathematical function (I call this the *prediction function*) to map from the input image to the label. The parameters of the prediction function are set by minimizing an error between the function’s predictions and the true data. This mathematical function that encapsulates this error is known as the *objective function*.}

\notes{This approach to machine learning is known as *supervised learning*.  Various approaches to supervised learning use different prediction functions, objective functions or different optimization algorithms to fit them.}

\notes{For example, *deep learning* makes use of *neural networks* to form the predictions. A neural network is a particular type of mathematical function that allows the algorithm designer to introduce invariances into the function.}

\notes{An invariance is an important way of including prior understanding in a machine learning model. For example, in an image, a car is still a car regardless of whether it’s in the upper left or lower right corner of the image. This is known as translation invariance. A neural network encodes translation invariance in *convolutional layers*. Convolutional neural networks are widely used in image recognition tasks.}

\notes{An alternative structure is known as a recurrent neural network (RNN).  RNNs neural networks encode temporal structure. They use auto regressive connections in their hidden layers, they can be seen as time series models which have non-linear auto-regressive basis functions. They are widely used in speech recognition and machine translation.}

\notes{Machine learning has been deployed in Speech Recognition (e.g. Alexa, deep neural networks, convolutional neural networks for speech recognition), in computer vision (e.g. Amazon Go, convolutional neural networks for person recognition and pose detection).}

\newslide{Data Science}
\slides{
* Arises from *happenstance data*.
* Differs from statistics in that the question comes *after* data collection.
}
\notes{The field of data science is related to AI, but philosophically different. It arises because we are increasingly creating large amounts of data through *happenstance* rather than active collection. In the modern era data is laid down by almost all our activities. The objective of data science is to extract insights from this data.}

\notes{Classically, in the field of statistics, data analysis proceeds by assuming that the question (or scientific hypothesis) comes before the data is created. E.g., if I want to determine the effectiveness of a particular drug I perform a *design* for my data collection. I use foundational approaches such as randomization to account for confounders. This made a lot of sense in an era where data had to be actively collected. The reduction in cost of data collection and storage now means that many data sets are available which weren’t collected with a particular question in mind. This is a challenge because bias in the way data was acquired can corrupt the insights we derive. We can perform randomized control trials (or A/B tests) to verify our conclusions, but the opportunity is to use data science techniques to better guide our question selection or even answer a question without the expense of a full randomized control trial (referred to as A/B testing in modern internet parlance).}
