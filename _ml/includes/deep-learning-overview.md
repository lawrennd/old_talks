\ifndef{deepLearningOverview}
\define{deepLearningOverview}
\editme

\section{Deep Learning}

\ifdef{whatDoesMachineLearningDo}

\newslide{Deep Learning}
\slides{
* These are interpretable models: vital for disease modeling etc.

* Modern machine learning methods are less interpretable

* Example: face recognition
}

\notes{Classical statistical models and simple machine learning models have a great deal in common. The main difference between the fields is philosophical. Machine learning practitioners are typically more concerned with the quality of prediciton (e.g. measured by ROC curve) while statisticians tend to focus more on the interpretability of the model and the validity of any decisions drawn from that interpretation. For example, a statistical model may be used to validate whether a large scale intervention (such as the mass provision of mosquito nets) has had a long term effect on disease (such as malaria). In this case one of the covariates is likely to be the provision level of nets in a particular region. The response variable would be the rate of malaria disease in the region. The parmaeter, $\beta_1$ associated with that covariate will demonstrate a positive or negative effect which would be validated in answering the question. The focus in statistics would be less on the accuracy of the response variable and more on the validity of the interpretation of the effect variable, $\beta_1$. 

A machine learning practitioner on the other hand would typically denote the parameter $w_1$, instead of $\beta_1$ and would only be interested in the output of the prediction function, $\mappingFunction(\cdot)$ rather than the parameter itself. The general formalism of the prediction function allows for *non-linear* models. In machine learning, the emphasis on prediction over interpretability means that non-linear models are often used. The parameters, $\mathbf{w}$, are a means to an end (good prediction) rather than an end in themselves (interpretable).}
\endif

<!-- No slide titles in this context -->
\ifndef{noSlideTitle}
\define{noSlideTitle}
\define{unDefineMe}
\endif

talk-macros.gpp}l/includes/deep-face.md}
talk-macros.gpp}l/includes/deep-learning-as-pinball.md}

\ifdef{unDefineMe}
\undef{unDefineMe}
\undef{noSlideTitle}
\endif

\endif
