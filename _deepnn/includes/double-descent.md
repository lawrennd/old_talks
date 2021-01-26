\ifndef{doubleDescent}
\define{doubleDescent}

\editme

\subsection{Double Descent}

  
\figure{\includepng{\diagramsDir/ml/double-descent}{100%}}{*Left* traditional perspective on generalisation. There is a sweet spot of operation where the training error is still non-zero. Overfitting occurs when the variance increases. *Right* The double descent phenomenon, the modern models operate in an interpolation regime where they reconstruct the training data fully, but are well regularised in their interpolations for test data. Figure from @Belkin:reconciling19.}{double-descent}



\notes{But the modern empirical finding is that when we move beyond Daddy bear,
into the dark forest of the massively overparameterized model we can
achieve good generalization. Indeed, recent work is showing that large language models are even *memorising* data [@Carlini-extracting20] like non-parametric models do.}

\notes{As @Zhang:understanding17 starkly illustrated with
their random labels experiment, within the dark forest there are some
terrible places, big bad wolves of overfitting that will gobble up
your model. But as empirical evidence shows there is also a safe and
hospitable Grandma's house where these highly overparameterized models
are safely consumed. Fundamentally, it must be about the route you
take through the forest, and the precautions you take to ensure the
wolf doesn't see where you're going and beat you to the door.}

\notes{There are two implications of this empirical result. Firstly,
that there is a great deal of new theory that needs to be
developed. Secondly, that theory is now obliged to conflate two
aspects to modelling that we generally like to keep separate: the
model and the algorithm.}

\notes{Classical statistical theory around predictive generalization
focusses specifically on the class of models that is being used for
data fitting. Historically, whether that theory follows a
Fisher-aligned estimation approach (see e.g. @Vapnik:book98) or
model-based Bayesian approach (see e.g. @Ghahramani:probabilistic15),
neither is fully equipped to deal with these new circumstances
because, to continue our rather tortured analogy, these theories
provide us with a characterization of the *destination* of the
algorithm, and seek to ensure that we reach that destination. Modern
machine learning requires theories of the *journey* and what our route
through the forest should be. }

\notes{Crucially, the destination is always associated with 100%
accuracy on the training set. An objective that is always achievable
for the overparameterized model.}

\notes{Intuitively, it seems that a highly overparameterized model
places Grandma's house on the edge of the dark forest. Making it
easily and quickly accessible to the algorithm. The larger the model,
the more exposed Grandma's house becomes. Perhaps this is due to some
form of blessing of dimensionality brings Grandma's house closer to
the edge of the forest in a high dimensional setting. Really, we
should think of Grandma's house as a low dimensional manifold of
destinations that are safe. A path through the forest where the wolf
of overfitting doesn't venture. In the GLM case, we know already that
when the number of parameters matches the number of data there is
precisely one location in parameter space where accuracy on the
training data is 100%. Our previous misunderstanding of generalization
stemmed from the fact that (seemingly) it is highly unlikely that this
single point is a good place to be from the perspective of
generalization. Additionally, it is often difficult to find. Finding
the precise polynomial coefficients in a least squares regression to
exactly fit the basis to a small data set such as the Olympic marathon
data requires careful consideration of the numerical properties and an
orthogonalization of the design matrix [@Lawson:least95].}

\notes{It seems that with a highly overparameterized model, these
locations become easier to find and they provide good generalization
properties. In machine learning this is known as the "double descent
phenomenon" (see e.g. @Belkin:reconciling19).}

\notes{See also this talk by Misha Belkin:  <http://www.ipam.ucla.edu/abstract/?tid=15552&pcode=GLWS4> and these related papers <https://www.pnas.org/content/116/32/15849.short>, <https://www.pnas.org/content/117/20/10625>}


\endif
