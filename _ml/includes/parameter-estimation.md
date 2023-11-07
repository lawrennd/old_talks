\ifndef{parameterEstimation}
\define{parameterEstimation}

\editme

\subsection{Parameter Estimation: Objective Functions}
\slides{
* After choosing *features* and *function class* we need *parameters*.
* Estimate $\weightVector$  by specifying an *objective function*.}

\notes{Once we have a set of features, and the class of functions we use is determined, we need to find the parameters of the model. 

The parameters of the model, $\weightVector$, are estimated by specifying an *objective function*. The objective function specifies the quality of the match between the prediction function and the *training data*. In supervised learning the objective function incorporates both the input data (in the ImageNet data the image, in the Olympic marathon data the year of the marathon) and a *label*. 

The label is where the term supervised learning comes from. The idea being that a supervisor, or annotator, has already looked at the data and given it labels. For regression problem, a typical objective function is the *squared error*,
$$
\errorFunction(\weightVector) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputVector_i))^2
$$
where the data is provided to us as a set of $n$ inputs, $\inputVector_1$, $\inputVector_2$, $\inputVector_3$, $\dots$, $\inputVector_n$ each one with an associated label, $\dataScalar_1$, $\dataScalar_2$, $\dataScalar_3$, $\dots$, $\dataScalar_\numData$. Sometimes the label is cheap to acquire. For example, in Newsfeed ranking Facebook are acquiring a label each time a user clicks on a post in their Newsfeed. Similarly, in ad-click prediction labels are obtained whenever an advert is clicked. More generally though, we have to employ human annotators to label the data. For example, ImageNet, the breakthrough deep learning result was annotated using Amazon's Mechanical Turk. Without such large scale human input, we would not have the breakthrough results on image categorization we have today. 

Some tasks are easier to annotate than others. For example, in the Tecator data, to acquire the actual values of water, protein and fat content in the meat samples further experiments may be required. It is not simply a matter of human labelling. Even if the task is easy for humans to solve there can be problems. For example, humans will extrapolate the context of an image. A colleague mentioned once to me a challenge where humans were labelling images as containing swimming pools, even though none was visible, because they could infer there must be a pool nearby, perhaps because there are kids wearing bathing suits. But there is no swimming pool in the image for the computer to find. The quality of any machine learning solution is very sensitive to the quality of annotated data we have. Investing in processes and tools to improve annotation of data is therefore priority for improving the quality of machine learning solutions. 

There can also be significant problems with misrepresentation in the data set. If data isn't collected carefully, then it can reflect biases about the population that we don't want our models to have. For example, if we design a face detector using Californians may not perform well when deployed in Kampala, Uganda.}

\newslide{Labels and Squared Error}
\slides{
* *Label* comes from supervisor or annotator.
* For regression *squared error*,
$$
\errorFunction(\weightVector) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputVector_i))^2
$$}

\newslide{Data Provision}
\slides{
* Given $\numData$ inputs, $\inputVector_1$, $\inputVector_2$, $\inputVector_3$, $\dots$, $\inputVector_\numData$
* And labels $\dataScalar_1$, $\dataScalar_2$, $\dataScalar_3$, $\dots$, $\dataScalar_\numData$.
* Sometimes label is cheap e.g. Newsfeed ranking
* Often it is very expensive. 
    * Manual labour
}

\newslide{Annotation}
\slides{
* Human annotators
    * E.g. in ImageNet annotated using Amazon's Mechanical Turk. (AI?)
* Without humans no AI.
* Not real intelligence, emulated}


\newslide{Annotation}
\slides{
* Some tasks *easier* to annotate than *others*.
    * Sometimes annotation requires an experiment (Tecator data)
}

\newslide{Annotation}
\slides{
* Even for *easy* tasks there will be problems.
    * E.g. humans extrapolate the context of an image.

* Quality of ML is very sensitive to data.
* Investing in processes and tools is vital.}

\newslide{Misrepresentation and Bias}
\slides{
* Bias can appear in the *model* and the *data*
* Data needs to be carefully collected
* E.g. face detectors trained on Europeans tested in Africa.}

\endif
