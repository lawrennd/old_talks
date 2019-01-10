\ifndef{inducingNotation}
\define{inducingNotation}
\editme

\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$}{\includepng{../slides/diagrams/nomenclature1}{90%}{negate}}


\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$  $${\color{\blueColor} \mappingFunction(\inputVector)} \sim {\mathcal GP}$$}{\includepng{../slides/diagrams/nomenclature2}{90%}{negate}}

\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$$$p({\color{\blueColor} \mappingFunctionVector}) = \gaussianSamp{\zerosVector}{\Kff}$$}{\includepng{../slides/diagrams/nomenclature3}{90%}{negate}
}

\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$  $$p( \mappingFunctionVector \given \dataVector,\inputMatrix)$$}{\includepng{../slides/diagrams/nomenclature3a}{90%}{negate}}

\endif
