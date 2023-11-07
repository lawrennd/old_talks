\ifndef{deepModelsAndGeneralization}
\define{deepModelsAndGeneralization}

\editme

\subsection{Deep Models and Generalization}

\notes{The new wave of predictive modelling techniques owes a great deal to the tradition of regression. But their success in generalizing to out-of-sample examples owes little to our traditional understanding of the theory of generalization. These models are highly overparameterized. As such, the traditional view would be that they should 'overfit' the data. But in reality, these very large models generalize well. Is it because they can't overfit?}

\notes{When it comes to the mismatch between our expectations about generalization and the reality of deep models, perhaps the paper that most clearly
demonstrated something was amiss was [@Zhang:understanding17], who
trained a large neural network via stochastic gradient descent to
label an image data set. Within Professor Efron's categorization of
regression model, such a model is a very complex regression model with
a particular link function and highly structured adaptive basis
functions, which are by tradition called neurons. Despite the
structuring of these basis functions (known as convolutional layers),
their adaptive nature means that the model contains many millions of
parameters. Traditional approaches to generalization suggest that the
model should over fit and [@Zhang:understanding17] proved that such
models can do just that. The data they used to fit the model, the
training set, was modified. They flipped labels randomly, removing any
information in the data. After training, the resulting model was able
to classify the training data with 100% accuracy. The experiment
clearly demonstrates that all our gravest doubts about
overparameterized models are true. If this model has the capacity to
fit data which is obviously nonsense, then it is clearly not
regularized. Our classical theories suggest that such models should
not generalize well on previously unseen data, or test data, but yet
the empirical experience is that they do generalize well. So, what's
going on?}

\notes{During a period of deploying machine learning models at Amazon,
I was introduced to a set of leadership principles, fourteen
different ideas to help individual Amazonians structure their
thinking. One of them was called "Dive Deep", and a key trigger for a
"Dive Deep" was when anecdote and data are in conflict. If there were
to be a set of Academic leadership principles, then clearly "Dive
Deep" should be triggered when empirical evidence and theory are in
conflict. The purpose of the principle within Amazon was to ensure
people don't depend overly on anecdotes *or* data when making their
decisions, but to develop deeper understandings of their business. In
academia, we are equally guilty of relying too much on empirical
studies or theory without ensuring they are reconciled. The
theoreticians' disbelief of what the experimenter tells them is
encapsulated in Kahnemann's idea of "theory induced blindness"
[@Kahneman:fastslow11]. Fortunately, the evidence for good
generalization in these mammoth models is now large enough that the
theory-blinders are falling away, and a serious look is being taken and
how and why these models can generalize well.}

\notes{An in-depth technical understanding that applies to all these
cases is not yet available. But some key ideas are. Firstly, if the
neural network model is over-capacity, and can fit nonsense data in
the manner demonstrated by [@Zhang:understanding17] then that
immediately implies that the good generalization is arising from how
the model is fitted to the data. When the number of parameters is so
large, the parameters are very badly determined. In machine learning,
the concept of version space [@Mitchell:version77] is the subset of
all the hypotheses that are consistent with the training examples. For
a neural network, the version space is where the neural network
parameters (or weights) give predictions for the training data 100%
accuracy. A traditional statistical perspective would eschew this
regime, convinced that the implication is that overfitting must have
occurred. But the empirical evidence from the deep learning community
is that these regimes produce classification algorithms with excellent
generalization properties. The resolution to this dilemma is *where*
in the version space the algorithm comes to rest. }

\endif
