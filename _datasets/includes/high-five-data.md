\ifndef{highFiveData}
\define{highFiveData}

\editme

\subsection{'High Five' Motion Capture Data}

\slides{* ‘High five’ data.
* From CMU Mocap Database [@CMU-mocap03].
* Model learns structure between two interacting subjects.}

\notes{Motion capture data from the CMU motion capture data base [@CMU-mocap03]. It contains two subjects approaching each other and executing a 'high five'. The subjects are number 10 and 11 and their motion numbers are 21.}

\setupcode{import pods}

\code{data = pods.datasets.cmu_mocap_high_five()}

\notes{The data dictionary contains the keys 'Y1' and 'Y2', which represent the motions of the two different subjects. Their skeleton files are included in the keys 'skel1' and 'skel2'.}

\code{data['Y1'].shape
data['Y2'].shape}

\notes{The data was used in the hierarchical GP-LVM paper [@Lawrence:hgplvm07] in an experiment that was also recreated in the Deep Gaussian process paper [@Damianou:deepgp13].}

\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys `info` and `details`.}


\code{print(data['info'])
print()
print(data['details'])}

\endif

