\ifndef{robotWirelessData}
\define{robotWirelessData}
\editme

\subsection{Robot Wireless Data}

\notes{The robot wireless data is taken from an experiment run by Brian Ferris at University of Washington. It consists of the measurements of WiFi access point signal strengths as Brian walked in a loop. It was published at IJCAI in 2007 [@Ferris:wifi07].}

\setupcode{import pods
import numpy as np}

\code{data=pods.datasets.robot_wireless()}

\notes{The ground truth is recorded in the data, the actual loop is given in the plot below.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
plt.plot(data['X'][:, 1], data['X'][:, 2], 'r.', markersize=5)
ax.set_xlabel('x position', fontsize=20)
ax.set_ylabel('y position', fontsize=20)
mlai.write_figure(figure=fig, 
                  filename='robot-wireless-ground-truth.svg',
                  directory='\writeDiagramsDir/datasets')}

\notes{\subsection{Robot Wireless Ground Truth}}

\figure{\includediagram{\diagramsDir/datasets/robot-wireless-ground-truth}{60%}}{Ground truth movement for the position taken while recording the multivariate time-course of wireless access point signal strengths.}{robot-wireless-ground-truth}

\notes{We will ignore this ground truth in making our predictions, but see if the model can recover something similar in one of the latent layers.}

\plotcode{output_dim=1
xlim = (-0.3, 1.3)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(np.linspace(0,1,215),
            data['Y'][:, output_dim], 
            'r.', markersize=5)

ax.set_xlabel('time', fontsize=20)
ax.set_ylabel('signal strength', fontsize=20)
xlim = (-0.2, 1.2)
ylim = (-0.6, 2.0)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

ma.write_figure(figure=fig, 
                filename='robot-wireless-dim-' + str(output_dim) + '.svg', 
                directory='\writeDiagramsDir/datasets')}


\subsection{Robot WiFi Data}

\notes{One challenge with the data is that the signal strength 'drops out'. This is because the device only tracks a limited number of wifi access points, when one of the access points falls outside the track, the value disappears (in the plot below it reads -0.5). The data is missing, but it is not missing at random because the implication is that the wireless access point must be weak to have dropped from the list of those that are tracked.}

\figure{\includediagram{\diagramsDir/datasets/robot-wireless-dim-1}{60%}}{Output dimension 1 from the robot wireless data. This plot shows signal strength changing over time.}{robot-wireless-data-dim-1}

\endif
