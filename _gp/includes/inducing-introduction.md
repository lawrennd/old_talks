\ifndef{inducingIntroduction}
\define{inducingIntroduction}
\editme

\newslide{Introducing $\inducingVector$}

Take an extra $\numInducing$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$

\newslide{Introducing $\inducingVector$}

\includeimg{../slides/diagrams/cov_inducing_withX.png}{60%}{negate}

\newslide{Introducing $\inducingVector$}

Take and extra $M$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$
$$\begin{aligned}
    p(\dataVector\given\mappingFunctionVector) &= \gaussianDist{\dataVector}{\mappingFunctionVector}{\dataStd^2 \eye}\\
    p(\mappingFunctionVector\given\inducingVector) &= \gaussianDist{\mappingFunctionVector}{ \Kfu\Kuu^{-1}\inducingVector}{ \tilde{\kernelMatrix}}\\
    p(\inducingVector) &= \gaussianDist{\inducingVector}{ \zerosVector}{\Kuu}
  \end{aligned}$$


\newslide{}

\columns{
$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$
}{
\includeimg{../slides/diagrams/nomenclature4}{90%}{negate}
}{30%}{70%}
$$
\begin{align}
                           &\qquad\inducingInputMatrix, \inducingVector\\                      &p({\color{red} \inducingVector})  = \gaussianSamp{\zerosVector}{\Kuu}\end{align}
$$

\newslide{}

\columns{
$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$ $$p(\inducingVector)  = \gaussianSamp{\zerosVector}{\Kuu}$$ $$\widetilde p({\color{red}\inducingVector}\given \dataVector,\inputMatrix)$$
}{
\includeimg{../slides/diagrams/nomenclature5.png}{90%}{negate}
}{30%}{70%}
