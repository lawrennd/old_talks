\ifndef{olympicMarathonKFoldValidation}
\define{olympicMarathonKFoldValidation}

\include{_datasets/includes/olympic-marathon-data.md}

\editme

\subsection{$k$-fold Cross Validation}

\slides{* Leave one out error can be very time consuming.
* Need to train your algorithm $\numData$ times.
* An alternative: $k$ fold cross validation.}

\setupplotcode{import mlai
import pods}

\plotcode{data_limits=xlim
basis = mlai.Basis(mlai.polynomial, number=1, data_limits=data_limits)
max_basis = 11}

\newslide{$k$-fold Cross Validation}

\setupplotcode{import teaching_plots as plot}
\plotcode{num_parts=5 # set k
plot.cv_fit(x, y, param_name='number', 
            param_range=(1, max_basis+1),
            model=mlai.LM, 
            basis=basis, 
            xlim=data_limits, 
            objective_ylim=[0.2,0.6], 
            num_parts=num_parts,
            diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('olympic_{num_parts}'.format(num_parts=num_parts) + 'cv{part:0>2}_LM_polynomial_number{number:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
                            part=IntSlider(0,0,5,1),
                            number=IntSlider(1, 1, max_basis, 1))}

\slides{
\startanimation{olympic_5cv_LM_polynomial}{0}{1}{fold}
\newframe{
  \startanimation{olympic_5cv00_LM_polynomial}{1}{11}{num basis}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number001}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number002}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number003}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number004}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number005}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number006}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number007}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv00_LM_polynomial_number008}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number009}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number010}}{olympic_5cv00_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number011}}{olympic_5cv00_LM_polynomial}
  \endanimation
}{olympic_5cv_LM_polynomial}
\newframe{
  \startanimation{olympic_5cv01_LM_polynomial}{1}{11}{num basis}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number001}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number002}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number003}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number004}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number005}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number006}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number007}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number008}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number009}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number010}}{olympic_5cv01_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv01_LM_polynomial_number011}}{olympic_5cv01_LM_polynomial}
  \endanimation
}{olympic_5cv_LM_polynomial}
\newframe{
  \startanimation{olympic_5cv02_LM_polynomial}{1}{11}{num basis}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number001}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number002}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number003}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number004}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number005}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number006}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number007}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number008}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number009}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number010}}{olympic_5cv02_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv02_LM_polynomial_number011}}{olympic_5cv02_LM_polynomial}
  \endanimation
}{olympic_5cv_LM_polynomial}
\newframe{
  \startanimation{olympic_5cv03_LM_polynomial}{1}{11}{num basis}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number001}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number002}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number003}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number004}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number005}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number006}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number007}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number008}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number009}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number010}}{olympic_5cv03_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv03_LM_polynomial_number011}}{olympic_5cv03_LM_polynomial}
  \endanimation
}{olympic_5cv_LM_polynomial}
\newframe{
  \startanimation{olympic_5cv04_LM_polynomial}{1}{11}{num basis}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number001}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number002}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number003}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number004}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number005}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number006}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number007}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number008}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number009}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number010}}{olympic_5cv04_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv04_LM_polynomial_number011}}{olympic_5cv04_LM_polynomial}
  \endanimation
}{olympic_5cv_LM_polynomial}
\newframe{
  \startanimation{olympic_5cv05_LM_polynomial}{1}{11}{num basis}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number001}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number002}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number003}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number004}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number005}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number006}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number007}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number008}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number009}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number010}}{olympic_5cv05_LM_polynomial}
  \newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_LM_polynomial_number011}}{olympic_5cv05_LM_polynomial}
  \endanimation
}{olympic_5cv_LM_polynomial}
\endanimation
}

\notes{Leave one out cross validation produces a very good estimate of the performance at test time, and is particularly useful if you don't have a lot of data. In these cases you need to make as much use of your data for model fitting as possible, and having a large hold out data set (to validate model performance) can have a significant effect on the size of the data set you have to fit your model, and correspondingly, the complexity of the model you can fit. However, leave one out cross validation involves fitting $\numData$ models, where $\numData$ is your number of training data. For the olympics example, this is only 27 model fits, but in practice many data sets consist thousands or millions of data points, and fitting many millions of models for estimating validation error isn't really practical. One option is to return to *hold out* validation, but another approach is to perform $k$-fold cross validation. In $k$-fold cross validation you split your data into $k$ parts. Then you use $k-1$ of those parts for training, and hold out one part for validation. Just like we did for the hold out validation above. In *cross* validation, however, you repeat this process. You swap the part of the data you just used for validation back in to the training set and select another part for validation. You then fit the model to the new training data and validate on the portion of data you've just extracted. Each split of training/validation data is called a *fold* and since you do this process $k$ times, the procedure is known as $k$-fold cross validation. The term *cross* refers to the fact that you cross over your validation portion back into the training data every time you perform a fold.}

\codeassignment{Perform $k$-fold cross validation on the olympic data
with your polynomial basis. Use $k$ set to 5 (e.g. five fold cross validation).
Do the different forms of validation select different models? Does five fold
cross validation always select the same model?

*Note*: The data doesn't divide into 5 equal size partitions for the five fold
cross validation error. Don't worry about this too much. Two of the partitions
will have an extra data point. You might find `np.random.permutation?` useful.
}{}{20}

\endif
