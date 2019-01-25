\ifndef{olympicBayesianPolynomials}
\define{olympicBayesianPolynomials}
\editme

\subsection{Olympic Data with Bayesian Polynomials}

\notes{Five fold cross validation tests the ability of the model to *interpolate*.}

\setupcode{import mlai
import pods}

\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']
num_data = x.shape[0]

data_limits = [1892, 2020]
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
			  diagrams='../slides/diagrams/ml')}


\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_BLM_polynomial_number{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml/', 
							num_basis=IntSlider(1, 1, 27, 1))}


\slides{
\startanimation{olympic_BLM_polynomial_number}{1}{26}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number001}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number002}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number003}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number004}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number005}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number006}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number007}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number008}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number009}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number010}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number011}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number012}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number013}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number014}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number015}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number016}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number017}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number018}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number019}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number020}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number021}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number022}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number023}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number024}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number025}}{olympic_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number026}}{olympic_BLM_polynomial_number}
\endanimation
}

\notesfigure{\includediagram{../slides/diagrams/ml/olympic_BLM_polynomial_number026}}{}}
\notes{\caption{Bayesian fit with 26th degree polynomial and negative marginal log likelihood.}}


\subsection{Hold Out Validation}

\notes{For the polynomial fit, we will now look at *hold out* validation, where we are holding out some of the most recent points. This tests the abilit of our model to *extrapolate*.}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.holdout_fit(x, y, param_name='number', param_range=(1, 27),
              diagrams='../slides/diagrams/ml',
              model=mlai.BLM, 
              basis=basis, 
              alpha=1, 
              sigma2=0.04,
              xlim=data_limits, 
              objective_ylim=[0.1,0.6], 
              permute=False)}

\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_val_BLM_polynomial_number{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
                            num_basis=IntSlider(1, 1, 27, 1))}

\slides{
\startanimation{olympic_val_BLM_polynomial_number}{1}{26}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number001}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number002}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number003}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number004}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number005}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number006}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number007}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number008}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number009}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number010}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number011}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number012}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number013}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number014}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number015}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number016}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number017}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number018}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number019}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number020}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number021}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number022}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number023}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number024}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number025}}{olympic_val_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number026}}{olympic_val_BLM_polynomial_number}
\endanimation
}

\notesfigure{\includediagram{../slides/diagrams/ml/olympic_val_BLM_polynomial_number026}}{}
\notes{\caption{Bayesian fit with 26th degree polynomial and hold out validation scores.}}

\subsection{5-fold Cross Validation}

\notes{Five fold cross validation tests the ability of the model to *interpolate*.}

\plotcode{num_parts=5
plot.cv_fit(x, y, param_name='number', param_range=(1, 27),  
            diagrams='../slides/diagrams/ml',
            model=mlai.BLM, 
            basis=basis, 
            alpha=1, 
            sigma2=0.04, 
            xlim=data_limits, 
            objective_ylim=[0.2,0.6], 
            num_parts=num_parts)}

\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_5cv{part:0>2}_BLM_polynomial_number{num_basis:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							part=(0, 5), 
							num_basis=IntSlider(1, 1, 27, 1))}



\slides{
\startanimation{olympic_5cv05_BLM_polynomial_number}{1}{26}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number001}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number002}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number003}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number004}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number005}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number006}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number007}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number008}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number009}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number010}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number011}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number012}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number013}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number014}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number015}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number016}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number017}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number018}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number019}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number020}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number021}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number022}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number023}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number024}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number025}}{olympic_5cv05_BLM_polynomial_number}
\newframe{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number026}}{olympic_5cv05_BLM_polynomial_number}
\endanimation
}

\notesfigure{\includediagram{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number026}}{}
\notes{\caption{Bayesian fit with 26th degree polynomial and five fold cross validation scores.}}

\endif
