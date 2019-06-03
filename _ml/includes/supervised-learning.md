\ifndef{supervisedLearning}
\define{supervisedLearning}
\editme

\section{Supervised Learning}
\newslide{Supervised Learning}
\slides{
* Most widely deployed machine learning technology.
    * Particular domain of success has been *classification*.
* Take input to function (e.g. image)
* Use output to place it in a class (e.g. dog or cat).
* Simple idea underpins a lot of machine learning.}
\notes{Supervised learning is one of the most widely deployed machine learning technologies, and a particular domain of success has been *classification*. Classification is the process of taking an input (which might be an image) and categorizing it into one of a number of different classes (e.g. dog or cat). This simple idea underpins a lot of machine learning. By scanning across the image we can also determine where the animal is in the image.}

\include{_ml/includes/the-perceptron.md}

\newslide{Classification}
\slides{
* Examples in a speech based intelligent agent:  *wake word* classification.
* Major breakthrough for images was in 2012 with the ImageNet result of [Alex Krizhevsky, Ilya Sutskever and Geoff Hinton](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-)
* ImageNet is a large data base of 14 million images with many thousands of classes.
* Data is used in a community-wide challenge for object categorization.
* Krizhevsky et al used *convolutional neural networks*.}
\notes{
Classification is perhaps the technique most closely assocated with machine learning. In the speech based agents, on-device classifiers are used to determine when the wake word is used. A wake word is a word that wakes up the device. For the Amazon Echo it is "Alexa", for Siri it is "Hey Siri". Once the wake word detected with a classifier, the speech can be uploaded to the cloud for full processing, the speech recognition stages. 

A major breakthrough in image classification came in 2012 with the ImageNet result of [Alex Krizhevsky, Ilya Sutskever and Geoff Hinton](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-) from the University of Toronto. ImageNet is a large data base of 14 million images with many thousands of classes. The data is used in a community-wide challenge for object categorization. Krizhevsky et al used convolutional neural networks to outperform all previous approaches on the challenge. They formed a company which was purchased shortly after by Google. This challenge, known as object categorisation, was a major obstacle for practical computer vision systems. Modern object categorization systems are close to human performance.}

\newslide{Supervised Learning}
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


\subsection{Supervised Learning Challenges}

\notes{There are three principal challenges in constructing a problem for supervised learning.}

1. choosing which features, $\inputVector$, are relevant in the prediction
2. defining the appropriate *class of function*, $\mappingFunction(\cdot)$.
3. selecting the right parameters, $\weightVector$.

\subsection{Feature Selection}
\slides{
* Olympic prediction example only using year to predict pace.
* Could also use *course characteristics* (e.g. how hilly) *temperature*. 
* Can use *feature selection algorithms*
* Automate the process of finding the features that we need.}
\notes{Feature selection is a critical stage in the algorithm design process. In the Olympic prediction example above we're only using time to predict the the pace of the runners. In practice we might also want to use characteristics of the course: how hilly it is, what the temperature was when the race was run. In 1904 the runners actually got lost during the race. Should we include 'lost' as a feature? It would certainly help explain the particularly slow time in 1904. The features we select should be ones we expect to correlate with the prediction. In statistics, these features are even called *predictors* which highlights their role in developing the prediction function. For Facebook newsfeed, we might use features that include how close your friendship is with the poster, or how often you react to that poster, or whether a photo is included in the post.

Sometimes we use feature selection algorithms, algorithms that automate the process of finding the features that we need. Classification is often used to rank search results, to decide which adverts to serve or, at Facebook, to determine what appears at the top of your newsfeed. In the Facebook example features might include how many likes a post has had, whether it has an image in it, whether you regularly interact with the friend who has posted. A good newsfeed ranking algorithm is critical to Facebook's success, just as good ad serving choice is critical to Google's success. These algorithms are in turn highly dependent on the feature sets used. Facebook in particular has made heavy investments in machine learning pipelines for evaluation of the feature utility.}

\newslide{Applications}
\slides{
*  rank search results, decide which adverts to serve or, what appears at the top of your newsfeed.
* Facebook features include number of likes, whether it's got an image, whether this is a friend you interact with.
* Newsfeed ranking algorithm is critical to Facebook's success.
* Heavy investments in machine learning pipelines for evaluation of the feature utility.} 

