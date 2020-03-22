\ifndef{olympicMarathonPolynomial}
\define{olympicMarathonPolynomial}

\editme

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
max_basis = 27

ll = np.array([np.nan]*(max_basis))
sum_squares = np.array([np.nan]*(max_basis))
basis=mlai.Basis(mlai.polynomial, number=1, data_limits=xlim)}

\code{plot.rmse_fit(x, y, param_name='number', param_range=(1, 28), 
              model=mlai.LM, basis=basis, 
              xlim=xlim, objective_ylim=[0, 0.8],
              diagrams='../slides/diagrams/ml')}

\displaysetupcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('olympic_LM_polynomial_number{num_basis:0>3}.svg',
                            directory='../slides/diagrams/ml', 
                            num_basis=IntSlider(1,1,28,1))}
                            
\endif
