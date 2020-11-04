\ifndef{catapultSimulation}
\define{catapultSimulation}

\editme

\subsection{Catapult Simulation}

\nicolasDurrandePicture{15%}

\notes{As a worked example we're going to introduce a catapult simulation written by Nicolas Durrande, <https://durrande.shinyapps.io/catapult/>.}

\figure{\includepng{\diagramsDir/uq/catapult-simulation}{80%}}{A catapult simulation for experimenting with surrogate models, kindly provided by Nicolas Durrande}{catapult-simulation}

\notes{The simulator allows you to set various parameters of the catapult including the axis of rotation, `roation_axis`, the position of the arm stop, `arm_stop`, and the location of the two bindings of the catapult's spring, `spring_binding_1` and `spring_binding_2`.}


\notes{These parameters are then collated in a vector,}
$$\inputVector_i = \begin{bmatrix}
\texttt{rotation_axis} \\
\texttt{arm_stop} \\
\texttt{spring_binding_1} \\
\texttt{spring_binding_2}
\end{bmatrix}
$$

\notes{Having set those parameters, you can run an experiment, by firing the catapult. This will show you how far it goes.}

\notes{To feed the model with the value of the catapult simulation we will use the following function.}

\setuphelpercode{import numpy as np}

\helpercode{def catapult_distance(x):
    """Request user input for the catapult."""
    y = np.zeros((x.shape[0], 1))
    for i in range(x.shape[0]):
        rotation_axis=x[i, 0]
        arm_stop=x[i, 1]
        spring_binding_1=x[i, 2]
        spring_binding_2=x[i, 3]
            
        print('Please set the following values:')
        print('x_1 = {rotation_axis:.2f} (rotation axis)'.format(rotation_axis=rotation_axis))
        print('x_2 = {arm_stop:.2f} (arm stop)'.format(arm_stop=arm_stop))
        print('x_3 = {spring_binding_1:.2f} (spring binding 1)'.format(spring_binding_1=spring_binding_1))
        print('x_4 = {spring_binding_2:.2f} (spring binding 2)'.format(spring_binding_2=spring_binding_2))
        y[i, 0] = float(input('What is the distance? '))
    return y}

\endif
