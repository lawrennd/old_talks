\ifndef{dimensionalityReduction}
\define{dimensionalityReduction}

\editme

\subsection{Dimensionality Reduction}
\slides{
* Compress the data by replacing the original data with reduced number of continuous variables.}
\notes{Dimensionality reduction methods compress the data by replacing the original data with a reduced number of continuous variables. One way of thinking of these methods is to imagine a marionette.}

\figure{\includediagramclass{../slides/diagrams/ml/marionette}{40%}}{Thinking of dimensionality reduction as a marionette. We observe the high dimensional pose of the puppet, $\inputVector$, but the movement of the puppeteer's hand, $\latentVector$ remains hidden to us. Dimensionality reduction aims to recover those hidden movements which generated the observations.}{marionette}

\newslide{Dimensionality Reduction}
\slides{
* Position of each body part of a marionette could be thought of as our data, $\inputVector_i$.
* Each data point is the 3-D co-ordinates of all the different body parts 
* Movement of parts determined by puppeteer via strings.
* For a simple puppet with one stick can move the stick up and down, left and right and twist.}
\notes{The position of each body part of a marionette could be thought of as our data, $\inputVector_i$. So, each data point consists of the 3-D co-ordinates of all the different body parts of the marionette. Let's say there are 13 different body parts (2 each of feet, knees, hips, hands, elbows, shoulders, one head). Each body part has an x, y, z position in Cartesian coordinates. So that's 39 numbers associated with each observation.} 


\newslide{Dimensionality Reduction}
\slides{
* This gives three parameters in the puppeteers control.
* Implies that the puppet we see moving is controlled by only 3 variables.
* These 3 variables are often called the hidden or *latent variables*. 
* Assume similar for real world data, observations are derived from lower dimensional underlying process}
\notes{The movement of these 39 parts is determined by the puppeteer via strings. Let's assume it's a very simple puppet, with just one stick to control it. The puppeteer can move the stick up and down, left and right. And they can twist it. This gives three parameters in the puppeteers control. This implies that the 39 variables we see moving are controlled by only 3 variables. These 3 variables are often called the hidden or *latent variables*. 

Dimensionality reduction assumes something similar for real world data. It assumes that the data we observe is generated from some lower dimensional underlying process. It then seeks to recover the values associated with this low dimensional process.} 

\subsubsection{Examples in Social Sciences}
\slides{
* Underpins *psychological scoring* such as *IQ* or *personality tests*
* Myers-Briggs assumes personality is four dimensional.
* Political belief (left/right wing).
* Also language modelling has taken similar approaches: [word2vec](https://arxiv.org/abs/1301.3781)}
\notes{Dimensionality reduction techniques underpin a lot of psychological scoring tests such as IQ tests or personality tests. An IQ test can involve several hundred questions, potentially giving a rich, high dimensional, characterization of some aspects of your intelligence. It is then summarized by a single number. Similarly, the Myers-Briggs personality test involves answering questions about preferences which are reduced to a set of numbers reflecting personality.

These tests are assuming that our intelligence is implicitly one-dimensional and that our personality is implicitly four dimensional. Other examples include political belief which is typically represented on a left to right scale. A one-dimensional distillation of an entire philosophy about how a country should be run. Our own leadership principles imply that our decisions have a fourteen-dimensional space underlying them. Each decision could be characterized by judging to what extent it embodies each of the principles. 

Political belief, personality, intelligence, leadership. None of these exist as a directly measurable quantity in the real world, rather they are inferred based on measurables. Dimensionality reduction is the process of allowing the computer to automatically find such underlying dimensions. This automatically allowing us to characterize each data point according to those explanatory variables. Each of these characteristics can be scored, and individuals can then be turned into vectors. 

This doesn't only apply to individuals, in recent years work on language modeling has taken a similar approach to words. The [word2vec](https://arxiv.org/abs/1301.3781) algorithm performed a dimensionality reduction on words, now you can take any word and map it to a latent space where similar words exhibit similar characteristics. A personality space for words.}

\subsubsection{Principal Component Analysis}
\slides{
* Principal component analysis (PCA) a linear dimensionality reduction technique
* In Hotelling's formulation of PCA: a assume $\inputVector$ is a linear weighted sum of the latent factors of interest.
* E.g. IQ test we would try and predict subject $i$'s answer to the $j$th question with the following function
$$
\dataScalar_{ij} = \mappingFunction_j(\latentScalar_i; \weightVector).
$$
$\latentScalar_i$ would be the IQ of subject $i$ and $\mappingFunction_j(\cdot)$ would function relating IQ and question answer.}
\notes{Principal component analysis (PCA) is arguably the queen of dimensionality reduction techniques. PCA was developed as an approach to dimensionality reduction in 1930s by Hotelling as a method for the social sciences. In Hotelling's formulation of PCA it was assumed that any data point, $\mathbf{x}$ could be represented as a weighted sum of the latent factors of interest, so that Hotelling described prediction functions (like in regression and classification above), only the regression is now *multiple output*.  And instead of predicting a label, $y_i$, we now try and force the regression to predict the observed feature vector, $\dataVector_i$. So, for example, on an IQ test we would try and predict subject $i$'s answer to the $j$th question with the following function
$$
\dataScalar_{ij} = \mappingFunction_j(\latentScalar_i; \weightVector).
$$
Here $z_i$ would be the IQ of subject $i$ and $\mappingFunction_j(\cdot)$ would be a function representing the relationship between the subject's IQ and their score on the answer to question $j$. This function is the same for all subjects, but the subject's IQ is assumed to differ leading to different scores for each subject.}

\newslide{Principal Component Analysis}

\figure{\includediagram{../slides/diagrams/ml/demManifoldPrint_all_1_2}{60%}}{Visualization of the first two principal components of an artificial data set. The data was generated by taking an image of a handwritten digit, 6, and rotating it 360 times, one degree each time. The first two principal components have been extracted in the diagram. The underlying circular shape is derived from the rotation of the data. Each image in the data set is projected on to the location its projected to in the latent space.}{dem-manifold-print-all-1-2}

\subsubsection{Hotelling's PCA}
\slides{
* Assume function is linear function. This idea is taken from a wider field known as *factor analysis*, so Hotelling described the challenge as
$$
\mappingFunction_j(\latentScalar_i; \weightVector) = \weightScalar_j \latentScalar_i
$$
* Answer to the $j$th question is predicted to be a scaling of the subject's IQ.
* Scale factor is given by $\weightScalar_j$.}
\notes{In Hotelling's formulation he assumed that the function was a linear function. This idea is taken from a wider field known as *factor analysis*, so Hotelling described the challenge as
$$
\mappingFunction_j(\latentScalar_i; \weightVector) = \weightScalar_j \latentScalar_i
$$
so the answer to the $j$th question is predicted to be a scaling of the subject's IQ. The scale factor is given by $\weightScalar_j$. If there are more latent dimensions then a matrix of parameters, $\weightMatrix$ is used, for example if there were two latent dimensions, we'd have
$$
\mappingFunction_j(\mathbf{\latentScalar}_i; \weightMatrix) = \weightScalar_{1j} \latentScalar_{1i} + \weightScalar_{2j} \latentScalar_{2i}
$$
where, if this were a personality test, then $\latentScalar_{1i}$ might represent the spectrum over a subject's extrovert/introvert and $\latentScalar_{2i}$ might represent where the subject was on the rational/perceptual scale. The function would make a prediction about the subjects answer to a particular question on the test (e.g. preference for office job vs preference for outdoor job). In factor analysis the parameters $\weightMatrix$ are known as the factor *loadings* and in PCA they are known as the principal components.}

\newslide{Higher Latent Dimensions}
\slides{
* For more latent dimensions matrix of scales, $\weightVector$
$$
\mappingFunction_j(\latentVector_i; \weightVector) = \weightScalar_{1j} \latentScalar_{1i} + \weightScalar_{2j} \latentScalar_{2i}
$$
*  $\latentScalar_{1i}$ might be extrovert/introvert and $\latentScalar_{2i}$ might rational/perceptual}


\subsubsection{Parameters}
\slides{
* Parameters $\weightVector$ are known as the factor *loadings* in FA.
* In PCA they are known as the principal components.
* To fit the model need *loadings*, $\weightVector$, and latent variables, $\latentMatrix$.
* Can use least squares (leads to *matrix factorization* and recommender systems).
* Recommender systems most elements of $\inputVector_i$ are missing.}
\notes{Fitting the model involves finding estimates for the loadings, $\weightMatrix$, and latent variables, $\latentMatrix$. There are different approaches including least squares. The least squares approach is used, for example, in recommender systems. In recommender systems this method is called *matrix factorization*. The customer characteristics, $\dataVector_i$ is the customer rating for each different product (or item) and the latent variables can be seen as a space of customer preferences. In the recommender system case, the loadings matrix also has an interpretation as product similarities.[^recommender] Recommender systems have a particular characteristic in that most of the entries of the vector $\dataVector_i$ are missing most of the time. 

[^recommender]: One way of thinking about this is to flip the model on its side. Instead of thinking about the $i$th subject and the $j$th characteristic. Assume that each product is the subject. So, the $j$th item is thought of as the subject, and each item's characteristic is given by the rating from a particular user. In this case symmetries in the model show that the matrix $\weightMatrix$ can now be seen as a matrix of *latent variables* and the matrix $\latentMatrix$ can be seen as *factor loadings*. So, you can think of the method as simultaneously doing a dimensionality reduction on the products and the users.  Recommender systems also use other approaches, some of them based on similarity measures. In a similarity measure-based recommender system the rating prediction is given by looking for similar products in the user profile and scoring the new product with a score that is a weighted sum  of those products.} 

\newslide{Probability}
\slides{
* PCA and factor analysis the unknown latent factors are dealt with through a probability distribution.
* Assume these "unknowns" are  drawn from a zero mean, unit variance normal distribution.
* That implies a particular *probability* density for data (PDF).
* The PDF has parameters depending on factor loadings to be estimated.}
\notes{In PCA and factor analysis the unknown latent factors are dealt with through a probability distribution. They are each assumed to be drawn from a zero mean, unit variance normal distribution. This leaves the factor loadings to be estimated. For PCA the maximum likelihood solution for the factor loadings can be shown to be given by the *eigenvalue decomposition* of the data covariance matrix. This is algorithmically simple and convenient, although slow to compute for very large data sets with many features and many subjects. The eigenvalue problem can also be derived from many other starting points: e.g. the directions of maximum variance in the data or finding a latent space that best preserves inter-point distances between the data, or the optimal linear compression of the data given a linear reconstruction. These many and varied justifications for the eigenvalue decomposition may account for the popularity of PCA. Indeed, there is even an interpretation for Google's original PageRank algorithm (which computed the *smallest* eigenvector of the internet's linkage matrix) as seeking the dominant principal component of the web.[^pagerankinterpretation]

[^pagerankinterpretation]: The interpretation requires you to think of the web as a series of web pages in a high dimensional space where distances between web pages are computed by moving along the links (in either direction). The PageRank is the one-dimensional space that best preserves those distances in the sense of an L1 norm. The interpretation works because the smallest eigenvalue of the linkage matrix is the *largest* eigenvalue of the inverse of the linkage matrix. The inverse linkage matrix (which would be impossible to compute) embeds similarities between pages according to how far apart they are via a random walk along the linkage matrix.}


\newslide{Maximum Likelihood}
\slides{
* Fit model by "maximising likelihood of data" under the PDF.
* Maxium likelihood for PCA is the *eigenvalue decomposition* of the data covariance matrix.
* Algorithmically simple and convenient, but slow to compute for very large data sets with many features and many subjects.}
\notes{Characterizing users according to past buying behavior and combining this with characteristics about products, is key to making good recommendations and returning useful search results. Further advances can be made if we understand the context of a particular session. For example, if a user is buying Christmas presents and searches for a dress, then it could be the case that the user is willing to spend a little more on the dress than in normal circumstances. Characterizing these effects requires more data and more complex algorithms. However, in domains such a search we are normally constrained by the speed with which we need to return results. Accounting for each of these factors while returning results with acceptable latency is a particular challenge.} 



\endif
