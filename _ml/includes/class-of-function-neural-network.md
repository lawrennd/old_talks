\ifndef{classOfFunctionNeuralNetwork}
\define{classOfFunctionNeuralNetwork}

\editme

\subsection{Class of Function: Neural Networks}
\slides{
* ImageNet: *convolutional neural network*
* Convolutional neural network introduces *invariances*}

\newslide{Class of Function: Invariances}
\slides{
* An invariance is a transformation of the input
    * e.g. a cat remains a cat regardless of location (translation), size (scale) or upside-down (rotation and reflection).
}

\notes{One class of function that has become popular recently is neural network functions, in particular deep neural networks. The ImageNet challenge uses *convolutional neural networks* which introduce a *translation invariance* to the prediction function.

It's impressive that only this additional invariance is enough to improve performance so much, particularly when we know that rotational invariances and scale invariances are also applicable for object detection in images.}

\include{_ml/includes/deep-learning-overview.md}

\subsection{Encoding Knowledge}
\slides{
* Encode invariance is encoding knowledge
* Unspecified invariances must be learned
* Learning may require a  *lot* more data.
* Less *data efficient*}

\notes{Knowledge that is not encoded in the prediction function must be learned through data. So any unspecified invariance (such as rotational or scale invariances) must be learned through the data. This means that learning would require a lot more data than otherwise would be necessary and results in less data efficient algorithms. 

The choice of predication funciton and invariances is therefore a critical stage in designing your machine learning algorithm. Unfortunately many invariances are non-trivial to incorporate and many machine learning algorithms focus on simpler concepts such as linearity or smoothness.}

\endif
