\ifndef{generalizationAndOverfitting}
\define{generalizationAndOverfitting}
\editme

\subsection{Generalization and Overfitting}
\slides{
* How does the model perform on previously unseen data?}
\notes{Once a supervised learning system is trained it can be placed in a sequential pipeline to automate a process that used to be done manually. 

Supervised learning is one of the dominant approaches to learning. But the cost and time associated with labeling data is a major bottleneck for deploying machine learning systems. The process for creating training data requires significant human intervention. For example, internationalization of a speech recognition system would require large speech corpora in new languages. 

An important distinction in machine learning is the separation between training data and test data (or production data). Training data is the data that was used to find the model parameters. Test data (or production data) is the data that is used with the live system. The ability of a machine learning system to predict well on production systems given only its training data is known as its *generalization* ability. This is the system's ability to predict in areas where it hasn't previously seen data.}



\newslide{Validation and Model Selection}
\slides{
* Selecting model at the *validation* step}

\newslide{Difficult Trap}
\slides{
* Vital that you avoid test data in training.
* Validation data is different from test data. }

\include{_ml/includes/olympic-marathon-hold-out-validation.md}

\include{_ml/includes/bias-variance-dilemma.md}

\subsection{Overfitting}

\figure{\includeyoutube{py8QrZPT48s}{600}{450}{4m0s}}{Alex Ihler discusses polynomials and overfitting.}{alex-ihler-overfitting}

\slides{*Alex Ihler on Polynomials and Overfitting*}

\notes{We can easily develop a simple prediction function that reconstructs the training data exactly, you can just use a look up table. But how would the lookup table predict between the training data, where examples haven't been seen before? The choice of the class of prediction functions is critical in ensuring that the model generalizes well. 

The generalization error is normally estimated by applying the objective function to a set of data that the model *wasn't* trained on, the test data. To ensure good performance we normally want a model that gives us a low generalization error. If we weren't sure of the right prediction function to use, then we could try 1,000 different prediction functions. Then we could use the one that gives us the lowest error on the test data. But you have to be careful. Selecting a model in this way is like a further stage of training where you are using the test data in the training.[^trainingtest] So when this is done, the data used for this is not known as test data, it is known as *validation data*. And the associated error is the *validation error*. Using the validation error for model selection is a standard machine learning technique, but it can be misleading about the final generalization error. Almost all machine learning practitioners know not to use the test data in your training procedure, but sometimes people forget that when validation data is used for model selection that validation error cannot be used as an unbiased estimate of the generalization performance.

[^trainingtest]: Using the test data in your training procedure is a major error in any machine learning procedure. It is extremely dangerous as it gives a misleading assessment of the model performance. The [Baidu ImageNet scandal](http://inverseprobability.com/2015/06/04/baidu-on-imagenet) was an example of a team competing in the ImageNet challenge which did this. The team had announced via the publication pre-print server Arxiv that they had a world-leading performance on the ImageNet challenge. This was reported in the mainstream media. Two weeks later the challenge organizers revealed that the team had created multiple accounts for checking their test performance more times than was permitted by the challenge rules. This was then reported as "AI's first doping scandal". The team lead was fired by Baidu.}

\endif
