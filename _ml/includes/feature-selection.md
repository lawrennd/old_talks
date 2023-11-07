\ifndef{featureSelection}
\define{featureSelection}

\editme

\subsection{Feature Selection}
\slides{
* Olympic prediction example only using year to predict pace.
* What else could we use?
* Can use *feature selection algorithms*
}

\notes{Feature selection is a critical stage in the algorithm design process. In the Olympic prediction example above we're only using time to predict the the pace of the runners. In practice we might also want to use characteristics of the course: how hilly it is, what the temperature was when the race was run. In 1904 the runners actually got lost during the race. Should we include 'lost' as a feature? It would certainly help explain the particularly slow time in 1904. The features we select should be ones we expect to correlate with the prediction. In statistics, these features are even called *predictors* which highlights their role in developing the prediction function. For Facebook newsfeed, we might use features that include how close your friendship is with the poster, or how often you react to that poster, or whether a photo is included in the post.

Sometimes we use feature selection algorithms, algorithms that automate the process of finding the features that we need. Classification is often used to rank search results, to decide which adverts to serve or, at Facebook, to determine what appears at the top of your newsfeed. In the Facebook example features might include how many likes a post has had, whether it has an image in it, whether you regularly interact with the friend who has posted. A good newsfeed ranking algorithm is critical to Facebook's success, just as good ad serving choice is critical to Google's success. These algorithms are in turn highly dependent on the feature sets used. Facebook in particular has made heavy investments in machine learning pipelines for evaluation of the feature utility.}

\newslide{Applications}
\slides{
*  rank search results, what adverts to show, newsfeed ranking
* Features:  number of likes, image present, friendship relationship
} 

\endif
