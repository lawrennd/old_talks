### Supervised Learning

* Most widely deployed machine learning technology.

    * Particular domain of success has been *classification*.

* Take input to function (e.g. image)

* Use output to place it in a class (e.g. dog or cat).

* Simple idea underpins a lot of machine learning.

\include{../../_ml/includes/the-perceptron.md}

### Classification

* Examples in a speech based intelligent agent:  *wake word* classification.

* Major breakthrough for images was in 2012 with the ImageNet result of [Alex Krizhevsky, Ilya Sutskever and Geoff Hinton](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-)

* ImageNet is a large data base of 14 million images with many thousands of classes.

* Data is used in a community-wide challenge for object categorization.

* Krizhevsky et al used *convolutional neural networks*.

### Supervised Learning

* Inputs, $\inputVector$, mapped to a label, $\dataScalar$, through a function $\mappingFunction(\cdot)$ dependent on parameters, $\weightVector$, 

$$
\dataScalar = \mappingFunction(\inputVector; \weightVector).
$$

* $f(\cdot)$ is known as the *prediction function*.

### Supervised Learning Challenges

1. choosing which features, $\inputVector$, are relevant in the prediction

2. defining the appropriate *class of function*, $\mappingFunction(\cdot)$.

3. selecting the right parameters, $\weightVector$. 

### Feature Selection

* Olympic prediction example only using year to predict pace.

* Could also use *course characteristics* (e.g. how hilly) *temperature*. 

* Can use *feature selection algorithms*

* Automate the process of finding the features that we need.

### Applications

*  rank search results,  decide which adverts to serve or, what appears at the top of your newsfeed.

* Facebook features include number of likes, whether it's got an image, whether this is a friend you interact with.

* Newsfeed ranking algorithm is critical to Facebook's success.

* Heavy investments in machine learning pipelines for evaluation of the feature utility. 

### Class of Function, $\mappingFunction(\cdot)$

* What should be the characteristics of the mapping between $\inputVector$ and $\dataScalar$?

* Often we choose it to be *smooth* (similar inputs lead to similar outputs).

* Often choose it to be a linear function.

* In *forecasting* we might want a *periodic* function (weekly or seasonal effects).

### Class of Function: Neural Networks

* For imagenet prediction function was a *convolutional neural network*

* A convolutional neural network introduces *invariances* into the function that are particular to image classification.

### Class of Function: Invariances

* An invariance is a transformation of the input that we don't want to effect the output.

    * e.g. a cat remains a cat regardless of location (translation), size (scale) or upside-down (rotation and reflection).

    * Convolutional neural networks encode invariances in the mathematical function. 

### Encoding Knowledge

* Encoding invariance is like encoding knowledge in the model.

* If we don't specify these invariances then the model must learn them.

* Learning invariances requires a *lot* more data.

* The amount of data required to achieve a certain performance is the *data efficiency*.

### Choosing Prediction Function

* Prediction function can be any set of parameterized functions.

* In the Olympic marathon example above we used a polynomial fit,

$$
\mappingFunction(x) = \weightScalar_0 + \weightScalar_1 x+ \weightScalar_2 x^2 + \weightScalar_3 x^3 + \weightScalar_4 x^4.
$$

* Olympic example is a supervised learning challenge. But it is a *regression* problem.

* A regression problem is one where the output is a continuous value (such as the pace in the marathon).


### Regression Problems

* In classification the output of prediction function is constrained to be discrete.

* An early example of a regression data set used in machine learning was [the Tecator data](http://lib.stat.cmu.edu/datasets/tecator)

    * Fat, water and protein content of meat samples was predicted as a function of the absorption of infrared light. 



### Parameter Estimation: Objective Functions

* After choosing *features* and *function class* we need *parameters*.

* Estimate $\weightVector$  by specifying an *objective function*.

* The objective function specifies the quality of the match between the prediction function and the *training data*.

* In supervised learning the objective function has input data (for ImageNet, the image, for Olympic marathon the year) and a *label*. 

### Labels and Squared Error

* *Label* is where the term supervised learning comes from.

* Idea is that a supervisor, or annotator, has already given labels.

* For regression problem, a typical objective function is the *squared error*,

$$
\errorFunction(\weightVector) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputVector_i))^2
$$

