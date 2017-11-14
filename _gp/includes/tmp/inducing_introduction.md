<!--frame start-->
### Introducing $\inducingVector$

Take an extra $\numInducing$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$

<!--frame end-->
<!--frame start-->
### Introducing $\inducingVector$ {#introducing-inducingvector}

\centering![image](../../../gp/tex/diagrams/cov_inducing_withX){height="0.6\textheight"}

<!--frame end-->
<!--frame start-->
### Introducing $\inducingVector$ {#introducing-inducingvector}

Take and extra $M$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$
$$\begin{aligned}
    p(\dataVector\given\mappingFunctionVector) &= \gaussianDist{\dataVector}{\mappingFunctionVector}{\dataStd^2 \eye}\\
    p(\mappingFunctionVector\given\inducingVector) &= \gaussianDist{\mappingFunctionVector}{ \Kfu\Kuu^{-1}\inducingVector}{ \Ktilde}\\
    p(\inducingVector) &= \gaussianDist{\inducingVector}{ \zerosVector}{\Kuu}
  \end{aligned}$$

<!--frame end-->
<!--frame start-->
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------- --
   [\semitransp $$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$ ]{} $$\begin{split}   \raisebox{-.9\height}{\includegraphics[width=\textwidth]{../../../gp/tex/diagrams/nomenclature4}}  
                                                                                                           &\qquad\inducingInputMatrix, \inducingVector\\                                                                                                                                                                                                    
                                                                                               &p({\color{red} \inducingVector})  = \gaussianSamp{\zerosVector}{\Kuu}                                                                                                                                                                                        
                                                                                                                          \end{split}$$                                                                                                                                                                                                                      
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------- --

<!--frame end-->
<!--frame start-->
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------- --
   [\semitransp $$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$ $$p(\inducingVector)  = \gaussianSamp{\zerosVector}{\Kuu}$$ ]{} $$\widetilde p({\color{red}\inducingVector}\given \dataVector,\inputMatrix)$$   \raisebox{-.9\height}{\includegraphics[width=\textwidth]{../../../gp/tex/diagrams/nomenclature5}}  
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------- --

<!--frame end-->

