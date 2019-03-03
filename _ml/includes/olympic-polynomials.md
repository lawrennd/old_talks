\ifndef{olympicPolynomial}
\define{olympicPolynomial}

\include{_ml/includes/olympic-data.md}

\editme

\subsection{Polynomial Fits to Olympic Data}

\setupcode{import numpy as np
from matplotlib import pyplot as plt
import mlai
import pods}

\code{basis = mlai.polynomial

data = pods.datasets.olympic_marathon_men()

x = data['X']
y = data['Y']

xlim = [1892, 2020]


basis=mlai.Basis(mlai.polynomial, number=1, data_limits=xlim)}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.rmse_fit(x, y, param_name='number', param_range=(1, 27), 
              model=mlai.LM, 
			  basis=basis,
              xlim=xlim, objective_ylim=[0, 0.8],
              diagrams='../slides/diagrams/ml')}

\setupdisplaycode{from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_LM_polynomial_num_basis{num_basis:0>3}.svg',
                            directory='../slides/diagrams/ml', 
                            num_basis=IntSlider(1,1,27,1))}


\slides{
\define{width}{80%}
\startanimation{olympic_LM_polynomial_num_basis}{1}{26}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis001}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis002}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis003}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis004}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis005}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis006}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis007}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis008}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis009}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis010}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis011}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis012}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis013}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis014}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis015}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis016}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis017}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis018}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis019}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis020}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis021}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis022}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis023}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis024}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis025}{\width}}{olympic_LM_polynomial_num_basis}
\newframe{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis026}{\width}}{olympic_LM_polynomial_num_basis}
\endanimation
}

\notes{\figure{\includediagram{../slides/diagrams/ml/olympic_LM_polynomial_num_basis026}{80%}}{Fit of a 26 degree polynomial to the olympic marathon data.}{olympic-lm-polynomial-num-basis-26}}


\endif