### Data Provision

* Here the data is provided to us as a set of $n$ inputs, $\inputVector_1$, $\inputVector_2$, $\inputVector_3$, $\dots$, $\inputVector_n$

* Each data point with an associated label, $\dataScalar_1$, $\dataScalar_2$, $\dataScalar_3$, $\dots$, $\dataScalar_n$.

* Sometimes the label is cheap to acquire.

     * E.g. in Newsfeed ranking Facebook are acquiring a label each time a user clicks on a post in their Newsfeed. (Data Science?)

     * In ad-click prediction labels are obtained whenever an advert is clicked.

### Annotation

* Often we have to employ human annotators to label the data.

    * E.g. in ImageNet, the breakthrough deep learning result was annotated using Amazon's Mechanical Turk. (AI?)

* Without large scale human input, would not have the breakthrough results in AI we have today. 


### Annotation

* Some tasks *easier* to annotate than *others.

    * For Tecator data, need to acquire the actual values of water, protein and fat content in the meat samples.

    * Each data point requires real experiments

### Annotation

* Even for *easy* tasks there will be problems.
 
    * E.g. humans extrapolate the context of an image.

* Quality of any machine learning solution is very sensitive to the quality of annotated data we have.

* Investing in processes and tools to improve annotation of data is therefore a strong priority. 

### Misrepresentation

* Can be significant problems with misrepresentation in the data sets.

* If data isn't collected carefully, it can reflect biases about the population that we don't want our models to have.

* A face detector using Californians may not perform well when deployed in Kampala, Uganda. 

### Automation

* Train  supervised learning system, place it in production

* Supervised learning is probably the dominant approaches to learning.

* Cost and time associated with labeling data is a major bottleneck for deploying machine learning systems.

* Creating training data requires significant human effort.

### Training and Test

* Very important distinction.

    * Separation between training data and test data (or production data).

* Training data is the data that was used to find the model parameters.

* Test data (or production data) is the data that is used with the live system.

* Ability of a machine learning system to predict well in production is known as its *generalization* ability.

* System's ability to predict in areas where it hasn't previously seen data.


### Generalization Error

* Easy to develop a prediction function that reconstructs the training data exactly: a look up table. you can just use a look up table.

* How would the lookup table predict *between* the training data, where examples haven't been seen before?

* Choice of the class of prediction functions is critical in ensuring that the model generalizes well. 

* Generalization error is normally estimated by applying the objective function to a set of data that the model *wasn't* trained on: the *test data*.

### Performance

* To ensure good performance we normally want a model that gives us a low generalization error.

* If we weren't sure of the right prediction function to use then we could try 1,000 different prediction functions.

* We could use the one that gives us the lowest error on the test data.

* But you have to be careful.

### Validation and Model Selection

* Selecting a model in this way is like a further stage of training where you are using the test data in the training.[^trainingtest]

* It is known as *validation*.

* The error is known as *validation error*.

*  Using the validation error for model selection is a standard machine learning technique.

### Difficult Trap

* All machine learning practitioners should know not to use the test data in your training procedure.

* But because validation data is used for model selection, it is not an unbiased estimate of the generalization performance.

[^trainingtest]: Using the test data in your training procedure is a major error in any machine learning procedure. It is extremely dangerous as it gives a misleading assessment of the model performance. The [Baidu ImageNet scandal](http://inverseprobability.com/2015/06/04/baidu-on-imagenet) was an example of a team competing in the ImageNet challenge which did this. The team had announced via the publication pre-print server Arxiv that they had a world-leading performance on the ImageNet challenge. This was reported in the mainstream media. Two weeks later the challenge organizers revealed that the team had created multiple accounts for checking their test performance more times than was permitted by the challenge rules. This was then reported as "AI's first doping scandal". The team lead was fired by Baidu. 


### Overfitting

\includeyoutube{py8QrZPT48s}{}{}{4m0s}


*Alex Ihler on Polynomials and Overfitting*
