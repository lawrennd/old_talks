\ifndef{osuRun1Data}
\define{osuRun1Data}

\editme

\subsection{OSU Motion Capture Data: Run 1}

\notes{Motion capture data the Open Motion Data Project by The Ohio State University Advanced Computing Center for the Arts and Design, http://accad.osu.edu/research/mocap/mocap_data.htm.}

\setupcode{import pods}

\notes{You can download any subject and motion from the data set. Here we will download motion `01` from subject `35`.}

\code{data = pods.datasets.osu_run1()}

\notes{The data dictionary contains the keys 'Y' and 'connect', which represent the data and connections that can be used to create the skeleton.}

\code{data['Y'].shape}

\notes{The data has often been used in talks demonstrating GP-LVM models and comparing variants such as back constrained and temporal models.}

\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys under `details`.}


\code{print(data['details'])}

\endif

