### Introducing $\inducingVector$ {data-transition="None"}

Take an extra $\numInducing$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$

### Introducing $\inducingVector$ {#introducing-inducingvector data-transition="None"}

\includeimg{../slides/diagrams/cov_inducing_withX.png}{60%}{negate}

### Introducing $\inducingVector$ {#introducing-inducingvector data-transition="None"}

Take and extra $M$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$
$$\begin{aligned}
    p(\dataVector\given\mappingFunctionVector) &= \gaussianDist{\dataVector}{\mappingFunctionVector}{\dataStd^2 \eye}\\
    p(\mappingFunctionVector\given\inducingVector) &= \gaussianDist{\mappingFunctionVector}{ \Kfu\Kuu^{-1}\inducingVector}{ \tilde{\kernelMatrix}}\\
    p(\inducingVector) &= \gaussianDist{\inducingVector}{ \zerosVector}{\Kuu}
  \end{aligned}$$


###  {data-transition="None"}

\columns{
$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$
}{
\includeimg{../slides/diagrams/nomenclature4}{90%}{negate}
}
\begin{align}
                                                                                                           &\qquad\inducingInputMatrix, \inducingVector\\                                                                                                                                                                                                    
                                                                                               &p({\color{red} \inducingVector})  = \gaussianSamp{\zerosVector}{\Kuu}                                                                                                                                                                                        
                                                                                                                          \end{align}$$  

###  {data-transition="None"}

\columns{
$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$ $$p(\inducingVector)  = \gaussianSamp{\zerosVector}{\Kuu}$$ $$\widetilde p({\color{red}\inducingVector}\given \dataVector,\inputMatrix)$$
}{
\includeimg{../slides/diagrams/nomenclature5.png}{90%}{negate}
}
