\ifndef{deepFace}
\define{deepFace}
\editme

\subsection{DeepFace}

\slides{\fragment{\smalltext{Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected.}}{fade-in}}

\figure{\includepng{\diagramsDir/deepface_neg}{100%}}{The DeepFace architecture [@Taigman:deepface14], visualized through colors to represent the functional mappings at each layer. There are 120 million parameters in the model.}{deep-face}

\slides{\alignright{\smalltext{Source: DeepFace [@Taigman:deepface14]}}}

\notes{The DeepFace architecture [@Taigman:deepface14] consists of layers that deal  with *translation* and *rotational* invariances. These layers are followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The neural network includes more than 120 million parameters, where more than 95% come from the local and fully connected layers.}


\endif
