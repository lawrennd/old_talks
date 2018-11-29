\subsection{Polynomial Fits to Olympic Data}

\setupcode{import numpy as np
from matplotlib import pyplot as plt
import teaching_plots as plot
import mlai
import pods}

\code{basis = mlai.polynomial

data = pods.datasets.olympic_marathon_men()

x = data['X']
y = data['Y']

xlim = [1892, 2020]


basis=mlai.Basis(mlai.polynomial, number=1, data_limits=xlim)}

\plotcode{plot.rmse_fit(x, y, param_name='number', param_range=(1, 27), 
              model=mlai.LM, 
			  basis=basis,
              xlim=xlim, objective_ylim=[0, 0.8],
              diagrams='../slides/diagrams/ml')}

\setupcode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_LM_polynomial_num_basis{num_basis:0>3}.svg',
                            directory='../slides/diagrams/ml', 
                            num_basis=IntSlider(1,1,27,1))}


\slides{
\startanimation{olympic_LM_polynomial_num_basis}{1}{26}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis001.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis002.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis003.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis004.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis005.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis006.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis007.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis008.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis009.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis010.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis011.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis012.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis013.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis014.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis015.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis016.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis017.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis018.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis019.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis020.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis021.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis022.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis023.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis024.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis025.svg}}{olympic_LM_polynomial_num_basis}
\newframe{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis026.svg}}{olympic_LM_polynomial_num_basis}
\endanimation
}

\notesfigure{\includesvg{../slides/diagrams/ml/olympic_LM_polynomial_num_basis026.svg}{}{}}