\subsection{Class of Function, $\mappingFunction(\cdot)$}
\slides{
* What should be the characteristics of the mapping between $\inputVector$ and $\dataScalar$?
* Often we choose it to be *smooth* (similar inputs lead to similar outputs).
* Often choose it to be a linear function.
* In *forecasting* we might want a *periodic* function (weekly or seasonal effects).}
\notes{By class of function we mean, what are the characteristics of the mapping between $\mathbf{x}$ and $y$. Often, we might choose it to be a smooth function. Sometimes we will choose it to be a linear function. If the prediction is a forecast, for example the demand of a particular product, then the function would need some periodic components to reflect seasonal or weekly effects. 

In the ImageNet challenge the input, $\mathbf{x}$, was in the form of an image. And the form of the prediction function was a *convolutional neural network* (more on this later). A convolutional neural network introduces *invariances* into the function that are particular to image classification. An invariance is a transformation of the input that we don't want to affect the output. For example, a cat in an image is still a cat no matter where it's located in the image (translation). The cat is also a cat regardless of how large it is (scale), or whether it's upside-down (rotation). Convolutional neural networks encode these invariances: scale invariance, rotation invariance and translation invariance; in the mathematical function. 

Encoding invariance in the prediction function is like encoding knowledge in the model. If we don't specify these invariances, then the model must learn them. This will require a lot more data to achieve the same performance, making the model less data efficient. Note that one invariance that is *not* encoded in a convolutional network is invariance to camera type. As a result, practitioners need to be careful to ensure that their training data is representative of the type of cameras that will be used when the model is deployed. 

In general the prediction function could be any set of parameterized functions. In the Olympic marathon data example above we used a polynomial fit,

$$
\mappingFunction(\inputScalar) = \weightScalar_0 + \weightScalar_1 \inputScalar+ \weightScalar_2 \inputScalar^2 + \weightScalar_3 \inputScalar^3 + \weightScalar_4 \inputScalar^4.
$$

The Olympic example is also a supervised learning challenge. But it is a *regression* problem. A regression problem is one where the output is a continuous value (such as the pace in the marathon). In classification the output is constrained to be discrete. For example, classifying whether or not an image contains a dog implies the output is binary. An early example of a regression problem used in machine learning was [the Tecator data](http://lib.stat.cmu.edu/datasets/tecator), where the fat, water and protein content of meat samples was predicted as a function of the absorption of infrared light.}



\newslide{Class of Function: Neural Networks}
\slides{
* For imagenet prediction function was a *convolutional neural network*
* A convolutional neural network introduces *invariances* into the function that are particular to image classification.}

\newslide{Class of Function: Invariances}
\slides{
* An invariance is a transformation of the input that we don't want to effect the output.
    * e.g. a cat remains a cat regardless of location (translation), size (scale) or upside-down (rotation and reflection).
    * Convolutional neural networks encode invariances in the mathematical function.}

\newslide{Encoding Knowledge}
\slides{
* Encoding invariance is like encoding knowledge in the model.
* If we don't specify these invariances then the model must learn them.
* Learning invariances requires a *lot* more data.
* The amount of data required to achieve a certain performance is the *data efficiency*.}

\newslide{Choosing Prediction Function}
\slides{
* Prediction function can be any set of parameterized functions.
* In the Olympic marathon example above we used a polynomial fit,
$$
\mappingFunction(\inputScalar) = \weightScalar_0 + \weightScalar_1 \inputScalar+ \weightScalar_2 \inputScalar^2 + \weightScalar_3 \inputScalar^3 + \weightScalar_4 \inputScalar^4.
$$
* Olympic example is a supervised learning challenge. But it is a *regression* problem.
* A regression problem is one where the output is a continuous value (such as the pace in the marathon).}


\newslide{Regression Problems}
\slides{
* In classification the output of prediction function is constrained to be discrete.
* An early example of a regression data set used in machine learning was [the Tecator data](http://lib.stat.cmu.edu/datasets/tecator)
    * Fat, water and protein content of meat samples was predicted as a function of the absorption of infrared light.}

\newslide{Parameter Estimation: Objective Functions}
\slides{
* After choosing *features* and *function class* we need *parameters*.
* Estimate $\weightVector$  by specifying an *objective function*.
* The objective function specifies the quality of the match between the prediction function and the *training data*.
* In supervised learning the objective function has input data (for ImageNet, the image, for Olympic marathon the year) and a *label*.}
\notes{### Parameter Estimation

Once we have a set of features, and the class of functions we use is determined, we need to find the parameters of the model. 

The parameters of the model, $\mathbf{w}$, are estimated by specifying an *objective function*. The objective function specifies the quality of the match between the prediction function and the *training data*. In supervised learning the objective function incorporates both the input data (in the ImageNet data the image, in the Olympic marathon data the year of the marathon) and a *label*. 

The label is where the term supervised learning comes from. The idea being that a supervisor, or annotator, has already looked at the data and given it labels. For regression problem, a typical objective function is the *squared error*,
$$
E(\mathbf{w}) = \sum_{i=1}^n (y_i - f(\mathbf{x}_i))^2
$$
where the data is provided to us as a set of $n$ inputs, $\mathbf{x}_1$, $\mathbf{x}_2$, $\mathbf{x}_3$, $\dots$, $\mathbf{x}_n$ each one with an associated label, $y_1$, $y_2$, $y_3$, $\dots$, $y_n$. Sometimes the label is cheap to acquire. For example, in Newsfeed ranking Facebook are acquiring a label each time a user clicks on a post in their Newsfeed. Similarly, in ad-click prediction labels are obtained whenever an advert is clicked. More generally though, we have to employ human annotators to label the data. For example, ImageNet, the breakthrough deep learning result was annotated using Amazon's Mechanical Turk. Without such large scale human input, we would not have the breakthrough results on image categorization we have today. 

Some tasks are easier to annotate than others. For example, in the Tecator data, to acquire the actual values of water, protein and fat content in the meat samples further experiments may be required. It is not simply a matter of human labelling. Even if the task is easy for humans to solve there can be problems. For example, humans will extrapolate the context of an image. A colleague mentioned once to me a challenge where humans were labelling images as containing swimming pools, even though none was visible, because they could infer there must be a pool nearby, perhaps because there are kids wearing bathing suits. But there is no swimming pool in the image for the computer to find. The quality of any machine learning solution is very sensitive to the quality of annotated data we have. Investing in processes and tools to improve annotation of data is therefore priority for improving the quality of machine learning solutions. 

There can also be significant problems with misrepresentation in the data set. If data isn't collected carefully, then it can reflect biases about the population that we don't want our models to have. For example, if we design a face detector using Californians may not perform well when deployed in Kampala, Uganda.}

\newslide{Labels and Squared Error}
\slides{
* *Label* is where the term supervised learning comes from.
* Idea is that a supervisor, or annotator, has already given labels.
* For regression problem, a typical objective function is the *squared error*,
$$
\errorFunction(\weightVector) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputVector_i))^2
$$}

\newslide{Data Provision}
\slides{
* Here the data is provided to us as a set of $\numData$ inputs, $\inputVector_1$, $\inputVector_2$, $\inputVector_3$, $\dots$, $\inputVector_\numData$
* Each data point with an associated label, $\dataScalar_1$, $\dataScalar_2$, $\dataScalar_3$, $\dots$, $\dataScalar_n$.
* Sometimes the label is cheap to acquire.
     * E.g. in Newsfeed ranking Facebook are acquiring a label each time a user clicks on a post in their Newsfeed. (Data Science?)
     * In ad-click prediction labels are obtained whenever an advert is clicked.}

\newslide{Annotation}
\slides{
* Often we have to employ human annotators to label the data.
    * E.g. in ImageNet, the breakthrough deep learning result was annotated using Amazon's Mechanical Turk. (AI?)
* Without large scale human input, would not have the breakthrough results in AI we have today. }


\newslide{Annotation}
\slides{
* Some tasks *easier* to annotate than *others*.
    * For Tecator data, need to acquire the actual values of water, protein and fat content in the meat samples.
    * Each data point requires real experiments}

\newslide{Annotation}
\slides{
* Even for *easy* tasks there will be problems.
    * E.g. humans extrapolate the context of an image.

* Quality of any machine learning solution is very sensitive to the quality of annotated data we have.
* Investing in processes and tools to improve annotation of data is therefore a strong priority.}

\newslide{Misrepresentation}
\slides{
* Can be significant problems with misrepresentation in the data sets.
* If data isn't collected carefully, it can reflect biases about the population that we don't want our models to have.
* A face detector using Californians may not perform well when deployed in Kampala, Uganda.}

\newslide{Automation}
\slides{
* Train supervised learning system, place it in production
* Supervised learning is probably the dominant approaches to learning.
* Cost and time associated with labeling data is a major bottleneck for deploying machine learning systems.
* Creating training data requires significant human effort.}

\newslide{Training and Test}
\slides{
* Very important distinction.
  * Separation between training data and test data (or production data).
* Training data is the data that was used to find the model parameters.
* Test data (or production data) is the data that is used with the live system.
* Ability of a machine learning system to predict well in production is known as its *generalization* ability.
* System's ability to predict in areas where it hasn't previously seen data.}


\subsection{Generalization and Overfitting}
\slides{
* Easy to develop a prediction function that reconstructs the training data exactly: a look up table. you can just use a look up table.
* How would the lookup table predict *between* the training data, where examples haven't been seen before?
* Choice of the class of prediction functions is critical in ensuring that the model generalizes well. 
* Generalization error is normally estimated by applying the objective function to a set of data that the model *wasn't* trained on: the *test data*.}
\notes{Once a supervised learning system is trained it can be placed in a sequential pipeline to automate a process that used to be done manually. 

Supervised learning is one of the dominant approaches to learning. But the cost and time associated with labeling data is a major bottleneck for deploying machine learning systems. The process for creating training data requires significant human intervention. For example, internationalization of a speech recognition system would require large speech corpora in new languages. 

An important distinction in machine learning is the separation between training data and test data (or production data). Training data is the data that was used to find the model parameters. Test data (or production data) is the data that is used with the live system. The ability of a machine learning system to predict well on production systems given only its training data is known as its *generalization* ability. This is the system's ability to predict in areas where it hasn't previously seen data.}


\newslide{Performance}
\slides{
* To ensure good performance we normally want a model that gives us a low generalization error.
* If we weren't sure of the right prediction function to use, then we could try 1,000 different prediction functions.
* We could use the one that gives us the lowest error on the test data.
* But you have to be careful.}

\newslide{Validation and Model Selection}
\slides{
* Selecting a model in this way is like a further stage of training where you are using the test data in the training.
* It is known as *validation*.
* The error is known as *validation error*.
*  Using the validation error for model selection is a standard machine learning technique.}

\newslide{Difficult Trap}
\slides{
* All machine learning practitioners should know not to use the test data in your training procedure.
* But because validation data is used for model selection, it is not an unbiased estimate of the generalization performance.}



\subsection{Overfitting}

\figure{\includeyoutube{py8QrZPT48s}{800}{600}{4m0s}}{Alex Ihler discusses polynomials and overfitting.}{alex-ihler-overfitting}

\slides{*Alex Ihler on Polynomials and Overfitting*}

\include{_ml/includes/olympic-polynomials.md}

\notes{\figure{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis026}{80%}}{Fit of a 26 degree polynomial to the olympic marathon data.}{olympic-lm-polynomial-num-basis-26}}

\notes{We can easily develop a simple prediction function that reconstructs the training data exactly, you can just use a look up table. But how would the lookup table predict between the training data, where examples haven't been seen before? The choice of the class of prediction functions is critical in ensuring that the model generalizes well. 

The generalization error is normally estimated by applying the objective function to a set of data that the model *wasn't* trained on, the test data. To ensure good performance we normally want a model that gives us a low generalization error. If we weren't sure of the right prediction function to use, then we could try 1,000 different prediction functions. Then we could use the one that gives us the lowest error on the test data. But you have to be careful. Selecting a model in this way is like a further stage of training where you are using the test data in the training.[^trainingtest] So when this is done, the data used for this is not known as test data, it is known as *validation data*. And the associated error is the *validation error*. Using the validation error for model selection is a standard machine learning technique, but it can be misleading about the final generalization error. Almost all machine learning practitioners know not to use the test data in your training procedure, but sometimes people forget that when validation data is used for model selection that validation error cannot be used as an unbiased estimate of the generalization performance.

[^trainingtest]: Using the test data in your training procedure is a major error in any machine learning procedure. It is extremely dangerous as it gives a misleading assessment of the model performance. The [Baidu ImageNet scandal](http://inverseprobability.com/2015/06/04/baidu-on-imagenet) was an example of a team competing in the ImageNet challenge which did this. The team had announced via the publication pre-print server Arxiv that they had a world-leading performance on the ImageNet challenge. This was reported in the mainstream media. Two weeks later the challenge organizers revealed that the team had created multiple accounts for checking their test performance more times than was permitted by the challenge rules. This was then reported as "AI's first doping scandal". The team lead was fired by Baidu.}

\endif
