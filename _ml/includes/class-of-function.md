\ifndef{classOfFunction}
\define{classOfFunction}

\editme

\subsection{Class of Function, $\mappingFunction(\cdot)$}
\slides{
* Mapping characteristic between $\inputVector$ and $\dataScalar$?
  * *smooth* (similar inputs lead to similar outputs).
  * linear function.
  * In *forecasting*,  *periodic*}
\notes{By class of function we mean, what are the characteristics of the mapping between $\mathbf{x}$ and $y$. Often, we might choose it to be a smooth function. Sometimes we will choose it to be a linear function. If the prediction is a forecast, for example the demand of a particular product, then the function would need some periodic components to reflect seasonal or weekly effects.}

talk-macros.gpp}p/includes/bda-forecasting.md}

\notes{In the ImageNet challenge the input, $\inputVector$, was in the form of an image. And the form of the prediction function was a *convolutional neural network* (more on this later). A convolutional neural network introduces *invariances* into the function that are particular to image classification. An invariance is a transformation of the input that we don't want to affect the output. For example, a cat in an image is still a cat no matter where it's located in the image (translation). The cat is also a cat regardless of how large it is (scale), or whether it's upside-down (rotation). Convolutional neural networks encode these invariances: scale invariance, rotation invariance and translation invariance; in the mathematical function. 

Encoding invariance in the prediction function is like encoding knowledge in the model. If we don't specify these invariances, then the model must learn them. This will require a lot more data to achieve the same performance, making the model less data efficient. Note that one invariance that is *not* encoded in a convolutional network is invariance to camera type. As a result, practitioners need to be careful to ensure that their training data is representative of the type of cameras that will be used when the model is deployed. 

In general the prediction function could be any set of parameterized functions. In the Olympic marathon data example above we used a polynomial fit,
$$
\mappingFunction(\inputScalar) = \weightScalar_0 + \weightScalar_1 \inputScalar+ \weightScalar_2 \inputScalar^2 + \weightScalar_3 \inputScalar^3 + \weightScalar_4 \inputScalar^4.
$$
The Olympic example is also a supervised learning challenge. But it is a *regression* problem. A regression problem is one where the output is a continuous value (such as the pace in the marathon). In classification the output is constrained to be discrete. For example, classifying whether or not an image contains a dog implies the output is binary. An early example of a regression problem used in machine learning was [the Tecator data](http://lib.stat.cmu.edu/datasets/tecator), where the fat, water and protein content of meat samples was predicted as a function of the absorption of infrared light.}

talk-macros.gpp}l/includes/class-of-function-neural-network.md}

\newslide{Choosing Prediction Function}
\slides{
* Any function e.g. polynomials for olympic data
$$
\mappingFunction(\inputScalar) = \weightScalar_0 + \weightScalar_1 \inputScalar+ \weightScalar_2 \inputScalar^2 + \weightScalar_3 \inputScalar^3 + \weightScalar_4 \inputScalar^4.
$$
}


\endif
