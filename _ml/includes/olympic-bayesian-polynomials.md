### Olympic Data with Bayesian Polynomials

\notes{Five fold cross validation tests the ability of the model to *interpolate*.}

\slides{
\setupcode{import mlai
import pods}

\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']
num_data = x.shape[0]

data_limits = [1892, 2020]
basis = mlai.basis(mlai.polynomial, number=1, data_limits=data_limits)

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
}

\slides{
\startslides{olympic_BLM_polynomial_number}{1}{26}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number001.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number002.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number003.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number004.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number005.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number006.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number007.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number008.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number009.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number010.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number011.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number012.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number013.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number014.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number015.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number016.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number017.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number018.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number019.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number020.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number021.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number022.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number023.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number024.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number025.svg}{}{olympic_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number026.svg}{}{olympic_BLM_polynomial_number}
}

\notesfigure{\includesvg{../slides/diagrams/ml/olympic_BLM_polynomial_number026.svg}{}{}}
\notes{\caption{Bayesian fit with 26th degree polynomial and negative marginal log likelihood.}}


### Hold Out Validation

\notes{For the polynomial fit, we will now look at *hold out* validation, where we are holding out some of the most recent points. This tests the abilit of our model to *extrapolate*.}

\slides{
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
}

\slides{
\startslides{olympic_val_BLM_polynomial_number}{1}{26}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number001.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number002.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number003.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number004.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number005.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number006.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number007.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number008.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number009.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number010.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number011.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number012.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number013.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number014.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number015.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number016.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number017.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number018.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number019.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number020.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number021.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number022.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number023.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number024.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number025.svg}{}{olympic_val_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number026.svg}{}{olympic_val_BLM_polynomial_number}
}

\notesfigure{\includesvg{../slides/diagrams/ml/olympic_val_BLM_polynomial_number026.svg}{}{}}
\notes{\caption{Bayesian fit with 26th degree polynomial and hold out validation scores.}}

### 5-fold Cross Validation

\notes{Five fold cross validation tests the ability of the model to *interpolate*.}

\slides{
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

}

\slides{
\startslides{olympic_5cv05_BLM_polynomial_number}{1}{26}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number001.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number002.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number003.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number004.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number005.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number006.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number007.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number008.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number009.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number010.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number011.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number012.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number013.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number014.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number015.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number016.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number017.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number018.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number019.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number020.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number021.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number022.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number023.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number024.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number025.svg}{}{olympic_5cv05_BLM_polynomial_number}
\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number026.svg}{}{olympic_5cv05_BLM_polynomial_number}
}

\notesfigure{\includesvg{../slides/diagrams/ml/olympic_5cv05_BLM_polynomial_number026.svg}{}{}}
\notes{\caption{Bayesian fit with 26th degree polynomial and five fold cross validation scores.}}
