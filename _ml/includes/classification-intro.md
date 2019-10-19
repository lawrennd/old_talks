\ifndef{classificationIntro}
\define{classificationIntro}
\editme

\subsection{Introduction to Classification}

\newslide{Classification}
\slides{
* *Wake word* classification (Global Pulse Project).
* Breakthrough in 2012 with ImageNet result of [Alex Krizhevsky, Ilya Sutskever and Geoff Hinton](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-)
}
\notes{Classification is perhaps the technique most closely assocated with machine learning. In the speech based agents, on-device classifiers are used to determine when the wake word is used. A wake word is a word that wakes up the device. For the Amazon Echo it is "Alexa", for Siri it is "Hey Siri". Once the wake word detected with a classifier, the speech can be uploaded to the cloud for full processing, the speech recognition stages. 

A major breakthrough in image classification came in 2012 with the ImageNet result of [Alex Krizhevsky, Ilya Sutskever and Geoff Hinton](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-) from the University of Toronto. ImageNet is a large data base of 14 million images with many thousands of classes. The data is used in a community-wide challenge for object categorization. Krizhevsky et al used convolutional neural networks to outperform all previous approaches on the challenge. They formed a company which was purchased shortly after by Google. This challenge, known as object categorisation, was a major obstacle for practical computer vision systems. Modern object categorization systems are close to human performance.}

\notes{Machine learning problems normally involve a prediction function and an objective function. Regression is the case where the prediction function iss over the real numbers, so the codomain of the functions, $\mappingFunction(\inputMatrix)$ was the real numbers or sometimes real vectors. The classification problem consists of predicting whether or not a particular example is a member of a particular class. So we may want to know if a particular image represents a digit 6 or if a particular user will click on a given advert. These are classification problems, and they require us to map to *yes* or *no* answers. That makes them naturally discrete mappings.}

\slides{* We are given a  data set containing 'inputs', $\inputMatrix$ and 'targets', $\dataVector$.
* Each data point consists of an input vector $\inputVector_i$ and a class label, $\dataScalar_i$.
* For binary classification assume $\dataScalar_i$ should be either $1$ (yes) or $-1$ (no).
* Input vector can be thought of as features.}


\newslide{Discrete Probability}

\notes{In classification we are given an input vector, $\inputVector$, and an associated label, $\dataScalar$ which either takes the value $-1$ to represent *no* or $1$ to represent *yes*.}
\slides{* Algorithms based on *prediction* function and *objective* function.
* For regression the *codomain* of the functions, $f(\inputMatrix)$ was the real numbers or sometimes real vectors. 
* In classification we are given an input vector, $\inputVector$, and an associated label, $\dataScalar$ which either takes the value $-1$ or $1$.}

\newslide{Classification}
\slides{
* Inputs, $\inputVector$, mapped to a label, $\dataScalar$, through a function $\mappingFunction(\cdot)$ dependent on parameters, $\weightVector$, 
$$
\dataScalar = \mappingFunction(\inputVector; \weightVector).
$$
* $\mappingFunction(\cdot)$ is known as the *prediction function*.}
\notes{
In supervised learning the inputs, $\inputVector$, are mapped to a label, $\dataScalar$, through a function $\mappingFunction(\cdot)$ that is dependent on a set of parameters, $\weightVector$, 
$$
\dataScalar = \mappingFunction(\inputVector; \weightVector).
$$
The function $\mappingFunction(\cdot)$ is known as the *prediction function*. The key challenges are (1) choosing which features, $\inputVector$, are relevant in the prediction, (2) defining the appropriate *class of function*, $\mappingFunction(\cdot)$, to use and (3) selecting the right parameters, $\weightVector$.}


\endif
