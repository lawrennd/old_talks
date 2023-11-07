\ifndef{cmuMocapData}
\define{cmuMocapData}

\editme

\subsection{CMU Mocap Database}

\notes{Motion capture data from the CMU motion capture data base [@CMU-mocap03].}

\setupcode{import pods}

\notes{You can download any subject and motion from the data set. Here we will download motion `01` from subject `35`.}

\code{subject='35' 
motion=['01']}

\code{data = pods.datasets.cmu_mocap(subject, motion)}

\notes{The data dictionary contains the keys 'Y' and 'skel', which represent the data and the skeleton..}

\code{data['Y'].shape}

\notes{The data was used in the hierarchical GP-LVM paper [@Lawrence:hgplvm07] in an experiment that was also recreated in the Deep Gaussian process paper [@Damianou:deepgp13].}

\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys `info` and `details`.}


\code{print(data['info'])
print()
print(data['details'])}

\endif

