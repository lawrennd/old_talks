\ifndef{olympicMarathonBayesianPolynomial}
\define{olympicMarathonBayesianPolynomial}

\include{_ml/includes/olympic-marathon-data.md}

\editme

\subsection{Olympic Data with Bayesian Polynomials}

\notes{Five fold cross validation tests the ability of the model to *interpolate*.}

\setupcode{import mlai
import pods}

\plotcode{data_limits = [1892, 2020]
basis = mlai.Basis(mlai.polynomial, number=1, data_limits=data_limits)

max_basis = y.shape[0]}

\plotcode{import teaching_plots as plot}
\plotcode{plot.rmse_fit(x, y, param_name='number', param_range=(1, max_basis+1),
              model=mlai.BLM, 
			  basis=basis, 
			  alpha=1, 
			  sigma2=0.04, 
			  data_limits=data_limits,
              xlim=data_limits, 
			  objective_ylim=[0.5,1.6]
			  diagrams='\diagramsDir/ml')}


\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_BLM_polynomial_number{num_basis:0>3}.svg', 
                            directory='\diagramsDir/ml/', 
							num_basis=IntSlider(1, 1, 27, 1))}


\slides{
\define{width}{80%}
\startanimation{olympic_BLM_polynomial_number}{1}{26}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number001}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number002}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number003}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number004}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number005}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number006}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number007}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number008}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number009}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number010}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number011}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number012}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number013}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number014}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number015}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number016}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number017}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number018}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number019}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number020}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number021}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number022}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number023}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number024}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number025}{\width}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number026}{\width}}{olympic_BLM_polynomial_number}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/olympic_BLM_polynomial_number026}{80%}}{Bayesian fit with 26th degree polynomial and negative marginal log likelihood.}{olympic-blm-polynomial-number-26}}


\subsection{Hold Out Validation}

\notes{For the polynomial fit, we will now look at *hold out* validation, where we are holding out some of the most recent points. This tests the abilit of our model to *extrapolate*.}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.holdout_fit(x, y, param_name='number', param_range=(1, 27),
              diagrams='\diagramsDir/ml',
              model=mlai.BLM, 
              basis=basis, 
              alpha=1, 
              sigma2=0.04,
              xlim=data_limits, 
              objective_ylim=[0.1,0.6], 
              permute=False)}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_val_BLM_polynomial_number{num_basis:0>3}.svg', 
                            directory='\diagramsDir/ml', 
                            num_basis=IntSlider(1, 1, 27, 1))}

\slides{
\startanimation{olympic_val_BLM_polynomial_number}{1}{26}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number001}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number002}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number003}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number004}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number005}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number006}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number007}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number008}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number009}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number010}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number011}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number012}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number013}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number014}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number015}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number016}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number017}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number018}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number019}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number020}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number021}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number022}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number023}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number024}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number025}{\width}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number026}{\width}}{olympic_val_BLM_polynomial_number}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/olympic_val_BLM_polynomial_number026}{80%}}{Bayesian fit with 26th degree polynomial and hold out validation scores.}{olympic-val-blm-polynomial-number-26}}

\subsection{5-fold Cross Validation}

\notes{Five fold cross validation tests the ability of the model to *interpolate*.}

\plotcode{num_parts=5
plot.cv_fit(x, y, param_name='number', param_range=(1, 27),  
            diagrams='\diagramsDir/ml',
            model=mlai.BLM, 
            basis=basis, 
            alpha=1, 
            sigma2=0.04, 
            xlim=data_limits, 
            objective_ylim=[0.2,0.6], 
            num_parts=num_parts)}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_5cv{part:0>2}_BLM_polynomial_number{num_basis:0>3}.svg', 
                            directory='\diagramsDir/ml', 
							part=(0, 5), 
							num_basis=IntSlider(1, 1, 27, 1))}



\slides{
\startanimation{olympic_5cv05_BLM_polynomial_number}{1}{26}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number001}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number002}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number003}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number004}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number005}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number006}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number007}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number008}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number009}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number010}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number011}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number012}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number013}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number014}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number015}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number016}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number017}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number018}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number019}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number020}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number021}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number022}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number023}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number024}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number025}{\width}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number026}{\width}}{olympic_5cv05_BLM_polynomial_number}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/olympic_5cv05_BLM_polynomial_number026}{80%}}{Bayesian fit with 26th degree polynomial and five fold cross validation scores.}{olympic-5cv05-blm-polynomial-number-26}}

\endif
