\ifndef{inducingNotation}
\define{inducingNotation}
\editme

\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$}{\includepng{\diagramsDir/nomenclature1}{90%}{negate}}{30%}{70%}


\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$  $${\color{\blueColor} \mappingFunction(\inputVector)} \sim {\mathcal GP}$$}{\includepng{\diagramsDir/nomenclature2}{90%}{negate}}{30%}{70%}

\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$$$p({\color{\blueColor} \mappingFunctionVector}) = \gaussianSamp{\zerosVector}{\Kff}$$}{\includepng{\diagramsDir/nomenclature3}{90%}{negate}
}{30%}{70%}

\newslide{}

\columns{
$$
\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}
$$ 
$$
p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}
$$
$$p( \mappingFunctionVector \given \dataVector,\inputMatrix)
$$}{\includepng{\diagramsDir/nomenclature3a}{90%}{negate}}{30%}{70%}

\endif
