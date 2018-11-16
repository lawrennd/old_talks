### Leave One Out Validation

\newslide{Leave One Out Error}

\slides{
* Take training set and remove one point.
* Train on the remaining data.
* Compute the error on the point you removed (which wasn't in the training data).
* Do this for each point in the training set in turn.
* Average the resulting error. 
* This is the leave one out error.}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.loo_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1),  
             model=mlai.LM, basis=basis, data_limits=data_limits, 
             xlim=data_limits, objective_ylim=[0, 0.8], prefix='olympic_loo',
			  diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('olympic_loo{part:0>3}_LM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							num_basis=IntSlider(1, 1, max_basis, 1), 
							part=IntSlider(0, 0, x.shape[0], 1))}

\slides{
\startanimation{olympic_loo000_LM_polynomial_num_basis}{1}{26}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis001.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis002.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis003.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis004.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis005.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis006.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis007.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis008.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis009.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis010.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis011.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis012.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis013.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis014.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis015.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis016.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis017.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis018.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis019.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis020.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis021.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis022.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis023.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis024.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis025.svg}}{olympic_loo000_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_loo000_LM_polynomial_num_basis026.svg}}{olympic_loo000_LM_polynomial_num_basis}
\endanimation
}


\notes{Hold out validation uses a portion of the data to hold out and a portion of the data to train on. There is always a compromise between how much data to hold out and how much data to train on. The more data you hold out, the better the estimate of your performance at 'run-time' (when the model is used to make predictions in real applications). However, by holding out more data, you leave less data to train on, so you have a better validation, but a poorer quality model fit than you could have had if you'd used all the data for training. Leave one out cross validation leaves as much data in the training phase as possible: you only take *one point* out for your validation set. However, if you do this for hold-out validation, then the quality of your validation error is very poor because you are testing the model quality on one point only. In *cross validation* the approach is to improve this estimate by doing more than one model fit. In *leave one out cross validation* you fit $\numData$ different models, where $\numData$ is the number of your data. For each model fit you take out one data point, and train the model on the remaining $n-1$ data points. You validate the model on the data point you've held out, but you do this $\numData$ times, once for each different model. You then take the *average* of all the $\numData$ badly estimated hold out validation errors. The average of this estimate is a good estimate of performance of those models on the test data.}

\codeassignment{Write code that computes the *leave one out* validation error for the olympic data and the polynomial basis. Use the functions you have created above: `objective`, `fit`, `polynomial`. Compute the *leave-one-out* cross validation error for basis functions containing a maximum degree from 0 to 17.}{5}{20}
